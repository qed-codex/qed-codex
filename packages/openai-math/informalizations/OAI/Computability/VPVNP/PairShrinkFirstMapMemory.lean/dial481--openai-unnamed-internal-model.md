---
{
  "module": "OAI/Computability/VPVNP/PairShrinkFirstMapMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkFirstMapMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkFirstMapMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resident inputs immediately after the shrinking hidden scan

The child scan stores one packet per preceding site. The hidden scan writes
above all of those packets and above the popped parent's own arguments.
It supplies the single shared value used at both ends of an absorbed edge.


### `Job.firstMapFields`

 Both families of inputs used by the first resident come from the same
concrete memory after the once-per-field guess. 

### `Job.parentStored_after_fields`

 The popped parent argument survives the older-child writes and the
upper-region hidden writes before the surviving-interval gather reads it. 
