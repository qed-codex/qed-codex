---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Aggregating the actual collision streams of all vertex pairs

The fixed program consumes framed pairs of already selected read plans.
Producing those selected plans from original plans and the remaining-index
table is a separate preparation step.  Every pair invokes the actual tuple
generator and collision machine; a final fixed unary tally produces the score.


### `pairBytes`

 Public pair-record payload: exactly two consecutive escape frames, each
containing the selected plan's ordinary unary-index record encoding. 

### `pairRecords`

 Runtime list framing around the public pair payloads. 

### `baseState`

 Persistent ports are current 13, width 3, alphabet 19, depth template 23.
Stream 11 accumulates leaves; stack 18 is reserved for the final unary score. 

### `generate_eval`

 The actual generator is lifted into the aggregate scorer. Only the
separate parser/depth-template ports lie outside its footprint. 

### `program_run`

 One fixed record iterator executes every pair's real generator/collision
program, then tallies its complete concatenated stream. 

### `allPairPlans`

 Any runtime mapping of the full ordered vertex-pair list has D squared
records, including maps whose selected plans depend on both vertices. 

### `streamedPairs_length_allPairs`

 The exact D squared times N squared leaf count is derived from the actual
pair list and generated tuple depth. 
