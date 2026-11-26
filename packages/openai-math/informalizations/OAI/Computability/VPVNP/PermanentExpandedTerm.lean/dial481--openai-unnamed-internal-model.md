---
{
  "module": "OAI/Computability/VPVNP/PermanentExpandedTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentExpandedTerm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentExpandedTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Expanding the rows outside the equality gadgets

A term chooses a direction in each variable-ring row and an occurrence in
each clause row. The internal gadget rows are kept together until their
three squarefree column coefficients are extracted.


### `expandedTerm`

 The summand associated to the choices in all exterior rows. 
