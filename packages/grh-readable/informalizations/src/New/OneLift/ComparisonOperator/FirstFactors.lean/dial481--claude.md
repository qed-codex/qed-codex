---
{
  "module": "src/New/OneLift/ComparisonOperator/FirstFactors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/FirstFactors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/FirstFactors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The first factors: P_V along W_j and W^add, integrality and size

Fix admissible data `D`, a tame character `ϑ` and an index `1 ≤ j ≤ m`. Write `E^n` for
the standard definite space of rank `n`, V″ for the one on `New.Data.FirstFactorIndex` and
W^add = E^{3m−j} ⊕ W♭ ⊕ E^{3m} for the one on `New.Data.AddedIndex`. Throughout, k = `D.k`,
m = `D.m`, M = `D.M`, and W_j is the space on `D.RowIndex` with r₊ = `D.posRank j` = k + j − 1
plus signs. This file writes P_V as a sum of products of a polynomial in X and a coordinate of
ζ(z), where X are the variables in the positive basis vectors of W_j and z those in W^add. Each
value of Υ is a double class sum of products of three theta kernels of definite spaces, and this
file bounds these kernels. By `New.Data.exists_isIntegralAndSmall_leftSideSeries`, for one constant
`c″ ≠ 0` the first factors φ″, the complex conjugates of c″Υ, are integral away from the norm of Q
and, if Q is empty, all their images under automorphisms of ℂ are small
(`New.Data.IsIntegralAndSmall`).

## Main definitions and results

* `New.Data.renameRowsCols_stackedDetProd_eq_sum`: P_V as a sum of products of a polynomial in X and
  a coordinate of ζ(z).
* `New.Data.exists_isIntegralAndSmall_leftSideSeries`: for 1 ≤ j ≤ m there is one c ≠ 0, independent
  of i, ϑ and h, such that every first factor y = conj (c · Υ) is integral and small in the sense of
  `New.Data.IsIntegralAndSmall`.

Notions from other files:
* `New.toPoly`, `New.weylNormSq`: the polynomial of a coordinate vector of weight κ, and the squared
  norm of the vector for the Gram matrix of κ. Here `κ τ h` counts the columns of height `h` at `τ`.
* `New.Data.FirstFactorIndex`: the indices of W_j, (E^j)⁻, E^{3m−j} and W♭ = E^{6m+1}.
* `New.Data.TameChar`, `New.Data.twistModulus`: a character `ϑ` of U(1)(𝔸) of weight 0 with tame
  part on a finite set Q = `ϑ.Q` of places, and the moduli ϖ^c Q.
* `New.Data.stackedDetProdCoords`: the coordinates of the polynomial map ζ.
* `New.Data.leftSideSeries`: the series Υ, built from theta kernels of definite spaces.

## Relation to the literature

The first factors enter the comparison of twisted theta forms on U(W_j) with twist-free ones,
`New.Data.exists_mul_thirdExchangeLeftSide_eq_choiceFn` in
`New.OneLift.ComparisonOperator.ThreeExchanges`: for every twist, an explicit theta form times a
number is a twist-free function, and the squared modulus of the number is a constant independent of
the twist divided by a product of squared Hecke L-values and powers of norms of places. This file
proves that the first factors are integral off the conductor and small when untwisted. The rank one
case (the lift is a scalar of square modulus an L-value), twisting on a square block and integral
theta data are known in the literature. Related work: T. Yang, Theta liftings and Hecke L-functions,
1997; Böcherer–Schmidt, p-adic measures attached to Siegel modular forms, 2000; Harris–Li–Skinner,
The Rallis inner product formula and p-adic L-functions, 2005.



## The product of determinants as a sum of products, along W_j and W^add


### `New.Data.renameRowsCols_stackedDetProd_eq_sum`

 The determinant product `New.Rows.stackedDetProd` of the matrices `New.Data.constantRows` for
the short basis `D.shortRows i` at the class chosen by `i` has its columns renamed. `f` renames the
positive indices of W_j, the space of the `j`-th lift with indices `D.RowIndex`. `g` renames the
indices `AddedIndex j` of W^add. The result equals the sum over `l` of the products of two factors:
the letter polynomial (`New.letterPoly`) of the `l`-th unit vector in the letters of sign `1`,
renamed by `f`, and the `l`-th coordinate `New.Data.stackedDetProdCoords`, renamed by `g`. 


## Integrality and size of the first factors

Each value of Υ is a double class sum of products of three theta kernels of definite pairs, to which
`New.Rows.exists_ne_zero_isModKernelScale` applies; the third is evaluated on the polynomial
coordinates `New.Data.stackedDetProdCoords`, whose degree and denominator come from
`New.Data.exists_isHomogeneousOverEntries_smul_stackedDetProdCoords`.

`New.weylGauge κ e h y ≤ 1` says that `y` is `p`-integral for the lattice at `h`, read through the
embedding `ιₚ : ℂ → ℂ_[p]` given by the instance `[PadicPlace p]`.


### `normQ_mul_M_pow_mem_modulus`

 With `M = D.M`, the integer `ϑ.normQ * M ^ c` lies in the ideal of the modulus
`D.twistModulus ϑ c`: the `c`-th power of the product of the chosen places (the places
`D.chosenPlace` of the data) times the product of the places in `ϑ.Q`. 

### `constantRows_mul_transpose_eq_mul_fromBlocks`

 Replacing the matrix Y by Y·Bᵀ multiplies the matrices `constantRows` on the right by the
transpose of the block diagonal matrix (1, 1, τB, τA) at each τ, whatever A is. 

### `firstFactorSize_sq_le_exp`

 Let `q` be the bound on the number of determinants, `n ≤ (10 m + 1) q` a degree with `n ≤ D.M`
and `0 < H ≤ (n ^ n) ^ 3` a denominator. Then the constant `chosenGroupOrder ^ 2`, the two class
numbers, three kernel bounds `exp x₁`, the order of GL_{3m} over the residue ring and the bound on
`H` times the coordinates give at most exp(f m b log² b) after squaring. Here f = `D.f` is the
number of infinite places, b = `D.b` and `D.natB` the weight at the b-places, log b = `D.logB`,
`D.offWeight` the weight at the other places, `D.gap` = 2 r⁸ the gap, x₁ = `D.x₁` the second cut-off
and `D.chosenGroupOrder` a common multiple of the orders of the stabilisers. 

### `modKernelBilin_stackedDetProdCoords_equivariant`

 Equivariance under rational points. Let Γ and γ' be rational unitary points of the definite
spaces W^add and V″, and let the constant rows built from Y' be those built from Y multiplied by
diag(1, Γ)ᵀ at each place. Then γ'⁻¹, acting on vectors of weight μ⁺, carries the complex conjugate
of the vector l ↦ c 𝖪[H·ζ_l](Γ g, γ' h) for Y' to that of l ↦ c 𝖪[H·ζ_l](g, h) for Y. Here 𝖪 is the
theta kernel `modKernelBilin` of (W^add, V″) for the datum Ψ modulo 𝔪, with both characters
`firstFactorChar ϑ j`, and ζ = `stackedDetProdCoords`. 

### `norm_shortRows_mul_transpose_le_one`

 Let `i` be a class with its short basis, whose vectors are the rows of `D.shortRows i`, and let
`γ` be a rational unitary point that moves the representative of the class into the points integral
above `p`. Then the entries of `D.shortRows i * γᵀ` are `p`-integral under every embedding `σ`. 

### `weylGauge_modKernelBilin_stackedDetProdCoords_le_one`

 Let v(Y, g, h) be the vector l ↦ conj (c 𝖪[H·ζ_l](g, h)). Here ζ = `stackedDetProdCoords j i Y`,
and 𝖪 is the theta kernel of the standard definite spaces W^add on `AddedIndex j` and V″ on
`FirstFactorIndex j`, with both characters `firstFactorChar ϑ j` for the tame character `ϑ` and a
datum `Ψ` on matrices modulo the modulus `𝔪`. Suppose that v(Y, g', h') has `p`-integral coordinates
under `ιₚ : ℂ → ℂ_[p]` whenever the finite adelic points `g'`, `h'` have integral components at the
primes above `p` (`integralAbove`) and the entries of `Y`, embedded in ℂ by `Φ τ`, are `p`-integral
under `ιₚ ∘ conj`. Let g be the block diagonal point (`U.blockSumOne`) with blocks `1`, the
representative in U(W♭) of the class of `i`, and `w` in U(E^{3m}). Then v(`D.shortRows i`, g, h) has
gauge at most one at every `h` (`weylGauge`): all coordinates of h⁻¹ · ιₚ(v) have norm at most
one. 

### `addedDatum_mem_integralAway`

 Let `ϑ` be a tame character with set of places Q, let ϖ be the product of the chosen places, and
let `u`, `x` be matrices modulo ϖ² and ϖ²Q. The datum `addedDatum ϑ j u x` is `0` or a sum, over
GL_{3m}(O_E/ϖ²), of values of the additive character attached to `u`. For each `n` it has norm at
most one under all ring maps `ℂ → ℂ_[l]` with `l` a prime coprime to `n`
(`New.Seesaw.integralAway`). 

### `norm_map_addedDatum_le`

 Every conjugate of a value of `New.Data.addedDatum`, for a matrix `u` modulo ϖ², has absolute
value at most the order of GL over the residue ring of `D.untwistedModulus 2` (the modulus ϖ², ϖ
the product of the chosen places), the number of terms in the sum defining it. 

### `card_le_gap`

 The ranks of the five spaces in the three kernels are at most the gap `Δ = D.gap`. 

### `sqrt_weylNormSq_smul_eval_stackedDetProdCoords_le`

 Let ζ = `stackedDetProdCoords j i (D.shortRows i)` be the vector of coordinates of the product
of determinants, polynomials in variables indexed by an infinite place in `D.Φ`, a row in
`FirstFactorIndex j` and a column in `AddedIndex j`. Evaluate `H • ζ` at a point `z` whose
`σ`-conjugates are at most `M ^ 4`, where `M = D.M`, and apply `σ`. If `q` bounds the total number
of determinants, the root of the squared norm (`New.weylNormSq`) of the result is at most
`√(H ^ 2 (M ^ 9) ^ ((12 m + 1) q))`, with `m = D.m`. 

### `sqrt_weylNormSq_comp_le_of_eval_le`

 Duality for a vector `v` of homogeneous polynomials of degree `n`. Its coordinates are indexed
by the basis `WeylIndex N κ` of the Weyl module of GL_N whose diagram at each `τ : T` has `κ τ h`
columns of height `h`. The norm of a coordinate vector is the square root of `weylNormSq`, its
squared norm for the positive definite Hermitian form of the Gram matrix. Let `σ` be a ring
automorphism of ℂ. Suppose that the `σ`-conjugates of the values of `v` on a set `S` have norm at
most `B`. Suppose also that a linear form `θ` has `‖σ (θ Q)‖ ≤ C` for every homogeneous `Q` of
degree `n` with `‖σ (Q z)‖ ≤ B` on `S`. Then the `σ`-conjugate of `θ ∘ v` has norm at most `C`. 

### `weylGauge_stdClassSum_stdClassSum_le_one`

 Let `p` be a prime with an embedding `ιₚ : ℂ → ℂ_[p]` (`PadicPlace p`). A vector `y` of weight
μ⁺ = `(untwistedDescentPair j).colsPlus` is `p`-integral at `h` if `weylGauge μ⁺ 0 h y ≤ 1`: all
coordinates of h⁻¹ · ιₚ(y) have norm at most one. Let every `f w v` be `p`-integral at `h`. Then so
is their double class sum over U(E^{3m}) and U(E^m) (`stdClassSum`, the sum of the values at class
representatives divided by the orders of the stabilisers), multiplied by the square of
`D.chosenGroupOrder`, which is a common multiple of these orders. 

### `weylNormSq_stdClassSum_stdClassSum_le`

 Let `q` = |D.Φ| (natB + offWeight + Δ + m Δ) be the bound on the number of determinants, with
the weights `D.natB`, `D.offWeight` and the gap Δ = `D.gap`. Let `n ≤ (10 m + 1) q`, `n ≤ M` for
M = `D.M`, and `0 < H ≤ (n ^ n) ^ 3`. Let every vector `F w v` have `φ`-conjugate of norm at most
exp(3 x₁) |GL_{3m}(O_E/ϖ²)| √(H² M^{9 (12 m + 1) q}), where x₁ = `D.x₁` is a size parameter of the
data and ϖ² = `D.untwistedModulus 2` is the square of the product of the chosen places. Then the
double class sum of `F`, multiplied by the square of `D.chosenGroupOrder` (a common multiple of the
orders of the stabilisers), has `φ`-conjugate of squared norm at most exp(f m b log² b), for the
number f = `D.f` of infinite places, the weight b = `D.b` and log b = `D.logB`. 

### `IsIntegralAndSmall`

 The vector `y` of weight `(untwistedDescentPair j).colsPlus` is integral at `h` away from the
norm `ϑ.normQ` of Q (the product of the norms of the places in `ϑ.Q`), and has small conjugates if
`ϑ.Q` is empty: the bound is exp(f m b log² b), for the number f = `D.f` of infinite places, the
weight b = `D.b` and log b = `D.logB`. 

### `IsIntegralAndSmall.weylGauge_le_one`

 `y` is `p`-integral at `h` for every prime `p` that does not divide `ϑ.normQ`. 

### `IsIntegralAndSmall.weylNormSq_le`

 If `ϑ.Q` is empty, all conjugates of `y` have squared norm at most exp(f m b log² b). 

### `norm_mul_modKernelStdSpace_twistedChiMPow_le_one`

 Let `ϑ` be a tame character and χ′ = χ^j ϑ, where χ = `D.chiM` is the fixed character of U(1)(𝔸)
of weight `0` and tame part `D.chiMLocal`. Take the theta kernel of the standard definite spaces
(E^m, E^{3m}) with characters χ′ and `1`, unit modulus, datum `1` and polynomial `1`, and a constant
`c` that normalises such kernels. For every prime `p` with an embedding `ιₚ : ℂ → ℂ_[p]`, the image
of `c` times the kernel has norm at most one at all finite adelic points `v`, `w`. 

### `norm_mul_modKernelStdSpace_one_le_one`

 Take the theta kernel `modKernelStdSpace` of (E^j, V″), with V″ the standard definite space on
the index set `FirstFactorIndex j`, for the characters `1` and `b`, a datum `Ψ` modulo `𝔪` and the
polynomial `1`. Let `c` be a constant that normalises such kernels. Let `b` have weight `e` at the
infinite places `D.Φ` and tame part `ψ`, a character of the residue field `ResField w` at each
finite place `w`. Let `𝔪` contain `q * D.M ^ 2`, with `D.M` the integer `M` of the data. Let the
values of `Ψ` have norm at most one under all ring maps `ℂ → ℂ_[l]` with `l` a prime coprime to `q`.
Let `p` be a prime coprime to `q`, and let `h` lie in `Gf D.E (FirstFactorIndex j)`, the finite
adelic unitary group of V″. Then the image under `ιₚ : ℂ → ℂ_[p]` of `c` times the kernel at `1` and
`h` has norm at most one. 

### `exists_star_leftSideSeries_eq_classSum`

 Expansion of the conjugate of a multiple of the series Υ = `leftSideSeries ϑ j (u, i) h`, for a
tame character `ϑ`, a matrix `u` modulo ϖ² (`D.untwistedModulus 2`, ϖ the product of the chosen
places) and a class with rows `i`. Let g = `D.chosenGroupOrder`, a common multiple of the orders of
the stabilisers. There is `c` of modulus one, depending only on `j`, such that the conjugate of g²
c₂ H c₀ conj(c₁) c Υ is g² times a double class sum over U(E^{3m}) and U(E^m) of conjugates of
products of three theta kernels of definite spaces: `k₀` of (E^m, E^{3m}), the conjugate of `k₁` of
(E^j, V″), and c₂ times the kernel of (W^add, V″) at the polynomial vector
`H • stackedDetProdCoords j i (D.shortRows i)`, formed with a short basis of the class. V″ and W^add
are the spaces on `FirstFactorIndex j` and `AddedIndex j`, and the last two kernels have modulus
ϖ²Q. Here `Ψ x` is the conjugate, at `normNegOne • x` (a chosen element of norm −1, reduced), of the
indicator of the matrix of the inclusion E^j → V″ (`inclMatrix`), and `b'` is the inverse of the
character `firstFactorChar ϑ j` times the power rank V″ of `upsilonU1` (υ on the norm-one ideles).
The scalars `c₀`, `c₁`, `c₂` and the integer `H` are arbitrary. 

### `exists_isIntegralAndSmall_leftSideSeries`

 For 1 ≤ j ≤ m there is one c ≠ 0, independent of i, ϑ and h, such that every vector y = conj
(c · Υ) is integral and small in the sense of `New.Data.IsIntegralAndSmall`: for every prime p that
does not divide `ϑ.normQ`, the product of the norms of the places in `ϑ.Q`, the coordinates of
h⁻¹ · ιₚ(y) are `p`-integral (`New.weylGauge` ≤ 1), and if `ϑ.Q = ∅`, every conjugate φ ∘ y,
φ ∈ Aut(ℂ), has squared norm at most exp(f m b log² b), with the number f = `D.f` of infinite
places, m = `D.m`, the weight b = `D.b` and log b = `D.logB`. 
