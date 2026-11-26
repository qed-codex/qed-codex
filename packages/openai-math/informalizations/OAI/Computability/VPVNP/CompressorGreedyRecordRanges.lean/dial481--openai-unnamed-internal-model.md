---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyRecordRanges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyRecordRanges.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyRecordRanges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addresses stored in the color and offset operand records

The color records point to labels in their own arena. The offset records
point to offset labels, projected displacements or the common zero cell.
All of these lie in the newly allocated greedy region.


### `color_pointer_range`

 Every color operand is the address of a label in the fresh color array. 

### `tag_pointer_range`

 Every offset operand points to an offset label, a projected displacement
word or the common zero word, all within the same fresh allocation. 
