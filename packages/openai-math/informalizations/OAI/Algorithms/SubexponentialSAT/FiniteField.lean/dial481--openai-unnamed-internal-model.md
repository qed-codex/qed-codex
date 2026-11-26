---
{
  "module": "OAI/Algorithms/SubexponentialSAT/FiniteField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FiniteField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/FiniteField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite extension and its defining polynomial

For each prime `p` and positive `h`, the field is constructed as mathlib's
`GaloisField p h`. Its size and extension degree are proved, not assumed.
A primitive element provides a monic irreducible polynomial of degree `h`,
and its polynomial quotient is identified with the same field.

The chosen primitive element and finite enumeration are noncomputable choices
of fixed finite objects. This module proves their mathematical existence and
properties; it does not claim an executable field-construction complexity bound.


### `E`

 The actual finite extension used for interpolation nodes. 

### `nodeEquiv`

 All nonzero elements, indexed by exactly `p^h - 1` positions. 

### `primitiveElement`

 A primitive element of the constructed field, chosen once for `p,h`. 

### `definingPolynomial`

 The monic irreducible polynomial defining the same extension. 

### `exists_monic_irreducible`

 In particular the needed defining polynomial exists for every positive
extension degree; it is not an assumption about the construction. 

### `quotientEquiv`

 Identify the polynomial quotient with the very same field used by the
interpolation layout, rather than an unrelated field of the same cardinality. 

### `polynomialQuotientEquiv`

 The identical equivalence written in the raw polynomial-quotient form used
by `SubexponentialSAT.LiftRing.Extension`, without importing that module. 
