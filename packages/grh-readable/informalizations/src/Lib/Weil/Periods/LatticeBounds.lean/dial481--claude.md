---
{
  "module": "src/Lib/Weil/Periods/LatticeBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/LatticeBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/LatticeBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finitely many orbits of lattices satisfy the bounds

Let `V` be a hermitian space presented as a part `X` plus a string of vectors. For a finite point
`x` let `Λ'⁻` be the intersection of its lattice with `X^⊥`, and `Λ⁻` the same for the point `1`.
The bounds are `q̄ ^ k Λ⁻ ⊆ Λ'⁻` and `q ^ k Λ'⁻ ⊆ Λ⁻`, for a finite adele `q` and a natural number
`k`.

* `New.Grading.finite_image_latticeMinus`: if `q` is invertible, finitely many `Λ'⁻` satisfy the
  bounds.
* `New.Grading.HasLatticeBounds.latticeMinus_componentOn`: under the bounds, `Λ'⁻` does not change
  when the components of `x` outside `Q ∪ Q̄` are replaced by `1`, for a set `Q` of places outside
  which `q` has valuation `1`.
* `New.Grading.exists_finite_representatives`: let `E` contain a primitive root of unity of order
  5040, let `q` be invertible and have valuation `1` outside `Q`. Among the double cosets under the
  finite Bessel subgroup and the stabiliser of the standard lattice, those with bounded orbit have
  finitely many representatives, supported on `Q ∪ Q̄`.

Notions from other files:
* `New.Grading`: an indexing of the basis of `V` by `X` and a string of vectors, with Gram matrix
  `1` on `X` and anti-diagonal on the string, which spans `X^⊥`; `stringProj` projects onto `X^⊥`.
  It gives each basis vector an integer grade; the part of a vector in a grade is its projection to
  the span of the basis vectors of that grade.
* `New.Space.lattice`: the lattice of a point `x`, the vectors with integral coordinates (entries in
  `Ô E`) in its frame, the columns of the matrix `V.xFin * x`, where `V.xFin` is the fixed
  invertible finite adelic matrix whose columns span the lattice of the point `1`.
* `New.idem`: the finite adele that is `1` at the places of a set and `0` at the others.
* `atPlace`: the component of a finite point at a place; `v`: the valuation of such a place.

## Relation to the literature

Known result: there are finitely many lattices between two given ones, and a lattice is determined
by its local components. Source: O'Meara, Introduction to Quadratic Forms, §81.


### `isOpen_lattice`

 The lattice of a finite point is open: it is the preimage of the integral vectors under the
inverse of the matrix of its frame. 

### `isCompact_lattice`

 The lattice of a finite point is compact: it is the image of the integral vectors under the
matrix of its frame. 

### `idem_smul_mem_lattice`

 The part `idem T • y` of `y` at the places of `T` lies in the lattice of `x` if and only if the
coordinates of `y` in the frame `V.xFin * x` of that lattice are integral at these places. 

### `idem_smul_mem_lattice_congr`

 If two points have the same components at the places of `T`, then the part `idem T • y` of a
vector `y` at these places lies in both of their lattices or in neither. 

### `smul_idem_smul_mem_lattice`

 For a scalar `c` of valuation `1` at the places of `T`, the part `idem T • y` of `y` at `T`
lies in a lattice if and only if its product with `c` does. 

### `mem_lattice_iff_idem_smul`

 A vector lies in a lattice if and only if its parts at the places of `T` and off `T` do. 

### `finite_image_latticeMinus`

 For an invertible finite adele `q`, the points `x` of the finite adelic unitary group with the
bounds `q̄ ^ k Λ⁻ ⊆ Λ'⁻`, `q ^ k Λ'⁻ ⊆ Λ⁻` give only finitely many intersections `Λ'⁻` of their
lattice with `X^⊥`. Here `Λ⁻` is the intersection for `x = 1`. 

### `HasLatticeBounds.latticeMinus_componentOn`

 Let `Y` present the hermitian space `V` as a part `X` plus a string of `s` vectors, which spans
`X^⊥`. For a point `g` of the finite adelic unitary group `Gf E ι`, `Y.latticeMinus g` is the
intersection with `X^⊥` of the lattice `V.lattice g`, the adelic vectors with integral coordinates
in the frame `V.xFin * g`. Write `Λ'⁻ = Y.latticeMinus x` and `Λ⁻ = Y.latticeMinus 1`, and assume
the bounds `q̄ ^ k Λ⁻ ⊆ Λ'⁻` and `q ^ k Λ'⁻ ⊆ Λ⁻` for a finite adele `q`. Let `Q` be a set of finite
places outside which `q` is a local unit (its multiplicative valuation `v` is `1`). Let
`x' = Gf.componentOn ι Q x` be the point with the components of `x` at the places of `Q` and their
conjugates, and with component `1` at the other places. Then `Y.latticeMinus x' = Λ'⁻`. 

### `exists_finite_representatives`

 Let `q` be an invertible finite adele of valuation `1` at the places outside `Q`, let `R` be the
finite Bessel subgroup `Y.besselFin` (it contains the image `Y.inclXFin a` of each point `a` of the
unitary group of `X`) and `J°` the stabiliser `stdLevel E ι` of the standard lattice. Assume that
`E` contains a primitive root of unity of order 5040. Then there is a finite set `T` of points
supported on `Q` and its conjugate such that `R x J°` meets `T` whenever the `R`-orbit of `x` is
bounded (`HasBoundedOrbit`: some point of it has a graded lattice whose intersection with `X^⊥`
satisfies the bounds given by `q` and `k`; graded means that it contains the part in each grade of
each of its vectors). 
