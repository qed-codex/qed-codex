---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwnerDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwnerDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical input bounds for the shrinking slot directory

The mixed-radix scan reads only the three descriptor arrays and the cyclic
successor array. Their lengths follow from the packed graph parameters. Placing
them below a common scratch base gives the source bounds for both owner passes.


### `genuineInputs_before`

 The role, old arc and subdivision arrays end below the scratch base.
Every decoded read is therefore stable throughout the two owner scans. 

### `dummyInput_before`

 Both sides of every dummy field read below the scratch base when the
packed-site successor array ends there. 
