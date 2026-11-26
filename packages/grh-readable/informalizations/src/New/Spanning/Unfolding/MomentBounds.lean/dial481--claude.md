---
{
  "module": "src/New/Spanning/Unfolding/MomentBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The second moment over the whole group

This file proves the bound on the sum of the second moments of the operators `P_s = P* s P` over the
whole group, stated in terms of their blocks. It bounds the contribution of the cosets of `R̄₀` and
that of the elements that are not open.

The blocks of `P_s` are the complex conjugates of the sums `amplitudeSum` over all terms, divided by
`unipotentCovolume`, so `‖P_s‖²` (Hilbert–Schmidt norm) is the `secondMoment` of these sums at `s`.
In the same way the terms in the Bessel subgroup `R₀ = besselS` give `r_ψ(s)`, and those off it give
`P_s - r_ψ(s)`. The operator `r_ψ(s)` is `New.Filling.besselTranslate`; the passage from operators
to blocks is `New.Filling.HasAmplitudeBlocks`.

We write `R̄₀` for `reducedImage besselS`, `D_X` for `sourceDim`, `𝒟_id` for `identitySecondMoment`,
`𝒟_main` for `mainSecondMoment`, `b` for the parameter `S.b` of the filling, `p_i` for
`levelPrime i`, `M = p₀ p₁` for the level, `f` for the number of infinite places, `k = |κ|`,
`n = ϱ + 1` for the length of the frame, `e₁` for its vector of index `0` and `δ_l` for the leading
minors of `frameGram`. In `InScalarCoset ζ s` the scalar `ζ` is an integral adele, acting through
its residues.

## Main definitions and results

* `New.Filling.sum_secondMoment_le`: `∑ ‖P_s‖² ≤ (1 + 9 b⁻⁴) 𝒟_main`, if `s ↦ ‖P_s‖²` has positive
  type and `‖P_1‖² ≤ 2 D_X`.
* `New.Filling.secondMoment_univ_eq_secondMoment_compl_besselS`: if `Ω` is disjoint from the
  reduction `R̄₀` of the Bessel subgroup, then the terms in the Bessel subgroup give `0` over `Ω`,
  so all terms and the terms off the Bessel subgroup have the same second moment over `Ω`.

Notions from other files:
* `termsOver c s c'`: the rational `γ` such that `h_c⁻¹ γ h_c'` (`translateByClassReps`) is integral
  with reduction `s`; such a `γ` lies over the block `(c, s, c')`.
* `amplitudeSum side T c s c'`: the sum of the amplitudes of the elements of `T` over that block.
* `secondMoment A Ω`: the sum of `‖A c s c'‖² / unipotentCovolume²` over all classes `c`, `c'` and
  `s ∈ Ω`.
* `reducedImage A`: the image in the finite group `ResidueGL` of the integral elements of `A`.


 ### The second moment over the whole group 

### `secondMoment_singleton`

 The second moment of a family of blocks at one element `σ`: `unipotentCovolume⁻²` times the sum
of the squared norms of the blocks over `σ`. 

### `secondMoment_eq_sum_secondMoment_singleton`

 The second moment of a family of blocks over a set `Ω` is the sum of its second moments at the
elements of `Ω`. 

### `secondMoment_univ_eq_secondMoment_compl_besselS`

 If `Ω` is disjoint from the reduction `R̄₀` of the Bessel subgroup, then the terms in the Bessel
subgroup give `0` over `Ω`, so all terms and the terms off the Bessel subgroup have the same second
moment over `Ω`. 

### `card_inScalarCoset_le`

 At most `M ^ f #R̄₀` elements lie in a coset of the reduction `R̄₀` of the Bessel subgroup by an
integral scalar (`InScalarCoset`), as only the residues of the scalar at the chosen places
matter. 

### `pow_mul_identitySecondMoment_le_mul_mainSecondMoment`

 Let the filling `S` be admissible (`IsAdmissible`), which includes the bound
`b^(11kf) 𝒟_id ≤ 𝒟_main`. Then `b^(5kf) 𝒟_id ≤ b^(-6ka) 𝒟_main` for any set `places` of chosen
places above the level prime `p₀` (`chosenPlaces 0`), where `a = #places`. 

### `levelPrime_pow_le_meetNorm_of_mem_fixer`

 For each chosen place `w` above `p₀`, let `vectors w` be a nonzero vector of the span of the
frame modulo `w`. If its Boolean is `true`, it is taken modulo the conjugate of `w` instead. Let `s`
fix all of them. So `meetNorm s`, the product of the norms of the places at which `s` meets, is at
least `levelPrime 0 ^ numInfPlaces E`. 

### `sum_secondMoment_inScalarCoset_le`

 Let `E` contain a primitive `5040`-th root of unity and let the filling data `S` be admissible
(`IsAdmissible`). For `s` in `ResidueGL`, write `‖P_s‖²` for the `secondMoment` at `s` of the
amplitude sums of all terms. If `‖P_s‖² ≤ 2 D_X` for all `s`, with `D_X = sourceDim`, then the sum
of `‖P_s‖²` over the cosets of the reduction `R̄₀` of the Bessel subgroup by integral scalars
(`InScalarCoset`) is at most `2 M ^ f 𝒟_id`. 

### `eight_mul_M_pow_mul_identitySecondMoment_le`

 Let the filling `S` be admissible (`IsAdmissible`). Then `8 M ^ f 𝒟_id ≤ b^(-6kf) 𝒟_main`, as
`b^(11kf) 𝒟_id ≤ 𝒟_main`, `8 M ^ f ≤ b (b²³) ^ f` and `23 f + 1 ≤ 5 k f`. 

### `div_levelPrime_pow_mul_mainSecondMoment_le`

 Let the filling `S` be admissible (`IsAdmissible`). The bound `(b^(2f) / p₀^f)^k 𝒟_main` on sums
over links is at most an eighth of `b^(-6kf) 𝒟_main`, as `b¹⁰ ≤ p₀` (`le_levelPrime`). 

### `secondMoment_fixer_univ_le`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). Let `D_X = sourceDim` be the number of pairs of a class and a coordinate, and
suppose `‖P_s‖² ≤ 2 D_X` for all `s`. At each of the `f` chosen places `w` above `p₀`, `vectors w`
is a `FrameVector`: a nonzero vector in the span of the frame `e₁, …, e_ϱ, z`, taken modulo `w` or
modulo its conjugate. Then the sum over the group `fixer` of the `s` that fix all these vectors
satisfies `∑ ‖P_s‖² ≤ b^(-6kf) 𝒟_main`. 

### `secondMoment_fixer_isOpenElement_le`

 Let the filling `S` be admissible (`IsAdmissible`) and assume Weil data on `E`. Over the open
`s` that fix the given nonzero vectors of the span of the frame at a set of `a` chosen places above
`p₀` (`fixer`) we have `∑ ‖P_s‖² ≤ (1 + 4 b⁻⁴) b^(-6ka) 𝒟_main`. The element `s` is open if at some
chosen place above `p₀` no leading minor of size less than `n = ϱ + 1` of `frameGram`, the matrix of
the products of the frame with its image under `s`, vanishes. 

### `levelPrime_pow_mul_sqrt_le`

 Let the filling `S` be admissible (`IsAdmissible`). For `l < n = ϱ + 1` we have
`p₀ ^ (l + r / 2) ≤ b ^ (6 k)`. Here `p₀ = levelPrime 0`, `b = S.b`, `k = |κ|`, and `r` is the rank
of the space, that is, the number of indices in `𝔰.BesselIndex`. 

### `sum_leadingMinor_eq_zero_le`

 Let the filling `S` be admissible (`IsAdmissible`), with large parameter `b = S.b` and with
`k = 𝔰.k` the rank of `X₀`. Let `β ≥ 0` on `ResidueGL` have positive type. Let `Γ` be a subgroup and
`w` a chosen place above `p₀`. The frame consists of the `ϱ + 1` basis vectors `e₁, …, e_ϱ, z`, and
a `FrameVector` at `w` is a nonzero vector of their span, taken modulo `w` or modulo its conjugate.
Suppose that the stabilizer in `Γ` of any such vector carries at most a proportion `b^(-6k)` of the
sum of `β` over `Γ`. Let `l < 𝔰.n`, and let `δ_l` be the leading minor of size `l` of the
`frameGram` of the component `s 0 w` over the residue field at `w`. Then the `s` in `Γ` with
`δ_l = 0` carry at most a proportion `3 / b¹⁰`. 

### `sum_not_isOpenElement_le`

 Let the filling `S` be admissible (`IsAdmissible`), with `k = 𝔰.k` the rank of `X₀` and `S.b`
its large parameter. Let `β ≥ 0` on `ResidueGL` have positive type: `β (a⁻¹ * b) = ⟪u a, u b⟫` for
all `a`, `b`, for a map `u` into an inner product space. Let `Γ` be a subgroup of `ResidueGL` and
`w` a chosen place above `p₀`. Suppose that for every nonzero vector of the span of the frame,
modulo `w` or its conjugate, the elements of `Γ` that fix it (`vectorFixer`) carry at most a
proportion `S.b^(-6k)` of the sum of `β` over `Γ`. Then the elements of `Γ` that are not open carry
at most a proportion `S.b⁻⁴` of that sum. 

### `le_one_add_nine_mul_of_le_add`

 If `M ≤ (1 + 4 x) C + x M` with `0 ≤ x ≤ 1/10` and `C ≥ 0`, then `M ≤ (1 + 9 x) C`. 

### `sum_secondMoment_le`

 Let the filling `S` over the CM field `E` be admissible (`IsAdmissible`) and assume Weil data on
`E`, which include a primitive `5040`-th root of unity. If `s ↦ ‖P_s‖²` has positive type, that is,
`‖P_(x⁻¹ y)‖² = ⟪u x, u y⟫` for vectors `u x` of an inner product space, and `‖P_1‖² ≤ 2 D_X`, then
`∑ ‖P_s‖² ≤ (1 + 9 b⁻⁴) 𝒟_main`. 
