# Large-project scanning and retrieval

Read this during Phase 1 when the size preflight selects `knowledge_graph`. Apply the same process independently to a baseline if provided. The goal is to reduce context in the paper pipeline; initial graph construction still costs time and tokens.

## 1. Inventory before source analysis

Run the bundled helper by absolute path, substituting the resolved paths:

```bash
python3 <plugin-root>/agent-workspace/scan_inventory.py <project-path> --output-dir <run-root>/agent-workspace/analysis/target
```

Use `analysis/base` for a baseline. Read only `scan-summary.json` initially; do not dump `file-inventory.jsonl` into context. The helper respects Git ignore rules in a Git worktree, excludes dependencies, build outputs, generated graph/workspace directories, binary files and symlinks, and streams file contents locally to count lines without placing them in model context. Outside Git, default exclusions apply; record additional project-specific exclusions and rerun with `--exclude NAME` as needed. Review `unreadable_files` and `excluded_symlinks`; do not silently describe those files as analyzed.

Default policy: select `knowledge_graph` if **any** of these holds: at least 1,000 text/source files, 100,000 lines, or 1,000,000 estimated tokens (text bytes / 4, a rough sizing heuristic). This is a configurable project2paper policy, not a model context limit. The helper accepts `--file-threshold`, `--line-threshold`, and `--token-threshold` overrides. Also switch to graph mode below those thresholds if the anticipated analysis exceeds the current context budget. Record the actual decision and reason in `project-map.json.scan_strategy`.

## 2. Reuse or build a graph

Prefer a compatible installed graph skill/tool such as [Understand Anything](https://github.com/Egonex-AI/Understand-Anything). Discover the tool and read its installed instructions before using it; do not invent an executable or assume a plugin is installed. Understand Anything currently exposes `$understand` on Codex and `/understand` on Claude Code. Its current default graph is `<project>/.ua/knowledge-graph.json`; older projects may use `.understand-anything/knowledge-graph.json`. These are skill invocations in the host, not shell commands. Other graph tools may use different paths and schemas.

1. Check for an existing graph and its metadata. Verify the repository/root, revision, working-tree changes, generation time, and included scope. A matching HEAD alone does not establish freshness when files are dirty or untracked. Update changed modules incrementally when supported. Record unresolved freshness or coverage gaps; an unverified/stale graph is a navigation hint only.
2. If no usable graph exists, invoke the available graph skill against the resolved target path. Use bounded module batches; save graph artifacts to disk and return compact summaries between batches. Follow the tool's own instructions. Prefer an incremental update over rebuilding the whole project. Do not install plugins automatically as part of a scan.
3. If the tool is unavailable or fails, build a **local module index** in `analysis/knowledge/target/` (or `base/`) from the inventory, manifests, imports, entry points, and bounded source reads. Write one module summary per file plus an `index.json` containing module IDs, summary paths, source paths, and dependency edges. Record `provider: "local-module-index"`, inferred edges, incomplete coverage, and the tool failure/unavailability reason. Do not claim this is an Understand Anything graph or that a whole-program graph was produced.
4. Save a compact `analysis/context-index.json` with separate `target` and optional `base` records: provider, absolute graph/index path, project root, revision (or null outside Git), dirty state, generated time, coverage/exclusions, freshness status, and limitations. Keep external tool schemas intact and reference their paths instead of copying a full graph into project-map.json. Include an overview and module-summary lookup paths so later phases can retrieve without loading the whole graph.

## 3. Context handoff and evidence

Keep `project-map.json` compact: aggregate counts, languages/frameworks, entry points, module overview, dependency summaries, and a `scan_strategy` record such as:

```json
{
  "mode": "knowledge_graph",
  "reason": "line threshold exceeded",
  "inventory_path": "analysis/target/file-inventory.jsonl",
  "summary_path": "analysis/target/scan-summary.json",
  "context_index_path": "analysis/context-index.json",
  "provider": "understand-anything",
  "limitations": []
}
```

Paths in this record are relative to the generated `agent-workspace/` unless explicitly absolute. Write actual values, including `mode: "module_index"` for fallback or `"direct"` for a small project. Even direct mode retains inventory and summary paths. For large baseline comparisons, store complete added/changed/removed path lists in a separate artifact and give `base_comparison` counts, a bounded preview, selected contribution areas, and that artifact's path. Compare actual contents/hashes, not file sizes alone.

For **Phases 2–5**, start from project-map + context-index + a compact overview. Select the relevant module/subgraph (normally one dependency hop), read only its summary and specific source excerpts, and persist new evidence before moving to the next module/chapter. Use JSON filtering or the provider's query tools to retrieve from a large graph; never read the full graph JSON or inventory into context. Record source paths, symbols/line ranges, and revision with every material claim. A graph is a retrieval aid, not proof of novelty, runtime behavior, or performance. Verify claims against current source, tests, measurements, and literature; mark missing evidence as a limitation or placeholder. Phase 5 must recheck the source behind claims even if graph summaries appear to support them.
