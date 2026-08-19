# Ruflo Adapter Boundary — Build 001

## Why an Adapter
NovelOS keeps fiction-domain rules stable while Ruflo supplies orchestration, MCP, hooks, memory, and swarm/runtime capabilities. Ruflo evolves quickly, so NovelOS should not encode its literary logic into Ruflo's internal directory layout.

## Current Ruflo Surface to Map
Based on the current upstream README, the full CLI path (`npx ruflo@latest init` / `init wizard`) supplies the full loop including agents, skills, MCP server, hooks, daemon, memory, and swarm coordination.

## Planned Mapping

NovelOS concept -> Ruflo surface

- agents/*.md -> agent definitions / prompts
- skills/*/SKILL.md -> Ruflo/Claude-compatible skills where practical
- memory policy -> AgentDB / RAG memory namespaces via adapter
- mode router -> pre-task hook/router
- memory commit -> post-task hook
- context retrieval -> memory/RAG calls before Writer/Planner
- targeted revision -> workflow/swarm routing

## Adapter Rules
1. NovelOS Constitution remains source of truth.
2. Ruflo self-learning must not directly rewrite Constitution or canon.
3. Discussion mode must block production agents.
4. Memory writes must preserve authority and status.
5. Semantic retrieval must not override canon.
6. Agent count should remain small unless a task genuinely benefits from more agents.

## Next Implementation Step
Create a local Ruflo-initialized workspace and map one end-to-end Story Room flow before mapping chapter production.
