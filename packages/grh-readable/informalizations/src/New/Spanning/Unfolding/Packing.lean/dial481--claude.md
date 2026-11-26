---
{
  "module": "src/New/Spanning/Unfolding/Packing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Class cutoffs and counting frames in boxes

The translates of the cutoff `S.classCutoff c` of a class `c` are shown to add up to one, and
weights bounded by cutoffs are shown to add up to at most a bound for the number of frames in a box.

## Main definitions and results

* `New.Filling.frameImage_eq_frameImage_one_of_close`: a term that moves the frame vectors of a
  point in a box very little fixes the frame.
* `New.Filling.encard_image_frameImage_le`: terms `γ` with `γ⁻¹ y` in a box have few images of the
  frame, since the frame vectors of the points `γ⁻¹ y` lie in a ball and are separated.
* `New.Filling.tsum_le_of_le_classCutoff_mul`: weights bounded by cutoffs add up to at most that
  bound for the number of frames.

Notions from other files:
* `New.frameImage`, `New.frameVector`: the image `γ f` of the frame `f = (e₁, …, e_ϱ, z)` under a
  matrix `γ`, and the vector `y⁻¹ f_a` in Euclidean space.
* `New.frameBox`, `New.besselLength`: the points whose frame vectors have norm at most `ρ`, and the
  infimum of `‖s y‖ + 1` (operator norm) over `s` in the Bessel subgroup.
* `New.Filling.frameBoxRadius`, `New.Filling.basisScale`: the number `S.b ^ (37 n)`, and the scales
  of the normalised basis at an infinite place.
* `New.Filling.classUnipotent`, `New.Filling.classCutoff`: the congruence group of rational
  unipotent elements attached to a class `c`, and a cutoff for its subgroup fixing the frame times
  the indicator of the reduced points.
* `New.Filling.termsOver`: the rational `γ` with `h_c⁻¹ γ h_c'` integral and of reduction `s`, where
  `h_c` is the representative `New.Filling.classRep` of the class `c`.
* `New.Filling.IsAdmissible`: the standing hypotheses, among them the size inequalities between
  `S.b`, `S.realM v` and `S.N`.


### `frameVector_sub_eq_sum`

 Let `γ`, `γ'` be rational elements of the unitary group whose images `γ f`, `γ' f` of the frame
`f = (e₁, …, e_ϱ, z)` differ only in the coordinates along the `e_a`. At an infinite place `v`, the
`b`-th frame vectors of `γ⁻¹ y` and `γ'⁻¹ y` then differ by a combination of the vectors `y⁻¹ e_a`.
The coefficient of `y⁻¹ e_a` is the difference of the coordinates along `e_a`, embedded by `Φ v` and
multiplied by the ratio of the scales of `f_b` and `e_a` in the normalised basis at `v`
(`S.basisScale v`). 

### `exists_gramSchmidtMatrix_le`

 Reduction of frames: for every class `c` and every point `y` at the infinite places, some `u` in
the congruence group `S.classUnipotent c` of rational unipotent elements makes all entries of
`gramSchmidtMatrix` of the components of `u y` at most `S.b ^ 26` in absolute value. Here
`gramSchmidtMatrix x` is the upper unitriangular matrix expressing the frame vectors
`x⁻¹ e₁, …, x⁻¹ e_ϱ, x⁻¹ z` in their Gram–Schmidt orthogonalisation. 

### `isBoxPartitionOfUnity_reducedIndicator`

 The indicator of the reduced points for the chosen set of representatives is a partition of
unity in boxes (`IsBoxPartitionOfUnity`) for every class `c`. 

### `IsBoxPartitionOfUnity.mem_frameBox`

 Let `ω` be a partition of unity in boxes for the class `c`: a weight whose translates under
`S.classUnipotent c` add up to one modulo the subgroup fixing the frame, and which vanishes unless
the frame vectors `(y v)⁻¹ f_a` have norm at most `b ^ 27` times `besselLength (y v)`, the infimum
of `‖s (y v)‖ + 1` over `s` in the Bessel subgroup. Here `b = S.b`. If `ω y ≠ 0` and
`besselLength (y v)` is at most `b ^ (6 n + 2) R` with `n = 𝔰.n`, then the frame vectors of `y v`
have norm at most `frameBoxRadius * R`. 

### `mem_frameBox_of_classCutoff_ne_zero`

 The cutoff `S.classCutoff c` of a class `c` is a cutoff for the rational unipotent elements
fixing the frame, times the indicator of the reduced points. If it is not zero at `y` and
`besselLength (y v)`, the infimum of `‖s (y v)‖ + 1` over `s` in the Bessel subgroup, is at most
`b ^ (6 n + 2) R`, with `b = S.b` and `n = 𝔰.n`, then the frame vectors `(y v)⁻¹ f_a` have norm at
most `frameBoxRadius * R`, where `frameBoxRadius = b ^ (37 n)`. 

### `mem_boxedPoints_of_classCutoff_ne_zero`

 If the cutoff of the class `c` is not zero at `y` and all components of `y` have length at most
`S.b ^ (6 n + 2)` with `n = 𝔰.n` (`InCut`), then `y` lies in the set `boxedPoints` of reduced points
in the cut. 

### `tsum_classCutoff_eq_one`

 The translates of `S.classCutoff c` under the congruence group `S.classUnipotent c` of rational
unipotent elements add up to one at every point `y`. 

### `frameImage_inr_eq_of_frameProducts_eq`

 Let `f = (e₁, …, e_ϱ, z)` be the frame. If the hermitian products `S.frameProducts g b a` of
`f_b` with `g f_a` equal those of `f_b` with `f_a` for all `b`, then `g` moves `f_a` only along the
vectors `e_i`: all other coordinates of `g f_a` and `f_a` agree. 

### `norm_Φ_frameProducts_sub_le`

 The hermitian products `S.frameProducts` of the frame vector `f_b` with `γ f_a` and with
`γ' f_a` differ, under the embedding `Φ v` at the place `v`, by at most `S.N` times the norm of
`y⁻¹ f_b` times the distance of the `a`-th frame vectors of `γ⁻¹ y` and `γ'⁻¹ y`. 

### `termsOver.isIntegral_inl_besselFrame`

 For a term `γ` over `(c, s, c')`, the coordinates along the `e_a` of the images `γ f_b` of the
frame vectors `e₁, …, e_ϱ, z` are algebraic integers. 

### `one_le_pow_mul_norm_basisScale_div`

 The scales `S.basisScale v` that normalise the basis at the place `v`
(`S.realM v ^ (ϱ - a + 1) / √N` on `e_a`, `1 / √N` on `z`) of two frame vectors differ by a factor
of at most `S.b ^ (23 ϱ)`. 

### `norm_Φ_sub_mul_norm_basisScale_div_le`

 Let `f = (e₁, …, e_ϱ, z)` be the frame. Suppose that `γ f` and `γ' f` differ only along the
`e_x`, and that `γ f_b` and `γ' f_b` have the same coordinates along `e_x` for `x > a`. Then the
difference of their coordinates along `e_a`, times the ratio of the scales of `f_b` and `e_a` in
the normalised basis at `v` (`S.basisScale v`), is at most the operator norm `‖w y‖` times the
distance of the `b`-th frame vectors of `γ⁻¹ y` and `γ'⁻¹ y`, for every `w` in the unipotent
subgroup `besselU`, whose rows along the `e_a` are unitriangular. 

### `frameImage_eq_frameImage_one_of_close`

 **Rigidity of frames.** Let `E` be a CM field and `S` admissible filling data over `E`
(`IsAdmissible`), with parameters `b = S.b` and `N = S.N`, a prime. Let `g` be a term over some
`(d, r, d')`: a rational element with `h_d⁻¹ g h_d'` integral and of reduction `r`, where `h_d` is
the representative of the class `d` (`termsOver`). Let `R ≥ 1`, `n = 𝔰.n` and
`ρ = frameBoxRadius * R` with `frameBoxRadius = b ^ (37 n)`. The frame is `f = (e₁, …, e_ϱ, 𝔰.z)`.
Let `z` be a point at the infinite places such that at every place the infimum `besselLength` of
`‖s z‖ + 1` over the Bessel subgroup is at most `b ^ (6 n + 2) R` and the frame vectors `z⁻¹ f_a`
have norm at most `ρ`. If the frame vectors of `g⁻¹ z` and `z` are at distance less than `(N ρ)⁻¹`
at every place, then `g` fixes the frame, that is, `g f = f`. 

### `encard_image_frameImage_le`

 **Packing of frames.** Let `E` be a CM field, `𝔰` a shape (`𝔰.ϱ` hyperbolic planes), and `S`
admissible data of the filling theorem over `E` (`IsAdmissible`), with parameter `b = S.b`. Let
`n = 𝔰.n`, `R ≥ 1` and `frameBoxRadius = b ^ (37 n)`. The frame is `f = (e₁, …, e_ϱ, z)`, and the
frame vectors of `x ∈ 𝔰.G₁` are the `x⁻¹ f_a` (`frameVector x a`). Let `A` be a set of rational `γ`,
each in `termsOver c s c'` for the given class `c` and some `s`, `c'`. Let `y` be a point of `𝔰.G₁`
at each infinite place. Suppose that for `γ ∈ A` the point `x = (S.ratToInf γ)⁻¹ y` has, at every
place, infimum of `‖s x‖ + 1` over the Bessel subgroup (`besselLength`) at most `b ^ (6 n + 2) R`.
Suppose also that it has frame vectors of norm at most `frameBoxRadius * R` (`frameBox`), and that
the frame vectors of any two of these points differ by an element of the real subspace `V`. Then the
images `γ f` (`frameImage`) of the frame take at most `(b ^ (6 n ^ 2) R ^ 2) ^ dim V` values on
`A`. 

### `tsum_le_of_le_classCutoff_mul`

 **Packing of weights.** Let `E` be a CM field with a primitive 5040-th root of unity and `S`
admissible filling data over `E` (`IsAdmissible`). Let `k p` be classes and `γ p` rational elements
with `p ↦ (k p, γ p)` injective, `w p` weights, `y` a point at the infinite places, `R ≥ 1`,
`b = S.b` and `n = 𝔰.n`. Suppose that for `p` in the support of `w` the element `γ p` is a term
over `(c, s, k p)` (`termsOver`), the point `x_p = (γ p)⁻¹ y` has at every place infimum of
`‖s x_p‖ + 1` over the Bessel subgroup (`besselLength`) at most `b ^ (6 n + 2) R`, and `w p` is at
most `x` times `S.classCutoff (k p)` at `x_p`, a cutoff for the rational unipotent elements fixing
the frame `f = (e₁, …, e_ϱ, z)` times the indicator of the reduced points. If the frame vectors
`x_p⁻¹ f_a` of any two of these points differ by an element of the real subspace `V`, then the
weights add up to at most `(b ^ (6 n ^ 2) R ^ 2) ^ dim V * x`. 

### `exists_classUnipotent_mul_mem_boxedPoints`

 Let `E` be a CM field with a primitive 5040-th root of unity, `S` admissible filling data over
`E` for the shape `𝔰` (`IsAdmissible`), and `c` a class in `S.Classes`. Suppose a point `y`
satisfies `InCut` at every infinite place `v`: `besselLength (y v)`, the infimum of ‖s (y v)‖ + 1
over `s` in the Bessel subgroup, is at most `S.b ^ (6 n + 2)`, where `n = 𝔰.n`. Then some `u` in
`S.classUnipotent c`, the congruence group of rational unipotent elements attached to `c`, has
`S.ratToInf u * y` in `boxedPoints`. The boxed points are those satisfying the same bound that are
reduced: the entries above the diagonal of their triangular matrices of Gram–Schmidt coefficients,
read in the rational frame, lie in a chosen residue domain. 

### `measurable_classCutoff`

 The cutoff of a class is measurable. 
