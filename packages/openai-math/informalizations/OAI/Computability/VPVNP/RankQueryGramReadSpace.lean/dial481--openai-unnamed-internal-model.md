---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramReadSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramReadSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramReadSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Live storage for two nested Macaulay reads

A long coefficient query may take exponential time. Its independently
certified stack-height bound is reused for the second query. Only the
short multiplication is charged by its running time.


### `BoundedRun.enlarge`

 Enlarging a cap keeps the same complete instruction trace. 

### `CorrectSpace`

 Every valid entry read returns the packed scalar `M i j` within `B` steps and `S` bits per
stack, preserving the indices and restoring a ready auxiliary state. 
