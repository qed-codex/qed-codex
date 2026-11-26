---
{
  "module": "src/New/Spanning/RemainingTerms/Box.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Box.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Box.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The box

Let `S : Filling E 𝔰` be admissible data for a CM field `E` and a shape `𝔰`, with `M = S.M` the
level and `b = S.b`. Consider the tuples of complex numbers, one for each infinite place, modulo
`M 𝓞_E`, and fix a measurable set `D` of representatives, each coordinate of each point of `D`
having modulus at most `b ^ 26`.

An archimedean point `y` is reduced if the entries above the diagonal of its triangular matrix
`S.ratTriangle y` lie in `D`. It is boxed if it is reduced and lies in the cut at every place `v`,
that is, `besselLength (y v) ≤ b ^ (6 n + 2)`, where `n = 𝔰.n = 𝔰.ϱ + 1`.

Notions from other files:
* `frameVector z a`: for `z` in `𝔰.G₁`, the image of the `a`-th frame vector under `z⁻¹`;
  `orthoFrame z` is the result of the Gram–Schmidt process on these vectors.
* `gramSchmidtMatrix z`: the unitriangular matrix of the coefficients of `frameVector z` in
  `orthoFrame z`; `S.ratTriangle` reads it in the rational frame.
* `besselLength z`: the infimum of `‖s * z‖ + 1` over `s` in the Bessel subgroup.
* `frameBox r`: the points at which all frame vectors have length at most `r`.

## Main definitions and results

* `New.Filling.exists_isResidueDomain`: such a set `D` exists.
* `New.Filling.boxedPoints`: the boxed points.
* `New.Filling.mul_mem_boxedPoints_iff`: invariance under the unipotent elements fixing the frame.
* `New.Filling.mem_frameBox_of_mem_boxedPoints`: at a boxed point the frame vectors have length at
  most `b ^ (37 n)`.


### `_root_.New.exists_measurableSet_existsUnique_add_mem`

 Let `V` be an abelian group and a standard Borel space with measurable translations. Let `L` be
a countable subgroup and `B` a measurable set that meets every coset of `L` in a finite nonempty
set. Then `B` contains a measurable set of representatives of the cosets. 

### `encard_le_of_isIntegral_norm_le`

 Few integral vectors have bounded conjugates. If `f` maps `A` injectively to vectors in `E^ι`
whose entries are algebraic integers of absolute value at most `r` under the embedding `Φ v` of
every infinite place `v` (chosen by the instance `PlaceEmbedding E`), then `A` has at most
`(1 + 2 r) ^ (2 |ι| m)` elements, where `m = Core.numInfPlaces E` is the number of infinite
places. 

### `mem_levelMultiples`

 A tuple of complex numbers, one for each infinite place, lies in `S.levelMultiples`, the
multiples of the level `M = S.M`, if and only if it consists of the images of `M x` for an integer
`x` of `E`. 

### `finite_setOf_levelMultiples_add_le`

 Let `S : Filling E 𝔰`, the data of the filling theorem, satisfy the standing hypotheses
`S.IsAdmissible`. For `r ≥ 0` and a tuple `w` over the infinite places, only finitely many `l` in
`S.levelMultiples` make all coordinates of `l + w` have modulus at most `r`. Here `S.levelMultiples`
is the set of tuples `M x`, where `x` is an integer of `E` and `M = S.M` is the level. 

### `exists_isResidueDomain`

 Let `S : Filling E 𝔰`, the data of the filling theorem over `E`, satisfy the standing hypotheses
`S.IsAdmissible`, which bound the data by powers of `b = S.b`. Then there is a set `D` with
`S.IsResidueDomain D`: a measurable set of representatives for the tuples of complex numbers, one
for each infinite place, modulo `M 𝓞_E`. 

### `mul_mem_reducedPoints_iff`

 For any set `D` of tuples over the infinite places, let `S.reducedPoints D` be the set of points
whose matrix has all its entries above the diagonal in `D`. This set is left invariant by the fixer
`besselFixer` of the frame, the elements fixing each frame vector: if every `s v` lies in
`besselFixer`, then `s * y` is in `S.reducedPoints D` if and only if `y` is. 

### `boxedPoints`

 The boxed points: the archimedean points `y` that are reduced for a chosen set satisfying
`New.Filling.IsResidueDomain` (one exists for admissible data) and lie in the cut at every infinite
place `v`, that is, `besselLength (y v) ≤ S.b ^ (6 * 𝔰.n + 2)`. 

### `inCut_of_mem_boxedPoints`

 A boxed point `y` lies in the cut at every infinite place `v`, that is,
`besselLength (y v) ≤ S.b ^ (6 * 𝔰.n + 2)`. 

### `mem_boxedPoints_of_reducedIndicator_ne_zero`

 If `S.reducedIndicator`, the indicator of the reduced points for the chosen set of
representatives, is nonzero at `y` and `y` lies in the cut at every infinite place
(`besselLength (y v) ≤ S.b ^ (6 * 𝔰.n + 2)`), then `y` is boxed. 

### `mul_mem_boxedPoints_iff`

 The group `New.Shape.Form.besselU0` consists of the elements of the Bessel unipotent group
`besselU` that fix each frame vector. If every component of `u` lies in `besselU0`, then `u * y` is
boxed if and only if `y` is. 

### `ratTriangle_eq_one_apply_of_le`

 On and below the diagonal, at every infinite place, the matrix `S.ratTriangle y` (the triangular
matrix of the frame at `y`, read in the rational frame) agrees with the identity matrix. 

### `IsResidueDomain.measurableSet_reducedPoints`

 If `D` is a set of representatives modulo `S.M 𝓞_E` as in `New.Filling.IsResidueDomain`, in
particular measurable, then the set of points whose triangular matrix has its entries above the
diagonal in `D` is measurable. 

### `norm_basisScale_div_le_one`

 At an infinite place `v` the scale `S.basisScale v` of the normalised basis is
`κ_v ^ (ϱ - a) / √N` at the `a`-th frame vector `𝔰.besselFrame a`. Here `ϱ = 𝔰.ϱ` is the number of
hyperbolic planes, `N = S.N` is the prime of the data, and `κ_v = S.realM v` is the real number
`S.M * Φ v S.deltaE / (2 π i)`. For admissible `S` one has `1 ≤ |κ_v|`, so the scale does not grow
along the frame: for `a ≤ b` the scale at `b` divided by the scale at `a` has modulus at most
one. 

### `IsResidueDomain.norm_gramSchmidtMatrix_le`

 Let `S` be admissible and `D` a measurable set of representatives modulo `S.M 𝓞_E` whose points
have modulus at most `S.b ^ 26` at every place. If `y` is reduced for `D`, that is, the entries
above the diagonal of `S.ratTriangle y` lie in `D`, then all entries of `gramSchmidtMatrix (y v)`
have modulus at most `S.b ^ 26`. 

### `IsResidueDomain.mem_frameBox`

 Let `S` be admissible, let `D` be a measurable set of representatives modulo `S.M 𝓞_E`, the
points of `D` having modulus at most `S.b ^ 26` at every place, and let `y` be reduced for `D`: the
entries of the triangular matrix `S.ratTriangle y` above the diagonal lie in `D`. Then at every
infinite place `v` the point `y v` is in the `frameBox` of radius
`S.b ^ 27 * besselLength (y v)`. 

### `mem_frameBox_of_mem_boxedPoints`

 Let `S` be admissible, that is, satisfy the standing hypotheses `New.Filling.IsAdmissible`,
`n = 𝔰.n`, and let `y` be boxed: the entries above the diagonal of `S.ratTriangle y` lie in the set
of representatives modulo `S.M 𝓞_E` chosen in `S.boxedPoints`, and
`besselLength (y v) ≤ S.b ^ (6 n + 2)` at every infinite place `v`, where `besselLength g` is the
infimum of `‖s * g‖ + 1` over `s` in the Bessel subgroup `besselS` of `𝔰.G₁`. Then `y v` lies in the
`frameBox` of radius `S.frameBoxRadius = S.b ^ (37 n)`. 

### `measurableSet_boxedPoints`

 For admissible data the set of boxed points is measurable. 
