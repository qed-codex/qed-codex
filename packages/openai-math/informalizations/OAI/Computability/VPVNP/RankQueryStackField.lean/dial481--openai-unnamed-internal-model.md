---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native coefficients for the determinant stack

Each scalar in a continuation is one canonical base-`p` word with `e` digits.
The product unpacks both words, uses Horner multiplication modulo the advised
monic polynomial, and packs the reduced answer. The interpretation in the
advised quotient is an injective ring homomorphism.


### `Scalar`

 Numeric scalar representation with a fixed advised modulus. 

### `Scalar.code`

 Packed index of the scalar's `e` base-`p` coordinates. 

### `pack`

 Pack a vector of prime-field coordinates into its finite scalar code. 

### `digits`

 Decode the scalar's packed index into its vector of prime-field coordinates. 

### `interpret`

 Evaluate the decoded coordinate polynomial at the adjoined root of the modulus. 

### `product`

 Materialize each round of the extension-field product before the next round. 

### `interpretation`

 Ring homomorphism interpreting encoded scalars in the algebra obtained by adjoining a root
of the modulus. 

### `code_lt`

 Every scalar occupies at most `e * clog 2 p` bits. 
