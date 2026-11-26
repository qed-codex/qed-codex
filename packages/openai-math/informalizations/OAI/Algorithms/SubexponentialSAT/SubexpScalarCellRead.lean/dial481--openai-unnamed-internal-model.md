---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpScalarCellRead.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScalarCellRead.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScalarCellRead.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving scalar-cell access with runtime addresses

The fixed program forms the unary address `row * N + col`, then calls the
measured persistent array reader. The table already contains complete scalar
frames, so selecting a cell requires no decoding or re-encoding.

Ports: table 0, output 1, unary dimension 2, unary row 3, unary column 4,
unary frame width 5, and initially empty scratch 6--11. Only output 1 changes.


### `indexCommand`

 Local address generation uses the checked unary-copy multiplication loop. 

### `Clean`

 Runtime scratch requirements; all six stacks are restored by the program. 

### `cost`

 Includes the address subprogram's return and the complete persistent read. 

### `command_eval`

 Selection from any fixed-width record table. The complete output frame
is prefixed to the caller's output; every other stack has its original value. 

### `inputSize`

 Measured input bytes, including the retained table and four unary inputs. 

### `table_cell`

 The address uses coordinate-major row order, with no reversal of frame bits. 

### `scalar_command_eval`

 In the matrix scalar encoding, the selected bytes are exactly the existing
forward scalar frame. No value-dependent instruction or decoding assumption is used. 
