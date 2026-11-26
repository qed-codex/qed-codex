---
{
  "module": "OAI/Computability/VPVNP/PermanentEntryProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentEntryProduct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentEntryProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Separating exterior ring edges from occurrence ports

A ring row chooses either a direct edge to the next exterior column or an
edge to the first interior column of its occurrence gadget. Multiplying the
row choices uses each active occurrence port exactly once.


### `ringEntry_product`

 Under the variable-splitting equivalence, ring inputs factor into the
direct exterior product and one interior variable for each active occurrence. 
