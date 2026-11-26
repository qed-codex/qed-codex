---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupPrimitives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupPrimitives.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SetupPrimitives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual fixed bit programs for the two logarithmic setup quantities.
Input and output numbers are arbitrary padded little-endian words. 

### `addConst`

 `k` is fixed syntax, not a natural-number machine instruction. 

### `logSucc`

 The floor binary logarithm plus one, with zero mapped to one. 

### `computeL`

 Sixteen explicit increments, followed by the actual log-plus-one program. 

### `L_le_wordLength`

 The numerical search fuel itself is linear in the original bit length. 
