---
{
  "module": "OAI/Computability/VPVNP/AffinePinCoefficient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinCoefficient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AffinePinCoefficient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Bounded native evaluation of an affine coefficient over the advised field 

### `encode`

 Represent a field element by its power-basis coefficients in the advised extension, using
the specified algebra isomorphism. 

### `scalar_encode`

 Each entry of the immutable pin table uses the same field encoding as the
matrix coefficients. 

### `entry`

 Initial work for a pin-row lookup, containing the binary coordinate index and the
concatenated fixed-width exponent words of the requested monomial. 

### `storage`

 Initial stack-height allowance for an affine coefficient query, accounting for its pin
mask, scalar table, packed exponent words, and field advice. 

### `space`

 Peak stack-height bound for the affine coefficient query obtained by adding its step budget
to the initial storage allowance. 

### `bounded`

 Every intermediate stack is bounded by the input-bank capacity plus the
polynomial clock of the call. 

### `encode_pin`

 Transport the scalar returned by the coordinate case split to the actual
pin coefficient over the chosen field. 

### `coefficient`

 Native affine-row lookup computes the packed coefficient in the actual
advised field at the requested exponent. 
