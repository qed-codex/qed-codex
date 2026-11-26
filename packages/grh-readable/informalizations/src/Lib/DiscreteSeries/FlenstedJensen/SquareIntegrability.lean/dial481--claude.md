---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decay, tail bounds and the L² model of the discrete series coefficient c_λ

Let `G = New.USign ε` be the unitary group of `diag ε`, let `l = 2λ` be a parameter, and let
`c_λ = New.HCParam.dsCoeff l` be its discrete series matrix coefficient. Norms of matrices are
operator norms on Euclidean space, and `a_g = New.blockDiagPart ε g` is the block diagonal part of
`g`. When `l` has gap `h`, Fischer's inequality gives `|c_λ(g)|² |det a_g|^h ≤ 1`, and the lower
bound `(‖g‖/2)² ≤ |det a_g|` turns this into polynomial decay of `c_λ`. The decay yields the
realisation of the module `U(𝔤)c_λ` in `L²(G)`. The file also gives explicit Lipschitz and tail
estimates for `l` with a big gap (`New.HCParam.HasLargeGap`) and entries bounded by `L`. Their
constants are polynomial in `L`.

## Main definitions and results

* `New.DiscreteSeries.norm_dsCoeff_le_pow`: if `l` has gap `h` (`New.HCParam.HasGap`) and `n` is
  nonempty, then |c_λ(g)| ≤ (2/‖g‖)^c for natural numbers c ≤ h.
* `New.HCParam.DsModule`, `New.HCParam.dsAction`, `New.HCParam.dsGenerator`: the module, its
  `gl n`-action by right derivatives, and its generator, which is `K`-highest by
  `New.isKHighest_dsGenerator`.
* `New.exists_smear_dsCoeffSmooth_eq`: every element of the module is an average
  ∫ α(y⁻¹) c_λ(g y) dy against a bump function α (a smearing of c_λ). This gives the decay bound
  `New.HCParam.HasLargeGap.exists_decay_bound`.
* `New.dsCoeff_schur_orthogonality`: Schur's product formula with the formal degree
  `New.HCParam.formalDegree`.
* `New.HCParam.HasLargeGap.toL2`: the embedding in `L²(G)`. The action is the derivative of right
  translation (`New.HCParam.HasLargeGap.isDerivedAction_toL2`), and each function is its own matrix
  coefficient against the generator
  (`New.HCParam.HasLargeGap.inner_toL2_dsGenerator_rightRegularL2`).
* `New.HCParam.HasLargeGap.isUnitaryCasimirGe`: the induced inner product is invariant, and the
  Casimir operator is at least `New.HCParam.casimirValue l`.

Notions from other files:
* `New.HCParam.IsKHighest`: a vector x of a gl_n-module is K-highest of weight ν if each E_aa acts
  on it by ν_a and the compact raising operators kill it.
* `New.HCParam.dsCoeff`: the function c_λ(g) = Ξ(a, a⁻¹g) of a complex matrix g, with a the block
  diagonal part of g and Ξ the normalised integral `New.HCParam.flenstedJensen`.
* `New.HCParam.HasGap`: the entries of `l = 2λ` are distinct and congruent to `n − 1` mod 2, and
  `|λ_i − λ_j| ≥ h` whenever `ε_i ≠ ε_j`.
* `New.HCParam.formalDegree`: for signs ε and l = 2λ, the reciprocal of the integral of |c_λ|² over
  U(diag ε) for the Haar measure normalised by the compact dual.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Rigidity.HighestVectorsAndFiltration`,
`Lib.DiscreteSeries.FlenstedJensen.PsiKTypes` and `Lib.DiscreteSeries.CuspKernel` for sources.


 ## Right translation on L²(U(diag ε)) as a unitary representation 

### `New.rightRegularL2`

 The action of U(diag ε) by right translation on the space of complex-valued L² functions on
U(diag ε), as a homomorphism to bounded operators. 

### `New.isUnitaryRep_rightRegularL2`

 Right translation on L²(U(diag ε)) is a unitary representation: it is strongly continuous, the
inner product is a hermitian, positive definite invariant form, and the operator norms are bounded
(growth exponent `A = 0`). 


## The determinant of the block diagonal part a_g

* `New.norm_det_blockDiagPart`: `|det a_g|` is the square of the absolute value of the minor on the
  indices of either sign; so the principal minor of g ∈ U(diag ε) on {i | ε i = σ}, for either sign
  σ, is nonzero (`New.U.principalMinor_sign_ne_zero`).


### `norm_det_blockDiagPart`

 For `g` in `U(diag ε)` and either sign `σ`, the determinant of the block diagonal part of `g`
(its entries `g i j` with `ε i = ε j`, zero elsewhere) has absolute value the square of that of the
principal minor of `g` on `{i | ε i = σ}` (the determinant of the submatrix on these indices). 

### `sq_le_norm_det_blockDiagPart`

 For `g` in `U(diag ε)`, the determinant of the block diagonal part of `g` has absolute value at
least `(‖g‖ / 2)²`, where `‖g‖` is the L² operator norm. 


## Decay bounds for c_λ

* `New.norm_dsCoeff_sq_mul_det_pow_le_one`: if `l` has gap `h` (`New.HCParam.HasGap`), then
  |c_λ(g)|² · |det a_g|^c ≤ 1 for natural numbers c ≤ h.


### `weightMinors_pos`

 For a positive definite matrix z and an integer vector w, the product `weightMinors w z` of
principal minors of z (divided by powers of det z) is positive. 

### `norm_principalMinor_blockDiagPart_le`

 Let `g` in U(diag ε) be positive definite with positive definite block diagonal part `a`, and
let `μ ≤ v` be integer vectors such that, for an integer `t`, the indices `i` with `μ i < t ≤ v i`
all have the same sign. Then |Δ_{t≤v}(a)| ≤ |Δ_{t≤μ}(a)| · |Δ_{t≤μ}(g)| · |Δ_{v<t}(g)|, where Δ is
the principal minor on the indicated indices. 

### `norm_det_blockDiagPart_pow_le`

 Let `l = 2λ` be a parameter of gap h (entries distinct and congruent to `card n - 1` mod 2, with
|λ i - λ j| ≥ h whenever ε i ≠ ε j), let c ≤ h be a natural number, and let `g` be a positive
definite element of U(diag ε) with block diagonal part `a` (the entries (i, j) with ε i = ε j). Then
`|det a| ^ c ≤ |m_{-λ-ρ}(g)|²`. Here λ + ρ is `paramAddRho l`, with ρ the half sum of all roots
positive for l, and m_w = `weightMinors w` is the product over integers t of the principal minors of
g on {i | t ≤ w_i}, each factor with t ≤ 0 divided by det g. 

### `norm_dsCoeff_sq_mul_det_pow_le_one`

 For a parameter l = 2λ of gap h (entries of λ with different signs are at least h apart), a
natural number c ≤ h, and g in U(diag ε): |c_λ(g)|²·|det a_g|^c ≤ 1, where c_λ = `l.dsCoeff` is the
discrete series coefficient and a_g is the block diagonal part of g. 

### `DiscreteSeries.norm_dsCoeff_le_pow`

 For nonempty n, a parameter l = 2λ of gap h, a natural number c ≤ h and g in U(diag ε):
|c_λ(g)| ≤ (2/‖g‖)^c, with the operator norm. 


## The module U(𝔤)c_λ and its L² model

Conventions: `New.HCParam.HasLargeGap l A` is gap `500 n³ + A`; `K = U(diag ε) ∩ U(n)`; `casimirK 1`
(all signs equal) is the Casimir operator `Ω = ∑ E_ab E_ba` of `gl n`.


 ### The module generated by `c_λ` 

### `HCParam.DsModule`

 The space U(𝔤)c_λ, l = 2λ, generated by c_λ under right derivatives inside the smooth
functions on U(diag ε). 

### `HCParam.dsAction`

 The gl_n-module structure on U(𝔤)c_λ obtained by restricting the action by right derivatives
on smooth functions. 

### `HCParam.dsGenerator`

 The function c_λ regarded as an element of the module U(𝔤)c_λ that it generates. 

### `dsCoeff_neg_mul_borel_inv`

 Equivariance on the right of the function `y ↦ (-l).dsCoeff y⁻¹`, for `l` with gap `h`. If
`x` is block diagonal, invertible and upper triangular in the order of decreasing `l`, then passing
from a group element `g` to `g * x` multiplies this function by `∏ i, x i i ^ Λ i`, where `Λ` is
the highest weight `l.lowestKType` of the lowest `K`-type. 

### `isKHighest_dsGenerator`

 Let `l = 2λ` have gap h (entries distinct and congruent to `card n - 1` mod 2, with |λ i - λ
j| ≥ h whenever ε i ≠ ε j). Then the generator c_λ = `l.dsCoeff` of the module U(𝔤)c_λ, with gl_n
acting by right derivatives (`dsAction`), is a highest vector of weight `l.lowestKType` for
K = U(diag ε) ∩ U(n). That is, each `E a a` acts on it by `lowestKType a`, and it is killed by every
`E a b` with ε a = ε b and l b < l a. Here `lowestKType` is Λ = λ + ρ - 2ρ_c, with ρ the half sum of
the roots positive for l and 2ρ_c the sum of the compact ones (ε i = ε j), i.e. the highest weight
of the lowest K-type. 

### `DiscreteSeries.norm_dsCoeff_le_one`

 Let `l = 2λ` be a parameter of gap `h` for the signs `ε`: its entries are distinct and of the
parity of `card n - 1`, and `|λ i - λ j| ≥ h` when `ε i ≠ ε j`. Then the function `c_λ = l.dsCoeff`
satisfies `‖c_λ(g)‖ ≤ 1` for every `g` in `U(diag ε)`. 

 ### Smearing 

### `integral_mul_dsCoeff_translate`

 Let n ≥ 1, let λ have gap 500n³+A, and let w be integrable on G = U(diag ε) with ∫_K
conj(m_Λ(k)) w(k⁻¹g) dk = ∫_K |m_Λ|² · w(g) for all g (m_Λ = `New.weightMinors` of the lowest K-type
Λ, and dk = `haarK ε` is the Haar measure of mass one on K = U(diag ε) ∩ U(n)).
Then ∫ w(g)c_λ(xga) dg = c_λ(x) ∫ w(g)c_λ(ga) dg. 

### `exists_smear_dsCoeffSmooth_eq`

 Let the index type n be nonempty, and let l = 2λ have gap 500n³+A, where n is its cardinality.
Every function f in U(𝔤)c_λ, the space generated by c_λ = `l.dsCoeff` under right derivatives, is a
smearing of c_λ. That is, there is a smooth function β of compact support on U(diag ε) (an element
of `New.DiscreteSeries.Bumps`) with f(g) = ∫ β(y⁻¹) c_λ(gy) dy for all g, which is
`New.DiscreteSeries.smear` of c_λ applied to β. 

 ### Decay, integrability and the product formula 

### `exists_decay_bound`

 For n ≥ 1, `l = 2λ` a parameter for ε of gap 500n³+A, f in U(𝔤)c_λ and a natural number
c ≤ 500n³+A, there is K with |f(g)| ≤ K(2/‖g‖)^c for all g in U(diag ε). Here c_λ is `dsCoeff`,
U(𝔤)c_λ is the space of smooth functions on U(diag ε) generated by c_λ under right derivatives, and
‖g‖ is the norm of g as a complex matrix. 

### `_root_.New.integrable_two_div_norm_pow`

 For `n ≥ 1` and a natural number `c > 8 n²`, the function `g ↦ (2 / ‖g‖) ^ c` is integrable on
`U(diag ε)`, where `‖g‖` is the operator norm. 

### `integrable_mul_norm_pow`

 For `λ` of gap `500 n³ + A`, `f` in `U(𝔤) c_λ` and a natural number `C ≤ A + 1`, the function
`g ↦ f g * ‖g‖ ^ C` is integrable on `U(diag ε)`, where `‖g‖` is the operator norm. 

### `integrable`

 For `λ` of gap `500 n³ + A`, every function in `U(𝔤) c_λ` is integrable. 

### `memLp`

 For `λ` of gap `500 n³ + A`, every function in `U(𝔤) c_λ` is square integrable. 

### `_root_.New.formalDegree_pos`

 For signs `ε` with `n` nonempty and a parameter `l = 2λ` of gap `500 n³ + A`, the formal degree
`deg_λ` is positive; `deg_λ` is the reciprocal of the integral of `|c_λ|²` over `U(diag ε)` for the
Haar measure `haarU`. 

### `integrable_dsKernel_mul_norm_pow`

 Let `l = 2λ` be a parameter for the signs `ε` with gap `500 n³ + A` (`HasLargeGap`), and let
`C ≤ A + 1` be a natural number. Then `g ↦ e_λ g * ‖g‖ ^ C` is integrable on the unitary group
`U(diag ε)`. Here `e_λ = deg_λ · conj c_λ` is `New.HCParam.dsKernel` and `‖g‖` is the operator
norm. 

### `_root_.New.dsCoeff_schur_orthogonality`

 Schur orthogonality: for n ≥ 1, `l = 2λ` a parameter for ε of gap 500n³+A, and x, a in U(diag
ε), deg_λ ∫ c_λ(xya) conj(c_λ(y)) dy = c_λ(x)c_λ(a). Here c_λ is `dsCoeff`, dy is the Haar measure
`volume` on U(diag ε), and deg_λ is the formal degree, the reciprocal of ∫ |c_λ|² dy. 

 ### The model in `L²` 

### `toL2`

 The linear map from U(𝔤)c_λ to L²(U(diag ε)) sending a function f to √(deg_λ)·f. 

### `_root_.New.inner_toLp_rightRegularL2_toLp`

 For square integrable functions `w` and `z` on `U(diag ε)`, the inner product in `L²` of `w`
with the right translate of `z` by `x` is `∫ g, z (g * x) * conj (w g)`. 

### `inner_toL2_rightRegularL2`

 The matrix coefficient of right translation by `x` between the images in `L²` of two functions
`y`, `z` of `U(𝔤) c_λ` is the formal degree times `∫ g, z (g * x) * conj (y g)`. 

### `continuous_rightRegularL2_toL2_dsGenerator`

 The orbit map `g ↦ R(g) c_λ` of the image of the generator in `L²` is continuous, where `R` is
right translation. 

### `inner_smear_rightRegularL2_toL2_dsGenerator`

 The inner product of `w` in `L²` with the smearing of the orbit map `g ↦ R(g) c_λ` by a bump
function `α` may be taken under the integral sign. 

### `rightRegularL2_toL2_eq_smear`

 If the function `y` of `U(𝔤) c_λ` is the smearing of `c_λ` by a bump function `α`, then its
right translate by `g` in `L²` is `∫ x, α x⁻¹ • R(g x) c_λ`, the smearing by `α` of the orbit map
of `c_λ`. 

### `isDerivedAction_toL2`

 The action `dsAction` of `gl n` on `U(𝔤) c_λ` is the derivative, along `toL2`, of right
translation on `L²`. 

### `inner_toL2_dsGenerator_rightRegularL2`

 For signs `ε` with `n` nonempty and a parameter `l = 2λ` of gap `500 n³ + A`, let `y` be any
function in `U(𝔤) c_λ`, the module generated by `c_λ` under right derivatives inside the smooth
functions on `U(diag ε)`. Then `y` is its own matrix coefficient against the generator `c_λ`:
`⟪c_λ, R(g) y⟫ = y g` for every `g ∈ U(diag ε)`. Here both functions are placed in `L²(U(diag ε))`
by `toL2` (multiplication by `√deg_λ`), and `R` is right translation. 

### `isDerivedAction_toL2_and_inner_toL2`

 For signs `ε` with `n` nonempty, let `l = 2λ` be a parameter with gap `500 n³ + A`
(`hg : l.HasLargeGap A`). Let `toL2` be the embedding f ↦ √(deg_λ)·f of the module `U(𝔤) c_λ`,
generated by `c_λ` under right derivatives, into `L²(U(diag ε))`. Then: the module action `dsAction`
is the derivative of the right regular representation along `toL2`; every `y` satisfies
`⟪toL2 c_λ, R(g) toL2 y⟫ = y(g)`; and `⟪toL2 y, R(x) toL2 z⟫ = deg_λ · ∫ z(g x) · conj(y(g)) dg`
over `U(diag ε)`, where `deg_λ` is the formal degree `formalDegree`. 

### `toL2_injective`

 The map `toL2` from `U(𝔤) c_λ` to `L²` is injective. 

### `instance : NormedAddCommGroup l.DsModule`

 The norm that `U(𝔤) c_λ` inherits from `L²` through `toL2`. 

### `instance : InnerProductSpace ℂ l.DsModule`

 The inner product that `U(𝔤) c_λ` inherits from `L²` through `toL2`. 

### `norm_dsGenerator`

 The generator `c_λ` has norm `1` for the norm pulled back from `L²` by `toL2`. 

### `norm_apply_le_norm`

 Each value of a function in `U(𝔤) c_λ` is bounded by the norm of the function pulled back from
`L²` by `toL2`. 

### `isUnitaryCasimirGe`

 The inner product that `U(𝔤) c_λ` inherits from `L²` is invariant under `𝔲(diag ε)`, and the
Casimir operator Ω = ∑ E_ab E_ba of `gl n` is at least `l.casimirValue`, the scalar by which Ω acts
on `c_λ`, on `U(𝔤) c_λ`. 

### `isUnitaryCasimirGe_dsAction`

 The three properties of the inner product that `U(𝔤) c_λ` inherits from `L²`: it is invariant
and the Casimir operator Ω = ∑ E_ab E_ba is at least `l.casimirValue`, the scalar by which Ω acts on
`c_λ` (`isUnitaryCasimirGe`); the generator is a unit vector (`norm_dsGenerator`); the values of a
function are bounded by its norm (`norm_apply_le_norm`).

A step in Flensted-Jensen's construction of Harish-Chandra's discrete series of U(p,q), for
parameters of large gap. `IsUnitaryCasimirGe` records only the inequality for Ω, although Ω acts on
the whole module by exactly `l.casimirValue`. 


## Lipschitz and tail bounds for c_λ

* `New.norm_dsCoeff_sub_le`: the Lipschitz bound for `c_λ` under right translation.
* `New.measure_ball_le_integral_dsCoeff`: since `‖c_λ‖ ≥ 1 / 2` on a small ball about `1`
  (`New.half_le_norm_dsCoeff`), a covering argument bounds the measure of a ball of radius `r` in
  terms of `∫ ‖c_λ‖ ^ 2`, on any group with a homomorphism to `New.USign ε`.
* `New.integral_formalDegree_mul_two_div_norm_pow_le`: the resulting bound for the integral of
  `l.formalDegree * (2 / ‖g‖) ^ c`.


### `norm_rightDeriv_dsCoeffSmooth_le`

 For `l = 2λ` of gap `500 n³ + B` with all `|l a| ≤ L`, the right derivative of `c_λ` along a
matrix `X` is bounded by `(n + 1)⁴ (n + L + 1) ‖X‖` at every point of `U(diag ε)`. 

### `conjTranspose_mul_signMatrix_mul_curve`

 For g in U(diag ε), A = g − 1 and real t, the matrix γ = 1 + t A u⁻¹ with u = 1 − ((t − 1)/2) A
satisfies γᴴ J γ = J, where J = diag ε and the inverse of a non-unit is 0. 

### `norm_dsCoeff_sub_le`

 For l = 2λ a parameter of gap 500n³+B with all |l_a| ≤ L, and x, g in U(diag ε):
|c_λ(xg) − c_λ(x)| ≤ 100(n+L+1)⁵‖g−1‖, in the operator norm. 

### `half_le_norm_dsCoeff`

 Let `l` have gap 500n³+B, all |l_a| ≤ L, and β ≥ n + L + 1, where n = card n. If g in
`New.USign ε` satisfies ‖g − 1‖ ≤ (200 β⁵)⁻¹ in the operator norm, then ‖c_λ(g)‖ ≥ 1/2. 

### `measure_ball_le_integral_dsCoeff`

 Let `l` have gap `500 n³ + B` and all `|l a| ≤ L`. Let `j` be a homomorphism from a group `S`
to `USign ε` and `ν` a right invariant measure on `S` for which `l.dsCoeff ∘ j` is square
integrable. For `r ≥ 1` the set of `s` with `‖j s‖ ≤ r` has measure at most
`(2000 * ℓ ^ 6 * r ^ 2) ^ (2 * card n ^ 2)` times `∫ 4 * ‖l.dsCoeff (j s)‖ ^ 2`, where
`ℓ = card n + L + 1`. 

### `integrable_formalDegree_mul_two_div_norm_pow`

 For a parameter `l` and a natural number `c > 8 n²`, the function
`g ↦ deg_λ * (2 / ‖g‖) ^ c` is integrable on `U(diag ε)`, where `deg_λ = l.formalDegree`. 

### `integral_formalDegree_mul_two_div_norm_pow_le`

 Let n = `card n` ≥ 1, and let `l = 2λ` be a parameter of gap `500 n³ + B`: its entries are
distinct and congruent to n - 1 mod 2, and |λ i - λ j| ≥ 500 n³ + B whenever ε i ≠ ε j. Suppose all
`|l a| ≤ L` and `c > 8 n²` is a natural number. Then the integral of `deg_λ * (2 / ‖g‖) ^ c` over
`U(diag ε)`, for its `volume` `New.haarU`, is at most `8 (2000 (n + L + 1)⁶) ^ (2 n²) 2 ^ c`, where
`deg_λ = l.formalDegree` is the reciprocal of the integral of |c_λ|² = |`l.dsCoeff`|² for that same
measure. 

### `integral_tail_le`

 For `l = 2λ` of gap `500 n³ + B` with all `|l a| ≤ L` and a natural number `c > 8 n²`, the
function `g ↦ deg_λ * (2 / ‖g‖) ^ c` is integrable on `U(diag ε)`, with integral at most
`8 (2000 (n + L + 1)⁶) ^ (2 n²) 2 ^ c`, where `deg_λ = l.formalDegree`. 
