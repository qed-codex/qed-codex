---
{
  "module": "src/Lib/General/Geometry/DenseComplexPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/DenseComplexPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/DenseComplexPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense families of complex points: reduced closures, separation of maps, and arcs

Identities between functions or morphisms on a reduced scheme can be checked on a dense family of
complex points. `New.IsDenseFamily ξ` says that the points `ξ z : Spec ℂ ⟶ X` have dense image, and
`New.IsSeparatingFamily ξ` says that moreover `X` is reduced. Every family of complex points factors
through its reduced closure, on which it is separating.

## Main definitions and results

* `New.exists_reduced_closure`: any family of complex points of `X` factors through a closed
  subscheme in which it is `New.IsSeparatingFamily`, namely the reduced closure.
* `New.IsSeparatingFamily.pointFn_ext`, `New.IsSeparatingFamily.hom_ext`: regular functions, and
  morphisms over `S` to a scheme separated over `S`, that agree at the points are equal.
* `New.IsSeparatingFamily.exists_map_of_coords`: if a linear system on `X` gives the points `e z`
  the same coordinates as a projective embedding of `G` gives points `p z`, then it comes from a
  morphism `X ⟶ G` that sends `e z` to `p z`.
* `New.exists_valuative_arc_of_isDenseFamily` joins any point of a locally noetherian scheme with
  finitely many dense complex points to one of them by an arc `Spec V → S`, with `V` the ring of a
  valuation of `ℂ` in `ℝ≥0`.

Notions from other files:
* `New.PointFn X`: rules that attach an element of `A` to every ring-valued point `Spec A ⟶ X`.
  It is regular on `U` (`IsRegularOn`) if, at points landing in `U`, it commutes with ring maps.
* `New.LineBundle X ι`: an open cover `U_i` of `X` with transition functions `g_ij`.
* `New.LineBundle.IsHomogeneousCoords`: `v` is a vector of homogeneous coordinates of the point `t`,
  that is, `t` lands in `U_j` exactly when `v_j` is a unit, and then `g_jk(t) = v_k / v_j`.
* `New.LineBundle.IsLinearSystem`: the data of a map to projective space, the model being
  `g_ij = s_j / s_i` on `U_i = {s_i ≠ 0}` for sections `s_i` without common zero.
* `New.LineBundle.IsProjEmbedding`: a linear system on a proper `X ⟶ S` for which points in one
  chart with the same affine coordinates and the same image in `S` are equal.


 ## Reduced closures of families of complex points 

### `New.exists_lift_of_dense_preimage`

 Let `i : Y ⟶ Z` be a closed immersion and `f : X ⟶ Z` with `X` reduced. If the preimage under
`f` of the image of `i` is dense in `X`, then `f` factors through `i`. 

### `New.IsDenseFamily`

 The images of the complex points `ξ z : Spec ℂ ⟶ X` form a dense subset of `X`. 

### `New.IsSeparatingFamily`

 `X` is reduced and the complex points `ξ z` are dense in it, so that regular functions are
determined by their values at these points. 

### `New.exists_reduced_closure`

 Reduced closure: complex points `ξ z : Spec ℂ ⟶ X` factor as `ξ z = i ∘ e z` through a closed
immersion `i : Y ⟶ X`, with `Y` reduced and the points `e z` dense in `Y`
(`IsSeparatingFamily e`). 

 ## Functions and morphisms on reduced schemes determined by dense points 

### `IsDenseFamily.surjective`

 A universally closed morphism `f : Y ⟶ X` is surjective if every point `ξ z` of a dense family
of complex points of `X` lifts to a complex point `y z` of `Y`. 

### `pointFn_ext`

 Let `X` be reduced and the complex points `ξ z` dense. Two functions on ring-valued points that
are regular on an open `U` (compatible with ring maps at points of `U`) and agree at all `ξ z`
landing in `U` agree at every ring-valued point `t` landing in `U`. 

### `hom_ext`

 Let `e z` be complex points of the `S`-scheme `X` over the points `η z` of `S`, with `X` reduced
and the `e z` dense. Two morphisms over `S` from `X` to a separated `G` that agree at every `e z`
are equal. 

### `exists_map_of_coords`

 Let `e z`, `p z` be complex points of the `S`-schemes `X`, `G` over the same point `η z`, with
`X` reduced and the `e z` dense. If a linear system `W` on `X` and a projective embedding `M` of
`G`, both with the finite index set `ι`, give `e z` and `p z` the same homogeneous coordinates
`v z`, then some morphism `d : X ⟶ G` over `S` sends each `e z` to `p z` and pulls the charts and
transition functions of `M` back to those of `W`. 

 ## Arcs from dense complex points to arbitrary points 

### `New.isPrime_map_C_mvPolynomial`

 The extension of a prime ideal of `A` to a polynomial ring over `A` is prime. 

### `New.height_map_C_le_one`

 A prime of a noetherian ring that is minimal over one element extends to a prime of height at
most one in a polynomial ring in finitely many variables. 

### `New.eq_map_C_of_ne_bot_of_le_map_C`

 Let `p` be a prime of a noetherian domain `A` that is minimal over one element. A nonzero prime
`J` of a polynomial ring over `A` that lies in the extension of `p` equals that extension. 

### `New.exists_valuation_le_pow_of_maximalIdeal_le`

 Let `V` be a valuation subring of a field in which every nonzero prime ideal contains the
maximal ideal. Then the valuation of `V` is archimedean: every value is bounded by a
power of any value above one. 

### `New.exists_nnreal_valuation`

 A valuation subring `V` of a field, in which every prime ideal with a nonzero element `c`
contains the maximal ideal, is the ring of a valuation with values in `ℝ≥0`. 

### `New.exists_subalgebra_minimalPrimes_span_singleton`

 Blowing up inside a valuation ring. Let `O ⟶ W` be a local map from a noetherian local ring to
a valuation ring. Then `W` has a noetherian `O`-subalgebra `A` with a prime `p` that is minimal
over one element and lies over the maximal ideal of `O`. 

### `New.exists_valuationSubring_comap_maximalIdeal_eq`

 Let `e` identify a ring `R` with a subring of a field `K`. Every prime `P` of `R` is the centre
of a valuation subring `U` of `K` that contains `R`. 

### `New.exists_nnreal_valuation_le_comap_maximalIdeal`

 Let `A` be a noetherian subring of a field `K` and `p` a prime of `A` that is minimal over one
element. Then `A` lies in the ring of a valuation `v` of `K` with values in `ℝ≥0`, in such a way
that `p` lies in the maximal ideal. 

### `New.exists_valuative_arc_of_isDenseFamily`

 Let `S` be a locally noetherian scheme with finitely many complex points `η i` whose images are
dense. For every point `s` of `S` there are an index `i`, a valuation `v` of `ℂ` with values in
`ℝ≥0` and a morphism `a` from the spectrum of its valuation ring `V` to `S` that restricts to `η i`
along `Spec ℂ ⟶ Spec V` (the map `specMap` of the inclusion) and sends the closed point to `s`. 
