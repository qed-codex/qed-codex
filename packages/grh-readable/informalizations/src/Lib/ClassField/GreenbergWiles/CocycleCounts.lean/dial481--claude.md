---
{
  "module": "src/Lib/ClassField/GreenbergWiles/CocycleCounts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/CocycleCounts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/CocycleCounts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counts of trivialised Galois cocycles for projective modules and central scalars

We count trivialised cocycles (`New.DiscreteModule.trivialisedCocycles`) of the absolute Galois
group `G` of a number field `K` (`IsProGalois G K Ω`: `G` acts on `Ω` as its Galois group over `K`)
in a finite module `V`. A trivialised cocycle vanishes on `I` and carries a trivialisation at each
place of `Ω` (the algebraic closure of `ℚ`) above `N` and infinity. Here
`New.IsLargeLevel.SplitPlaces` is the data of finitely many places not dividing `N`, indexed by `ι`,
with Frobenius elements `s.φ i` in `U`. The set `I` is the union of the inertia groups above the
other places not dividing `N`.

## Main definitions and results

* `New.IsLargeLevel.SplitPlaces.card_trivialised_of_isHigmanProjective`: for `V` killed by `l`,
  fixed by `U` and projective over `G ⧸ U` in Higman's sense, given `z`, `n` with `ρ(z) − n`
  injective on `V` and with `z • r − n • r` fixed by `U` for every unit `r` fixed by all `s.φ i`
  with `l • r` a `U`-fixed `N`-unit, at most `#V ^ (#ι + 1)` trivialised cocycles, with equality
  under further hypotheses.
* `New.IsLargeLevel.SplitPlaces.hasFewCocycles_of_central`: let `K` be totally complex and `r ≠ 0`.
  Suppose some `z`, central modulo `U` and with `l`-adic cyclotomic character `1`, satisfies
  `V.FiniteKilledFixedInj (l ^ r) U z 1`. Suppose also that the Frobenii of the split places detect
  roots. Then `V` has at most `#V ^ (#ι + 1)` trivialised cocycles.

Notions from other files:
* `New.DiscreteModule.IsHigmanProjective`: Higman's criterion relative to Q of finite index: some
  additive τ : A → A has ∑ gτg⁻¹ = 1, summed over chosen representatives g of G/Q.
* `New.DiscreteModule.FiniteKilledFixedInj`: The G-module A is finite and killed by n, Q acts
  trivially on it, and ρ(z) − m is injective on it.
* `New.IsLargeLevel.fixedSUnits`: The N-units of the fixed field of U: the N-units of Ω that are
  fixed by U.

## Relation to the literature

An upper bound of the kind the Greenberg–Wiles formula gives when the dual Selmer group vanishes;
the hypothesis on the Frobenii `s.φ i` takes the place of that vanishing. Only this bound is proved
(with a case of equality for projective modules), under the hypothesis that `ρ(z) − n` is injective
on `V`; for modules that are not projective, `n = 1` and `z` is central modulo `U`. No local duality
is used: the dual Selmer group is replaced by linear relations among the values of a cocycle on tame
inertia at the split places.

Source: H. Darmon, F. Diamond, R. Taylor, Fermat's Last Theorem (1995; revised 2007), Thm 2.18–2.19;
A. Wiles, Ann. of Math. 141 (1995), Prop. 1.6; J. S. Milne, Arithmetic Duality Theorems, I 4.10,
5.1; L. Washington, Galois cohomology (1997), Thm 2.



## The count for a projective module

`New.IsLargeLevel.SplitPlaces.card_trivialised_of_isHigmanProjective` bounds the order of the group
of trivialised cocycles by `#V ^ (#ι + 1)`, with a case of equality, under further hypotheses on `V`
and `z` (`hV_fin`, `h_fix`).

The proof compares the group with the `G ⧸ U`-equivariant maps from (`N`-units) `× ℤ` to `V`. It
uses the reciprocity law `New.IsLargeLevel.SplitPlaces.power_residue_reciprocity` and the unit
theorem `New.IsLargeLevel.dirichlet_fixedSUnits`.


### `New.IsLargeLevel.exists_linearMap_factor_of_ker_le`

 Let `β : A → B` and `f : A → V` be additive maps, where `B` and `V` are vector spaces over
`ZMod l`. If `f` vanishes wherever `β` does, then `f = v ∘ β` for a `ZMod l`-linear map `v`. 

### `New.IsLargeLevel.exists_act_torsion_eq_nsmul`

 Let `G` act on `Ω` (`New.Ω`, the algebraic closure of `ℚ`) as the Galois group over the number
field `K`. On a torsion element of (`N`-units of the fixed field of `U`) `× ℤ`, the element `z` acts
by a natural number that is congruent modulo `l` to the cyclotomic character of `z`. 

### `Representation.apply_sum_trace_eq_add`

 Averaging with a Higman trace. Let `W` represent the finite group `Δ` on `V`, and let the
additive `τ : V → V` satisfy `∑ δ, δ (τ (δ⁻¹ a)) = a`. Let `F : X → V` on a `Δ`-set `X`, and let
`g (F x) = F (g • x) + c` for all `x`. Then `g` moves the average `∑ δ, δ (τ (δ⁻¹ (F (δ • x₀))))`
by `c`. 

### `exists_act_sub_nsmul_eq_nsmul_of_symbol_eq_zero`

 Let `b y i` be the `l`-th power residue symbol of the `N`-unit `y` of the field of `U` at the
Frobenius `frob i`: `ζ ^ b y i = frob i r / r` whenever `r ^ l = y`, for the root of unity `ζ` of
`New.rootPowHom`. Let `U` fix `z r / r ^ n` whenever `r ^ l` is such an `N`-unit and every
`frob i` fixes `r` (written additively in `New.DiscreteUnits Ω`). If all symbols of
`y` vanish, then `z y / y ^ n` is the `l`-th power of an `N`-unit. 

### `symbolIntertwiningMap`

 The equivariant maps given by power residue symbols. For `a : ι → V` and `c` fixed by `G` (in
the kernel of the coboundary map `coboundaryMap V.ρ`), the map from (`N`-units) `× ℤ` to `V` given
by `(y, k) ↦ ∑ (i, δ), b (δ y) i • δ⁻¹ (a i) + k • c` is `G ⧸ U`-equivariant, where `W` is the
action of `G ⧸ U` on `V`. 

### `mem_range_symbolIntertwiningMap`

 Let `W` be the action of `G ⧸ U` on `V` (that is, `V.ρ g = W g`), let `l` kill `V`, and let
`z - n` be injective on `V`. Let `τ` be a Higman trace: `∑ δ, δ (τ (δ⁻¹ a)) = a`. Let `b` and
`h_fix` be as in `exists_act_sub_nsmul_eq_nsmul_of_symbol_eq_zero`. Then every `G ⧸ U`-equivariant
`x` from (`N`-units) `× ℤ` to `V` is given by symbols: it lies in the range of
`symbolIntertwiningMap W hW b`. 

### `torsion_le_ker_of_map_act_eq`

 Let `l` kill `V`, let `z - n` be injective on `V`, and let `z` raise the `l`-th roots of unity
in `Ω` (`New.Ω`, the algebraic closure of `ℚ`) to the power `n`. Then every `ℤ`-linear `x` from
(`N`-units) `× ℤ` to `V` that commutes with `z` kills the torsion. 

### `exists_mem_trivialisedCocycles_of_mem_ker`

 The converse of reciprocity on the kernel of `symbolIntertwiningMap`. Let `W` be the action of
`G ⧸ U` on `V`, let `τ` be a Higman trace, and let `h_conv` say that a family `f` satisfying the
symbol relations gives, for each `a : V`, a trivialised cocycle with value `∑ δ, δ (f (i, δ) • a)`
at each `γ i`. If `(a, c)` lies in the kernel, then `c = 0` and some trivialised cocycle takes the
value `a i` at each `γ i`. 

### `AddMonoidHom.card_eq_card_ker_mul_card_mul_card_range`

 Counting along `r : T → J` and a surjection `p` from `ker r` onto `D`:
`#T = #(ker p) * #D * #(range r)`. 

### `AddMonoidHom.card_pow_succ_eq_card_mul_card_range_mul_card_ker`

 Counting along `d : A → B` and a surjection `j` from `(ι → A) × ker d` onto `H`:
`#A ^ (#ι + 1) = #H * #(range d) * #(ker j)`. 

### `New.IsLargeLevel.SplitPlaces.card_trivialised_of_isHigmanProjective`

 Count of the trivialised cocycles, for split places indexed by `ι`. Let `V` be finite, killed by
the prime `l`, fixed by `U`, Higman-projective over `G ⧸ U`, with `z - n` injective; let `U` fix
`z r / r ^ n` whenever `r ^ l` is an `N`-unit fixed by `U` and every `s.φ i` fixes `r`. (a) There
are between one and `#V ^ (#ι + 1)` of them. (b) Exactly `#V ^ (#ι + 1)` if `z` raises the `l`-th
roots of unity to the power `n` and `K` is totally complex. Trivialised cocycles are pairs of `f` on
the places of Ω over `N` and ∞ and a continuous `c : G → V` zero on `I`, with
`g f(x) = f(gx) + c(g)`. `I` is inertia above the primes prime to `N` other than the split `v i`,
and `s.φ i ∈ U` are Frobenii at them. 

### `New.IsLargeLevel.SplitPlaces.hasFewCocycles_of_isHigmanProjective`

 Under the hypotheses of `card_trivialised_of_isHigmanProjective`, there are between one and
`#V ^ (#ι + 1)` trivialised cocycles. 

### `New.IsLargeLevel.SplitPlaces.card_trivialisedCocycles_eq_of_isHigmanProjective`

 Under the hypotheses of `card_trivialised_of_isHigmanProjective`, if `K` is totally complex and
`z` raises the `l`-th roots of unity to the power `n`, there are exactly `#V ^ (#ι + 1)`
trivialised cocycles. 

 ## The count for modules with a central scalar 

### `New.IsLargeLevel.SplitPlaces.fixes_sub_of_frobeniiDetectRoots`

 Let the Frobenii detect the roots of units (`U` fixes every `x` that all `s.φ i` fix with
`m • x` an `N`-unit fixed by `U`), and let `z` be central modulo `U` and fix the `l`-th roots of
unity, `l ∣ m`. If `l • x` is an `N`-unit fixed by `U` and the Frobenii fix `x`, then every `g` that
fixes `l • x` fixes `z x - x`. 

### `New.IsLargeLevel.SplitPlaces.card_trivialised_restrict_of_isHigmanProjective`

 The exact count over an open subgroup `B` of `G = Gal(Ω/K)` that contains `U` and `z`. Let `K`
be totally complex, let `S` be split places for `l`, and let `z` fix the `l`-th roots of unity.
Suppose (`hfix`) that for every `x` fixed by the Frobenii `S.φ i` with `l • x` an `N`-unit fixed
by `U`, every `g` fixing `l • x` fixes `z x - x`. Let `U ≤ Q` in `B`, with `Q` fixing the `l`-th
roots of unity, and let `W` be a `B`-module that is finite, killed by `l`, fixed by `Q`, with
`z - 1` injective, and projective over `B/Q` in Higman's sense. Then `W` has exactly
`#W ^ (#(ι × G/B) + 1)` trivialised cocycles. 

### `New.IsLargeLevel.SplitPlaces.card_trivialised_eq_of_map_range_eq_top`

 The exact count for modules killed by `l`. Let `S`, `z` and `hfix` be as in
`card_trivialised_restrict_of_isHigmanProjective`, with `z` central modulo `U` and fixing the `l`-th
roots of unity, and let `K` be totally complex. Suppose that for every short exact sequence
`W₁ → W → W₂` of `G`-modules, with `W` finite, killed by `l`, fixed by `U` and with `z - 1`
injective, the induced map on trivialised cocycles of `W` and `W₂` is onto. Then every such `W` has
exactly `#W ^ (#ι + 1)` trivialised cocycles: the ratio of the two counts is multiplicative, and `1`
on projective modules. 

### `New.DiscreteModule.trivialisedCocycles.fst_injective`

 A trivialised cocycle `p = (trivialisation, cocycle)` is determined by its trivialisation. 

### `New.DiscreteModule.trivialisedCocycles.map_range_eq_top_of_hasFewCocycles`

 Lifting from an upper bound that projective modules attain. Let `l` be prime, `U` open normal in
the compact group `G`, and `z` central modulo `U`. Consider the modules `F` that are finite, killed
by `l`, fixed by `U` and on which `ρ z - 1` is injective. Suppose each has between one and `#F ^ k`
trivialised cocycles, and those projective over `G ⧸ U` in Higman's sense have at least `#F ^ k`.
Then along a short exact sequence `W₁ → W → W₂` with `W` such a module, every trivialised cocycle
of `W₂` lifts to `W`. 

### `New.DiscreteModule.trivialisedCocycles.map_range_eq_top_of_restrictTo`

 Lifting by corestriction. Let `B` be an open subgroup of finite index prime to `l` that contains
the conjugation-stable set `I`. Let `π : W → W₂` be onto, with `I` fixing `W` and `l` killing `W₂`,
and let `πB` be `π` as a map of `B`-modules. If every trivialised cocycle of `W₂` for `B` lifts to
`W`, then so does every trivialised cocycle of `W₂` for `G`. 

### `OpenSubgroup.exists_le_normal_mem_coprime_index`

 Let `P` be an open subgroup of index prime to `l` that contains all commutators `⁅z, g⁆`. Then
some open subgroup `B ≥ P` normalises `P` and contains `z`, and both the index of `P` in `B` and the
index of `B` are prime to `l`. 

### `New.IsLargeLevel.SplitPlaces.hasFewCocycles_of_central`

 Let `K` be totally complex and `r ≠ 0`, and let `s` be split places for `U` indexed by the
finite type `ι`, at levels `l ^ r` and `N`: distinct primes prime to `N` with Frobenii `s.φ i` in
`U`, where `I` is the union of the inertia groups above the other primes prime to `N`. Let `V` be
finite, killed by `l ^ r`, fixed by `U`, with `ρ(z) − 1` injective; let `z` have `l`-adic cyclotomic
character `1` and all `⁅z, g⁆` in `U`; and let `U` fix every `x ∈ Ωˣ` that the Frobenii `s.φ i` fix
and whose `l ^ r`-th power is an `N`-unit of the field of `U`. Then `V` has at least one and at most
`#V ^ (#ι + 1)` cocycles trivialised at the places above `N` and infinity (`PlaceAboveLevel N`) and
on `I`.

This is only an upper bound in the spirit of the Greenberg–Wiles formula: it counts trivialised
cocycles over a totally complex field, given such an element `z`, and its statement involves no dual
Selmer group. 
