---
{
  "module": "src/New/Congruences/Lifting/CupOrthogonalityBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupOrthogonalityBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupOrthogonalityBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From sides to lattices: few low jumps, b-letters and tame types

Bounds for the power of p that makes the crystalline cocycles `New.Period.crysCocycles` of a lattice
L orthogonal (`New.Lift.cupOrthogonal`, under cup product) to a class of lattices
`New.Lift.InClass`. The class is given by admissibility, jump sets and polynomials that kill
inertia. The estimates themselves are proved for sides (`New.Lift.KummerChart.PairingSide`) over a
Kummer chart `New.Lift.KummerChart`. This file passes to lattices.

* `New.Lift.KummerChart.universalSide`,
  `New.Lift.KummerChart.pow_smul_mem_cupOrthogonal_of_isScaledCupCoboundary`: the side of all
  crystalline cocycles of L, and orthogonality from the relation
  `New.Lift.Pairing.IsScaledCupCoboundary` for all paired sides.
* `New.Lift.KummerChart.dualDefect_eq_zero_and_dualDefect_le`: the defect `New.Lift.dualDefect` is 0
  if there is no small negative jump, and is bounded if there are few low jumps.
* `New.Lift.KummerChart.hasCupExponent_any_pattern`,
  `New.Lift.KummerChart.hasCupExponent_sparse_thick`: explicit exponents (`New.Lift.HasCupExponent`)
  for any pattern of b-letters and for sparse b-letters.
* `New.Lift.hasCupExponent_of_isTameType`: an explicit exponent for tame inertial types
  (`New.Lift.IsTameType`).

Jumps lie in windows `New.Lift.FitsWindows` = [−η, η] ∪ ε[b, b + W]. An embedding g of O lies
over the letter i if g ζ = θ(ω(i)), where ζ is a root of unity in O and ω(i) is the Teichmüller lift
of i. The jump set `New.Lift.KummerChart.letterJumps` at i collects 0 and the sets U g for the g
over i.

Notions from other files:
* `New.Lift.KummerChart.LetterRoot`: The elements ζ of O with ζ^q = 1, where q = p^f − 1 is the
  number of letters of the chart.
* `New.Lift.KummerChart.Letter`: The letters of a Kummer chart: the multiplicative group of the
  field with p^f elements in the tilt of the ring of integers of C_p.
* `New.Period.theta`: Fontaine's ring homomorphism θ from A_inf to the ring of integers of C_p,
  sending the Teichmüller lift [x] to x^♯.

## Relation to the literature

Over Q_p, take potentially crystalline lattices of tame inertial type with weights in two windows
small against p. For these, a power of p makes Bloch–Kato classes cup to zero with those of
congruent dual lattices. The exponent, used in the Selmer bound, depends on the sizes of the types
and windows but not on the ramification index. Small ramification, the tame potentially
Barsotti–Tate case and Kisin modules with descent data for generic tame types are treated in the
literature. Related work: Iovita–Marmora, Continuity of the finite Bloch–Kato cohomology, 2015;
Nekovář, Compatibility of arithmetic and algebraic local constants II, 2018; Le–Le Hung–Levin–Morra,
Local models for Galois deformation rings, 2023.

Work over unramified p-adic fields with p ≥ 5, where p divides no non-zero integer near 0 or the
large weights. There, crystalline classes modulo those cupping to zero with congruent dual lattices
have length O(1 + large weight/p) per low weight plus O(rank × (window width + 1)), times the
residue degree and the length of O/p, and zero length absent small negative weights. This bounds the
loss above p in the Selmer bound. No loss for weights below p−1, exact Breuil–Kisin sequences for
weights of one sign, and torsion located by weights modulo p are known in the literature. Related
work: Iovita–Marmora, Continuity of the finite Bloch–Kato cohomology, 2015; Čoupek–Gazaki–Marmora,
Exactness of Breuil–Kisin functors, 2026; Gao–Liu, Integral filtered Sen theory and applications,
2024.


### `IsTameType`

 `K` holds for `X ^ e - 1`, with `e` the least common multiple of the `p ^ i - 1` for
`1 ≤ i ≤ r`, and for some monic polynomial over `ℤ_[p]` of degree at most `N`. 

### `KummerChart.letterJumps`

 The jump set at the letter `i`: the union of `{0}` and the sets `U g` for the embeddings `g` of
`O` with `g ζ = θ(ω(i))`, where `ω(i)` is the Teichmüller lift `k.letterTeich i`. 

### `KummerChart.universalSide`

 Let the sets of the filter F contain the subgroup `k.subgroup` of the chart, and let L lie in
the class (`New.Lift.InClass`) along F with jump sets U. The side (a lattice with jump sets at the
letters and a parametrised module of cocycles) is formed by L, the parameter lattice Z_f(L) of all
crystalline cocycles, and the jump sets `New.Lift.KummerChart.letterJumps` of U at the letters.
Membership in the class makes L potentially crystalline, so Z_f(L) is finitely generated. 

### `KummerChart.mem_letterJumps`

 The jumps at the letter `i` are `0` and the elements of the sets `U g` of the embeddings `g`
with `g ζ = theta (k.letterTeich i)`, the image under `theta` of the Teichmüller lift of `i`. 

### `KummerChart.fitsWindows_letterJumps`

 If the sets `U g` of all embeddings `g` lie in a window `[-η, η] ∪ ε [b, b + W]`, then so does
the jump set `letterJumps` at each letter. 

### `FitsWindows.neg_add_sub_one_le`

 Let the set `V` lie in `[-η, η] ∪ -ε [b, b + W]` and `V'` in `[-η, η] ∪ ε [b, b + W]`, for a
sign `ε` and `η ≤ b`. Then `-(v + v') - 1 ≤ b + W + η` for `v ∈ V` and `v' ∈ V'`, since `v` and `v'`
cannot both lie in `-[b, b + W]`. 

### `KummerChart.le_of_mem_jumpSet_tateDualSide`

 Let `P` pair the lattices of the sides `S` and `S'`. The jumps at the letter `i` of the side
`P.tateDualSide` of the Tate dual of their tensor product are `0` and the `-(v + v') - 1`, with `v`
and `v'` jumps of `S` and `S'` at `i`; so a common bound `B ≥ 0` for these bounds its jump set. 

### `KummerChart.sum_card_algHom_le_finrank`

 Write `ω(i)` for the Teichmüller lift `k.letterTeich i` and `θ` for Fontaine's map `theta` from
`A_inf` to `O_C`. Let `ζ` be an element of `O` with `ζ ^ (p ^ k.f - 1) = 1`. An embedding `g` of `O`
into `ℂ_[p]` satisfies `g ζ = θ(ω(i))` for at most one letter `i`, so the numbers of such `g` for
the different letters add up to at most the rank of `O` over `ℤ_[p]`. 

### `length_quotient_mul_length_residueField`

 The length of `O / p` over `O` times the residue degree of `O` is the rank of `O` over
`ℤ_[p]`. 

### `InClass.sum_jump_le_finrank`

 For a lattice `L` in the class `InClass F K U` and an embedding `g : O →ₐ[ℤ_[p]] ℂ_[p]`, the
Hodge–Tate jumps of `L` at `g` in a finite set `J`, counted with multiplicity (`jump L.ρ g u`),
number at most `finrank O L`. 

### `lcm_pow_sub_one_le`

 For `q > 1`, the least common multiple of the `q ^ i - 1` for `1 ≤ i ≤ r` is at most
`q ^ r ^ 2`. 

### `KummerChart.sum_jumpMultiplicity_le`

 Let the sets of the filter `F` contain the subgroup `k.subgroup` (`hF`), and let `L` lie in the
class `InClass F ⊥ U` (`h`). Suppose that at each embedding `g` the jumps of `L` in `J`, counted
with multiplicity, number at most `n`. Then the jumps in `J` of the side `k.universalSide ζ hF h` at
the letter `i`, counted with multiplicity, number at most `n` times the number of embeddings `g`
with `g ζ = theta (k.letterTeich i)`. 

### `KummerChart.pow_smul_mem_cupOrthogonal_of_isScaledCupCoboundary`

 Let `Γ → Gp p = Gal(ℚ̄_p / ℚ_p)` be an open embedding and `F` a filter on `Γ` whose sets contain
the subgroup `k.subgroup` of the chart. Let the lattices `Y` with property `Q` lie in
`InClass F ⊥ U` and `L` in `InClass F ⊥ U'`. Let `x` be a crystalline cocycle of `L` such that, for
all such `Y`, all pairings `P` and all crystalline cocycles `c` of `Y`, the cup product of `c` and
`p ^ e • x` is a coboundary. Then `p ^ e • x` lies in the annihilator `cupOrthogonal Q L` of these
lattices under cup products. 

### `KummerChart.crysCocycles_le_cupOrthogonal_of_no_small_neg_jump`

 Let `Γ → Gp p = Gal(ℚ̄_p / ℚ_p)` be an open embedding, let the chart `k` be unramified and
`p ≥ 5`, and at each letter `i` let `b i + W + η ≤ (p - 3) a`, `6 (a + η + W) < b i`, and let `p`
divide no nonzero integer within `6 (a + η + W)` of `0` or `± b i` (`NoMultipleNear`). Let `L` be
crystalline with Hodge–Tate jumps in `U'`, and at each letter let the jump sets of `U` and `U'` lie
in `[-η, η] ∪ ∓ε i [b i, b i + W]`, with opposite signs. If `U` and `U'` avoid `[-a, 0)`, or `U'`
lies in `[-η, 0]`, then every crystalline cocycle of `L` lies in `cupOrthogonal`: its cup product
with every crystalline cocycle of a crystalline lattice with jumps in `U` is a coboundary. 

### `KummerChart.dualDefect_le_of_few_low_weights`

 Few low jumps. Let `Γ → Gp p` be an open embedding, let the chart be unramified, `p ≥ 5`,
`η ≥ 1`, and at each letter `i` let `b i + W + η ≤ (p - 3) a`, `6 (a + η + W) < b i`, and let `p`
divide no nonzero integer within `6 (a + η + W)` of `0` or `± b i` (`NoMultipleNear`). Let `L` be
crystalline with jumps in `U'`, and at each letter let the jump sets of `U` and `U'` lie in
`[-η, η]` and in far windows `[b i, b i + W]` of opposite signs. If `L` has at most `m` jumps in
`[-η, η]` at each embedding, then the defect `dualDefect`, the length of the crystalline cocycles of
`L` modulo those orthogonal to the crystalline lattices with jumps in `U`, is at most
`11 f (m (a + 1) + rank L · (W + 1))` times the length of `O / p`, where `f = k.f`. 

### `KummerChart.dualDefect_eq_zero_and_dualDefect_le`

 The defect at generic primes. Let `Γ → Gp p` be an open embedding, and let the root `ζ` assign
the embeddings of `O` to the letters of the chart `k`. Let `k` be unramified, `p ≥ 5`, `η ≥ 1`, and
at each letter `i` let `b i + W + η ≤ (p - 3) a`, `6 (a + η + W) < b i`, and let `p` divide no
nonzero integer within `6 (a + η + W)` of `0` or `± b i`. Let `L` be crystalline with jumps in `U'`,
where `U` and `U'` lie at each letter in `[-η, η]` and in the opposite far windows
`∓ε i [b i, b i + W]`.

The defect `dualDefect` is the length of the crystalline cocycles of `L` modulo those orthogonal to
the crystalline lattices with jumps in `U`. It vanishes if `U` and `U'` avoid `[-a, 0)` or `U'` lies
in `[-η, 0]`. If `L` has at most `m` jumps in `[-η, η]` at each embedding, it is at most
`11 f (m (a + 1) + rank L · (W + 1))` times the length of `O / p`, where `f = k.f`. 

### `KummerChart.hasCupExponent_any_pattern`

 Let `Γ → Gp p` be an open embedding, and let the root `ζ` assign the embeddings of `O` to the
letters of the chart `k`. Let `k` be unramified, `p ≥ 7`, `η ≥ 1` and `V + 4 η ≤ M`. Let `L` be
crystalline with jumps in `U'`, where `U` and `U'` lie at each letter in `[-η, η]` and in opposite
far windows of width `V`, which start at `b` at the b-letters (those with `IsBLetter i`) and at `G`
at the others, with `0 < G ≤ b`. If `b < K p ^ 2`, `2 G < K p` and `M ≤ K`, then
`p ^ (10⁴ (K + ⌊log_p (2 (b + M))⌋))` times any crystalline cocycle of `L` is orthogonal under cup
products to the crystalline cocycles of the crystalline lattices with jumps in `U`. 

### `KummerChart.hasCupExponent_sparse_thick`

 Let `Γ → Gp p` be an open embedding, and let the root `ζ` assign the embeddings of `O` to the
letters of the chart `k`. Let `η ≥ 1`, and let `L` be crystalline with jumps in `U'`, where `U` and
`U'` lie at each letter in `[-η, η]` and in opposite far windows of width `V`, which start at `b` at
the b-letters (those with `IsBLetter i`) and at `G` at the others, with `G + V ≤ η`; so the low
window `[-η, η]` contains the far windows of the other letters. Suppose that no three b-letters
follow one another along the orbits of `letterFrob : i ↦ i ^ p` with both gaps between `1` and
`J ≥ 1`. Suppose also that either the chart is unramified with `p ≥ 7` and `10 p ^ J η ≤ b`, or the
sign `ε` is constant and `8 e ≤ p ^ (J + 1)`. Let `2 e (b + 5 η) ≤ p ^ (J + 1) δ` and
`20 (J + 1 + d) η + ⌊log_p (2 (b + 5 η))⌋ ≤ M`, where `e = k.e` is the ramification index and
`d = k.differentBound` is `0` for `e = 1` and `v_p(e) + 1` otherwise. Then
`p ^ (10³ (δ + (J + 1) M))` times any crystalline cocycle of `L` is orthogonal under cup products to
the crystalline cocycles of the crystalline lattices with jumps in `U`. 

### `KummerChart.linearFrob_comp_subtype`

 Let `Γ → Gp p` be injective. Restricting a lattice `Y` to the subgroup `k.subgroup` of a chart
does not change the operator `linearFrob` of `(s, m)` on the potentially crystalline periods. 

### `TameChart.linearFrob_eq_one`

 Let `Γ → Gp p` be bijective, let `d` be a tame chart with subgroup `d.subgroup` and ramification
index `d.e`, and let `Y` be potentially crystalline. The elements `s` of inertia
(`IsWeilPair (toGp s) 0`) act on the periods of `Y` by `linearFrob Y.ρ s 0`. If `X ^ d.e - 1` kills
all these operators (`IsKilledBy`), then those of inertia elements in `d.subgroup` are trivial. 

### `TameChart.inClass_of_pow_sub_one`

 Descent along a tame chart. Let `Γ → Gp p` be a surjective open embedding, `F` any filter on
`Γ`, and `d` a tame chart with subgroup `d.subgroup` and ramification index `d.e`. Let the lattice
`Y` lie in `InClass F K U`: its periods fixed near `1` and on a set of `F` span, its jumps at each
embedding `g` lie in `U g`, and each polynomial allowed by `K s` kills `s` on the periods, for `s`
in inertia. If `K s` allows `X ^ d.e - 1` at every `s` in inertia, then `Y` is crystalline over
`d.subgroup` with jumps in `U`: it lies in the class of the filter of the sets containing
`d.subgroup` and the empty relation `⊥`. 

### `exists_tameChart_e_eq_lcm`

 If `Γ` maps onto `Gp p` and the number `r` is less than the prime `p`, there is a tame chart
whose ramification index is the least common multiple of the `p ^ i - 1` for `1 ≤ i ≤ r`. 

### `TameChart.differentBound_le_one`

 The number `differentBound` of a tame chart is at most `1`, since `p` does not divide the
ramification index. 

### `noMultipleNear_of_add_lt`

 If `b + n < q`, then `q` divides no nonzero integer within distance `n` of `0`, `b` or `-b`. 

### `FitsWindows.le_add_add`

 An element of `[-η, η] ∪ ε [b, b + W]` is at most `b + W + η`. 

### `FitsWindows.neg_add_le_of_opposite`

 Let the set `V` lie in `[-η, η] ∪ -ε [b, b + W]` and `V'` in `[-η, η] ∪ ε [b, b + W]`, for a
sign `ε`. At most one of `v ∈ V` and `v' ∈ V'` is below `-η`, so `-(v + v') ≤ b + W + 2 η`. 

### `hasCupExponent_of_isTameType`

 Let `Γ → Gp p = Gal(ℚ̄_p / ℚ_p)` be a surjective open embedding. For each `s` in inertia let
`K s` be a tame type: it holds for `X ^ e - 1`, with `e` the least common multiple of the
`p ^ i - 1` for `1 ≤ i ≤ r`, and for a monic polynomial over `ℤ_[p]` of degree at most `N`. A
lattice lies in `InClass F K U` if its periods fixed on a neighbourhood of `1` that belongs to the
filter `F` span, its Hodge–Tate jumps at each embedding `g` of `O` lie in `U g`, and each polynomial
allowed by `K s` kills `s` on its periods, for `s` in inertia. Let `L` lie in the class for `U'` and
`s ↦ K s⁻¹`. If `U` and `U'` lie at each embedding in `[-η, η]` and in the opposite far windows
`∓ε [b, b + W]`, and `p > b + 6 (W + η) + r² (N + 1)² + 2`, then
`p ^ (3 r² (N + 1)² + 150 (η + W + 1))` times any crystalline cocycle of `L` has cup product a
coboundary with every crystalline cocycle of a lattice in `InClass F K U` paired with `L`. 
