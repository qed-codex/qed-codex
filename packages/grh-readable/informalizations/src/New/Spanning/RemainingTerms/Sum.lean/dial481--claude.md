---
{
  "module": "src/New/Spanning/RemainingTerms/Sum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Sum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Sum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The remaining terms: a bound for their sum

Size, gain and count are combined: pairs of terms that do not lie in the same link class contribute
at most `b ^ (-k f) 𝒟_id`, and pairs in the same link class gain the norm of the places at which the
block meets.

* `New.Filling.sum_termSize_mul_le`: sets of near pairs, one for each two classes, with
  `τ ^ (l + 6) D η ^ (-k) ≤ B` contribute at most `τ B` in all. Here `l` is the corank of the common
  lattice, the gain `η` is such that `(d η)²` is at most the product of the two gauges for the
  discriminant `d` of that lattice, and `D` bounds the second moments of both cell ranks.
* `New.Filling.sum_termSize_mul_not_inSameLinkClass_le`: pairs with different links, or with equal
  links and `𝗀 = 0`, contribute at most `b ^ (-k f) 𝒟_id`.
* `New.Filling.sum_termSize_mul_inSameLinkClass_le`: pairs with equal links and `𝗀 ≠ 0` over blocks
  that meet at places of total norm at least `z` contribute at most `(b ^ (2 f) / z) ^ k 𝒟_main`.
* `New.Filling.secondMoment_remainingTerms_le`, `New.Filling.linkSecondMoment_le_of_le_meetNorm`:
  the resulting bounds for the second moment of the remaining terms.

Here `b = S.b` is the scale, `M = S.M` the congruence level, `k = 𝔰.k` and `n = 𝔰.n` are sizes of
the shape, `f` is the number of infinite places, `τ = S.tailScale = b ^ (k f / 4)` is the number
whose powers may be lost, `𝗀 = S.termDisc`, `𝒟_id = S.identitySecondMoment` and
`𝒟_main = S.mainSecondMoment`.

Notions from other files:
* `S.cellRank γ`: the cell rank of a rational element `γ`, the index of its cell.
* `S.termsOver c s c'`: the rational elements that are integral in the position given by the classes
  `c`, `c'` and have reduction `s`; the triple `(c, s, c')` is called a block.
* `S.IsNearPairOverAgreeingBlock c c' q`: both terms of `q` are near, are the chosen elements of
  their orbits, have a cell rank, and lie over one block `(c, s, c')` whose `s` agrees
  (`S.Agrees s`).
* `S.pairDiscriminant c c' γ γ'`: the discriminant of the common lattice `L₁₂` of two terms, a
  lattice in `commonLink γ γ'`; its corank is `k - finrank E (commonLink γ γ')`.
* `S.termSize c c' γ`: the bound `τ² (D_j / (n_p G ^ k)) ^ (1 / 2)` for the orbit of `γ`, with the
  second moment `D_j = S.cellRankSecondMoment j`, the gauge `G = S.levelGauge j c c' γ` and
  `n_p = S.pairCountScale`.

## Relation to the literature

The second moment of the Poincaré series expands over pairs of rational elements congruent mod `M`.
Discriminant gains, lattice counts and a weighted Schur test show that degenerate terms and pairs
with different links are negligible, and that the remaining terms shrink where frames meet mod `M`,
which isolates the main term. Discarding small cells and off-diagonal terms of Petersson-type and
relative trace formulas by congruences and counts is known in the literature. Related work:
Michel–Ramakrishnan–Yang, Bessel periods on U(2,1)×U(1,1), 2023; Kowalski–Saha–Tsimerman, Local
spectral equidistribution for Siegel modular forms, 2012; Blomer, Density theorems for GL(n), 2023.


### `eq_of_mem_termsOver`

 A term `γ` over the classes `c`, `c'` determines the reduction `s` of its block `(c, s, c')`. 

### `IsNearPairOverAgreeingBlock.one_le_pairDiscriminant`

 The common lattice of a near pair (two near representative terms over one block whose `s`
agrees) has discriminant at least `1`. 

### `IsNearPairOverAgreeingBlock.pairDiscriminant_sq_le`

 For a near pair `(γ, γ')`, the square of the discriminant of the common lattice is at most
`(2 / M) ^ (2 i f)` times the product of the two gauges, where `i` is the codimension in each link
(`New.link`) of the intersection of the links, `M = S.M` is the congruence level and `f` is the
number of infinite places. 

### `IsNearPairOverAgreeingBlock.corank_le_and_pairDiscriminant_le`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
Let `(γ, γ')` be a near pair over the classes `c`, `c'`. Its common lattice has corank at most `n³`
and discriminant at most `S.discriminantBound = b ^ (n³ f)`. 

### `IsNearPairOverAgreeingBlock.mem_boundedDiscNearPairs`

 A near pair (two near representative terms over one block whose `s` agrees) lies in
`S.boundedDiscNearPairs l c c'`, the set of near pairs of corank `l` and bounded discriminant, for
`l` the corank of its common lattice. 

### `termSize_sq_le`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
Let `c`, `c'` be classes and `γ` a rational point of cell rank `j = S.cellRank γ` whose gauge
`G = S.levelGauge j c c' γ` is positive. If the constant `S.cellRankSecondMoment j` is at most `D`,
then the square of the size `S.termSize c c' γ` is at most `τ⁴ D / (n_p G ^ k)`. 

### `IsNearPairOverAgreeingBlock.termSize_mul_le`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
Let `(γ, γ')` be a near pair over the classes `c`, `c'` and `d` the discriminant of its common
lattice `S.pairLattice`. Let `η > 0`. If `(d η)²` is at most the product of the two gauges and the
constants `S.cellRankSecondMoment` of both cell ranks are at most `D`, then the product of the sizes
`S.termSize` is at most `τ⁴ D η ^ (-k) d ^ (-k) / n_p`. 

### `IsNearPairOverAgreeingBlock.ofReal_termSize_mul_le`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
Let `(γ, γ')` be a near pair over the classes `c`, `c'`, whose common lattice `S.pairLattice` has
corank `l = k - finrank E (commonLink γ γ')` and discriminant `d = S.pairDiscriminant c c' γ γ'`.
Let `η > 0`. Suppose that `(d η)²` is at most the product of the two gauges, `D` bounds the
constants `S.cellRankSecondMoment` of both cell ranks, and `τ ^ (l + 6) D η ^ (-k) ≤ B`. Then the
product of the sizes `S.termSize` is at most `B d ^ (-k) / (τ ^ (l + 2) n_p)`. 

### `cube_add_one_le_tailScale`

 The number `n³ + 1` of possible coranks is at most `τ = S.tailScale`. 

### `sum_termSize_mul_le`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
For all classes `c`, `c'` let `P c c'` be a set of near pairs over `c`, `c'`. Suppose that for each
pair, with a common lattice of corank `l` and discriminant `d`, there are `η > 0` and `D` such that
`(d η)²` is at most the product of the two gauges, `D` bounds the constants `S.cellRankSecondMoment`
of both cell ranks, and `τ ^ (l + 6) D η ^ (-k) ≤ B`, where `τ = S.tailScale`, `k = 𝔰.k` and
`B ≥ 0`. Then the products of the sizes `S.termSize` of the two terms add up to at most `τ B`. 

### `InSameLinkClass`

 Two terms lie in the same link class if `𝗀 = S.termDisc` vanishes for neither and their links
(`New.link`) are equal. 

### `cellRankSecondMoment_le_mainSecondMoment`

 Let `S` be data of the filling theorem that satisfy the standing hypotheses `S.IsAdmissible`.
The second moment `S.cellRankSecondMoment j` of every cell rank `j` is at most `S.mainSecondMoment`,
the second moment of the top cell rank `ϱ + 1`. 

### `pow_mul_mainSecondMoment_div_le`

 Let `E` be a CM field, and let `S` be data of the filling theorem over `E` that satisfy the
standing hypotheses `S.IsAdmissible`. For `i ≥ 1` and `l ≤ i + 1` we have `τ ^ (l + 6) 𝒟_main
(M / 2) ^ (-i f k) ≤ τ ^ (-10) 𝒟_id`. This serves pairs whose links intersect in codimension `i` and
whose common lattice has corank `l`. 

### `sum_termSize_mul_not_inSameLinkClass_le`

 **Remaining terms, pairs that do not lie in the same link class.** Let `E` be a CM field with a
primitive root of unity of order 5040, and let `S` be data of the filling theorem over `E` that
satisfy the standing hypotheses `S.IsAdmissible`. Sum over all classes `c`, `c'` and all near pairs
over them whose links (`New.link`) differ or for one of which `𝗀 = S.termDisc` vanishes. The
products of the sizes of the two terms add up to at most `b ^ (-k f) 𝒟_id`. 

### `sum_termSize_mul_inSameLinkClass_le`

 **Remaining terms, pairs in the same link class.** Let `E` be a CM field with a primitive root
of unity of order 5040, and let `S` be data of the filling theorem over `E` that satisfy the
standing hypotheses `S.IsAdmissible`. Let `z ≠ 0`. Sum over all classes `c`, `c'` and all near pairs
over them with equal links (`New.link`), with `𝗀 = S.termDisc ≠ 0` for both terms, and whose
reduction `s` has `z ≤ S.meetNorm s`. The products of the sizes `S.termSize` of the two terms add up
to at most `(b ^ (2 f) / z) ^ k 𝒟_main`. 

### `Piece`

 The pieces into which a block is split: one for each link, and one for `𝗀 = 0`. 

### `piece`

 The piece of a term `γ`: its link if `𝗀(γ) = S.termDisc γ ≠ 0`; the terms with `𝗀 = 0` form one
further piece. 

### `piece_eq_some_iff`

 The piece of `γ` is the submodule `Λ` if and only if `𝗀(γ) = S.termDisc γ` is not zero and the
link of `γ` is `Λ`. 

### `IsStable.inter_piece`

 The part `T ∩ S.piece ⁻¹' {κ}` of a stable set `T` in one piece `κ` is stable. A stable set is
one invariant on both sides under the rational points of the Bessel unipotent group. This holds
because `S.termDisc` and the link are invariant. 

### `mem_of_mem_nearRepresentativesOver`

 A near representative of `T` over a block `(c, s, c')` (a chosen near term, that has a cell
rank, where `s` agrees) belongs to `T`. 

### `mem_termsOver_of_mem_nearRepresentativesOver`

 A near representative of `T` over the block `(c, s, c')` is a term over this block. 

### `isNearPairOverAgreeingBlock_of_mem_nearRepresentativesOver`

 Two near representatives over the same block `(c, s, c')` form a near pair over an agreeing
block, that is, two near representatives over one block whose reduction `s` agrees. 

### `enorm_amplitudeSum_mul_le`

 Let `E` be a CM field with a primitive root of unity of order 5040, and let `S` be data of the
filling theorem over `E` that satisfy the standing hypotheses `S.IsAdmissible`. Let `T`, `T'` be
subsets of `Γ* = S.remainingTerms` that are stable, that is, invariant on both sides under the
rational points of the Bessel unipotent group. The product of the norms of the sums of the
amplitudes of their terms over `(c, s, c')` is at most the sum, over a near representative of `T`
and one of `T'`, of the square of the covolume `S.unipotentCovolume` times the product of the two
sizes.

A rational point `γ` lies over `(c, s, c')` if `h_c⁻¹ γ h_c'` (`h_c = S.classRep c`) is integral
with reduction `s`. Its amplitude is the integral over the archimedean points `y` of
`β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^*`, where `β_c = S.classCutoff c` and `W` is the cut Bessel
function, the Bessel function times a cutoff in the length `besselLength` at each infinite place. A
near representative of `T` over `(c, s, c')` is a `γ ∈ T` over `(c, s, c')` that is near (some
archimedean point `y` and `γ⁻¹ y` are both reduced and of bounded size, `S.boxedPoints`), is the
chosen element of its double coset under the groups `S.classUnipotent₀` and has a cell rank; there
are none unless `S.Agrees s`. The size `S.termSize c c' γ` is `τ² (D_j / (n_p G ^ k)) ^ (1 / 2)`,
where `j = S.cellRank γ` is the index of the cell of `γ`, `D_j = S.cellRankSecondMoment j`,
`G = S.levelGauge j c c' γ` is its gauge, `n_p = S.pairCountScale` and `τ = S.tailScale`. 

### `enorm_amplitudeSum_sq_le`

 Let `E` be a CM field with a primitive root of unity of order 5040, and let `S` be data of the
filling theorem over `E` that satisfy the standing hypotheses `S.IsAdmissible`. Let
`T ⊆ Γ* = S.remainingTerms` be stable (invariant on both sides under the rational points of the
Bessel unipotent group). The squared norm of the sum of the amplitudes of the terms of `T` over
`(c, s, c')` is at most the sum over submodules `Λ` of the same squared norms for the terms of `T`
with `𝗀 = S.termDisc ≠ 0` and link `Λ`, plus `S.unipotentCovolume ^ 2` times the sum of the products
of the sizes over the pairs of near representatives of `T` whose links differ or for one of which
`𝗀` vanishes.

The link `link γ` is the module of pairs (class of `t`, class of `γ⁻¹ t`) in `X^⊥/X`,
`X = ⟨e₁, …, e_ϱ⟩`, `t ⊥ X, γ X`. A rational point `γ` lies over `(c, s, c')` if `h_c⁻¹ γ h_c'`
(`h_c = S.classRep c`) is integral with reduction `s`. Its amplitude is the integral over the
archimedean points `y` of `β_c(y) β_c'(γ⁻¹ y) W(y) ⊗ W(γ⁻¹ y)^*`, where `β_c = S.classCutoff c` and
`W` is the cut Bessel function, the Bessel function times a cutoff in the length `besselLength` at
each infinite place. A near representative of `T` over `(c, s, c')` is a `γ ∈ T` over `(c, s, c')`
that is near (some archimedean point `y` and `γ⁻¹ y` are both reduced and of bounded size,
`S.boxedPoints`), is the chosen element of its double coset under the groups `S.classUnipotent₀` and
has a cell rank; there are none unless `S.Agrees s`. The size `S.termSize c c' γ` is
`τ² (D_j / (n_p G ^ k)) ^ (1 / 2)`, where `j = S.cellRank γ` is the index of the cell of `γ`,
`D_j = S.cellRankSecondMoment j`, `G = S.levelGauge j c c' γ` is its gauge, `n_p = S.pairCountScale`
and `τ = S.tailScale`. 

### `secondMoment_remainingTerms_le`

 **Remaining terms, reduction to one link.** Let `E` be a CM field with a primitive root of unity
of order 5040, and let `S` be data of the filling theorem over `E` that satisfy the standing
hypotheses `S.IsAdmissible`. Let `Ω` be a set of reductions, `w ≥ 0` and `ν = S.unipotentCovolume`.
Suppose that the terms with `𝗀 = S.termDisc ≠ 0`, taken link by link, have sum of squared norms of
amplitude sums (`linkSecondMoment`) at most `w ν²` over `Ω`. Then the second moment over `Ω` of
`Γ* = S.remainingTerms`, for the cut Bessel function, is at most `w + b ^ (-k f) 𝒟_id`. 

### `linkSecondMoment_le_of_le_meetNorm`

 **Remaining terms, one link at a time.** Let `E` be a CM field with a primitive root of unity of
order 5040, and let `S` be data of the filling theorem over `E` that satisfy the standing hypotheses
`S.IsAdmissible`. Let `Ω` be a set of reductions, that is, of elements of `S.ResidueGL`, the product
of the general linear groups over the residue fields at the chosen places above the level `M = S.M`.
A reduction `s` meets at a place above `M` if, modulo that place, the span of the frame and its
image under `s` share a nonzero vector; `S.meetNorm s` is the norm of the product of the places at
which `s` meets. Let `z ≠ 0` be a natural number with `z ≤ S.meetNorm s` for every `s ∈ Ω`.

Let `T` be the set of rational points `γ` of the unitary group with `S.termDisc γ ≠ 0`. For classes
`c`, `c'`, a reduction `s` and a submodule `Λ`, take the sum of the amplitudes of the `γ ∈ T` that
lie over `(c, s, c')` and have link `Λ`. The squared norms of these sums, added over all `c`, `c'`,
`s ∈ Ω` and `Λ`, give `linkSecondMoment T Ω`, and this is at most `(b ^ (2 f) / z) ^ k 𝒟_main ν²`.
Here `b = S.b` is the size parameter, `k = 𝔰.k` is the dimension of the definite space, `f` is the
number of infinite places of `E`, and `𝒟_main = S.mainSecondMoment` and the covolume
`ν = S.unipotentCovolume` are real constants attached to `S`. 
