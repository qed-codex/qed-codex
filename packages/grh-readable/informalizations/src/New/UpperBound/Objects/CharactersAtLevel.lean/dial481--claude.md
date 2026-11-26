---
{
  "module": "src/New/UpperBound/Objects/CharactersAtLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/CharactersAtLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/CharactersAtLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Characters of the lifts of the chain above the level N

This file shows that the characters of the lifts of the chain are unramified above the level `N`.
It identifies the character given by `New.rankTwist` and `New.AutChar.spaceChar` with a base
change. It also moves scalings at the primes dividing π, which lie above `N`, through chains of
lifts. A chain whose data at one lift are fixed by such a scaling annihilates the forms `ψ - z ψ`.

## Main definitions and results

* `New.Data.spaceChar_rankTwist`: `New.rankTwist` followed by `New.AutChar.spaceChar` gives the base
  change of the character of a lift.
* `New.Data.tensorChainLift_eq_zero_of_ramified`: for the chosen scaling `z_w` at a prime `w`
  dividing `π` and a tensor `t` of the data of the first `m` lifts, take `j < m` such that
  `ω(1, z_w)` on the factor of the lift from stage `j` to stage `j + 1` fixes `t`. Then the chain
  with the data `t` vanishes on the ramified source forms (`New.Data.ramifiedSourceForms`).

Notions from other files:
* `New.Data.N`: The level: a chosen prime N ≡ 1 mod q₂² with log N ∈ [λ, λ + √(log b)], where
  λ = `New.Data.logLevelTarget`.
* `New.Data.liftKernel`: The theta kernel of the lift from forms on X_j (`New.Data.FormX`) to forms
  on X_{j+1}. The finite unitary groups of X_j and X_{j+1} act on its data by ω.
* `New.chain`, `New.doubleLiftChain`, `New.TensorChain.lift`: The chain of theta lifts with data
  Φ_0, Φ_1, …, the same chain taken in pairs with data in S_{2i} ⊗ S_{2i+1}, and the chain with a
  tensor of data.

## Relation to the literature

See `New.UpperBound.Divisibility.ValuationAtLevel` for related work.


### `charUnramifiedAt_rankTwist_of_N_mem`

 Let `ν_j = D.chainChar ϑ j` be the character of `U(1)(𝔸)` used, for `j ≥ 1`, by the lift from
`X_{j-1}` to `X_j`. At a place `w` of `E` above the level `N`, the twist `rankTwist ν_j n`
(`ν_j` times `upsilonU1 ^ ⌊#n / 2⌋`) has a base change whose finite part is trivial on the local
units at `w`. 

### `spaceChar_rankTwist`

 Let ν = `D.chainChar ϑ i` be the character of U(1)(𝔸) used, for i ≥ 1, by the lift from X_{i-1}
to X_i with the twist ϑ. Applying `New.rankTwist` for X_j and then `New.AutChar.spaceChar` in rank
|X_j| to ν gives the Hecke character x ↦ ν(x/x̄), as |X_j| is even. 

### `liftKernel_omega_scaling`

 The finite adelic unitary groups of the definite spaces `X_j` and `X_{j+1}` act by the twisted
Weil action `ω` on the data of the theta lift `D.liftKernel ϑ j` from forms on `X_j` to forms on
`X_{j+1}`, twisted by the tame character `ϑ`. Let `w` be a prime dividing `π = D.piN`, the integer
of `E` with `π π̄ = N` for the level `N = D.N`, and `z` a scaling at `w`. Then the pair of scalars
`(z, z)` acts trivially. 

### `liftKernel_lift_scaling`

 Each lift of the chain commutes with the scalings at a prime `w` dividing `π`: for a scaling `z`
at `w`, a datum `Φ` of the lift from stage `j` to stage `j + 1` and a form `φ` of stage `j`, the
lift of the translate of `φ` by `z` is the translate by `z` of the lift of `φ`. 

### `liftKernel_lift_sub_scaling`

 The lift from stage `j` to stage `j + 1` takes forms `ψ - z ψ`, for a scaling `z` at a prime
`w` dividing `π`, to forms of the same kind: the lift of `ψ - z ψ` is `χ - z χ` for the lift `χ`
of `ψ`. 

### `liftKernel_lift_sub_scaling_eq_zero`

 Let `z` be a scaling at a prime `w` dividing `π`, and let `Φ` be a datum fixed by `ω(1, z)`.
Then the lift from stage `j` to stage `j + 1` with datum `Φ` sends `ψ - z ψ` to `0` for every form
`ψ` of stage `j`, where `z ψ` is the right translate of `ψ` by `z`. 

### `tensorChainLift_sub_scaling_eq_zero`

 Let `t` be a tensor of data of the first `m` lifts, so that `TensorChain.lift` is the composite
of these lifts, extended linearly in `t`. Let `z` be a scaling at a prime `w` dividing `π = D.piN`,
the integer of `E` with `π π̄ = N` for the level `N = D.N`, and let `j < m`. If `ω(1, z)`, acting on
factor `j` alone, fixes `t`, then the chain with data `t` sends `ψ - z ψ` to `0` for every algebraic
form `ψ` on `X_0`. 

### `tensorChainLift_eq_zero_of_ramified`

 Let `w` be a prime dividing `π = D.piN`, the integer of `E` with `π π̄ = N` for the level
`N = D.N`, let `t` be a tensor of data of the first `m` lifts, and let `j < m`. If `ω(1, z_w)`,
acting on factor `j` alone, fixes `t`, then the chain of lifts with data `t` annihilates the
ramified source forms: the forms on `X_0` of level `D.levelX 0` whose translates by `z_v ^ k`,
`0 ≤ k < N - 1`, have sum `0` for each prime `v` dividing `π`, where `z_v = D.scalingGenerator v` is
the chosen scaling at `v` (integral, `1` off `v` and `v̄`, of order `N - 1` modulo `v`). 

### `doubleLiftChain_eq_zero_of_ramified`

 For each `l`, the finite adelic unitary groups of the definite spaces `X_l` and `X_{l+1}` act
by the twisted Weil action `ω` on the data (Schwartz functions in `(D.homX l).finitePart`) of the
theta lift `D.liftKernel ϑ l` from forms on `X_l` to forms on `X_{l+1}`, twisted by the tame
character `ϑ`.
Let `τ i` lie in the tensor product of the data for `l = 2 i` and `l = 2 i + 1`, so that it gives a
map from forms on `X_{2i}` to forms on `X_{2i+2}`; `doubleLiftChain` is the composite of the first
`p` of these maps. Let `w` be a prime dividing `π = D.piN`, the integer of `E` with `π π̄ = N` for
the level `N = D.N`. If for some `i < p` the operator `ω(1, z_w)` on the second tensor factor fixes
`τ i`, then the composite annihilates the ramified source forms: the forms on `X_0` of level
`D.levelX 0` whose translates by `z_v ^ k`, `0 ≤ k < N - 1`, have sum `0` for each prime `v`
dividing `π`, where `z_v = D.scalingGenerator v` is the chosen scaling at `v` (integral, `1` off
`v` and `v̄`, of order `N - 1` modulo `v`). 
