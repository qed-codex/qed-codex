---
{
  "module": "OAI/Computability/VPVNP/MacaulayRelations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRelations.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayRelations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linear relations in the reduced slice algebra

Appendix D.1 descends a bounded coefficient row test to the field of definition.
A power of the cardinality of this finite field acts linearly on polynomials.
Thus a relation among polynomial values on the slice becomes a relation among
the powered coefficient rows modulo the Macaulay row space.


### `rowSpan_descent`

 Membership of a row over the base field descends through any field extension.
Apply a base-linear retraction of the scalar inclusion to the coefficient equations. 

### `coefficientRow_pow_mem_of_extension`

 The bounded Rabinowitsch certificate may have coefficients in an extension field,
even though the matrix and the tested row are over the base field. 

### `WeakCertificateBound`

 A uniform weak Nullstellensatz certificate bound for systems of degree at most
`D` in `n` variables. The extra equation in the Rabinowitsch system has index `none`. 

### `row_test_of_weakCertificateBound`

 The two directions of the D.1 row-space criterion. The forward direction takes
the uniform degree bound from the effective weak Nullstellensatz as a hypothesis. 

### `linearCombination_pow_card`

 A power of the field cardinality distributes over linear combinations and fixes
their coefficients. 

### `poweredRows_sum`

 Coefficient rows commute with the base-linear Frobenius relation. 

### `poweredRows_relation_iff`

 The value relation for a list of queried polynomials is exactly the corresponding
linear relation on their powered rows modulo the Macaulay row space. In particular
this applies to the monomial lists used in the prefix-rank and coordinate tests. 
