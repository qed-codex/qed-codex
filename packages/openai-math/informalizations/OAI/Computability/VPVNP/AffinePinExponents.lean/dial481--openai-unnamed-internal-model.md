---
{
  "module": "OAI/Computability/VPVNP/AffinePinExponents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinExponents.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinExponents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the monomial of an affine pin row from its packed exponent bits

The low bit of the selected variable has a known offset in the packed
exponent array. A single scan distinguishes the zero vector, the vector
with just this one low bit set, and all other bit patterns. The scan
consumes the exponent scratch buffer and the unary offset. It returns
one bit for each of the two distinguished cases.


### `Port`

 Input stacks for the packed exponents and unary offset, with output stacks for the constant
and unit-monomial flags. 

### `Kind`

 Classify the monomial at coordinate `i` as the constant monomial, the variable `X i`, or a
different monomial. 

### `State`

 Control states for scanning to the selected exponent bit, checking the remaining bits, and
emitting the two classification flags. 

### `selected`

 Classify the prefix ending at the low bit of the selected coordinate. A previous nonzero
bit forces the other case. 

### `tailKind`

 Retain the prefix classification when every remaining exponent bit is false, and classify
the monomial as other when a true bit occurs. 

### `code`

 Stack instructions that consume the unary offset and packed exponents and write the
constant and selected-unit flags. 

### `bank`

 Place the exponent bit stream, offset markers, and existing flag-stack contents on the four
classifier ports. 

### `machine`

 Run the packed-exponent classifier from an empty scanned prefix and return after writing
both flags. 

### `classify`

 Zero except possibly at the selected bit gives the constant or linear
coefficient. A nonzero bit anywhere else gives the zero coefficient. 
