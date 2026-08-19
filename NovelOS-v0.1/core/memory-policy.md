# NovelOS Memory Policy v0.1

## Principle
Store what future work genuinely needs. Do not model what the model can already understand from local context.

## Four Primary Memory Types

### 1. FACT
Reliable, atomic story facts required for continuity.
Examples: identity, chronology, location, possession, knowledge boundary, confirmed event.

### 2. SUMMARY
Compact account of what happened in a chapter, scene, discussion, or decision.
Used for long-range retrieval, not as a replacement for the original text.

### 3. KEY_PASSAGE
Original text worth preserving because its value may be lost by summarization.
Reasons may include: emotional subtext, character voice, relationship texture, atmosphere, motif, unresolved meaning.
Default: do not rewrite automatically.

### 4. CREATIVE_HISTORY
Ideas, discussion notes, rejected/parked possibilities, unresolved questions, and decisions explaining how the work developed.
This records the history of the work, not a psychological profile of the author.

## Authority
Suggested order of authority:
1. explicit author lock
2. current canon/bible
3. approved prose
4. approved design decision
5. discussion proposal
6. model hypothesis

Lower authority must not overwrite higher authority silently.

## Canonization
Discussion content begins UNCONFIRMED. Promotion to canon requires explicit author confirmation or a clearly authorized production decision.

## Contradictions
When new material conflicts with canon, store the conflict and route it to Continuity/Director. Do not silently choose the newest fact.

## Retrieval
Retrieve by task need. Prefer:
- relevant canon
- current character/location/knowledge state
- recent summaries
- directly related prior events
- active unresolved questions/foreshadowing
- relevant key passages
- semantic matches

Do not flood context with all memory.

## Literary Restraint
Do not summarize away a passage whose force seems to depend on wording, rhythm, silence, or ambiguity. Preserve the original as KEY_PASSAGE.

## Unknowns
Unknown, disputed, ambiguous, and intentionally unresolved states are first-class memory values.
