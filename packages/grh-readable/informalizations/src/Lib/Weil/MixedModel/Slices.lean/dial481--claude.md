---
{
  "module": "src/Lib/Weil/MixedModel/Slices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/Slices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/Slices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Real, named and finite slices of data in the mixed model of an adapted splitting

For a splitting `D` of `V` over `V₀` adapted at the point 1 in a basis `t` (`D.IsAdapted 1 t`), the
adelic mixed model separates into a real part and a finite part. Vectors named by a function `Φ` of
their components at finitely many finite places have slices that are scalar multiples of named
vectors when `Φ` factors in an adapted frame. For `Φ` standard in an integral frame, orthogonality
of characters then gives the source term explicitly.

## Main definitions and results

* `New.Space.Splitting.IsAdapted.mixedModel`: the mixed Schrödinger–Fock model v ↦ v[a]
  (`New.Fock.MixedModel`) at the infinite places that D induces.
* `New.Exchange.zeroTerm_integrated`: the zero term of v ⊗ f is v[0] ⊗ (zero term of f°).
* `New.Exchange.slice_integrated`: the slice at `(t⁻¹)ᴴ x` of v ⊗ f is the real slice of v at
  the real part of x tensored with the slice of f° at the finite part.
* `New.Exchange.ReadsAt.lift`: a chosen continuous additive section of the map `π` that reads the
  components at `S`.
* `New.Exchange.slice_localDatum`: if `Φ` factors in an adapted frame, a slice is a scalar times
  a named vector.
* `New.Exchange.adaptedFrame`: a base-adapted splitting gives, through `π`, an integral frame over
  `F` in three blocks.
* `New.Exchange.ReadsAt.homSlice_localDatum`: the source term of `v ⊗ Φ` for `Φ` that is standard
  in that frame at the matrices whose first block is `π` of the finite part of the given point.

Notions from other files:
* `New.Space.Splitting`: A decomposition V = (lE^p ⊕ kE^p) ⊥ ιV₀ over E: isotropic frames l, k with
  l*Jk = 1 for the hermitian form J of V, an isometry ι from V₀ orthogonal to both, and
  rk V = rk V₀ + 2p.
* `New.Space.Splitting.IsAdapted`: `D.IsAdapted g t` says that the matrix g⁻¹(l tᴴ⁻¹, k t, ι) of
  adelic frames has orthonormal columns at the infinite places and integral finite part.
* `New.𝔸`: The product of one copy of ℂ for each infinite place of E with the finite adeles 𝔸_f:
  the adele ring of E when E is totally complex.
* `New.Space.Splitting.slice`: the slice `f ↦ f[x]` at `x ∈ 𝔸^p`, a bounded map from 𝒮(V) to
  𝒮(V₀).
* `New.Exchange.IsBaseAdapted`: The adelic frame (l, k, ι) of the splitting has orthonormal columns
  at every infinite place and integral entries at every finite place.
* `New.Exchange.IntegralFrame`: An integral invertible matrix cut into column blocks (K I L), with
  its integral inverse cut into row blocks K′, I′, L′. `adaptedFrame h D` is the frame (k, ι, l) of
  an adapted splitting read through π.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## The real mixed model of an adapted splitting

Conventions: `New.Space.integrated V v f` = v ⊗ f is the integral of v(y) ϱ(y) f over the real
vectors y, so it puts the Fock vector v in place of the real vacuum. f° = `New.Space.projReal V f`
is the real vacuum projection.


### `vacuumFactor`

 For a splitting adapted at `1`, the nonzero constant `c` such that the mixed term `D.slice x` at
`x` of the vacuum of `V` is `c * ‖vacuumFn (tᴴ x)‖ ^ 2` times the vacuum of `V₀`
(`slice_vacElem_eq_vacuumFactor_smul`). It is chosen from `IsAdapted.slice_omega_vacElem`. 

### `slice_vacElem_eq_vacuumFactor_smul`

 The defining property of `vacuumFactor`: if the splitting `D` of `V` over `V₀` is adapted at
`1` in the basis `t`, the mixed term at `x` of the vacuum of `V` is
`vacuumFactor hD * ‖vacuumFn (tᴴ x)‖ ^ 2` times the vacuum of `V₀`, where `vacuumFn` is the standard
vacuum function on adelic vectors. 

### `eq_of_integrated_zeroTerm_eq`

 If `D` is adapted at `1`, two vectors `v` and `u` of the Fock space of `V₀` are equal as soon
as `V₀.integrated v` and `V₀.integrated u` (the operators `f ↦ v ⊗ f`) agree on all zero terms
`D.zeroTerm (V.projReal f)` of projections on the real vacuum of `V`. 

### `_root_.New.Space.Splitting.IsAdapted.mixedModel`

 The mixed Schrödinger–Fock model at the infinite places of a splitting `D` adapted at `1` in
the basis `t`. Its three blocks of directions are the real parts of `l tᴴ⁻¹`, `ι` and `k t`. The
slice at `a` is the translation by `l tᴴ⁻¹ a` followed by the map of Fock spaces that the zero term
induces (`New.Space.Splitting.IsAdapted.exists_apply_zero_omega_integrated_eq`). 

### `zeroTerm_integrated`

 If `D` is adapted at `1`, the zero term of `v ⊗ f` (written `V.integrated v f`) is
`v' ⊗ f'`, where `v'` is the slice at `0` of `v` in the real mixed model and `f'` is the zero term
of the projection of `f` on the real vacuum. 

### `slice_integrated`

 If `D` is adapted at `1` in the basis `t`, the mixed term at `(t⁻¹)ᴴ x` of `v ⊗ f` (written
`V.integrated v f`) is `v' ⊗ f'`, where `v'` is the slice of `v` in the real mixed model at the
real coordinates of `x` and `f'` is the mixed term at `(t⁻¹)ᴴ` times the finite part of `x` of the
projection of `f` on the real vacuum. 


## The real part of the terms along a line in each space

`New.Exchange.lineTermReal` is the map of Fock spaces that the operator `New.Exchange.lineTerm`
induces at the infinite places: a slice of the real mixed model
`New.Space.Splitting.IsAdapted.mixedModel` of the splitting `New.Exchange.lineTermSplitting`, taken
at a point supported on the last coordinate.


### `targetWeight`

 For a source space with finite basis `n` and a character of weight `μ`, the weight
`⌊#n / 2⌋ - μ w` in which the real points of the target group act at the infinite place `w`. 

### `lineTermReal`

 For base-adapted splittings `A` of `W'` over `W` and `X` of `V'` over `V` along lines, the real
part of the operator `lineTerm A X β a` (`β` selects one of its two models): the slice, in the real
mixed model of the splitting `lineTermSplitting A X β` of `Hom(W', V')` over `Hom(W, V)`, at the
point with coordinates `a` on the last coordinate (the line) and `0` elsewhere. 


## The real slice of a datum in the mixed model

For an adapted splitting `D` of `X` into a hyperbolic part and `W₁` (`New.Space.Splitting`,
`New.Exchange.IsBaseAdapted`), a vector of the Fock space `New.PairFock` of the pair `(X, V)` is
read in the mixed model as a function of a matrix `x` with values in the Fock space of `(W₁, V)`.


### `New.Exchange.realSlice`

 The slice of a real datum for (X, V) at the real part of the adelic matrix x: its value in the
mixed model attached to the splitting of Hom(X, V) induced by the base-adapted splitting D of X
over W₁, a real datum for (W₁, V). 


## Slices of named data in the mixed model

A vector of the global model is named by a function `Φ` of the components at a set `S` of finite
places (`New.Exchange.namedVector`). The components are read by a ring map `π : 𝔸f E →+* F`
(`New.Exchange.ReadsAt`) into a product of local fields `F` with integers `O`
(`New.SemilocalField`).


### `ReadsAt.lift`

 A chosen continuous additive section of `π` that takes `π x` to `idem S * x`, where `idem S` is
the idempotent of `𝔸f E` that is 1 at the places of `S` and 0 elsewhere
(`ReadsAt.continuous_lift_and_apply_lift`). 

### `ReadsAt.ψ`

 The additive character `y ↦ selfDualAddChar E (σ y)` of `F` (`selfDualAddChar E` is the
character of `𝔸f E` for which `Ô E` is self-dual), where `σ = h.lift` is a chosen section of `π`
with `σ (π x) = idem S * x`. 

### `ReadsAt.hasIntegralConductor_psi`

 If `π` reads the components at `S`, the induced character `h.ψ` of `F` has conductor the ring
of integers `O`: it is continuous, and `h.ψ (t * ·)` is trivial on `O` exactly for `t ∈ O`. 

### `ReadsAt.measurePreserving_comp`

 If `π : 𝔸f E →+* F` reads the components at `S`, then applying it coordinatewise carries the
Haar measure of finite adelic vectors (mass one on the integral vectors), restricted to the
vectors integral at the places outside `S`, to the volume on `p → F`. 

### `ReadsAt.sliceDatum_eq_prod_setIntegral_smul`

 Suppose that at the points with coordinates `(π x, z, y)` in the frame `D.frameAt 1 u` a
continuous function `Φ` is the product of the `f i (z i)`, cut off to `O`, times `Ψ y`. Then the
partial Fourier integral `sliceDatum` of `Φ` at the finite part of `x` is the product of the Fourier
integrals of the `f i` over `O` times `Ψ`. 

### `slice_localDatum`

 The slice `D.slice` at `u⁻¹ᴴ (scaleIdele E • x)` of a datum `v ⊗ Φ` (`localDatum`: real
part `v`, named by the Schwartz–Bruhat function `Φ` of the components read through `π`;
`scaleIdele E` is the fixed scaling idele). Here `D` is adapted in the basis `u`, with adelic frame
`D.frameAt 1 u`. Suppose that at the points with coordinates `(π x, z, y)` in this frame the
function `Φ` is the product of the `f i (z i)`, cut off to `O`, times `Ψ y`. Then the slice is the
datum of `Ψ` and of the real slice of `v`, times the constant `vacuumFactor` (replaced by zero
unless the finite part of `x` is integral off `S.conjClosure`) and the Fourier integrals of the
`f i` over `O`. 

### `adaptedFrame`

 For a base-adapted splitting `A`, the images under `π` of the finite parts of the adelic frame
`(k, ι, l)` and of its dual frame, as mutually inverse integral matrices over `F`. 


## Slices of data standard in an integral frame

`New.Exchange.ReadsAt.homSlice_localDatum` computes the term `New.Space.Splitting.homSlice` of a
datum `v ⊗ Φ` (`New.Exchange.localDatum`) for a base-adapted splitting `D`
(`New.Exchange.IsBaseAdapted`), when the function `Φ` of the components at `S` agrees with a
standard datum (`New.Exchange.IntegralFrame.stdDatum`) of the integral frame of `D` on the matrices
with the given first block.


### `IntegralFrame.isIntMatrix_iff_blocks`

 A matrix has entries in `O` exactly when its three blocks of coordinates in an integral frame
do. 

### `IntegralFrame.blocks_mul_K`

 The matrix with blocks of coordinates `k`, `w`, `l` in the frame `A` has first block `k`. 

### `IntegralFrame.stdDatum_blocks`

 At the matrix with blocks of coordinates `k`, `w`, `l` in the frame `A`, the function
`A.stdDatum G` is `G (k, w)` if the three blocks are integral and `0` otherwise. 

### `ReadsAt.setIntegral_psi_mul`

 Orthogonality of characters: the integral of `t ↦ h.ψ (c * t)` over `O` is `1` if `c` lies in
`O` and `0` otherwise, since `h.ψ` has conductor `O` and `O` has volume one. 

### `ReadsAt.mem_Ô_iff`

 A finite adele `c` is integral exactly when it is integral off `S` and its conjugate, on the
conjugate of `S` (read by `π (star c)`), and on `S` (read by `π c`). 

### `ReadsAt.homSlice_localDatum`

 Let `Φ` be a Schwartz–Bruhat function, and write `y` for the finite part of `x`. Suppose that
on the matrices `w` whose first block in the frame of `D` is `π y`, the function `Φ` is `G` of the
first two blocks if `w` is integral and `0` otherwise (`stdDatum`). Then `D.homSlice` (translate
by the map that is the given point on the `k`-frame, then take the zero term) of `v ⊗ Φ`
(`localDatum`) at `scaleIdele E • x` is zero unless `y` is integral; then it is `vacuumFactor`
times the real slice of `v` at `x` tensored with the function `z ↦ G (π y, z)` on integral `z`. 
