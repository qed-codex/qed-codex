---
{
  "module": "src/Lib/Weil/Periods/PointLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/PointLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/PointLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lattice of a finite point of a graded space

A finite point `x` of the unitary group of a hermitian space `V` gives a self-dual lattice
`New.Space.lattice` over `Ô`, spanned by the orthonormal frame `V.xFin * x`. A grading
(`New.Grading`) writes `V = X ⊕ X^⊥`, where `X^⊥` is spanned by the string. The lattice has an
intersection `Λ'⁻` with `X^⊥` (`New.Grading.latticeMinus`) and a projection `Λ'⁺` to `X^⊥`
(`New.Grading.latticePlus`); `Λ⁻` is the intersection for the point `1`.

* `New.Space.mem_lattice_iff_formFin`: the lattice of a point is self-dual.
* `New.Space.lattice_eq_iff`: two points have the same lattice if and only if they differ by an
  integral unitary matrix.
* `New.Grading.mem_latticeMinus_iff_formFin`, `New.Grading.mem_latticePlus_iff_formFin`: the
  intersection and the projection are dual to each other.
* `New.Grading.exists_lattice_inclXFin_mul_eq`: lattices of points with the same intersection with
  `X^⊥` are conjugate under the unitary group of `X`, assuming `[HasPrimitiveRoot5040 E]`.

Notions from other files:
* `𝔸f E`, `Ô E`: the finite adeles of the CM field `E` and their subring of integral adeles.
* `Gf E ι`, `stdLevel E ι`: the matrices `g` over `𝔸f E` with `gᴴ g = 1`, and those with integral
  entries.
* `Space E ι ε`: a Gram matrix `V.J` over `E` with a frame `V.xFin` over `𝔸f E` in which the form is
  standard; `V.ratCoordMatrixFin g` is the matrix `V.xFin * g * V.xFin⁻¹`.
* `Grading V N X s`: an identification `Y.indexEquiv` of the basis indices with `X ⊕ Fin s`, for
  which the form is standard on `X` and the string of `s` vectors is orthogonal to `X`.

## Relation to the literature

The results are known: duality of lattices, and Witt's theorem for unimodular hermitian lattices.
Sources: O'Meara, Introduction to Quadratic Forms; Jacobowitz, Hermitian forms over local fields
(1962).


### `smul_le_iff_forall`

 An inclusion `c • A ≤ B` of lattices of finite adelic vectors can be checked on the vectors of
`A`. 

### `isPrimitiveMatrix_of_mulVec_mem_iff`

 A matrix `P` over the finite adeles with a left inverse (`HasLeftInv P`) is primitive (integral
with an integral left inverse) if, for every vector `c`, the vector `P c` is integral if and only
if `c` is. 

### `lattice`

 The lattice of a finite point `x`, in rational coordinates: the vectors whose coordinates in
the frame `V.xFin * x` are integral. 

### `formFin`

 The hermitian form of `V` on finite adelic vectors, conjugate linear in the first variable. 

### `mulVec_mem_lattice`

 The lattice of `x` consists of the images of the integral vectors in the frame
`V.xFin * x`. 

### `gram_xFin_mul_eq_one`

 For a finite point `x`, the frame `V.xFin * x` is orthonormal for the form of `V`. 

### `gram_frame_inv`

 The Gram matrix of `V` is `g⁻¹ᴴ g⁻¹` for the orthonormal frame `g = V.xFin * x`. 

### `formFin_eq_dotProduct`

 For a finite point `x`, the form of `V` is the standard form in the coordinates of the frame
`V.xFin * x`. 

### `star_formFin`

 The form of `V` on finite adelic vectors is hermitian. 

### `formFin_star_smul`

 A scalar moves from the second argument of the form of `V` to the first with a conjugation. 

### `mem_lattice_iff_formFin`

 The lattice of a point is its own dual: `z` lies in it if and only if its products with all
vectors of the lattice are integral. 

### `mulVec_mem_lattice_mul`

 The point `g`, acting in rational coordinates, carries the lattice of `x` onto that of
`g x`. 

### `lattice_le_iff`

 The lattice of `x'` is contained in that of `x` if and only if the change of frame `x⁻¹ * x'`
is integral, that is, lies in `stdLevel E ι`. 

### `lattice_eq_iff`

 Two points have the same lattice if and only if they differ by an integral unitary matrix. 

### `conj_mem_stdLevel_iff`

 The conjugate `x⁻¹ g x` lies in the group `stdLevel E ι` of integral unitary matrices if and
only if `g`, acting through its matrix `V.ratCoordMatrixFin g` in rational coordinates, maps the
lattice of `x` into itself. 

### `ratCoordMatrixFin_isometry`

 The matrix of a finite point `g` in rational coordinates preserves the Gram matrix of `V`. 

### `gradeProj`

 The projection to the span of the basis vectors `i` of grade `d`, that is, with
`Y.gradeOf i = d`, where `Y.gradeOf` is the integer grade that the grading attaches to each
index. 

### `stringProj`

 The orthogonal projection to `X^⊥`, the span of the string. 

### `IsGraded`

 A lattice is graded if it contains, for each integer `d`, the part `Y.gradeProj d y` of grade
`d` of each of its vectors `y`. 

### `latticeMinus`

 The intersection `Λ'⁻` of the lattice of `x` with `X^⊥`. 

### `latticePlus`

 The projection `Λ'⁺` of the lattice of `x` to `X^⊥`. 

### `HasLatticeBounds`

 The bounds `q̄ ^ k Λ⁻ ⊆ Λ'⁻` and `q ^ k Λ'⁻ ⊆ Λ⁻`, where `Λ'⁻` and `Λ⁻` are the intersections
with `X^⊥` of the lattices of `x` and of `1`. 

### `HasLatticeBounds.lower`

 `q̄ ^ k Λ⁻ ⊆ Λ'⁻`. 

### `HasLatticeBounds.upper`

 `q ^ k Λ'⁻ ⊆ Λ⁻`. 

### `HasBoundedOrbit`

 The orbit of `x` under the finite Bessel subgroup has a point whose lattice is graded and
satisfies the bounds `New.Grading.HasLatticeBounds`. 

### `stringMapFin`

 The finite part of the matrix `Y.stringMap Y'` (the second component of each of its entries),
acting on vectors: the map between two graded spaces that kills `X` and sends each string vector to
a multiple of the string vector with the same number. 

### `stringProj_eq_self_iff`

 A vector is fixed by the projection to `X^⊥` if and only if its coordinates on `X` vanish. 

### `stringProj_smul_of_mem_latticePlus`

 Multiples of vectors of the projection `Λ'⁺` lie in `X^⊥`. 

### `formFin_stringProj`

 The projection to `X^⊥` is self-adjoint for the form of `V`. 

### `mem_latticeMinus_iff_formFin`

 A vector `z` of `X^⊥` lies in the intersection `Λ'⁻` of the lattice of `x` with `X^⊥` if and
only if its products with the projection `Λ'⁺` of this lattice to `X^⊥` are integral. 

### `stringProj_eq_of_formFin_eq`

 The form of `V` is nondegenerate on `X^⊥`: vectors with the same products against `X^⊥` have the
same projection to `X^⊥`. 

### `exists_isPrimitiveMatrix_basis`

 The space `X^⊥` has a basis `B` that is primitive in the lattice of `x`: read in the frame
`V.xFin * x`, the matrix `B` is integral with an integral left inverse. 

### `mem_latticePlus_iff_formFin`

 A vector `z` of `X^⊥` lies in the projection `Λ'⁺` of the lattice of `x` to `X^⊥` if and only
if its products with the intersection `Λ'⁻` of this lattice with `X^⊥` are integral. 

### `formFin_star_smul_mem`

 Let `Λ'⁻` and `Λ'⁺` be the intersection with `X^⊥` and the projection to `X^⊥` of the lattice
of `x`. If `c A ⊆ Λ'⁻`, then every vector of `c̄ Λ'⁺` has integral products with the vectors of
`A`. 

### `star_smul_latticePlus_le`

 Let `Λ₁⁻`, `Λ₂⁻` be the intersections with `X^⊥` of the lattices of `x`, `x'`, and `Λ₁⁺`,
`Λ₂⁺` their projections to `X^⊥`. An inclusion `c Λ₁⁻ ⊆ Λ₂⁻` gives `c̄ Λ₂⁺ ⊆ Λ₁⁺` by duality. 

### `star_smul_latticePlus_le_latticeMinus`

 Let `Λ'⁻` and `Λ'⁺` be the intersection with `X^⊥` and the projection to `X^⊥` of the lattice
of `x`. An inclusion `c Λ'⁺ ⊆ Λ'⁻` gives `c̄ Λ'⁺ ⊆ Λ'⁻` by duality. 

### `exists_inclXFin_eq_of_mulVec_eq`

 A finite point `g` whose matrix `V.ratCoordMatrixFin g` in rational coordinates fixes `X^⊥`
(the span of the string) pointwise is in the image of the embedding `Y.inclXFin` of the unitary
group of `X`. 

### `exists_lattice_inclXFin_mul_eq`

 Assume that `E` contains a primitive root of unity of order 5040
(`[HasPrimitiveRoot5040 E]`). If the lattices of two points have the same intersection with
`X^⊥`, then some finite point `a` of the unitary group of `X`, embedded by `Y.inclXFin` in that of
`V`, carries one lattice to the other. 
