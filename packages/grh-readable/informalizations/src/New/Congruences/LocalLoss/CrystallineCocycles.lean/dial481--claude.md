---
{
  "module": "src/New/Congruences/LocalLoss/CrystallineCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Crystalline cocycles and the defect of a crystalline lattice at a place above ℓ

This file gives local estimates at a place above ℓ for the module `New.Period.crysCocycles` of
crystalline cocycles of a Galois lattice `L` over a coefficient ring `O`. Throughout, the instance
`OverGp Γ ℓ` gives a homomorphism j from `Γ` to G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ) with open image.
`New.CoeffRing.normLength` normalises lengths so that `O / ℓ` has length `1`. For a crystalline
lattice, the defect `New.Lift.dualDefect` for a class of lattices is the length of the cocycles
modulo those in the annihilator `New.Lift.cupOrthogonal` of the lattices in the class. This file
computes the rank of the crystalline cocycles and bounds the normalised defect of a lattice whose
jumps lie in windows, under the size conditions `New.Selmer.CrystallineSizes`.

## Main definitions and results

* `New.Selmer.finrank_crysCocycles_eq_add_neg_jumps`: the rank is `rank L` plus the number of
  negative Hodge–Tate jumps at the embeddings that belong to the place.
* `New.Selmer.normLength_dualDefect_le_of_hasCupExponent`: if a power ℓ^k carries the cocycles into
  the annihilator of a class of lattices, as `New.Lift.HasCupExponent` says, then the defect is
  bounded in terms of k.
* `New.Selmer.normLength_dualDefect_le_of_crystallineSizes`: the defect is bounded in terms of the
  crystalline loss `New.Selmer.crystallineLoss`, uniformly in `ℓ`.

Notions from other files:
* `New.Lift.GalLattice`: A finite free O-module with a compatible ℤ_ℓ-module structure, together
  with an O-linear representation of the group Γ on it.
* `New.Period.IsPotentiallyCrystalline`: for a representation on T and the crystalline period ring
  B, the elements of B⊗T fixed by all g with j(g) near 1 span B⊗T over B.
* `New.Period.crysCocycles`: Z_f(T), the module, over the coefficient ring, of maps c: Γ → T such
  that some y in B⊗T has 1⊗c(g) = gy − y for all g.
* `New.Period.jump`: The multiplicity of the Hodge–Tate jump u at γ: the dimension over ℚ̄_ℓ (zero
  if infinite) of the space `New.Period.hodgeTateMaps`.

## Relation to the literature

See `New.Congruences.LocalLoss.CrystallineDefect` for related work.



## Rank of crystalline cocycles and a length bound

`New.Period.HasJumps ρ γ J` says that `J` is the multiset of jumps at the coefficient embedding `γ`.


### `matrixLattice`

 The Γ-lattice over R given by the module R^n with Γ acting through the matrix representation
ρ. 

### `finrank_crysCocycles_eq_add_neg_jumps`

 Let `E` be a CM field containing a primitive `5040`-th root of unity, `e` an embedding of `E`
into `ℚ̄_ℓ`, and let `𝒥.toGp : Γ → G_ℓ` be an open embedding onto the elements of
`G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` that fix `e E` (`h_group`). Let `O` be the ring of integers of a finite
Galois extension of `ℚ_ℓ` and `L` a potentially crystalline `O`-lattice with action of `Γ`. For `g`
in `G_ℓ`, `coefficientEmbedding O g` is the embedding `x ↦ g x` of `O` into `ℂ_ℓ`, and
`complexEmbeddingOf e g` is the complex embedding `ι⁻¹ ∘ g⁻¹ ∘ e` of `E`, with `ι : ℂ ≃ ℚ̄_ℓ` the
isomorphism fixed by `PadicIso ℓ`. Suppose that for each `g` the Hodge–Tate jumps of `L` at the
first are the multiset `J` at the second. Then the rank of the module of crystalline cocycles of `L`
is `rank L` plus the number of negative jumps, summed over the distinct embeddings `ι⁻¹ ∘ g⁻¹ ∘ e`
of `E`.

A case of the Bloch–Kato rank formula for crystalline cocycles. 

### `normLength_dualDefect_le_of_hasCupExponent`

 From an exponent to the defect. Let `L` be potentially crystalline, and let `ℓ ^ k` carry the
crystalline cocycles of `L` into `cupOrthogonal 𝒬 L`, the functions orthogonal to the lattices in
`𝒬` under the cup product (this is `HasCupExponent 𝒬 L k`). The defect `dualDefect 𝒬 L` is the
length of the crystalline cocycles modulo `cupOrthogonal 𝒬 L`. Then this defect, normalised so that
`O / ℓ` has length `1` (`normLength`), is at most `y` times the index of the image of `Γ` under
`𝒥.toGp` in `G_ℓ`, for any `y ≥ 2 k · rank L`. 


## The defect of a crystalline lattice with jumps in a window

`New.Lift.FitsWindows η ε b W U` says that the jump set `U` lies in the union of the low window
`[-η, η]` and the far window `ε [b, b + W]`.


### `New.Selmer.le_crystallineLoss_of_pow_dvd`

 The crystalline loss `crystallineLoss h b ℓ` is the `ℓ`-adic valuation of `(2 b)!` times the
`h³`-th power of the product of the positive integers in `(b - 30 h³, b + 30 h³]`. If `ℓ ^ n`
divides this number, then `n ≤ crystallineLoss h b ℓ`. 

### `New.Selmer.two_mul_lt_mul_crystallineLoss_succ`

 The bound `2 b < ℓ (crystallineLoss h b ℓ + 1)` on the crystalline loss `crystallineLoss h b ℓ`,
the `ℓ`-adic valuation of `(2 b)! (∏ k) ^ h³`, where `k` runs over the positive integers in
`(b - 30 h³, b + 30 h³]`. The factor `(2 b)!` alone gives it. 

### `New.Selmer.cube_le_crystallineLoss_of_dvd`

 If `ℓ` divides some positive integer in `(b - 30 h³, b + 30 h³]`, then the crystalline loss
`crystallineLoss h b ℓ` is at least `h³`. 

### `New.Selmer.natLog_lt_of_two_mul_log_lt`

 If `H ≤ 4 b` and `2 log (4 b) < m`, then `⌊log_ℓ H⌋ < m`, because `log ℓ ≥ 1 / 2`. 

### `New.Selmer.noMultipleNear_of_forall_not_dvd`

 Suppose that `ℓ > G + δ + n` divides no integer in `(b - c, b + c]` and that `δ + n < c`. Then
`NoMultipleNear ℓ n a` holds for `a = b + δ` and for `a = G + δ`: `ℓ` divides no nonzero integer
within `n` of `0` or `± a`. 

### `New.Selmer.CrystallineSizes`

 The size conditions of the crystalline bound: `Q² ≪ h`, `h³ ≪ G`, `h³ G ≪ b`, `log b ≪ m` and
`Q η ≪ h³`, with `δ < η`. Here `A ≪ B` stands for `99 A ≤ B`, except in the logarithmic one. 

### `New.Selmer.CrystallineSizes.bound_pos`

 The bound `Q` for small primes is positive. 

### `New.Selmer.CrystallineSizes.sq_le`

 `Q² ≪ h`, with room for the width `W` of the far windows and for `m`. 

### `New.Selmer.CrystallineSizes.cube_le`

 `h³ ≪ G`. 

### `New.Selmer.CrystallineSizes.mul_cube_le`

 `h³ G ≪ b`. 

### `New.Selmer.CrystallineSizes.log_lt`

 `2 log (4 b) < m`. 

### `New.Selmer.CrystallineSizes.shift_lt`

 The shift `δ` of the far windows is less than the radius `η` of the low window. 

### `New.Selmer.CrystallineSizes.low_le`

 `Q η ≪ h³`, with room for `W Q` and `h`. 

### `New.Selmer.HasFewLowJumps`

 The lattice `L` has few low jumps: at each embedding the negative members of `U` and `U'` are
at most `-h / 2`, and at most `μ` jumps of `L` lie in `[-η, η]`. 

### `New.Selmer.HasFewLowJumps.two_mul_le`

 The negative members of `U g` and `U' g` are at most `-h / 2`. 

### `New.Selmer.HasFewLowJumps.sum_jump_le`

 At most `μ` jumps of `L` at `g`, counted with multiplicity, lie in `[-η, η]`. 

### `New.Selmer.LettersReadThick`

 `LettersReadThick k letter th ε Q h T s`: for embeddings `g` indexed by `ι`, with thickness
`th g` and sign `ε g`, the value `letter g` in `ℂ_ℓ` determines both by the functions `T` and `s`,
at thick `g` and, if `Q < ℓ`, at every `g`. Here `k` is a Kummer chart, the prime `ℓ` is small if
`ℓ ≤ Q`, and `h` bounds the ramification. The degree of `k` is the index of `Γ`, the chart is
unramified with `ℓ ≥ 7`, or `ℓ ≤ Q` and all signs agree; for `ℓ ≤ Q` thick letters are sparse. 

### `New.Selmer.LettersReadThick.e_mul_f_eq_index`

 The degree `e f` of the chart is the index of the image of `Γ` in `G_ℓ`. 

### `New.Selmer.LettersReadThick.e_le`

 The ramification `e` of the chart is at most `h`. 

### `New.Selmer.LettersReadThick.thick_iff`

 The letter reads thickness at thick embeddings, and at all embeddings if `Q < ℓ`. 

### `New.Selmer.LettersReadThick.sign_eq`

 The letter reads the sign at thick embeddings, and at all embeddings if `Q < ℓ`. 

### `New.Selmer.LettersReadThick.isUnramified_or_sign_eq`

 The chart is unramified with `ℓ ≥ 7`, or `ℓ ≤ Q` and all letters have the same sign. 

### `New.Selmer.LettersReadThick.not_thick_pow`

 For `ℓ ≤ Q` no three thick letters, that is letters with `T`, follow one another at
  distances `≤ log_ℓ h³` in an orbit of `z ↦ z ^ ℓ`. 

### `New.Selmer.fitsWindows_letterJumps`

 Let `k` be a Kummer chart of `Γ`. Its letters `i` are the units of `𝔽_{ℓ^f}`, and
`ω = theta (k.letterTeich i)` is the root of unity in `ℂ_ℓ` that Fontaine's map `θ` gives to the
Teichmüller lift of `i`; `ζ` in `O` has `ζ ^ (ℓ ^ f - 1) = 1`. `FitsWindows η ε a W V` says
`V ⊆ [-η, η] ∪ ε · [a, a + W]`. Let the jump sets `U g` fit the windows with sign `ε g`, with
`a = b + δ` at thick `g` (`th g`) and `a = G + δ` at thin ones, and let `g ζ` determine thickness
and sign through `T` and `s` at thick `g`, and at all `g` if `Q < ℓ`. Then `k.letterJumps ζ U i`,
the union of `{0}` and the `U g` with `g ζ = ω`, fits the windows given by `T ω` and `s ω`, with the
low window widened to `[-2 G, 2 G]` if `ℓ ≤ Q`: it holds the old low window as `η ≤ G`, and the far
windows of the thin `g` as `δ + W ≤ G`. 

### `New.Selmer.CrystallineSizes.differentBound_mul_add_log_le`

 Assume the size conditions `CrystallineSizes`, that the ramification index `e` of the Kummer
chart `k` is at most `h`, and that `2 (b + δ) < h² K`. Then `20 (⌊log_ℓ h³⌋ + 1 + d) · 2 G + ⌊log_ℓ
(2 (b + δ + 10 G))⌋ ≤ K`, where `d = k.differentBound` is `0` if `e = 1` and `v_ℓ(e) + 1`
otherwise. 

### `New.Selmer.LettersReadThick.hasCupExponent_of_le`

 The exponent for small primes `ℓ ≤ Q`. Let `Γ → G_ℓ` be an open embedding. The hypothesis
`h_sizes` is the list of inequalities `Q² ≪ h`, `m ≪ h`, `W Q ≪ h`, `h³ ≪ G`, `h³ G ≪ b`,
`Q η ≪ h³`, `2 log (4 b) < m` and `δ < η`. `InClass ⊤ ⊥ U` is the class of crystalline lattices
whose Hodge–Tate jumps at each embedding `g` of `O` lie in `U g`; let `L` lie in the class for `U'`.
Let `k` be a Kummer chart of `Γ`. The letters `i` of `k` are the units of `𝔽_{ℓ^f}`; `ζ` in `O` has
`ζ ^ (ℓ ^ f - 1) = 1`, and `k.letterJumps ζ U i` is the union of `{0}` and the sets `U g` for the
embeddings `g : O → ℂ_ℓ` such that `g ζ` is the Teichmüller root of unity of `i`. The predicate `T`
(thick) and the sign `s` on `ℂ_ℓ` satisfy `LettersReadThick`: the ramification of `k` is at most
`h`, the chart is unramified with `ℓ ≥ 7` or `s` is constant, and thick values are sparse along
`z ↦ z ^ ℓ`; `ι`, `letter`, `th`, `ε` enter only through `h_chart`. At each letter let the jumps
from `U` and `U'` lie in the union of `[-2 G, 2 G]` and opposite far windows of width `W`, starting
at `b + δ` if the letter is thick and at `G + δ` otherwise. If `2 (b + δ) < h² K`, then
`ℓ ^ (10⁴ K (⌊log_ℓ h³⌋ + 1))` times any crystalline cocycle of `L` is orthogonal under cup products
to the class for `U`. 

### `New.Selmer.CrystallineSizes.hasCupExponent_of_cube_le`

 The exponent for large primes `ℓ > Q` and large loss `v ≥ h³`. Let `Γ → G_ℓ` be an open
embedding and `ℓ ≥ 7`. The hypothesis `h_sizes` is the list of inequalities `Q² ≪ h`, `m ≪ h`,
`W Q ≪ h`, `h³ ≪ G`, `h³ G ≪ b`, `Q η ≪ h³`, `2 log (4 b) < m` and `δ < η`. `InClass ⊤ ⊥ U` is the
class of crystalline lattices whose Hodge–Tate jumps at each embedding `g` of `O` lie in `U g`; let
`L` lie in the class for `U'`. Let `k` be a Kummer chart of `Γ`, unramified. The letters `i` of `k`
are the units of `𝔽_{ℓ^f}`; `ζ` in `O` has `ζ ^ (ℓ ^ f - 1) = 1`, and `k.letterJumps ζ U i` is the
union of `{0}` and the sets `U g` for the embeddings `g : O → ℂ_ℓ` such that `g ζ` is the
Teichmüller root of unity of `i`. At each letter let the jumps from `U` and `U'` lie in the union of
`[-η, η]` and the far windows `-s i · [a, a + W]` and `s i · [a, a + W]`, where `a = b + δ` if `T i`
holds and `a = G + δ` otherwise. If `2 b < ℓ (v + 1)` and `2 v < (K + 1) Q`, then `ℓ ^ (10⁴ K m)`
times any crystalline cocycle of `L` is orthogonal under cup products to the class for `U`. 

### `New.Selmer.CrystallineSizes.noMultipleNear`

 The gap condition for small loss. Under the size conditions `h_sizes`, let `2 b < ℓ (v + 1)`
with `v < h³`, and let `ℓ` divide no integer in `(b - 30 h³, b + 30 h³]`. Then `ℓ` divides no
nonzero integer within `6 (2 (v + 1) + η + W)` of `0` or `± a`, for `a = b + δ` and `a = G + δ`. 

### `New.Selmer.normLength_dualDefect_le_of_noMultipleNear`

 Let `Γ → G_ℓ` be an open embedding, `ℓ ≥ 7`, and `O` the ring of integers of a finite Galois
extension of `ℚ_ℓ`. The hypothesis `h_sizes` is the list of inequalities `Q² ≪ h`, `m ≪ h`,
`W Q ≪ h`, `h³ ≪ G`, `h³ G ≪ b`, `Q η ≪ h³`, `2 log (4 b) < m` and `δ < η`. `InClass ⊤ ⊥ U` is the
class of crystalline lattices whose Hodge–Tate jumps at each embedding `g` of `O` lie in `U g`; let
the `O`-lattice `L` lie in the class for `U'`. Let `k` be a Kummer chart of `Γ`, unramified and with
`f = [G_ℓ : Γ]`. The letters `i` of `k` are the units of `𝔽_{ℓ^f}`; `ζ` in `O` has
`ζ ^ (ℓ ^ f - 1) = 1`, and `k.letterJumps ζ U i` is the union of `{0}` and the sets `U g` for the
embeddings `g : O → ℂ_ℓ` such that `g ζ` is the Teichmüller root of unity of `i`. Assume:
* `hU`, `hU'`: at each letter the jumps from `U` and `U'` lie in the union of `[-η, η]` and the far
  windows `-s i · [a, a + W]` and `s i · [a, a + W]`, where `a = b + δ` if `T i` holds and
  `a = G + δ` otherwise;
* `h_jumps`: either the negative members of all `U g` and `U' g` are at most `-h / 2` and at most
  `μ` jumps of `L` at each `g` lie in `[-η, η]`, or every `U' g` lies in `[-η, 0]`;
* `2 b < ℓ (v + 1)`, `v < h³` and `2 v < (K + 1) Q`;
* `h_gap`: `ℓ` divides no nonzero integer within `6 (2 (v + 1) + η + W)` of `0` or `± a`.

Then the defect of `L` for the class of `U`, the length of the crystalline cocycles modulo those
orthogonal, under cup products, to the crystalline cocycles of the lattices in the class, normalised
so that `O / ℓ` has length `1`, is at most `[G_ℓ : Γ] · y` for any
`y ≥ 10⁵ (rank L · K m + μ v)`. 

### `New.Selmer.normLength_dualDefect_le_of_crystallineSizes`

 Let `Γ → G_ℓ = Gal(ℚ̄_ℓ / ℚ_ℓ)` be an open embedding (`h_open`), `O` the ring of integers of a
finite Galois extension of `ℚ_ℓ`, and `L` a finite free `O`-module with an action of `Γ`. Each
embedding `g` of `O` into `ℂ_ℓ` is thick (`th g`) or thin, has a sign `ε g`, and has finite sets
`U g` and `U' g` of allowed Hodge–Tate jumps; `InClass ⊤ ⊥ U` is the class of crystalline lattices
whose jumps at each `g` lie in `U g`. Assume:
* `h_sizes`: `Q² ≪ h`, `h³ ≪ G`, `h³ G ≪ b`, `Q η ≪ h³`, `2 log (4 b) < m` and `δ < η`, in the
  explicit form of `CrystallineSizes`;
* `hU`, `hU'`: with `a = b + δ` at thick `g` and `a = G + δ` at thin `g`, the set `U g` lies in
  `[-η, η] ∪ -ε g · [a, a + W]` and `U' g` lies in `[-η, η] ∪ ε g · [a, a + W]`;
* `hL`: `L` is crystalline with jumps in `U'`;
* `h_jumps`: either the negative members of all `U g` and `U' g` are at most `-h / 2` and at most
  `μ` jumps of `L` at each `g` lie in `[-η, η]`, or every `U' g` lies in `[-η, 0]`;
* `h_chart`: `k` is a Kummer chart of `Γ` of degree `e f = [G_ℓ : Γ]` and ramification `e ≤ h`, and
  `ζ` in `O` has `ζ ^ (ℓ ^ f - 1) = 1`. At thick `g`, and at all `g` if `Q < ℓ`, thickness is
  `T (g ζ)` and the sign is `s (g ζ)`. The chart is unramified with `ℓ ≥ 7`, or `ℓ ≤ Q` and `s` is
  constant. If `ℓ ≤ Q`, no three values with `T` follow one another at distances at most `log_ℓ h³`
  along `z ↦ z ^ ℓ`;
* `hy`: `y ≥ 10⁵ (rank L · ⌊2 λ / Q⌋ · m + μ λ)`, where `λ = crystallineLoss h b ℓ` is the `ℓ`-adic
  valuation of `(2 b)! (∏ n) ^ h³`, with `n` over the positive integers in `(b - 30 h³, b + 30 h³]`.

The defect `dualDefect (InClass ⊤ ⊥ U) L` is the length of the crystalline cocycles of `L` modulo
those orthogonal, under cup products, to the crystalline cocycles of all lattices in the class.
Normalised so that `O / ℓ` has length `1`, it is at most `[G_ℓ : Γ] · y`. 
