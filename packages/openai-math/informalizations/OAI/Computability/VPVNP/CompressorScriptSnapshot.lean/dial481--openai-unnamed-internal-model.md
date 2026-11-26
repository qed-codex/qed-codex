---
{
  "module": "OAI/Computability/VPVNP/CompressorScriptSnapshot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScriptSnapshot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScriptSnapshot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The operands loaded by each actual compressor-script visit

The calendar and recipe compute an address and all public worker operands in
the current memory. The launcher copies these operands to the active frame,
increments the ordinal and preserves the row count. All addresses are derived
from the declared workspace layout.


### `recipeState`

 Compute the level header used by the script recipe from the calendar and the current
memory. 

### `operand`

 Evaluate a recipe expression at a script occurrence using its level header and calendar
memory. 

### `snapshot`

 The row directory, active frame, and controller counter properties all
hold on the actual output of the calendar and its selected recipe. 
