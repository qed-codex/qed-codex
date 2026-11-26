---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationMaskProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationMaskProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationMaskProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed native constructor for original-coordinate singleton masks.
Masters212/218 are retained; output214 and scratch120/221/222/223 are the
only touched stacks. No table of masks or semantic mask oracle is supplied. 

### `zero_run`

 Zero-mask construction retains the count master and all unrelated stacks. 

### `selectCommand`

 Read the zero zeroPrefix, replace the selected bit, and restore the zeroPrefix. 

### `advance`

 One native step advances the caller's original-coordinate unary index. 
