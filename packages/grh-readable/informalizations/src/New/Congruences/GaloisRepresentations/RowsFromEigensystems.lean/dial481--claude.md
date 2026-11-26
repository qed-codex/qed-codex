---
{
  "module": "src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Main summand conditions on Hodge–Tate jumps and existence of main summands for Hecke eigensystems

This file passes from Hecke eigensystems of forms to the main summands (`New.Selmer.IsMainSummand`)
that enter the Selmer groups. The Hodge–Tate jumps occurring for the main summands of the descent
pairs (W_j, V_j) satisfy the numerical conditions `New.Selmer.IsMainSummandWeights`. Each such jump
is small or near `∓ w_j`, and few jumps are small. At a pair of conjugate embeddings at most
rank-many jumps are negative.

## Main definitions and results

* `New.Selmer.isMainSummandWeights_mainPair`: the single jump of a main pair obeys
  `New.Selmer.IsMainSummandWeights` in rank `1`.
* `New.Selmer.isMainSummandWeights_descentPair`: the jumps built from `New.Data.targetParameter` and
  `New.Data.liftWeight` obey `New.Selmer.IsMainSummandWeights` in rank `D.r`.
* `New.Selmer.exists_isMainSummand_of_isRepOfType`: take a representation `R` with admissible labels
  whose shifted jumps obey `New.Selmer.IsMainSummandWeights`. Assume its traces are limits of the
  values of `b`. Then it gives a representation `T` with `New.Selmer.IsMainSummand O b T`.
* `New.Selmer.exists_isMainSummand_descentPair`: a Hecke eigensystem of a good form on
  `D.spaceW D.m` gives a main summand for each descent pair of the trivial twist.

Notions from other files:
* `New.Selmer.IsMainSummandWeights D r t J`: numerical conditions on the jumps `J σ`, a multiset of
  integers for each complex embedding `σ` of the CM field `D.E`.
* `New.Selmer.IsMainSummand O z T`: `T` is like a main summand, and for every twist of the pair `O`
  by a tame character `ϑ` the normalised representation attached to a lift of the system `z` has the
  trace of `T` twisted by `ϑ⁻¹` plus a string of powers of the inverse cyclotomic character.
* `New.Selmer.IsLiftSetting O c ϑ`: the descent pair `O` fits the twist `ϑ` and the labels `c` are
  admissible.
* `New.Selmer.IsRepOfType O k J c S R`: `R` is a conjugate self-dual representation of level `S`
  (`New.Selmer.IsConjSelfDualOfLevel`) with jumps `J`, and inertia at the chosen places acts through
  the roots of the labels `c`.
* `New.Data.goodForms`, `New.Data.eigenPart`: the image of the idempotent e₀ on forms of principal
  level at the chosen places, and the forms on which the Hecke operators act by given scalars.

## Relation to the literature

The Galois representation of each eigenform in a space of theta lifts has the trace of a twisted
block, which does not depend on the twist, plus a string of powers of the inverse cyclotomic
character. This shape follows from the unramified theta correspondence. Related work: Rallis,
Langlands' functoriality and the Weil representation, 1982; Khare–Larsen–Savin, Functoriality and
the inverse Galois problem, 2008; Arias-de-Reyna–Dieulefait–Shin–Wiese, Compatible systems of
symplectic Galois representations III, 2015.


 ## The jumps of descent pairs and of main pairs satisfy the conditions on a main summand 

### `cmSign_star`

 The sign `cmSign` of a complex embedding (`1` on the CM type, `-1` off it) changes under complex
conjugation. 

### `abs_descentPair_weight_add_liftWeight_le`

 Let `D` be admissible data (`Data P`) over the CM field `D.E`, with rank `r = D.r`, number of
lifts `m = D.m`, `k = D.k = r + 1 - m` and `t = D.t = 5 r`. At a complex embedding `σ` of `D.E`,
over the infinite place `v`, the `q`-th jump (Hodge–Tate weight) of the `j`-th descent pair is the
integer `u = t / 2 - ε (λ_q + w_j)`. Here `t / 2` is integer division, `ε = cmSign σ` is `1` on the
CM type and `-1` off it, `λ_q = D.targetParameter v q` is the fixed parameter of the rank `r` group
and `w_j = D.liftWeight j v` is minus the weight of the character of the `j`-th lift. For
`q + 1 < k` the jump is high: `|ε u + w_j| ≤ t`. 

### `le_natAbs_descentPair_jump_and_le`

 Let `D` be admissible data over the CM field `D.E`, with `r = D.r`, `m = D.m`, `k = D.k` and
`Δ = D.gap`. Let `1 ≤ j ≤ m` (`D.LiftIndex`). At a complex embedding `σ` over the infinite place
`v`, the `q`-th jump (Hodge–Tate weight) of the `j`-th descent pair is the integer
`u = t / 2 - ε (λ_q + w_j)`, with `t = D.t`, `ε = cmSign σ = ±1` (`1` on the CM type),
`λ_q = D.targetParameter v q` and `w_j = D.liftWeight j v`, minus the weight of the character of
the `j`-th lift. For `k ≤ q + 1 ≤ r` the jump is low: `Δ / 4 ≤ |u| ≤ 2 m Δ`. 

### `countP_low_weights_descentPair`

 Let `D` be admissible data, `1 ≤ j ≤ m = D.m` and `σ` a complex embedding of the CM field `D.E`
over the infinite place `v`. The jumps (Hodge–Tate weights) of the `j`-th descent pair at `σ` are
the `r = D.r` integers `t / 2 - ε (λ_q + w_j)`, `q < r`, where `t = D.t`, `ε = cmSign σ = ±1`,
`λ_q = D.targetParameter v q` and `w_j = D.liftWeight j v` is minus the weight of the character of
the `j`-th lift. If `2 m Δ ≤ B` and `B + t < w_j`, with `Δ = D.gap`, then exactly `m` of them have
modulus at most `B`. 

### `isMainSummandWeights_descentPair`

 Let `1 ≤ j ≤ m` (`D.LiftIndex`, `m = D.m`). At a complex embedding `σ`, over the infinite place
`v`, take as jumps (Hodge–Tate weights) the `r = D.r` integers `t / 2 - ε (λ_q + w_j)`, `q < r`, of
the `j`-th descent pair. Here `t = D.t`, `ε = cmSign σ` is `1` on the CM type and `-1` off it,
`λ_q = D.targetParameter v q` is the fixed parameter of the rank `r` group, and
`w_j = D.liftWeight j v` is minus the weight of the character of the lift. These jumps satisfy
`IsMainSummandWeights D r t`. 

### `abs_mainPair_weight_add_liftWeight_le`

 Let `p` be a critical pair of the data `D`: an integer `z = p.z` and a character of `U(1)` of
weight `-c`, with `c = p.negWeight`. Let it be a main pair for `j` (`IsMainPair`): in particular
`m < z ≤ r` and `w_j + r - t ≤ c ≤ w_j`, where `m = D.m`, `r = D.r`, `t = D.t = 5 r` and
`w_j = D.liftWeight j` is minus the weight of the character of the `j`-th lift. At a complex
embedding `σ` over the infinite place `v`, with `ε = cmSign σ = ±1`, the jump (Hodge–Tate weight)
of `p` is `u = z - 1 - ε c v`. It is high: `|ε u + w_j v| ≤ t`. 

### `isMainSummandWeights_mainPair`

 Let `p` be a main pair for `j` (`IsMainPair`): an integer `z = p.z` and a character of `U(1)` of
weight `-c`, `c = p.negWeight`, with in particular `m < z ≤ r` and `w_j + r - t ≤ c ≤ w_j`, where
`w_j = D.liftWeight j` is minus the weight of the character of the `j`-th lift. At a complex
embedding `σ` over the infinite place `v`, take the single jump (Hodge–Tate weight)
`z - 1 - ε c v`, with `ε = cmSign σ` equal to `1` on the CM type and `-1` off it. These jumps
satisfy `IsMainSummandWeights D 1 (2 z - 1)`, the conditions on the jumps of a rank one
representation that is paired with `2 z - 1` consecutive powers of the inverse cyclotomic character:
each is low or within `t` of `-ε w_j`, few are small, and at most one at `σ` and its conjugate is
negative. 

 ## One main summand for all twists, and main summands from eigensystems of good forms 

### `apply_one_eq_of_heckePolyEval_eq`

 Let `r` and `n` be nonempty. Suppose that, for all `X`, the Hecke polynomial at `w` of rank `n`
with eigenvalues `s` equals `qPochhammer q t (α X) = ∏_{l < t} (1 - q ^ l α X)` times the Hecke
polynomial of rank `r` with eigenvalues `z` at `β X`, where `q` is the norm of `w`. Comparing the
linear terms gives `s 1 = β z 1 + (∑_{i < t} q ^ i) α z 0`. 

### `IsRepOfType.isMainSummandLike_twistByChar`

 Let `O` be a descent pair over the CM field `D.E` of the data `D`: two spaces of dimensions
`r < n`, a character `μ = O.u1Char` of `U(1)` of weight `O.weight`, and chosen places
`O.chosenPlace i`. Put `t = O.rankDiff = n - r` and assume `r - t = 2 a`. Let `c` give for each
chosen place a polynomial over its residue field, admissible for `O` and the trivial twist
(`IsLiftSetting`). Let `R` be an `r`-dimensional `ℓ`-adic Galois representation of `D.E` that is
conjugate self-dual, unramified off the places that `O` allows (empty extra level), has jumps
(Hodge–Tate weights) `J`, and whose inertia at the chosen places acts through the roots of `c`
(`IsRepOfType`). Lower the jumps at each embedding `σ` by `a - cmSign σ * O.weight v`, with `v` the
place of `σ` and `cmSign σ = ±1`, and suppose that they obey the numerical conditions
`IsMainSummandWeights`. Then `R` twisted by the avatar of `O.hasWeight.inv.toAlgebraic 0 a`, the
algebraic Hecke character `μ⁻¹(x / x̄) |x| ^ a`, is like a main summand (`IsMainSummandLike`) with
the lowered jumps and string length `t`. 

### `neg_coeff_eq_of_hasLiftHeckePolynomial`

 Let the nonzero form `y` of the descent pair `V` of ranks `0 < r < n` lift the system `b` of
Hecke eigenvalues, and let `H` be its Hecke polynomial at a split place `w` of norm `q` away from
the places of `V` and their conjugates. Then minus the coefficient of `X ^ (n - 1)` in `H` is
`q ^ t ν / ν' * b w 1 + (∑_{i < t} q ^ i) ν`. Here `t = n - r`, `ν = V.charW.frobValue r w` and
`ν' = V.charV.frobValue n w`: for a character `χ` of `U(1)` and rank `N`, `χ.frobValue` is the value
at a uniformizer at `w` of the Hecke character `x ↦ χ(x / x̄) υ(x) ^ (-N)`, times `q ^ (N / 2)`. 

### `eventually_trace_frob_eq_of_hasLiftHeckePolynomial`

 The identity of traces at Frobenius elements. Let `O` be a descent pair over `D.E` of ranks
`r < n` with character `μ = O.u1Char`, let `c` be admissible labels for it and the trivial twist
(`IsLiftSetting`), and let `r - (n - r) = 2 a`. Let the descent pair `V` have character `μ ϑ`, with
`ϑ` tame, and let the eigenform `y` on `V` with Hecke polynomials `H` lift the system `b` of Hecke
eigenvalues. Then for most Frobenius elements `g = x.frob` at places `w = x.place`, minus the
coefficient of `X ^ (n - 1)` in `H w`, times `normalizingAvatar V g`, equals `θ₀(g) θ(g) b w 1`
plus the sum of the first `n - r` powers of the inverse cyclotomic character at `g`. An avatar is
the `ℓ`-adic Galois character of an algebraic Hecke character; `θ₀` and `θ` are those of
`ϑ.hasWeight.inv.toAlgebraic 0 0`, that is `ϑ⁻¹(x / x̄)`, and of `O.hasWeight.inv.toAlgebraic 0 a`,
that is `μ⁻¹(x / x̄) |x| ^ a`; `normalizingAvatar V` is the one made in the same way from the
inverse of the character `V.charW` of the space of rank `r`, with weight `-r`. Complex numbers are
carried to `ℓ`-adic ones by the isomorphism `ι.ιℓ`. 

### `exists_isMainSummand_of_isRepOfType`

 Let `O` be a descent pair of ranks `r < n`, with weight `w` and `t = n - r`. Assume that the
labels `c` are admissible for `O` and the trivial twist (`IsLiftSetting`), and that `R` is a
representation with these labels, jumps `J` and empty level (`IsRepOfType`) whose trace at each `g`
is the limit of the Hecke eigenvalues `b v 1` along most Frobenius elements tending to `g`, at
places `v`, carried to `ℓ`-adic numbers by the isomorphism `ι.ιℓ : ℂ ≃+* ℚ̄_ℓ`. Assume also that the
jumps `J σ`, lowered by `(r - t) / 2 - cmSign σ * w v` with `v` the infinite place of `σ` and
`cmSign σ` equal to `1` on the CM type and `-1` off it, obey the numerical conditions
`IsMainSummandWeights`. Then there is a `T` with `IsMainSummand O b T`: a main summand that gives
the traces of the representations attached to the lifts of `b` for all tame twists of `O`. 

### `map_jumps_sub_eq_map_targetParameter`

 Let the weight `(d, κ)` give at each infinite place `v` of the CM field `D.E` (the type `D.Φ`) a
shape `d v` and an integer `κ v`, and suppose that its doubled Harish-Chandra parameter is
`D.paramW`, twice the target parameter `λ_q = D.targetParameter v q` in rank `r = D.r`. Put
`t = D.t`, and at a complex embedding `σ` over `v` let `ε = cmSign σ` be `1` on the CM type and
`-1` off it. Then the jumps (Hodge–Tate weights) of `(d, κ)` at `σ`, lowered by
`(r - t) / 2 + ε w` for any integer `w`, are the numbers `t / 2 - ε (λ_q + w)` for `q < r`. 

### `_root_.New.Data.isEigenform_of_hasHeckePolyAt`

 A nonzero function with Hecke polynomial `Q w` at every split place `w` off the chosen places
and their conjugates is an eigenform for the system `Q`. 

### `exists_isMainSummand_descentPair`

 Let the Hecke eigenvalues `p (w, i)` occur in a nonzero good form on `D.spaceW D.m`: a form of
principal level at the chosen places, in the image of the idempotent `D.e₀`. Let `O` be the `j`-th
descent pair of the trivial twist, `1 ≤ j ≤ m = D.m`: its two spaces have dimensions `r = D.r` and
`r + t`, `t = D.t`, and its character has weight `-D.liftWeight j`. Then some `r`-dimensional
`ℓ`-adic Galois representation `T` of `D.E` has `IsMainSummand O` for `p`. 
