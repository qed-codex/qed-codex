---
{
  "module": "src/New/Determinant/Exchange/TheoremForPartners.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/TheoremForPartners.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/TheoremForPartners.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exchange of theta integrals for matched functions and for data modulo an ideal

The exchange identity compares the theta integrals to U(W) from two spaces of complementary ranks.
For matched functions at the ramified places of a tame character, it holds with a constant whose
absolute value is expressed, up to a factor free of the character, through L-values and the ratio
`New.Exchange.equalRankThetaRatio`. This ratio is the squared absolute value of the theta integral
in equal rank, divided by the product of L-values `L_*` at half the rank of the space. For a
suitable Schwartz vector it is a nonzero constant that does not depend on the character. Together
these give the exchange theorem for finite data given by functions on matrices over `O_E / 𝔪`.

## Main definitions and results

* `New.Exchange.exchange_of_matches`: the exchange identity, with the constant measured by
  `New.Exchange.lValueProdInt` and `New.Exchange.equalRankThetaRatio`.
* `New.Exchange.exists_equalRankThetaRatio_eq_const`: the value of that ratio on `H ⊕ W`, for `W` of
  rank `2 k + 2 q` with `q` negative signs and `k ≤ μ`.
* `New.Exchange.exchange_theorem`, `New.Exchange.exchange_identity`: the exchange theorem, for one
  choice and for all choices of splitting characters.

Notions from other files:
* `New.PairFock E s t` is the Fock space of real data for a pair of spaces with signs `s`, `t`. A
  vector is a Schwartz vector (`New.Exchange.IsSchwartzVector`) if all its moments `fockMoment N v`
  are finite.
* `New.Exchange.thetaIntegral S T a b f` is the function g ↦ ∫ θ^{S,T}_{a,b}(f)(g,h) dh on U(S), the
  integral of the theta kernel `New.pairTheta` over [U(T)]. `New.Exchange.thetaLarge` and
  `New.Exchange.thetaSmall` are its cases for a datum v ⊗ Φ: Φ is read at the ramified places of a
  tame character, or Φ of the transpose is read at their conjugates.
* `New.Exchange.SplitTameChar.semilocalChar` is the character t ↦ ν(t/t̄) of ∏_{w∈S} E_w, t read as
  an idele supported on S, extended by 0 to non-invertible elements.
* `New.Exchange.lValueProd` is the number `L_*(e)` = (∏_{w ∈ S} Nw)^(e²) · ∏_{z=1}^{e}
  |L^S(z, ν)|²; `New.Exchange.lValueProdInt` extends it to integers by `L_*(-e) = L_*(e)⁻¹`.
* `υ` is the splitting character of the Weil data, `upsilonU1` its restriction to the norm-one
  ideles, and `rankTwist a n` is the character `a υ ^ ⌊|n| / 2⌋` of [U(1)].
* `AreMatched O σ χ Φ Ψ` says that `Φ` and `Ψ` are supported on the last rows of `k⁻¹` and the first
  columns of `k`, for `k` invertible over `O` and split by `σ`, and differ there by `χ (det k)`.
* `stdRowDatum σ χ z` and `stdColDatum χ z` are the standard functions of an integral matrix `z`:
  they send `x` to `χ⁻¹` of the determinant of `z` stacked on `x`, respectively of `z * x`, and to
  zero where this is not defined over the integers.
* `localDatum S T v Φ r` is the vector with real part `v`, the function `Φ` at the places that `r`
  reads, and the vacuum elsewhere; `modDatum S T 𝔪 Φ v` is the same for a function `Φ` modulo `𝔪`.

## Relation to the literature

Let V and V' be hermitian spaces of type `New.Space` over a CM field with `New.WeilData` whose ranks
and negative signs add up to those of W, which has q negative signs, with 2q + 2 ≤ rk W and rk
V − rk V' = 2e ≥ 0, and let the weights μ satisfy rk W ≤ 2μ + 2q. Then theta integrals over U(V) and
U(V') agree on matched ramified data up to a nonzero constant c, so theta lifts can be exchanged.
Only |c|² is given, up to an uncomputed factor: it is sized by the conductor and the Hecke L-values
at 1,…,e. Equal theta lifts of characters of complementary groups are known for trivial characters
(Siegel–Weil) and for O(3), O(1) to Mp(2). Related work: Snitz, Theta correspondence of automorphic
characters, J. Number Theory 122 (2007), arXiv math/0509486; Erez, Morphisms of global theta lifts
of non-trivial automorphic characters of orthogonal groups, arXiv 2401.13469, 2024; Gan–Qiu–Takeda,
The regularized Siegel–Weil formula (second term identity) and the Rallis inner product formula,
2014.



## The exchange identity for matched functions

`New.Exchange.exchange_of_matches` compares the theta integrals to U(W) from two spaces V and U of
complementary ranks. The identity at the top of the tower descends by removing planes
(`exists_rowColExchangeIdentity_of_even_rank`), passes from standard data to all matched functions
(`thetaLarge_eq_smul_of_areMatched`), and is translated from `(W, U⁻)` back to `(U, W)`
(`exists_mul_thetaSmall_adjointDatum_eq_mul_integral`).


### `adjointCoords`

 Passing to adjoint maps: the change of coordinates that carries data for the pair `(U, W)` to
data for `(W, U⁻)`. Here `W` has signs `s`, `U` has signs `u` and the opposite space `U⁻` has
signs `-u`. 

### `adjointCoords_finEquiv_apply`

 On finite adelic matrices `adjointCoords` is the conjugate transpose, scaled by the integral
unit `normNegOne` of norm `-1`. 

### `adjointDatum`

 The real vector `y^ad` for `(W, U⁻)` that belongs to a real vector `y` for `(U, W)`: the image
of `y` under the real part of `adjointCoords`. 

### `IsSchwartzVector.adjointDatum`

 Let `U`, `W` have signs `u`, `s` and let `y` be a vector of the real Fock space of `(U, W)` all
of whose moments are finite. Then so are all moments of `adjointDatum y`, the vector for `(W, U⁻)`
obtained by passing to adjoint maps; the opposite space `U⁻` has signs `-u`. 

### `neg_mem_flipSpace_Gamma_iff`

 `New.G.neg` carries the rational points of `U` onto those of the opposite space
`U⁻ = flipSpace U`. 

### `_root_.New.AreMatched.right_eq_pow_mul_apply_smul`

 Multiplying the argument by a unit `ε` of `O` divides the second of two matched functions by
`χ ε ^ card b`, the value of `χ` at the determinant of the scalar matrix `ε` of size `b`. 

### `exists_localDatum_adjointDatum_eq_smul`

 Let `σ` split `n` into `b` and `r`, let `𝔠` be a tame character: a character `ν = 𝔠.character`
of `[U(1)]` of weight `μ`, tamely ramified exactly at a finite set `S = 𝔠.ramifiedPlaces` of split
places, and let `y` lie in the real Fock space of `(U, W)`. There is a number `a` of modulus one
with the following property. Let `Ψ` be a Schwartz–Bruhat function on left invertible matrices that
is matched with some `Φ`: `Φ` is supported on the last rows of `k⁻¹` and `Ψ` on the first columns of
`k` (split by `σ`), for `k` in `GL_n` of the local integers at `S`, and there
`Φ = 𝔠.semilocalChar (det k) * Ψ`. Let `U⁻ = flipSpace U` be the opposite space, `adjointCoords` the
passage to adjoint maps from `(U, W)` to `(W, U⁻)`, and `y^ad = adjointDatum y` the image of `y`.
Then the datum with real part `y^ad`, the function `x ↦ Ψ xᵀ` at the conjugates of `S`
(`𝔠.readsAt.star`) and the vacuum elsewhere is `a` times the image of the datum with real part `y`,
the function `Ψ` at `S` (`𝔠.readsAt`) and the vacuum elsewhere. 

### `exists_mul_thetaSmall_adjointDatum_eq_mul_integral`

 Let `W` have even rank, split by `σ` into `b` and `r`, let `𝔠` be a tame character: a character
`ν = 𝔠.character` of `[U(1)]` of weight `μ`, tamely ramified exactly at a finite set
`S = 𝔠.ramifiedPlaces` of split places, and put `γ = rankTwist ν⁻¹ n = ν⁻¹ υ ^ (rk W / 2)`. There is
a number `d` of modulus one with the following property. Let `Ψ` be a Schwartz–Bruhat function on
left invertible matrices that is matched with some `Φ`: `Φ` is supported on the last rows of `k⁻¹`
and `Ψ` on the first columns of `k` (split by `σ`), for `k` in `GL_n` of the local integers at `S`,
and there `Φ = 𝔠.semilocalChar (det k) * Ψ`. Let `U⁻ = flipSpace U` be the opposite space and
`y^ad = adjointDatum y` the image of `y` under passage to adjoint maps. Then for `g` in the adelic
group `U(W) = G E s`, `γ (det g)` times `thetaSmall`, the theta integral of `(W, U⁻)` over `[U(U⁻)]`
with characters `ν υ ^ (rk W / 2)`, `υ ^ rk U`, real part `y^ad` and `x ↦ Ψ xᵀ` at the conjugates of
`S`, is `d` times the integral over the quotient `[U(U)]` of the theta kernel `pairTheta` of
`(U, W)` with characters `γ`, `γ`, real part `y` and `Ψ` at `S`. 

### `thetaLarge_eq_smul_of_areMatched`

 Let `W` have even rank `rk U + rk V` (`σ`, `h_even`), let `𝔠` be a tame character: a character
`ν = 𝔠.character` of `[U(1)]` of weight `μ`, tamely ramified exactly at a finite set
`S = 𝔠.ramifiedPlaces` of split places, put `χ = 𝔠.semilocalChar`, and let `v`, `y` be real Schwartz
vectors. The standard functions `stdRowDatum σ χ z`, `stdColDatum χ z` send `x` to `χ⁻¹` of the
determinant of `z` stacked on `x`, resp. of `z * x`. Suppose that `thetaLarge` is `c` times
`thetaSmall` on them for all `z` with integral entries. Then the same holds for all matched `Φ`, `Ψ`
with `Ψ` locally constant, and `Ψ` has compact support in the left invertible matrices. 

### `exists_rowColExchangeIdentity_of_even_rank`

 Let `W₀ = H ⊕ W` with `H` a hyperbolic plane, and let `W` have even rank `rk U + rk V` (`σ`,
`h_even`) and as many negative signs (`negCount`) as `V ⊕ U⁻`, with `U⁻` the opposite space
(`h_signs`). For real Schwartz vectors `z` for `(W₀, W₀)` and `y` for `(W, U)` there is a vector `v`
for `(W, V)` with `RowColExchangeIdentity W V U μ σ v y`: `v` and `y` are Schwartz, and there is a
real `C` such that each tame character `𝔠` of weight `μ` has a number `c` with (a) and (b). (a)
`C |c| ^ 2` is `L_*(rk V - rk W / 2)` times the equal rank ratio `|I(z)(1)| ^ 2 / L_*(rk W₀ / 2)`,
where `I(z)` is the theta integral of `(W₀, W₀)` at `z` and `χ⁻¹(det)`, `χ = 𝔠.semilocalChar`. (b)
On the standard functions `stdRowDatum σ χ`, `stdColDatum χ` of each integral matrix (`χ⁻¹` of the
determinant that it completes), `thetaLarge` over `[U(V)]` at `v` is `c` times `thetaSmall` over
`[U(U)]` at `y`. 

### `exchange_of_matches`

 Let `W₀ = H ⊕ W` with `H` a hyperbolic plane, and let `W` have even rank `rk U + rk V` (`σ`,
`h_even`) and as many negative signs as `U` and `V` together (`h_signs`). Let `z` for `(W₀, W₀)` and
`y` for `(U, W)` be real Schwartz vectors. There are `C` and a Schwartz vector `v` for `(W, V)` such
that each tame character `𝔠` of weight `μ` has a number `c` with (a) and (b). Put `ν = 𝔠.character`,
`S = 𝔠.ramifiedPlaces`, `χ = 𝔠.semilocalChar` and `γ = ν⁻¹ υ ^ (rk W / 2)`, where `υ` is the
splitting character of the Weil data on norm-one ideles (`upsilonU1`). (a) `C |c| ^ 2` is
`L_*(rk V - rk W / 2)` times the equal rank ratio `|I(z)(1)| ^ 2 / L_*(rk W₀ / 2)`, where `I(z)` is
the theta integral of `(W₀, W₀)` at `z` and `χ⁻¹(det)`, `L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2)
∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2` and `L_*(-e) = L_*(e)⁻¹` (`lValueProdInt`). (b) For all matched
functions `Φ`, `Ψ` with `Ψ` locally constant, the integral over `[U(V)]` of the theta kernel of
`(W, V)` with characters `γ`, `1` at `(v, Φ)` is `c` times the integral over `[U(U)]` of the theta
kernel of `(U, W)` with characters `γ`, `γ` at `(y, Ψ)`, as functions on `U(W) = G E s`. 


## The value of the equal rank theta integral

For `W₀ = H ⊕ W` of even rank and a Schwartz vector `v`, the theta integral of `(W₀, W₀)` on `v` and
the datum `χ⁻¹(det)` is a constant `I₀(v)`. Let `rk W = 2 k + 2 q`, where `q` is the number of
negative signs of `W`, and `k ≤ μ`. We find `v` with `|I₀(v)| ^ 2 = C L_*(rk W₀ / 2)`, where `C ≠ 0`
does not depend on the character (`exists_equalRankThetaRatio_eq_const`). The value for the standard
positive definite `W` (`exists_equalRankThetaRatio_const_ne_zero`) is carried up one hyperbolic
plane at a time; the ratio depends only on the signs of `W₀` (`equalRankThetaRatio_eq_of_signs_eq`).

Let `J` be positive definite of rank `2 k`, `k ≤ μ`, and `Y = H ⊕ J`. For a space `X` write
`r_X(v) = |I(v)(1)| ^ 2 / L_*(rk X / 2)` (`equalRankThetaRatio`), where `I(v)` is the theta integral
of `(X, X)`. Put `L_*(-k) = L_*(k)⁻¹`.

1. Non-vanishing (`exists_equalRankThetaRatio_ne_zero`). Fix the character, and suppose `r_Y(v) = 0`
   for all `v`. The periods that compute the Fourier coefficients for `(H ^ (2 k) ⊕ Y, J⁻ ⊕ Y)` are
   then zero, so this theta integral vanishes on standard data at every Schwartz vector
   (`thetaLargeVanishes_of_equalRankThetaRatio_eq_zero`). Vanishing descends along the `2 k + 1`
   planes to `(J, 0)` (`ThetaLargeVanishes.of_add_planes`, which uses the functional equation of
   `L`). But there the integral of the vacuum is a volume, not zero.
2. The identity used twice (`exists_equalRankThetaRatio_sq_eq`). Fix `v` for `(Y, Y)`. The identity
   for `(J, J, 0)` gives `y` such that `I(y)` is a constant `c₁` times a volume, with
   `B |c₁| ^ 2 = L_*(k) r_Y(v)`. The identity for `(J, 0, J)`, with `y` on the right, gives a number
   `ξ` and `c₂` with `C |c₂| ^ 2 = L_*(-k) r_Y(v)`. Integrating the theta kernel of `y` over both
   groups, in both orders, gives `ξ = c₁ c₂`. So `r_Y(v) ^ 2 = B C |ξ| ^ 2`, where `B`, `C`, `ξ` do
   not depend on the character.
3. The first floor (`exists_equalRankThetaRatio_const_ne_zero`). For the `v` that step 1 gives for
   one character, `r_Y(v) ≥ 0` is one nonzero number for all characters.
4. Adding a plane (`exists_equalRankThetaRatio_add_plane`). Let `W' = W ⊕ H` and `rk W = 2 d`. Given
   `v` for `(W, W)`, choose `v'` for `(W', W')` whose cone integral has the theta integrals of `v`.
   The constant function `I(v')` equals its constant term `κ I(v)(1)`, and `|κ| ^ 2` is a constant
   times `L_*(d + 1) / L_*(d)`.


### `integral_thetaOnRealData_eq_zero`

 Let `𝔠` be a tame character, `χ = 𝔠.semilocalChar` and `γ = rankTwist 𝔠.character⁻¹
n = 𝔠.character⁻¹ υ ^ ⌊rk W / 2⌋`. Suppose that `thetaLarge`, the theta integral of `(W, W)` over
the second `[U(W)]` with characters `γ`, `γ`, vanishes at the finite datum `χ⁻¹(det)`
(`stdColDatum χ 1`) for all real Schwartz vectors, and let `w` be such a vector for `(W, V.sum W)`.
Form `thetaOnRealData`, the theta series as a functional of the real vector, with characters `γ` and
`γ β` for any character `β`, and finite datum `f ⊗ χ⁻¹(det)` (`boxProd` of `f` for `(W, V)` and
`namedVector`, the vacuum with this function put in at the ramified places, which `𝔠.readsAt`
reads), after the Heisenberg translation by the adelic matrix with rows `x` for `V` and `0` for `W`.
Then for `g` in `U(W)` and `y` in `U(V)` its value at `w` and `(g, (y, l))` has integral zero over
`l` in `[U(W)]`. 

### `isSchwartzVector_realPairWeil`

 The real Weil representation `realPairWeil` of a pair of unitary groups with signs `s`, `t` and
weights `γ`, `γ'` preserves the Fock vectors all of whose moments are finite. 

### `thetaLargeVanishes_of_equalRankThetaRatio_eq_zero`

 Let `J = stdSpace E m` be positive definite of even rank `2 k`,
`Y = H ⊕ J = hyperbolicSum Unit J` with `H` a hyperbolic plane, and `𝔠` a tame character: a
character `ν = 𝔠.character` of `[U(1)]` of weight `μ`, tamely ramified exactly at a finite set
`S = 𝔠.ramifiedPlaces` of split places. Suppose that the equal rank ratio of `Y`, the normalised
square of the theta integral of `(Y, Y)` at `1`, is zero at every Schwartz vector. Then the theta
integral of the pair `(H ^ (2 k) ⊕ Y, J⁻ ⊕ Y)` vanishes at every Schwartz vector and every standard
datum: `𝔠.semilocalChar⁻¹` of the determinant of an integral `m`-row matrix completed by a variable
one, the rows being ordered by `sumAssoc`. 

### `exists_equalRankThetaRatio_ne_zero`

 Non-vanishing: let `J = stdSpace E m` be the positive definite space of rank `2 k` and let
`k ≤ μ w` at every infinite place `w`. Let `𝔠` be a tame character: a character of `[U(1)]` of
weight `μ`, tamely ramified exactly at a finite set of split places. There is a Schwartz vector `v`
at which the equal rank ratio of `Y = H ⊕ J = hyperbolicSum Unit J`, the normalised square of the
theta integral of `(Y, Y)` at `1`, is not zero. 

### `eq_mul_of_integral_pairTheta`

 Let `J` be positive definite. Let the integral of the theta kernel of `(J, J)` over the target
group be the constant `a`, and let `c` times its integral over the source group be the constant `b`.
Then `b = c a`, by Fubini's theorem. 

### `exists_thetaLarge_eq_mul_quotMeasure`

 The exchange identity for `(J, J, 0)`. Let `J` be positive definite of rank `2 k` and `v` a
Schwartz vector for `(H ⊕ J, H ⊕ J)`, with `H` a hyperbolic plane. There are `B` and a Schwartz `y`
for `(J, J)` such that, for each tame character `𝔠` of weight `μ`, the theta integral of `y` and the
finite datum `stdColDatum χ 1`, the function `χ⁻¹(det)` for `χ = 𝔠.semilocalChar`, is a constant `c`
times the volume of `[U(0)]`, where `B |c| ^ 2` is `L_*(k)` times the equal rank ratio
`|I(v)(1)| ^ 2 / L_*(k + 1)`. Here `I(v)` is the theta integral at `v` and `χ⁻¹(det)`, and
`L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2` for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`. 

### `exists_quotMeasure_mul_eq_mul_integral_pairTheta`

 The exchange identity for `(J, 0, J)`. Let `J` be positive definite of rank `2 k`, and let `v`
for `(H ⊕ J, H ⊕ J)`, with `H` a hyperbolic plane, and `y` for `(J, J)` be Schwartz vectors. There
are `C` and a number `ξ` such that each tame character `𝔠` of weight `μ` has a number `c` as
follows. The volume of `[U(0)]` times `ξ` is `c` times the integral over the first `[U(J)]` of the
theta kernel of `(J, J)` with both characters `γ = ν⁻¹ υ ^ k` and datum `y` at the infinite places,
`χ⁻¹(det)` (`stdColDatum χ 1`) at `S` and the vacuum elsewhere (`localDatum`), and `C |c| ^ 2` is
`L_*(-k) = L_*(k)⁻¹` times the equal rank ratio `|I(v)(1)| ^ 2 / L_*(k + 1)`. Here
`ν = 𝔠.character`, `S = 𝔠.ramifiedPlaces`, `χ = 𝔠.semilocalChar`, `υ` is the splitting character of
the Weil data on norm-one ideles, `I(v)` is the theta integral at `v` and `χ⁻¹(det)`, and
`L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2`. 

### `exists_equalRankThetaRatio_sq_eq`

 The exchange identity used twice. Let `J` be positive definite of rank `2 k` and `v` a Schwartz
vector for `(H ⊕ J, H ⊕ J)`, with `H` a hyperbolic plane. As `𝔠` runs through the tame characters of
weight `μ`, the square of the equal rank ratio `|I(v)(1)| ^ 2 / L_*(k + 1)` is one number `D`. Here
`I(v)` is the theta integral `thetaLarge` with real part `v` and the function `χ⁻¹(det)` at the
ramified places, `χ = 𝔠.semilocalChar`, and `L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i,
ν)| ^ 2` for `ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`. 

### `exists_equalRankThetaRatio_const_ne_zero`

 The value on the first floor. Let `J` be the standard positive definite space of rank `2 k` and
`k ≤ μ` at every infinite place. Some Schwartz vector `v` for `(H ⊕ J, H ⊕ J)` has an equal rank
ratio that is one number `C ≠ 0` for all tame characters of weight `μ`. 

### `exists_equalRankThetaRatio_add_plane`

 Adding a plane. Let `W` have even rank and let `A` be an adapted splitting `W' = W ⊕ H` with `H`
a hyperbolic plane (its frames are orthonormal at the infinite and integral at the finite places).
Each Schwartz vector `v` for `(W, W)` has a Schwartz vector `v'` for `(W', W')` whose equal rank
ratio is `C` times the ratio `|I(v)(1)| ^ 2 / L_*(rk W / 2)` of `v`. The constant `C > 0` is the
same for all tame characters `𝔠` of weight `μ`. Here `I(v)` is the theta integral `thetaLarge` with
real part `v` and the function `χ⁻¹(det)` at the ramified places, `χ = 𝔠.semilocalChar`, and
`L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2` for `ν = 𝔠.character` and
`S = 𝔠.ramifiedPlaces`. 

### `equalRankThetaRatio_eq_of_signs_eq`

 Let `Y` have even rank and let `A` be an adapted splitting `Y = W ⊕ H` with `H` a hyperbolic
plane (its frames are orthonormal at the infinite and integral at the finite places). Let `Y₁` be
any space with the signs of `Y`, `𝔠` a tame character and `v` a Schwartz vector (all Fock moments
finite). Then the equal rank ratio `|I(1)| ^ 2 / L_*(rank / 2)` is the same for `Y₁` and `Y`, where
`I` is the theta integral of `v` and `𝔠.semilocalChar⁻¹(det)` for the pair `(Y₁, Y₁)`, resp.
`(Y, Y)`, and `L_* = lValueProdInt 𝔠` is a product of partial L-values of `𝔠`. 

### `exists_equalRankThetaRatio_eq_const`

 The value of the equal rank ratio. Let `rk W = 2 k + 2 q`, where `q` is the number of negative
signs of `W`, and `k ≤ μ` at every infinite place. There are a Schwartz vector (all Fock moments
finite) `v` for `(H ⊕ W, H ⊕ W)`, with `H` a hyperbolic plane, and `C ≠ 0` such that
`|I(v)(1)| ^ 2 / L_*(rk W / 2 + 1) = C` for every tame character `𝔠` of weight `μ`. Here `I(v)` is
the theta integral `thetaLarge` with real part `v` and the function `χ⁻¹(det)` at the ramified
places, `χ = 𝔠.semilocalChar`, and `L_*(e) = ∏_{w ∈ S} q_w ^ (e ^ 2) ∏_{1 ≤ i ≤ e} |L^S(i, ν)| ^ 2`
for `ν = 𝔠.character` and `S = 𝔠.ramifiedPlaces`. 


## The exchange theorem for data modulo an ideal

`New.Exchange.exchange_theorem` exchanges a theta integral over `[U(V)]` for one over `[U(V')]`, for
finite data given by functions on matrices over `O_E / 𝔪`. It is deduced from
`New.Exchange.exchange_of_matches`, the same exchange for data on the completions at the primes of
`𝔪`, and the value `New.Exchange.exists_equalRankThetaRatio_eq_const`.


### `spaceChar_mul_spaceChar_eq_iff`

 The space character `α.spaceChar p` is the Hecke character `x ↦ α (x / x̄) υ x ^ (-p)`. In even
rank `card N = p + q` those of `α` in rank `p` and of `α'` in rank `q` multiply to the inverse of
the base change `x ↦ ν (x / x̄)` exactly if `α * α' = rankTwist ν⁻¹ N = ν⁻¹ υ ^ (card N / 2)`. 

### `exists_areMatched_modDatum_eq`

 Let `W`, `V`, `V'` be spaces with coordinates indexed by `n`, `a`, `b`, split by
`σ : b ⊕ a ≃ n`, and let the tame character `𝔠` be ramified exactly at the primes of the modulus
`𝔪`. Let `Φ`, `Ψ` be matched functions over `O_E / 𝔪` for the product `χ` of the residue characters
of `𝔠`: `Φ` is supported on the last rows of `k⁻¹` and `Ψ` on the first columns of `k` (split by
`σ`), for `k` in `GL_n(O_E / 𝔪)` (the subring `⊤`), and there `Φ = χ (det k) * Ψ`. Then there are
functions `Φ'`, `Ψ'` on matrices over the completions at these primes, matched over the local
integers `SemilocalField.O` for `𝔠.semilocalChar`, with `Ψ'` locally constant, that give the same
adelic data as `Φ` for `(W, V)` and `Ψ` for `(V', W)`, whatever the real vector. 

### `exchange_theorem`

 Let `W`, `V`, `V'` have ranks `|n| = |b| + |a|` (split by `σ`), `|a| = |b| + 2e` and `|b|`. Let
`W` have as many negative signs `q` as `V` and `V'` together, with `2q + 2 ≤ |n|`. Let the weights
satisfy `|n| ≤ 2 μ + 2q`, and let `v` be a real Schwartz vector for `(V', W)`. There are `C` and a
Schwartz `x` for `(W, V)` such that every character `ν` of `[U(1)]` of weight `μ` that is tame for
`(𝔪, χ)` (ramified exactly at the primes of `𝔪`, with residue character `χ`) has some `c ≠ 0` with
(a) and (b). (a) `‖c‖²` is `C` times `lValueProd 𝔪.places ν e`, a power of the norm of the primes of
`𝔪` times the product of the squares of the partial L-values `|L^S(z, ν)|` for `z = 1, …, e`, with
`S` the primes of `𝔪`; so `C > 0` as soon as such a `ν` exists. (b) For all matched functions `Φ`,
`Ψ` modulo `𝔪`, the theta integral of `(x, Φ)` over `[U(V)]` is `c` times that of `(v, Ψ)` over
`[U(V')]`, as functions on `U(W)`. The left side has the characters `γ` and `1`, the right side `γ`
and `γ`, with `γ = rankTwist ν⁻¹ n = ν⁻¹ υ ^ (|n| / 2)`. 

### `exchange_identity`

 Let `W`, `V`, `V'` have ranks `|n| = |b| + |a|` (split by `σ`), `|a| = |b| + 2e`, `|b|`. Let `W`
have as many negative signs `q` as `V` and `V'` together, with `2q + 2 ≤ |n| ≤ 2 μ + 2q`, and let
`v` be a real Schwartz vector for `(V', W)`. There are `C > 0` and a Schwartz vector `x` for
`(W, V)`, chosen before `𝔪` and `ν`, such that every character `ν` of `[U(1)]` of weight `μ` that is
tame for `(𝔪, χ)` has a number `c` as follows. Its size is `‖c‖² = C * lValueProd 𝔪.places ν e ≠ 0`.
For all `α`, `α'` such that the characters `α.spaceChar |a|` of `V` and `α'.spaceChar |b|` of `V'`
have product inverse to the base change `x ↦ ν (x / x̄)`, and all matched functions `Φ`, `Ψ` modulo
`𝔪`, the theta integral of `(x, Φ)` over `[U(V)]` is `c` times that of `(v, Ψ)` over `[U(V')]`, as
functions on `U(W)`. The character of `W` is `rankTwist ν⁻¹ n = ν⁻¹ υ ^ (|n| / 2)`, and `modDatum`
puts a function modulo `𝔪` at the primes of `𝔪` and the vacuum at the other finite places. 
