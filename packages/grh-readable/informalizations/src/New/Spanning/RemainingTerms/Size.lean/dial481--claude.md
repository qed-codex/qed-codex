---
{
  "module": "src/New/Spanning/RemainingTerms/Size.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Size.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Size.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The orbit bound: a bound for a block of amplitudes; the second moment of a set of terms

Let `S : New.Filling E 𝔰` be filling data. The block `New.Filling.amplitudeSum S side T c s c'` is
the sum of the amplitudes of the rational elements of `T` that lie over the classes `c`, `c'` with
reduction `s` in `New.Filling.ResidueGL S`. The argument `side : New.FullOrCut` selects the full or
the cut Bessel functions. Write `ν` for `New.Filling.unipotentCovolume S`, the covolume of the
unipotent group of a class, `d₁` for `New.Filling.identitySecondMoment S` and `b` for the size
parameter `S.b ≥ 1`. The file defines the second moment of a family of blocks and proves that its
square root is subadditive. Its main result bounds the norm of a single block by ν times the sum of
the orbit bounds of the near orbits.

## Main definitions and results

* `New.Filling.secondMoment A Ω`: for a family of blocks `A c s c'`, the sum of the squared norms of
  the blocks with `s ∈ Ω`, divided by `ν²`.
* `New.Filling.secondMoment_sub_cut_le`: the second moment of the difference between the blocks of
  `U` and those for the cut functions is at most `b⁻⁴⁰` times `identitySecondMoment`.
* `New.Filling.enorm_integral_besselKernel_le`: the bound for one term on the open cell, from the
  bound `New.BesselSystem.enorm_integral_pairKernel_cut_le` for a family of real points.
* `New.Filling.enorm_amplitudeSum_le_orbitBound_top`: the bound for a block when
  `New.Filling.termDisc` vanishes nowhere on `T`; it rests on a change of weight
  (`New.Filling.hasSum_amplitudeSum_of_cutoff`) and the bound for one term.
* `New.Filling.enorm_amplitudeSum_le_orbitBound`: one bound for a stable set of terms of one cell
  rank `j` (`New.Filling.HasCellRank`), none of cell rank `0` over the block. Terms with large
  `New.Filling.termDiscNorm` use the open cell, the others are summed by
  `New.Filling.tsum_amplitudeMajorant_orbit_le`.
* `New.Filling.enorm_amplitudeSum_le_tsum_termSize`: a cut block of a stable subset of
  `New.Filling.remainingTerms` is at most `ν` times the sum of the sizes of its near
  representatives.

Notions from other files:
* `New.Filling.termsOver`: The rational γ such that h_c⁻¹ γ h_c' is integral and has reduction s,
  where h_c is the representative of the class c.
* `New.Filling.ResidueGL`: The finite group of reductions, a product of general linear groups over
  the residue fields at the chosen places.
* `New.Filling.termDisc`: The element 𝗀(γ) = |D_{ϱ+1}|² − N²|D_ϱ|² of E, formed from the last two
  leading minors of the matrix of products between the frame and its image under γ; N = S.N.
* `New.Filling.IsNear`: Some archimedean point y has both y and γ⁻¹ y among the boxed points;
  `New.Filling.IsNearRepresentative` says also that γ is the chosen element of its orbit.
* `New.Filling.IsAdmissible`: The standing hypotheses on the filling data, mostly size inequalities
  between its parameters.

## Relation to the literature

See `New.Spanning.RemainingTerms.Sum` for related work.



## Second moment of a set of terms and transfer to cut Bessel functions

The second moment `New.Filling.secondMoment` sums the squared norms of the blocks, divided by `ν²`.


### `secondMoment`

 The second moment 𝖤(A, Ω) of a family of blocks `A c s c'` in a normed group: ν⁻² times the sum
over classes c, c' and s ∈ Ω of the squared norm of `A c s c'`, with ν = `S.unipotentCovolume`. 

### `linkSecondMoment`

 The sum, over classes `c`, `c'`, reductions `s ∈ Ω` and submodules `Λ`, of the squared norm of
the block over `(c, s, c')` of the terms `γ` of `T` with `New.link γ = Λ`, for the cut Bessel
function. It takes values in `ℝ≥0∞` and, unlike `New.Filling.secondMoment`, is not divided by
`ν²`. 

### `amplitudeSum_eq_inter_compl_add_inter`

 The blocks (sums of amplitudes over two classes and a reduction) of a set `T` of rational
elements are the sums of the blocks of `T ∩ Uᶜ` and of `T ∩ U`. 

### `sqrt_secondMoment_add_le`

 Minkowski's inequality for the second moment: for families `A`, `B` of vectors `A c s c'` in
`V`, indexed by `S.Classes × S.ResidueGL × S.Classes`, `√(secondMoment (A + B) Ω) ≤ √(secondMoment A
Ω) + √(secondMoment B Ω)`. 

### `sum_norm_amplitudeSum_sub_cut_le`

 For a set `U` of rational elements and fixed `c`, `s`, consider the amplitude sums
`S.amplitudeSum .full U c s c'` and `S.amplitudeSum .cut U c s c'`. The norms of their differences
have sum over `c'` at most `ν b ^ (-k³ f) / 2`. Here `ν` is `S.unipotentCovolume`, `b = S.b` is the
size parameter, `k = 𝔰.k` and `f` is the number of infinite places of `E`. 

### `card_residueGL_mul_b_pow_le`

 The cardinality of `S.ResidueGL` times `S.b ^ 40` is at most `(S.b ^ (𝔰.k ^ 3 * f) * 2) ^ 2`,
where `f` is the number of infinite places of `E`. 

### `secondMoment_sub_cut_le`

 For a set `U` of rational elements, passing from the Bessel function to its cut changes the
blocks over the reductions in `Ω` little: the sum over classes `c`, `c'` and `s ∈ Ω` of the squared
norms of the differences of the blocks, divided by the square of the covolume
`ν = S.unipotentCovolume`, is at most `b⁻⁴⁰` times `identitySecondMoment`. 


## Bound for a block of amplitudes of a stable set

The norm of a block is bounded under `New.Filling.IsAdmissible`, for the cut Bessel functions
(`New.FullOrCut.cut`) and a set `T` stable under the unipotent group on both sides
(`New.Filling.IsStable`).


### `eq_one_of_mul_eq_mul_of_termDisc_ne_zero`

 Let `p γ = γ w` with `p` in `U⁰_c` (the elements of the unipotent group `U_c` of the class `c`
that fix the frame) and `w` in `U_c'`. If `𝗀(γ) = S.termDisc γ`, formed from the last two leading
minors of the frame products of `γ`, is nonzero, then `w = 1`. Hence `p = 1`: the stabilizer in
`U⁰_c` of the coset `γ U_c'` is trivial. 

### `tsum_ite_representative_eq_one`

 Let `ρ` choose a representative in each double coset of `U⁰_c = S.classUnipotent₀ c` and
`U_c' = S.classUnipotent c'`, and let `γ` have `S.termDisc γ ≠ 0`. Then exactly one pair `(a, b)` in
these groups carries `γ` to the representative `a γ b⁻¹` of its double coset; this is written as a
sum of indicators equal to 1. 

### `enorm_integral_besselKernel_le`

 **Open cell.** Let `W` be the cut Bessel vector on the archimedean points, so that the kernel
`S.besselKernel .cut γ y` is the tensor `W(y) ⊗ W(γ⁻¹ y)^*`; with `.full` the uncut vector is meant.
A point `y` lies in the cut at the place `v` (`InCut`) if its size `besselLength` is at most
`b ^ (6 n + 2)`, where `b = S.b` is the size parameter and `n = ϱ + 1`. It lies in the box
(`frameBox`) if it moves the frame to vectors `y⁻¹ f_a` of norm at most `ρ = S.frameBoxRadius`. Let
`γ` be near, that is, some `y` has `y` and `γ⁻¹ y` both reduced (`reducedPoints`) and in the cut at
every place, and let `𝗀(γ) = S.termDisc γ ≠ 0`. Let the weight `ω ≤ 1` be measurable, left invariant
under the fixer of the frame, and zero at the points that at some place lie in the cut but not in
the box. Let `ε²` bound the product over `v` of the numbers `pairingBoundSq`: explicit bounds for
the squared local pairing, in terms of the local value of `𝗀`, the radius `ρ`, and the degree and
the dimension of the Bessel system `S.besselSystem v`. Then the integral of `ω` times the cut kernel
has norm at most `ε` plus the integral of `ω` times the norm of the difference of the full and the
cut kernel. 

### `exists_isNearRepresentative_of_besselKernel_ne_zero`

 Let `U_c` be the unipotent group of the class `c` and `U⁰_c` its subgroup fixing the frame. An
archimedean point `y` is reduced if the entries above the diagonal of the matrix `S.ratTriangle y`
lie in a fixed set of representatives modulo `M 𝓞_E`, and boxed if moreover its size `besselLength`
is at most `b ^ (6 n + 2)` at every infinite place. If the cut Bessel kernel `W(y) ⊗ W(γ⁻¹ y)^*` of
`γ` is nonzero at a reduced point `y`, then the double coset `U⁰_c γ U_c'` contains an element `δ`
that is near and is the chosen element of its smaller double coset `U⁰_c δ U⁰_c'`. 

### `isIntegral_termDisc`

 The element `𝗀(γ) = |D_{ϱ+1}|² - N² |D_ϱ|²` (`termDisc γ`), formed from the last two leading
minors of the matrix of frame products, is an algebraic integer for a rational `γ` in
`S.termsOver c s c'`. 

### `toReal_smul_besselKernel_eq_zero`

 If no element `δ` of the double coset `U⁰_c γ U_c'` is near and the chosen element of
`U⁰_c δ U⁰_c'` (`IsNearRepresentative`), then the cut Bessel kernel of `γ` is zero at every reduced
point `y`, that is, wherever `S.reducedIndicator y ≠ 0`. 

### `tsum_representative_weight_eq_one`

 Let `T` be a set of rational elements with `𝗀 = termDisc ≠ 0` that is stable under the rational
unipotent group on both sides, and let `ρ` choose a representative in each double coset
`U⁰_c γ U_c'`, where `U_c = S.classUnipotent c` and `U⁰_c` is its subgroup fixing the frame. Let
`ω` be a partition of unity in boxes for `U_c` modulo `U⁰_c`; the property used is that
`∑ x ∈ U_c, a x * ω (x y) = 1` for every weight `a` whose sum over each coset `U⁰_c x` is one. Then
for `γ ∈ T` the sum of `ω (u y)` over the pairs `(u, u')` in `U_c × U_c'` for which `u γ u'⁻¹` is
the representative of its double coset equals one. 

### `enorm_amplitudeSum_le_orbitBound_top`

 The bound for a block through the open cell. Let `T` be a set of rational elements, invariant
under the rational unipotent group on both sides, on which `𝗀 = termDisc` does not vanish. The terms
over `(c, s, c')` are the `γ` with `h_c⁻¹ γ h_c'` integral and of reduction `s`, and the cut block
`amplitudeSum` is the sum of their amplitudes, the integrals of the cut Bessel kernel against the
cutoffs of `c` and `c'`. Its norm is at most the covolume `ν = unipotentCovolume` times a sum over
the terms `γ` that are near and are the chosen element of their double coset `U⁰_c γ U⁰_c'`, with
`U⁰_c` the group of the unipotent elements of the class `c` fixing the frame. The summand is
`orbitBound j x`, an explicit constant times `x ^ (-k / 2)`, at the top rank `j = ⊤ = ϱ + 1` and at
`x = termDiscNorm γ`, the product of the `|𝗀(γ)|_v` over the infinite places. 

### `isNear_of_amplitudeMajorant_ne_zero`

 If the majorant `S.amplitudeMajorant .cut c c' γ` of the amplitude of `γ` over the classes `c`,
`c'` is nonzero, then `γ` is near (`S.IsNear γ`): some archimedean point `y` has both `y` and
`γ⁻¹ y` in `S.boxedPoints`. 

### `enorm_amplitudeSum_le_of_termDiscNorm_le`

 The bound for a block by Schur's test. Write `D_l(γ)` for the leading minors of the matrix of
products of the frame with its image under `γ`, and `f` for the number of infinite places. Let `T`
be stable under the rational unipotent group on both sides, with all elements of cell rank `j`: the
two flags share vectors from the index `j` on, `D_j ≠ 0`, and `𝗀 = termDisc` is nonzero exactly if
`j = ϱ + 1`. Suppose that on `T` the norm `termDiscNorm` of `𝗀` is at most `N ^ f * minorNorm j`,
where `minorNorm j` is the norm of `D_j`, divided by `N ^ (2 f)` at the top rank, and that no
element of `T` over `(c, s, c')` has cell rank `0`. Then the cut block is at most the covolume
`ν = unipotentCovolume` times a sum over the near terms `γ` that are the chosen element of their
double coset `U⁰_c γ U⁰_c'` under the frame-fixing unipotent groups. The summand is
`orbitBound j x`, an explicit constant depending on `j` times `x ^ (-k / 2)`, at
`x = maxGauge j c c' γ`. 

### `enorm_amplitudeSum_le_orbitBound`

 Write `D_l(γ)` for the leading minors of the matrix of products of the frame with its image
under `γ`, `𝗀 = |D_{ϱ+1}|² - N² |D_ϱ|²`, and `f` for the number of infinite places. Let `T` be
stable under the rational unipotent group on both sides, with all elements of cell rank `j`, and
with no element of cell rank `0` over `(c, s, c')`. Then the cut block is at most the covolume
`ν = unipotentCovolume` times a sum over the near terms `γ` that are the chosen element of their
double coset `U⁰_c γ U⁰_c'` under the frame-fixing unipotent groups. The summand is
`orbitBound j x`, an explicit constant depending on `j` times `x ^ (-k / 2)`, at
`x = maxGauge j c c' γ`. This is the larger of the norm `termDiscNorm` of `𝗀` and
`N ^ f * minorNorm j`, divided by the lattice indices `isotropicRowsIndex j` at `h_c⁻¹ γ h_c'` and
at its inverse. The sum is empty, and the block is `0`, unless `s` agrees: integral unipotent `u`,
`u'` whose reductions satisfy `u s = s u'` have the same value of the character `unipotentChar`. 

### `hasSum_amplitudeSum_fibre`

 For a function `f` on the rational elements, the amplitude sum `S.amplitudeSum side T c s c'` is
the sum over `i` of the amplitude sums `S.amplitudeSum side (T ∩ f ⁻¹' {i}) c s c'` of the
fibres. 

### `enorm_amplitudeSum_le_tsum_fibre`

 For a function `f` on the rational elements, the norm of the cut amplitude sum
`S.amplitudeSum .cut T c s c'` is at most the sum over `i` of the norms of the cut amplitude sums of
the fibres `T ∩ f ⁻¹' {i}` at the same `c`, `s`, `c'`. 

### `hasCellRank_cellRank_of_mem`

 Every element of `Γ* = S.remainingTerms` has a cell rank, namely `S.cellRank γ`. 

### `enorm_amplitudeSum_le_tsum_termSize`

 **Size.** Let `S` be admissible filling data of shape `𝔰` over a CM field `E` with a primitive
root of unity of order 5040. The set `Γ* = S.remainingTerms` consists of the rational `γ` with
`𝗀(γ) = S.termDisc γ ≠ 0`, and of those with `𝗀(γ) = 0` that move the isotropic space `⟨e₁, …, e_ϱ⟩`
and for which the unipotent character takes the same value at unipotent `u`, `u'` with `u γ = γ u'`.
Let `T ⊆ Γ*` be stable under the rational unipotent group on both sides, and fix classes `c`, `c'`
and a reduction `s`. The norm of the cut block is at most the covolume `unipotentCovolume` times the
sum of the sizes of the near representatives. These are the terms of `T` over the block that are
near, are the chosen element of their orbit `U⁰_c γ U⁰_c'` and have a cell rank `j ≤ ϱ + 1`,
provided `s` agrees; otherwise there are none. 
