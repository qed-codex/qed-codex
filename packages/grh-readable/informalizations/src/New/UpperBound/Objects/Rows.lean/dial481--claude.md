---
{
  "module": "src/New/UpperBound/Objects/Rows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spaces Y_j and W_j, the forms on them, and the target parameter

This file treats the hermitian spaces Y_j and W_j and the forms on them, for admissible data
`New.Data` and a tame character ϑ with modulus Q. The chosen places are the prime divisors of
`New.Data.piM`, written π̄₀π̄₁ as one symbol, with conjugate `New.Data.piMBar` written π₀π₁. These
are one half of the places above M = p₀p₁, and N = ππ̄ is the level. The target parameter ς
(`New.Data.targetParameter`) is a staircase whose lower steps are at least the gap h = 2h₂ apart, so
the spaces of forms `New.Data.principalForms` are finite-dimensional. This file also sets up the
levels and Weil representation data along the spaces Y_j, the gaps of the target parameter, and the
Harish-Chandra parameters on the descent pairs (W_j, V_j).

## Main definitions and results

* `New.Data.spaceY`: the spaces Y_j with their lattices; `New.Data.spaceW`: the diagonal spaces W_j.
* `New.Data.goodForms`: the image of the idempotent e₀ on forms of principal level at the chosen
  places.
* `New.Data.isCuspKernel_typeKernel_paramW`: for signs such that entries of ς at indices of opposite
  sign differ by at least h, the kernel of this parameter (`New.Data.paramW` = 2ς) is a cusp kernel
  of order h₂.
* `New.Data.paramsCorrespond_descentPair`, `New.Data.fitsParams_descentPair`: the parameters on W_j
  and V_j correspond, by insertion of the block of the centre −w_j, and the descent pair (W_j, V_j)
  satisfies `New.DescentPair.FitsParams`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.Data.TameChar`: a character of U(1)(𝔸) of weight 0 with tame part supported on a finite set Q
  of places of norm prime to MN, Q disjoint from its conjugate.
* `New.Data.liftWeight`: the weight w_j = κ(σ) + j·h + h₂ at the infinite place σ, with
  κ = `New.Data.weight`, h the gap and h₂ half the gap.


### `New.Shape.besselIndexEquiv`

 The bijection from κ plus a string of length 2ϱ + 1 to the basis indices
`New.Shape.BesselIndex`: κ goes to the x_i, and the string index a goes to e_a if a < ϱ, to z if
a = ϱ and to e*_{2ϱ−a} if a > ϱ (e and e* numbered from 0). 

 ### Sizes and places 

### `instance {u : Bool} : D.HasLogBound u D.ϱ (D.logX / 2 + (if u then 2 else -4))`

 The number ϱ lies between m/4 and m, so that `exp (logX / 2 - 4) ≤ ϱ ≤ exp (logX / 2 + 2)`;
`u` chooses between the upper and the lower bound. 

### `normQ_mem_and_notMem_of_mem_Q`

 A place w of the modulus Q of ϑ, or the conjugate of one, divides the product `ϑ.normQ` of
the norms of the places of Q, and divides neither π̄₀π̄₁ (`D.piM`) nor the level N. 

### `levelPlaces`

 The system of places (`New.LevelPlaces`) formed by the chosen places above p₀, p₁ and the places
of the modulus Q of ϑ. 

### `twistModulus`

 The modulus `ϖ^c Q` if `b` is `true` (the default) and `ϖ^c` if `b` is `false`. Here `ϖ` is the
product of the chosen places above p₀, p₁, and `Q` is the product of the places of the modulus of
`ϑ` (`New.LevelPlaces.levelModulus`). 

### `nonempty_modulus_places`

 For `c ≠ 0` some place divides the modulus `D.twistModulus ϑ c b`, which is `ϖ^c Q` or `ϖ^c`
with `ϖ` the product of the chosen places. 

 ### Ideles, lattices and spaces 

### `chosenIdele`

 A finite idele that generates the ideal `(π̄₀ π̄₁)` and is `1` away from the chosen places;
see `valued_chosenIdele` and `chosenIdele_apply_of_not_isChosen`. The ideal is a modulus because
the conjugate of a chosen place is not chosen. 

### `valued_chosenIdele`

 The order of `chosenIdele` at `w` is the multiplicity of `w` in the ideal `(π̄₀ π̄₁)`, where
`π̄₀ π̄₁` is `D.piM`. 

### `ideleA`

 The finite idele α/β, with α the idele of the Weil data (`New.WeilData`) and β the
conjugate of `chosenIdele`, which generates the ideal (π₀π₁); it generates the fractional ideal
𝔞 = 𝔞₀/π₀π₁, where 𝔞₀ is the ideal of α. 

### `piNIdele`

 The principal finite idele of E given by the nonzero element π. 

### `isSplitSquarefree_piNIdele`

 The principal idele of `π` satisfies `N = π π̄`, is a uniformiser at the places `D.piNPlaces`
that divide `π` and a unit elsewhere, and no place of `D.piNPlaces` has its conjugate there. 

### `latticeScale`

 For index j, the finite idele (a/ā) raised to ⌈(m−j)/2⌉, exponent zero for j ≥ m, where a is
the idele `New.Data.ideleA`. 

### `indexEquivY`

 For j < m, a bijection from the indices of X_j plus 2ϱ + 1 − j string indices to those of Y_j:
`New.Shape.besselIndexEquiv` for j = 0, an arbitrary one (the two sides have the same number of
elements) otherwise. 

### `exists_space_isStd_of_le_and_gram_eq_of_lt`

 There is a hermitian space with the signs of `Y_j` that is standard for `D.m ≤ j` and that, for
`j < D.m`, has the Gram matrix `gradedGram` (identity on `X_j`, antidiagonal on the string) and, up
to an integral change of basis that is trivial at the chosen places, the lattice basis
`gradedLatticeBasis`. The lattice basis of `V` is the finite part `V.xFin` of its point. 

### `spaceY`

 The hermitian space `Y_j` with its lattice `𝖬_j`, chosen as in
`exists_space_isStd_of_le_and_gram_eq_of_lt`. Its properties are `isStd_spaceY_of_le`,
`spaceY_gram_eq` and `exists_spaceY_xFin_eq`. 

### `isStd_spaceY_of_le`

 For `D.m ≤ j` the space `Y_j` is standard: all its signs are `1` and its point is `1`. 

### `spaceY_gram_eq`

 For `j < D.m` the Gram matrix of `Y_j` is `gradedGram`: the identity on `X_j` and antidiagonal
on a string of `2 ϱ + 1 - j` further vectors, with entries `1` except for `-N` at the middle vector
if there is one. 

### `exists_spaceY_xFin_eq`

 For `j < D.m` the lattice basis `xFin` of `Y_j` is `gradedLatticeBasis` times a matrix `k` in
`intGL`, invertible over the integral finite adeles `Ô`, whose reduction (`reduceAt`) at each chosen
place is `1`. 

### `isStd_spaceY_last`

 The last space Y_m is standard: all its signs are +1 and its point is 1. 

### `spaceW`

 For index j, the diagonal hermitian space W_j of rank r over E whose diagonal entries are the
signs `D.signsW j`. 

 ### Forms and descent pairs 

### `principalForms`

 The forms on V of parameter ς (`New.Data.paramW` is 2ς) that are fixed by the principal level
`levelOf D.chosenPlace ⊥` at the chosen places above p₀, p₁. The character is the trivial one,
written as a composite with the reduction map of the level. 

### `principalRep`

 The complex representation of 𝖦 = ∏ GL_r(𝔽_w), over the chosen places w, on the forms on V of
principal level: an element acts through an integral lift with the given reductions. 

### `goodForms`

 The good forms on V: the image of the idempotent e₀ of ℂ[𝖦] acting on forms of principal
level at the chosen places above p₀, p₁. 

### `targetForms`

 The target forms: the good forms (`New.Data.goodForms`) on the space Y₀. 

### `targetDim`

 The complex dimension of the space of target forms (`New.Data.targetForms`), the good forms on
Y₀. 

### `descentPair`

 The j-th descent pair (`New.DescentPair`) for ϑ: W = W_j of rank r, V = I_{r+t}, the character
μ_j⁰ϑ of weight −w_j, and the places `New.Data.levelPlaces`. The basis vectors of sign + are
numbered by `New.Data.basisNumber`, those of sign − in the reverse order. Let ς_τ denote the target
parameter `New.Data.targetParameter`. The column count `colsPlus` at height i (the bound variable
`gap` below) is the positive part of ς_τ(i − 1) − max(ς_τ(i), (t − 1)/2 − w_j(τ)) − 1. The column
count `colsMinus` at height i is the positive part of
min(ς_τ(r − i − 1), −w_j(τ) − (t − 1)/2) − ς_τ(r − i) − 1. 


## Levels and Weil representation data along the chain of spaces

* `New.Data.levelY`: the integral points of `U(Y_j)` that reduce to 1 at all level places
  `New.Data.levelPlaces` (the chosen places above p₀p₁ and those of Q).
* `New.Data.LevelReductionsY`: the group of families of reductions at the level places.
* `New.Data.pointDatumY`: the datum named by the indicator of the inclusion `Y_j → Y_{j+1}` modulo
  the level places `New.Data.levelPlaces`.


### `inclY`

 The inclusion of the basis index set of Y_j in that of Y_{j+1} as the first summand. 

### `liftTamePart_eq_of_mem_Q`

 At a place w of the modulus Q of ϑ the character `D.liftTamePart ϑ j w` = ω_w^j ψ_w equals the
tame part ψ_w = `ϑ.tamePart w` of ϑ, since w is not chosen and ω = `D.chiMLocal` is trivial at such
places. 

### `levelY`

 The subgroup of the lattice stabiliser K₀ for Y_j of elements reducing to 1 at every level
place: the chosen places and the places of the modulus Q of ϑ. 

### `levelY_le_chosenLevel`

 The group `levelY ϑ j` is contained in `D.chosenLevel`, that is, its elements reduce to 1 at the
chosen places. 

### `LevelReductionsY`

 The group ∏_w GL(Y_j mod w) of families of invertible matrices indexed by the basis of Y_j, one
over the residue field of each level place w: the chosen places (the left summand of the index set)
and the places of the modulus Q of ϑ (the right summand). The reductions of an integral point of
U(Y_j) at the level places form such a family. 

### `pointDatumY`

 The datum `Υ_{j+1}` on `Hom(Y_j, Y_{j+1})`: at the level places (the chosen places and those of
`ϑ.Q`) it is the indicator function of the inclusion matrix modulo their product, and at the other
finite places it is the vacuum (`New.vacuumDatum`). 

### `thetaKernelY`

 The Weil representation of U(Y_j) × U(Y_{j+1}) on data on Hom(Y_j, Y_{j+1}), with splitting
characters νυ^⌊n/2⌋ for the two ranks n, ν = μ⁰_{j+1}ϑ^{j+1}. 

### `chainTamePart`

 The tame part of the character μ⁰_{j+1}ϑ^{j+1} of lift j + 1, a family of characters of the
residue fields. 

### `thetaKernelY_omega_pointDatumY_eq_smul`

 Let `k`, `k'` be integral finite points of `U(Y_j)`, `U(Y_{j+1})` with reductions `g`, `g'` at
the level places. Assume `g' ι = ι g` at each of them, where `ι = inclMatrix _ (D.inclY j)` is the
matrix of the inclusion `Y_j → Y_{j+1}`, so that `g' ι` is the submatrix of the columns of `g'`
indexed by `Y_j`. Then in the Weil representation `New.Data.thetaKernelY` the pair `(k, k')`
multiplies the datum `New.Data.pointDatumY` by the product over the level places of
`ψ (det g') / ψ (det g)`, for `ψ` the tame character `New.Data.chainTamePart`. 


## Gaps of the target parameter and finiteness of spaces of forms

* `New.Data.hasGap_signsY_paramW`, `New.Data.hasGap_paramW`: for the signs of Y₀ and of W_j, entries
  of ς at indices of opposite sign differ by at least h (`New.HCParam.HasGap`).


### `hasGap_signsY_paramW`

 At each infinite place, the doubled target parameter 2ς is a parameter of gap h for the signs
`New.Data.signsY` of Y₀. 

### `hasGap_paramW`

 At each infinite place, the doubled target parameter 2ς is a parameter of gap h for the signs
`New.Data.signsW` of W_j. 

### `isCuspKernel_typeKernel_paramW`

 If at each infinite place `v` the doubled parameter `D.paramW v` (twice the target parameter)
has gap `D.gap` for the signs `s`, then the product kernel `typeKernel D.paramW s` is a cusp kernel
of order `D.halfGap`, half the gap. 

### `instance {V : Space D.E D.RowIndex s} : Module.Finite ℂ (D.principalForms V)`

 If at each infinite place 2ς is a parameter of gap h for the signs s of V, the forms on V of
parameter ς and principal level at the chosen places make up a finite-dimensional space. 


## Harish-Chandra parameters on the seesaw spaces and descent pairs

* `New.Data.isHCParam_paramY`: the parameters on Y_m are those of the weight of the algebraic forms
  on this space.

Parameters are doubled so as to be integers.


### `card_Y_le`

 For `j ≤ m` the rank of `Y_j` is at most `n_m = k + m (t + 1)`. 

### `isHCParam_paramY`

 The doubled parameter `D.paramY D.m` of `Y_m` lists, in some order, the entries of twice the
Harish-Chandra parameter λ + ρ of the weight λ with column numbers `D.columnsY` and determinant
exponent `D.lastEntry D.m`. 

### `card_filter_basisNumber`

 If q singles out the basis indices whose number lies in [a, b), and b ≤ r, there are b − a of
them (natural subtraction). 

### `paramW_lt_iff`

 At `τ`, the doubled parameter 2ς = `D.paramW τ` is strictly decreasing in the basis number:
`D.paramW τ a < D.paramW τ b` exactly when `D.basisNumber b < D.basisNumber a`. 

### `negCount_signsW`

 For 1 ≤ j ≤ m, the space W_j has exactly m − j minus signs. 

### `sum_Ioo_posRank_columnCount_descentPair`

 Let `ϑ` be a tame character, `τ` an infinite place and `1 ≤ j ≤ m`. The weight at `τ` of the
forms on the space `V_j` of the `j`-th descent pair, of rank `r + t = card (D.RowIndex ⊕ Fin D.t)`,
has `columnCount τ i = colsPlus τ i + colsMinus τ (r + t - i)` columns of height `i`. The number of
columns of height `i` with `D.posRank j < i < r + t`, where `D.posRank j = k + j - 1` is the number
of plus signs of `W_j`, is the sum of `colsMinus τ i` over `1 ≤ i < r + t`. 

### `hcParameter_descentPair`

 Let `ϑ` be a tame character, `τ` an infinite place, `j` a lift index and `p < r + t`. At `τ`,
entry `p` of twice the Harish-Chandra parameter (`hcParameter`) of the weight of forms on
`V = I_{r+t}` of the `j`-th descent pair `D.descentPair ϑ j` is `r - 2 a + 2 ℓ`. With
`a = D.posRank j`, `ς = D.targetParameter τ` and `w = D.liftWeight j τ`:
* `ℓ = ς_p + w` for `p < a`;
* `ℓ = ⌊t / 2⌋ - (p - a)` for `a ≤ p < a + t`;
* `ℓ = ς_{p - t} + w` for `a + t ≤ p`. 

### `descentCentres`

 The system of centres (`New.CentreSystem`) at τ for the j-th descent pair: its stem is the
doubled target parameter {2ς_p : p < r}, and its only centre is the down centre `.inr (j - 1)`, at
−w_j and with a block of length t. 

### `descentCentres_centre`

 The value of the centre `.inr (j - 1)` of `D.descentCentres τ j` is `-D.liftWeight j τ`, minus
the weight at `τ` of the character of the `j`-th lift. 

### `sign_descentCentres`

 When the block of the only centre of `New.Data.descentCentres` is present, every entry has the
sign +. 

### `isParam_paramW`

 The doubled parameter `D.paramW τ` (2ς on W_j), with signs `D.signsW j` and read as a vector by
`toHCParam`, is a parameter of the centre system `D.descentCentres τ j` with no block (∅) and global
sign 1. Its entries are those of the stem {2ς_p : p < r}, and the sign is − exactly at the entries
below −2w_j, with w_j = `D.liftWeight j τ`. 

### `hcParameter_descentPair_sub`

 For p < r + t: entry p of the doubled parameter `hcParameter` of `D.descentPair ϑ j` at τ, in
decreasing order, lowered by 2u − 1 for u = m − j + w_j − (r − 1)/2. With a = `D.posRank j` and
ς = `D.targetParameter τ`, the entries are: first 2ς_p for p < a, then the t entries
2(−w_j) + t − 1 − 2(p − a) (the doubled block of length t centred at −w_j), then 2ς_(p−t). 

### `isParam_paramV`

 Let ϑ be a tame character, τ an infinite place, 1 ≤ j ≤ m, w_j = `D.liftWeight j τ` and
u = m − j + w_j − ⌊r/2⌋. Let l = `paramV τ` − 2u, where `paramV τ` is twice the Harish-Chandra
parameter at τ on the positive definite space V_j of rank r + t of the j-th descent pair. The system
`New.Data.descentCentres` has the stem {2ς_p : p < r}, with ς = `D.targetParameter τ`, and one
centre, with index `.inr (j - 1)`, value −w_j and block {−2w_j + t − 1 − 2b : b < t}. Then l is the
parameter of this system with the block present and common sign 1: the ranks agree, the numbers l
x + 1 are the entries of the stem and of the block, and each of them has the sign +. 

### `paramsCorrespond_descentPair`

 Let `ϑ` be a tame character and 1 ≤ j ≤ m. The doubled parameter 2ς = `D.paramW` on W_j (signs
`D.signsW j`) and the doubled parameter `paramV` of the j-th descent pair `D.descentPair ϑ j` on V_j
(all signs +) correspond: at every infinite place τ they satisfy the block rule `New.IsBlockRule`
for two weights. The first is the number `negCount (D.signsW j)` of minus signs of W_j, which is
m − j (`negCount_signsW`). The second is ⌊(r + t)/2⌋ − w_j(τ). 

### `fitsParams_descentPair`

 The doubled parameter 2ς = `D.paramW` on W_j fits the j-th descent pair (W_j, V_j), that is:
* it corresponds to the doubled parameter `paramV` on V_j;
* at every infinite place, `numbering c` is the position, counted from 0, of the basis vector c of
  W_j among those of its sign, ordered by decreasing ς for the sign + and increasing ς for −;
* `colsPlus τ i` vanishes if i exceeds the number of basis vectors of sign +, and `colsMinus τ i`
  vanishes if i exceeds the number of basis vectors of sign −. 
