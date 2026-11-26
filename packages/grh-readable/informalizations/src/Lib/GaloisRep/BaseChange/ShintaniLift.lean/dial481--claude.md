---
{
  "module": "src/Lib/GaloisRep/BaseChange/ShintaniLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/ShintaniLift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/ShintaniLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Base change at an inert place carries a label to its Shintani lift

Base change along a step `E'/E` (`New.IsStep E' μ`, which among other things makes `[E' : E]` prime)
at a place `w` of `E` that is split over `E⁺` and inert in `E'`: the local matching comes from
Shintani lifting for `GL n` over the residue fields.

* `New.inflateConj`: the conjugate of a function on `GL n` of the residue field, pulled back along
  reduction to `GL n 𝒪_w` and extended by zero to `GL n` of the completion.
* `New.exists_representation_heckeFun_inflateConj`: on forms of principal level at `w`, its Hecke
  operator is the action of a group algebra element of the finite group.
* `New.isLocalMatching_shintani`: inflated `Ξ` and, for some `φ`, inflated `g ↦ S ⟨g, φ⟩` are
  matching local data, where `S` is a class function on the semidirect product that descends to `Ξ`.
* `New.exists_baseChange_hasLabel`: a form with label `Ξ` at `w` has a weak base change with the
  lift `Ξ'` as label at the place `u` above `w`.

`New.localCongruence n w 0` is the kernel of reduction of `GL n 𝒪_w`; `New.HasLabel f hw χ` says
that this kernel fixes `f` and that `∑ conj (χ x) x` does not kill `f`.

Notions from other files:
* `New.Lift`: F lifts to F' over Z if, for every m, one Z-combination of characters of GL_m(k') ⋊
  Gal(k'/k) descends to both F (over k) and F' (over k').
* `New.IsLocalMatching`: Retracts G, G' of the adelic groups above a finite set of places,
  compatible levels, and bi-invariant functions that form matching pairs at a level where σ-cocycles
  split.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.


### `inflateConj`

 The inflation of `χ`, conjugated: the function on `GL n (LocField w)` that sends `g` in
`GL n 𝒪_w` (`intGL n Valued.v.integer`) to `conj (χ (reduceGL g))`, the complex conjugate of `χ`
at the reduction of `g` modulo `w`, and is `0` outside `GL n 𝒪_w`. 

### `exists_representation_heckeFun_inflateConj`

 Let `K` be the forms of weight `κ` in `stdSpace E n` that are fixed by the kernel of reduction
at the split place `w`. On `K ⊓ W`, for each subrepresentation `W`, the finite group
`GL n (ResField w)` acts by some `ρ` such that the following holds for every `χ` and `v`, with `x`
the action of `∑ conj (χ g) g` on `v`. (a) The Hecke operator of `inflateConj χ` (which is
`conj (χ (g mod w))` on `GL n 𝒪_w` and `0` elsewhere) sends `v` to `x`. (b) `v` has label `χ`
(`New.HasLabel`: `v` is fixed by the reduction kernel and `∑ conj (χ g)` times the translates of `v`
by lifts of `g` is nonzero) exactly when `x ≠ 0`. 

### `reduceGL_map_locMap`

 Reduction commutes with the map of completions induced by `ι`, if `ψ` is the map of residue
fields that `ι` induces on global integers. 

### `galActionGL_apply`

 The Galois action on `GL n` of the residue field applies the automorphism to the entries. 

### `exists_mk_reduceGL_pow_eq_mk_reduceGL_twistedNorm`

 Let `σ` in `Gal(E'/E)` fix the finite place `u` of `E'` and induce `φ` on the residue field of
`u`, where `φ` is an automorphism over the residue field of the place `w` of `E`. Let `a` be an
element of the finite adelic unitary group over `E'` whose component at `u` lies in `GL n 𝒪_u`.
Then the twisted norm `N = a · σ(a) ⋯ σ^{m-1}(a)` also has its component at `u` in `GL n 𝒪_u`, and
in `GL n (ResField u) ⋊ Gal(ResField u/ResField w)` the `m`-th power of (reduction of `a`, `φ`) is
(reduction of `N`, `φ ^ m`). 

### `exists_ne_one_and_frobeniusAlgEquivOfAlgebraic_apply_eq`

 Let `u` be the only place of `E'` above `w`, and let `φ`, the Frobenius of the residue
extension at `u`, be nontrivial. Then some `σ ≠ 1` in `Gal(E'/E)` fixes `u`, lies outside the
inertia group of `u`, and induces `φ` on the residue field of `u`. 

### `isLocalMatching_shintani`

 Let `E'/E` be a step with `μ` (`New.IsStep`) and let `w` be split with `μ` trivial on its
ideles. Let `u` be the only place above `w`, split, with residue field of degree `[E' : E]` over
that of `w`, and let `Ξ` be a function on similarity classes of matrices over `ResField w`
(`New.Hall`). If `S` on `GalSemidirect (ResField w) (ResField u) n` is a class function that
descends to `Ξ` (so `S ⟨a, φ⟩ = Ξ.evalGL b` when `φ ≠ 1` and `⟨a, φ⟩ ^ orderOf φ` is `inl` of `b`
mapped to `ResField u`), then for some `φ` in the residue Galois group the inflations of the complex
conjugates of `Ξ` and of `S ⟨·, φ⟩` are matching local data (`New.IsLocalMatching`) above `{w}`.
Here `GL n` at `w` and at `u` is embedded by `New.ofSplitPlace`, at level `≡ 1` mod the maximal
ideal. 

### `exists_baseChange_hasLabel`

 Let `E'` contain a primitive 5040th root of unity, `w` be split with `μ` trivial on its ideles,
and `u` the only place above `w`, split, of residue degree `[E' : E]`. If the form `f` has the
character `Ξ` as label at `w` and `Ξ'` is a lift of `Ξ` (`New.Lift ℕ`), then some eigenform `f'`
(nonzero, with polynomials `P` at the places of `E'`) over `E'` of weight `κ.baseChange` is a weak
base change of `f` off `w` and `w̄`, with label `Ξ'` at `u`. 
