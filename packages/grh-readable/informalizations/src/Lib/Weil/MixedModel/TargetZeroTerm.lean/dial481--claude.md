---
{
  "module": "src/Lib/Weil/MixedModel/TargetZeroTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/TargetZeroTerm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/TargetZeroTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Zero terms of the mixed models of the Weil representation at the real places

The hermitian space `W'` splits as an isotropic line, `W` and a dual line (the splitting
`A : W'.Splitting W Unit`), and `V'` splits as an isotropic line `B`, `V` and a dual line (the
splitting `X : V'.Splitting V Unit`). This file studies the zero term along `Hom(W, B)` of slices of
vectors in the mixed models of the Weil representation at the real places.

## Main definitions and results

* `New.Exchange.realTargetZeroTerm W X`: the zero term along `Hom(W, B)` at the real places.
* `New.Exchange.lineTermReal_true_eq_realTargetZeroTerm`: the real part of the line term is this
  zero term of a slice.
* `New.Exchange.exists_realTargetZeroTerm_eq`: every Schwartz vector is such a zero term.
* `New.Exchange.realSlice_realPairWeil`, `New.Exchange.exists_realTargetZeroTerm_realPairWeil`: real
  points of the target group act on slices, and those with `lineVector X` as an eigenvector at every
  place act on zero terms when `2 ∣ card n`.

Notions from other files:
* `New.Space.Splitting V' V p`: a decomposition of `V'` into isotropic frames `l`, `k` with `p`
  columns and an isometric copy of `V`; `kAdelic`, `lAdelic`, `iAdelic` are its adelic frames, and
  `IsBaseAdapted` says that together they are orthonormal at the infinite places and integral at the
  finite places.
* `homSource`, `homTarget`: the splittings of `Hom(W', V')` over `Hom(W, V')` and of `Hom(W, V')`
  over `Hom(W, V)` induced by `A` and by `X`; `zeroTerm` is the zero term of a splitting.
* `IsAdapted.mixedModel`: the mixed model at the real places of a splitting adapted to a basis; its
  `slice` at a point, and `realSlice` for the splitting `homSource`, map the Fock space `PairFock`
  of one space of homomorphisms to that of a smaller one.
* `lineTerm`, `lineTermReal`: the operator that translates along the line and takes both zero terms,
  and its real part; `realPairWeil γ γ'` is the real Weil action of a pair with weights.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## The zero term along `Hom(W, B)` at the real places

The real part `lineTermReal A X true a` of the line term is the zero term along `Hom(W, B)` of the
slice along `A` at `a` times the frame of `B` (`lineTermReal_true_eq_realTargetZeroTerm`). Every
Schwartz vector for `(W, V)` is such a zero term (`exists_realTargetZeroTerm_eq`).


### `adaptedTargetBasis`

 The change of basis that makes the frame of `X.homTarget W` orthonormal and integral. 

### `frameAt_homTarget`

 In the basis `adaptedTargetBasis W`, the frame of the splitting `X.homTarget W` of `Hom(W, V')`
has the column blocks `X.lAdelic ⊗ₖ stdForm E s` (`stdForm E s` is the diagonal matrix of the signs
`s`), `X.kAdelic ⊗ₖ 1` and `X.iAdelic ⊗ₖ 1`. 

### `isAdapted_homTarget`

 If the frames of `X` are orthonormal at the infinite places and integral (`IsBaseAdapted`), the
splitting `X.homTarget W` is adapted at `1` to the basis `adaptedTargetBasis W`. 

### `realTargetZeroTerm`

 The zero term along `Hom(W, B)` at the real places, where `B` is the isotropic line of `X`. 

### `homSlice_integrated_of_real`

 Let `x` be an adelic matrix with finite part zero. The term `A.homSlice` at `scaleIdele E • x`
of the datum `integrated v f` (real part `v`, finite part `f`) is the datum with real part the slice
of `v` at `x` and finite part the zero term of the real vacuum projection of `f`. 

### `lineTermReal_true_eq_realTargetZeroTerm`

 Let `A` and `X` be base-adapted splittings of `W'` over `W` and of `V'` over `V` along a single
hyperbolic plane, and let `B` be the isotropic line of `X`. Then in the model `β = true`, where the
line term is the slice along `A` followed by the zero term along `Hom(W, B)`, the real part of the
line term at the real point `a` sends `v` to the following. First take the slice `realSlice A V'` of
`v` along `A` at the real point `a • X.kAdelic`, where `X.kAdelic` is the frame of `B`. Then take
the zero term of this slice along `Hom(W, B)` (`realTargetZeroTerm`). 

### `exists_realTargetZeroTerm_eq`

 Let `X` split `V'` as `V` plus one hyperbolic plane, and let it be base-adapted
(`IsBaseAdapted X`): the adelic matrix with column blocks `lAdelic`, `kAdelic`, `iAdelic` has
orthonormal columns at every infinite place and integral entries at every finite place. Then every
Schwartz vector `v` for `(W, V)` is the zero term at the real places along `Hom(W, B)`
(`realTargetZeroTerm`) of some Schwartz vector `v'` for `(W, V')`. Here a Schwartz vector is an
element of the Fock space of `Hom(W, V)` (resp. `Hom(W, V')`) at the infinite places whose weighted
norms are all finite (`IsSchwartzVector`), and `B` is the isotropic line of `X`. 


## Real points of the target group on slices and zero terms

The slice along `A` of `h v` at `x` is `h` applied to the slice of `v` at `h⁻¹ x`, for real `h`
(`realSlice_realPairWeil`). A real point that preserves the line `B` acts on the zero term along
`Hom(W, B)` through a real point of `U(V)`, a phase and a power of the modulus
(`exists_realTargetZeroTerm_realPairWeil`). Both statements are the real parts of the adelic laws of
the mixed models.


### `realPairWeil_target_eq_smul`

 Changing the weight on the target group multiplies the action by powers of determinants: for a
real point `h` of `U(V)`, `realPairWeil γ 0 (1, h)` is `∏ w, det (h w) ^ (γ w - δ w)` times
`realPairWeil δ 0 (1, h)`. 

### `realSlice_realPairWeil`

 A real point `h` of the target group `U(V')` moves the slice at `x` to the slice at `h⁻¹ x`:
the slice at `x` of `realPairWeil (γ + 1) 0 (1, h) v` is `realPairWeil γ 0 (1, h)` of the slice of
`v` at `h⁻¹ x`. 

### `lineVector`

 The component at the infinite place `w` of the vector that spans the isotropic line of `X`. 

### `exists_real_block_of_actsOnFrame`

 If a real point `g` of `U(V')` acts on the frame of the line `B` by `m`, its block
`X.iCoord * g * X.iAdelic` on `V` (where `X.iCoord * X.iAdelic = 1`) is a real point of `U(V)`. 

### `exists_realTargetZeroTerm_realPairWeil`

 Let `card n` be even, and let the real point `g` of `U(V')` multiply the vector `lineVector X w`
spanning the line `B` at each infinite place `w` by a number `a w ≠ 0`. Then there is a real point
`h` of `U(V)` such that, under the zero term along `Hom(W, B)`, `g` with the weight
`targetWeight n μ` (at `w`: `card n / 2 - μ w`) acts as `h` with the same weight, times the phase
`∏ w, (a w / |a w|) ^ (-2 μ w)` and the power `card n / 2` of the idele norm of `a`. 
