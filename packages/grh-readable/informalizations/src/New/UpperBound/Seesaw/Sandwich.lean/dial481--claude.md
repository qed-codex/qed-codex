---
{
  "module": "src/New/UpperBound/Seesaw/Sandwich.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Sandwich.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Sandwich.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds for the lattices of points on graded spaces

Let `Λ'` be the lattice `V.lattice x` of a finite point `x` of a graded space and `Λ` the lattice
of the point `1`. The file proves lattice steps of the induction for the bounds
`Q̄ ^ k Λ⁻ ⊆ Λ'⁻ ⊆ Q ^ (-k) Λ⁻`, where `q` generates `Q`.

* `New.Grading.smul_latticeMinus_le_of_map_latticePlus`: if `sh Λ⁺` is `a` times the `Λ⁻` of the
  next space, then the upper bound on one space and an inclusion `(q̄ / a) sh Λ'⁺ ⊆ Λ''⁻`, with
  `Λ''` the lattice of a point on the next space, give the lower bound on the next space.
* `New.Grading.SpansLattice.hasLatticeBounds_or_latticeSplitsAt`: for a grading over `X ⊕ Unit`,
  duality turns the lower bound into both bounds, unless `s` is odd and `Λ'` splits along `X ⊕ Unit`
  at a place above `N`.
* `New.Grading.LatticeSplitsAt.conj_scalarFin_mem`: if `Λ'` splits along `X` at a place `w ≠ w̄`,
  then the integral scalings of `X` supported at `w` and `w̄` preserve `Λ'`.

Notions from other files:

* `Gf E ι`: the finite adelic unitary group in the variables `ι`, whose elements are the finite
  points. The lattice `V.lattice x` is spanned over `Ô E` by the columns of `V.xFin * x`, where
  `V.xFin` is the finite frame of the hermitian space `V`.
* `New.Grading V N X s`: a splitting of the basis `ι` of `V` into an orthonormal part `X` of grade
  `0` and a string of `s` vectors, where vector `i` pairs only with vector `s - 1 - i`, to `1`,
  except that the middle vector (for odd `s`) pairs with itself to `-N`.
* `Y.latticePlus x`, `Y.latticeMinus x`: the projection `Λ'⁺` of the lattice of `x` to `X^⊥` and
  its intersection `Λ'⁻` with `X^⊥`, the span of the string.
* `Y.stringMapFin Y'`: the shift `sh` from the vectors of one graded space to those of the next.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `LatticeSplitsAt`

 Let `Y` split the basis of `V` into `X` and a string spanning `X^⊥`, and let `Λ' = V.lattice x`
be the lattice of the point `x` of the finite adelic unitary group. Then `Λ'` splits along `X` at
the place `w` if there the projection `Λ'⁺` of `Λ'` to `X^⊥` lies in the intersection `Λ'⁻` of `Λ'`
with `X^⊥`, so the two are equal. The idempotent `idem {w}` cuts out the component at `w`. 

### `LatticeSplitsAt.conj`

 If the lattice of `x` splits along `X` at the place `w`, then it splits at the complex conjugate
place `star w` too. 

### `inclXFin_scalarFin_mulVec`

 In rational coordinates, the finite point `Y.inclXFin (scalarFin X z)` of `U(V)`, which scales
`X` by `z`, sends a vector `y` to `y + (z - 1) (y - p y)`, where `p = Y.stringProj` is the
projection to `X^⊥`. 

### `LatticeSplitsAt.idem_smul_sub_stringProj_mem`

 Let the lattice of `x` split along `X` at the place `w`: there its projection to `X^⊥` lies in
the lattice. For every vector `y` of the lattice, the component at `w` (cut out by `idem {w}`) of
the part `y - Y.stringProj y` of `y` in `X` lies in the lattice. 

### `inclXFin_scalarFin_map_evalAt`

 At a place `u` where the unitary adele `z` is `1`, the finite point that scales `X` by `z`,
conjugated by the finite frame `V.xFin` into rational coordinates, has the identity matrix. 

### `LatticeSplitsAt.conj_scalarFin_mem`

 Let `x` be a point of the finite adelic unitary group `Gf E ι` whose lattice, spanned by the
columns of `V.xFin * x`, splits along `X` at a place `w ≠ w̄`: there its projection to `X^⊥` lies in
the lattice. Let `z` be an integral unitary adele that is `1` off `w` and `w̄`. Then the conjugate
by `x` of the scaling `Y.inclXFin (scalarFin X z)` of `X` by `z` lies in `maxCompactAt ι w`: it is
integral and trivial off `w` and `w̄`. 

### `smul_latticeMinus_le_of_map_latticePlus`

 Write `Λ⁺` and `Λ'⁺` for the projections to `X^⊥` of the lattices of `1` and `x`, `Λ⁻` and `Λ'⁻`
for their intersections with `X^⊥`, and `M⁻` and `M'⁻` for the intersections with `X'^⊥` of the
lattices of `1` and `x'` in `V'`. Let `sh Λ⁺ = a M⁻` and `(q̄ / a) sh Λ'⁺ ⊆ M'⁻` for finite ideles
`a`, `q`. Then the upper bound `q ^ k Λ'⁻ ⊆ Λ⁻` on `V` gives `q̄ ^ (k + 1) M⁻ ⊆ M'⁻` on `V'`. 

### `latticeSplitsAt_of_generates`

 Write `Λ±` and `Λ'±` for the projection to `X^⊥` (`+`) and the intersection with it (`-`) of the
lattices of `1` and `x`, and `v` for the valuation at a place. Let `q` and `q̄` be units at `w`, let
`q̄ ^ k Λ⁻ ⊆ Λ'⁻` and `q ^ k Λ'⁺ ⊆ Λ⁺`, and let `y ∈ Λ'⁻` be such that `q ^ k y` generates `Λ⁺` over
`Λ⁻` at `w`. Then the lattice of `x` splits at `w`: there `Λ'⁺ ⊆ Λ⁺ = Λ⁻ + Ô y ⊆ Λ'⁻`. 

### `SpansLattice.hasLatticeBounds_or_latticeSplitsAt`

 Let the lattice of `1` have the basis `gradedLatticeBasis` built from the ideles `a`, `π` and
the unitary adele `u`. Let `N = π π̄` with `π` a uniformiser at the places of `P`, none of which has
its conjugate in `P`, and a unit elsewhere, and let `q` be a unit at the places of `P` and their
conjugates. Write `Λ⁻` and `Λ'⁻` for the intersections of the lattices of `1` and `x` with
`(X ⊕ Unit)^⊥`, and assume the lower bound `q̄ ^ k Λ⁻ ⊆ Λ'⁻`. Then the upper bound `q ^ k Λ'⁻ ⊆ Λ⁻`
holds too, or `s` is odd and the lattice of `x` splits at some `w ∈ P`: there its projection to
`(X ⊕ Unit)^⊥` lies in `Λ'⁻`. 

### `HasBoundedOrbit.of_forall`

 Suppose that each translate `r x` by the finite Bessel subgroup `Y.besselFin` whose lattice is
graded (closed under the projections to the grades) has the bounds `Y.HasLatticeBounds q k`. Then
the orbit of `x` is bounded: some translate has both properties, as every orbit has a graded
lattice. The field `E` is assumed to contain a primitive root of unity of order `5040`. 

### `SpansLattice.hasBoundedOrbit_zero`

 Let the lattice of `1`, spanned by the finite frame `V.xFin`, have the basis
`gradedLatticeBasis` with parameters `a`, `π`, `u`. If the orbit of the finite point `x` under the
finite Bessel subgroup `Y.besselFin` has an integral point `r x ∈ stdLevel E ι`, then some point of
the orbit has a graded lattice with the bounds for `k = 0`: the lattice of `r x` is the one of
`1`. 
