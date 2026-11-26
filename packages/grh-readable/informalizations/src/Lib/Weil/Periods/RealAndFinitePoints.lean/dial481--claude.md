---
{
  "module": "src/Lib/Weil/Periods/RealAndFinitePoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/RealAndFinitePoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/RealAndFinitePoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Real and finite points of the Bessel group

The Bessel group `R(𝔸)` splits as `R(F_∞) × R(𝔸_fin)`, and both factors are unimodular. A function
on `R(𝔸)` that is supported on one coset of a level in the finite variable, and depends there only
on the real variable, has an integral that reduces to `R(F_∞)`.

Notions used in the statements:
* `G E ε = GInf E ε × Gf E ι` is the adelic unitary group `G(𝔸) = G_∞ × G_f`.
* `Y.besselGroup` is the Bessel (Fourier–Jacobi) subgroup `R(𝔸)` of the grading
  `Y : Grading V N X s` of the space `V : Space E ι ε` over the CM field `E` (both defined in
  earlier files); its real points `R(F_∞)` are `Y.besselReal`, and its finite points `R(𝔸_fin)` are
  `Y.besselFin`.
* A level `K` (`IsLevel K`) is an open subgroup of `G_f` inside the standard compact subgroup.


### `New.isMulRightInvariant_of_prod`

 If the product `μ × η` of two nonzero σ-finite measures on groups `A` and `B` is right
invariant, then both factors are right invariant. 

### `mem_besselReal_iff`

 A real point `x` lies in `R(F_∞)` if and only if `(x, 1)` lies in the Bessel group `R(𝔸)`. 

### `mem_besselFin_iff`

 A finite point `t` lies in `R(𝔸_fin)` if and only if `(1, t)` lies in the Bessel group
`R(𝔸)`. 

### `mk_mem_besselGroup`

 A real point `s` and a finite point `t` of the Bessel group `R(𝔸)` give the point `(s, t)` of
`R(𝔸)`. 

### `fst_mem_besselReal`

 The real component `r_∞` of a point `r` of the Bessel group `R(𝔸)` is a real point of the
Bessel group. 

### `besselProdEquiv`

 The decomposition `R(𝔸) = R(F_∞) × R(𝔸_fin)`: the map `(s, t) ↦ (s, t)` from the real points
times the finite points of the Bessel group to the Bessel group, as an isomorphism of
topological groups. 

### `isHaarMeasure_map_besselProdEquiv`

 The image of the product of the Haar measures of `R(F_∞)` and `R(𝔸_fin)` is a Haar measure
on `R(𝔸)`. 

### `isMulRightInvariant_haar_besselReal_besselFin`

 The groups `R(F_∞)` and `R(𝔸_fin)` of real and finite points of the Bessel subgroup `R` are
unimodular: their left Haar measures are right invariant. 

### `exists_integral_eq_mul_integral_besselReal`

 Let `K` be a level and `J = R(𝔸_fin) ∩ K`. There is a constant `c ≠ 0`, the volume of `J`
for compatible Haar measures, with this property. Let `t₀` be a point of `R(𝔸_fin)`, and let `f`
be integrable on `R(𝔸)`, vanish off `R(F_∞) × t₀ J` and equal `a s` at the points `(s, t)` of this
set. Then `a` is integrable on `R(F_∞)` and `∫_{R(𝔸)} f = c ∫_{R(F_∞)} a`. 
