import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "scan_inventory", ROOT / "agent-workspace/scan_inventory.py")
scanner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scanner)


class ScanInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()
        self.output = self.root / "scan-results"

    def write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def test_inventory_counts_without_source_bodies_or_generated_data(self):
        self.write("src/main.py", b"secret_source_body\nlast_line")
        self.write("empty.py", b"")
        self.write("image.bin", b"\0not text")
        for excluded in ("node_modules", ".git", "dist", "agent-workspace/analysis", ".ua"):
            self.write(f"{excluded}/ignored.py", b"ignored\n")
        (self.root / "link.py").symlink_to(self.root / "src/main.py")
        # Outputs under the target must not count themselves, including on rerun.
        first = scanner.scan_project(self.root, self.output)
        second = scanner.scan_project(self.root, self.output)
        self.assertEqual(first, second)
        self.assertEqual(first["total_files"], 2)
        self.assertEqual(first["total_lines"], 2)
        self.assertEqual(first["text_bytes"], 28)
        self.assertEqual(first["estimated_tokens"], 7)
        self.assertEqual(first["binary_files"], 1)
        self.assertEqual(first["excluded_symlinks"], 1)
        inventory = (self.output / "file-inventory.jsonl").read_text()
        self.assertNotIn("secret_source_body", inventory)
        self.assertEqual({json.loads(line)["path"] for line in inventory.splitlines()},
                         {"src/main.py", "empty.py"})

    def test_each_threshold_selects_graph_at_boundary(self):
        self.write("main.py", b"one\ntwo\n")
        for kwargs, reason in (({"file_threshold": 1}, "files"),
                               ({"line_threshold": 2}, "lines"),
                               ({"token_threshold": 2}, "estimated_tokens")):
            with self.subTest(reason=reason):
                result = scanner.scan_project(self.root, self.output, **kwargs)
                self.assertEqual(result["scan_strategy"], "knowledge_graph")
                self.assertIn(reason, result["thresholds_exceeded"])
        result = scanner.scan_project(self.root, self.output)
        self.assertEqual(result["scan_strategy"], "direct")

    @unittest.skipUnless(shutil.which("git"), "Git not installed")
    def test_git_ignores_and_subdirectory_scan(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.write(".gitignore", b"ignored/\n*.tmp\n")
        self.write("ignored/private.py", b"ignored\n")
        self.write("src/ignored.tmp", b"ignored\n")
        self.write("src/new untracked.py", b"hello\n")
        self.write("tracked.py", b"tracked\n")
        subprocess.run(["git", "-C", str(self.root), "add", "tracked.py"], check=True)
        result = scanner.scan_project(self.root, self.output)
        self.assertEqual(result["total_files"], 3)
        result = scanner.scan_project(self.root / "src", self.output)
        self.assertEqual(result["total_files"], 1)
        entry = json.loads((self.output / "file-inventory.jsonl").read_text())
        self.assertEqual(entry["path"], "new untracked.py")

    def test_extra_exclusion_and_invalid_inputs(self):
        self.write("generated/huge.txt", b"skip\n")
        result = scanner.scan_project(self.root, self.output, exclude=["generated"])
        self.assertEqual(result["total_files"], 0)
        for project, output, kwargs in (
            (self.root / "missing", self.output, {}),
            (self.root, self.output, {"file_threshold": 0}),
            (self.root, self.root, {}),
        ):
            with self.subTest(project=project, output=output, kwargs=kwargs):
                with self.assertRaises(ValueError):
                    scanner.scan_project(project, output, **kwargs)

    def test_workspace_helpers_are_source_but_generated_outputs_are_excluded(self):
        self.write("agent-workspace/helper.py", b"actual source\n")
        self.write("agent-workspace/templates/paper.md", b"template source\n")
        for generated in ("analysis", "output", "project-input"):
            self.write(f"agent-workspace/{generated}/data.txt", b"generated\n")
        result = scanner.scan_project(self.root, self.output)
        self.assertEqual(result["total_files"], 2)

    def test_cli_returns_only_pointers_and_decision(self):
        self.write("main.py", b"private implementation\n")
        result = subprocess.run(
            ["python3", str(ROOT / "agent-workspace/scan_inventory.py"), str(self.root),
             "--output-dir", str(self.output), "--file-threshold", "1"],
            capture_output=True, text=True, check=True,
        )
        message = json.loads(result.stdout)
        self.assertEqual(message["scan_strategy"], "knowledge_graph")
        self.assertTrue(Path(message["summary_path"]).is_file())
        self.assertNotIn("private implementation", result.stdout)


if __name__ == "__main__":
    unittest.main()
