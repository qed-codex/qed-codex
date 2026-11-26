---
{
  "module": "src/New/Determinant/Exchange/EquivariantDifference.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/EquivariantDifference.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/EquivariantDifference.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The difference in the exchange identity as an equivariant lift

This file is a step towards the identity between theta integrals over `U(V)` and `U(V')`, where
`rk W = rk V + rk V'`. The identity is taken for matched functions `Φ`, `Ψ` at the ramified places
of the tame character `𝔠`. This file defines the small side `New.Exchange.thetaSmall`. It proves
how `thetaLarge` and `thetaSmall` change under translation at the ramified places, and that both
are invariant under the integral points of `U(W)` that are trivial there. From this it shows that
the difference of the two sides is an equivariant lift.

## Main definitions and results

* `New.Exchange.thetaSmall`: the theta integral for `V'` of the datum `Ψ`.
* `New.Exchange.exists_isEquivariantLift_eq_thetaLarge_sub_smul`: the difference
  `thetaLarge Φ - c • thetaSmall Ψ` is a linear map of `Ψ` alone, on a `GL_n`-stable space, and is
  equivariant (`New.Exchange.IsEquivariantLift`).

Notions from other files:
* `thetaIntegral S T α β f`: the integral over `[U(T)]` of the theta kernel of the datum `f`.
* `thetaLarge W V 𝔠 v Φ`: the theta integral over `[U(V)]` of the datum `v ⊗ Φ`.
* `localChar P ξ k`: the character `t ↦ ξ t * |t| ^ (k / 2)` of the completions at `P`.
* `sameSectionPairs χ σ`: pairs `(Φ, Ψ)` of Schwartz–Bruhat functions on `a × n` and `n × b`
  matrices, `σ : b ⊕ a ≃ n`, whose values of `localSection χ` at the blocks of `k` differ by
  `χ (det k)`.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work.


### `thetaSmall`

 The small side: the theta integral over `U(V)`, as a function on `U(W)`, of the datum with real
part `v` and component `y ↦ Ψ yᵀ`, read in the model at the conjugates of the ramified places of
`𝔠`. The two characters of `U(1)` are `ν υ ^ ⌊rk W / 2⌋` (`rankTwist`) and `υ ^ rk V`, where
`ν = 𝔠.character`. Here `υ` is the splitting character of the Weil data, restricted to the norm-one
ideles (`upsilonU1`). In the exchange identity it is applied to the space `V'`. 

### `IsTargetBounded.pairWeil_one_left`

 Polynomial growth of the theta kernel on `U(W)`, uniform on `U(V)` (`IsTargetBounded`), is kept
when the datum is moved by an element `k` of `U(V)`. 

### `thetaIntegral_smul`

 The theta integral is homogeneous in the datum. 

### `ReadsAt.pairWeil_localDatum_of_mem_supportedOn`

 Let `π` be a ring map from the finite adeles of the CM field `E` to `F` that reads the
components at a set `A` of places (`ReadsAt`): `A` is disjoint from its conjugate, `π` has a
continuous additive section onto the `A`-part, and `π x` is integral exactly if `x` is so at `A`.
Let `φ` be Schwartz–Bruhat, vanishing outside some set `U`, and let `g ∈ U(W)`, `h ∈ U(V)` be finite
points supported on `A` and its conjugate. In the Weil representation (`pairWeil`), `(g, h)` moves
the datum of `φ` to that of `x ↦ φ (π h⁻¹ * x * π g)`. Here the datum (`localDatum`) is the vector
`v` of the Fock space `PairFock` at the infinite places, `φ` at `A` and the vacuum elsewhere. The
new datum is multiplied by `χ_W (det h) / χ_V (det g) * |det g| ^ (rk V / 2) / |det h| ^ (rk
W / 2)`. The determinants are taken on `A` (`detOn`) and `|·|` is `ideleAbs`.
`χ_W = α.spaceChar (rk W)` and `χ_V = β.spaceChar (rk V)`. 

### `pairWeil_inv_localDatum`

 Let `𝔠` be a split tame character: a character `ν = 𝔠.character` of the norm-one ideles, tamely
ramified exactly at a finite set `S = 𝔠.ramifiedPlaces` of places disjoint from its conjugate. Let
`rk W` be even and let `k ∈ U(V)` be finite (`Gf`), supported at `S` and its conjugate, with
component `k_S` at `S`. Consider the datum `localDatum W V v Φ 𝔠.readsAt`: `v` at the infinite
places, the function `Φ` at `S` and the vacuum elsewhere. It lies in the Weil representation
`pairWeil` of `(W, V)` with both characters `ν⁻¹ υ ^ ⌊rk W / 2⌋` (`rankTwist`), `υ` being the
splitting character of the Weil data. Then `k⁻¹` moves it to the same datum with `x ↦ Φ (k_S * x)`
in place of `Φ`, times the value at `det k_S` of `t ↦ ν (t / t̄) |t| ^ (rk W / 2)` (`localChar`).
Here `Φ` is Schwartz–Bruhat on the matrices `x` of full row rank. 

### `thetaLarge_translate_mul`

 Let `𝔠` be a split tame character, with character `ν` of the norm-one ideles and finite set `S`
of ramified places. Let `rk W = card b + rk V` (`σ`) be even, and let `χ` be the character
`t ↦ ν (t / t̄) |t| ^ (rk W / 2)` at `S` (`localChar`). Let `(Φ, Ψ)` be a same-section pair for `χ`
and `σ`: both are Schwartz–Bruhat on matrices of full rank, and for each invertible `k` the coset
sum `localSection χ` of `y ↦ Φ yᵀ` at the transposed rows `a` of `k⁻¹` is `χ (det k)` times that of
`Ψ` at the columns `b` of `k`. By `thetaLarge W V 𝔠 v Φ` is meant the function on `U(W)` that
integrates over `[U(V)]` the theta kernel of the datum `v` at the infinite places, `Φ` at `S`, the
vacuum elsewhere, both characters being `ν⁻¹ υ ^ ⌊rk W / 2⌋` for the splitting character `υ` of the
Weil data. Let `g ∈ U(W)` be finite, supported at `S` and its conjugate, with component `g_S` at
`S`. Then `thetaLarge` of `y ↦ χ (det g_S⁻¹) Φ (y g_S⁻¹)` at `x g` is that of `Φ` at `x` divided by
`(υ |·| ^ (1 / 2)) (det g_S) ^ card b`. 

### `thetaSmall_translate_mul`

 By `thetaSmall W V' 𝔠 v' Ψ` is meant the function on `U(W)` that integrates over `[U(V')]` the
theta kernel of the datum `v'` at the infinite places and `y ↦ Ψ yᵀ` at the conjugates of the
ramified places `S` of `𝔠`; the space `V'` has rank `card b`. Let `g ∈ U(W)` be finite, supported at
`S` and its conjugate, with component `g_S` at `S`. If `y ↦ Ψ (g_S y)` is Schwartz–Bruhat, its
`thetaSmall` at `x g` is `thetaSmall Ψ` at `x` divided by `(υ |·| ^ (1 / 2)) (det g_S) ^ card b`,
where `υ` is the splitting Hecke character of the Weil data. 

### `thetaLarge_mul_of_mem_stdLevel`

 For Schwartz–Bruhat `Φ`, `thetaLarge Φ` is right invariant under the integral points `k` of
`U(W)` that are trivial at the ramified places of `𝔠`. 

### `thetaSmall_mul_of_mem_stdLevel`

 For Schwartz–Bruhat `Ψ`, `thetaSmall Ψ` is right invariant under the integral points `k` of
`U(W)` that are trivial at the ramified places of `𝔠`. 

### `exists_linear_thetaSmall`

 For `v'` with all moments finite, `thetaSmall` is linear on Schwartz–Bruhat functions. 

### `exists_linear_thetaLarge`

 Let `rk W = rk V' + rk V` be even and `v` have all moments finite. Let `ν` be the character of
`𝔠`, `S` its ramified places, and let `thetaLarge W V 𝔠 v Φ` be the theta integral over `[U(V)]` of
the datum `v` at the infinite places and `Φ` at `S`, as a function on `U(W)`. A same-section pair
`(Φ, Ψ)` for `χ t = ν (t / t̄) |t| ^ (rk W / 2)` consists of Schwartz–Bruhat functions on `a × n`
and `n × b` matrices at `S` whose coset sums `localSection χ` at complementary blocks of each
invertible `k` differ by the factor `χ (det k)`. On these pairs `thetaLarge Φ` is a linear function
of `Ψ`. 

### `exists_isEquivariantLift_eq_thetaLarge_sub_smul`

 Let `𝔠` be a split tame character, with character `ν` of the norm-one ideles and finite set `S`
of ramified places, and let `υ` be the splitting Hecke character of the Weil data. Let
`rk W = rk V' + rk V` be even, `v`, `v'` real data with all moments finite, `c ∈ ℂ`. There are a
space `M` of functions on matrices at `S` and a linear map `𝒟` with (a) and (b). (a) `M` consists of
Schwartz–Bruhat functions and is stable under translation. `𝒟` maps `M` to automorphic functions on
`U(W)`. It is equivariant at `S` for the inverse of `υ ^ card b |·| ^ (card b / 2)` of the
determinant. It is invariant under the integral points elsewhere (`IsEquivariantLift`). (b) Let `Ψ`
be locally constant with a matched function `Φ`: both are supported on blocks of integral invertible
`k`, where their values differ by `𝔠.semilocalChar (det k)`, for the character
`𝔠.semilocalChar : t ↦ ν (t / t̄)` at `S`. Then `Ψ` lies in `M`, and
`𝒟 Ψ = thetaLarge Φ - c • thetaSmall Ψ`. 
