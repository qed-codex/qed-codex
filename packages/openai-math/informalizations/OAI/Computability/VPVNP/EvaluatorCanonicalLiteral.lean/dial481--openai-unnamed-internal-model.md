---
{
  "module": "OAI/Computability/VPVNP/EvaluatorCanonicalLiteral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCanonicalLiteral.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCanonicalLiteral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The literal evaluator for the canonical finite slice

The basis and the unit ordinal used by the tape program are the dense
ordinals furnished by the monomial prefix-rank queries. The physical matrix
reader receives the source ordinal before the destination ordinal. The
algebraic query returns the coefficient in the opposite order.

The point-count bound gives an index word width fixed independently of the
choice of pin values, the prime and the binary exponents.


### `canonicalGroundFintype`

 The finite enumeration of the slice ground field used to express canonical evaluator
coordinates and bound the number of point ordinals. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : DecidableEq (Ground p t d)`

 Decidable equality on the finite slice ground field used by the canonical
coordinate-algebra construction. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Algebra (Ground p t d) (Ambient p)`

 The algebra structure on the ambient field induced by the chosen embedding of the finite
slice ground field. 

### `Model.canonical_dimension_le`

 The number of dense ordinals is bounded by the paper's geometric
point count for the chosen slice. 

### `ordinalWidth`

 An extra bit lets the register store the dimension itself, including at a power of two. 

### `Model.dimensionWord`

 The dimension of the canonical coordinate-algebra presentation encoded in a v-bit word for
the evaluator. 

### `Model.canonical_literal_evaluator`

 Instantiate equation (8.2) and the uniform head bound on the canonical
Macaulay presentation. Both assertions concern the same literal two-tape
program and the same raw input. 
