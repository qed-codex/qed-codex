---
{
  "module": "OAI/Computability/VPVNP/PairNativeFlowPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFlowPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFlowPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From a tick-only structured flow to a native configuration prefix

The linked guards execute a single local step. An elementary instruction
whose event is a tick also has a local native successor and preserves both
memories. Composing those successors yields the concrete endpoint and the
exact instruction count independently of the behavior at the exit label.


### `Exec.toPrefix_of_ticks`

 Local steps in the structured derivation give a genuine native prefix
from the entry registers to the exit registers. 

### `Exec.toPrefix`

 Specialization used by the operand and cache arithmetic, which supply
their tick count directly. 
