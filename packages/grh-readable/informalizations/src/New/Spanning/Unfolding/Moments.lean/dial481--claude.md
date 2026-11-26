---
{
  "module": "src/New/Spanning/Unfolding/Moments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The second moments of the operators `P* s P`, and good forms

Let `S` be admissible filling data, with size parameter `b = S.b`. The finite group
`Ḡ = S.ResidueGL` has one factor for each of the two level primes `p_i = S.levelPrime i`, and
`R̄₀ = S.reducedImage besselS` is the image of the Bessel subgroup in it. The source is the space of
dimension `D_X = S.sourceDim` with coordinates indexed by the classes and the coordinates of the
Bessel function. For a map `P` from the source to a representation `ρ` of `Ḡ` put `P_s = P* ρ(s) P`;
all norms of operators are Hilbert–Schmidt norms. The file proves the two moment bounds for the
`P_s`, and deduces that `e₀ P` is almost an isometry for the projection `e₀` onto the target forms.
We write `𝒟_id = S.identitySecondMoment` and `𝒟_main = S.mainSecondMoment`.

## Main definitions and results

* `New.Filling.HasAmplitudeBlocks`: the blocks of `P_s` are the conjugates of the amplitude sums,
  divided by the covolume.
* `New.Filling.besselTranslate`: the unitary representation `r_ψ` of `R̄₀` on the source, extended
  by `0`.
* `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sub_besselTranslate_sq_le`: over `R̄₀`
  times one factor of `Ḡ`, `∑ ‖P_s - r_ψ(s)‖² ≤ b⁻¹² 𝒟_id`.
* `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sub_one_sq_le`: `‖P* P - 1‖² ≤ b⁻¹² D_X`.
* `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le`: `∑ ‖P_s‖² ≤ (1 + 9 b⁻⁴) 𝒟_main`
  over `Ḡ`.
* `New.Filling.HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp`: `e₀ P` is almost an isometry in
  mean square, with the error `5 b⁻⁴`.

Notions from other files:
* `New.Filling.reduction`: the homomorphism from the stabilizer `K = S.latticeStabilizer` of the
  lattice to `Ḡ` that reduces matrix entries modulo the chosen places above `p₀` and `p₁`.
* `New.Filling.termsOver`: the terms over a block `(c, s, c')`, the rational `γ` such that
  `h_c⁻¹ γ h_c'` lies in `K` and has reduction `s`.
* `New.Filling.amplitudeSum`: the sum of the amplitudes of the terms of a set over a block.
* `New.Filling.identitySecondMoment`, `New.Filling.mainSecondMoment`: the numbers `#R̄₀ · D_X` and
  `D_X² / (deg · mass)`, with `deg = S.besselDegree` and the mass `New.mass` of the genus of the
  standard lattice of rank `r`.

## Relation to the literature

For the normalised Poincaré map `P`, the mean over level translates `s` of `‖P* s P‖²` is at most
nearly `D_X² / D₀`, with `D₀` the expected dimension of the target, and bad types carry little of
`P`. In rank one, Poisson summation on a product of two Kloosterman sides with a sharp diagonal term
is known in the literature. Related work: Herman, Beyond endoscopy for the Rankin–Selberg
L-function, 2011; Iwaniec–Li, The orthogonality of Hecke eigenvalues, 2007;
Michel–Ramakrishnan–Yang, Bessel periods on U(2,1)×U(1,1), 2023.

See `New.Spanning.SecondMoment.SpanningTheorem` and `New.Spanning.RemainingTerms.Sum` for related
work.



## The operators `P_s` and `r_ψ(s)`, and the second moments

In statements about `P`, `ρ` is a representation of `Ḡ`, unitary where stated, on a space of finite
dimension.


### `_root_.New.IsCentralProj.isSymmetricProjection`

 In a unitary representation `ρ` of a finite group, a central idempotent `z` of the group algebra
(an idempotent whose coefficients form a class function) acts as an orthogonal projection. 

### `HasAmplitudeBlocks`

 Let `Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields at the
chosen places of `S`. The source is the Euclidean space with coordinates `(c, i)`, where `c` is a
class (a double coset of the definite unitary group `U(X₀)` for the level) and `i` is a coordinate
of the Bessel function `W` at the infinite places. For a representation `ρ` of `Ḡ` on `V` and a
linear map `P` from the source to `V`, this says that the block `(c, c')` of `P_s = P* ρ(s) P` is
the complex conjugate of `A(c, s, c') / ν`. Here `ν = unipotentCovolume`, and
`A(c, s, c') = amplitudeSum .full .univ c s c'` is the sum of the amplitudes
`∫ β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^* dy` over all terms, the rational `γ` such that
`h_c⁻¹ γ h_c'` is integral with reduction `s`; `h_c` represents the class `c` and
`β_c = classCutoff c`. This holds for the Poincaré map after scaling. 

### `hasAmplitudeBlocks_smul_of_inner_eq`

 Let `S` be filling data for a unitary group over the CM field `E`, and `Ḡ = S.ResidueGL` the
product of the general linear groups over the residue fields at the chosen places. Let `ρ` be a
representation of `Ḡ` on `V` and `P` a linear map to `V` from the Euclidean space with basis `e_x`,
where `x` is a pair of a class (a double coset of the definite unitary group `U(X₀)` for the level)
and a coordinate of the Bessel function `W` at the infinite places. Suppose that
`⟪ρ(s) P e_y, P e_x⟫` is `c > 0` times the entry of `amplitudeSum .full .univ`, the sum over all
rational terms of the amplitude integrals of the uncut function `W`. Then `(c ν) ^ (-1/2) P`
satisfies `HasAmplitudeBlocks`, the same identity with `ν⁻¹` in place of `c`, where
`ν = S.unipotentCovolume > 0`. 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_sq_eq_secondMoment`

 Let `S` be filling data (`Filling`) for a unitary group `G` over the CM field `E`, and let
`Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields at the chosen
places above the two level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates
`(c, i)`, where `c` is a class (a double coset of the definite unitary group `U(X₀)` for the level)
and `i` is a coordinate of the Bessel function `W` at the infinite places. Let `ρ` be a
representation of `Ḡ` on `V` and `P` a linear map from the source to `V`. Suppose
`HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the conjugate of
`A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum, over the
rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral of
`W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Then the squared
Hilbert–Schmidt norm of `P_s` is `∑ ‖A(c, s, c')‖² / ν²` over pairs of classes, the second moment at
`s` of all terms (`.univ`) for the uncut function `W` (`.full`). 

### `besselTranslate`

 The operator `r_ψ(s)` on the source: its blocks are the complex conjugates of the sums of
amplitudes (`amplitudeSum`) of the terms in the Bessel subgroup, divided by `unipotentCovolume`. For
`s` in the image `R̄₀` of the Bessel subgroup it is the translation by `s`, twisted by the
character: each class `c` has a term of the Bessel subgroup over some block `(c, s, c')`
(`exists_besselS_mem_termsOver`), its matrix is given by `besselFn_mul_of_eq_embedH`, and
`besselTranslate_apply` gives the value of the operator. 

### `besselTranslate_eq_zero`

 The operator `r_ψ(s) = besselTranslate s`, whose blocks are sums over rational elements of the
Bessel subgroup with reduction `s`, vanishes for `s` off the image of that subgroup in
`S.ResidueGL`. 

### `besselTranslate_apply`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. Let
`r_ψ(s) = S.besselTranslate s` be the operator on the source `ℂ^(classes × Bessel coordinates)`
whose blocks are the complex conjugates of the normalised amplitude sums of the rational elements of
the Bessel subgroup `besselS`. Let `γ` be a rational element of that subgroup over the block
`(c, s, c')`: `h_c⁻¹ γ h_c'` is integral with reduction `s`, where `h_c` represents the class `c`.
Suppose `W(γ y) = M W(y)` for all points `y` of `G` at the infinite places, where
`W = S.besselFn .full` is the vector of Bessel functions. Then the value of `r_ψ(s) φ` at the class
`c` is the entrywise conjugate of `M` applied to the value of `φ` at `c'`. 

### `besselTranslate_one`

 For admissible filling data `S` over a CM field `E` with a primitive `5040`-th root of unity,
the operator `r_ψ(1) = besselTranslate 1` is the identity. 

### `besselTranslate_mul`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. Then
`r_ψ(s t) = r_ψ(s) r_ψ(t)` for `s` and `t` in `R̄₀`. 

### `besselTranslate_mul_left`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. Then
`r_ψ(t s) = r_ψ(t) r_ψ(s)` for `t` in `R̄₀` and every `s` in `Ḡ`. 

### `adjoint_besselTranslate`

 Let `S` be admissible filling data over a CM field `E` with a primitive `5040`-th root of unity.
The adjoint of `r_ψ(s) = besselTranslate s` is `r_ψ(s⁻¹)`. So, by `besselTranslate_mul` and
`besselTranslate_one`, `r_ψ` is a unitary representation of the image of the Bessel subgroup. 

### `hilbertSchmidtNorm_besselTranslate_comp`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. For `t`
in `R̄₀` the operator `r_ψ(t)` is unitary, so composing an operator `A` of the source on the left
with it does not change the Hilbert–Schmidt norm. 

### `trace_besselTranslate`

 Let `S` be admissible filling data over a CM field `E` with a primitive `5040`-th root of unity.
The trace of `r_ψ(s) = besselTranslate s` is a sum over classes `c` and Bessel coordinates `i`. Each
summand is the `(i, i)` entry of the full amplitude sum `amplitudeSum` of the terms in the Bessel
subgroup `besselS` over the block `(c, s⁻¹, c)`, divided by `unipotentCovolume`. 

### `HasAmplitudeBlocks.adjoint_comp_rep_mul_right`

 Equivariance on the right. Let `S` be admissible filling data for a unitary group `G` over the
CM field `E`, which contains a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the
product of the general linear groups over the residue fields at the chosen places above the two
level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates `(c, i)`, where `c` is a
class (a double coset of the definite unitary group `U(X₀)` for the level) and `i` is a coordinate
of the Bessel function `W` at the infinite places. Let `ρ` be a representation of `Ḡ` on `V` and `P`
a linear map from the source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of
`P_s = P* ρ(s) P` is the conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and
`A(c, s, c')` is the sum, over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with
reduction `s`, of an integral of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class
`c`). Let `r_ψ(s) = S.besselTranslate s` be the operator on the source with the same blocks, but
summed only over the `γ` in the Bessel subgroup `besselS` (block unitriangular elements times
`U(X₀)`), and let `R̄₀` be the image of that subgroup in `Ḡ`. Then `P_(s t) = P_s r_ψ(t)` for `t` in
`R̄₀`. 

### `HasAmplitudeBlocks.rep_comp_eq_comp_besselTranslate`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a double coset of the
definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the Bessel function `W` at
the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V` and `P` a linear map from the
source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the
conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum,
over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral
of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let
`r_ψ(s) = S.besselTranslate s` be the operator on the source with the same blocks, but summed only
over the `γ` in the Bessel subgroup `besselS` (block unitriangular elements times `U(X₀)`), and let
`R̄₀` be the image of that subgroup in `Ḡ`. Then `ρ(t) P = P r_ψ(t)` for `t` in `R̄₀`. 

### `HasAmplitudeBlocks.adjoint_comp_rep_mul_left`

 Equivariance on the left. Let `S` be admissible filling data for a unitary group `G` over the CM
field `E`, which contains a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the
product of the general linear groups over the residue fields at the chosen places above the two
level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates `(c, i)`, where `c` is a
class (a double coset of the definite unitary group `U(X₀)` for the level) and `i` is a coordinate
of the Bessel function `W` at the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V`
and `P` a linear map from the source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of
`P_s = P* ρ(s) P` is the conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and
`A(c, s, c')` is the sum, over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with
reduction `s`, of an integral of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class
`c`). Let `r_ψ(s) = S.besselTranslate s` be the operator on the source with the same blocks, but
summed only over the `γ` in the Bessel subgroup `besselS` (block unitriangular elements times
`U(X₀)`), and let `R̄₀` be the image of that subgroup in `Ḡ`. Then `P_(t s) = r_ψ(t) P_s` for `t` in
`R̄₀`. 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_sub_besselTranslate_sq`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which contains
a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`. Suppose `HasAmplitudeBlocks`: the block
`(c, c')` of `P_s = P* ρ(s) P` is the conjugate of `A(c, s, c') / ν`, where
`ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum, over the rational `γ` in `G` such that
`h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs
(`h_c` represents the class `c`). Then the squared Hilbert–Schmidt norm of `P_s - r_ψ(s)` is the
second moment `∑ ‖A'(c, s, c')‖² / ν²` over pairs of classes, where `A'` is summed over the `γ`
outside the Bessel subgroup and `‖·‖` is the Euclidean norm of the entries. 

### `HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sub_besselTranslate_sq_le`

 **Second moment near the Bessel subgroup.** Let `S` be admissible filling data for a unitary
group `G` over the CM field `E`, which contains a primitive `5040`-th root of unity, and let
`Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields at the chosen
places above the two level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates
`(c, i)`, where `c` is a class (a double coset of the definite unitary group `U(X₀)` for the level)
and `i` is a coordinate of the Bessel function `W` at the infinite places. Let `ρ` be a
representation of `Ḡ` on `V` and `P` a linear map from the source to `V`. Suppose
`HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the conjugate of
`A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum, over the
rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral of
`W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let
`r_ψ(s) = S.besselTranslate s` be the operator on the source with the same blocks, but summed only
over the `γ` in the Bessel subgroup `besselS` (block unitriangular elements times `U(X₀)`), and let
`R̄₀` be the image of that subgroup in `Ḡ`. Then `∑ ‖P_s - r_ψ(s)‖² ≤ b⁻¹² 𝒟_id` in Hilbert–Schmidt
norm, the sum being over the `s` that coincide with an element of `R̄₀` above the prime `p_(i+1)`
other than `p_i`. Here `b = S.b ≥ 1000` is the size parameter of `S`, and
`𝒟_id = S.identitySecondMoment` is `#R̄₀` times the dimension of the source. 

### `le_sourceDim_div_of_card_nsmul_le`

 If `#R̄₀ · y ≤ b⁻¹² 𝒟_id`, then `y ≤ b⁻¹² D_X`. Here `R̄₀` is the image of the Bessel subgroup
in `S.ResidueGL`, `b = S.b`, `D_X = sourceDim` and `𝒟_id = identitySecondMoment = #R̄₀ · D_X`. 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_sub_one_sq_le`

 **Near isometry.** Let `S` be admissible filling data for a unitary group `G` over the CM field
`E`, which contains a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the product of
the general linear groups over the residue fields at the chosen places above the two level primes
`p₀`, `p₁`. The source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a
double coset of the definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the
Bessel function `W` at the infinite places. Let `ρ` be a representation of `Ḡ` on `V` and `P` a
linear map from the source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of
`P_s = P* ρ(s) P` is the conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and
`A(c, s, c')` is the sum, over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with
reduction `s`, of an integral of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class
`c`). Then `‖P* P - 1‖² ≤ b⁻¹² D_X` in Hilbert–Schmidt norm, where `D_X = S.sourceDim` is the
dimension of the source and `b = S.b ≥ 1000` is the size parameter of `S`. 

### `hilbertSchmidtNorm_one_sq_eq_sourceDim`

 The identity of the source has squared Hilbert–Schmidt norm `D_X = sourceDim`. 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_adjoint_comp_sq_le`

 Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary group `G` over the
CM field `E`, which contains a primitive `5040`-th root of unity, and let `Ḡ = S.ResidueGL` be the
product of the general linear groups over the residue fields at the chosen places above the two
level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates `(c, i)`, where `c` is a
class (a double coset of the definite unitary group `U(X₀)` for the level) and `i` is a coordinate
of the Bessel function `W` at the infinite places. Let `ρ` be a representation of `Ḡ` on `V` and `P`
a linear map from the source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of
`P_s = P* ρ(s) P` is the conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and
`A(c, s, c')` is the sum, over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with
reduction `s`, of an integral of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class
`c`). Then `‖P* P‖² ≤ 2 D_X` in Hilbert–Schmidt norm, where `D_X = S.sourceDim` is the dimension of
the source. 

### `HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le`

 **Second moment.** Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary
group `G` over the CM field `E`, which carries Weil data (a primitive `5040`-th root of unity and a
splitting character, see `WeilData`), and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a double coset of the
definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the Bessel function `W` at
the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V` and `P` a linear map from the
source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the
conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum,
over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral
of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Then
`∑ ‖P_s‖² ≤ (1 + 9 b⁻⁴) 𝒟_main` in Hilbert–Schmidt norm, the sum being over all `s` in `Ḡ`. Here
`b = S.b ≥ 1000` is the size parameter of `S`, and `𝒟_main = S.mainSecondMoment` is the square of
the dimension of the source divided by the product of `S.besselDegree` (the product of the degree
constants of the local Bessel systems) and `New.mass` (the sum of `1 / #Aut` over the genus of the
standard lattice). 

 ## Good forms: the remainder 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_sum_smul_sub_besselTranslate_sq_le`

 **The remainder.** Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary
group `G` over the CM field `E`, which contains a primitive `5040`-th root of unity, and let
`Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields at the chosen
places above the two level primes `p₀`, `p₁`. The source is the Euclidean space with coordinates
`(c, i)`, where `c` is a class (a double coset of the definite unitary group `U(X₀)` for the level)
and `i` is a coordinate of the Bessel function `W` at the infinite places. Let `ρ` be a unitary
representation of `Ḡ` on `V` and `P` a linear map from the source to `V`. Suppose
`HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the conjugate of
`A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum, over the
rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral of
`W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let
`r_ψ(s) = S.besselTranslate s` be the operator on the source with the same blocks, but summed only
over the `γ` in the Bessel subgroup `besselS` (block unitriangular elements times `U(X₀)`). Write
`Ḡ = G_0 × G_1`, where `G_i` is the factor above `p_i`, made of matrices indexed by the basis
`𝔰.BesselIndex` of the hermitian space of shape `𝔰`, and embedded by `Pi.mulSingle i`. Then for a
central idempotent `x = ∑ x(t) t` of `ℂ[G_i]` (an idempotent whose coefficients form a class
function; it is then self-adjoint) we have `‖∑ x(t) (P_t - r_ψ(t))‖² ≤ b⁻¹² D_X` in Hilbert–Schmidt
norm, the sum being over `t` in `G_i`. Here `b = S.b ≥ 1000` is the size parameter of `S` and
`D_X = S.sourceDim` is the dimension of the source. 

 ## Good forms: the trace of `r_ψ` against a central idempotent of one factor 

### `sum_norm_sq_coeff_of_isCentralProj`

 For a finite group `G` and a central idempotent `x` of the complex group algebra
`MonoidAlgebra ℂ G` (`IsCentralProj x`), `∑ s, ‖x.coeff s‖² = (x.coeff 1).re`. 

### `mem_besselU_of_reduction_eq_one`

 Let `S` be admissible filling data over a CM field `E` with Weil data. Let `γ` be in the Bessel
subgroup and `k = translateByClassReps c c γ`, that is `h_c⁻¹ γ h_c` for the representative `h_c` of
the class `c`. If `k` lies in the stabilizer `latticeStabilizer` of the lattice and reduces to `1`
at the chosen places above the level prime `p_j`, then `k` lies in the unipotent subgroup
`besselU`. 

### `reducedChar`

 The character `ψ_U` on the image `Ū₀` of the integral unipotent elements in the finite group
`S.ResidueGL`, extended by `0`. Its value at `s` is `S.unipotentChar k` for a unipotent `k` that
reduces to `s`; the choice does not matter (`extendedBesselChar_toPlaces_eq_reducedChar`). 

### `reducedCharMean`

 The mean `ψ_U^♮(s)` of `ψ_U = reducedChar`, extended by `0`, over the conjugates of `s` in the
finite group `S.ResidueGL`. 

### `reducedCharMean_conj`

 The mean `ψ_U^♮` of `ψ_U` over conjugates is a class function. 

### `trace_besselTranslate_eq_mul_reducedChar`

 Let `S` be admissible filling data over a CM field `E` with Weil data, and let `s` in
`S.ResidueGL` be `1` above the level prime `p_j`. The trace of `r_ψ(s) = S.besselTranslate s`, the
translation of the source by `s` twisted by the Bessel character, is `D_X ψ_U(s)`. Here
`D_X = S.sourceDim` and `ψ_U = S.reducedChar` is the character of the integral unipotent group, read
on reductions and extended by `0` off its image. 

### `extendedBesselChar_toPlaces_eq_reducedChar`

 Let `S` be filling data for a unitary group `G` over the CM field `E`, with level primes `p₀`,
`p₁`, and let `Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields
at the chosen places above them. Let `M = p₀ p₁`, and let `T` be a finite conjugation-stable set of
finite places off which `M⁻¹` is integral, so that `T` contains the places above `M`. Over the
product `LocProd T` of the completions at `T`, let `K` be the group of integral points of `G` and
`K(M)` its principal congruence subgroup of level `M`. Let `F` be a filling datum (`IsFillingData`):
a large lattice datum with `3ϱ + 6` hyperbolic pairs and `k - (6ϱ + 13)` orthonormal vectors, for
the ranks `ϱ = 𝔰.ϱ` and `k = 𝔰.k` of the shape, with modulus `F.levelUnit = M` and local character
`ψ(x) = ψ_f(-x / ϖ)`, where `ϖ` generates the different. The function
`χ_M = extendedBesselChar F.levelUnit` is `ψ(σ(u) / M)` on `u K(M)` for `u` in the block
unitriangular group `𝖴 = besselU`, with `σ(u)` the sum of the entries at the simple roots, and `0`
off `𝖴 K(M)`. Then for `l` in the stabilizer of the lattice, `χ_M` at the component of `l` at `T` is
`ψ_U` at the reduction of `l`, where `ψ_U = S.reducedChar` is the character `u ↦ ψ_f(-σ(u) / (M ϖ))`
of the integral points of `𝖴`, read on their reductions in `Ḡ` and extended by `0`. 

### `integral_extendedBesselChar_conj_eq`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, and let
`Ḡ = S.ResidueGL` be the product of the general linear groups over the residue fields at the chosen
places above the two level primes `p₀`, `p₁`. Let `M = p₀ p₁`, and let `T` be a finite
conjugation-stable set of finite places off which `M⁻¹` is integral, so that `T` contains the places
above `M`. Over the product `LocProd T` of the completions at `T`, let `K` be the group of integral
points of `G` and `K(M)` its principal congruence subgroup of level `M`. Let `F` be a filling datum
(`IsFillingData`): a large lattice datum with `3ϱ + 6` hyperbolic pairs and `k - (6ϱ + 13)`
orthonormal vectors, for the ranks `ϱ = 𝔰.ϱ` and `k = 𝔰.k` of the shape, with modulus
`F.levelUnit = M` and local character `ψ(x) = ψ_f(-x / ϖ)`, where `ϖ` generates the different. The
function `χ_M = extendedBesselChar F.levelUnit` is `ψ(σ(u) / M)` on `u K(M)` for `u` in the block
unitriangular group `𝖴 = besselU`, with `σ(u)` the sum of the entries at the simple roots, and `0`
off `𝖴 K(M)`. Then for `l` in the stabilizer of the lattice, `∫_K χ_M(y l y⁻¹) dy` for the measure
`dy = F.groupMeasure` is `vol(K)` times the value at the reduction of `l` of `S.reducedCharMean`,
the mean of `ψ_U` over conjugates. Here `ψ_U = S.reducedChar` is the character
`u ↦ ψ_f(-σ(u) / (M ϖ))` of the integral points of `𝖴`, read on their reductions in `Ḡ` and extended
by `0`. 

### `sum_sq_norm_integral_extendedBesselChar_conjugate_le`

 Let `S` be admissible filling data for a unitary group `G` over the CM field `E`, which carries
Weil data, and let `Ḡ = S.ResidueGL` be the product of the general linear groups over the residue
fields at the chosen places above the two level primes `p₀`, `p₁`. Let `M = p₀ p₁`, and let `T` be a
finite conjugation-stable set of finite places off which `M⁻¹` is integral, so that `T` contains the
places above `M`. Over the product `LocProd T` of the completions at `T`, let `K` be the group of
integral points of `G` and `K(M)` its principal congruence subgroup of level `M`. Let `F` be a
filling datum (`IsFillingData`): a large lattice datum with `3ϱ + 6` hyperbolic pairs and
`k - (6ϱ + 13)` orthonormal vectors, for the ranks `ϱ = 𝔰.ϱ` and `k = 𝔰.k` of the shape, with
modulus `F.levelUnit = M` and local character `ψ(x) = ψ_f(-x / ϖ)`, where `ϖ` generates the
different. The function `χ_M = extendedBesselChar F.levelUnit` is `ψ(τ(u) / M)` on `u K(M)` for `u`
in the block unitriangular group `𝖴 = besselU`, with `τ(u)` the sum of the entries at the simple
roots, and `0` off `𝖴 K(M)`. Suppose that `T` consists of chosen places and their conjugates, and
put `a z = ∫_K χ_M(y z y⁻¹) dy` for the measure `dy = F.groupMeasure`. For a finite family `σ` in
the stabilizer of the lattice whose members have different reductions in `Ḡ` we have
`∑ |a (σ s)|² ≤ 2 vol(K)²`, where `a` is evaluated at the component of `σ s` at `T`. 

### `inv_ideleM_mem_integralOff`

 Let `S` be filling data over the CM field `E`, with level primes `p₀`, `p₁` and, for each `p_i`,
a chosen set `S.chosenPlaces i` of places of norm `p_i`, such that the chosen places and their
conjugates have product `M = p₀ p₁`. If a finite set `T` of finite places contains all of these,
then the inverse of the finite idele `S.ideleM` of `M` is integral off `T`. 

### `sum_norm_reducedCharMean_sq_le`

 **The induced character.** Let `S` be admissible filling data for a unitary group `G` over the
CM field `E`, which carries Weil data, and let `Ḡ = S.ResidueGL` be the product of the general
linear groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`.
Let `ψ_U = S.reducedChar` be the additive character (`unipotentChar`) of the integral block
unitriangular elements of `G`, read on their reductions in `Ḡ` and extended by `0`, and let
`ψ_U^♮(s) = S.reducedCharMean s` be its mean over the conjugates of `s`. Then `∑ |ψ_U^♮(s)|² ≤ 2`,
the sum being over all `s` in `Ḡ`. 

### `re_sum_coeff_mul_trace_besselTranslate_le`

 **The trace.** Let `S` be admissible filling data for a unitary group `G` over the CM field `E`,
which carries Weil data, and let `Ḡ = S.ResidueGL` be the product of the general linear groups over
the residue fields at the chosen places above the two level primes `p₀`, `p₁`. Let
`r_ψ(s) = S.besselTranslate s` be the operator on the source `ℂ^(classes × Bessel coordinates)`
whose blocks are the complex conjugates of the normalised amplitude sums of the rational elements of
the Bessel subgroup `besselS`. Let `x` be a central idempotent of the group algebra of the factor of
`Ḡ` above `p_i`, made of matrices indexed by the basis `𝔰.BesselIndex` of the hermitian space, with
`Re x(1) ≤ b⁻⁸ / 2`. Then the trace of `r_ψ(x) = ∑ x(s) r_ψ(s)` has real part at most `b⁻⁴ D_X`. 

 ## Good forms: one prime and both primes 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_asAlgebraHom_comp_sq_le`

 **One prime.** Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary
group `G` over the CM field `E`, which carries Weil data (a primitive `5040`-th root of unity and a
splitting character, see `WeilData`), and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a double coset of the
definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the Bessel function `W` at
the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V` and `P` a linear map from the
source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the
conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum,
over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral
of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let `x` be a central
idempotent (an idempotent whose coefficients form a class function; it is then self-adjoint) of the
group algebra of the factor of `Ḡ` above `p_i`, made of matrices indexed by the basis
`𝔰.BesselIndex` of the hermitian space, with `Re x(1) ≤ b⁻⁸ / 2`, where `b = S.b ≥ 1000` is the size
parameter of `S`. Then `‖x P‖² ≤ 2 b⁻⁴ D_X` in Hilbert–Schmidt norm, where `x` acts on `V` through
`ρ` and `D_X = S.sourceDim` is the dimension of the source. 

### `finrank_source_eq_sourceDim`

 The source has dimension `D_X = S.sourceDim`. 

### `HasAmplitudeBlocks.hilbertSchmidtNorm_one_sub_piTensorElem_comp_sq_le`

 **Both primes.** Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary
group `G` over the CM field `E`, which carries Weil data (a primitive `5040`-th root of unity and a
splitting character, see `WeilData`), and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a double coset of the
definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the Bessel function `W` at
the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V` and `P` a linear map from the
source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the
conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum,
over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral
of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let `g_i` be a central
idempotent (an idempotent whose coefficients form a class function; it is then self-adjoint) of the
group algebra of the factor of `Ḡ` above `p_i`, such that the coefficient of `1 - g_i` at `1` has
real part at most `b⁻⁸ / 2`, where `b = S.b ≥ 1000` is the size parameter of `S`. Let
`e₀ = piTensorElem g` be the tensor product `g₀ ⊗ g₁` in `ℂ[Ḡ]`, acting on `V` through `ρ`. Then
`‖(1 - e₀) P‖² ≤ 4 b⁻⁴ D_X` in Hilbert–Schmidt norm, where `D_X = S.sourceDim` is the dimension of
the source. 

### `HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp`

 **Good forms.** Let `S` be admissible filling data (`Filling`, `IsAdmissible`) for a unitary
group `G` over the CM field `E`, which carries Weil data (a primitive `5040`-th root of unity and a
splitting character, see `WeilData`), and let `Ḡ = S.ResidueGL` be the product of the general linear
groups over the residue fields at the chosen places above the two level primes `p₀`, `p₁`. The
source is the Euclidean space with coordinates `(c, i)`, where `c` is a class (a double coset of the
definite unitary group `U(X₀)` for the level) and `i` is a coordinate of the Bessel function `W` at
the infinite places. Let `ρ` be a unitary representation of `Ḡ` on `V` and `P` a linear map from the
source to `V`. Suppose `HasAmplitudeBlocks`: the block `(c, c')` of `P_s = P* ρ(s) P` is the
conjugate of `A(c, s, c') / ν`, where `ν = S.unipotentCovolume > 0` and `A(c, s, c')` is the sum,
over the rational `γ` in `G` such that `h_c⁻¹ γ h_c'` is integral with reduction `s`, of an integral
of `W(y) ⊗ W(γ⁻¹ y)^*` against cutoffs (`h_c` represents the class `c`). Let `g_i` be a central
idempotent (an idempotent whose coefficients form a class function; it is then self-adjoint) of the
group algebra of the factor of `Ḡ` above `p_i`, such that the coefficient of `1 - g_i` at `1` has
real part at most `b⁻⁸ / 2`, where `b = S.b ≥ 1000` is the size parameter of `S`. Let
`e₀ = piTensorElem g` be the tensor product `g₀ ⊗ g₁` in `ℂ[Ḡ]`, acting on `V` through `ρ`. Then
`e₀ P` is almost an isometry from below in mean square (`IsNearIsometry`) with error `5 b⁻⁴`:
`‖e₀ P pr_U‖² ≥ dim U - 5 b⁻⁴ D_X` in Hilbert–Schmidt norm for every subspace `U` of the source,
where `pr_U` is the orthogonal projection onto `U` and `D_X` is the dimension of the source. 
