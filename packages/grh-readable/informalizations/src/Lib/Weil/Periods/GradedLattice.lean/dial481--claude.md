---
{
  "module": "src/Lib/Weil/Periods/GradedLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/GradedLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/GradedLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iwasawa decomposition for the flag of the grades

`New.Grading.exists_isGraded`: let `V` be a hermitian space over a CM field with a primitive root of
unity of order 5040, with a grading `Y` of its basis. Every point of the finite adelic unitary group
is moved by some unipotent element to a point whose lattice is graded.

The lattice has a basis that does not lower grades (Hermite form). Witt's theorem over `Ô` corrects
it so that its Gram matrix is that of its part of degree `0`
(`New.Grading.exists_gram_mul_eq_gram_degreeZeroPart`).

The map between the corrected basis and that part is a unipotent isometry.

Notions from other files:
* `New.Grading`: an indexing of the basis of a hermitian space by `X` and a string of `s` vectors in
  which the Gram matrix `V.J` is the standard one, `gradedGram Y.indexEquiv N`, with constant `N`
  (and `V.J⁻¹` is the one with constant `N⁻¹`); it gives every index a grade `Y.gradeOf i`.
* `New.HasDegreeGe w' w d A`: the entry `A i k` is `0` whenever `w' i < w k + d`.
* `New.intGL ι (Ô E)`: the invertible matrices with entries in the integral finite adeles `Ô E`
  whose inverse has entries there too.
* `New.Space.lattice V x`: the vectors whose coordinates in the frame `V.xFin * x` are integral,
  where `x` is a finite adelic unitary matrix.
* `New.Grading.IsGraded`: a lattice contains the part in each grade of each of its vectors.

## Relation to the literature

Known result: the Iwasawa decomposition of an unramified unitary group. Source: J. Tits, Reductive
groups over local fields, Proc. Sympos. Pure Math. 33 (1979), 3.3.2.


### `degreeZeroPart`

 The part of degree `0` of a matrix `A`, for weights `w'` on the rows and `w` on the columns:
the entries `(i, k)` with `w' i = w k` are kept and the others are replaced by `0`. 

### `HasDegreeGe.sub_degreeZeroPart`

 If `A i k = 0` whenever `w' i < w k`, then removing the part of degree `0` from `A` leaves a
matrix whose entries vanish whenever `w' i ≤ w k`. 

### `degreeZeroPart_mul`

 On matrices of degree at least `0` (the entry `(i, k)` vanishes where the weight of the row is
less than that of the column), taking the part of degree `0` (the entries where these two weights
are equal) is multiplicative. 

### `IsIntMatrix.degreeZeroPart`

 If all entries of `A` lie in the subring `O`, then so do those of its part of degree `0`. 

### `HasDegreeGe.conjTranspose`

 If `A` raises weights by at least `d`, from `w` on the columns to `w'` on the rows, then `Aᴴ`
does so from `-w'` on the columns to `-w` on the rows. 

### `degreeZeroPart_conjTranspose`

 Taking the part of degree `0` commutes with the conjugate transpose, the weights of rows and
columns being negated and swapped. 

### `isPrimitiveMatrix_submatrix_of_mem_intGL`

 Distinct columns of an element of `GL(Ô)` form a primitive matrix: one with integral entries
and an integral left inverse. 

### `Space.frame_mul_conjTranspose`

 For the orthonormal frame `g = V.xFin * x` (`V.xFin` is a fixed finite adelic frame with
`V.xFinᴴ * V.J * V.xFin = 1`) of the lattice of a point `x` of the finite adelic unitary group, the
matrix `g * gᴴ` is the image in the finite adeles of the inverse of the Gram matrix `V.J` of `V`. 

### `exists_gram_eq_degreeZeroPart`

 Let `E` be a CM field with a primitive root of unity of order 5040, and let `k` lie in
`GL(Ô)` (invertible over the integral finite adeles), with Gram matrix `G = kᴴ * k`. Suppose that
`G i j = 0` for `w i + w j > 0` and `G⁻¹ i j = 0` for `w i + w j < 0`. Then a change of basis `n` in
`GL(Ô)`, with `n - 1` raising the weights `w`, carries `G` to its part on the entries with
`w i + w j = 0`. 

### `exists_basis_hasDegreeGe`

 Hermite form for the flag of the grades: for an invertible adelic matrix `Z`, the `Ô`-lattice
spanned by its columns has a basis `b` (so `Z⁻¹ * b ∈ GL(Ô)`) such that `b` and `b⁻¹` do not lower
the grades of the grading `Y`. 

### `map_gradedGram_apply_eq_zero`

 The matrix `gradedGram Y.indexEquiv M`, the standard Gram matrix for the indexing of `Y` with
any constant `M`, has row `i` zero outside column `Y.stringReversal i`, so it pairs grade `d` only
with grade `-d`; this is stated for its image in the finite adeles. 

### `degreeZeroPart_mulVec_gradeProj`

 The part of degree `0` of a matrix `A`, for the grades of `Y`, commutes with the projection to
each grade. 

### `exists_gram_mul_eq_gram_degreeZeroPart`

 For a finite point `x` of `V`, let `b` be a basis of the lattice `V.lattice x` (that is, `b`
differs from `V.xFin * x` by an element of `GL(Ô)`) such that `b` and `b⁻¹` do not lower the grades
of the grading `Y`. Then for some `n` in `GL(Ô)`, with `n - 1` raising grades, the basis `b * n` has
the same Gram matrix for the form `V.J` as the part of degree `0` of `b`. Here `E` is a CM field
containing a primitive root of unity of order `5040`. 

### `exists_isGraded`

 Iwasawa decomposition for the flag of the grades of the grading `Y` of `V`, over a CM field with
a primitive root of unity of order 5040: for every point `x` of the finite adelic unitary group
there is a `u` such that `(1, u)`, the adelic element that is `1` at the infinite places, lies in
`Y.unipotent` (its matrix in rational coordinates, minus `1`, raises grades) and the lattice
`V.lattice (u * x)` of the point `u * x` is graded, that is, contains the part in each grade of each
of its vectors. 
