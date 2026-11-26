---
{
  "module": "src/New/UpperBound/Objects/RowChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/RowChain.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/RowChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The chain of theta lifts ι_μ along the spaces Y_j: level, character and 𝖦-equivariance

This file defines the theta lifts `New.Data.liftY` from forms on Y_j to forms on Y_{j+1} and their
composite, the chain ι_μ = `New.Data.lowerChain`, for a tame character ϑ with modulus Q. It
determines the level and character of the image on Y_m and shows that the chain commutes with
𝖦 = ∏ GL_r(𝔽_w). The basis of Y_j is indexed by `New.BlockIndex`, a block 0 of size r followed by
j blocks of size t; `New.blockNumber` is the number of the block.

## Main definitions and results

* `New.Data.lowerChain`, `New.Data.lowerChainAtLevel`: the chain; it lands in the level
  `New.Data.lastLevel`, cut out by `New.Data.lastResidueLevel`, with the character
  `New.Data.lastLevelChar`.
* `New.Data.algFormRep_lowerChain`: how block triangular elements act on the image;
  `New.Data.lowerChain_principalRep`: the chain commutes with 𝖦 = ∏ GL_r(𝔽_w) (`New.Data.chosenGL`).

Notions from other files:
* `New.Data.TameChar`: a character of U(1)(𝔸) of weight 0 with tame part supported on a finite set Q
  of places of norm prime to MN, Q disjoint from its conjugate.
* `New.algFormRep`: right translation by the finite adelic unitary group on algebraic forms of a
  given weight; the weight λ° on Y_m has column numbers `New.Data.columnsY` and determinant exponent
  `New.Data.lastEntry` m.
* `New.Data.spaceY`: the hermitian space Y_j with its lattice 𝖬_j.
* `New.Data.levelPlaces`: the chosen places above p₀, p₁ and the places of the modulus Q of ϑ.
* `New.Data.pointDatumY`: the finite datum on Hom(Y_j, Y_{j+1}), the indicator of the inclusion
  modulo the level places and the vacuum elsewhere.


### `New.blockNumber`

 The number, from 0 to j, of the block containing an index: 0 on R and l on the l-th copy of
T. 

### `New.blockNumber_eq_zero_iff`

 An index has block number 0 if and only if it lies in the image of the first block R. 

### `FormY`

 The forms on U(Y_j) of the type given by the parameter `New.Data.paramY` and the signs of Y_j,
with the Petersson product. 

### `harmonicY`

 The joint harmonic of lift j + 1: the product over the infinite places of the chosen joint
harmonics for the parameters and signs of Y_j and Y_{j+1}. The splitting character on a space of
rank n has weight ⌊n/2⌋ − w_{j+1}(τ) at τ. 

### `datumY`

 The datum φ ⊗ Υ on Hom(Y_j, Y_{j+1}) of lift j + 1: the joint harmonic at infinity and the
finite datum `New.Data.pointDatumY`. 

### `paramsCorrespond_paramY`

 For j < m the doubled parameters `New.Data.paramY` of Y_j and Y_(j+1), with their signs,
correspond (`New.ParamsCorrespond`) for the weights `New.Data.gridWeight` of the characters of lift
j + 1. 

### `isArrow_datumY`

 For j < m the datum `New.Data.datumY` ϑ j of lift j + 1 is an arrow (`New.IsArrow`: a kernel
whose lifts take forms of the source type to forms of the target type) both ways: (a) from forms on
Y_j to forms on Y_(j+1), and (b) for the swapped Weil representation, from forms of the conjugate
type on Y_(j+1) to forms of the conjugate type on Y_j. 

### `isArrow_thetaKernelY_datumY`

 For j < m the datum `New.Data.datumY` ϑ j of lift j + 1 is an arrow from forms on Y_j to forms
on Y_(j+1). 

### `isArrow_swap_thetaKernelY_datumY`

 For j < m the datum `New.Data.datumY` ϑ j of lift j + 1 is an arrow for the swapped Weil
representation, from forms of the conjugate type on Y_(j+1) to forms of the conjugate type on
Y_j. 

### `liftY`

 Lift j + 1, from forms on Y_j to forms on Y_{j+1}: the theta lift with datum `New.Data.datumY`,
multiplied by the index in K₀ of the level `New.Data.levelY`. 

### `lastResidueLevel`

 The group of reductions that cuts out the level on Y_m: the families in ∏_w GL(Y_m mod w), w
over the level places, that are 1 at the chosen places above p₀, p₁ (the left summand) and block
upper triangular at the places of Q (the right summand). 

### `mem_lastResidueLevel`

 A family lies in `New.Data.lastResidueLevel` if and only if it is 1 at the chosen places above
p₀, p₁ and block upper triangular at the places of Q. 

### `eq_one_of_mem_lastResidueLevel`

 A family in `New.Data.lastResidueLevel` is 1 at the chosen places above p₀, p₁. 

### `mem_parabolic_of_mem_lastResidueLevel`

 For a tame character ϑ, the component of a family in `New.Data.lastResidueLevel` at any level
place (a chosen place above p₀, p₁ or a place of the modulus Q of ϑ) is block upper triangular for
the blocks `New.blockNumber` of Y_m. 

### `lastLevel`

 The level J_m on the last space Y_m of the chain: the elements of K₀ = `New.stdLevel` that are 1
modulo the chosen places above p₀, p₁ and block upper triangular modulo each place of Q. 

### `lowerChainUpTo`

 The composite of the first j theta lifts along Y₀, …, Y_j for the twist ϑ, from forms of
principal level at the chosen places on Y₀ to forms on Y_j. 

### `lowerChain`

 The map ι_μ for the twist ϑ: the composite of the m lifts from forms of principal level at the
chosen places on Y₀ to forms on Y_m, read as algebraic forms of weight λ°. The subscript μ stands
for the characters μ_j⁰ϑ^j = `D.chainChar ϑ j` (1 ≤ j ≤ m) of the lifts. 

### `det_toSquareBlock_toBlocks₁₁`

 The determinants of the diagonal blocks of the upper left corner of a matrix on `j + 2` blocks
are those of its first `j + 1` diagonal blocks. 

### `det_eq_det_toBlocks₁₁_mul`

 The determinant of a block upper triangular matrix on `j + 2` blocks is that of its upper left
corner times that of its last diagonal block. 

### `formRep_liftY`

 Fix a tame character `ϑ` and assume that the datum of lift `j + 1` for `ϑ` is an arrow. Let `k`,
`k'` be integral finite points of `U(Y_(j+1))`, `U(Y_j)` with reductions `g`, `g'` at the level
places such that `g ι = ι g'` at each of them, for `ι` the matrix of the inclusion `Y_j → Y_(j+1)`.
Then the translate by `k` of the lift `liftY ϑ j z` of a form `z` is the lift of the translate of
`z` by `k'`, times the product over the level places of `ψ (det g) / ψ (det g')`, where
`ψ = chainTamePart ϑ j` is the tame part of the character of the lift. 

### `formRep_lowerChainUpTo_eq_lowerChainUpTo_smul`

 Fix a tame character `ϑ` and `j ≤ m`. Let `k` be an element of K₀ (`stdLevel`, the stabiliser of
the standard lattice) on `Y_j` (`D.spaceY j`) whose reductions `g` at the level places are block
upper triangular and have block 0 equal to `s` (in `chosenGL`) at the chosen places. Then the
translate by `k` of `lowerChainUpTo ϑ j y`, the composite of the first `j` lifts applied to `y`, is
that composite applied to `c • (s · y)`, where `s · y` is the action `principalRep`. Here `c` is the
product over the level places and `l < j` of the tame character `chainTamePart ϑ l` of lift `l + 1`
at the determinant of the diagonal block `l + 1` of `g`. 

### `algFormRep_lowerChain`

 The law of the chain ι_μ = `lowerChain ϑ` of the m lifts with characters μ_j⁰ϑ^j, for a tame
character ϑ with modulus Q. Let k ∈ K₀ on Y_m have reductions g = (g_w) at the level places w that
are block upper triangular at every w and have block 0 equal to s ∈ 𝖦 at the chosen places. Then
k·ι_μ(y) = c · ι_μ(s·y), where c is the product over all w and all l < m of the tame character
`chainTamePart ϑ l` of lift l + 1 at w, evaluated on the determinant of the diagonal block l + 1 of
g_w. 

### `lastLevelChar`

 The character of the level on Y_m: k ↦ ∏_w ∏_{l<m} ψ_{l,w}(det k_w^{(l+1)}), where w runs over
all level places (the chosen ones above p₀, p₁ and those of Q), k_w^{(l+1)} is the diagonal block
l + 1 of the component k_w (`New.blockHom`) and ψ_l = `New.Data.chainTamePart` ϑ l is the tame
character of lift l + 1. The chain of compositions reads from the right: component at w, block,
determinant, character. 

### `lowerChain_mem_levelSpace`

 Let ϑ be a tame character with modulus Q and y a form on Y₀ of principal level at the chosen
places. The level `lastLevel ϑ` consists of the k ∈ K₀ on Y_m that reduce to 1 at the chosen places
and are block upper triangular modulo the places of Q. Such a k multiplies the algebraic form
ι_μ(y) = `lowerChain ϑ y` by the value of `lastLevelChar ϑ` at the reductions (k_w) of k: the
product, over these places w and over l < m, of the tame character `chainTamePart ϑ l` of lift l + 1
at w, evaluated on the determinant of the diagonal block l + 1 of k_w. 

### `lowerChainAtLevel`

 The map ι_μ with its target restricted to the space of algebraic forms on Y_m with level J_m
(`New.Data.lastLevel`) and the character `New.Data.lastLevelChar`. 

### `firstBlockLift`

 For s in 𝖦, a chosen element of K₀ on Y_m reducing to diag(s, 1) at the chosen places above p₀,
p₁ and to 1 at Q. 

### `lowerChain_principalRep`

 For a tame character ϑ with modulus Q, the chain ι_μ = `lowerChain ϑ` of the m lifts with
characters μ_j⁰ϑ^j commutes with the group 𝖦 = `D.chosenGL`: for s in 𝖦 and a form y of principal
level on Y₀, ι_μ(s·y) is the right translate of ι_μ(y) by `firstBlockLift ϑ s`, an element of K₀ on
Y_m that reduces to diag(s, 1) at the chosen places and to 1 at Q. 
