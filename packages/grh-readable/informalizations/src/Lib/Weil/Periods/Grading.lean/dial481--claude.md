---
{
  "module": "src/Lib/Weil/Periods/Grading.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Graded hermitian spaces X ⊕ J_s, Bessel subgroups, the map T, and c_λ in a frame

A hermitian space `V = X ⊕ J_s` is presented (`New.Grading`) as a space `X` with an orthonormal
basis plus a string of `s` vectors with antidiagonal Gram matrix, whose entries are 1 except `-N`
for the middle vector (`N = N̄ ≠ 0`). The weight, also called grade, is `0` on `X` and `s - 1 - 2i`
on the `i`-th string vector. The grading defines three objects in `U(V)(𝔸)`: the unipotent subgroup
`New.Grading.unipotent`, which raises weights; the embedding `New.Grading.inclX` of `U(X)`; and the
Bessel subgroup `New.Grading.besselGroup`. These are described by matrix entries in rational
coordinates. For a second graded space `V' = X' ⊕ J_(s-1)` the map `T : V → V'`
(`New.Grading.stringMap`) is studied, and separately the matrix coefficient c_λ of a discrete series
is transported to `U(J)` through a frame.

## Main definitions and results

* `New.Grading`: a presentation of `V` in this form, with a constant `genericConst` for the generic
  character.
* `New.Grading.stringMap`: the map between two graded spaces that kills `X` and sends each string
  vector to a multiple of the string vector with the same number (to `0` if there is none). It has
  degree at least `-1` when `s' = s - 1`. `New.Grading.AgreesWithStringMap` is partial agreement
  with it.
* `New.Grading.besselProj`, `New.Grading.exists_besselGroup_proj`,
  `New.Grading.exists_unipotent_mul_inclX`: taking the X-block is a homomorphism from
  `New.Grading.besselGroup` onto U(X) with kernel `New.Grading.unipotent`, split by
  `New.Grading.inclX`.
* `New.isIdempotentKernel_dsCoeffInFrame`: for λ with a large gap, the formal degree times
  `New.HCParam.dsCoeffInFrame l` is an idempotent kernel on `U J` (Schur orthogonality).
* `New.Grading.hasDegreeGe_zero_mul_stringMap_mul_sub`: the Bessel subgroups
  `New.Grading.besselGroup` of both spaces fix `T` modulo degree at least `0`.
* `New.Grading.formAdjoint_stringMap_mul_stringMap_eq_shift`,
  `New.Grading.stringMap_mul_formAdjoint_stringMap_eq_shift`: `T† T` is the shift
  `New.Grading.shift` of `V`, and `T T†` is that of `V'` when the two constants agree;
  `New.Grading.formAdjoint_stringMap_mul_stringMap` states both.

Notions from other files:
* `New.Space`: a hermitian space with a point: a matrix J over E and an x in GL_n(𝔸) such that xᴴJx
  is diag(ε) at the infinite places and 1 at the finite places. `V.Γ` is the group of g whose matrix
  in rational coordinates has entries in E; `New.stdSpace E X` is the definite space on X with point
  1.
* `New.𝔸`: the adele ring of the CM field E, as the product of ℂ^f (one copy of ℂ for each infinite
  place) and the finite adeles.
* `New.G`: the adelic unitary group G = G_∞ × G_f of the form diag(ε) at the infinite places and 1
  at the finite places; `g.adeleMatrix` is the adelic matrix of g.
* `New.IsHermitianInvolution J`: the complex matrix J satisfies J* = J and J² = 1.
* `New.HCParam.HasLargeGap`, `New.HCParam.formalDegree`: for l = 2λ and signs ε on n indices, the
  condition that λ has gap 500n³+A for a natural number A, and the reciprocal of the integral of
  |c_λ|² over U(diag ε) for the compact dual measure.

## Relation to the literature

Known; see `Lib.Weil.Periods.Unfolding` and `Lib.DiscreteSeries.CuspKernel` for sources.

Part of a known construction: adelic points of unitary groups in rational coordinates. See
`Lib.Adelic.Unitary.WeakApproximation`.



## Gradings X ⊕ J_s of a hermitian space and their subgroups

All matrix conditions are in rational coordinates (`New.Space.ratCoordMatrix`).


### `gradedBlocks`

 The block diagonal matrix with block A from X to X' and block B from string to string,
reindexed along e and e'. 

### `gradedGram`

 The Gram matrix of X plus a string of length s: identity on X; string vectors a, b with
a + b = s − 1 pair to 1, or to −N if a = b. 

### `Space.ratCoordMatrix`

 For a space (J, x) and g in G, the adelic matrix x g x⁻¹ of g in rational coordinates. This is
the matrix of an element of U(J)(𝔸), and it is multiplicative in g. 

### `Grading`

 A presentation of `V` as `X ⊕ J_s`: an indexing of the basis by `X` and a string of `s` vectors
for which the Gram matrix is `New.gradedGram`, with `N = N̄ ≠ 0`. It also carries a constant
`c = genericConst`, with `c = c̄ ≠ 0` in `E`, for the generic character. Certain multiples of the
string vectors, defined in `Lib.Weil.Periods.StringPowers`, are the vectors `𝔢 ^ i`, which pair to
`-N` for opposite grades. 

### `Grading.indexEquiv`

 The splitting of the basis of `V` into `X`, of grade 0, and a string of `s` vectors. 

### `Grading.gram_eq`

 The Gram matrix is 1 on `X`; vector i of the string pairs only with vector s - 1 - i, to 1,
  but to -N if it is the middle vector. 

### `Grading.N_ne_zero_and_star_eq`

 `N` is nonzero and fixed by complex conjugation. 

### `Grading.genericConst`

 The constant of the generic character, nonzero and fixed by complex conjugation. 

### `gradeOf`

 The grade of a basis index of X plus a string of length s: 0 on X, and s − 1 − 2i on the
i-th string vector. 

### `gradeOf_inr`

 For a grading `Y` of `V`, which indexes the basis of `V` by `X` together with a string of `s`
vectors, the `a`-th string vector (the basis index `Y.indexEquiv (Sum.inr a)`) has grade
`s - 1 - 2 * a`. 

### `unipotent`

 The unipotent subgroup of the g in G whose matrix in rational coordinates, minus 1, strictly
raises grades. 

### `inclX`

 The homomorphism from the adelic unitary group of the standard definite space on X to that
of V, acting on X and fixing the string vectors. 

### `ratCoordMatrix_inclX`

 In rational coordinates, `Y.inclX h` is block diagonal: the matrix of `h` on `X` and the
identity on the string. 

### `besselGroup`

 The Bessel (Fourier–Jacobi) subgroup: the `g` whose matrix in rational coordinates sends each
string vector of weight `≥ 0` to itself plus a combination of string vectors of higher weight.
In the column `k` of such a vector, the entries in the rows `i` of weight at most that of `k` are
those of the identity matrix. 

### `mem_besselGroup`

 An element `g` lies in the Bessel subgroup if and only if its matrix in rational coordinates
agrees with the identity at every entry (i, k) with k a string index of grade ≥ 0 and grade(i) at
most grade(k). 

### `ratBessel`

 The rational points of U(V) that lie in the Bessel (Fourier–Jacobi) subgroup of the grading
Y. 


## Degrees of matrices and entrywise membership in the subgroups

* `New.HasDegreeGe`: a matrix raises weights by at least `d`; degrees add (`New.HasDegreeGe.mul`).


 ### Degrees and rational coordinates 

### `HasDegreeGe`

 The matrix x raises weights by at least d: x_{ba} = 0 whenever w'(b) < w(a) + d. 

### `HasDegreeGe.mul`

 Degree bounds add: if `x` has degree at least `d` and `y` has degree at least `d'`, then
`x * y` has degree at least `e` for every `e ≤ d + d'`. 

### `Space.mem_Gamma_iff_ratCoordMatrix`

 An adelic point lies in the group `V.Γ` of rational points if and only if all entries of its
matrix in rational coordinates come from `E` under the diagonal embedding `New.toAdele`. 

 ### The unipotent and Bessel subgroups 

### `mem_unipotent`

 For a grading `Y` presenting the hermitian space `V` over the CM field `E` as `X ⊕ J_s`, an
element `g` of the adelic unitary group of `V` lies in `Y.unipotent` iff its matrix in rational
coordinates minus 1 raises grades by at least 1. That is, its (b, a) entry vanishes whenever
`Y.gradeOf b < Y.gradeOf a + 1`, where the grade is 0 on `X` and s − 1 − 2i on the i-th string
vector. 

### `hasDegreeGe_two_of_odd`

 For a string of odd length all grades are even, so an element of the unipotent group, whose
matrix minus 1 raises grades, raises them by at least 2. 

### `mem_besselGroup_iff_sub_one`

 Membership in the Bessel subgroup, by the vanishing of entries of `g - 1`. The vectors of `X`
have weight `0`, so the first condition selects the string vectors of weight `≥ 0`. 

### `inclX_mem_besselGroup`

 Let `Y` present the hermitian space `V` over the CM field `E` as `X ⊕ J_s`. For every element
`a` of the adelic unitary group of the standard definite space on `X`, its image under `Y.inclX`
(acting on `X` and fixing the string vectors) lies in the Bessel (Fourier–Jacobi) subgroup
`Y.besselGroup` of the adelic unitary group of `V`. 

### `unipotent_le_besselGroup`

 For a grading `Y` presenting the hermitian space `V` over the CM field `E` as `X ⊕ J_s`, the
unipotent subgroup `Y.unipotent` is contained in the Bessel (Fourier–Jacobi) subgroup
`Y.besselGroup`. Here `Y.unipotent` consists of the `g` whose matrix in rational coordinates minus 1
strictly raises grades. 

### `isClosed_besselGroup`

 The Bessel group `Y.besselGroup` is closed. 

### `inclX_mem_ratBessel`

 The embedding `Y.inclX` sends the rational points of the standard definite space on `X` to
rational points in the Bessel subgroup. 


## The map T, the shift and the string reversal

* `New.Grading.stringReversal`: the involution of the indices that fixes `X` and reverses the
  string.


### `stringReversal`

 The involution of the basis indices of V that fixes the indices of X and exchanges the
string vectors i and s − 1 − i. 

### `stringMap`

 The rational map `V → V'` that kills `X` and sends the string vector `a` to `t a` times the
string vector of `V'` with the same number (to `0` if there is none). For `s` odd, `t a` is
`1`, `-N c`, `c` when the weight of `a` is positive, zero, negative. For `s` even, `t a` is
`c`, `1` when the weight is positive, negative. It has degree at least `-1` when `s' = s - 1`.
For `s' = s - 1` and equal constants `c` it sends each `𝔢 ^ i` (`New.Grading.stringPower`) to
`𝔢 ^ i`, which is `0` in `V'` for `i = s - 1` (`New.Grading.stringMap_mulVec_stringPower`). 

### `AgreesWithStringMap`

 The condition that the matrix w agrees with T (`New.Grading.stringMap`) at all entries (b, a)
where a has positive grade and b has grade below that of a. 

### `mapDegree`

 For weights d on the target basis and an index pair (b, a), the integer d(b) minus the grade
of a in Y: the amount by which the entry (b, a) of a map raises grades. 

### `nonnegMaps`

 For weights d on the target indices, the additive group of rational matrices
(`ratMatrices E ι' ι`, adelic matrices with entries from E) whose entry (b, a) vanishes whenever
d(b) is less than the grade of a. 

### `shift`

 Multiplication by `𝔢`: the rational map `V → V` that kills `X` and the last string vector and
sends the string vector `b` to a multiple of the vector `b + 1`. The factor is `-N c` if `b` has
weight `0`, `-N c²` if `b` has weight `1`, and `c` otherwise. It sends `𝔢 ^ i` to `𝔢 ^ (i + 1)`
(`New.Grading.shift_mulVec_stringPower`). 


## Adjoints in graded coordinates and the projection to U(X)

Matrix computations in a space presented as X plus a string (`New.Grading`).

* `New.Grading.formAdjoint_apply`: the entries of the adjoint `New.Space.formAdjoint` of an adelic
  matrix.


### `Space.formAdjoint`

 The adjoint J⁻¹yᴴJ' of an adelic map y from the space with Gram matrix J to the space with
Gram matrix J'. 

### `Space.formAdjoint_ratCoordMatrix_mul`

 The adjoint of `g y` is the adjoint of `y` times `g⁻¹`, because `g` preserves the form. 

### `map_gradedGram_mul_apply`

 For the graded Gram matrix `Gr` over `E` with any constant `M`, a ring homomorphism
`f : E →+* R` and a matrix `A` over `R`, the entry (i, p) of f(Gr) times `A` is
f(Gr(i, σi)) · A(σi, p), where σ is the dual index `New.Grading.stringReversal`. 

### `vecMul_J_apply`

 The entry a of the row vector y J is y(σa) J(σa, a), with σ the dual index
`New.Grading.stringReversal`. 

### `formAdjoint_apply`

 The entry (a, b) of the adjoint J⁻¹ yᴴ J' is the conjugate of the entry of y at the dual indices
(σ'b, σa), times the entries J⁻¹(a, σa) and J'(σ'b, b). Here σ and σ' are the dual indices
`New.Grading.stringReversal` of `Y` and `Y'`. Both presentations have the same N. 

 ### The Bessel subgroup and its projection to U(X) 

### `mem_besselGroup_iff`

 g lies in `New.Grading.besselGroup` if and only if its matrix agrees with the identity at every
entry (i, k) such that weight(i) ≤ weight(k) and i or k is an index of the string. 

### `hasDegreeGe_zero_of_mem_besselGroup`

 The matrix of an element of `New.Grading.besselGroup` in rational coordinates does not lower
weights: its entry (i, k) is zero when weight(i) < weight(k). 

### `submatrix_inl_map_J`

 The X-block of the Gram matrix of `V` over the adeles is the standard form of the definite
space on X. 

### `submatrix_inl_ratCoordMatrix_unitary`

 For g in `New.Grading.besselGroup`, the X-block B of its matrix in rational coordinates
satisfies Bᴴ S B = S, where S is the standard form of the definite space on X. 

### `submatrix_inl_ratCoordMatrix_mul`

 On `New.Grading.besselGroup`, the X-block of the matrix in rational coordinates is
multiplicative. 

### `besselProj`

 The projection from `New.Grading.besselGroup` to the adelic unitary group of the standard
definite space on X: it takes an element to the X-block of its matrix in rational coordinates. 

### `adeleMatrix_besselProj`

 The matrix of `Y.besselProj r` is the X-block of the matrix of `r` in rational coordinates. 

### `mem_unipotent_iff_besselProj_eq_one`

 An element of the Bessel group lies in the unipotent group if and only if its projection to U(X)
is trivial. 

### `mul_inv_inclX_besselProj_mem_unipotent`

 An element `r` of the Bessel group agrees with the embedding of its projection to U(X) up to a
unipotent factor on the left. 

### `exists_besselGroup_proj`

 There is a continuous homomorphism p from `New.Grading.besselGroup` to the adelic unitary group
of the standard definite space on X such that (a) r · `New.Grading.inclX`(p r)⁻¹ lies in
`New.Grading.unipotent`, (b) p ∘ `New.Grading.inclX` is the identity, (c) the kernel of p is
`New.Grading.unipotent`, (d) p maps rational points to rational points. The projection
`New.Grading.besselProj` is such a p. 

### `exists_unipotent_mul_inclX`

 Every element of the Bessel group `New.Grading.besselGroup` is a product na with n in the
unipotent group and a in U(X). 


## Rational coordinates of finite adelic points; finite Bessel subgroups

Points of the adelic group of a space `V = (J, x)` are matrices preserving
the standard form of signs `ε`;
`V.ratCoordMatrix g = x g x⁻¹` is the matrix in rational coordinates, and `New.Space.xFin` the
finite part of `x`.

* `New.Grading.besselFin`, `New.Grading.inclXFin`: for `V` presented as `X` plus a string
  (`New.Grading`), the finite parts of the Bessel subgroup `New.Grading.besselGroup` and of the
  embedding `New.Grading.inclX` of `U(X)`.


### `ratCoordMatrixFin`

 For g in G_f, the matrix x_f g x_f⁻¹ of g in rational coordinates. 

### `ratCoordMatrixFin_snd`

 The finite part of the matrix of g in rational coordinates is the matrix of the finite component
of g in rational coordinates. 

### `ratCoordMatrix_inr`

 For g in G_f, the matrix of (1, g) in rational coordinates is the identity at the infinite
places and `V.ratCoordMatrixFin g` at the finite places. 

### `gram_xFin`

 The finite part x_f of the point of a space (J, x) satisfies x_fᴴ J x_f = 1 over the finite
adeles, to which J is mapped entrywise. This is the finite part of `V.gram_point`. 

### `besselFin`

 The finite points `g` such that `(1, g)` lies in the Bessel subgroup `Y.besselGroup`. 

### `inclXFin`

 The embedding of the finite points of `U(X)` in those of `U(V)`: the finite component of
`Y.inclX (1, h)`. 

### `ratCoordMatrixFin_inclXFin`

 In rational coordinates the matrix of `inclXFin h` is `h` on `X` and the identity on the
string. 

### `instance : IsClosed (Y.besselFin : Set (Gf E ι))`

 The finite Bessel subgroup is closed. 


## c_λ on U(J) through a frame

The matrix coefficient c_λ = `New.HCParam.dsCoeff` (`l = 2λ`) of a discrete series is defined on
the unitary group `New.USign ε` of the diagonal form with signs `ε`. Let `J` be a hermitian
involution and `p` a frame (`New.DiscreteSeries.SignFrame J ε`), that is, an invertible matrix with
`pᴴ J p = diag ε`.


### `DiscreteSeries.SignFrame`

 A frame for the complex matrix J with signs ε: an invertible matrix p (the field `matrix`) with
pᴴJp = diag(ε). 

### `DiscreteSeries.SignFrame.matrix`

 The invertible matrix p of the frame. 

### `DiscreteSeries.SignFrame.gram_eq`

 The matrix p satisfies pᴴJp = diag(ε). 

### `DiscreteSeries.frameEquiv`

 The isomorphism of topological groups U(J) → U(diag ε), g ↦ p⁻¹gp, for the frame p of
`New.DiscreteSeries.SignFrame J ε`, so that pᴴJp = diag(ε). 

### `HCParam.dsCoeffInFrame`

 The function g ↦ c_λ(p⁻¹gp) on U(J), for l = 2λ and the frame p of
`New.DiscreteSeries.SignFrame J ε`, so that pᴴJp = diag(ε). 

### `DiscreteSeries.measurePreserving_frameEquiv`

 The isomorphism g ↦ P⁻¹gP from U(J) to U(diag ε), for the matrix P of a frame, carries the
measure `New.haarU` of U(J), which is the `volume` there, to that of U(diag ε). 

### `DiscreteSeries.integral_comp_frameEquiv`

 The integral over U(J) of f(p⁻¹gp), for the frame p, is the integral of f over U(diag ε). 

### `isIdempotentKernel_dsCoeffInFrame`

 If l = 2λ is a parameter with gap 500n³+A, J is a hermitian involution and pᴴJp = diag(ε), the
function deg_λ c_λ (formal degree times coefficient), carried to U(J) by the frame p, is an
idempotent kernel on U(J): continuous, integrable, self-adjoint, nonzero at 1 and reproducing
under convolution. 

 ## Degree of T, invariance under the Bessel subgroups, and T†T 

### `hasDegreeGe_neg_one_stringMap`

 For s' = s − 1, the map T = `New.Grading.stringMap` lowers weights by at most 1. 

### `hasDegreeGe_zero_mul_stringMap_mul_sub`

 Let s' = s − 1. For g in `New.Grading.besselGroup` of Y and δ in that of Y', the map δTg − T has
degree at least 0, where T = `New.Grading.stringMap` and δ, g are read in rational coordinates. 

### `formAdjoint_stringMap`

 Let `s' = s - 1` and `T = Y.stringMap Y'`. The adjoint `T†` of `T` for the two forms kills `X'`
and sends the string vector `b` of `Y'` to a multiple of the string vector `a = b + 1` of `Y`. For
`s` odd the factor is `c` or `1` when the weight of `a` is nonnegative or negative. For `s` even
it is `1`, `-N c`, `c` when the weight of `a` is positive, `-1`, less than `-1`. 

### `formAdjoint_stringMap_mul_stringMap_eq_shift`

 Let `T = Y.stringMap Y'`, where `Y'` has a string of length `s - 1`. `T` is the rational map
`V → V'` that kills `X` and sends each string vector of `Y` to a multiple of the one of `Y'` with
the same number (`0` if none). Let `T†` be its adjoint for the two forms. Then `T† T` is `Y.shift`,
the map that kills `X` and the last string vector and moves each other string vector of `Y` to a
multiple of the next one. 

### `stringMap_mul_formAdjoint_stringMap_eq_shift`

 Let `s' = s - 1`, `T = Y.stringMap Y'` and let `T†` be its adjoint for the two forms. If `Y` and
`Y'` have the same constant of the generic character, `Y'.genericConst = Y.genericConst`, then
`T T†` is the shift `Y'.shift` of `Y'`. 

### `formAdjoint_stringMap_mul_stringMap`

 Let `Y` present `V` as `X ⊕ J_s` and `Y'` present `V'` as `X' ⊕ J_{s-1}` with the same `N`, each
carrying a constant `c = c̄ ≠ 0`. Let `T = Y.stringMap Y'` be the map `V → V'` that kills `X` and
sends the string vector `a` to `t a` times the string vector of `Y'` with the same number (to `0` if
there is none), where `t a` depends on the parity of `s`, the weight of `a`, `c` and `N`, and let
`T†` be its adjoint for the two hermitian forms. (a) `T† T` is `Y.shift`, the map that kills `X` and
the last string vector and sends each string vector `b` to `-N c`, `-N c²` or `c` times the vector
`b + 1`, according as `b` has weight `0`, `1` or another weight; (b) if
`Y'.genericConst = Y.genericConst`, then `T T†` is the shift `Y'.shift` of `Y'`. 
