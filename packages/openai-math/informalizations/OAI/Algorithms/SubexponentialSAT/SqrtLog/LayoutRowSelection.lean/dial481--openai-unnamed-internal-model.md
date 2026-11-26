---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRowSelection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRowSelection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutRowSelection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting actual integer constraint rows

This module isolates the semantic certificate for row selection. A later finite
minor search may produce the certificate; rational spanning is used only before
reduction, so the actual rows and their integer coefficient bounds are retained.


### `exists_actual_row_basis`

 The number of selected actual rows is exactly the rational constraint rank.
No coefficient rescaling and no modular row-space assertion is involved. 

### `selected_bound`

 Any height bound on the original integer rows remains literally true. 
