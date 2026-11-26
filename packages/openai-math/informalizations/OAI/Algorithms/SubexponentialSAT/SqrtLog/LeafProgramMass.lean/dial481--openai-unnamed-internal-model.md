---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramMass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramMass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramMass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The primitive integer accumulator used after each marked-clause count.
Both operands have runtime lengths. The fixed instruction table adds them
exactly and restores little-endian orientation; no arithmetic instruction or
precomputed mass is admitted into the machine model. 

### `command_eval`

 This adds two binary words with an actual execution of the fixed adder. 
