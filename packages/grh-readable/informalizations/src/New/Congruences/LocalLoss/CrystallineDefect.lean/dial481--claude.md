---
{
  "module": "src/New/Congruences/LocalLoss/CrystallineDefect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineDefect.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineDefect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The defect of the dual of a summand at a place above ℓ

This file bounds, at a place above ℓ, the normalised defect of the Tate dual of a summand whose
class is adapted to the summands of the data `D`. Here `New.Selmer.IsCompletionGroup` identifies Γ
with the Galois group of a completion of E, and `complexEmbeddingOf e g` is the complex embedding of
E read by g in G_ℓ. This file checks that the data satisfy the size conditions of the crystalline
bound, treats the tame case at the primes `D.levelPrime n`, and compares both bounds with the local
loss `New.Selmer.defectBound`.

## Main definitions and results

* `New.Selmer.IsSummandClass`: The lattices `L i` are the summands at a place above `ℓ`, and `F`,
  `K`, `U` are the data of a class `New.Lift.InClass F K U` adapted to them. The summand `L none` is
  the main summand, of rank `r` and with jumps `J g` at `coefficientEmbedding O g`; the summand
  `L (some c)` has the single jump `c < t`.
* `New.Selmer.summand_defect_le_at_place`: let `D` be the data, take the coefficient ring `O`
  sufficiently large, and consider summands consisting of one lattice of rank r, the main summand,
  and further lattices with a single jump each. If a summand lies in a tame or crystalline class
  adapted to the summands, then the defect of its dual is at most [G_ℓ :
  j(Γ)] · rank · `New.Selmer.defectBound` / x, where x = 1 for the main summand and x = D.t
  otherwise.

Notions from other files:
* `New.Lift.GalLattice`: A finite free O-module with a compatible ℤ_ℓ-module structure, together
  with an O-linear representation of the group Γ on it.
* `New.Period.IsPotentiallyCrystalline`: for a representation on T and the crystalline period ring
  B, the elements of B⊗T fixed by all g with j(g) near 1 span B⊗T over B.
* `New.Period.jump`: The multiplicity of the Hodge–Tate jump u at γ: the dimension over ℚ̄_ℓ (zero
  if infinite) of the space `New.Period.hodgeTateMaps`.
* `New.Data.t`: The natural number t = 5r, where r is the rank in the data.
* `New.Selmer.CrystallineSizes`: the size conditions of the crystalline bound on its eight
  parameters.

## Relation to the literature

See `New.Congruences.FirstOrder.RibetElement` for related work. See `Lib.PadicHodge.BlochKato` for
sources.


### `New.Selmer.farWindowStart`

 The start of the far window at the embedding `σ` that holds the jumps near `∓ w_i`: it is
`D.natB` if the place of `σ` lies in `D.bPlaces` and `D.offWeight` otherwise, plus `i Δ + h₂ - 2 t`
with `Δ = D.gap`, `h₂ = D.halfGap` and `t = D.t`. 

### `New.Selmer.fitsWindows_and_image_neg_sub_one`

 Let `w_i = D.liftWeight i` be the `i`-th weight at the place of `σ`, and let `ε = cmSign σ` be
`1` if `σ` is in the CM type and `-1` otherwise. Let each member of `J` be low
(`Δ / 4 ≤ |u| ≤ 2 m Δ` with `Δ = D.gap`) or within `D.t` of `-ε w_i`, and let each member of `U` lie
in `J` or in `[0, t)`, with `t ≤ D.t`. Put `η = h₂² + 1` with `h₂ = D.halfGap`, and let
`S = farWindowStart D i σ`, which equals `w_i - 2 D.t`. Then `U` lies in the union of `[-η, η]` and
`-ε [S, S + 4 D.t]`, and the dual jumps `-u - 1` lie in the union of `[-η, η]` and
`ε [S, S + 4 D.t]`. 

### `New.Selmer.sum_count_neg_sub_one_le`

 If `2 ≤ h²`, the members `a` of `J` whose dual jump `-a - 1` lies in `[-h² - 1, h² + 1]` are
at most as many as those with `|a| ≤ 2 h²`, both counted with multiplicity. 

### `New.Selmer.smul_eq_pow_of_coefficientEmbedding_eq_pow`

 A relation between two letters determines the action on roots of unity: if `ζ` in `O` is a
primitive `N`-th root of unity and `g' ζ = (g ζ) ^ n`, then `g' g⁻¹` raises every `N`-th root of
unity to the power `n`. 

### `New.Selmer.complexEmbeddingOf_eq_of_coefficientEmbedding_eq`

 Let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto the elements of `G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that
fix `e E`. Let `k` be a Kummer chart of `Γ` (a subring `W(𝔽_{ℓ^f})⟦z⟧` of `A_inf` adapted to `Γ`)
that is unramified, with `f = k.f`, and let `ζ` in `O` be a primitive `(ℓ ^ f - 1)`-th root of
unity. If `g ζ = g' ζ`, where `coefficientEmbedding O g` is the embedding `x ↦ g x` of `O ⊆ ℚ̄_ℓ`
into `ℂ_ℓ`, then `g` and `g'` give the same complex embedding of `E`. 

### `New.Selmer.pow_ordProj_pow_sub_one_eq_one`

 If a Frobenius `F` for `ℓ ^ f` (`IsFrob (intQpBar ℓ) (ℓ ^ f) F`) fixes a primitive `N`-th root
of unity `z`, then `z ^ ℓ ^ v` is an `(ℓ ^ f - 1)`-th root of unity. Here `v = N.factorization ℓ` is
the `ℓ`-adic valuation of `N`, so `z ^ ℓ ^ v` has order prime to `ℓ`. 

### `New.Selmer.notMem_bPlaces_of_coefficientEmbedding_eq_pow`

 No three b-places follow one another closely along `z ↦ z ^ ℓ`, for `ℓ ≤ D.k * D.t`. Here
`D.bPlaces` is the sparse set of infinite places of `E = D.E` of weight `D.natB`. Let `j : Γ → G_ℓ`
be an open embedding onto the elements that fix `e E`, let its image contain `F` acting as
`x ↦ x ^ ℓ ^ f` on the residue field of the valuation ring `intQpBar ℓ` of `ℚ̄_ℓ`, and let `ζ` in
`O` be a primitive `(ℓ ^ f - 1)`-th root of unity. Write `g ζ` for `coefficientEmbedding O g ζ`. If
`g₁ ζ = (g₀ ζ) ^ ℓ ^ a` and `g₂ ζ = (g₀ ζ) ^ ℓ ^ (a + b)` with `1 ≤ a, b ≤ ⌊log_ℓ (D.halfGap ^ 3)⌋`,
and the complex embeddings `complexEmbeddingOf e g` of `E` for `g = g₀` and `g = g₂` lie at places
in `D.bPlaces`, then that for `g = g₁` does not. 

### `New.Selmer.eventually_exists_lettersReadThick`

 Let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto the elements of `G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that
fix `e E`, where `E = D.E`, and put `Q = D.k * D.t`. For `O` large there are a Kummer chart of `Γ`
(a subring `W(𝔽_{ℓ^f})⟦z⟧` of `A_inf` adapted to `Γ`, of ramification `k.e` and with `f = k.f`) `k`,
an element `ζ` of `O` with `ζ ^ (ℓ ^ f - 1) = 1`, a predicate `T` and a sign `s` on `ℂ_ℓ` with the
following properties, the clauses of `LettersReadThick`. The degree `k.e * k.f` is `[G_ℓ : Γ]` and
`k.e ≤ h₂ = D.halfGap`. Write `g ζ` for `coefficientEmbedding O g ζ` and
`σ = complexEmbeddingOf e g`. The place of `σ` lies in the set `D.bPlaces` of places of weight
`D.natB` if and only if `T (g ζ)`, and the sign `cmSign σ` of `σ` for the CM type is `s (g ζ)`; this
holds for every `g` if `Q < ℓ`, and otherwise for the `g` at b-places. The chart is unramified with
`7 ≤ ℓ`, or else `ℓ ≤ Q` and `s` is constant. For `ℓ ≤ Q` no three values with `T` follow one
another at distances `≤ log_ℓ h₂³` along `z ↦ z ^ ℓ`. 

### `New.Selmer.mem_range_of_modEq_one`

 Let `j : Γ → Gp ℓ` identify `Γ` with the completion group of an embedding `e` of `D.E`
(`IsCompletionGroup e j`). If `ℓ ≡ 1` modulo `D.cyclotomicConductor`, then all of `Gp ℓ` fixes the
image of `E`, so `j` is onto. 

### `New.Selmer.IsMainSummandWeights.le_two_mul_natAbs`

 Every jump `u` of a main summand, that is every member of a multiset `J σ` that satisfies
`New.Selmer.IsMainSummandWeights`, has `|u| ≥ h₂ / 2` with `h₂ = D.halfGap`: either it is low, so
that `|u| ≥ Δ / 4` with `Δ = D.gap = 2 h₂`, or it lies within `D.t` of the weight `∓ w_i` of the
data, signed by the CM type (`cmSign`), and `w_i ≥ h₂ ≥ 3 D.t`. 

### `New.Selmer.two_mul_tame_exponent_le_defectBound`

 Let `ℓ = D.levelPrime n` be one of the two level primes of the data `D`, let `r = D.r` be the
rank, `t = D.t = 5 r` and `0 < x ≤ t`. The number `3 r² ((r + t) r + 1)² + 150 (h₂² + 4 t + 2)` is
the exponent of `ℓ` that `New.Lift.hasCupExponent_of_isTameType` gives at the sizes of the data.
Twice this number is at most `defectBound D ℓ / x`, with
`defectBound D ℓ = 10⁶ (m / k) (b v_ℓ(M) + λ)` in the nonnegative reals, where `m = D.m`,
`k = D.k = D.r + 1 - m`, `b = D.natB` is the weight at the b-places, `M = D.M` is the product of the
two level primes, and `λ = crystallineLoss h₂ b ℓ` is the `ℓ`-adic valuation of
`(2 b)! (∏ a) ^ h₂³`, with `a` over the positive integers in `(b - 30 h₂³, b + 30 h₂³]` and
`h₂ = D.halfGap = D.r ^ 8`. The term `10⁶ (m / k) b v_ℓ(M) / x` suffices. 

### `New.Selmer.crystalline_bound_le_defectBound`

 Let `t = D.t = 5 D.r` and `0 < x ≤ t`. Then
`10⁵ (ρ ⌊2 λ / (k t)⌋ m + ⌊ρ m / (k x)⌋ λ) ≤ ρ · defectBound D ℓ / x`, with
`defectBound D ℓ = 10⁶ (m / k) (b v_ℓ(M) + λ)` in the nonnegative reals, where `m = D.m`,
`k = D.k = D.r + 1 - m`, `b = D.natB` is the weight at the b-places, `M = D.M` is the product of the
two level primes, and `λ = crystallineLoss h₂ b ℓ` is the `ℓ`-adic valuation of
`(2 b)! (∏ a) ^ h₂³`, with `a` over the positive integers in `(b - 30 h₂³, b + 30 h₂³]` and
`h₂ = D.halfGap = D.r ^ 8`. The left side is the bound of
`New.Selmer.normLength_dualDefect_le_of_crystallineSizes` for a lattice of rank `ρ`, with `Q = k t`
and `μ = ⌊ρ m / (k x)⌋`. 

### `New.Selmer.IsSummandClass`

 The lattices `L i` are the summands at a place above `ℓ`, and `F`, `K`, `U` are the data of a
class `New.Lift.InClass F K U` adapted to them. The summand `L none` is the main summand, of rank
`r` and with jumps `J g` at `coefficientEmbedding O g`; the summand `L (some c)` has the single jump
`c < t`. 

### `New.Selmer.IsSummandClass.tame_or_crystalline`

 The class is tame, with `ℓ` one of the primes `D.levelPrime n`, or crystalline with no
  condition on inertia. 

### `New.Selmer.IsSummandClass.exists_jump_ne_zero`

 Every jump allowed by `U` is a jump of one of the summands. 

### `New.Selmer.IsSummandClass.hasJumps_none`

 The main summand has the jumps `J`. 

### `New.Selmer.IsSummandClass.hasJumps_some`

 The summand `L (some c)` has the single jump `c`. 

### `New.Selmer.IsSummandClass.finrank_none`

 The main summand has rank `r`. 

### `New.Selmer.crystallineSizes_data`

 The data satisfy the size conditions `CrystallineSizes` with `Q = D.k * D.t`, `m = D.m`,
`h = D.halfGap`, `G = D.offWeight`, `b = D.natB`, `η = h² + 1`, `W = 4 D.t` and the shift
`δ = i D.gap + h - 2 D.t`, for `i ≤ D.m`; each condition is a comparison of logarithmic scales. 

### `New.Selmer.hasFewLowJumps_tateDual_of_isMainSummandWeights`

 Put `h₂ = D.halfGap`, `m = D.m` and `k = D.k = D.r + 1 - m`. Let the multisets `J σ`, for the
complex embeddings `σ` of `D.E`, be the weights of a main summand. Let `L` be a potentially
crystalline lattice over the ring of integers `O` of a finite Galois extension of `ℚ_ℓ`, with an
action of `Γ → G_ℓ`, whose Hodge–Tate jumps at each embedding `γ` of `O`, with multiplicity
`jump L.ρ γ u`, are `J (σ γ)`. Let `U γ` consist of members of `J (σ γ)` and integers in `[0, t)`,
and `U' γ` of jumps of the Tate dual of `L`. Then the dual has few low jumps (`HasFewLowJumps`): the
negative members of `U γ` and `U' γ` are at most `-h₂ / 2`, and at most `⌊r m / k⌋` of its jumps at
`γ` lie in `[-h₂² - 1, h₂² + 1]`. 

### `New.Selmer.subset_Icc_of_jump_eq_single`

 If the lattice `L` is potentially crystalline with the single Hodge–Tate jump `c < D.t`, then
every jump of its Tate dual, which is `-c - 1`, lies in `[-h₂² - 1, 0]`, where `h₂ = D.halfGap`. 

### `New.Selmer.normLength_dualDefect_le_defectBound_of_isTameType`

 The tame case, at one of the two level primes `ℓ = D.levelPrime n` of the data `D`. Here `D.r`
is the rank parameter of the data and `D.t = 5 D.r`; the rank of the lattice `L` is arbitrary.
Let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto the elements of
`G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that fix `e E`, where `E = D.E`. A lattice lies in `InClass F K U` if its
crystalline periods fixed on a neighbourhood of `1` that belongs to the filter `F` span, its
Hodge–Tate jumps at each embedding `γ` of `O` lie in `U γ`, and each polynomial allowed by `K s`
kills `s` on its periods, for `s` in inertia. Assume:
* `hL`: `L` lies in the class for `F`, `s ↦ K s⁻¹` and `U'`;
* `h_tame`: for each `s` in inertia (`IsWeilPair (𝒥.toGp s) 0`) the condition `K s` on polynomials
  holds for `X ^ e' - 1`, with `e'` the least common multiple of the `ℓ ^ a - 1` for `1 ≤ a ≤ D.r`,
  and for a monic polynomial over `ℤ_ℓ` of degree at most `(D.r + D.t) D.r` (`IsTameType`);
* `hU`, `hU'`: with `η = h₂² + 1`, the sign `ε = cmSign σ` of a complex embedding `σ` for the CM
  type, and `S = farWindowStart D i σ` (the `i`-th lift weight at `σ` minus `2 D.t`, `i ≤ D.m`),
  each `U γ` lies in `[-η, η] ∪ -ε · [S, S + 4 D.t]` and each `U' γ` in
  `[-η, η] ∪ ε · [S, S + 4 D.t]`.

Then the defect of `L` for the class `InClass F K U`, the length of the crystalline cocycles modulo
those orthogonal, under cup products, to the crystalline cocycles of the lattices in the class,
normalised so that `O / ℓ` has length `1`, is at most `[G_ℓ : Γ] · rank L · defectBound D ℓ / x` for
`0 < x ≤ D.t`. Here `defectBound D ℓ = 10⁶ (m / k) (b v_ℓ(M) + λ)` in the nonnegative reals, where
`m = D.m`, `k = D.k = D.r + 1 - m`, `b = D.natB` is the weight at the b-places, `M = D.M` is the
product of the two level primes, and `λ = crystallineLoss h₂ b ℓ` is the `ℓ`-adic valuation of
`(2 b)! (∏ a) ^ h₂³`, with `a` over the positive integers in `(b - 30 h₂³, b + 30 h₂³]` and
`h₂ = D.halfGap = D.r ^ 8`. 

### `New.Selmer.normLength_dualDefect_le_of_isSummandClass`

 The defect bound at one place above `ℓ`. Let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto the
elements of `G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that fix `e E`, where `E = D.E`; each `g` in `G_ℓ` gives a
complex embedding `complexEmbeddingOf e g` of `E`. Let the multisets `J σ` be the weights of a main
summand (`IsMainSummandWeights`): `1 ≤ r ≤ D.r`, `t ≤ D.t = 5 D.r`, each member `u` of `J σ` has
`h₂ / 2 ≤ |u| ≤ 4 m h₂` or lies within `D.t` of `∓ w_i(σ)` for one lift weight
`w_i = D.liftWeight i` with `i ≤ m`, at most `r m / k` members have `|u| ≤ 2 h₂²`, and at most `r`
members of `J σ` and `J σ̄` together are negative. Here `O` runs over the rings of integers of
finite Galois extensions of `ℚ_ℓ`, and large means containing a given one. Let `O` be large. A
lattice lies in `InClass F K U` if its crystalline periods fixed on a neighbourhood of `1` that
belongs to the filter `F` span, its Hodge–Tate jumps at each embedding `γ` of `O` lie in `U γ`, and
each polynomial allowed by `K s` kills `s` on its periods, for `s` in inertia. Let the class be
adapted to the lattices `L c` (`IsSummandClass`): it is tame with `ℓ` a level prime of `D`, or
crystalline (`F = ⊤`, `K = ⊥`); each member of `U γ` is a jump of some `L c`; the main summand
`L none` has rank `r` and jumps `J (complexEmbeddingOf e g)` at the embedding `a ↦ g a` of `O`; and
`L (some c)` has the single jump `c`. If `L c` lies in the class, then the defect of its Tate dual,
the length of the crystalline cocycles modulo those orthogonal, under cup products, to the
crystalline cocycles of the lattices in the class, normalised so that `O / ℓ` has length `1`, is at
most `[G_ℓ : Γ] · rank (L c) · defectBound D ℓ / x`, where `x = 1` for the main summand and
`x = D.t` otherwise. Here `defectBound D ℓ = 10⁶ (m / k) (b v_ℓ(M) + λ)` in the nonnegative reals,
where `m = D.m`, `k = D.k = D.r + 1 - m`, `b = D.natB` is the weight at the b-places, `M = D.M` is
the product of the two level primes, and `λ = crystallineLoss h₂ b ℓ` is the `ℓ`-adic valuation of
`(2 b)! (∏ a) ^ h₂³`, with `a` over the positive integers in `(b - 30 h₂³, b + 30 h₂³]` and
`h₂ = D.halfGap = D.r ^ 8`; the division by `x` is exact. 

### `New.Selmer.summand_defect_le_at_place`

 The bound of `New.Selmer.normLength_dualDefect_le_of_isSummandClass`, with the clauses of
`New.Selmer.IsSummandClass` as separate hypotheses. Let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto
the elements of `G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that fix `e E`, where `E = D.E`. Let the multisets `J σ`,
for the complex embeddings `σ` of `E`, be the weights of a main summand (`IsMainSummandWeights`):
`1 ≤ r ≤ D.r`, `t ≤ D.t = 5 D.r`, each member `u` of `J σ` has `h₂ / 2 ≤ |u| ≤ 4 m h₂` or lies
within `D.t` of `∓ w_i(σ)` for one lift weight `w_i = D.liftWeight i` with `i ≤ m`, at most
`r m / k` members have `|u| ≤ 2 h₂²`, and at most `r` members of `J σ` and `J σ̄` together are
negative. Let the coefficient ring `O` be large. The class `InClass F K U` of lattices (given by
admissibility along `F`, polynomial conditions `K s` on inertia and allowed Hodge–Tate jumps `U γ`)
is crystalline without condition on inertia, or tame: `ℓ` is one of the two level primes
`D.levelPrime n`, and for each `s` in inertia (`IsWeilPair (𝒥.toGp s) 0`) the condition `K s` on
polynomials holds for `X ^ e' - 1`, with `e'` the least common multiple of the `ℓ ^ a - 1` for
`1 ≤ a ≤ D.r`, and for a monic polynomial over `ℤ_ℓ` of degree at most `(D.r + D.t) D.r`
(`IsTameType`). Each member of `U γ` is a jump of a summand `L i`. At the embedding
`coefficientEmbedding O g : a ↦ g a` of `O`, the main summand `L none`, of rank `r`, has the jumps
`J σ` for the complex embedding `σ = complexEmbeddingOf e g` given by `g`, and `L (some c)` has the
single jump `c`. If `L c` lies in the class, the defect of its Tate dual, the length of the
crystalline cocycles modulo those orthogonal, under cup products, to the crystalline cocycles of the
lattices in the class, normalised so that `O / ℓ` has length `1`, is at most
`[G_ℓ : Γ] · rank (L c) · defectBound D ℓ / x`, where `x = 1` for the main summand and `x = D.t`
otherwise. Here `defectBound D ℓ = 10⁶ (m / k) (b v_ℓ(M) + λ)` in the nonnegative reals, where
`m = D.m`, `k = D.k = D.r + 1 - m`, `b = D.natB` is the weight at the b-places, `M = D.M` is the
product of the two level primes, and `λ = crystallineLoss h₂ b ℓ` is the `ℓ`-adic valuation of
`(2 b)! (∏ a) ^ h₂³`, with `a` over the positive integers in `(b - 30 h₂³, b + 30 h₂³]` and
`h₂ = D.halfGap = D.r ^ 8`. 
