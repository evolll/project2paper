import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PluginPackagingTests(unittest.TestCase):
    def test_marketplace_resolves_complete_plugin_in_installed_location(self):
        with tempfile.TemporaryDirectory() as directory:
            installed = Path(directory) / "cache/project2paper/0.4.0"
            shutil.copytree(ROOT, installed, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            marketplace = json.loads((installed / ".agents/plugins/marketplace.json").read_text())
            plugin_entry, = marketplace["plugins"]
            plugin_root = (installed / plugin_entry["source"]["path"]).resolve()
            manifest = json.loads((plugin_root / ".codex-plugin/plugin.json").read_text())
            self.assertEqual(plugin_entry["name"], manifest["name"])
            self.assertEqual(manifest["version"], json.loads(
                (plugin_root / ".claude-plugin/plugin.json").read_text())["version"])
            skill_dir = plugin_root / manifest["skills"] / "project2paper"
            self.assertTrue((skill_dir / "SKILL.md").is_file())
            # The canonical skill finds bundled resources from its own location.
            resolved_root = (skill_dir / "../..").resolve()
            self.assertEqual(resolved_root, plugin_root)
            for name in ("project-scanner", "research-extractor", "project-analyzer",
                         "paper-writer", "paper-reviewer"):
                self.assertTrue((resolved_root / "agents" / f"{name}.md").is_file())
            self.assertTrue((resolved_root / "agent-workspace/scan_inventory.py").is_file())
            self.assertTrue((skill_dir / "references/large-projects.md").is_file())
            self.assertTrue((skill_dir / "agents/openai.yaml").is_file())
            linked_skill = Path(directory) / "personal-skills/project2paper"
            linked_skill.parent.mkdir()
            linked_skill.symlink_to(skill_dir)
            self.assertEqual((linked_skill.resolve() / "../..").resolve(), plugin_root)


if __name__ == "__main__":
    unittest.main()
