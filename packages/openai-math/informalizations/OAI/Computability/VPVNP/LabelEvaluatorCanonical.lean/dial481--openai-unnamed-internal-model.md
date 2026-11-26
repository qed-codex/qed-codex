---
{
  "module": "OAI/Computability/VPVNP/LabelEvaluatorCanonical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorCanonical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorCanonical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The graded monomial basis of the label evaluator

The dense ordinals returned by the prefix-rank algorithm are identified with
the retained indices of a slice presentation. Multiplication and Frobenius
entries in this presentation are exactly the scalars returned by the indexed
query. The distinguished unit is dense ordinal zero.


### `Canonical`

 A slice presentation whose listing, dense basis ordinals and field-valued
queries use the same enumeration of monomials. 

### `Canonical.presentation`

 Monomial presentation of the finite-slice coordinate algebra identified with the bounded
  rank-query data. 

### `Canonical.ordinal`

 Equivalence from dense basis ordinals to the greedy pivot indices in the canonical
  monomial listing. 

### `exists_canonical`

 Build the canonical presentation from the very equations used to query
the matrix, allowing any equal presentation of their affine ideal. 

### `Canonical.denseBasis`

 The canonical presentation's basis, indexed by the dense machine ordinals. 

### `Canonical.denseBasis_apply`

 Ordinal `i` denotes exactly the basis monomial returned by the numeric prefix ranks. 

### `Canonical.matrixEntry_dense`

 The physical query stores the coefficient at the destination ordinal. 

### `Canonical.label_transition`

 The path matrix is transposed relative to the coefficient array of label multiplication. 

### `Canonical.frobenius_transition`

 The Frobenius path matrix has the same destination/source convention. 

### `Canonical.denseBasis_unit`

 The dense unit ordinal labels the constant monomial. 

### `Canonical.functional_apply`

 The output functional first reads the dense unit ordinal and then the
prime-field coordinate of that coefficient. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 Finite enumeration of the ground field used to identify the canonical rank-query
presentation. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : DecidableEq (Ground p t d)`

 Decidable equality on the finite ground field used to select canonical pivots. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Algebra (Ground p t d) (Ambient p)`

 Algebra structure on the ambient field induced by the ground-field embedding for the
canonical presentation. 

### `Model.canonicalPresentation`

 Select the presentation for this exact input reader, prime and advised slice. 

### `Model.withCanonicalPresentation`

 Use the verified ordinal basis in the algebraic label evaluator at every
input exponent vector and every bit width. 

### `Model.canonical_functional`

 For the rebuilt model the actual physical ordinal in the first coordinate
of the functional has value zero. 

### `Model.canonical_pathCount_mod`

 Counting matrix-index paths on the actual dense ordinals recovers the
functional of the canonical model modulo the advised prime. 
