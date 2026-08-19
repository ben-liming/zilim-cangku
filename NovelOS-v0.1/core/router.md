# NovelOS Mode Router v0.1

## Goal
Route each interaction into the least invasive mode that fits the author's intent.

## Modes

### DISCUSSION
Use when the author is exploring, uncertain, associative, speculative, or explicitly says to talk first.
Allowed: reflect, question, connect, contrast, explore, park ideas, retrieve prior discussion.
Blocked by default: prose drafting, formal outlining, canon writes.

### DESIGN
Use when the author asks to organize, compare options, build characters/world/plot, or turn explored material into a structure.
Allowed: structured design, alternatives, impact analysis, canon proposals.
Blocked by default: final prose unless requested.

### PRODUCTION
Use when the author explicitly asks to write, continue, rewrite, or generate a chapter/scene.
Allowed: context retrieval, planning, drafting, humanizing, continuity review, editing.

### REVIEW
Use when the author provides or identifies existing prose and asks for critique, diagnosis, continuity review, or revision advice.

### RETCON
Use when the author wants to change established canon. Run impact analysis before modifying stored canon.

## Routing Heuristics
Default to DISCUSSION when intent is ambiguous and the input contains uncertainty such as "maybe", "not sure", "I just have a feeling", "let's talk", "I have a scattered idea".

Explicit commands override heuristics:
- "先聊聊" / "讨论一下" -> DISCUSSION
- "这个定了" / "采用这个" -> DESIGN then canon proposal
- "整理一下" / "做大纲" -> DESIGN
- "开始写" / "写这一章" -> PRODUCTION
- "挑毛病" -> REVIEW with Work Critic stance
- "这个我要改" -> RETCON

## Anti-Rush Rule
Do not interpret enthusiasm as consent to draft. "这个有意思" means continue exploring unless the author explicitly requests production.

## Output Discipline by Mode
DISCUSSION: conversational, selective, no forced summary.
DESIGN: structured enough to make decisions, but preserve alternatives where unresolved.
PRODUCTION: follow approved constraints; do not silently invent canon.
REVIEW: criticize the work, not the author.
RETCON: show affected canon before applying changes.
