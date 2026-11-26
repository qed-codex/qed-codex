---
{
  "module": "src/New/Spanning/Unfolding/ReducedPoints.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eichler-type unipotent elements, colouring bounds and reduced points

This file gives explicit elements of the congruence subgroup `New.Filling.classUnipotent` of
`New.Shape.Form.besselU` by Eichler's formula along isotropic basis vectors `e_a`. It also proves
counting tools for the remaining terms: weighted sums are bounded by colouring, and the index of a
scaled lattice is computed.
Finally, every point at the infinite places is moved to a reduced point by exactly one coset of
unipotent elements, so that the indicator of the reduced points is a partition of unity in boxes.

## Main definitions and results

* `New.Filling.exists_mem_classUnipotent_eq_one_add_smul`: the general element, along several `e_a`
  at once.
* `New.Filling.exists_eichler_classUnipotent`: an element with one prescribed row.
* `New.Filling.tsum_le_of_encard_range_le`: a weighted sum is at most the number of colours times
  the bound for one colour; `New.Filling.tsum_le_relIndex_pow_mul`: colours are residue classes
  modulo a subgroup of finite index.
* `New.Filling.IsResidueDomain.exists_mul_mem_reducedPoints_iff_rightCoset`: exactly one coset of
  unipotent elements moves a point to a reduced point (`New.Filling.reducedPoints`).
* `New.Filling.IsResidueDomain.isBoxPartitionOfUnity`: the indicator of the reduced points has the
  properties `New.Filling.IsBoxPartitionOfUnity`.

Notions from other files:
* `New.Filling.classUnipotent c`: the group `𝖴_c(M)` of rational unipotent elements that lie in the
  principal congruence subgroup at the class `c`; `New.Filling.classUnipotent₀ c` is its subgroup
  fixing the frame `e_1, …, e_ϱ, z`, whose indices are given by `New.Shape.besselFrame`.
* `New.Filling.IsResidueDomain`: a measurable set `D` of representatives modulo `M 𝓞_E` of modulus
  at most `b ^ 26`; `New.Filling.reducedPoints D`: the points with all entries of their triangular
  matrix above the diagonal in `D`.
* `New.Filling.IsAdmissible`: the standing hypotheses, among them `|ϖ| ≤ b` and `1 ≤ |κ_v|` at
  every infinite place.

Here and below `M = S.M` is the level of the filling data `S`.



## Eichler-type elements of the unipotent congruence subgroups

Indices `𝔰.BesselIndex` come in three blocks: `.inl a` for `e_a`, a middle block, and
`.inr (.inr a)` for the dual vector `e*_a`. The middle block has the indices of the vector `z` and
those of the space `X₀`, given by `𝔰.indexX₀`. `S.ratGram` is the Gram matrix, `S.M` the level,
`New.Filling.finAdeleMatrix` maps a rational matrix to the finite adeles, and `S.classCoord c`
passes to coordinates in the basis `New.Filling.classBasis c` of the lattice of the class `c`.


### `conjTranspose_eichler_mul_mul`

 Eichler maps are isometries. Let `J` be hermitian, let the columns of `x` be isotropic and
orthogonal to each other and to those of `u`, let `s` be skew-hermitian, and let `g = star g` and
`τ + star τ = g`. Then `1 + g (x uᴴ J - (u + x (τ uᴴ J u - s)) xᴴ J)` preserves `J`. 

### `eichler_apply_eq_zero_of_level_le`

 Eichler maps along the columns `e_{p b}` are unitriangular. Let `J = S.ratGram` be the Gram
matrix over `E` of the filling-theorem data `S`. Let `x` have the columns `e_{p b}`. Let the columns
of `u` have coordinate `0` at the dual vector `e*_a` (index `eStar a`) whenever `a ≤ p b'` for some
`b'`. Then entry `(i, j)` of Eichler's matrix `x uᴴ J - (u + x (τ uᴴ J u - s)) xᴴ J` is `0` whenever
`BesselIndex.level j ≤ BesselIndex.level i`. 

### `isIntMatrix_ideleM_inv_smul_eichler`

 Eichler maps have level `M = S.M`. Let `J = S.ratGram` be the Gram matrix. Let the columns of
`x` and `u` lie in the lattice of the class `c`, let the matrix `s` and the number `τ` be integral,
and let the rational isometry `γ` have the matrix `1 + M (x uᴴ J - (u + x (τ uᴴ J u - s)) xᴴ J)`.
Then `M⁻¹ (γ' - 1)` has entries in `Ô`, where `γ' = S.translateByClassReps c c γ` is `γ` written in
the basis of the lattice and `S.ideleM` is `M` as a unit of the finite adeles. 

### `exists_mem_classUnipotent_eq_one_add_smul`

 A general element of `𝖴_c(M)`, given by Eichler's formula, when `E` contains a primitive 5040th
root of unity. Let `J = S.ratGram`. Let `x` have the columns `e_{p b}`. Let the columns of `u` lie
in the lattice of the class `c`. Let `u` also have coordinate `0` at the dual vector `e*_a` (index
`eStar a`) for all `b, b'` and every `a ≤ p b'`. Let `s` be integral and skew-hermitian. Then there
is `γ` in the group `𝖴_c(M)` of rational unipotent elements of level `M = S.M` at `c` with two
properties. (a) `γ` fixes the frame `e₁, …, e_ϱ, z`, that is, it lies in `S.classUnipotent₀ c`, if
the columns of `u` are orthogonal to the frame. (b) `γ` has the matrix
`1 + M (x uᴴ J - (u + x (τ uᴴ J u - s)) xᴴ J)` for some `τ : E`. 

### `exists_eichler_classUnipotent`

 An element of `𝖴_c(M) = S.classUnipotent c` with given rows at the `e_b`; here `M = S.M` is the
level and `E` contains a primitive 5040th root of unity. Let the row vector `l` vanish at `e_b` and
at the dual vector `e*_b` for all `b ≤ a`; these are exactly the indices `j` for which
`RealPlace.IsFreeEntry (a, j)` fails. Let `l` be integral on the lattice of the class `c`, spanned
over `Ô` by the columns of `classBasis c`, and let `s` be an integer of `E` with `star s = -s`. Then
some `γ` in `𝖴_c(M)` has, in `γ - 1` and outside the column `e*_a` (index `eStar a`), the row `M l`
at `e_a` and zero rows at the other `e_b`. If `l = 0`, the only entry of these rows that can be
nonzero is `M s` at `(e_a, e*_a)`. 

### `exists_integral_form_besselFrame`

 For each vector `f_b` of the frame `e_1, …, e_ϱ, z` there is a rational linear form that is
integral on the lattice of the class `c`, spanned over `Ô` by the columns of `classBasis c`, takes
the value `1` at `f_b`, and vanishes at the other basis vectors outside `X₀` (whose indices are the
range of `𝔰.indexX₀`). 

### `exists_classUnipotent_frameMatrix_eq`

 Let `E` contain a primitive 5040th root of unity. For `a < b` and `x` an integer of `E`, the
matrix `1 + Matrix.single a b (M x)` is `frameMatrix u` for some `u` in the congruence subgroup
`𝖴_c(M) = S.classUnipotent c` of the class `c`. Here `frameMatrix u` is the matrix of `u` on the
frame `e_1, …, e_ϱ, z`, and `M = S.M` is the level. 

### `exists_frameMatrix_classUnipotent_eq_mul`

 An element `u` of the congruence subgroup `𝖴_c(M) = S.classUnipotent c` acts on the frame
`e_1, …, e_ϱ, z` by a matrix `frameMatrix u` whose entries above the diagonal are multiples of the
level `M = S.M` by integers of `E`. 


## Colouring bounds and the index of scaled lattices

Here `New.submoduleIndex M M'` is the index of `M ⊓ M'` in `M'`, and `New.genIndex c` is `[Ô : c Ô]`
for `c ∈ Ô`.


### `tsum_le_of_encard_range_le`

 Colour the set `A` with at most `N` colours so that elements of one colour are `R`-related. If
every nonempty subset of `A` of pairwise `R`-related elements has total weight at most `x` for the
weight `w`, then `A` has total weight at most `N * x`. 

### `tsum_le_relIndex_pow_mul`

 Colouring by residue classes. Let `f a`, for `a ∈ A`, be a vector with entries in `K'`, and let
`K ⊓ K'` have finite index in `K'`. If every nonempty subset of `A` on which `f` is constant modulo
`K` has total weight at most `x`, then `A` has total weight at most `[K' : K ⊓ K'] ^ card ι * x`. 

### `submoduleIndex_smul_intVectors`

 The index of `c Ô^ι` in the lattice `intVectors (Ô E) ι = Ô^ι` of integral vectors of finite
adeles is `[Ô : c Ô] ^ card ι` (`genIndex c = [Ô : c Ô]`), for a unit `c` of the finite adeles that
lies in `Ô`. 

### `submoduleIndex_smul_ne_zero`

 For a unit `c` of the finite adeles that lies in `Ô`, the index of `c Ô^ι` in `Ô^ι` is not
zero. 


## Reduced points

The elements of `S.classUnipotent c` that move a given point to a reduced one
(`New.Filling.reducedPoints`) form exactly one coset of `S.classUnipotent₀ c`.


### `existsUnique_mul_unitriangular_mem`

 Reduction of unitriangular matrices. Let `L` be an additive submonoid of the ring `R`, and let
every element of `R` have exactly one translate by `L` in `D`. Let `Γ` be a group of upper
unitriangular matrices whose entries above the diagonal lie in `L` and which contains the elementary
matrices `1 + single a b l` with `a < b` and `l` in `L`. Then for every unitriangular `x` exactly
one `γ` in `Γ` puts all entries of `x γ` above the diagonal in `D`. 

### `ratTriangle_eq_sum`

 Let `u` in the rational unitary group `S.G E` of the filling-theorem data `S` lie in `besselU`,
the block upper unitriangular isometries. `S.ratTriangle y a b v` is entry `(a, b)` of the
triangular matrix `gramSchmidtMatrix (y v)`, read in the rational frame. It equals the sum over `l`
of `S.ratTriangle (S.ratToInf u * y) a l v * Φ v (frameMatrix u l b)`. Here `frameMatrix u` is the
submatrix of `u` on the frame (e₁, …, e_ϱ, z), and `Φ v` is the chosen embedding at `v`. 

### `IsResidueDomain.exists_mul_mem_reducedPoints_iff_rightCoset`

 Let `S` be filling data over `E`, where `E` contains a primitive 5040th root of unity, and let
`D` be a set of representatives modulo `S.M 𝓞_E` as in `New.Filling.IsResidueDomain`. For each class
`c` in `S.Classes` and each point `y`, the `u` in `S.classUnipotent c` with `S.ratToInf u * y`
reduced for `D` form exactly one right coset of `S.classUnipotent₀ c`. 

### `IsResidueDomain.isBoxPartitionOfUnity`

 Let `S` satisfy the standing hypotheses `New.Filling.IsAdmissible`, let `E` contain a primitive
5040th root of unity, and let `D` be a set of representatives modulo `S.M 𝓞_E` as in
`New.Filling.IsResidueDomain`. For every class `c`, the indicator `ω` of the points reduced for `D`
is a partition of unity in boxes. 
