---
{
  "module": "src/New/Spanning/Unfolding/SquareExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The expansion of the squares and the second moment near the Bessel subgroup

This file proves the expansion of the squares and the bound on the second moment near `R̄₀`, where
`R̄₀ = reducedImage besselS` is the reduction of the Bessel subgroup. These results concern the
operators `P_s = P* s P`, stated in terms of their blocks. The terms in the Bessel subgroup give the
operator `r_ψ(s)`, which is `New.Filling.besselTranslate`, and the terms off it give `P_s - r_ψ(s)`.
Along the way it treats the terms of cell rank `0` and the cosets `ζ R̄₀` by integral `ζ ∈ E` with
`ζ ζ̄ = 1`, called roots of unity (these are the roots of unity of `E`, by Kronecker's theorem), and
it computes the blocks of the Bessel subgroup.

## Main definitions and results

* `New.Filling.sqrt_secondMoment_compl_besselS_le`: the expansion of the squares.
* `New.Filling.secondMoment_compl_besselS_le`: `P_s` is close to `r_ψ(s)` near `R̄₀`.

Notions from other files:
* `termsOver c s c'`: the rational `γ` such that `h_c⁻¹ γ h_c'` (`translateByClassReps`) is integral
  with reduction `s`; such a `γ` lies over the block `(c, s, c')`.
* `amplitudeSum side T c s c'`: the sum of the amplitudes of the elements of `T` over that block.
* `secondMoment A Ω`: the sum of `‖A c s c'‖² / unipotentCovolume²` over all classes `c`, `c'` and
  `s ∈ Ω`.
* `reducedImage A`: the image in the finite group `ResidueGL` of the integral elements of `A`.


### `scalarIsometry`

 A scalar `ζ` with `ζ ζ̄ = 1` as an isometry of the form `J`. 

### `val_scalarIsometry_inv_mul`

 For `ζ ζ̄ = 1` and an isometry `g` of `J`, the matrix of `ζ⁻¹ g` is `ζ̄` times that of `g`. 

### `leadingMinor_frameGram_eq_zero`

 Let `ϱ > 0`, so that the first frame vector `e₁` is orthogonal to the frame. If `g` maps `e₁` to
a multiple of itself, then the leading minors of positive size of `frameGram g`, the matrix of the
products of the frame with its image under `g`, vanish. 

### `le_apply_one_of_inner_eq`

 A real function `β` of positive type on a group, that is, with `β (a⁻¹ b) = ⟪u a, u b⟫` for
vectors `u a` of an inner product space, is largest at `1`. 

### `sum_subgroup_filter`

 The sum of `β` over the elements of a subgroup `H` with the property `p`, read in the whole
group. 

### `mulVec_apply_eq_of_eq_zero_of_lt`

 If row `j` of `M` vanishes before the index `b`, and `v` vanishes after `b` and is `1` at `b`,
then the entry `j` of `M v` is `M j b`. 

### `mem_besselS_of_pairOccursAt`

 Suppose that for every index `a` the frame and its image under `γ` have a common vector that is
a combination of their vectors up to `a`, with coefficient `1` at `a` in both
(`PairOccursAt`). Then `γ` lies in the Bessel subgroup. 

### `PairOccursAt.apply_besselFrame_zero`

 If the first frame vector satisfies `ζ e₁ = γ e₁` in the form of `PairOccursAt` at the
index `0`, then `ζ` is the diagonal entry of `γ` at `e₁`. 

### `scalarIsometry_inv_mul_mem_besselS`

 Let `ζ ζ̄ = 1`. If the frame and its image under `γ` have common vectors with leading
coefficients `ζ` and `1` at every index, then `ζ⁻¹ γ` lies in the Bessel subgroup. 

 ### Terms of cell rank `0` and scalar cosets 

### `translateByClassReps_mem_besselS`

 For `γ` in the Bessel subgroup and classes `c`, `c'` with representatives `h_c`, `h_c'`, the
finite adelic element `h_c⁻¹ γ h_c'` lies in the Bessel subgroup. 

### `apply_besselFrame_zero_mem_Ô`

 If `h_c⁻¹ γ h_c' = translateByClassReps c c' γ` is an element `k` of the stabilizer of the
lattice, then the diagonal entry of `γ` at the first frame vector `e₁` is integral, being the same
entry of `k`. 

### `val_reduction_of_eq_smul_one`

 If the matrix of an element `z` of the stabilizer of the lattice is the scalar `ζ`, an integral
adele, then its reduction at a chosen place `w` is the residue of `ζ` at `w`. 

### `exists_scalar_mul_besselS`

 The classes `c`, `c'` are double cosets of the unitary group of the middle space `X₀`, with
representatives `h_c`, `h_c'`; a rational `γ` lies over the block `(c, s, c')` (`termsOver`) if
`h_c⁻¹ γ h_c'` is integral with reduction `s`. Let such a `γ` have norm-one pairs occurring from
level `0`: for one `ζ` with `ζ ζ̄ = 1`, the frame and its image under `γ` have common vectors with
leading coefficients `ζ`, `1` at every index. Then there is an integral `ζ` with `ζ ζ̄ = 1` such
that `γ` lies in `ζ` times the Bessel subgroup and `s` in `ζ` times the reduction of the Bessel
subgroup (`InScalarCoset`). 

### `apply_besselFrame_zero_of_mem_besselS`

 An integral element of the Bessel subgroup fixes the first frame vector `e₁`. 

### `apply_besselFrame_zero_of_mem_reducedImage`

 An element `t` of the reduction of the Bessel subgroup fixes the first frame vector modulo
every chosen place `w`: its column there is that of the identity matrix. 

### `meetsAt_of_eq_of_mem_reducedImage`

 Let `s` coincide, at the chosen places above `p_i`, with an element `t` of the reduction of the
Bessel subgroup. Then modulo each such place `w`, and modulo its conjugate (`isConj = true`), the
span of the frame and its image under `s` share a nonzero vector (`MeetsAt`), namely the first
frame vector. 

### `InScalarCoset.not_isOpenElement`

 An element `s` of `ζ` times the reduction of the Bessel subgroup is not open (`IsOpenElement`):
at every chosen place the leading minor of size `1` of the products of the frame with its image
under `s` vanishes. 

### `amplitudeSum_besselS_eq_zero`

 If `s` is not in the reduction of the Bessel subgroup, the terms in the Bessel subgroup
contribute `0` to every block `(c, s, c')`, as none of them lies over it. 

### `isStable_compl_besselS`

 The complement of the Bessel subgroup is stable under multiplication by the unipotent group
`besselU` on both sides. 

### `eq_one_of_reduceAt_scalar_eq_one`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). An integral `ζ ∈ E` with `ζ ζ̄ = 1` that is `1` modulo every place of
`chosenPlaces i`, the finite places of norm `p_i = levelPrime i` chosen in `S`, is `1`. 

### `forty_le_k_mul_numInfPlaces`

 The product `k f` of the rank `k` of `X₀` and the number `f` of infinite places of `E` is at
least `40`. 

### `AvoidsScalarCosets`

 The set `Ω` is disjoint from the cosets `ζ R̄₀` of the reduction `R̄₀` of the Bessel subgroup,
for all integral `ζ ≠ 1` in `E` with `ζ ζ̄ = 1`. 

### `AvoidsScalarCosets.not_normOnePairOccursFrom_zero`

 Let `Ω` avoid the cosets of the reduction of the Bessel subgroup by the roots of unity `ζ ≠ 1`.
Then no `γ` off the Bessel subgroup that lies over a block `(c, s, c')` with `s ∈ Ω` has a norm-one
pair occurring from level `0`: such a `γ` is `ζ` times an element of the Bessel subgroup, and
`ζ = 1`. 

### `normOnePairOccursFrom_zero_of_mem_besselS`

 An element `γ` of the Bessel subgroup has a norm-one pair occurring from level `0`: at every
index, the frame and its image under `γ` have a common vector with both leading coefficients `1`. 

 ### The blocks of the Bessel subgroup 

### `besselFn_mul_of_eq_embedH`

 Let `u` lie in the unipotent group `besselU`. At each infinite place `v`, let the image
`ratToInf η v` of `η` be `embedH (k v)`: the unitary matrix `k v` in `U(κ)` acts on `X₀` and the
other basis vectors are fixed. Then, for either `side` (full or cut), left translation by the image
of `u η` multiplies the values of `besselFn` by the tensor product (`kroneckerPi`) of the matrices
`rep (k v)` of the local Bessel systems `besselSystem v`, divided by `unipotentChar` of the finite
adelic image `ratToFin u`. 

### `exists_unitary_besselFn_mul`

 For `side` either the full Bessel function or its cut, an element `γ` of the Bessel subgroup
`besselS` acts on the values of `besselFn side` by a unitary matrix. That is, there is a unitary `M`
indexed by `BesselCoord` with `besselFn side (ratToInf γ * y) = M *ᵥ besselFn side y` for all
`y`. 

### `amplitudeSum_besselS_apply`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). The classes `c` index the double cosets of the unitary group of `X₀`, with
representatives `h_c`, and `termsOver c s c'` is the set of rational `γ` with `h_c⁻¹ γ h_c'`
integral of reduction `s`: these lie over the block `(c, s, c')`. Let `γ` in the Bessel subgroup
`besselS` lie over it and act on the values of the full Bessel function by the matrix `M`, whose
indices `BesselCoord` are the coordinates of those values. Then the sum of amplitudes
(`amplitudeSum`, for the full function) of the terms in the Bessel subgroup is
`unipotentCovolume • M` over this block and `0` over the blocks `(c, s, d)` with `d ≠ c'`; here
`unipotentCovolume` is the positive constant that stands for the covolume of the unipotent lattice
at a class. 

### `amplitudeSum_besselS_inv`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). For classes `c`, `d` and `s` in `ResidueGL`, a term lies over the block
`(c, s, d)` (`termsOver`) if `h_c⁻¹ γ h_d` is integral with reduction `s`. The sum of amplitudes
(`amplitudeSum`, for the full Bessel function) of the terms in the Bessel subgroup `besselS` over
`(d, s⁻¹, c)` is the adjoint of that over `(c, s, d)`, as a matrix indexed by the coordinates of the
Bessel function. 

### `amplitudeSum_mul_inv_apply`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). Let `δ` in the Bessel subgroup lie over `(d, t, d')` and act on the values of the
full Bessel function by `N`, and let `T` be a set of terms that is stable with `T δ = T`. Then the
sum of amplitudes of `T`, for the full function, over `(c, s t⁻¹, d)` is `A Nᴴ`, where `A` is that
over `(c, s, d')`. 

 ### The expansion of the squares and the second moment near `R̄₀` 

### `AvoidsScalarCosets.amplitudeSum_compl_besselS_eq`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). Let `Ω` avoid the cosets `ζ R̄₀` of the roots of unity `ζ ≠ 1`, and let `s ∈ Ω`.
Then over each block at `s` the terms off the Bessel subgroup `besselS` have the same sum of
amplitudes as the terms of `Γ* = remainingTerms`. These are the `γ` with `termDisc γ ≠ 0`, and those
with agreeing characters that move the span of the isotropic frame vectors `e₁, …, e_ϱ`. 

### `sqrt_secondMoment_compl_besselS_le`

 Let `E` contain a primitive `5040`-th root of unity, let the filling `S` be admissible
(`IsAdmissible`), and let `Ω` avoid the cosets of the reduction of the Bessel subgroup by the roots
of unity `ζ ≠ 1`. For each block over `Ω` and each link, sum the amplitudes for the cut Bessel
function of the terms with that link and nonzero `termDisc`; let the squared norms of these sums
(`linkSecondMoment`) add up to at most `C unipotentCovolume²`, with `C ≥ 0` and the positive
constant `unipotentCovolume` that stands for the covolume of the unipotent lattice at a class. Then
the second moment over `Ω` of the terms off the Bessel subgroup, for the full Bessel function, has
square root at most `C^(1/2) + b⁻¹⁵ 𝒟_id^(1/2)`, where `b = S.b` and `𝒟_id = identitySecondMoment`
is the order of the reduction of the Bessel subgroup times the number `sourceDim` of pairs of a
class and a coordinate. 

### `prod_levelPrime_le_meetNorm_of_eq`

 Let `E` contain a primitive `5040`-th root of unity and let the filling `S` be admissible
(`IsAdmissible`). Let `s` coincide, at the chosen places above `p_i = levelPrime i`, with an element
`t` of `reducedImage besselS`, the reduction of the Bessel subgroup. Then the product of the norms
`p_i` of these places and their conjugates is at most `meetNorm s`, the product of the norms of the
places at which `s` meets, as `s` meets at each of them. 

### `avoidsScalarCosets_setOf_exists_apply_eq`

 The set of the `s` that coincide with an element of `R̄₀`, the reduction of the Bessel subgroup,
at the chosen places above `p_i` avoids the cosets `ζ R̄₀` with `ζ ≠ 1`: such an `s` fixes the first
frame vector there, so `ζ` is `1` modulo these places. 

### `M_div_b_le_levelPrime_sq`

 Each level prime `levelPrime i` is at most `b` times the other, so `M / b ≤ p_i ^ 2`, with
`p_i = levelPrime i`, for the level `M = p₀ p₁`. 

### `secondMoment_compl_besselS_le`

 The second moment near the Bessel subgroup. Let `E` contain a primitive `5040`-th root of unity
and let the filling `S` be admissible (`IsAdmissible`). Let `Ω` be the set of `s` that coincide with
an element of `R̄₀` at the chosen places above `p_i`. Then the second moment over `Ω` of the terms
off the Bessel subgroup, that is `∑ ‖P_s - r_ψ(s)‖²`, is at most `b⁻¹² 𝒟_id`. Here `P_s` and
`r_ψ(s)` are the operators whose blocks at `s` are the conjugates of the amplitude sums of all terms
and of the terms in the Bessel subgroup, divided by `unipotentCovolume`, `R̄₀` is the reduction of
the Bessel subgroup, `p_i = levelPrime i`, `b` is the parameter `S.b` of the filling and
`𝒟_id = identitySecondMoment = #R̄₀ D_X`, with `D_X = sourceDim` the number of pairs of a class and
a coordinate. 
