---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit polynomial envelopes for the concrete native raw-hash interpreter.
S bounds the number of retained keys; B and d are actual encoded coefficient
width and extension dimension. No arithmetic or parser callback is free. 

### `entries`

 The table consists of one actual serialized incidence dictionary for each
original variable. It is the same table for every literal occurrence. 

### `clause_le`

 Fixed-width clause traversal with the actual lookup and arithmetic costs. 

### `row_le`

 A weighted clause includes parsing, clause evaluation, scalar multiplication,
normalization into the row accumulator, and physical frame cleanup. 
