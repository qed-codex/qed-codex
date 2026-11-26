---
{
  "module": "OAI/Computability/VPVNP/SliceField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite slice field and its defining polynomial

Section 8.2 uses the smallest positive extension degree of the prime field
whose cardinality `Q` exceeds twice the point-count bound `N`. A monic
irreducible polynomial gives a presentation of that extension, using at most
`2 log₂ Q` bits for all coefficients below its leading term.


### `extensionDegree`

 Smallest positive degree giving a prime-power cardinality above `2 * N`. 

### `FieldOf`

 The selected extension of the prime field. 

### `embed`

 Embed the advised field in the ambient algebraic closure for the hyperplane cuts. 

### `polynomialOfBits`

 Read the low coefficients of a monic polynomial from fixed-width binary words. 

### `exists_polynomial_advice`

 The field description encodes the minimal polynomial of a power-basis generator
and hence defines the selected field up to prime-field algebra isomorphism. 

### `advice_length_le`

 The complete binary advice for the monic polynomial has length at most twice
the base-two logarithm of the cardinality of the selected field. 
