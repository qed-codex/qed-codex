---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSeparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSeparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSeparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrarily many independent symbolic color groups

Section 4.3 of `source/subexponential-sat.txt`.  The color type is an arbitrary
finite type, so the results apply to `Fin r` with no fixed bound on `r`.
Every sum and product is a genuine finite operation in a commutative semiring.
The independence assumptions are pointwise statements about group values,
not assumptions about the desired sum identity.


### `sum_prod_eq_prod_sum`

 Finite distributivity over all independent color choices. 

### `weighted_separation`

 Equation (4.6) for fixed outer data.  The group of color `g` depends only
on the `g` input.  All other inputs may therefore be replaced by their fixed
representatives when evaluating that group, while the actual weight stays. 

### `sum_reindex_fibers`

 An actual equivalence reindexes the full assignment space by its outer
data and one independent inner choice for each color. 

### `weighted_separation_equiv`

 Full-input form of (4.6), including a proved bijective reindexing and an
arbitrary finite number of color groups. 

### `weighted_separation_equiv_map_weights`

 Scalar weights may be embedded into the symbolic value ring.  For
polynomial values, instantiate `φ` with the appropriate constant homomorphism. 

### `coordinate_prod_partition`

 A product over coordinates splits across any pairwise-disjoint finite
family of supports, together with the complement of their union. 

### `momentWeight_partition`

 The finite-support monomial weight from the actual moment definition
splits into one weight per color and a complementary-coordinate weight. 

### `momentWeight_of_components`

 Restriction equalities, such as those proved for actual coordinate
reconstruction, give exact factorization for any coordinate-label function.
No additive or multiplicative property of `lift` is assumed. 

### `momentWeight_coordinateAssemble`

 Exact moment weights for the actual zero-extension-and-sum coordinate
assembly. Pairwise disjointness alone supplies all required restrictions. 

### `momentWeight_coordinateSplit_symm`

 The same identity stated for the inverse of the actual coordinate linear
equivalence, ready to compose with the family quotient/coset equivalence. 

### `momentWeight_coordinateReconstruct`

 The exact weight identity for the layout's actual multicolor coordinate
and quotient reconstruction. It discharges the scalar factorization premise
of `weighted_separation_equiv` with no additional weight assumption. 
