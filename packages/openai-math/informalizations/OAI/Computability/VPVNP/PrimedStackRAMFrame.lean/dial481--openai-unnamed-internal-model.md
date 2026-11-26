---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory represented at each node visit

Input, mark and count cells occupy disjoint regions from the frame planes.
The external stack instructions leave the full input rectangle, every mark
and every production count intact.


### `dataCell`

 Recognize an input cell, leaf-position mark, or production counter among the parser’s
scratch locations. 

### `DataEq`

 Agreement of two memories on the assembled inputs, leaf marks, and production counts of the
scratch rectangle based at `base`. 

### `frames`

 The frame list encoded as exact machine words (top first). 

### `Holds`

 One complete logical visit state together with its assembled input rectangle. 
