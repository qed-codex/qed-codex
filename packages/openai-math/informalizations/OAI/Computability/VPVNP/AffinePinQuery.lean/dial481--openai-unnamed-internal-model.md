---
{
  "module": "OAI/Computability/VPVNP/AffinePinQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack program for affine pin coefficients

The immutable pin mask and table are independent of the row and queried
monomial. The program computes three offsets from the live row index,
classifies the packed exponent, selects the pin, and performs the scalar
operation in the advised power basis.


### `Port`

 The combined ports for classifying a queried monomial, reading its pin data, and computing
the field coefficient. 

### `machine`

 Select the coordinate’s mask bit and field value, classify the requested exponent, and
compute the coefficient of its affine pin equation. 

### `mask`

 The coordinate-ordered bit vector indicating which variables are pinned. 

### `values`

 Concatenate the pinned-value table in coordinate order, encoding every field element in
limbs of `v` bits. 

### `advice`

 The fixed exponent width, scalar width, pin mask, and packed field-value table used for
every monomial query of this slice. 

### `frame`

 Combine the pin advice and current lookup state with a clean field-arithmetic bank
containing the packed extension modulus. 

### `cost`

 Uniform step bound over the `t` coordinate rows for decoding an index, scanning the
exponents, reading the pin table, and returning a scalar. 

### `machine_runs`

 Return the canonical scalar for the indexed row and queried exponent.
All temporary stacks are clean at the return. 
