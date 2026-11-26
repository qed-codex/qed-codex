---
{
  "module": "src/New/UpperBound/Seesaw/LevelIdeles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/LevelIdeles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/LevelIdeles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Valuations of the chosen ideles, and lattices and levels at the chosen places

Facts at the finite places about the chosen data `D : New.Data P` and a tame character `ϑ`. The
notions used:
* `New.Data.piM` is the integer `π̄₀ π̄₁` of `E`, whose product with its conjugate is `M = p₀ p₁`
  (`New.Data.M`). The chosen places are the prime divisors of `π̄₀ π̄₁`.
* `New.Data.chosenIdele` is a finite idele that generates the ideal `(π̄₀ π̄₁)` and is `1` away from
  the chosen places.
* `New.Data.ideleA` is the idele `a = α / star chosenIdele`, with `α` the idele of the Weil data.
* `New.Data.gradingY k` presents the hermitian space `Y_k = New.Data.spaceY k` as an orthonormal
  part plus a string of `2 ϱ + 1 - k` vectors.
* `New.levelOf w H` is the group of integral elements of the finite adelic unitary group whose
  reductions at the places `w i` form an element of `H`.

## Main definitions and results

* `New.Data.v_chosenIdele`: `New.Data.chosenIdele` has the valuations of `π̄₀ π̄₁` at every finite
  place.
* `New.Data.v_gradingY_genericConst_eq_ideleA_mul_star`: the constant of the grading
  `New.Data.gradingY` has the valuations of `a ā`.
* `New.Data.spansLattice_gradingY`: the graded space `Y_k` carries the lattice with basis
  `New.gradedLatticeBasis`.
* `New.Data.chosenLevel_inf_trivialOn_le`: elements of principal level `π̄₀ π̄₁` that are `1` at the
  places `ϑ.Q` lie in the trivial level at the places `New.Data.levelPlaces`.

## Relation to the literature

These are auxiliary facts about the data `New.Data`; no external source is cited.


### `absNorm_piM`

 The ideal of `E` spanned by `D.piM`, an integer of `K` of norm `p₀ p₁` viewed in `E`, has norm
`M ^ f`, where `M = D.M = p₀ p₁` and `f = D.f` is the number of infinite places of `E`. 

### `v_chosenIdele`

 At each finite place `w` of `E`, the finite idele `D.chosenIdele` has the same valuation `v` as
`D.piM`, an integer of `K` of norm `p₀ p₁` viewed in `E`, whose ideal the idele generates. 

### `v_alpha_mul_star_eq_ideleA_norm_mul_M`

 Let `D` be admissible data, with field `E = D.E` and level `M = D.M = p₀ p₁`, a natural number.
At each finite place `w` of `E`, with `v` the valuation of the completion of `E` at `w`, the norm
`α ᾱ` of the finite idele `α = WeilData.α` in the Weil data of `E` has the valuation of `a ā M`.
Here `a = D.ideleA = α / star D.chosenIdele`, and `D.chosenIdele` generates an ideal whose product
with its conjugate is `(M)`. 

### `v_gradingY_genericConst_eq_ideleA_mul_star`

 Let `D` be admissible data, with field `E = P.E D.towerExp`, level `M = D.M = p₀ p₁` and
`D.m = 2 ϱ + 2` lifts (`ϱ = D.ϱ`), and let `k ≤ 2 ϱ + 1`, that is `k < D.m`. The grading
`D.gradingY k` presents the hermitian space `Y_k = D.spaceY k` over `E` as an orthonormal part plus
a string of `2 ϱ + 1 - k` vectors with antidiagonal Gram matrix, and carries the constant
`genericConst = -(j M δ_E)⁻¹` of `E`. At each finite place `w` of `E`, with `v` the valuation of
the completion at `w`, this constant has the valuation of `a ā`.
Here `j` and `α` are the purely imaginary element and the finite idele of the Weil data of `E`,
`δ_E = P.deltaE D.towerExp` generates the different of `E`, and
`a = D.ideleA = α / star D.chosenIdele`. 

### `spansLattice_gradingY`

 Let `k ≤ 2 ϱ + 1`, where `ϱ = D.ϱ`. The grading `D.gradingY k` presents the hermitian space
`Y_k = D.spaceY k` over `E` as an orthonormal part, with last vector `y`, plus a string of
`s = 2 ϱ + 1 - k` vectors. Let `a = D.ideleA`, let `π = D.piNIdele` be the principal idele of the
integer `D.piN` of `E` with `π π̄ = D.N`, and let `u = D.latticeScale k = (a / ā) ^ ⌈(2 ϱ + 2 -
k) / 2⌉`. Then the finite adelic basis `xFin` of `Y_k` spans the same lattice over `Ô` as the
following basis `New.gradedLatticeBasis`. For odd `s`, multiply the string vectors by `u` and
replace `y` by `y / π̄ + u z / (π π̄)`, with `z` the middle vector of the string. For even `s`,
multiply the first half of the string by `u / a` and the second half by `u ā`. All other vectors are
unchanged. 

### `chosenLevel_inf_trivialOn_le`

 Let `ϑ` be a tame character: an automorphic character of `U(1)` of weight `0` whose tame part, a
family of characters of the residue fields, is trivial outside the finite set of places `ϑ.Q`. Let
`g` in the finite adelic unitary group indexed by `n` be integral with reduction `1` at the chosen
places (`D.chosenLevel`) and have component `1` at the places of `ϑ.Q` (`trivialOn`). Then `g` is
integral with reduction `1` at all places of `D.levelPlaces ϑ`, which are the chosen places and
those of `ϑ.Q`: it lies in `levelOf` at these places for the trivial group `⊥` of reductions. 
