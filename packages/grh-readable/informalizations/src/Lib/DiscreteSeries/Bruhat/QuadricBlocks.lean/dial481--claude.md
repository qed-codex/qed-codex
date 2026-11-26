---
{
  "module": "src/Lib/DiscreteSeries/Bruhat/QuadricBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/QuadricBlocks.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/QuadricBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Solving the equation of a quadric in a block of coordinates

Let a hermitian form T on A^κ be the orthogonal sum of an orthonormal block and of its complement.
On a quadric in a hyperbolic plane plus T the part w of a vector outside the block is free, and the
part in the block lies on a quadric of the block, whose value is that of the given quadric minus
h(w, w). The measure of the quadric is the volume in w times the measures of these quadrics of the
block. This holds at any place, for any s-finite kernel that disintegrates the volume of the block
along its form.

## Main definitions and results
* `New.Floors.Place.IsSolvedIn`: a measure is the volume in the coordinates outside a block times
  an s-finite kernel of measures in the coordinates of the block, each of mass at most M on a box.
* `New.Floors.Place.IsDisintegration.lintegral_lintegral_comm`: on the orthogonal sum of two
  spaces, each with an s-finite kernel that disintegrates its measure, the equation of a quadric
  may be solved in either of them.
* `New.Floors.Place.IsDisintegration.isSolvedIn_quadricMeasure`: the measure of a quadric is solved
  in an orthonormal block, given an s-finite kernel on the quadrics of the block that disintegrates
  the volume and gives mass at most M to a box.

Notions from other files:
* `New.Floors.Place`: a star ring A with Haar volume, an element τ of trace one, a skew unit δ and
  a Haar measure ν on the skew elements.
* `New.Floors.Place.quadricMeasure`: the measure on the quadric h(y, y) = δ⁻¹ b in a hyperbolic
  plane plus T, the image of a product measure under `New.Floors.Place.flatChart`. Here b, the
  index of the quadric, is skew.
* `New.Floors.Place.IsDisintegration`: a family of measures on the quadrics of a form, continuous
  in the index, whose integral over the index is a given measure.

## Relation to the literature
Elementary: Tonelli's theorem and the invariance of Haar measure.


### `coordinateBox`

 The vectors with all coordinates in S. 

### `volume_coordinateBox`

 The box of S in A^κ has volume vol(S)^(card κ). 

### `exists_equiv_comp_inr_eq`

 An injective map to a finite type κ extends to a bijection onto κ from the disjoint union of
its source with a finite type. 

### `exists_kernel_eq_map`

 The images of an s-finite measure under a measurable family of maps form an s-finite kernel. 

### `measurePreserving_sumElim_comp_symm`

 Joining two vectors along a bijection of indices preserves the volume. 

### `IsSolvedIn`

 The measure ρ on A^κ is solved in the block of coordinates `blk`: it is the volume in the other
coordinates w times measures ζ(w) in the coordinates of the block. The ζ(w) form an s-finite kernel,
and each gives mass at most M to the box of S, the vectors with all coordinates in S. 

### `isSolvedIn_volume`

 The volume is solved in any block: it is the volume in the other coordinates times the volume in
the coordinates of the block. Any bound M for the volume of the box of S in A^B may be taken. 

### `quadricIndex`

 The index of the quadric h(x, x) = r: the skew element τδr − star (τδr), with τ of trace one and
δ the skew unit of the place. It is δr if r is hermitian. 

### `measurable_quadricIndex`

 The index of the quadric h(x, x) = r is a measurable function of r. 

### `coe_quadricIndex`

 For hermitian r the index `quadricIndex r` is δr, where δ is the skew unit of the place. 

### `IsDisintegration.lintegral_quadricIndex`

 Let the measures l(b) disintegrate μ along h(x, x) = x̄ᵀJx. Then ∫ G(index of h(x, x), x) dμ is
the double integral of G(b, x) against dl(b) and the Haar measure ν = `skewMeasure` of skew b. Here
the index of r is `quadricIndex r`, which is δr for hermitian r. 

### `IsDisintegration.lintegral_lintegral_comm`

 Let the s-finite kernels l and l' disintegrate μ and μ' along the forms J and J', so that l(b)
lives on the vectors whose value under the form has index b (`quadricIndex`). On the quadric of
index β of the sum of the forms, one may let the first vector run freely and solve for the second,
or the reverse: the two iterated integrals agree. 

### `submatrix_eq_fromBlocks_one_of_orthonormal`

 Let T be hermitian and let e split κ into κ₂ and B so that the basis vectors indexed by B are
orthonormal and orthogonal to the others. Then T is block diagonal along e, with block 1 on B. 

### `flatChart_sumElim_comp_symm`

 Let T be block diagonal along e, with blocks T₂ and 1. In the flat chart of the quadric of index
β of a hyperbolic plane plus T, the part z in the second block is free, and the rest is the flat
chart of the quadric of index β − (index of h(z, z)) of the plane plus T₂. 

### `measurePreserving_join_coordinates`

 The volume in (z, (t, w), a) is carried to that in ((t, x), a), where x joins w and z along e
and a is skew. 

### `IsDisintegration.isSolvedIn_quadricMeasure`

 Let the measures l(b) on A^B, for skew b, disintegrate the volume along x ↦ x*x, so l(b) is the
fibre measure on x*x = δ⁻¹b with δ the skew unit of the place, and let each give mass at most M to
the box of S (vectors with all coordinates in S). For a hermitian form T on A^κ, let `blk` inject B
into indices whose rows of T are those of the identity. Then `quadricMeasure T β`, the fibre measure
dv / dh(v, v) on the quadric h(v, v) = δ⁻¹β with h a hyperbolic plane plus T, is solved in this
block: it is the volume in the other coordinates times an s-finite kernel of block measures, each of
mass at most M on the box. 
