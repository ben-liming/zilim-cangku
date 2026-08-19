# NovelOS v0.1 — Build 001

NovelOS is a long-form fiction creation system designed around four priorities:

1. discuss before writing when the work is still unclear
2. preserve long-term story memory without flattening literature into data
3. separate discovery, design, production, and review
4. keep the work—not the system or the author profile—at the center

## Current Build
Build 001 establishes the constitution, mode router, memory policy, minimal agents, and minimal skills.

## What v0.1 deliberately does NOT do yet
- no heavy aesthetic scoring
- no emotional percentages
- no giant character schema
- no automatic self-modification of prompts
- no automatic canonization from discussion
- no hard dependency on Ruflo internal directory conventions

## Ruflo integration
Ruflo is treated as the orchestration/runtime layer, while NovelOS keeps fiction-specific rules in its own files. Current Ruflo documentation describes the full CLI init path as providing agents, skills, MCP, hooks, daemon, memory and swarm capabilities; Build 001 therefore keeps an adapter boundary rather than embedding unstable runtime internals directly.

Suggested Ruflo setup for future adapter work:

```bash
npx ruflo@latest init wizard
```

or:

```bash
npx ruflo@latest init
```

## Next Build
Build 002 should add:
- a small working memory store format
- discussion-session capture
- idea/decision records
- context-pack builder
- one demo Story Room session
- Ruflo adapter notes/hooks mapping

## Design Rule
If a new feature makes the system more impressive but the work worse, remove the feature.
