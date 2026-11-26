---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsABWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsABWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native equal-piece widths and prefix offsets for all AB bundles

The source index enumerates the piece ranks of each bundle consecutively.
One probe retrieves its total thick width. Two writes give the width and
prefix offset of this particular piece. Division by zero at a zero remainder
implements the zero indicator in the machine's prescribed word arithmetic.


### `visit`

 Public words give the number of pieces, rectangle stride, total-width column,
AB width and AB offset bases. The latter two rectangles share their row stride. 

### `row`

 Recover the bundle number from the linear piece cursor by dividing by the number of pieces
per bundle. 

### `rank`

 Recover the piece's rank within its bundle as the remainder of the linear cursor. 

### `input`

 Address of the selected bundle's total-width word in the input column. 

### `address`

 Address of a piece's width or offset in the corresponding output rectangle, using the
bundle stride and piece rank. 

### `extra`

 The machine-word indicator that this rank receives one of the extra units left over after
dividing the bundle width. 

### `offset`

 The sum of the widths assigned to earlier pieces, including their share of the division
remainder. 

### `events`

 The events for one AB-piece visit, including the read of the bundle total and the writes of
the piece width and prefix offset. 

### `pieceStart`

 Starting index of piece rank r in a balanced split. 
