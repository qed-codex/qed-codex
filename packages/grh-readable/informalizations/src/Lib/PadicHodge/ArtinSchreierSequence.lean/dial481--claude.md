---
{
  "module": "src/Lib/PadicHodge/ArtinSchreierSequence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/ArtinSchreierSequence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/ArtinSchreierSequence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# W(𝔪^♭), the diagonal tensor module W(C^♭) ⊗ T and the Artin–Schreier sequence

`New.Period.OFlat = O^♭` is the tilt of the ring of integers of `ℂ_p`, and `New.Period.CFlat = C^♭`
is its fraction field. We write `New.Period.WittCFlat = W(C^♭)` and `A_inf = W(O^♭)`; the prime is
fixed by `[ThePrime p]`, and `New.Gp p` is the Galois group of `ℚ̄_p` over `ℚ_p`. The ideal
`W(𝔪) = W(𝔪^♭)` of `A_inf` is introduced, and the sets `W(𝔪) + p ^ m W(C^♭)` serve as neighbourhoods
of `0` for which the Galois action on `W(C^♭)` is continuous. For a group Γ (`[GroupOverGp p]`,
elements of type `GroupOverGp.G`) that maps to `Gp p`, and a representation of Γ on a ℤ_p-module T,
the module W(C^♭) ⊗ T with the diagonal action of ℤ × Γ is built, together with base change of
linear and bilinear maps. For T = ℤ_p/p^m(1) this gives an Artin–Schreier sequence: φ − 1 is onto,
and its kernel modulo W(𝔪^♭)·(1 ⊗ 1) is ℤ_p/p^m.

## Main definitions and results

* `New.Lift.wittOfMaxIdeal`: the kernel of the reduction `A_inf → W(k)`; by
  `New.Lift.mem_wittOfMaxIdeal` its elements are the Witt vectors none of whose coefficients is a
  unit.
* `New.Lift.WittCFlat.eventually_smul_sub_mem`: for `a`, `d` in `W(C^♭)` and `g` near `1` in
  `New.Gp p`, the element `(g • a - a) * d` lies in `W(𝔪) + p ^ m W(C^♭)`.
* `New.Lift.DiagTensor`: the module W(C^♭) ⊗ T with its diagonal action.
* `New.Lift.smallPart`: the A_inf-submodule W(𝔪^♭)·(1 ⊗ 1) of M = W(C^♭) ⊗ ℤ_p/p^m(1).
* `New.Lift.TateTwist.exists_eq_phi_smul_sub`,
  `New.Lift.TateTwist.exists_sub_mk_one_mem_smallPart_of_phi_smul_sub_mem` and
  `New.Lift.TateTwist.eq_zero_of_mk_one_mem_smallPart`: φ − 1 is onto M, and its kernel modulo
  W(𝔪^♭)·(1 ⊗ 1) is ℤ_p/p^m.
* `New.Lift.TateTwist.eventually_map_smul_sub_mem_smallPart`: let ρ be a representation with
  ρ(g)y − y divisible by p^m for g near 1, and let L be a linear map from W(C^♭) ⊗ ρ into M. Then
  for each v, L(gv − v) lies in W(𝔪^♭)·(1 ⊗ 1) for g near 1.

Notions from other files:
* `New.Period.toWittResidue`: the ring map `A_inf = W(O^♭) → W(k)`, `k` the residue field of `O^♭`,
  that reduces each Witt coordinate.
* `New.Lift.FrobGroup Γ`: the group `ℤ × Γ`; `FrobGroup.snd` is the projection to `Γ`, `inr g` is
  `(0, g)` and `φ` is `(1, 1)`, which acts as the Frobenius.
* `New.Period.nearOne Γ`: the filter "near `1`" on `Γ`, pulled back from the neighbourhoods of `1`
  in `Gp p`.

## Relation to the literature

Known result: The Artin–Schreier–Witt resolution over the tilt. Only the φ−1 step of Herr's complex
is treated, on Witt vectors of the tilt of C_p modulo p^m, and the Γ-step is not treated. Source: L.
Herr, Sur la cohomologie galoisienne des corps p-adiques, Bull. SMF 126 (1998) 563–600.


 ## The ideal W(𝔪^♭) and continuity of the Galois action on W(C^♭) 

### `wittOfMaxIdeal`

 The ideal W(𝔪^♭) of A_inf: the kernel of the map from A_inf to the Witt vectors of the
residue field of O^♭. 

### `mem_wittOfMaxIdeal`

 An element of `A_inf` lies in `W(𝔪^♭)` exactly when none of its Witt coordinates is a unit. 

### `teichmuller_mem_wittOfMaxIdeal`

 The Teichmüller lift `[x]` of a non-unit `x` of `O^♭` lies in `W(𝔪^♭)`: its zeroth coordinate is
`x` and the others are `0`. 

### `smul_oFlat_eq_tiltMap`

 An element `σ` of `Gp p` acts on `O^♭` as the map of tilts induced by its action on `O_C`. 

### `coeff_oFlat_mul`

 The `n`-th coordinate of `O^♭ = PreTilt OC p` is multiplicative (stated for `O^♭`, which is the
perfection of `O_C / p` only by definition). 

### `coeff_oFlat_sub`

 The `n`-th coordinate of `O^♭` is additive on differences. 

### `eventually_coeff_smul_eq`

 For `h` near `g`, the elements `h • x` and `g • x` of the tilt have the same `n`-th coordinate
modulo `p`: it comes from the translate of `x.untiltRoot n`, whose orbit map is continuous. 

### `continuous_smul_cFlat`

 For the valuation topology on `C^♭`, the orbit map `g ↦ g • y` of each `y` is continuous. 

### `WittCFlat.eventually_smul_sub_mem`

 Continuity of the Galois action on `W(C^♭)`: for `a`, `d` in `W(C^♭)` and `m ≥ 0`, for all `g`
near `1` in `Gp p` the element `(g • a - a) * d` lies in `W(𝔪^♭) + p ^ m W(C^♭)`. 


## The module W(C^♭) ⊗ T with its diagonal action

Let ρ be a representation of Γ on a ℤ_p-module T. `New.Lift.DiagTensor` ρ is W(C^♭) ⊗ T over ℤ_p,
with the action of ℤ × Γ (`New.Lift.FrobGroup`) given by m(a ⊗ t) = ma ⊗ ρ(m₂)t, where m₂ is the
image of m in Γ.


### `New.Lift.DiagTensor`

 The tensor product `W(C^♭) ⊗ T` over `ℤ_p`, for a representation `T` of `Γ`. 

### `map`

 For a `ℤ_p`-linear map `f : T → T'`, the `W(C^♭)`-linear map `1 ⊗ f` from `W(C^♭) ⊗ T` to
`W(C^♭) ⊗ T'`. 

### `pair`

 For a `ℤ_p`-bilinear map `b : T × T' → T''`, its `W(C^♭)`-bilinear extension
`(W(C^♭) ⊗ T) × (W(C^♭) ⊗ T') → W(C^♭) ⊗ T''`. 

### `mk`

 The map `(a, t) ↦ a ⊗ t` into `W(C^♭) ⊗ T`, linear over `W(C^♭)` in `a` and over `ℤ_p` in
`t`. 

### `induction`

 A property of the elements of `W(C^♭) ⊗ T` that holds for the pure tensors `a ⊗ t` and is
stable under addition holds for all elements. 

### `_root_.New.Lift.diagTensor_induction`

 `DiagTensor.induction` with the element last. Stability under addition has a default proof,
meant for the case where `P x` says that additive maps agree at `x`. 


## The Artin–Schreier sequence with coefficients ℤ/p^m(1)

Let M be W(C^♭) ⊗ ℤ_p/p^m(1): the module `New.Lift.DiagTensor` of the representation of Γ on ℤ_p/p^m
through the cyclotomic character `New.Period.χ`. In Lean this is
`Rep.of (charRep (QuotSpan (p ^ m)) χ)`, where `QuotSpan` is ℤ_p modulo the span of p^m and
`charRep` makes Γ act through χ.


### `smallPart`

 The `A_inf`-submodule `W(𝔪^♭) • (1 ⊗ 1)` of `W(C^♭) ⊗ ℤ_p/p^m(1)`: the image of the ideal
`New.Lift.wittOfMaxIdeal` under `a ↦ a • (1 ⊗ 1)`. 

### `smul_mem_smallPart`

 The submodule `New.Lift.smallPart m` is stable under Γ. 

### `exists_const_of_frobenius_sub`

 If `φ x - x` lies in `W(𝔪)` modulo `p ^ m`, then `x` is a constant of `ℤ_[p]` modulo `W(𝔪)` and
`p ^ m`. 

### `pow_dvd_of_pow_dvd_algebraMap_sub`

 A constant of `ℤ_[p]` that lies in `W(𝔪)` modulo `p ^ m` is divisible by `p ^ m`. 

### `TateTwist.pow_smul_eq_zero`

 `p ^ m` kills `W(C^♭) ⊗ ℤ_p/p^m(1)`. 

### `TateTwist.oneTmul`

 The map `x ↦ x ⊗ 1` from `W(C^♭)` onto `W(C^♭) ⊗ ℤ_p/p^m(1)`. 

### `TateTwist.phi_smul_oneTmul`

 The Frobenius `φ` acts on `x ⊗ 1` through its first factor. 

### `TateTwist.mk_one_mk_eq_oneTmul`

 A constant `1 ⊗ c`, for `c` in `ℤ_p`, is `c ⊗ 1`. 

### `TateTwist.oneTmul_mem_smallPart_iff`

 `x ⊗ 1` lies in `W(𝔪^♭) • (1 ⊗ 1)` exactly when `x` is congruent modulo `p ^ m` to an element
of `W(𝔪^♭)`. 

### `TateTwist.exists_eq_phi_smul_sub`

 `φ - 1` is onto `W(C^♭) ⊗ ℤ_p/p^m(1)`, as it is onto `W(C^♭)`. 

### `TateTwist.exists_sub_mk_one_mem_smallPart_of_phi_smul_sub_mem`

 If `φ d - d` lies in `W(𝔪^♭) • (1 ⊗ 1)` (`New.Lift.smallPart`), then `d` is a constant `1 ⊗ k`
modulo that submodule. 

### `TateTwist.eq_zero_of_mk_one_mem_smallPart`

 A constant `1 ⊗ k` of `W(C^♭) ⊗ ℤ_p/p^m(1)` lies in `W(𝔪^♭) • (1 ⊗ 1)` (`New.Lift.smallPart`)
only for `k = 0`. 

### `TateTwist.eventually_map_smul_sub_mem_smallPart`

 Let `ρ` be a representation of `Γ` with `g y - y` divisible by `p ^ m` for `g` near `1`, for
each `y`, and `L` a `W(C^♭)`-linear map from `W(C^♭) ⊗ ρ` to `W(C^♭) ⊗ ℤ_p/p^m(1)`. Then for each
`v`, `L (g v - v)` lies in `W(𝔪^♭) • (1 ⊗ 1)` (`New.Lift.smallPart`) for `g` near `1`. 

### `TateTwist.smallPart_spec`

 Five facts about `M = W(C^♭) ⊗ ℤ_p/p^m(1)` and `S = W(𝔪^♭) • (1 ⊗ 1)` (`New.Lift.smallPart`) in
one statement; the elements `1 ⊗ k`, with `k` in ℤ_p/p^m(1) (in (c) and in (d)), are the constants.
They are (a) `TateTwist.pow_smul_eq_zero`, (b) `TateTwist.exists_eq_phi_smul_sub`, (c)
`TateTwist.exists_sub_mk_one_mem_smallPart_of_phi_smul_sub_mem`, (d)
`TateTwist.eq_zero_of_mk_one_mem_smallPart` and (e)
`TateTwist.eventually_map_smul_sub_mem_smallPart`. 
