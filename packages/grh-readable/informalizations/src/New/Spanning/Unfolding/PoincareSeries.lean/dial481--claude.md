---
{
  "module": "src/New/Spanning/Unfolding/PoincareSeries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Poincaré series of fitting spaces, unfolding, Petersson products and source form coordinates

This file builds Poincaré series from the Bessel functions of filling data S (`New.Filling`) on a
hermitian space V that fits S, and computes their Petersson products.

K = `New.Filling.latticeStabilizer` and K(M) = `New.Filling.principalLevel` are levels in the
lattice basis of S. Here K(M) is the kernel of reduction at the chosen places, and M in this
notation is the product of the two level primes, not an adelic point. For a graded space Y on V that
fits S, the groups attached to Y correspond to those of S under `New.Filling.Fits.adelicEquiv` and
`New.Filling.Fits.finiteEquiv`, and algebraic forms of level `S.sourceLevel` get coordinates indexed
by classes and indices.

## Main definitions and results

* `New.Filling.Fits`: V matches S; this gives the identifications `New.Filling.Fits.ratEquiv`
  (rational points), `New.Filling.Fits.realHomeomorph` (infinite places) and
  `New.Filling.Fits.finiteEquiv` (finite places).
* `New.Filling.Fits.cutBessel`, `New.Filling.Fits.poincareSeries`: a coordinate i of the Bessel
  function, cut off and supported on the coset of a class c, and the series ∑_a φ_a ∑_γ of these,
  a = (c, i).
* `New.Filling.Fits.petersson_poincare`: the Petersson products of translated series are the
  amplitude sums `New.Filling.amplitudeSum` times the volume of the level.
* `New.Filling.Fits.poincareMap`, `New.Filling.Fits.coe_poincareMap`: the series are forms of level
  `New.Filling.stdPrincipalLevel`, linear in φ.
* `New.Filling.Fits.sourceFormCoords`: algebraic forms of level `S.sourceLevel` as vectors of the
  Euclidean space on classes times indices.
* `New.Filling.Fits.finrank_levelSpace_eq_sourceDim`: the dimension of the space of these forms is
  the number of classes times the dimension of the weight, and it is positive.

Notions from other files:
* `New.Filling.besselFn`: W_i(y), the product over the infinite places v of the i_v-th coordinate of
  the local Bessel function W_v at y_v. Only the full (not the cut) function is used: `.full`.
* `New.Filling.classRep`, `New.Filling.classUnipotent`, `New.Filling.classCutoff`: for a class c,
  its representative h_c, the group 𝖴_c(M) of rational unipotent u with h_c⁻¹ u h_c ∈ K(M), and a
  cutoff β_c at the infinite places whose translates under 𝖴_c(M) sum to 1.
* `New.Filling.termsOver`: the rational γ such that h_c⁻¹ γ h_c' lies in K and has reduction s.
* `New.Shape.Form.besselU`: the Bessel unipotent group 𝖴: the isometries of
  `New.Shape.Form.splitGram` T that are block upper unitriangular for the levels
  `New.BesselIndex.level`, so trivial on the middle block.
* X₀ is the hermitian space on κ with the standard form, all signs +1; U(X₀) is its unitary group.

## Relation to the literature

The file also contains known results stated on this proof's data: Poincaré series along a Bessel
subgroup and their unfolding. See `Lib.DiscreteSeries.Bruhat.FloorGroups`.


### `Fits`

 The hermitian space V, with grading Y, fits the filling data S: the Bessel system of S at each
infinite place v has type (l v, kw v), Y is standardly indexed, and `typeKernel l ε` is an
idempotent kernel. The finite part of the point of V is a finite idele times `toBesselH 𝔰 ↑S.N η`
times `S.latticeBasis` times an integral matrix that reduces to 1 at the chosen places. The element
η is central. 

### `Fits.isDiscreteSeriesBessel`

 The Bessel system at each infinite place `v` has type `(l v, kw v)`. 

### `Fits.index_eq`

 The grading `Y` labels the basis of `V` in the standard way, by `besselIndexEquiv`. 

### `Fits.isIdempotentKernel`

 The kernel `typeKernel l ε` is idempotent. 

### `Fits.exists_point_eq`

 The finite part of the point of `V` is a finite idele times `toBesselH _ ↑S.N η` times
  `S.latticeBasis` times an integral matrix that reduces to 1 at the chosen places. 

### `Fits.central`

 The element η commutes with every element of the finite adelic unitary group on κ. 

### `stdPrincipalLevel`

 The principal level at the chosen places of S (integral matrices that reduce to 1 there), as an
open subgroup of the finite adelic unitary group in orthonormal local bases. 

 ### Identifying the groups of `V` and of `S` 

### `J_eq_ratGram`

 If V fits S, the Gram matrix of V is the rational Gram matrix of S. 

### `ratEquiv`

 The isomorphism from the rational points of the unitary group of S onto the discrete
subgroup Γ of V, given by `New.Space.ratEmbed`. 

### `adelicEquiv`

 The isomorphism, given by the point of V, from the standard adelic group of signs ε onto the
adelic points of the unitary group of S. 

### `adelicEquiv_ratEquiv`

 For γ a rational point of the unitary group of S, `X.adelicEquiv` applied to the image
`X.ratEquiv γ` of γ in Γ equals `S.ratToAdelic γ`, the diagonal embedding of γ into the adelic
group. 

### `gram_map_evalInf_point`

 Let the hermitian space V fit the filling data S, and let x_v be the component of the point
`V.x` at an infinite place v. Then x_vᴴ J x_v is the diagonal matrix of the signs ε, where J is the
Gram matrix of S over ℂ: ϱ hyperbolic pairs around the middle block `S.ratMiddle ℂ`. 

### `realHomeomorph`

 The homeomorphism from G_∞ onto ∏_v G₁, g_v ↦ d_v⁻¹x_v g_v p⁻¹, with x the point of V,
d_v = `New.Filling.basisScaleGL` and p the chosen unitary sign frame. 

### `realHomeomorph_mul`

 The homeomorphism `X.realHomeomorph` turns left translation by g into left translation by the
infinite part of `X.adelicEquiv g`. 

### `finiteEquiv`

 The isomorphism from the standard finite adelic unitary group onto that of S in the lattice
basis: conjugate by the finite point of V, change to the lattice basis, then conjugate by the
inverse of the image `New.Filling.inclHFin` of η, that is x ↦ ι(η)⁻¹ x ι(η). 

### `finiteEquiv_eq_conj_adelicToFin`

 On finite parts, `X.finiteEquiv` is the finite part of `X.adelicEquiv` in the lattice basis,
conjugated by the inverse of `S.inclHFin η`. 

### `exists_coe_finiteEquiv_eq_conj`

 The isomorphism `New.Filling.Fits.finiteEquiv` is conjugation by an integral matrix x that
reduces to 1 at the chosen places. 

### `finiteEquiv_mem_latticeStabilizer_iff`

 The image of k under `New.Filling.Fits.finiteEquiv` preserves the lattice of S if and only if k
is integral in the orthonormal local bases of V. 

### `reduction_finiteEquiv_iff`

 The image of k under `New.Filling.Fits.finiteEquiv` lies in the lattice stabilizer
`New.Filling.latticeStabilizer` with reduction s if and only if k lies in the integral subgroup
`New.stdLevel` with reduction s at the chosen places. Here s is a family of matrices over the
residue fields of these places. 

### `mem_stdPrincipalLevel_iff`

 An element k lies in the principal level `S.stdPrincipalLevel`, taken in orthonormal local
bases, if and only if its image under `New.Filling.Fits.finiteEquiv` lies in the principal level
`S.principalLevel`, taken in the lattice basis of S. 

 ### The Poincaré series 

### `cutBessel`

 For a = (c, i), the function of adelic g equal to β_c(y) W_i(y), y the image of g_∞ under
`New.Filling.Fits.realHomeomorph`, if ψ⁻¹(h_c⁻¹ ι(η)) g_f lies in `New.Filling.stdPrincipalLevel`,
and 0 otherwise; here ψ = `New.Filling.Fits.finiteEquiv`, ι = `New.Filling.inclHFin`, and β_c is the
cutoff of c. 

### `cutBessel_ratEquiv_mul`

 For a = (c, i) and a rational point γ of the unitary group of S, `New.Filling.Fits.cutBessel` a
evaluated at (image of γ under `New.Filling.Fits.ratEquiv`)·g equals β_c(y) W_i(y) if h_c⁻¹ γ_f ι(η)
ψ(g_f) lies in `New.Filling.principalLevel`, and 0 otherwise. Here y is γ_∞ times the image of g_∞
under `New.Filling.Fits.realHomeomorph`. Also ψ = `New.Filling.Fits.finiteEquiv`,
ι = `New.Filling.inclHFin`, h_c = `New.Filling.classRep` of c and β_c is the cutoff of c. The
element η is the central finite adelic point of U(X₀) in the fit `X : S.Fits V l kw Y η`. 

### `enorm_cutBessel_ratEquiv_mul_le`

 The cut-off function of a = (c, i) at γ·g is bounded by β_c(y) ∏_v ‖W_v(y_v)‖, where y is γ_∞
times the image of g_∞ under `New.Filling.Fits.realHomeomorph`, β_c is the cutoff of c and W_v is
the local Bessel function. 

### `poincareSeries`

 The Poincaré series of φ: g ↦ ∑_a φ_a ∑_{γ∈Γ} `New.Filling.Fits.cutBessel` a (γg), where
Γ = `V.Γ` is the group of rational points and a runs over pairs (class, coordinate). 

### `measurable_cutBessel`

 For admissible filling data, the cut-off Bessel function of a is measurable on the adelic
group. 

### `tsum_cutBessel_classUnipotent`

 Assume `S.IsAdmissible`. For a = (c, i) and adelic g, sum `X.cutBessel a` at u·g over u in the
rational unipotent group `S.classUnipotent c`, with u embedded by `X.ratEquiv`. The sum is W_i(y),
the i-th coordinate of the full Bessel function `S.besselFn` at the image y of g_∞ under
`X.realHomeomorph`, if h_c⁻¹ ι(η) ψ(g_f) lies in `S.principalLevel`, and 0 otherwise. Here
h_c = `S.classRep c`, η is the central element in `X : S.Fits V l kw Y η`, ι = `S.inclHFin` and
ψ = `X.finiteEquiv`. 

### `exists_tsum_enorm_cutBessel_le`

 Let V fit the admissible filling data S (the hypothesis X) and let a = (class, coordinate). The
sums over γ in the group `V.Γ` of rational points of the norms of the cut-off Bessel function
`X.cutBessel a` at γg are bounded uniformly in the adelic point g.

Known result: a step in the convergence of Poincaré series along a Bessel subgroup. 

 ### Unfolding and Petersson products 

### `integrable_cutBessel`

 If the filling data are admissible, each cut-off Bessel function `X.cutBessel a` is integrable
on the adelic group. 

### `mul_tsum_cutBessel`

 A function y invariant under Γ = `V.Γ` moves into the sum over Γ of the translates of
`X.cutBessel a`. 

### `integrable_mul_cutBessel`

 For admissible filling data and a form y on V of any type e (a bounded automorphic function),
the product y·`X.cutBessel a` is integrable on the adelic group. 

### `integrable_mul_tsum_cutBessel`

 For admissible filling data and a form y on V of any type e, the product of y with the sum over
Γ = `V.Γ` of the translates of `X.cutBessel a` is integrable on Γ∖G. 

### `integral_mul_tsum_cutBessel`

 Unfolding of one term, for admissible filling data and a form y on V of any type e: the
integral over Γ∖G of y times the sum over Γ = `V.Γ` of the translates of `X.cutBessel a` is
∫_G y·`X.cutBessel a`. 

### `mul_poincareSeries_eq_sum`

 The product of y with the Poincaré series of φ, expanded over the pairs a. 

### `integrable_mul_poincareSeries`

 For admissible filling data and a form y on V of any type e (a bounded automorphic function),
the product of y with the Poincaré series of φ is integrable on Γ∖G. 

### `integral_mul_poincareSeries`

 Unfolding, for admissible filling data and a form y on V of any type e (a bounded automorphic
function): the integral over Γ∖G of y times the Poincaré series of φ is
∑_a φ_a ∫_G y·`X.cutBessel a`. 

### `integrable_and_integral_mul_poincareSeries`

 Unfolding, for admissible filling data S. Let y be a form on V of any type e (a bounded
automorphic function). Then y times the Poincaré series of φ is integrable on Γ∖G, with integral ∑_a
φ_a ∫_G y·`X.cutBessel a`.

Known result: the unfolding of Poincaré series along a Bessel subgroup. 

### `integral_typeKernel_mul_besselFn`

 Right convolution over the real points with `typeKernel l ε` fixes each coordinate of the full
Bessel function, read on G_∞ through `X.realHomeomorph`. 

### `realConv_tsum_cutBessel_classUnipotent`

 Assume `S.IsAdmissible`. Let a = (c, i) and δ be in the adelic group. Consider the function
x ↦ sum over u in `S.classUnipotent c` of `X.cutBessel a` (u δ x). This function is fixed by right
convolution with `typeKernel l ε`: its convolution at each g equals its value at g. 

### `exists_levelSpace_tsum_cutBessel_eq`

 Let V fit the admissible filling data S (the hypothesis X) and let a = (class, coordinate). The
series g ↦ ∑_γ `X.cutBessel a` (γg) over the rational points γ ∈ `V.Γ` is a form on V of type
`typeKernel l ε` (the discrete series kernel of parameter l) and level `S.stdPrincipalLevel`. 

### `poincareMap`

 For admissible filling data, the linear map from source forms φ to forms of type
`typeKernel l ε` and level `S.stdPrincipalLevel` that sends the basis vector at a to the form
g ↦ ∑_{γ∈Γ} `X.cutBessel a` (γg). It sends φ to the Poincaré series of φ, by
`New.Filling.Fits.coe_poincareMap`. 

### `coe_poincareMap`

 Let the hermitian space V fit the admissible filling data S (the hypothesis X), and let φ be a
vector with coordinates φ_a indexed by pairs a = (class, Bessel coordinate). The form
`X.poincareMap φ` on V, of type `typeKernel l ε` and level `S.stdPrincipalLevel`, is as a function
on the adelic group the Poincaré series `X.poincareSeries φ`. 

### `measurePreserving_realHomeomorph`

 The homeomorphism `X.realHomeomorph` from G_∞ onto ∏_v `𝔰.G₁` preserves the volumes. 

### `classPoint`

 The point ψ⁻¹(ι(η)⁻¹ h_c) of the finite adelic group of V that represents the class c. Here
h_c = `S.classRep c`, ψ = `New.Filling.Fits.finiteEquiv`, ι = `New.Filling.inclHFin`, and η is the
central element of the fit. 

### `cutBessel_eq_mul_indicator`

 The function `X.cutBessel a g` equals `S.classCutoff a.1` times the `a.2`-th coordinate of
`S.besselFn .full`, both evaluated at `X.realHomeomorph g.1`, times the indicator of
`S.stdPrincipalLevel` evaluated at `(X.classPoint a.1)⁻¹ * g.2`. 

### `integral_mul_poincareSeries_eq_sum_classes`

 **Folding.** Let V fit the admissible filling data S (the hypothesis X), and let z be a form on
V of type e and principal level J = `S.stdPrincipalLevel`. The integral over Γ∖G, Γ = `V.Γ`, of z
times the Poincaré series of φ is the volume of J times the sum over the classes c of ∫_{G_∞} β_c(y)
(∑_i φ_{(c, i)} W_i(y)) z(x, x_c) dx. Here y is the image of x under `X.realHomeomorph`,
x_c = `X.classPoint c`, W_i is the i-th coordinate of the Bessel function, and
β_c = `S.classCutoff c` is the cutoff for the quotient by `S.classUnipotent c`. 

### `hasLevel_mul_right`

 The principal level `S.stdPrincipalLevel` is normalised by the integral group `New.stdLevel`, so
the translate by an integral k of a function of principal level has principal level. 

### `mem_principalLevel_iff_mem_termsOver`

 Let S be filling data, K = `S.latticeStabilizer` the integral points of its finite adelic
unitary group, and K(M) = `S.principalLevel` the elements of K whose reduction at the chosen places
is 1. Let c, c' be classes with representatives h_c = `S.classRep c` and h_c', let x be a finite
adelic point with h_c⁻¹ x ∈ K(M), and let k ∈ K have reduction s. For a rational point γ with finite
part γ_f = `S.ratToFin γ`, the element h_c'⁻¹ γ_f⁻¹ x k lies in K(M) if and only if γ is a term over
(c, s, c'). 

### `amplitudeSum_apply_eq_integral_tsum`

 Let the filling data S be admissible, let T be a set of rational points, c and c' classes with
representatives h_c and h_c', and s a family of matrices over the residue fields of the chosen
places. The terms over (c, s, c') are the rational γ such that h_c⁻¹ γ h_c' lies in
`S.latticeStabilizer` and has reduction s. The amplitude sum is the sum, over the terms γ in T, of
the integrals over y ∈ ∏_v `𝔰.G₁` of β_c(y) β_c'(γ⁻¹y) `S.besselKernel .full γ y`. In its entry
i = (i₁, i₂) sum and integral can be exchanged. Here `𝔰.G₁` is the complex unitary group of the
hermitian form of the shape 𝔰, β_c is the cutoff `S.classCutoff c`, and the entry i of the kernel is
W_{i₁}(y) conj(W_{i₂}(γ⁻¹y)), with W the full Bessel function. 

### `petersson_poincare`

 Let the hermitian space V fit the admissible filling data S, and let 𝒫a be the Poincaré series
(`X.poincareMap`) of the basis vector at a, as a form on V of type `typeKernel l ε`. For a = (c, i),
a' = (c', i') and k in `New.stdLevel` with reduction s at the chosen places, the Petersson product
⟨k𝒫a', 𝒫a⟩ is the volume of `S.stdPrincipalLevel` times the (i, i') entry of the amplitude sum, ∑_γ
∫ β_c(y) β_c'(γ⁻¹y) W_i(y) conj(W_i'(γ⁻¹y)) dy. Here γ runs over the rational points such that h_c⁻¹
γ h_c' lies in `S.latticeStabilizer` and has reduction s, y runs over ∏_v `𝔰.G₁`,
h_c = `S.classRep c`, β_c = `S.classCutoff c`, and W is the full Bessel function
`S.besselFn .full`. 


## Groups of a graded fitting space and source forms in Bessel coordinates

* `New.Filling.Fits.adelicToFin_adelicEquiv_inclX`, `New.Filling.Fits.finiteEquiv_inclX`,
  `New.Filling.Fits.adelicToInf_inclX`: the embeddings of U(X₀) agree.


### `New.Shape.submatrix_fromBlocks_besselIndexEquiv`

 In the labelling `𝔰.besselIndexEquiv`, the matrix acting by m on κ and trivially on the string
of length 2ϱ + 1 is the block matrix with m in the κ-block and the identity elsewhere. 

### `New.kroneckerPi_mulVec_prod`

 A Kronecker product acts on a product vector factor by factor. 

### `gradeOf_eq_two_mul_sub_level`

 The grade of an index in the grading Y is twice the difference of ϱ and its level. 

### `mem_unipotent_iff_mem_besselU`

 Under `X.adelicEquiv`, the unipotent group of the grading Y corresponds to the Bessel unipotent
group `besselU` of the adelic group of S. 

### `mem_besselGroup_iff_mem_besselS`

 Under `X.adelicEquiv`, the Bessel group of the grading Y corresponds to the Bessel group
`besselS` of the adelic group of S. 

### `coe_adelicEquiv_inclX`

 The image of `Y.inclX a` under `X.adelicEquiv` is, as a matrix over the adeles, the block matrix
that acts by `G.toUnitary a` on the κ block and fixes all other basis vectors. 

### `adelicToFin_adelicEquiv_inclX`

 For `a` in the adelic unitary group of U(X₀) on κ: map `Y.inclX a` by `X.adelicEquiv`, then take
the finite part in the lattice basis (`S.adelicToFin`). The result is `S.inclHFin a.2`. 

### `finiteEquiv_inclX`

 The isomorphism `X.finiteEquiv` takes the finite part of `Y.inclX a` to `S.inclHFin a.2`. 

### `finiteEquiv_inclXFin`

 The isomorphism `X.finiteEquiv` takes the embedding `Y.inclXFin` of the finite adelic points of
U(X₀) to `S.inclHFin`. 

### `inclXFin_mem_stdLevel_iff`

 If `X` says that `V` with grading `Y` fits `S`, then for `a` in `Gf E 𝔰.κ` (finite adelic
U(X₀)), `Y.inclXFin a` lies in `stdLevel`, the stabiliser of the standard lattice, if and only if
`S.inclHFin a` lies in `S.latticeStabilizer`. 

### `inclXFin_mem_stdPrincipalLevel_iff`

 A finite adelic point of U(X₀), embedded by the grading Y, lies in the principal level of V at
the chosen places if and only if its image `S.inclHFin a` lies in the principal level of S. 

### `adelicToInf_inclX`

 At each infinite place v, the embedding `Y.inclX` of the adelic unitary group U(X₀) on κ,
rescaled into `𝔰.G₁`, is the embedding `toBesselH` applied to the component at v. 

### `exists_weylBesselEquiv`

 If the graded hermitian space V fits the filling data S, there is a linear isomorphism A from
functions on `WeylIndex 𝔰.κ kw` to functions on `S.BesselCoord` with this property. For every family
g of unitary κ×κ matrices g v, one per infinite place v, and every x, the vector A x times
`kroneckerPi` of the matrices `(S.besselSystem v).rep (g v)` equals A applied to `schur kw` of the
transposes (g v)ᵀ times x. 

### `weylBesselEquiv`

 A fixed change of coordinates as in `exists_weylBesselEquiv`, from the values of forms to the
dual of the values of the Bessel function. 

### `weylBesselEquiv_vecMul`

 The change of coordinates `X.weylBesselEquiv` turns the Schur matrix of the transposes of the
g v into right multiplication by the Kronecker product of the local representations. 

### `sourceFormCoords`

 The linear isomorphism that sends an algebraic form of weight kw and level `S.sourceLevel` to
its values at the class representatives, in the coordinates `weylBesselEquiv`. 

### `sourceDim_eq_card_mul_finrank`

 If V fits the filling data S with weight kw, then `S.sourceDim` is the number of classes times
the dimension of the representation of weight kw. 

### `finrank_levelSpace_eq_sourceDim`

 Let E be a CM field, and let V, with grading Y, fit the filling data S: among other conditions,
the Bessel system of S at each infinite place v has type (l v, kw v), and η is central. Let X₀ be
the hermitian space on `𝔰.κ` with the standard definite form. The space of algebraic forms on U(X₀)
of weight (kw, 0) and level `S.sourceLevel` has dimension `S.sourceDim`. This equals the number of
double cosets `S.Classes` of U(X₀) at that level times the dimension of `WeylIndex 𝔰.κ kw → ℂ`, the
representation of weight kw, and it is positive. 
