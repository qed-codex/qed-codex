---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpaceSeek.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceSeek.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpaceSeek.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical head displacement during a stack seek and rewind

Passing a packed cell advances the first head by one and moves the second
head left by two to store the cell and its tag. Restoring the cell reverses
both movements. These counts include blank stack delimiters.


### `seek_travel`

 The seek moves one packed cell right and two scratch cells left for
every cell of the prefix. 

### `restore_travel`

 Rewind all saved cells to their original order, returning the scratch
head to its original position. The final empty test moves neither head. 
