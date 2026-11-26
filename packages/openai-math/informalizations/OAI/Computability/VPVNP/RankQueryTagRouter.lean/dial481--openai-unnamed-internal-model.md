---
{
  "module": "OAI/Computability/VPVNP/RankQueryTagRouter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryTagRouter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryTagRouter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Fixed finite control for the low bits of a descriptor tag

The code pops a fixed number of little-endian bits, restores them in the
opposite order, and enters the selected subroutine with its original bank.


### `select`

 Read `n` low-order bits from a tag, restore them to the stack, and invoke the continuation
indexed by their little-endian value. 

### `digits_runs`

 A tag known to fit in the tested bits is selected exactly. 
