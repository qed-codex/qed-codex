---
{
  "module": "src/New/OneLift/ComparisonOperator/ThetaKernelEstimates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ThetaKernelEstimates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ThetaKernelEstimates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decay of Fock matrix coefficients, sparse theta sums and the isolation estimate

This file holds the estimates behind the theorem that products span. The Heisenberg matrix
coefficients of a homogeneous Fock vector decay faster than any power. So in a theta sum over a
sparse lattice the term of `0` dominates, and a mean over additive characters produces such a sum.
Bounds for integrals of matrix coefficients of holomorphic discrete series then give the isolation
estimate `New.Data.norm_apply_one_le_of_forall_isPeak`, the last step of the proof: the mean over a
circle of peaks.

## Main definitions and results

* `New.Fock.norm_fockInner_realHeisenbergOp_le`: the decay of the coefficient `⟨v, ϱ(y) ω(σ) v⟩` in
  `y`.
* `New.Rows.firstMinimum_mul_le_hom`: the first minimum of `Hom (S, T)` is bounded below by the
  product of the first minima of `S` and `T`, up to an explicit constant.
* `New.Rows.exists_norm_modKernel_sub_fockInner_le`: for a suitable finite datum `Ψ` modulo `𝔪`, the
  theta kernel at real translates of `(g, h)` differs from a Fock matrix coefficient by a small
  error if the lattice of `Hom (S, T)` has no short vectors.
* `New.Data.integral_norm_holMinorsPi_mul_pow_le`: the integral of the basic function of a weight
  with a large gap against a power of the norm, compared with a squared `L²` norm.
* `New.Data.norm_apply_one_le_of_forall_isPeak`: let a bounded function `K₀` be close, for every
  peak of a holomorphic `F`, to a holomorphic `K` whose weighted integral against the translate of
  `F` vanishes. Then `K₀ 1` is small.

Notions from other files:
* `New.Fock.fockSpace`: The Fock space: integrable functions c on ℂ^ι with c(x) = ∫ c(y)β(y,x)e(x−y)
  dy, β the Heisenberg bicharacter, e the Gaussian exp(−|x|²/2), under the L¹ norm.
* `New.Fock.fockInner`: The bounded sesquilinear form on the Fock space, conjugate-linear in the
  first variable, (c, c′) ↦ ∫ c̄ c′.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.GInf`: The archimedean unitary group G_∞ for signs s: one copy of the complex unitary group
  U(diag s) for each infinite place of E.
* `New.IsPosFirstOrder`: The order o has distinct values and puts every index of sign +1 before
  every index of sign −1.
* `New.Space.vecAtPoint`: the adelic vector x⁻¹y of a rational vector y at the point x of a space;
  the lattice `New.Space.baseLattice` consists of the y for which it has integral finite part.
* `New.realCoord`: the Fock coordinates of an adelic vector: its components at the infinite places
  τ, times √(2π Im τ(j)), with j the element fixed by the Weil data.

## Relation to the literature

See `New.OneLift.ComparisonOperator.ProductsSpan` for related work. See
`Lib.Weil.DualPair.ThetaLiftConvergence` and `Lib.Adelic.Reduction.FiniteVolume` for sources.



## Decay of Heisenberg matrix coefficients of homogeneous Fock vectors

One estimate, `New.Fock.norm_fockInner_realHeisenbergOp_le`: for a homogeneous polynomial P and v =
v_P in the Fock space, the coefficient ⟨v, ϱ(y)ω(σ)v⟩ decays faster than any power of |y|, with
explicit constants and polynomial growth in ‖σ‖. Here ϱ = `New.Fock.realHeisenbergOp` is the
Heisenberg action, ω = `New.Fock.realWeil` the Weil representation of U(ε), and v_P =
`New.Fock.polyVector` ε P.


### `New.Fock.norm_sq_le_norm_sq_add_norm_mulVec_add_sq`

 For `σ` in `U(ε)` and vectors `x`, `y`, the points `x` and `σ x + y` cannot both be
small: `|y|² ≤ 2 ‖σ‖² (|x|² + |σ x + y|²)`, with Euclidean norms and the ℓ² operator norm. 

### `New.Fock.norm_fockInner_realHeisenbergOp_le`

 Let ι be nonempty, P a complex polynomial with P(cx) = c^d P(x) for real c, v = v_P its Fock
vector (`polyVector`), σ in U(ε), and y ≠ 0 in ℂ^ι. For natural numbers A ≥ d + |ι| and n,
|⟨v, ϱ(y)ω(σ)v⟩| ≤ (4(A + n))^n |y|^{−2n} ‖σ‖^{|ι| + 2n} ⟨v, v⟩.
Here ϱ = `realHeisenbergOp` is the Heisenberg action on the Fock space and ω = `realWeil` the Weil
representation of U(ε), |y| = `‖toLp 2 y‖` is the Euclidean norm, ‖σ‖ the ℓ² operator norm of the
matrix of σ, and ⟨v, v⟩ is real. 


## First minimum of Hom(S, T) and sparse theta sums

`New.Space.firstMinimum V` is the length of a shortest nonzero vector of the lattice of `V`, cut off
at `1`. A point `g` enters by moving the space, as in `V.move g`. `New.modKernel S T a b 𝔪 Ψ Q` is
the theta kernel of `(S, T)` for the characters `a`, `b`, the function `Ψ` on matrices modulo `𝔪`
and the polynomial `Q`.


### `firstMinimum_mul_le_hom`

 For a space `V` let `λ(V) = V.firstMinimum` be the minimum of `1` and the length of a shortest
nonzero vector of the lattice of `V`. If the natural number `N ≠ 0` lies in the different of `E`,
then `λ(S) λ(T) / (C |n'| |n|) ≤ λ(Hom (S, T))`, where `C = shortBasisConst E n N = 6 N (f |n|)²`
and `f` is the number of infinite places of `E`. 

### `dataInner_traceChar`

 Let `S`, `T` be hermitian spaces over `E` with signs `s`, `s'` at the infinite places, and
`S.hom T = Hom (S, T)`. Let `t` be a matrix modulo the ideal `𝔪` and `Ψ_t(y) = ψ(tr(y t))` its
additive character (`traceChar t`), with `ψ` the chosen primitive character of the residue ring. Let
`v`, `w` be vectors of the Fock space in the variables `(τ, (i, k))`, `τ` an infinite place, with
signs `s' i * s k`, and `z` an adelic vector of `Hom (S, T)`. The datum `v ⊗ Ψ_t ⊗ vac` (`modDatum`)
is the function on adelic vectors made of `v` at the infinite places, `Ψ_t` at the places dividing
`𝔪` and the vacuum elsewhere; `dataInner` is the pairing `∫ c̄ c'` of such functions and `ϱ` the
Heisenberg action on them.

Then `⟨v ⊗ Ψ_t ⊗ vac, ϱ(z)(w ⊗ Ψ_t ⊗ vac)⟩` is a product of three factors. Write `z_f` for the
finite part of `z`, and `α`, `j` for the finite idele and the imaginary element of `E` fixed by
`WeilData E`. The first factor is `Ψ_t` read (by `liftFn`) at `finCoord z = α⁻¹ z_f`. The second is
the Fock coefficient `⟨v, ϱ(x) w⟩` at `x = realCoord z`, the components of `z` at the places `τ`
times `√(2π Im τ(j))`. The third is `vacuumFn` at `finVec (finCoord z) = (0, z_f)`: a complex number
of modulus `1` if `α⁻¹ z_f` is integral, and `0` otherwise. 

### `norm_pairHomInf_le_mul`

 Let `u` and `u'` be families of matrices `u τ` in `U(diag s)` and `u' τ` in `U(diag s')`, one
for each infinite place `τ` of `E` (`GInf`). The block diagonal matrix `pairHomInf (u, u')`, which
acts on `n' × n` matrices by `x ↦ (u' τ) x (u τ)⁻¹` at `τ`, has ℓ² operator norm at most
`maxOpNorm u * maxOpNorm u'`, where `maxOpNorm u` is the largest of the norms `‖u τ‖`. 

### `le_norm_realCoord`

 Let `V` be a hermitian space over `E` with adelic point `x` (`Space`). Its lattice
`V.baseLattice` consists of the rational vectors `y` whose adelic vector `V.vecAtPoint y = x⁻¹ y`
has integral finite part, and `λ = V.firstMinimum` is the minimum of `1` and the length of a
shortest nonzero lattice vector. Let `Φ w` be the chosen complex embedding at the infinite place `w`
and `j` the element of `E` with `Im (Φ w j) > 0` fixed by `WeilData E`. Let `c ≠ 0` and `m > 0`
satisfy `m |Φ w c| ≤ √(2π Im (Φ w j)) λ` for all `w`. If `y ≠ 0` and `c y` lies in the lattice, then
the Fock coordinates of `x⁻¹ y` have Euclidean norm at least `m`. 

### `le_norm_realCoord_sub`

 Let `c ≠ 0` and `m > 0` satisfy `m ‖Φ w c‖ ≤ √(2π Im (Φ w j)) · V.firstMinimum` at every
infinite place `w`. If `y ≠ z` and both `c • y` and `c • z` lie in `V.baseLattice`, then the Fock
coordinates `realCoord (V.vecAtPoint y)` and `realCoord (V.vecAtPoint z)` are at distance at least
`m`. 

### `tsum_inv_norm_realCoord_pow_le`

 Let `V` be a hermitian space over `E` with adelic point `x` (`Space`). Its lattice
`V.baseLattice` consists of the rational vectors `y` whose adelic vector `V.vecAtPoint y = x⁻¹ y`
has integral finite part, and `λ = V.firstMinimum` is the minimum of `1` and the length of a
shortest nonzero lattice vector. Let `Φ w` be the chosen complex embedding at the infinite place `w`
and `j` the element of `E` with `Im (Φ w j) > 0` fixed by `WeilData E`. Let `c ≠ 0` and `m > 0`
satisfy `m |Φ w c| ≤ √(2π Im (Φ w j)) λ` for all `w`. Let `y` run over the nonzero vectors with
`c y` in the lattice, and let `|y|` be the Euclidean norm of the Fock coordinates of `x⁻¹ y`. If `q`
exceeds the number of these coordinates, then `m ≤ |y|` for all such `y`, and `∑ |y| ^ (-2q)`
converges and is at most `(5 / m) ^ (2q)`. 

### `sum_dataInner_traceChar_div_card`

 Let `S`, `T` be hermitian spaces with signs `s`, `s'`, let `p` be an adelic point of the unitary
group of `S.hom T = Hom (S, T)`, whose signs are `homSigns s s' (i, k) = s' i * s k`, let `v`, `w`
be Fock vectors and let `y` be a rational vector. For a matrix `t` modulo the modulus `𝔪` with
additive character `Ψ_t = traceChar t`, the datum `v ⊗ Ψ_t ⊗ vac` (`modDatum`) is made of `v` at the
infinite places, `Ψ_t` at the places dividing `𝔪` and the vacuum vector elsewhere. Average over `t`
the pairing (`dataInner`) of `ω(p)(v ⊗ Ψ_t ⊗ vac)` with the Heisenberg translate `ϱ`, by the adelic
vector of `y` (`vecAtPoint`), of `ω(p)(w ⊗ Ψ_t ⊗ vac)`, where `ω` is the Weil action.

Let `x` be the adelic vector of `y` at the point of `Hom (S, T)` moved by `p`, with finite parts
`(x i).2`, and let `finCoord x` be these finite parts divided by the finite idele `α`. If
`finCoord x` is integral and vanishes modulo `𝔪`, the average is `fockInner v (realHeisenbergOp ξ
w) * ψf (traceOne * j / 2 * ∑ i, conj (x i).2 * (x i).2)`; otherwise it is `0`. Here
`realHeisenbergOp` is the Heisenberg action on the Fock space, `ξ = realCoord x` lists the
components of `x` at the infinite places `τ` times `√(2π Im τ(j))`, and `ψf` is the finite part of
the standard additive character. The idele `α` and the imaginary `j` in `E` are fixed by
`WeilData E`, and `traceOne = (1 - j⁻¹) / 2`. 

### `modKernel_expect_traceChar`

 Let the characters `a`, `b` of the unitary adeles of `E` (`AutChar`) have weights `γ`, `γ'` at
the infinite places and tame parts `ψ`, `ψ'` at the finite ones, and let `Ψ` be the average of the
characters `Ψ_t = traceChar t`, weighted by the conjugates of their theta kernels at `(g, h)`. Then
the kernel of `Ψ` at `(g u, h u')`, for real points `u`, `u'`, is the average over `t` of
`θ(ω(p)(w ⊗ Ψ_t ⊗ vac)) conj θ(ω(p)(v ⊗ Ψ_t ⊗ vac))`. Here `p = onHom (g, h)` is the point of
`Hom (S, T)` given by `(g, h)`, `ω` the untwisted adelic Weil action, `θ` the theta functional, `v`
the Fock vector of `Q` and `w = Ω(u, u') v`, with `Ω = realPairWeil γ γ'` the real Weil
representation of the pair twisted by powers of the determinants with exponents from `γ`, `γ'`. 

### `exists_norm_modKernel_sub_fockInner_le`

 Let `S`, `T` be hermitian spaces over `E` with signs `s`, `s'`, let `g`, `h` be points of their
adelic unitary groups, and let `a`, `b` be characters of the unitary adeles of `E` with weights `γ`,
`γ'` and tame parts `ψ`, `ψ'` (`HasWeight`). The class `WeilData E` fixes an imaginary element `j`
of `E` and a finite idele `α` that makes `Ô E` self-dual for the pairing `ψ_f(j α ᾱ z z')`. Let
`c ≠ 0` be such that `c α z` is integral for every `z` in `Ô E` that vanishes modulo `𝔪`. Let `λ` be
the first minimum of `Hom (S, T)` with the points moved by `g` and `h`, let `m > 0` satisfy
`m |Φ w c| ≤ √(2π Im (Φ w j)) λ` at all infinite places `w`, and let `q` exceed the number of
complex variables. Let `Q` be homogeneous of degree `d` under real scalings, with Fock vector `v`.

For a function `Ψ` on matrices modulo `𝔪`, the theta kernel `modKernel S T a b 𝔪 Ψ Q` sends a pair
of points `p` to `θ(ω_{a,b}(p)(v ⊗ Ψ ⊗ vac))`: the theta functional of the datum made of `v` at the
infinite places, `Ψ` at the places dividing `𝔪` and the vacuum elsewhere, moved by the Weil action
twisted by `a` and `b`. Then some `Ψ` has the property that, for all real points `u`, `u'`, this
kernel at `(g u, h u')` is within `(100 (d + 2q) / m²) ^ q (‖u‖ ‖u'‖) ^ (3q) |⟨v, v⟩|` of
`⟨v, Ω(u, u') v⟩`. Here `Ω` is the real Weil representation `realPairWeil γ γ'`, on the Fock space
for the signs `(τ, (i, k)) ↦ s' i * s k`, and `‖u‖ = maxOpNorm u` is the largest operator norm of
`u` at a place. 


## Integrals of holomorphic discrete series coefficients and isolation

Archimedean estimates on `New.GInf E s`, the product of the groups `U(diag s)` over the `f`
infinite places. `New.holMinorsPi s k` is the basic function `Min^hol` of weight `k`, a product of
quotients of principal minors, written `m_k`. For dominant `k` (`New.IsKDominant`) with a large gap
between the two sign blocks (`New.HasHolGap`) it is a matrix coefficient of a holomorphic discrete
series. Below, `u`, `u'` are two such weights, the entries of `u` at most `5 b` in modulus, and
`b = D.b`, `n_* = New.Data.nStar D` for admissible data `D`.

* `New.Data.integral_norm_holMinorsPi_mul_pow_le`: `∫ |m_u|²` is positive, and
  `∫ |m_u'(h)| |h| ^ (6 n_*) dh ≤ b ^ n_* ∫ |m_u|²`.
* `New.Data.integrable_mul_holMinorsPi`: a continuous function of growth at most
  `C |h| ^ (6 n_*)` is integrable against `m_u'`, with integral at most `C b ^ n_* ∫ |m_u|²`.
* `New.Data.integrable_holMinorsPi`: `m_u` is integrable; the bound on its entries is not needed.


### `one_le_maxOpNorm`

 A point of the archimedean unitary group has operator norm at least `1` at every place, so the
largest of these norms is at least `1`. 

### `eight_mul_pow_mul_two_pow_le`

 Let `D` be admissible data, with weight `b = D.b` and rank step `t = D.t`; in such data `b` is
very large against `t`. For natural numbers `n ≤ t` and `L ≤ 10 b + t`, the constant
`8 (2000 (n + L + 1)⁶) ^ (2 n²) 2 ^ (10 n³)` of `New.integral_tail_le` is at most
`2 ^ (13 t³) b ^ (14 t²)`. 

### `two_pow_mul_pow_f_le_b_pow_nStar`

 Let `D` be admissible data, with weight `b = D.b`, rank step `t = D.t`, number `f = D.f` of
infinite places and `n_* = nStar D = 2 f t³`. Then the tail bound `B = 2 ^ (13 t³) b ^ (14 t²)` of
`integrable_tail_and_integral_le` satisfies `2 ^ (6 n_*) B ^ f ≤ b ^ n_*`. 

### `two_mul_card_pow_three_le_nStar`

 For admissible data `D` and rank `n ≤ t = D.t` we have `2 n³ ≤ n_*`,
where `n_* = nStar D = 2 f t³`, since there are `f ≥ 1` infinite places. 

### `eight_mul_card_sq_lt`

 In rank `n ≥ 1` the order of decay `10 n³` exceeds `8 n²`, the threshold for integrability on
`U(diag s)`. 

### `hasLargeGap_and_dsCoeff_eq_holMinors`

 In rank `1 ≤ n ≤ t = D.t` let the order `o` put the signs `+1` first, and let the weight `v` be
dominant within each sign block, with gap `300 n_*` between the blocks, `n_* = nStar D`. Let
`2 ρ = twoRho (-o) ⊤`, with entries `#{j | o i < o j} - #{j | o j < o i}`. Then `l = 2 v + 2 ρ` is a
doubled Harish-Chandra parameter of gap `500 n³ + 8 n_*`, and its discrete series coefficient
`dsCoeff` is `holMinors s v`: the quotient `m_{v+c} / m_c` of products of principal minors, where
`c i = 2 ∑ |v j|` at a sign `+1` and `c i = 0` otherwise. 

### `integrable_tail_and_integral_le`

 Let `D` be admissible data, `b = D.b`, `t = D.t`, and let the rank satisfy `1 ≤ n ≤ t`. For an
integer function `o` on the indices let `2 ρ = twoRho (-o) ⊤`, with entries
`#{j | o i < o j} - #{j | o j < o i}`. Let `l = 2 v + 2 ρ` be a doubled Harish-Chandra parameter of
gap `500 n³ + gap`, with `|v i| ≤ 5 b` for all `i`. Then the tail `deg(l) (2 / ‖g‖) ^ (10 n³)`, with
`deg` the formal degree, is integrable on `U(diag s)`, with integral at most
`2 ^ (13 t³) b ^ (14 t²)`. 

### `norm_holMinorsPi_mul_pow_le`

 In rank `1 ≤ n ≤ t = D.t` let the order `o` put the signs `+1` first, and let the weights `u' τ`
be dominant within each sign block, with gap `300 n_*` between the blocks, `n_* = nStar D`. Then
`|m_u'(h)| |h| ^ (6 n_*) ≤ 2 ^ (6 n_*) ∏_τ (2 / ‖h τ‖) ^ (10 n³)` for `h` in the archimedean group
`GInf D.E s`. Here `τ` runs over the infinite places, `m_u' = holMinorsPi s u'` is the product
over `τ` of the quotients of minors `holMinors s (u' τ)`, and `|h| = maxOpNorm h` is the largest
of the operator norms `‖h τ‖`. 

### `integrable_norm_holMinorsPi_mul_pow`

 In rank `1 ≤ n ≤ t = D.t` let the order `o` put the signs `+1` first, and let the weights `u τ`
be dominant within each sign block, with gap `300 n_*` between the blocks, `n_* = nStar D`. Then
`|m_u(h)| |h| ^ (6 n_*)` is integrable on `GInf D.E s`, the product of the groups `U(diag s)` over
the infinite places `τ` of `D.E`. Here `m_u = holMinorsPi s u` is the product over `τ` of the
quotients of minors `holMinors s (u τ)` of weight `u τ`, and `|h| = maxOpNorm h` is the largest of
the operator norms `‖h τ‖`. 

### `integral_norm_holMinorsPi_sq_eq_inv_prod`

 If the factor `holMinors s (u τ)` of `m_u = holMinorsPi s u` is the discrete series coefficient
of parameter `l τ` at every infinite place `τ`, then `∫ |m_u|²` is the inverse of the product of
the formal degrees of the `l τ`. 

### `integral_norm_holMinorsPi_sq_pos`

 In rank `1 ≤ n ≤ t = D.t` let the order `o` put the signs `+1` first, and let the weights `u τ`
be dominant within each sign block, with gap `300 n_*` between the blocks, `n_* = nStar D`. Then
`∫ |m_u|² > 0`, with the integral over `GInf D.E s`, the product of the groups `U(diag s)` over
the infinite places `τ` of `D.E`. Here `m_u = holMinorsPi s u` is the product over `τ` of the
quotients of minors `holMinors s (u τ)` of weight `u τ`. 

### `integral_norm_holMinorsPi_mul_pow_le`

 Let `D` be admissible data, `b = D.b`, `t = D.t`, `n_* = nStar D`, and let the rank satisfy
`1 ≤ n ≤ t`. Let the order `o` put the signs `+1` first. Let the weights `u τ`, `u' τ` at the
infinite places `τ` be dominant within each sign block, with gap `300 n_*` between the blocks, and
let `u` have entries of modulus at most `5 b`. Write `m_u = holMinorsPi s u` for the product of
quotients of minors of weight `u`, and `|h| = maxOpNorm h` for the largest operator norm of `h` at
a place. Then `∫ |m_u|² > 0`, and `|m_u'(h)| |h| ^ (6 n_*)` is integrable with integral at most
`b ^ n_* ∫ |m_u|²`. 

### `integrable_mul_holMinorsPi`

 Let `D` be admissible data (`Data P`), `b = D.b`, `t = D.t`, `n_* = nStar D`, and let the index
type `n` be nonempty with `card n ≤ t`. Let `s` be signs and let the order `o` put the indices of
sign `+1` first. Let the weights `u`, `u'` be K-dominant for `o` within each sign block, with gap
`300 n_*` between the blocks, and let the entries of `u` be at most `5 b` in modulus. Write
`m_u = holMinorsPi s u` and `|h| = maxOpNorm h` for `h` in `GInf D.E s`. If `A` is continuous on
`GInf D.E s` and `|A h| ≤ C |h| ^ (6 n_*)`, then `A m_u'` is integrable and
`|∫ A m_u'| ≤ C b ^ n_* ∫ |m_u|²`. 

### `integrable_holMinorsPi`

 Let `D : Data P`, `t = D.t`, `n_* = nStar D`, and let the rank satisfy `1 ≤ n ≤ t`. Let the
order `o` put the signs `+1` first, and let the weights `u τ` be dominant within each sign block,
with gap `300 n_*` between the blocks. Then `holMinorsPi s u`, the product of quotients of minors of
weight `u`, is integrable. 

### `norm_integral_mul_holMinorsPi_mul_le`

 Let `D` be admissible data, `b = D.b`, `t = D.t`, `n_* = nStar D`, and let the rank satisfy
`1 ≤ n ≤ t`. Let the order `o` put the signs `+1` first, let the weights `u`, `u'` be dominant
within each sign block with gap `300 n_*` between the blocks, the entries of `u` at most `5 b` in
modulus. Write `m_u = holMinorsPi s u` and `|h| = maxOpNorm h`. Let `W`, `K`, `K'` be continuous,
`|W| ≤ M`, and `K`, `K'` both within `δ |h| ^ (6 n_*)` of a function `K₀`. If `∫ W K' m_u' = 0` and
`K m_u' W` is integrable, then `|∫ K m_u' W| ≤ 2 δ M b ^ n_* ∫ |m_u|²`. 

### `integral_mul_norm_apply_one_mul_le`

 Let the order `o` put the signs `+1` first, let `u` be dominant within each sign block, write
`m_u = holMinorsPi s u`, and let `f` be holomorphic of weight `u`: it extends analytically to
products with `o`-triangular matrices, on which it transforms by the character `u`. Let `W θ` be a
family of functions on the group whose mean over the circle is the conjugate of `c m_u`, with
`c ≠ 0`. If `f(h) W θ h` is jointly integrable and `|∫ f W θ| ≤ B` whenever this integral converges,
then `(∫ |m_u|²) |f 1| |c| ≤ B`. 

### `norm_apply_one_le_of_forall_isPeak`

 Let `D` be admissible data (`Data`), of which only these are used: the CM field `E = D.E`, the
set `D.Φ` of its `f` infinite places `τ`, the number `t = D.t`, the weight `b = D.b`, which is very
large against `t`, and `n_* = nStar D = 2 f t³`. For signs `s` on `n` indices, `1 ≤ n ≤ t`, the
group `GInf D.E s` is the product of the groups `U(diag s)` over `τ`, with its Haar measure `dh`,
and `G D.E s` is its product with the finite adelic unitary group. Let the order `o` put the signs
`+1` first. Let the weights `u τ`, `u' τ` be dominant within each sign block, with entries at the
sign `-1` larger by at least `300 n_*` than those at the sign `+1` (`HasHolGap`), and let `u` have
entries of modulus at most `5 b`. Write `m_u' = holMinorsPi s u'` for the product over `τ` of the
quotients of principal minors `holMinors s (u' τ)`, and `|h| = maxOpNorm h` for the largest operator
norm of `h` at a place.

Let `F` on `G D.E s` be continuous and holomorphic of weight `u` in the archimedean variable, with a
peak `z` (`F` is bounded and `|F z|` exceeds half of `sup |F|`), and let `K₀` be bounded. Suppose
that at every peak `x` we have `∫ conj F(x h) K(h) m_u'(h) dh = 0` for some `K` that is holomorphic
of weight `u - u'` and has `|K h - K₀ h| ≤ δ |h| ^ (6 n_*)`. Then `|K₀ 1| ≤ (4 b ^ n_* + 1) δ`. 
