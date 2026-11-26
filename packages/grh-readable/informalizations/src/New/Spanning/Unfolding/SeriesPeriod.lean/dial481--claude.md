---
{
  "module": "src/New/Spanning/Unfolding/SeriesPeriod.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Poincaré map as a Poincaré series of the Bessel function

There are a real point `g₀` and a linear form `t` for which the form `D.poincareAt g₀ t φ`, which
represents the Bessel period of `φ`, is the Poincaré series of the Bessel function; the map
`D.poincare` is defined by such a choice. Pair the series with a form `y` of the conjugate type.
Unfolding gives a sum over the classes `c` of integrals over `U_c \ G(F_∞)`. Insert the integral
formula of the Bessel function, an integral over `R(F_∞)`, and move the quotient by `U_c` to that
variable; the conjugate kernel reproduces `y`, and the sum
`∑_c ∫_{U_c \ R(F_∞)} 𝒲 (s, h_c) y (s g₀, h_c) ds` remains. The period is a multiple of the same
sum, because `[R] / J'` is the disjoint union of the `U_c \ R(F_∞)`.

Notions from other files:
* `S.Fits V l kw Y η`: the space `V` with the grading `Y` and the central element `η` fits the
  filling data `S`; it identifies the adelic group of `V` with that of `S`.
* `h.poincareSeries φ`: the series `g ↦ ∑_a φ_a ∑_{γ ∈ G(F)} h.cutBessel a (γ g)`, where `a` runs
  over the pairs `(c, i)` of a class and a coordinate, and `h.cutBessel (c, i)` is `β_c` times the
  `i`-th coordinate of the Bessel function on `G(F_∞) × h_c J` and zero elsewhere.
* `Y.besselGroup`, `Y.unipotent`, `Y.inclX`: the group `R(𝔸)`, its unipotent radical and the
  inclusion of `H(𝔸)`, the unitary group of the form on the part `𝔰.κ` of the basis;
  `Y.ratBessel` is `R(F)`, `Y.besselReal` is `R(F_∞)`, `Y.besselFin` is `R(𝔸_fin)`, and
  `Y.besselMeasure` computes integrals over `[R] = R(F) \ R(𝔸)`.
* `J = S.stdPrincipalLevel` is the principal level, and `J' = R(𝔸_fin) ∩ J`.
* `h_c = h.classPoint c`, `U_c = S.classUnipotent c`, `β_c = S.classCutoff c`: the image in
  `R(𝔸_fin)` of `c.out * η⁻¹`, with `c.out` the representative of the class `c`; the group of
  rational unipotents `u` with `h_c⁻¹ u h_c ∈ J`; and a weight at the infinite places whose
  translates under `U_c` add up to one. An integral over a quotient by `U_c` is written as an
  integral against `β_c`.
* `h.besselChar`: the character of `R(𝔸)` given by the entries at the simple roots. The hypothesis
  `hj_genericConst` is `ȷ Y.genericConst = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`, `M = S.M`,
  `ϖ = S.deltaE` and `Y.genericConst` the constant of `ψ_U = Y.unipotentChar`; it makes
  `h.besselChar` equal to `ψ_U` on `U(𝔸)`.
* `Y.sourceFn t φ`: the function `𝒲 (u a) = ψ_U (u) t (ǎ_∞⁻¹ φ (a_fin))` on `R(𝔸)`, where `ǎ_∞`
  is the action `conjWeylRep` of the real component `a_∞` of `a`.

## Relation to the literature

Unfolding a Poincaré series against an automorphic form is standard.


 ### Rational points and the character of `R(𝔸)` 

### `ratEquiv_mem_unipotent`

 If `V` fits `S` (`h`) and `u` is a rational point lying in the Bessel unipotent group `besselU`,
then its image `h.ratEquiv u` lies in the unipotent group `Y.unipotent` of `Y`. 

### `mem_besselS_of_ratEquiv_mem_besselGroup`

 If `V` fits `S` (`h`) and `σ` is a rational point of the unitary group of `S` whose image
`h.ratEquiv σ` lies in the Bessel group `Y.besselGroup`, then `σ` lies in the Bessel subgroup
`besselS`. 

### `besselChar_mul`

 The character `h.besselChar` is multiplicative on the Bessel group `R(𝔸)`. 

### `adelicEquiv_inclX`

 The identification `h.adelicEquiv` of the adelic groups of `V` and `S` carries the inclusion
`Y.inclX` of `H(𝔸)` to the standard inclusion `toBesselH`. 

### `besselChar_inclX`

 The character `h.besselChar` of `R(𝔸)` is trivial on the image under `Y.inclX` of the adelic
unitary group `H(𝔸)` of the standard definite space on `κ`: `h.besselChar (Y.inclX a) = 1`. 

### `besselChar_mul_inv_inclX`

 For `r` in the Bessel group `Y.besselGroup` and any adelic point `a` of the unitary group of the
standard definite space, `h.besselChar` takes the same value at `r * (Y.inclX a)⁻¹` as at `r`. 

### `shift_eq_smul_besselCharMatrix`

 Suppose the space `V` with the grading `Y` fits the filling data `S`; in particular `Y` labels
the basis of `V` in the standard way. Then the shift `𝔢 = Y.shift` of the grading is `c C`, where
`c = Y.genericConst` and `C` is `besselCharMatrix` at the middle block `S.ratMiddle` of the form of
`S`. 

### `besselChar_eq_unipotentChar`

 Suppose `V` with the grading `Y` fits the filling data `S`, and let `h.besselChar r` be the
standard additive character of `E` at `-(M ϖ)⁻¹ σ`. Here `M = S.M`, `ϖ = S.deltaE`, and `σ` is the
sum `simpleRootSum` of the entries of `r` at the simple roots, read in the adelic group of `S`. Let
`c = Y.genericConst` be the constant of the generic character `ψ_U = Y.unipotentChar`, and assume
`ȷ c = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`. Then `h.besselChar u = ψ_U u` for every `u` in
`Y.unipotent`, the unipotent radical of the Bessel group. 

### `sourceFn_eq_besselChar_mul`

 Let `ȷ c = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`, `c = Y.genericConst`, `M = S.M` and
`ϖ = S.deltaE`, so that `h.besselChar` extends the generic character `ψ_U`. Then `sourceFn t φ` at
`r ∈ R(𝔸)` is `h.besselChar r` times the coefficient `algFormCoeff 1 t φ` at the `H`-part
`Y.leviPart r` of `r`. 

 ### The points `h_c` and the groups `U_c` 

### `classPoint_eq_inclXFin`

 The point `h_c` is the image under `H → R` of the representative of `c` times `η⁻¹`. 

### `classPoint_mem_besselFin`

 The point `h.classPoint c` that represents the class `c` lies in `Y.besselFin`, the finite
points `g` such that `(1, g)` lies in the Bessel group `Y.besselGroup`. 

### `inv_classPoint_mul_mem_iff`

 A finite point `t` lies in the coset `h.classPoint c * S.stdPrincipalLevel` if and only if
`S.inclHFin η * h.finiteEquiv t`, in the lattice basis of `S`, lies in
`S.classRep c * S.principalLevel`. 

### `ratEquiv_classUnipotent_mem_besselGroup`

 For `u` in `S.classUnipotent c`, its image `h.ratEquiv u` in the discrete subgroup of `V` lies
in the Bessel group `Y.besselGroup`. 

### `classSection`

 The point `(s, h_c)` of `R(𝔸)`, for a class `c` and a real point `s` of `R`. 

### `classUnipotentToReal`

 The homomorphism `u ↦ u_∞` from `U_c = S.classUnipotent c` to `R(F_∞)`. 

### `tsum_classCutoff_realHomeomorph`

 Suppose `V` fits the admissible filling data `S`, and let `c` be a class. Then
`∑_{u ∈ U_c} β_c (u_∞ x) = 1` for every `x ∈ G(F_∞)`. 

### `exists_ratEquiv_mul_classPoint`

 An element `u` of `U_c` moves `(x, h_c)` to `(u_∞ x, h_c)` up to a right factor in the principal
level, namely `h_c⁻¹ u_fin h_c`. 

 ### The Bessel function as an integral over `R(F_∞)` 

### `sourceFn_classSection`

 Suppose `V` fits `S` and `ȷ Y.genericConst = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`, `M = S.M` and
`ϖ = S.deltaE`, so that `h.besselChar` extends `ψ_U`. Let `ψ` be an algebraic form on `H`, let `t`
be any linear form on its space of values, and let `𝒲` be `sourceFn t` of the translate of `ψ` by
`η`. Let `s = u a` be a real point of `R = U ⋊ H`, so that `a_∞ = (Y.leviPart (s, 1)).1` is the real
component of its `H`-part, and let `h.classSection c s = (s, h_c)`. Then
`𝒲 (s, h_c) = ψ_U (u) t (ǎ_∞⁻¹ ψ (c.out))`, where `ǎ_∞` is the action of `a_∞` by `conjWeylRep` and
`ψ_U (u)` is written `h.besselChar (s, 1)`. 

### `exists_dotProduct_besselFn_eq_integral`

 **The integral formula of the Bessel function, paired with the value of a form on `H`.** Suppose
`V` fits `S` and `ȷ Y.genericConst = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`, `M = S.M` and `ϖ = S.deltaE`.
Then there are a real point `g₀` and a linear form `t` with the following property for every form
`ψ` on `H`, class `c` and real point `x` of the group of `V`. The value of `ψ` at the representative
`c.out`, taken to the coordinates of the Bessel function by the linear isomorphism
`h.weylBesselEquiv`, paired with the full, uncut Bessel function `S.besselFn .full` at the image of
`x` in the real group of `S`, is `∫_{R(F_∞)} conj e (g₀⁻¹ s⁻¹ x) 𝒲 (s, h_c) ds`. Here
`e = typeKernel l ε` is the kernel of the type, `(s, h_c) = h.classSection c s` with `h_c` the
finite point of `c`, and `𝒲 = sourceFn t` of the translate of `ψ` by `η`. 

### `integral_classCutoff_integral_mul`

 **Moving the quotient by `U_c` from `G(F_∞)` to `R(F_∞)`.** Suppose `V` fits the admissible
filling data `S`, and let `G(F_∞) = GInf E ε` and `R(F_∞) = Y.besselReal`. Let `y` be a form of type
`e` (`V.IsForm e y`), for an integrable continuous `e`, and of level `S.stdPrincipalLevel`. Let `W`
on `R(F_∞)` be measurable, left invariant under `U_c` and integrable over `U_c \ R(F_∞)`. Then
`∫_{U_c \ G(F_∞)} (∫_{R(F_∞)} e (g₀⁻¹ s⁻¹ x) W (s) ds) y (x, h_c) dx` equals
`∫_{U_c \ R(F_∞)} W (s) y (s g₀, h_c) ds`. 

 ### The period, class by class 

### `adelicToFin_adelicEquiv_mem_besselU`

 The finite part of a point of the unipotent group of `Y`, in the lattice basis of `S`, lies in
the Bessel unipotent group `besselU`. 

### `exists_eq_unipotent_mul_inclX`

 Suppose `V` fits `S` (`h`). Let `k` be a point of `Y.besselFin` that lies in the principal level
`S.stdPrincipalLevel`. Then `(1, k) = u * Y.inclX (1, a)` for some `a` in the level `S.sourceLevel`
and some `u` in the unipotent subgroup `Y.unipotent` of the grading with `h.besselChar u = 1`. 

### `sourceFn_mul_of_mem_stdPrincipalLevel`

 Suppose `V` fits `S` (`h`), `S` is admissible and `ȷ c = -(M ϖ)⁻¹`, with `ȷ = WeilData.j`,
`c = Y.genericConst`, `M = S.M`, `ϖ = S.deltaE`. Let `t` be a linear functional and `ψ` an algebraic
form fixed by `S.sourceLevel`. Let `𝒲 = Y.sourceFn t (algFormRep kw 0 η ψ)`, built from the
translate of `ψ` by `η`. Then `𝒲 (r * Y.besselProdEquiv (1, k)) = 𝒲 (r)` for `r` in `Y.besselGroup`
and `k` in `Y.besselFin` lying in the principal level `S.stdPrincipalLevel`. 

### `exists_ratBessel_mul_mem_coset`

 Suppose `V` fits `S` (`h`) and `S` is admissible. Every point `r` of the Bessel group
`Y.besselGroup` can be moved by a rational point `γ` of `Y.ratBessel` so that the finite part of
`γ * r` lies in `h_c J` for some `c` in `S.Classes`. 

### `eq_and_exists_classUnipotent_of_mem_coset`

 Let `c`, `d` be classes, `J = S.stdPrincipalLevel` the principal level, and
`U_c = S.classUnipotent c`. Suppose the finite part of `g` lies in `h.classPoint d * J`, `γ` is in
`Y.ratBessel`, and the finite part of `γ g` lies in `h.classPoint c * J`. Then `c = d` and
`γ = h.ratEquiv u` for some `u` in `U_c`. 

### `classWeight`

 The weight on `R(𝔸)` that is `β_c (r_∞)` if `r_fin` lies in `h_c J` and zero otherwise, where
`β_c` is the cutoff of the class `c`. 

### `measurable_classWeight`

 For each class `c`, the weight `h.classWeight c` on the Bessel group `Y.besselGroup` is a
measurable function. 

### `isCutoff_sum_classWeight`

 Suppose `V` fits `S` (`h`). The sum over classes `c` of `h.classWeight c r` is a cutoff for the
action of `R(F) = Y.ratBessel` on `R(𝔸) = Y.besselGroup`: it is measurable and sums to 1 over each
`R(F)`-orbit. 

### `exists_integral_besselMeasure_eq_sum`

 **The quotient `[R] / J'` is the disjoint union of the `U_c \ R(F_∞)`.** Suppose `V` fits the
admissible filling data `S`.

There is a constant `volJ' ≠ 0` such that, with `J' = R(𝔸_fin) ∩ J` and `R(𝔸_fin) = Y.besselFin`,
the following holds for every measurable function `F` on `R(𝔸)` that is left invariant under `R(F)`,
right invariant under `J'` and integrable over `[R]`. Each function `s ↦ F (s, h_c)` is integrable
over `U_c \ R(F_∞)`, and `∫_{[R]} F = volJ' ∑_c ∫_{U_c \ R(F_∞)} F (s, h_c) ds`. 

 ### The series represents the period 

### `sourceFormCoords_apply`

 The coordinate `(c, i)` of a source form `ψ` is the `i`-th coordinate of its value at the
representative of the class `c`. 

### `exists_integral_poincareSeries_eq_period`

 **The Poincaré series represents a Bessel period.** Suppose `V` with the grading `Y` fits the
admissible filling data `S`: the type, the indexing and the lattice of `V` agree with those of `S`,
up to the central element `η` of `H(𝔸_fin)`. Let `ȷ Y.genericConst = -(M ϖ)⁻¹`, with
`ȷ = WeilData.j`, `M = S.M` and `ϖ = S.deltaE`, so that the character of the filling data is `ψ_U`.
There are a real point `g₀` and a linear form `t` with `∫_{[G]} y · 𝒫 ψ = ∫_{[R]} 𝒲 (r) y (r g₀) dr`
for every source form `ψ` and every form `y` of the conjugate type and principal level. Here `𝒫 ψ`
is the series over `G(F)` of the Bessel function, with coefficients the values
`h.sourceFormCoords ψ` of `ψ` at the class representatives, and `𝒲` is `sourceFn t` of the translate
of `ψ` by `η`. 

### `exists_poincareAt_eq_poincareMap_comp`

 Let `D` be admissible data for the parameters `P`. They give the CM field `D.E`, the hermitian
spaces `X₀` and `Y₀`, the source forms and the filling data `D.filling` with their Bessel function.
For a real point `g` of the unitary group of `Y₀` and a linear form `t` on the space of values of
the source forms, `D.poincareAt g t φ` is the form on `Y₀` of the chosen type and level whose
Petersson product with every such form is the Bessel period of the source form `φ` (Riesz
representation). There are `g` and `t` such that, for every `φ`, it is the Poincaré series of the
Bessel function with the coefficients `D.sourceFormCoords φ`: the values at the class
representatives of the translate of `φ` by the central element `D.latticeScale 0`, in the
coordinates of the Bessel function. 

### `besselPoint`

 A chosen real point `g` at which, for a suitable linear form `t`, the form `D.poincareAt g t φ`
that represents the Bessel period of every source form `φ` is the Poincaré series of the Bessel
function. 

### `besselForm`

 A chosen linear form for which, at the point `D.besselPoint`, the Bessel period is represented
by the Poincaré series. 

### `poincare`

 The Poincaré map at the chosen point `besselPoint` and linear form `besselForm`: it sends a
source form to the form on `Y₀` that represents its Bessel period, which for this choice is the
Poincaré series of the Bessel function. 

### `poincare_eq_poincareMap_comp`

 The Poincaré map sends a source form `φ` to the Poincaré series of the Bessel function with the
coefficients `D.sourceFormCoords φ`, the values at the class representatives of the central
translate of `φ` by `D.latticeScale 0`. 
