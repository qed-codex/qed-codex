---
{
  "module": "OAI/Computability/VPVNP/ShiftedFactorization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedFactorization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedFactorization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two energy cutoffs in the shifted crossing

Appendix B of *VP and VNP differ over every field* extracts `[z^(-s-1) w^s]`
from a product of two normally ordered fermionic fields times `(z-w)^L`.
On the exterior basis of occupation states in the first `N` modes, the two orders
of the product give different finite matrix factorizations over the integers.
All energy variables are doubled to keep track of the half-integral mode energies.


### `Occupation`

 An exterior basis state specified by the occupied modes among the first `N` modes. 

### `doubledEnergy`

 Twice the energy of an occupation state, obtained by summing `2 * r + 1` over its occupied
modes. 

### `FieldTerm`

 One creation or annihilation term in a divided derivative of a fermionic field on the first
`N` modes. 

### `FieldTerm.mode`

 The mode whose occupation is changed by this field term. 

### `FieldTerm.create`

 Selects creation when true and annihilation when false. 

### `FieldTerm.derivative`

 The order of the divided derivative applied to this field term. 

### `exponent`

 Laurent exponent after the divided derivative. 

### `weight`

 The doubled source weight `2 * derivative + 1` contributed by this field term. 

### `derivativeCoefficient`

 The integer coefficient of the divided derivative on the chosen mode, including the sign
from differentiating an annihilation term. 

### `matrix`

 The signed exterior creation or deletion, with the divided derivative coefficient. 

### `normalOrder`

 Move creations left and deletions right, preserving the order within each group. 

### `normal_word_homogeneous`

 The permutation and derivative weights affect the values of entries, while
every supported entry changes energy by the exponent plus the source weight. 

### `normal_coefficient_homogeneous`

 A coefficient of a sum of normally ordered words with the same source
weight is homogeneous on the exterior basis. 

### `normalInversions`

 Exponent of the normal-ordering sign: each deletion crosses the creations to
its right. 

### `normalBlock`

 Coefficient of the normally ordered product of the divided derivatives of
orders `D 0, …, D (m-1)`, truncating the modes to `Fin N`. 

### `normalBlock_homogeneous`

 The coefficient `[z^b] Y_D` changes doubled energy by precisely
`2b + ∑ᵢ(2Dᵢ+1)` whenever its matrix entry is nonzero. 

### `ModeHomogeneous`

 A coefficient of exponent `b` for a block of doubled energy `h` changes doubled
energy by `2*b+h`. 

### `Cutoff`

 The states whose specified energy is at most `E`. 

### `multiplier`

 The coefficient of `z^(L-a) w^a` in `(z-w)^L`. 

### `firstExponent`

 The power `-s - 1 - L + a` required from the first field after choosing `z^(L-a) * w^a` in
the multiplier. 

### `secondExponent`

 The power `s - a` required from the second field after choosing the term of degree `a` in
`w` in the multiplier. 

### `multiplier_expansion`

 Expanding the polynomial multiplier into individual signed binomial weights. 

### `coordinateCount`

 Number of coordinates in either finite factorization. 

### `HasShiftedFactorizations`

 Two factorizations of the signed coefficient, with an integral factor on each side
of the two respective cuts. The finite coordinate types include the binomial index
and the intermediate occupation state. 

### `shiftedBlockFactorization`

 For `[z^(-s-1) w^s]`, the first product has the intermediate bound
`E+H+2*s` in doubled energy, and the reversed product has `E+H-2*s`.
The two product-coordinate types display both exact integer factorizations. 

### `normalBlock_factorization`

 Apply the two distinct finite cut factorizations directly to the signed coefficient
of the concrete normally ordered field products. The two lists of derivative orders
have the same length and their doubled source energies are constant in this block. 

### `factorization_rank`

 Integer rank factorizations give the same bound after passage to any field. 
