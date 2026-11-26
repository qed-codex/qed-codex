---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/Defs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Harish-Chandra parameters, c_λ, deg_λ, e_λ and holomorphic discrete series

This file collects the definitions behind the discrete series of `G = New.USign ε`. A Harish-Chandra
parameter `λ` is stored as the integer vector `l = 2λ`, and the root `e_i - e_j` is positive when
`l j < l i`. The file proves elementary identities for `ρ`, `λ + ρ` and `Λ = λ + ρ - 2ρ_c`, and for
the gap condition. It then sets up Borel matrices, weights and holomorphic functions of weight `u`
for the holomorphic discrete series.

## Main definitions and results

* `New.HCParam.HasGap`, `New.HCParam.HasLargeGap`: `λ` is regular, each `λ i` lies in
  `(n - 1) / 2 + ℤ`, and entries of `λ` with opposite signs `ε` are far apart, at least by the gap.
* `New.paramAddRho`, `New.HCParam.lowestKType`, `New.HCParam.casimirValue`, `New.weylDimensionPoly`:
  `λ + ρ`, `λ + ρ - 2ρ_c`, `|λ|² - |ρ|²` and the product of the positive roots at `λ` divided by
  `∏_{i < n} i!`.
* `New.weightMinors`, `New.HCParam.flenstedJensen`, `New.HCParam.dsCoeff`: a product of principal
  minors (`New.principalMinor`), Flensted-Jensen's integral of such products over `K`, and the
  function `c_λ` that it defines.
* `New.HCParam.formalDegree`, `New.HCParam.dsKernel`: `deg_λ = (∫ |c_λ|²)⁻¹` for the measure
  `New.haarU`, and `e_λ = deg_λ * conj c_λ`.
* `New.IsPosFirstOrder`, `New.IsKDominant`, `New.HasHolGap`: the indices of sign `1` come first; a
  weight does not increase within a block; a weight jumps up by at least `γ` from the first block to
  the second.
* `New.IsHolOfWeight`: a function on a product of copies of the group extends analytically to the
  products `h * b`, `b` invertible triangular, transforming under `b` by the character of weight
  `u`; an optional second sign vector restricts `h` and `b` to block diagonal matrices.

Notions from other files:
* `New.USign`: for a vector of signs `ε`, the unitary group `U(J)` of the diagonal matrix
  `J = New.signMatrix ε` with entries `ε i`.
* `New.principalMinor`: the determinant of the square submatrix on the indices with a given
  property.
* `New.haarU`: a measure on `U(J)` obtained from Lebesgue measure by a Cayley chart; a Haar measure
  for a hermitian involution `J`.

## Relation to the literature

The definitions are part of three known results, each treated in another file:
* Flensted-Jensen's function as the coefficient of the lowest K-type of a discrete series, in
  `Lib.DiscreteSeries.FlenstedJensen.PsiKTypes`;
* the lowest K-type and the Casimir value determine a discrete series coefficient, in
  `Lib.DiscreteSeries.Rigidity.HighestVectorsAndFiltration`;
* the highest coefficient of a holomorphic discrete series and its reproducing property, in
  `Lib.DiscreteSeries.Holomorphic.HighestVectorExtension`.



## Harish-Chandra parameters, discrete series coefficients, formal degrees

* `New.maxCompactU`, `New.haarK`: the subgroup `K = G ∩ U(n)` and its Haar measure of mass one.


 ### The Lie algebra and the exponential map 

### `unitaryLie`

 The Lie algebra of `U(J)`: the real vector space of complex matrices `X` with
`Xᴴ * J + J * X = 0`. 

### `expU`

 For `X` with `Xᴴ * J + J * X = 0`, the matrix exponential of `X` as an element of the group
`U(J)`. 

 ### Parameters and weights 

### `weightMinors`

 The product over all integers `t` of the principal minor of `g` on `{i | t ≤ l i}`, each factor
with `t ≤ 0` divided by `det g`. For invertible `g` almost all factors are `1`. For a dominant
weight `l` it is the coefficient of a highest vector of weight `l`. 

### `gapThreshold`

 The gap `500 n³ + A`, where `n` is the number of indices. 

### `twoRho`

 The vector with i-th entry #{j : r(i,j), l_j < l_i} − #{j : r(i,j), l_i < l_j}: the sum of
those roots e_i − e_j selected by r that are positive for l, when r is symmetric. 

### `paramAddRho`

 The integer vector with entries (l_i + 2ρ_i)/2 rounded down, ρ the half sum of roots
positive for l; it is λ+ρ for a parameter l = 2λ. 

### `weylDimensionPoly`

 The product of `λ i - λ j` over the pairs with `λ j < λ i`, divided by `∏_{i < card n} i!`, for
`l = 2λ`. 

 ### The compact subgroup 

### `maxCompactU`

 The subgroup U(diag ε)∩U(n) of U(diag ε), consisting of the elements that are unitary
matrices. 

### `haarK`

 The Haar measure of total mass one on the compact group K=U(diag ε)∩U(n). 

 ### Block diagonal parts, parameters and discrete series coefficients 

### `entryMask`

 The continuous linear map that keeps the entries `(i, j)` of a matrix with `r i j` and puts `0`
elsewhere. 

### `blockDiagPart`

 For signs ε, the continuous linear map that keeps the entries (i, j) of a matrix with ε_i=ε_j
and puts zero elsewhere. 

### `HCParam`

 Integer vectors indexed by n, attached to the signs ε; they serve as doubled Harish-Chandra
parameters l = 2λ and as integral weights of U(diag ε). 

### `toHCParam`

 The integer vector l, regarded as a doubled parameter or weight for the signs ε. 

### `compactForm`

 The same integer vector l, regarded for the signs all equal to 1, that is for the compact
group U(n). 

### `kTypeNormSq`

 The integral ∫_K |m_l(k)|² dk over K = U(diag ε)∩U(n) with total mass one, where
m_l = `New.weightMinors l` is the product of principal minors of weight l. 

### `HasGap`

 The vector `l = 2λ` is a parameter of gap `h`: its entries are distinct and congruent to
`card n - 1` mod 2, and `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. 

### `HasGap.injective`

 The entries of `l = 2λ` are distinct. 

### `HasGap.parity`

 Each entry of `l` has the parity of `card n - 1`, that is, `λ i ∈ (card n - 1) / 2 + ℤ`. 

### `HasGap.gap`

 Entries of `λ` with different signs `ε` are at least `h` apart. 

### `HasLargeGap`

 The vector `l = 2λ` is a parameter for the signs `ε` with gap `500 n³ + A`. 

### `lowestKType`

 The integer vector `paramAddRho l - 2ρ_c`, where `2ρ_c` is the sum of the compact roots
(`ε i = ε j`) that are positive for `l`. For a parameter `l = 2λ` it is `Λ = λ + ρ - 2ρ_c`, the
highest weight of the lowest K-type. 

### `casimirValue`

 For l = 2λ, the real number κ_λ = |λ|² − |ρ|², ρ the half sum of the roots positive for l. 

### `flenstedJensen`

 Flensted-Jensen's integral ∫_K m_Λ(gk) conj(m_Λ(k)) / m_{−λ−ρ}(kᴴzk) dk divided by
∫_K |m_Λ|², for l = 2λ, Λ = λ+ρ−2ρ_c and m_w = `New.weightMinors w`. For a parameter l the
factor 1 / ∫_K |m_Λ|² is, by Schur's relations, the dimension of the K-type Λ. 

### `dsCoeff`

 The function c_λ(g) = Ξ(a, a⁻¹g) of a complex matrix g, with a the block diagonal part of g
and Ξ the normalised integral `New.HCParam.flenstedJensen`. On U(diag ε), for a parameter with a
gap, every splitting g = pzqᴴ with p, q block diagonal and z accretive gives the same value
(`New.dsCoeff_eq_integral_of_eq_mul_mul_conjTranspose`). 

### `formalDegree`

 For signs ε and l=2λ, the reciprocal of the integral of |c_λ|² over U(diag ε) for the
measure `New.haarU`, which is the `volume` of that group. 

### `dsKernel`

 The complex function on U(diag ε) given by deg_λ times the complex conjugate of c_λ(g), for
l=2λ. 

 ### Counting negative signs 

### `negCount`

 The number of indices `i` with sign `a i = -1`. It is additive over `a ⊕ᵥ b`, the sign vector
`Sum.elim a b` on `α ⊕ β` (`New.Exchange.negCount_sumElim`). 

### `_root_.New.exists_equiv_comp_eq_of_negCount_eq`

 Sign vectors on index types of the same size with equally many negative signs (`negCount`, the
number of entries `-1`) differ by a bijection of the indices. 


## Arithmetic of ρ, λ + ρ, Λ and the gap condition

Elementary facts about `ρ`, and, for a Harish-Chandra parameter `l = 2λ` with signs `ε i = ±1`
(`New.HCParam.HasGap`: distinct entries `≡ n - 1` mod 2, and `|l i - l j| ≥ 2h` whenever
`ε i ≠ ε j`), about `λ + ρ` and `Λ = New.HCParam.lowestKType l`.


### `abs_twoRho_le`

 Every entry of `New.twoRho l r`, a difference of two numbers of indices, has absolute value at
most the number of all indices. 

### `twoRho_neg`

 The vector `New.twoRho l r`, whose `i`-th entry counts the `j` related to `i` by `r` with
`l j < l i` minus those with `l i < l j`, changes sign with `l`. 

### `card_lt_add_card_gt_add_one`

 For injective `l`, the number of indices `j` with `l j < l i`, plus the number of those with
`l i < l j`, plus one for `i` itself, is the number of all indices. 

### `two_mul_paramAddRho`

 `2(λ + ρ) = l + 2ρ`, where `2ρ = New.twoRho l ⊤` is the sum of the roots positive for `l`: for a
parameter `l = 2λ` of some gap (distinct entries congruent to `n - 1` mod 2) the division by 2 in
`New.paramAddRho l` is exact. 

### `two_mul_lowestKType`

 For a parameter `l = 2λ` of some gap `h` (distinct entries congruent to `n - 1` mod 2, those at
indices with different signs `ε` at least `2h` apart), twice
`Λ = New.HCParam.lowestKType l` is `l + 2ρ_n - 2ρ_c`. Here `ρ_n` and `ρ_c` are the half sums of
the roots `e_i - e_j` with `l j < l i` and with `ε i ≠ ε j`, respectively `ε i = ε j`, and
`New.twoRho l r` is the sum of those roots for the relation `r`. 

### `abs_lowestKType_le`

 If `l = 2λ` is a parameter of gap `h` for the signs `ε` (distinct entries congruent to `n - 1`
mod 2, those at indices with different signs at least `2h` apart) and `|l a| ≤ L` for all `a`,
then every entry of `Λ = New.HCParam.lowestKType l`, the vector `λ + ρ - 2ρ_c`, satisfies
`|Λ a| ≤ L + n`, where `n` is the number of indices. 

### `HCParam.HasGap.signs_one`

 If l = 2λ is a parameter of gap h for the signs ε (distinct entries congruent to n − 1 mod 2,
those at indices with different signs at least 2h apart), then `l.compactForm`, the same vector
for the constant signs +1 (that is, for the compact group U(n)), is a parameter of gap h as
well. 


## Borel matrices, K-dominance and holomorphic functions of weight u

An integer vector `o`, usually injective, orders the indices; weights are integer vectors.

* `New.IsBorelMatrix`, `New.diagChar`, `New.blockDiagAlg`, `New.diagTorus`: the matrices of the
  Borel subgroup for `o`, their characters, the algebra of block diagonal matrices and the map
  from tuples in the circle to diagonal elements of the group.


### `diagChar`

 For an integer vector w and a complex square matrix b, the product over i of the diagonal
entries b_ii raised to the power w_i. 

### `IsBorelMatrix`

 The matrix b is invertible and block upper triangular for o: b_ij = 0 whenever o_j < o_i. For
injective o it is upper triangular in the order given by o. 

### `IsKDominant`

 The weight w is K-dominant for the order o: w_j ≤ w_i whenever ε_i = ε_j and o_i < o_j. 

### `IsPosFirstOrder`

 The order o has distinct values and puts every index of sign +1 before every index of sign
−1. 

### `HasHolGap`

 The condition on signs ε, integer vector w and natural number γ that w_i + γ ≤ w_j whenever
ε_i = +1 and ε_j = −1. 

### `blockDiagAlg`

 The algebra of complex matrices commuting with diag(ε), that is the block diagonal matrices
for the signs ε. 

### `IsHolOfWeight`

 F on U(diag ε)^Φ is holomorphic of weight u: some function F' of tuples of matrices is analytic
at all products hb, with F'(hb) = ∏_τ `New.diagChar` (u τ) (b τ) · F(h). Here h is in the group, b
is invertible and o-triangular, and both commute with diag(ε'), which is no condition for the
default ε' = 1. 

### `holMinors`

 For signs ε, weight w and matrix b, the quotient m_{w+c}(b)/m_c(b) of products of
principal minors m = `New.weightMinors`, where c_i = 2∑|w_j| if ε_i = +1 and c_i = 0 otherwise. 

### `holMinorsPi`

 For weights u_τ and a tuple h in U(diag ε)^Φ, the product over τ of the quotients of minors
`New.holMinors` of weight u_τ at h_τ. 

### `diagTorus`

 For a tuple t of complex numbers of modulus one, the diagonal matrix diag(t) as an element
of U(diag ε). 
