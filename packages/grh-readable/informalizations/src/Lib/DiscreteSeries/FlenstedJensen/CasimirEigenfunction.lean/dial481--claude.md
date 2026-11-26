---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/CasimirEigenfunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/CasimirEigenfunction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/CasimirEigenfunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flensted-Jensen's integral, analyticity of c_λ and its Casimir eigenvalue

This file studies the coefficient c_λ = `New.HCParam.dsCoeff l`, with `l = 2λ`, on the group
`U(diag ε)`, where `K = U(diag ε) ∩ U(n)`. It proves that c_λ is complex analytic, so defines a
smooth function `New.HCParam.dsCoeffSmooth` in `New.SmoothU`. For a parameter with a gap
(`New.HCParam.HasGap`, assumed in all results listed below), Flensted-Jensen's integral over `K`,
which gives c_λ, does not depend on the admissible block diagonal factor, and c_λ is an
eigenfunction of the Casimir operator of `gl_n`.

## Main definitions and results

* `New.flenstedJensen_eq_of_accretive`, `New.dsCoeff_eq_flenstedJensen`: any block diagonal `a` with
  `a⁻¹ g` accretive (`Matrix.IsAccretive`: `z + zᴴ` positive definite) gives the same value. The
  integrand is a density on the flag variety of `K_ℂ`; polarization makes the integral locally
  constant, and the admissible `a` form a convex set.
* `New.flenstedJensen_eq_integral_of_eq_mul_mul_conjTranspose`,
  `New.dsCoeff_eq_integral_of_eq_mul_mul_conjTranspose`: the value as an integral over `K` for any
  splitting `g = p z qᴴ` with `p`, `q` block diagonal and `z` accretive.
* `New.DiscreteSeries.splitCoeff_triangular_mul_mul_triangular`,
  `New.DiscreteSeries.flenstedJensen_triangular_mul_mul_triangular`: block diagonal triangular
  factors, lower on the left and upper on the right, come out as characters.
* `New.casimir_dsCoeffSmooth`: the function c_λ (`New.HCParam.dsCoeffSmooth`, l = 2λ) on U(diag ε)
  is an eigenfunction of the Casimir operator Σ_{a,b} E_ab E_ba of gl_n, acting by right derivatives
  (`New.rightDeriv`), with eigenvalue `New.HCParam.casimirValue` l = |λ|² − |ρ|². Near a point c_λ
  is an average over k in K = `New.maxCompactU` of functions that are lowest weight vectors of
  weight λ + ρ (highest vectors for the roots positive for −l) in the basis k E_ab k⁻¹ of gl_n, and
  the Casimir operator does not depend on the basis.

Notions from other files:
* `New.USign`: For a vector of signs ε, the unitary group U(J) of the diagonal matrix J=diag(ε).
* `New.SmoothU`: Smooth functions on `U(diag ε)`: the restrictions of the smooth functions on all
  matrices.
* `New.HCParam.HasGap`: the entries of `l = 2λ` are distinct, of the parity of `card n - 1`, and
  those with different signs differ by at least `2h`.
* `New.blockDiagAlg ε`: the matrices that commute with `diag ε`, the block diagonal matrices.

## Relation to the literature

Known; see `Lib.DiscreteSeries.FlenstedJensen.PsiKTypes` for sources.



## Flensted-Jensen's integral and analyticity of the coefficient

Flensted-Jensen's integral `New.HCParam.flenstedJensen l a z` is the integral over
`K = U(diag ε) ∩ U(n)` of `m_Λ(a k) * conj m_Λ(k) / m_{-λ-ρ}(kᴴ z k)`, normalised by `∫ |m_Λ|²`,
where `m_w = New.weightMinors w` is a product of principal minors, `Λ = New.HCParam.lowestKType l`
and `λ + ρ = New.paramAddRho l`. The function `New.HCParam.dsCoeff l g` is its value at
`(a, a⁻¹ g)` with `a = New.blockDiagPart ε g` the block diagonal part of `g`.

For a parameter of some gap the value is the same for every block diagonal `a` with `a⁻¹ g`
accretive: these `a` form a convex set, so it is enough that the derivative in `a` vanishes. Up to
the normalising constant the integral is `I(a, 1)`, where `I = New.HCParam.splittingIntegral l g` is
analytic at each pair `(p, r)` with `r g⁻¹ p` accretive. For a parameter of some gap the integrand
of `I` is a density for the triangular subgroup of `K_ℂ`, so `I(p x, xᴴ r) = I(p, r)` for invertible
block diagonal `x`. Polarization of this invariance shows that the derivative of `I` in `p` vanishes
in the block diagonal directions.


### `twoRho_lt_twoRho`

 For an integer vector `l`, the sum `2ρ = twoRho l ⊤` of all roots that are positive for `l` has
its entries in the strict order of those of `l`. 

### `fderiv_eq_of_borel_equivariant`

 The derivative of an equivariant function in an elementary direction. Let `f` have derivative
`D` at `s`. Suppose that `f (c b) = diagChar w b * f s`, with `diagChar w b = ∏ a, b a a ^ w a`,
whenever `c b` is near `s` and `b` is block diagonal, invertible and triangular for the order
`-o`. Suppose also that `c` maps the line `1 + t • single i j 1`, where `ε i = ε j` and
`o j ≤ o i`, to the line `s + t • v`. Then `D v` is `w i * f s` if `i = j`, and `0` otherwise. 

 ### Analyticity of the coefficient 

### `isAnalyticFamily_flenstedJensen`

 Let `a` be analytic at the matrix `g` with `(a g)⁻¹ g` accretive (positive definite Hermitian
part). Then the integrand of `New.HCParam.flenstedJensen l (a x) ((a x)⁻¹ * x)`, made of the
products of principal minors `weightMinors` of weights `Λ = l.lowestKType` and `-(λ + ρ)`, is an
analytic family in `x` near `g`: it is given by an analytic function with values in `C(K, ℂ)`,
`K = maxCompactU ε` being the compact group `U(diag ε) ∩ U(n)`. 

### `HCParam.analyticAt_dsCoeff`

 For all signs ε and integer vectors l = 2λ, the function c_λ = `l.dsCoeff`, Flensted-Jensen's
integral with the block diagonal part of the matrix as factor, is complex analytic at every point
g of U(diag ε). 

 ### Dominance of the weights 

### `HCParam.HasGap.paramAddRho_lt_iff`

 For a parameter `l = 2λ` of gap `h`, the entries of `λ + ρ = paramAddRho l`, with ρ the half sum
of the roots positive for `l`, are ordered as those of `l`. 

### `HCParam.HasGap.isKDominant_neg_paramAddRho`

 For a parameter `l = 2λ` of gap `h`, the weight `-(λ + ρ)` is dominant for the order `l` with
all signs equal: its entries decrease as those of `l` increase. 

### `HCParam.HasGap.isKDominant_lowestKType`

 For a parameter l = 2λ of gap h, the weight Λ = λ+ρ−2ρ_c, with 2ρ_c the sum of the roots
e_i − e_j with ε_i = ε_j that are positive for l, is K-dominant for the order −l: Λ_j ≤ Λ_i whenever
ε_i = ε_j and l_j < l_i. 

 ### The splitting integral 

### `HCParam.splittingIntegrand`

 The function `F(y) = m_Λ(p y) · conj m_Λ(q y) / m_{λ+ρ}(yᴴ qᴴ g⁻¹ p y)`, written in `r = qᴴ`
so that it depends holomorphically on the pair `(p, r)`. Here `l = 2λ`, `Λ = l.lowestKType` and
`m_w = weightMinors w` is the product of principal minors of weight `w`. 

### `HCParam.splittingIntegral`

 The integral `I(p, r)` of `splittingIntegrand` over `K = U(diag ε) ∩ U(n)` for its Haar measure
`haarK ε` of mass one, as a function of the pair `(p, r)`, where `r` stands for `qᴴ`. 

### `flenstedJensen_eq_splittingIntegral`

 For a matrix `a` with `a⁻¹ g` accretive, Flensted-Jensen's normalised integral at `(a, a⁻¹ g)`
is the integral `I(a, 1) = l.splittingIntegral g (a, 1)` divided by
`Λ.kTypeNormSq = ∫_K |m_Λ|²`, where `Λ = l.lowestKType`. 

### `DiscreteSeries.isBorelMatrix_conjTranspose`

 The adjoint of an invertible matrix that is lower triangular for the order `o` is invertible
and upper triangular for `o`. 

### `splittingIntegrand_mul_borel`

 Let `l = 2λ` be a parameter of some gap `h` (distinct entries congruent to `card n - 1` mod 2).
Let `F = l.splittingIntegrand g p r` be the function
`F(y) = m_Λ(p y) · conj m_Λ(q y) / m_{λ+ρ}(yᴴ qᴴ g⁻¹ p y)`,
written with `r = qᴴ`, where `Λ = l.lowestKType` and `m_w` is the product of principal
minors of weight `w`. If `r g⁻¹ p` is accretive and `y` is invertible, then
`F(y b) = |b^(-2ρ_c)|² F(y)` for every invertible block diagonal `b` (commuting with diag ε) that is
upper triangular in the order of decreasing `l`, so `F` is a density. Here `2ρ_c` is the sum of the
compact positive roots (the roots e_i − e_j with `ε i = ε j` that are positive for `l`), and
`b^w = diagChar w b` is ∏ b_ii^(w_i). 

### `splittingIntegral_mul_conjTranspose_mul`

 Invariance: for a parameter `l` of gap `h`, a matrix `r g⁻¹ p` that is accretive and an
invertible block diagonal `x`, one has `I(p x, xᴴ r) = I(p, r)`, where
`I = l.splittingIntegral g` and a matrix `z` is accretive if `z + zᴴ` is positive definite. 

### `analyticAt_splittingIntegral`

 The integral `I = HCParam.splittingIntegral l g` over `K` is complex analytic at each pair
`(p, r)` for which `r g⁻¹ p` is accretive. 

### `apply_mul_zero_eq_zero_of_polarization`

 Polarization: a complex linear form on pairs that vanishes at `(p Y, Yᴴ)` for all `Y` in a
complex subspace vanishes at `(p X, 0)` for each `X` in it, since `Y ↦ Yᴴ` is antilinear. 

### `fderiv_splittingIntegral_eq_zero`

 Let `l` have gap `h`, let `p` be block diagonal for the signs and let `g⁻¹ p` be accretive.
Then the derivative at `(p, 1)` of `I = HCParam.splittingIntegral l g` vanishes at `(X, 0)` for
each block diagonal `X`. 

 ### Independence of the splitting 

### `flenstedJensen_eq_of_accretive`

 Independence of the splitting: let `l = 2λ` have gap `h` (distinct entries ≡ `card n - 1` mod 2,
`|λ i - λ j| ≥ h` when `ε i ≠ ε j`) and let `g` be any complex matrix. Then Flensted-Jensen's
integral `l.flenstedJensen a z = ∫_K m_Λ(ak) conj(m_Λ(k)) / m_{−λ−ρ}(kᴴzk) dk / ∫_K |m_Λ|²` at
`z = a⁻¹ g` is the same for all `a` commuting with `diag ε` with `a⁻¹ g` accretive (`z + zᴴ`
positive definite). 

### `dsCoeff_eq_flenstedJensen`

 Let `l = 2λ` be a parameter of some gap `m` (distinct entries of one parity, those of `λ` at
opposite signs at least `m` apart) and `g` in `U(diag ε)`. Then c_λ(g) = `l.dsCoeff g` is
Flensted-Jensen's integral at `(a, a⁻¹ g)` for any block diagonal `a` such that `a⁻¹ g` is
accretive (positive definite Hermitian part). 

### `flenstedJensen_eq_integral_of_eq_mul_mul_conjTranspose`

 Let `l = 2λ` be a parameter of gap `h` and `g = p z qᴴ` with `p`, `q` block diagonal and `z`
accretive (`z + zᴴ > 0`). For block diagonal `a` with `a⁻¹ g` accretive, Flensted-Jensen's integral
at `(a, a⁻¹ g)` is `∫_K m_Λ(p k) conj m_Λ(q k) / m_{-λ-ρ}(kᴴ z k) dk / ∫_K |m_Λ|²`, with the
products of minors `m_w = weightMinors w`, `Λ = l.lowestKType` and `λ + ρ = paramAddRho l`. For
invertible `p`, `q` one such `a` is `p q⁻¹`, so the integral depends only on the product
`p z qᴴ`. 

 ### The coefficient as a holomorphic function on the set of products 

### `splittable`

 The set of the matrices `g` for which `z = a⁻¹ g` is accretive (`z + zᴴ > 0`) for some `a` that
is block diagonal for the signs `ε`; such an `a` is invertible. These are the products `p z qᴴ` with
`p`, `q` invertible and block diagonal and `z` accretive; see `New.mem_splittable_iff`. 

### `mem_splittable_iff`

 A matrix lies in `New.splittable ε` if and only if it is a product `p z qᴴ` with `p`, `q`
invertible and block diagonal for the signs `ε` and `z` accretive. 

### `eventually_isAccretive_inv_mul`

 If `a⁻¹ g` is accretive, then so is `a⁻¹ x` for all `x` near `g`. 

### `isOpen_splittable`

 The set `splittable ε` is open in `Matrix n n ℂ`. This is the set of complex matrices `g` with
`a⁻¹ g` accretive (`z + zᴴ > 0`) for some block diagonal `a`, that is, the products `p z qᴴ` with
`p`, `q` invertible block diagonal and `z` accretive. 

### `HCParam.splitCoeff`

 The coefficient on the set `New.splittable ε` of products: Flensted-Jensen's integral at
`(a, a⁻¹ g)` for a chosen block diagonal `a` with `a⁻¹ g` accretive, and `0` off this set. 

### `splitCoeff_eq_flenstedJensen`

 For a parameter `l` of gap `h`, the coefficient `l.splitCoeff g` is Flensted-Jensen's integral
at `(a, a⁻¹ g)` for every block diagonal `a` with `a⁻¹ g` accretive. 

### `splitCoeff_mul_mul_conjTranspose`

 The coefficient at a product. Let `l = 2λ` be a parameter of gap `h`: its entries are distinct
and congruent to `card n - 1` mod 2, and `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. Let `p`, `q` be
invertible and block diagonal (commuting with `diag ε`) and `z` accretive (`z + zᴴ > 0`). Consider
`l.splitCoeff`, which at a matrix `g` with `a⁻¹ g` accretive for some block diagonal `a` is
Flensted-Jensen's integral at `(a, a⁻¹ g)` for a chosen such `a`, and is `0` elsewhere. Then
`l.splitCoeff (p z qᴴ)` is `∫_K m_Λ(p k) conj m_Λ(q k) / m_{-λ-ρ}(kᴴ z k) dk / ∫_K |m_Λ|²`; here
`K = U(diag ε) ∩ U(n)` carries its Haar measure of mass one, `m_w = weightMinors w` is the product
of principal minors of weight `w`, `Λ = l.lowestKType` and `λ + ρ = paramAddRho l`. 

### `splitCoeff_eq_dsCoeff`

 Let `l = 2λ` be a parameter of gap `h`: its entries are distinct and congruent to `card n - 1`
mod 2, and `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. Then for every `g` in `U(diag ε)`,
`l.splitCoeff g = l.dsCoeff g`. Here `splitCoeff` is Flensted-Jensen's integral at `(a, a⁻¹ g)` for
a block diagonal `a` with `a⁻¹ g` accretive (and `0` if there is none), and `dsCoeff` is
`c_λ(g) = Ξ(a, a⁻¹ g)` with `a` the block diagonal part of `g`. 

### `dsCoeff_eq_integral_of_eq_mul_mul_conjTranspose`

 The coefficient in any splitting. Let `l = 2λ` be a parameter of gap `m`: its entries are
distinct and congruent to `card n - 1` mod 2, and `|λ i - λ j| ≥ m` whenever `ε i ≠ ε j`. Let `g` in
`U(diag ε)` be a product `p z qᴴ` with `p`, `q` block diagonal (commuting with `diag ε`) and `z`
accretive (`z + zᴴ > 0`). Then `l.dsCoeff g`, the function `c_λ(g) = Ξ(a, a⁻¹g)` with `a` the block
diagonal part of `g` and `Ξ` Flensted-Jensen's normalised integral, is `∫_K m_Λ(p k) conj m_Λ(q
k) / m_{-λ-ρ}(kᴴ z k) dk / ∫_K |m_Λ|²`; here `K = U(diag ε) ∩ U(n)` carries its Haar measure of mass
one, `m_w = weightMinors w` is the product of principal minors of weight `w`, `Λ = l.lowestKType`
and `λ + ρ = paramAddRho l`. 

### `analyticOnNhd_splitCoeff`

 For a parameter `l` of gap `h`, the coefficient `l.splitCoeff` is holomorphic on the open set
`New.splittable ε` of the products `p z qᴴ` with `p`, `q` invertible and block diagonal and `z`
accretive (`z + zᴴ > 0`). On this set, `l.splitCoeff g` is Flensted-Jensen's integral at
`(a, a⁻¹ g)` for a block diagonal `a` with `a⁻¹ g` accretive. This is a corollary of the
independence of the splitting; on the group itself the later proofs use
`New.HCParam.analyticAt_dsCoeff`. 

 ## Triangular factors 

### `splitCoeff_triangular_mul_mul_triangular`

 Let `l = 2λ` be a parameter of gap `h` (in particular with distinct entries), and let `b'` and
`b` be block diagonal and invertible, with `b'` lower and `b` upper triangular in the order of
decreasing `l`. Let `c = l.splitCoeff` be Flensted-Jensen's integral at `(a, a⁻¹ g)` for a block
diagonal `a` with `a⁻¹ g` accretive, on the open set `New.splittable ε` of the products `p z qᴴ`
with `p`, `q` invertible and block diagonal and `z` accretive (`z + zᴴ > 0`). Then for `g` in this
set, `c (b' g b) = b' ^ Λ b ^ Λ c g`, where `b ^ Λ = ∏ i, b i i ^ Λ i` and `Λ = l.lowestKType` is
the highest weight of the lowest `K`-type. 

### `flenstedJensen_triangular_mul_mul_triangular`

 Let `l = 2λ` be a parameter of gap `h` (in particular with distinct entries), and
let `b'` and `b` be block diagonal and invertible, `b'` lower and `b` upper triangular in the order
of decreasing `l`. If `y` and `b' y b` are accretive (positive definite Hermitian part), then
Flensted-Jensen's coefficient `c = l.flenstedJensen 1` satisfies `c (b' y b) = b' ^ Λ b ^ Λ c y`,
where `b ^ Λ = ∏ i, b i i ^ Λ i` for the highest weight `Λ` of the lowest `K`-type. 

 ## c_λ as a smooth function on U(diag ε) 

### `New.HCParam.dsCoeffSmooth`

 The function c_λ, l = 2λ, regarded as an element of the space of smooth complex functions on
U(diag ε). 

### `New.continuous_dsCoeff`

 The function c_λ = `HCParam.dsCoeff l` is continuous on U(diag ε): its composite with any
continuous map `f : X → U(diag ε)` is continuous. Here c_λ(g) = Ξ(a, a⁻¹g), with `a` the block
diagonal part of `g` and Ξ Flensted-Jensen's normalised integral. 

 ## The Casimir eigenvalue of c_λ 

### `exists_equiv_fin_lt_iff`

 The indices can be numbered so that an injective integer vector l is strictly increasing. 

### `casimirValue_eq_casimirKValue_paramAddRho`

 For a parameter `l = 2λ` of gap `h`, the eigenvalue |λ|² − |ρ|² = `HCParam.casimirValue l` is
the value `casimirKValue` that the Casimir operator takes on a lowest weight vector of weight
`λ + ρ`, that is, a highest vector for the roots positive for `-l`, all pairs of indices counting
as compact (`compactForm`). 

### `fderiv_flenstedJensen_integrand_single`

 Let `l` have gap `h`, let `y` be in U(diag ε), `k` in K and `a⁻¹ y` accretive. Let `F`, with
values in continuous functions on K, be differentiable at `y`, and let `F x k` agree for matrices
`x` near `y` with the integrand of Flensted-Jensen's integral at `(a, a⁻¹ x)`, a quotient of
products of principal minors `weightMinors`. For `l i ≤ l j`, the derivative of `F` in the direction
`y (k E_ij k⁻¹)`, evaluated at `k`, is `(λ + ρ) i` times `F y k` if `i = j` and zero otherwise,
where λ + ρ = `paramAddRho l`. 

### `apply_casimirK_rightDeriv_of_lowest_weight`

 Let `l = 2λ` have gap `h` (distinct entries congruent to `card n - 1` mod 2, with
|λ_i − λ_j| ≥ h whenever ε_i ≠ ε_j), let `f` be a smooth function on U(diag ε) with values in `E`,
let `L` be a continuous linear form on `E` and `k` an invertible matrix. Suppose that near `g` the
function `L ∘ f` is a lowest weight vector of weight λ + ρ = `paramAddRho l` in the basis
`k E_ab k⁻¹` of gl_n, acting by right derivatives. Then the Casimir operator `casimirK 1` of gl_n
multiplies the value of `L ∘ f` at `g` by |λ|² − |ρ|² = `l.casimirValue`. 

### `casimir_dsCoeffSmooth`

 Let `l = 2λ` be a parameter of gap `h`: its entries are distinct and congruent to `card n - 1`
mod 2, and `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. Then the Casimir operator Ω = Σ_{a,b} E_ab E_ba
of gl_n, acting on smooth functions on U(diag ε) by complexified right derivatives, satisfies
Ωc_λ = (|λ|² − |ρ|²) c_λ. Here c_λ is `HCParam.dsCoeffSmooth l`, ρ is the half sum of the roots
positive for `l`, and the eigenvalue is `HCParam.casimirValue l`. The operator
`New.GlModule.casimirK` sums over the pairs with equal signs; for the constant sign vector 1 these
are all pairs, so `casimirK 1` is Ω.

This proves the Casimir eigenvalue formula of Harish-Chandra's discrete series in the case of the
explicit function c_λ on U(p,q) (Flensted-Jensen's function), for any gap. 
