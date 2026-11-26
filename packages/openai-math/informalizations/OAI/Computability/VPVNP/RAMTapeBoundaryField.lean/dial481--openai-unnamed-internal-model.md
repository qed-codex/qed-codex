---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning one field of adjacent boundary records

A unary stack determines the field width. The control reads one pair of bits
per mark, saves the right bit, and moves the mark to a second stack. On reaching
the end of the width stack, it restores all marks for the next field.


### `Port`

 Ports for two field streams, the unary width and its temporary copy, and saved right-hand
bits. 

### `store`

 Construct the field-scanner bank from the width, restoration, input, and saved-bit stacks. 

### `State`

 Field-scanning control carrying a comparison accumulator through paired reads, bit saving,
and width restoration. 

### `code`

 Consume one bit pair per width mark, apply the comparison update, save the right bit, and
restore the width for the next field. 

### `fold`

 Apply the field comparison update to consecutive bit pairs until either list ends. 

### `runs`

 A field of width `xs.length` takes five instructions per pair and two per
restored mark. The two additional pops detect the ends of the width stacks. 
