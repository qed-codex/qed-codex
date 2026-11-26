---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Separation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Separation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Separation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Separation of the symbolic moment sums

Section 4.5, equation (4.8).  The input arguments of the two group functions
are separated while their values remain in one common commutative semiring.
In particular, the value semiring may be a polynomial or quotient ring;
there is no assertion that its formal variables split into disjoint groups.

All independence and weight hypotheses below concern the summands and are
pointwise.  The sum identity itself is proved by finite distributivity.


### `separated_sum`

 The distributive identity underlying (4.8), with the two functions already
written in terms of the input component on which each depends. 

### `weighted_separation`

 Weighted separation from actual independence on the two finite sets.
Representatives must belong to those sets; only the group functions use
representatives, while every weight retains its actual summation input. 

### `weighted_separation_fintype`

 The same result for finite types, including finite coset subtypes. 

### `weighted_separation_map_weights`

 Scalar weights can be embedded into a polynomial or quotient ring by a
ring homomorphism.  In the moment application this homomorphism is `C`. 

### `weighted_separation_outer`

 Summing (4.8) over any explicit finite collection of outer data.
The finite inner sets and their representatives may depend on the outer data. 

### `sum_reindex_fibers`

 An actual equivalence, rather than an assumed sum identity, reindexes a
finite input space by outer data and two finite fibers. 

### `weighted_separation_equiv`

 Full-input version of (4.8), with dependent coset-like fibers. The
equivalence supplies exhaustive, nonduplicating input enumeration. 

### `coordinateWeight`

 A monomial weight computed with arbitrary coordinate labels.  The label
map is an ordinary function: it need not preserve sums or products. 

### `coordinateWeight_union`

 Splitting an exact coordinate-label monomial across disjoint supports. 

### `coordinateWeight_three`

 The three weights in (4.8), with the complement represented by `sstar`.
No homomorphism property of the exact integer-label map is assumed. 

### `coordinateWeight_partition`

 If the three supports cover all coordinates, their product is the full
monomial weight used in the moment sum. 

### `coordinateWeight_congr`

 A weight on one block depends only on the input coordinates in that block. 

### `momentWeight_partition`

 The actual finite-support moment weight splits over the two supports and
their complement.  The exponents retain their original ambient indices. 

### `momentWeight_coordinateReconstruct`

 The concrete valuation reconstructed from an outer datum and its two
coset points has exactly the product of the three local moment weights.
The label map is arbitrary; no additive property of exact integer labels is
used.  This discharges the weight-factorization premise for the layout's
actual coordinate equivalence. 

### `rowGroup`

 A group built from chosen lifts of linear row values, with the other input
components in `offset`.  `build` may compose factor polynomials, multiply them,
and take a canonical truncation.  It is one fixed function of the beta values. 

### `rowGroup_add_invariant`

 Linear annihilation gives exact group independence, even for an arbitrary
lift and arbitrary fixed symbolic construction from the lifted parameters. 

### `liftedRowGroup`

 Build a symbolic group directly from the lifted rows and fixed residue
section of `CosetInvariance`.  Nonlinear coordinate representatives are allowed. 

### `liftedRowGroup_add_invariant`

 Exact beta constancy passes through any fixed symbolic construction,
including polynomial composition, products, and canonical truncation. 

### `liftedRowGroup_eq_of_sub_mem`

 Equivalent form for two arbitrary representatives of one fixed coset. 

### `coset_weighted_separation`

 Actual submodule-coset sums, enumerated by their submodule elements.
The hypotheses state translation invariance of each symbolic group along
its own submodule and pointwise factorization of the exact weight. 

### `coset_row_group_separation`

 A direct connection from annihilating linear rows to (4.8).
The group constructors can be actual symbolic polynomial constructions.
Their invariance is proved from the row kernels, rather than supplied as an
assumption about the resulting sums or resulting group values. 

### `coset_sum_decomposition`

 The outer-data enumeration covers the full split assignment space exactly
once. This is proved using the actual quotient-fiber equivalence. 

### `coset_full_weighted_separation`

 Full assignment-to-separated-coset identity. The group assumptions are
pointwise invariance under differences in the specified submodules; the
actual quotient partition and the separated finite summation are both proved. 
