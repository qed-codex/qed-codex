---
{
  "module": "OAI/Computability/VPVNP/PermanentInterior.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentInterior.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentInterior.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The squarefree interior coefficient of a cycle-cover term

Once the directions of the ring rows and the choices of the clause rows
are fixed, each occurrence gadget sees two incoming bits. Its internal
rows cancel unless these bits agree. When they agree, the coefficient
retains the two exit columns precisely for the selected occurrence.


### `coeff_expandedTerm`

 Extracting the interior coefficient enforces both occurrence ownership and
agreement between the two incoming ports. 
