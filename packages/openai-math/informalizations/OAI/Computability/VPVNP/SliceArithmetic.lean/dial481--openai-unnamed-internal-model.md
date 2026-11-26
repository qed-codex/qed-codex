---
{
  "module": "OAI/Computability/VPVNP/SliceArithmetic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmetic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmetic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary coefficient vectors for the evaluator's slice field

The prime modulus, extension degree and low coefficients of the defining monic
polynomial come from the advice. An extension-field element is represented by
its coefficients in increasing degree order. Each coefficient occupies
`clog 2 p` bits in the evaluator's little-endian word format.


### `Vector`

 Canonical residues of the `e` low coefficients, in increasing degree order. 

### `encode`

 Encode the coefficient vector with exactly `e * clog 2 p` bits. 

### `ofBits`

 Decode all bit strings by reducing each word modulo the supplied prime. 

### `modulus`

 Read the advised polynomial from its low coefficients. 

### `value`

 Interpret a coefficient vector in the advised quotient ring. 

### `zero`

 The zero element in the power basis, with zero in each of the `e` coefficient positions. 

### `one`

 Power-basis vector of the constant polynomial one, with its unit coefficient in degree
zero. 

### `add`

 Add the two power-basis vectors coefficientwise modulo `p`. 

### `scale`

 Multiply every coefficient of a power-basis vector by the prime-field scalar `a`. 

### `cast_val_eq_finEquiv`

 The residue of a canonical limb is the image under the finite-ring equivalence. 

### `repr_value`

 Decoding a vector and taking its `i`th power-basis coordinate recovers the
stored limb exactly. 
