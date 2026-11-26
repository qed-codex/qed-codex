---
{
  "module": "OAI/Computability/VPVNP/AffinePinStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reading the pinned coordinate and classifying its exponent 

### `Port`

 Stacks for decoding the row index, computing offsets, reading the pin mask and scalar
table, and classifying the packed exponent. 

### `Advice`

 Immutable lookup data for the affine pin stage, including the two record widths, membership
mask, and packed field values. 

### `Advice.w`

 Number of bits in each coordinate’s exponent word in the packed monomial. 

### `Advice.scalarWidth`

 Number of bits per field element in the packed table of coordinate values. 

### `Advice.mask`

 One Boolean flag per coordinate, set precisely for the pinned coordinates in the query
  advice. 

### `Advice.values`

 Consecutive fixed-width blocks holding the coordinate values in field representation. 

### `Work`

 Mutable state of a pin-row query, including the coordinate index, offset, exponent stream,
extracted value, and classification flags. 

### `Work.binary`

 Binary input word identifying the coordinate whose pin row is being queried. 

### `Work.index`

 Decoded coordinate index, stored as a unary counter and reused for both pin-table reads. 

### `Work.offset`

 Bit offset to the selected exponent's low bit, represented by one unary mark per bit to
  skip. 

### `Work.exponents`

 Packed exponent words of the queried monomial, consumed while testing for the constant
  and selected-variable monomials. 

### `Work.value`

 Output stack for the packed scalar at the selected coordinate in the pin-value table. 

### `Work.active`

 Output stack for the mask bit indicating whether the selected coordinate is pinned. 

### `Work.constant`

 Output flag for the constant monomial, set when all bits in the exponent vector are zero. 

### `Work.unit`

 Output flag for the selected variable's monomial, set when its low exponent bit is the
  only bit equal to one. 

### `frame`

 Place the pin mask, scalar values and stride markers on their advice stacks and encode the
mutable work fields on the stage's remaining ports. 

### `machine`

 Decode the coordinate, classify its queried monomial, read its mask bit and packed pin
value, and clear the unary index. 

### `cost`

 Step bound for a stage call at row `i`, covering its binary decoding, exponent-offset
calculation, scan of `n` exponent bits, two table reads and index cleanup. 

### `machine_runs`

 The tables and width markers are retained. The row word, exponent vector,
unary row index and all other scratch are consumed or reclaimed. 
