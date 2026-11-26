---
{
  "module": "OAI/Computability/VPVNP/PairShrinkMapJobInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkMapJobInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkMapJobInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native shrinking party and its selected kernel witness

The same placed old factors, independently supplied new halves and once-guessed
absorbed labels give the same entry input in the executable map and in the
local polynomial witness.


### `noncomputable local instance : DecidableEq X.Base`

 Classical decidable equality on the compression state’s base vertices for identifying the
native map input with the selected kernel input. 

### `Job.entryInput_eq_witness`

 Reading the stored parent and its placed child packets gives the input
whose accepted name list appears in the shrinking kernel's monomial witness. 
