---
{
  "module": "OAI/Computability/VPVNP/ShiftedPairing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedPairing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedPairing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The integral pairing for shifted crossing

Appendix B of *VP and VNP differ over every field* gives the coefficient of the
full fermionic contraction as a signed binomial determinant. In each sector of
fixed particle number, Cauchy–Binet expresses this determinant as a Gram matrix
of Pascal minors. A nonzero minor can only lower the energy of the intermediate
index. This proves that the pairing on the entire energy cutoff is unimodular.

Its integral inverse acts on the first operator index in both crossing terms.
The two factorization index sets can have different sizes, and each gives a
flattening rank bound after specialization to an arbitrary field.


### `compound`

 Matrix of the size-`m` minors, with each index set in increasing order. 

### `compound_transpose`

 Transposition exchanges the two index sets of every minor. 

### `compound_mul`

 Cauchy–Binet over an arbitrary commutative ring. 

### `pascalMinor_support`

 If an integer Pascal minor is nonzero, each selected column index is at
most the corresponding selected row index. 

### `pascalMinor_diagonal`

 Every principal minor of the integer Pascal matrix has determinant one. 

### `pascalMatrix`

 The matrix of binomial coefficients before taking exterior powers. 

### `pascalGram`

 The Gram matrix of Pascal's triangle gives the contraction kernel. 

### `doubledSectorEnergy`

 A sector of Fock states with fixed occupation number and bounded doubled energy. 

### `doubledSectorEnergy_eq`

 Doubling removes all half-integral mode energies in a fixed occupation sector. 

### `sectorPoleDegree_eq`

 For a pair of equally large, nonempty blocks the pole degree `L = h + h' - 1`
is an integer. The numerator in its doubled-energy formula is exactly even. 

### `EnergySector`

 The states with exactly `m` occupied modes among the first `n` and doubled energy at most
`bound`. 

### `sectorPascal`

 Pascal minors on the energy downset of a fixed occupation number. 

### `sectorPascal_gram`

 No intermediate index outside the energy cutoff contributes to Cauchy–Binet. 

### `sectorPascal_det`

 The restricted matrix of Pascal minors has determinant one, including ties in energy. 

### `crossingRowSign`

 The sign of a full matching in the order of the fermionic fields of Appendix B. 

### `sectorPairing`

 The signed determinant of the full-contraction coefficients in equation (B.1),
restricted to an energy sector. 

### `sectorPairing_isUnit`

 Equation (B.1)'s integral pairing in each fixed-cardinality sector is unimodular. 

### `crossingPairing`

 The pairing on all nonempty states uses the positive particle-number sectors as blocks. 

### `crossingPairing_isUnit`

 The simultaneous pairing on every nonempty state under the energy cutoff has
an integral inverse. 

### `doubledSectorEnergy_eq_sum`

 Enumerating the modes in increasing order preserves the total doubled energy. 

### `BoundedState`

 A nonvacuum fermionic state in the energy ball of doubled radius `B`. 

### `boundedStateEquivSectors`

 Decompose the energy-bounded nonvacuum states into blocks by occupation number. 

### `boundedStatePairing`

 The full integral pairing on the nonempty finite subsets of natural modes of
doubled energy at most `B`. 

### `boundedStatePairing_isUnit`

 An integral inverse exists for every energy cutoff in the infinite-mode indexing. 

### `boundedStatePairing_eq_zero_of_card_ne`

 On states with different occupation numbers the full-contraction pairing vanishes. 

### `boundedStatePairing_eq_det`

 In the natural-mode indexing, the integral pairing is the signed determinant
of the binomial contraction kernel, in increasing order on both lists. 

### `normalizeCrossing`

 Apply the inverse of the integral pairing on the first index in both crossing
families. This preserves the original two index sets of factors. 

### `crossingMatrix`

 Integral coefficients of a tensor flattened on one crossing cut. 

### `crossingMatrix_rank_cast`

 Reducing the chosen integral flattening to any field preserves its bound
by the number of intermediate coordinates, including in characteristic two. 

### `crossingRanks_overField`

 Both flattenings and their two different bounds specialize simultaneously.
The swapped second coordinates display the opposite cut of the second summand. 
