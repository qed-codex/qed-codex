---
{
  "module": "src/Lib/Shimura/ThetaModuli/FlatClosure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/FlatClosure.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/FlatClosure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flat families of ideals cut out by points and the flat closure of theta points

An ideal of polynomials is cut out by points in the chart `c` if it contains `X c - 1`, the forms of
degree `r ^ j` have prescribed ranks modulo the ideal, and its forms of degree `r ^ j` with `j ≤ i`
are those that vanish at given points. When the points are the images of the same `A`-valued points,
such ideals fit into a flat family over `A`, and a degree bound for monomial ideals shows that
finitely many degrees suffice.

## Main definitions and results

* `New.Variety.ThetaNull.IsCutDegree`, `New.Variety.ThetaNull.eventually_isCutDegree`: for every
  large enough `d`, a monomial ideal with at most `σ i` standard monomials of degree `r ^ i` for all
  `i ≤ d` has at most `σ i` of them in every degree `r ^ i`.
* `New.Variety.ThetaNull.eq_map_and_flat_of_isCutOut`: let `I₀` and the `I n` be cut out by the
  images of the same `A`-valued points along a local map `φ` and jointly injective maps `ψ n` to one
  field `K`, with `r > 1` and `i` such a bound. Let `T` be the polynomials over `A` that map into
  every `I n`. Then `I₀` is the reduction of `T`, and the quotient by `T` is flat.
* `New.Variety.ThetaNull.IsCutOutAt`: at a field-valued point `t` of `S`, the vanishing ideals of a
  set `Z` in the affine charts are cut out (`New.Variety.ThetaNull.IsCutOut`) by the values at `t`
  of given maps `P a` from `S` to projective space.
* `New.Variety.ThetaNull.exists_isFlatClosure`: for points `θ n z` of projective space over complex
  points `η n` of a reduced `S`, cut out (`New.Variety.ThetaNull.IsCutOutAt`) at each `η n` by
  linear systems `P`, with `r > 1` and `i` a degree bound (`New.Variety.ThetaNull.IsCutDegree`),
  where every point of `S` specialises to a geometric point at which some set is cut out, the
  reduced closure of the points over a finite dense set of the `η n` is flat over `S`, and every
  point of `S` specialises to a geometric point with reduced fibre.

Notions from other files:
* `AddSemigroupIdeal (J →₀ ℕ)` (Mathlib): a set of exponents that is closed under adding any
  exponent, that is, a monomial ideal.
* `New.LineBundle` with `New.LineBundle.IsLinearSystem`: a map from a scheme to projective space,
  given by charts and the ratios of coordinates on them.
* `New.IsDenseFamily`: a family of complex points of a scheme whose images are dense.
* `New.Variety.AllSpecializeTo`: every point of a scheme S specialises to the image of some point
  over an algebraically closed field that satisfies a property Q of field-valued points.

## Relation to the literature

Known; see `Lib.Shimura.ThetaModuli.UniversalFamily` for sources.



## Ideals cut out by points and a degree bound for monomial ideals

Commutative algebra for flat families of ideals cut out by points. Polynomials are in finitely many
variables `J`. Monomials are exponents `J →₀ ℕ`, and a monomial outside a monomial ideal is called
standard.

The idea: explicit determinants give forms in `T` with all needed leading monomials. Division by
them shows that the standard monomials span, and ranks give freeness.


### `instance : Fintype (degree ⁻¹' {d} : Set (J →₀ ℕ))`

 In finitely many variables there are finitely many exponents of total degree `d`. 

 ### A degree bound for monomial ideals 

### `IsCutDegree`

 `d` is a degree bound for monomial ideals in the variables `J` with counts `σ`: every monomial
ideal `M` that leaves out at most `σ i` monomials of degree `r ^ i` for all `i ≤ d` does so for
all `i`. 

### `thetaRanks`

 For a subgroup `T` of an additive group `G`, the integer part of the square root of the number
of `y` with `r ^ j • y ∈ T`. 

### `eventually_isCutDegree`

 Every large enough `d` is a degree bound (`IsCutDegree`) for monomial ideals in finitely many
variables `J` with counts `σ`. 

### `imageMod`

 The image of a submodule of `A[X]` in the quotient `A[X] ⧸ T`. 

### `IsCutOut`

 An ideal `I` of polynomials over the field `k` in the variables `J` is cut out by the points
`p a` of `k ^ J` in the chart `c`, with ranks `σ j` in every degree `r ^ j` and the vanishing
condition in the degrees `r ^ j` with `j ≤ i`: the ideal `I` contains `X c - 1`. For each `j`,
the forms of degree `r ^ j` span a space of dimension `σ j` modulo `I`. For `j ≤ i`, the forms of
degree `r ^ j` in `I` are exactly those that vanish at all the points `p a`. 

### `IsCutOut.X_sub_one_mem`

 The coordinate `X c` is `1` modulo `I`: the ideal lives in the affine chart `c`. 

### `IsCutOut.rank`

 The forms of degree `r ^ j` span a space of dimension `σ j` modulo `I`. 

### `IsCutOut.mem_iff_vanish`

 For `j ≤ i`, a form of degree `r ^ j` lies in `I` iff it vanishes at all the points `p a`. 

### `restrictSupport_le_homogeneousSubmodule`

 A polynomial supported on exponents of total degree `d` outside a set `M` is a form of degree
`d`. 

### `instance : Module.Finite A (homogeneousSubmodule J A d)`

 In finitely many variables the forms of degree `d` form a finite `A`-module. 

 ### Flatness 

### `imageMod_homogeneousSubmodule_eq`

 Division with remainder. Let `φ : A →+* k` be a local homomorphism to a field. If every exponent
in `W` leads the nonzero reduction along `φ` of a form in `T`, then modulo any ideal `I` containing
the image of `T` the monomials of degree `d` outside `W` span the forms of degree `d`. 

### `eq_zero_of_ncard_le_finrank`

 If the monomials in `S` span modulo `I` a space of dimension at least their number, they are
independent modulo `I`. 

### `exists_independent_monomials`

 Among the monomials in `S` there are as many independent ones modulo `I` as the dimension of
the space they span modulo `I`. 

### `IsCutOut.minors_eq_zero_iff`

 Let `I` be cut out by the points `p a` in the chart `c` (`IsCutOut`: ranks `σ j` in the
degrees `r ^ j`, vanishing conditions up to the degree `r ^ i`). Monomials `μ b`, `b < n`, of a
degree `r ^ j` with `j ≤ i` are dependent modulo `I` iff the `n × n` determinant of their values at
`n` of the points `p a` vanishes for every choice of the `n` points (repetitions allowed). 

### `cofactorForm`

 The determinant whose first row is the `n + 1` monomials `μ l` and whose other rows are their
values at the `n` points `p s`, expanded along the first row. 

### `IsCutOut.map_cofactorForm_mem`

 Suppose `I`, an ideal of polynomials over `k` in the variables `J`, is cut out in the chart `c`
by the points `ρ ∘ P a` in the sense of `IsCutOut r i σ c`. This means `X c - 1 ∈ I`, forms of
degree `r ^ j` span a space of dimension `σ j` modulo `I`, and for `j ≤ i` the forms of degree
`r ^ j` in `I` are exactly those that vanish at all the points `ρ ∘ P a`. For `j ≤ i`, take
`σ j + 1` monomials `μ` of degree `r ^ j` and `σ j` of the points `P (a s)`, and form their
`cofactorForm`: the determinant whose first row is the monomials and whose other rows are their
values at the points, expanded along the first row. Its image under `ρ` lies in `I`. 

### `leadingExponents`

 The exponents that lead, for the monomial order `o`, the nonzero reduction along `φ` of a form
in `T`. They form a monomial ideal. 

### `IsCutOut.ncard_diff_leadingExponents_le`

 Let `φ : A →+* k` be a local homomorphism to a field, and let `I₀` be cut out in chart `c` by
the points `φ ∘ P a` (`IsCutOut`: `X c - 1 ∈ I₀`, the forms of degree `r ^ j` have rank `σ j` modulo
`I₀`, with the vanishing condition for `j ≤ i`). Let `T` reduce into `I₀`, let `j ≤ i`, and let `T`
contain the cofactor form (the determinant with first row the monomials, other rows their values at
the points) of any `σ j + 1` monomials of degree `r ^ j` at any `σ j` of the `P a`. Then at most
`σ j` monomials of degree `r ^ j` are not leading exponents of `T`. 

### `flat_of_exists_restrictSupport_of_eq_zero`

 Let `S j` be sets of exponents such that modulo `T` every polynomial of total degree at most `j`
is congruent to one supported on `S j`, and no nonzero polynomial supported on `S j` lies in `T`.
Then `A[X] ⧸ T` is flat over `A`. 

### `eq_map_and_flat_of_isCutOut`

 Let `φ : A → k` be a local homomorphism to a field, let the maps `ψ n : A → K` have no common
nonzero kernel element, let `1 < r`, and let `i` be a degree bound for the counts `σ`
(`IsCutDegree J i r σ`). Assume that `I₀` is cut out (`IsCutOut`) in the chart `c` by the points
`φ (P a)`, with ranks `σ` and the vanishing condition up to degree `r ^ i`, and that each `I n` is
cut out in the same way by the points `ψ n (P a)`. Then the ideal `T`, consisting of the polynomials
`f` over `A` with `ψ n f ∈ I n` for every `n`, generates `I₀` along `φ`, and `A[X] ⧸ T` is flat over
`A`. 


## The flat projective closure of a dense family of theta points

A map to projective space is a line bundle `New.LineBundle` with `New.LineBundle.IsLinearSystem`.
Its transition functions `transition i j` are the ratios of coordinates `s j / s i` on the chart
`opens i`. `New.LineBundle.IsHomogeneousCoords` gives the homogeneous coordinates of a point.
`New.IsSeparatingFamily ξ` adds to `New.IsDenseFamily ξ` that the scheme is reduced.


### `IsCutOutAt`

 The ideals of a set `Z ⊂ K ^ J` are cut out at a point `t` of `S` with values in the field `K`
by the maps `P a` to projective space. That is: for every choice of charts `l a` of the `P a` that
contain `t` and every chart `c`, the vanishing ideal of the points `v ∈ Z` with `v c ≠ 0`, scaled to
`v c = 1`, satisfies `New.Variety.ThetaNull.IsCutOut r i σ c` for the affine coordinates of the
points `P a` at `t` (ranks `σ j` in the degrees `r ^ j`, and in the degrees `r ^ j` with `j ≤ i`
the forms of the ideal are those that vanish at these points). 

### `isCutOut_of_isCutOutAt`

 Let the `P a` be linear systems on `S` with charts `l a` that contain the point
`s : Spec R ⟶ S`, and let `t = Spec φ ≫ s` for a ring map `φ : R → K` to a field. If the
ideals of `Z` are cut out by `P` at `t`, then in each chart `c` they are cut out by the images
under `φ` of the affine coordinates of the `P a` at `s`. 

### `IsFlatClosure`

 `A` is a flat projective family over `S` spanned by points `e n z` over the complex points
`η n` of `S`, with homogeneous coordinates `θ n z` in the linear system `N`. 

### `IsFlatClosure.isProjEmbedding`

 `A` is proper over `S`, and the linear system `N` separates points with the same image
  in `S`. 

### `IsFlatClosure.flat`

 `A` is flat over `S`. 

### `IsFlatClosure.isHomogeneousCoords`

 The point `e n z` has homogeneous coordinates `θ n z`. 

### `IsFlatClosure.isSeparatingFamily_fibre`

 The fibre over `η n` is reduced, and the points `e n z` are dense in it. 

### `IsFlatClosure.allSpecializeTo_isReduced`

 Every point of `S` specialises to a geometric point over which the fibre is reduced. 

### `IsFlatClosure.isSeparatingFamily`

 `A` is reduced, and all the points `e n z` together are dense in it. 

### `IsChartPresentation`

 The chart `c` of the linear system `L` on a scheme `X` over `Spec R` is affine, and `u` presents
its ring of sections as a quotient of the polynomial ring in the affine coordinates. Here
`specMap ψ` is the morphism of spectra given by a ring map `ψ`, and `ofSection g B t` is the value
of a section `g` at a `B`-valued point `t`. 

### `IsChartPresentation.isAffineOpen`

 The chart is affine. 

### `IsChartPresentation.surjective`

 Every section over the chart is a polynomial in the coordinates. 

### `IsChartPresentation.specMap_comp_C`

 `u` is compatible with the structure maps to `Spec R`. 

### `IsChartPresentation.ofSection_eq`

 At a point `t` of the chart, `u f` is the value of `f` at the affine coordinates of `t`. 

### `flat_of_isChartPresentation`

 `X` is flat over `Spec R` if the ring of each chart is a flat `R`-module. 

### `isReduced_of_isChartPresentation`

 `X` is reduced if the ideal of each chart is radical. 

### `isDenseFamily_of_isChartPresentation`

 Complex points `x v` of a complex scheme `X`, with homogeneous coordinates `θ v`, are dense if
in each chart `c` a polynomial vanishing at all the `θ v` with `θ v c ≠ 0`, scaled to `θ v c = 1`,
lies in the ideal of the chart. 

### `IsChartPresentation.ker_le_ker_iff`

 In the chart `c` of the base change of `z : A ⟶ S` along `b`, a map `φ` kills the ideal of the
chart exactly when the `φ (X j)` are the coordinates of a point of `A` in the chart `c` that lies
over the point of `S` given by `φ.comp C` and `b`. 

### `IsChartPresentation.mem_ker_stalk_iff`

 Let `A` and `S` be reduced schemes with `z : A ⟶ S`, and let `u` present the chart `c` of the
pullback of the line bundle `N` to the base change of `A` to the local ring of `S` at `p`. Let the
complex points `x (a, v)` be dense in `A`, lie over the complex points `ξ a` of `S` (finitely many
`a`), and have homogeneous coordinates `θ a v` for `N`. Then a polynomial `f` over the local ring
lies in the kernel of `u` exactly when, for every `a` and every `ψ : stalk → ℂ` through which `ξ a`
factors, the image of `f` under `ψ` vanishes at every point `θ a v / (θ a v) c` with
`(θ a v) c ≠ 0`. 

### `flat_stalkMap_of_flat_snd`

 If the base change of `z` to the local ring at `p` is flat, then `z` is flat at every point
whose image generalises `p`. 

### `exists_reduced_projective_closure`

 Complex points `ξ w` of `S` and nonzero vectors `θ w` give points of `ℙ^J × S`. Their reduced
closure `A` is projective over `S`, with dense points `x w` over `ξ w` with coordinates `θ w`. 

### `flat_snd_and_iInf_ker_eq_of_isCutOutAt`

 The main step towards `exists_isFlatClosure`. Let `S` be reduced, with finitely many dense
complex points `η (j a)`, and at every `η n` the ideals of the vectors `θ n v` are cut out by the
linear systems `P`, where `1 < r` and `i` is a degree bound for the ranks `σ`. Let `A` be reduced
over `S`, with dense complex points `x₀ (a, v)` over `η (j a)` with homogeneous coordinates
`θ (j a) v` for `N`, and let `u b c` present the chart `c` of the base change of `A` along each `b`.
At a field-valued point `t` of `S` where the ideals of `Z` are cut out by `P`: the base change of
`A` to the local ring of `S` at the image of `t` is flat, and in each chart `c` the ideal of the
fibre over `t` is the vanishing ideal of the `v ∈ Z` with `v c ≠ 0`, scaled to `v c = 1`. 

### `exists_isHomogeneousCoords_of_ker_le_ker`

 Let `N` embed `A` in projective space over `S` along `z`, let `ξ` be a complex point of `S`, and
let `u` present the chart `c` of the fibre of `A` over `ξ`. A vector `θ₀` with `θ₀ c ≠ 0` whose
evaluation (scaled to `θ₀ c = 1`) vanishes on the ideal of the chart is the vector of homogeneous
coordinates of a point of `A` over `ξ`. 

### `exists_isFlatClosure`

 Let `S` be reduced, with complex points `η n` of which finitely many, the `η (j a)`, are dense.
Let nonzero vectors `θ n v` be given whose ideals are cut out at `η n` by linear systems `P a`
(`IsCutOutAt`: ranks `σ m` in every degree `r ^ m`, vanishing in the degrees `r ^ m` with `m ≤ i`),
where `r > 1` and `i` is a degree bound for the ranks `σ`. Let every point of `S` specialise to a
geometric point where some set has its ideals cut out by `P`. Then the `θ n v` are the coordinates
of points spanning a flat projective family over `S`. 
