---
{
  "module": "src/New/Determinant/Exchange/VanishingDescends.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/VanishingDescends.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/VanishingDescends.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vanishing of theta integrals descends along hyperbolic planes

If the theta integral of `(W ⊕ H, V ⊕ H)` vanishes on all Schwartz vectors and standard data, so
does that of `(W, V)`, provided `W` has even rank and `rk V - rk W / 2 ≥ -k` for a natural number
`k ≤ min μ`. The constant term along the new isotropic line is a value of Tate's integral, and for
the vectors of `exists_thetaLarge_cone_eq_mul` this integral is, by analytic continuation, the theta
integral of `(W, V)` times factors that do not vanish at the value in question.

Notions from other files:
* `thetaLarge W V 𝔠 v Φ`: the theta integral over `[U(V)]` of `v ⊗ Φ`, a function on `G E s`;
* `stdRowDatum σ χ y`: the finite datum `x ↦ χ⁻¹ (det (y; x))`, supported where the square matrix
  `(y; x)`, with rows ordered by `σ`, is invertible and integral;
* `SplitTameChar E μ`: a tame character of weight `μ`, ramified at a finite set of split places;
* `negCount s`: the number of signs `-1` among `s`.

## Relation to the literature

See `New.Determinant.Exchange.TheoremForPartners` for related work.


### `ThetaLargeVanishes`

 Let `W` and `V` be hermitian spaces over `E` with bases indexed by `n` and `r` and with signs
`s` and `t` at the infinite places. The theta integral of `(W, V)` for the split tame character `𝔠`,
a function on the adelic unitary group `G E s` of `W`, vanishes on all Schwartz vectors `v` (all
Fock moments finite) of the Fock space `PairFock E s t` of `Hom(W, V)` and all standard data
`stdRowDatum σ 𝔠.semilocalChar y`. Here `y` is any integral `b × n` matrix over the product of the
completions at the ramified places `𝔠.ramifiedPlaces`, and `σ` orders the rows of `y` and of an
`r × n` matrix into a square matrix. 

### `ThetaLargeVanishes.congr_spaces`

 Let `W`, `W₁` be hermitian spaces with the same signs `s`, and `V`, `V₁` with the same signs
`t`. If, for the split tame character `𝔠`, the theta integral of `(W, V)` at every point of the
unitary group of `W` vanishes on all Schwartz vectors and all standard data, so does that of
`(W₁, V₁)`. 

### `negCount_sumElim_hyperbolicSigns_unit`

 Adding a hyperbolic plane, with signs `hyperbolicSigns Unit` (one `+1` and one `-1`), to signs
`ε` adds one negative sign. 

### `ThetaLargeVanishes.of_add_plane`

 Descent along one hyperbolic plane `H`. Let `A` and `X` be adapted splittings (orthonormal at
the infinite and integral at the finite places) `W' = W ⊕ H` and `V' = V ⊕ H` of hermitian spaces.
Let `W` be of even rank and `-k ≤ rk V - rk W / 2`, with `k ≤ μ w` at every infinite place `w`,
where `μ` is the weight of the split tame character `𝔠`.

If at every point of the unitary group of `W'` the theta integral of `(W', V')` vanishes on all
Schwartz vectors (finite weighted norms) and all data `stdRowDatum σ' 𝔠.semilocalChar y'`, then at
every point `g` of the unitary group of `W` that of `(W, V)` vanishes on all Schwartz vectors and
all data `stdRowDatum σ 𝔠.semilocalChar y`. Here `y'` and `y` are arbitrary integral matrices at
the ramified places of `𝔠`, with rows indexed by `b` and columns by the bases of `W'` and `W`; the
orderings `σ` and `σ'` of these rows and those indexed by the basis of `V`, respectively `V'`, into
a square matrix are arbitrary. 

### `ThetaLargeVanishes.of_add_planes`

 Descent along any positive number `j` of hyperbolic planes `H`. Let the hermitian space `W'`
have the rank and number of negative signs of `W ⊕ H ^ j`, and let `V'` have the number of negative
signs of `V ⊕ H ^ j`; its rank is then that of `V ⊕ H ^ j` too, by `σ` and `σ'`. Let `W` be of even
rank and `-k ≤ rk V - rk W / 2`, where `k ≤ μ w` at every infinite place `w` and `μ` is the weight
of the split tame character `𝔠`.

If at every point of the unitary group of `W'` the theta integral of `(W', V')` vanishes on all
Schwartz vectors and all data `stdRowDatum σ' 𝔠.semilocalChar y'`, then at every point of the
unitary group of `W` that of `(W, V)` vanishes on all Schwartz vectors and all data
`stdRowDatum σ 𝔠.semilocalChar y`. Integrality at the ramified places of `𝔠` is the only condition
on the matrices `y'` and `y`; their rows are indexed by `b`, and `σ`, `σ'` order these rows and
those indexed by the basis of `V`, respectively `V'`, into a square matrix. 
