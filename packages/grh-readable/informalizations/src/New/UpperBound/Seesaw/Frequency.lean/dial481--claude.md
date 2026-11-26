---
{
  "module": "src/New/UpperBound/Seesaw/Frequency.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Frequency.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Frequency.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shift at a nonzero constant term maps lattices into lattices

`Y` and `Y'` present the spaces `V` and `V'` as a block plus a string, of lengths `s` and `s - 1`,
and `sh = Y.stringMap Y'` is the shift between the strings, of degree `-1`.

* `New.Grading.IsGraded.mulVec_mem_of_homogeneous`: a homogeneous part of a map between graded
  lattices maps the first lattice into the second.
* `New.Grading.exists_mapsTo_lattice_hasDegreeGe_sub_smul_stringMap`: let the constant term of
  `t ⊗ f` at `sh` not vanish at `(x, x')`, with `f` fixed by the Heisenberg operators of
  `b Ô ^ (ι' × ι)`; then modulo degree at least `0` the multiple `(b̄ / α) sh` maps the lattice of
  `x` into that of `x'`.
* `New.Grading.smul_map_stringMapFin_latticePlus_le`: at graded points this multiple of `sh` maps
  `Λ'⁺` of the first point into `Λ'⁻` of the second.

Notions from other files:
* `Y.gradeOf` is the grade of a basis index: `0` on the block `X` and `s - 1 - 2 i` on the string
  vector `i`; `HasDegreeGe w' w d A` says that the entry `(p, q)` of `A` is `0` if
  `w' p < w q + d`.
* `V.lattice g`, for a finite point `g`, is the lattice `g Λ` in rational coordinates;
  `Y.latticePlus g` is its projection `Λ'⁺` to `X^⊥` and `Y.latticeMinus g` is its intersection
  `Λ'⁻` with `X^⊥`.
* `Y.mapDegree Y'.gradeOf (p, q)` is the degree of the entry `(p, q)`, and `Y.constTerm` is the
  constant term along the entries of positive degree.
* `matrixToVec` and `vecToMatrix` pass between matrices and vectors indexed by `ι' × ι`.
* `Y.IsGraded L` says that the lattice `L` contains each graded part of each of its vectors.
* `Y.constTermAtStringMap Y' μ F x x'` is the constant term at `sh`, for the weights `Y'.gradeOf`,
  of the Weil translate of `F` by `(x, x')`, twisted by the characters `μ`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `Space.Splitting.conjTranspose_isotropicBasisFin`

 Let `D` be a Witt decomposition of the Hermitian space `V` into two dual isotropic subspaces,
with bases indexed by `p`, and an isometric image of `V'` orthogonal to both. The columns of `D.k`
are the basis of the first isotropic subspace, and `D.isotropicBasisFin` is this basis over the
finite adeles, written in lattice coordinates. Its adjoint is `D.kᴴ * V.J * V.xFin`. 

### `IsGraded.mulVec_mem_of_homogeneous`

 Let the bases of `V` and `V'` carry the integer grades `Y.gradeOf` and `Y'.gradeOf`, and let `W`
map a lattice `L` into a lattice `L'`, both graded. Then the part `T` of `W` of degree `e`, whose
entry `(p, q)` is that of `W` if the grade of `p` is that of `q` plus `e` and is `0` otherwise, also
maps `L` into `L'`. 

### `stringMap_eq_zero_of_gradeOf_ne`

 The shift `Y.stringMap Y'` from the string of basis vectors of `V` to that of `V'` is
homogeneous of degree `-1`: its entry `(p, q)` vanishes unless the grade of `p` is one less than
that of `q`. 

### `stringMapFin_stringProj`

 The finite part `Y.stringMapFin Y'` of the shift between the strings kills the block `X`, so it
does not change under composition with the projection `Y.stringProj` to the span `X^⊥` of the string
of `V`. 

### `stringProj_stringMapFin`

 The finite part `Y.stringMapFin Y'` of the shift between the strings takes its values in the
span `X'^⊥` of the string of `V'`, so they are fixed by the projection `Y'.stringProj` to it. 

### `hasDegreeGe_zero_ratCoordMatrixFin`

 Let `r` be a finite point of the Bessel group of the grading `Y` of `V`, that is, `r` fixes each
string vector of grade `≥ 0` up to vectors of higher grade. Then the matrix of `r` in rational
coordinates does not lower grades. 

### `hasDegreeGe_zero_mul_mul_sub`

 The Bessel group of a grading fixes each string vector of grade `≥ 0` up to vectors of higher
grade. If `W` agrees with `c` times the finite part of the shift up to a matrix that does not lower
grades, then so does `r' W r`, read in rational coordinates. Here `r ∈ Y.besselFin` and
`r' ∈ Y'.besselFin` are finite points of the Bessel groups of `Y` and `Y'`. 

### `zeroTermFin_finHeisenbergOp_stringMap_ne_zero`

 Let `D` be a Witt decomposition of `Hom (V, V')` with isotropic basis `D.k` indexed by the
entries of positive degree and with complement `V₀`. The zero term
`D.zeroTerm : 𝒮 (Hom (V, V')) → 𝒮 V₀` averages theta functions along `D.k`, and `zeroTermFin D F` is
the zero term of `v ⊗ F` for a fixed translate `v` of the Fock vacuum. Assume that the constant term
is the theta value on `V₀` of the zero term. Let `t` be a vector of the real Fock space of
`Hom (V, V')`, `f` a vector of the Weil representation `𝒮 (V.hom V')` and
`t ⊗ f = (V.hom V').integrated t f`. Translate `t ⊗ f` by adelic points `(x, x')` of `U(V) × U(V')`
in the Weil representation twisted by the characters `μ ι`, `μ ι'` of `[U(1)]`. If the constant term
of this translate at `sh`, `Y.constTermAtStringMap Y' μ (t ⊗ f) x x'`, is nonzero, then
`zeroTermFin D` does not kill the translate of `f` by the finite part of `(x, x')` and then by the
finite Heisenberg operator of `sh`. 

### `xFin_mulVec_finCoord_homAtPoint_sub`

 Let `M` be an adelic matrix and `l` a finite vector. Subtract `c g l`, where `g` is the finite
part of `(x, x')` acting on `Hom (V, V')`, from the finite coordinates of the point of
`Hom (V, V')` given by `M`. In rational coordinates the difference is the finite part of `M`
divided by the idele `α` of the Weil data, less `c` times the product of `V'.xFin x'.2`, the matrix
of `l` and the inverse of `V.xFin x.2`. 

### `exists_mapsTo_lattice_hasDegreeGe_sub_smul_stringMap`

 Let `t` be a vector of the real Fock space of `Hom (V, V')`, let `f ∈ 𝒮 (V.hom V')` and
`t ⊗ f = (V.hom V').integrated t f`. Translate `t ⊗ f` by adelic points `(x, x')` of `U(V) × U(V')`
in the Weil representation twisted by the characters `μ ι`, `μ ι'` of `[U(1)]`. Let the constant
term of this translate at `sh` be nonzero, and let `f` be fixed by the finite Heisenberg operators
of `b Ô ^ (ι' × ι)`. Then some matrix `W` maps the lattice `V.lattice x.2` into `V'.lattice x'.2`
and agrees with `b̄ / α` times the finite part of `sh` up to a matrix that does not lower grades.
Here `α` is the finite idele of `WeilData E` that makes `Ô` self-dual. 

### `smul_map_stringMapFin_latticePlus_le`

 The gradings `Y`, `Y'` split the bases of the Hermitian spaces `V`, `V'` (of signs `ε`, `ε'` at
the infinite places) into blocks `X`, `X'` of grade `0` and strings of `s` and `s - 1` vectors,
which span `X^⊥` and `X'^⊥`. The shift `sh = Y.stringMap Y'`, with finite part `Y.stringMapFin Y'`,
is the rational map `V → V'` that kills `X` and sends each string vector to a multiple of the one
with the same number; it lowers grades by one. The constant term at `sh` of a vector of the Weil
representation `𝒮 (V.hom V')` is the mean of its theta function, translated by `sh`, over the adelic
maps `V → V'` that raise grades, modulo rational ones.

Let `t` be a vector of the real Fock space of `Hom (V, V')`, whose signs are the products of those
of `ε` and `ε'`, let `f ∈ 𝒮 (V.hom V')` and `t ⊗ f = (V.hom V').integrated t f`. Translate `t ⊗ f`
by adelic points `(x, x')` of `U(V) × U(V')` in the Weil representation twisted by the characters
`μ ι`, `μ ι'` of `[U(1)]`. Let the constant term of this translate at `sh` be nonzero, and let `f`
be fixed by the finite Heisenberg operators of `b Ô ^ (ι' × ι)`. Let `r`, `r'` be finite points of
the Bessel groups (which fix each string vector of grade `≥ 0` up to vectors of higher grade) such
that the lattices of `r x.2` and `r' x'.2` are graded, that is, contain the part in each grade of
each of their vectors. Then `b̄ / α` times the finite part of `sh` maps the projection to `X^⊥` of
the lattice of `r x.2` into the intersection with `X'^⊥` of the lattice of `r' x'.2`. Here `α` is
the finite idele of `WeilData E` that makes `Ô` self-dual. 
