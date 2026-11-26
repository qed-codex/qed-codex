---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleImageChildren.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleImageChildren.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleImageChildren.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical child argument scan in the fixed shrinking image

The selected substep first copies the node and old directory pointer, builds
its slot-ordinal register bank, and reads the child arguments. Every register
outside that segment's bank is preserved, including the shared level locator.


### `argumentBank`

 The concrete register embedding for the old-child argument scan within the selected shrink
stage. 

### `imageChildren`

 This is the trace of the physical child prefix in a scheduled stage. 

### `imageChildren_realizes`

 Exact local execution, including partial tapes, on the installed child
code. The inputs are the located words and actual rows, and the continuation
gets the complete packet writes as a function of its original memory. 
