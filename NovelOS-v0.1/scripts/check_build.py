from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "core/constitution.md",
    "core/router.md",
    "core/memory-policy.md",
    "agents/story-partner.md",
    "agents/director.md",
    "agents/planner.md",
    "agents/writer.md",
    "agents/humanizer.md",
    "agents/editor.md",
    "agents/continuity.md",
    "agents/memory-keeper.md",
    "skills/story-room/SKILL.md",
    "skills/idea-to-canon/SKILL.md",
    "skills/context-retrieval/SKILL.md",
    "skills/chapter-generation/SKILL.md",
    "novelos.config.yaml",
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("BUILD INVALID")
    for p in missing:
        print("missing:", p)
    sys.exit(1)

sample = ROOT / "projects/demo-novel/notes/discussion-001.json"
with sample.open("r", encoding="utf-8") as f:
    data = json.load(f)
assert data["mode"] == "DISCUSSION"
assert data["canon_changes"] == []
print("BUILD OK")
print(f"required_files={len(required)}")
print("discussion_mode_blocks_canon=true")
