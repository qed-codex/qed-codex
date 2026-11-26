---
{
  "module": "src/New/Congruences/LocalLoss/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local loss above ℓ: main summand weights, b-places, crystalline relations and crystalline colength

This file provides the data for the bound on the loss of a lift at the places of `E` above `ℓ`
(`New.Selmer.eventually_exists_inClass_sum_dualDefect_le`). It defines the conditions on the weights
of a main summand and the unit of that bound, and studies the signs of the embeddings in a Galois
orbit that define b-places. Fix `ι : ℂ ≃ ℚ̄_ℓ` through `New.PadicIso`. For `e : E → ℚ̄_ℓ` and `g` in
`New.Gp ℓ`,
`New.Selmer.complexEmbeddingOf e g = ι⁻¹ ∘ g⁻¹ ∘ e`. `New.Selmer.cmSign σ` is `1` if `σ` belongs to
the CM type and `-1` if not.

## Main definitions and results

* `New.Selmer.crystallineLoss`, `New.Selmer.defectBound`: the crystalline loss, and the unit of the
  bound on the total loss of a lift.
* `New.Selmer.ribetCocycles.exists_graph_subrepresentation`: for an element `a` of a noetherian ring
  `O` and finitely many matrix representations `u x` of a group, a cocycle with values in `(O/aO)^d`
  that obeys every linear relation among the families `(u x g - 1)_x` comes from an equivariant map
  on a subrepresentation, given by its graph. Its domain contains the families `(u x g - 1)_x` and
  all multiples of a power of `a` (Artin–Rees).
* `New.Selmer.SummandCoordIndex`, `New.Selmer.summandRep`: the summands of a lift, namely the main
  summand and `t` powers of the inverse cyclotomic character (`New.Selmer.tateTwist`).
* `New.Selmer.crysCocyclesAt`, `New.Selmer.crysRelations`: the crystalline cocycles at `v`, and the
  union over the places `v` above `ℓ` of the linear relations that hold on them, read as relations
  on functions on the global Galois group.
* `New.Selmer.crystallineColength`: the length by which cocycles in `New.Selmer.ribetCocycles`, with
  values in `(O/ℓ^M O)^n`, can miss these relations.

Notions from other files:
* `New.Parameters`: The fixed parameters: a multiple `q₀` of `18480 = 16 · 3 · 5 · 7 · 11` and a
  prime `d` with `d ≡ q₀/2 - 1 mod q₀`. For these, `P.E s = K(ζ)`, where `K = ℚ(√-d)` and `P.ζ s` is
  a root of unity of order `P.q₁ s = 3^c 2^s q₀`, `c = ⌊log₃ s⌋ + 5`. The group `P.Φ s` of infinite
  places of `P.E s` is identified with `(ℤ/q₁)ˣ`, and `P.placeClass` reduces it modulo a divisor of
  `q₁`.
* `New.Data`: The admissible data `D`. Among them are the ranks `m`, `r`, `k = r + 1 - m`, the
  length `t = 5r`, the weight `natB` and the set `D.bPlaces` of b-places of `D.E = P.E D.towerExp`,
  which lies in the cyclotomic field of order `D.cyclotomicConductor = q₁ d`.
* `New.Gp`: The absolute Galois group G_p = Gal(Q̄_p over Q_p).
* `New.Period.crysCocycles`: Z_f(T), the module of maps c: Γ → T such that some y in B⊗T, B = B_max,
  has 1⊗c(g) = gy − y for all g.
* `New.CoeffRing`: Rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`.

## Relation to the literature

See `Lib.PadicHodge.BlochKato` and `Lib.ClassField.Places.LocalFields` for sources.



## Signs of embeddings, jump conditions of a main summand and the defect bound

* `New.Selmer.IsMainSummandWeights`: where the jumps of a main summand lie and how many are small or
  negative.

The numbers `D.k = D.r + 1 - D.m`, `D.halfGap = D.r ^ 8` (half the gap) and `D.natB` are read off
the data.


### `cmSign`

 The sign of a complex embedding σ of E: 1 if σ is the embedding the CM type chooses at its
place, and −1 otherwise. 

### `complexEmbeddingOf`

 The complex embedding ι⁻¹ ∘ g⁻¹ ∘ e of E, for e: E → ℚ̄_ℓ and g in G_ℓ. 

### `IsMainSummandWeights`

 The conditions on the jumps `J σ` (a multiset of integers for each complex embedding `σ`) of a
main summand of rank `r` with a string of length `t`, for admissible data `D`: each jump is low or
near `∓w_j(σ)`, where `w_j = D.liftWeight j` is the weight of the `j`-th lift, `j ≤ D.m`; few jumps
have `|u| ≤ 2 halfGap²`, and at most `r` jumps at `σ` and `σ̄` together are negative. 

### `IsMainSummandWeights.rank_mem`

 The rank `r` lies between `1` and `D.r`. 

### `IsMainSummandWeights.t_le`

 The length `t` of the string is at most `D.t`. 

### `IsMainSummandWeights.low_or_high`

 For one `j ≤ m`, each jump `u` at an embedding `σ` is low, `Δ / 4 ≤ |u| ≤ 2 m Δ` with
  `Δ = D.gap = 2 halfGap`, or high: within `D.t` of `-w_j(σ)` if `σ` is in the CM type, of `w_j(σ)`
  otherwise. 

### `IsMainSummandWeights.card_small_le`

 At most `r m / k` jumps `u` at `σ` are small: `|u| ≤ 2 halfGap²`. 

### `IsMainSummandWeights.card_neg_le`

 At most `r` jumps at `σ` and `σ̄` together are negative. 

### `lt_natAbs_of_abs_add_liftWeight_le`

 Let `σ` be a complex embedding of the field `E` of the admissible data `D`, with sign
`cmSign σ` equal to `1` if `σ` belongs to the CM type and `-1` if not. Let `w` be the weight
`D.liftWeight j` of the character of the `j`-th lift at the infinite place of `σ`, and let
`D.t = 5 * D.r`. If an integer `u` lies within `D.t` of `-cmSign σ * w`, then `|u|` exceeds every
`B` with `B + D.t < w`. 

### `crystallineLoss`

 The crystalline loss of three natural numbers h, b, l: the l-adic valuation of the product of
(2b)! and P^(h³), where P is the product of the natural numbers k with
max(b − 30h³, 0) < k ≤ b + 30h³. 

### `defectBound`

 The unit at `l` of the bound on the loss of a lift, for the data `D`:
`10⁶ (m/k) (natB v_l(M) + crystallineLoss halfGap natB l)`, where `v_l` is the `l`-adic valuation
and `M = D.M` is the product of the two level primes. 


## Spacing and signs of the b-places in a Galois orbit

For `e : E → ℚ̄_ℓ`, each `g` gives a complex embedding `New.Selmer.complexEmbeddingOf e g`, and so
an infinite place. The infinite places of `E` form a group identified with `(ℤ/q₁)ˣ` through the
action on the root of unity `New.Parameters.ζ`.

The results use two properties of the set `D.bPlaces` of b-places: its members have class `-1`
modulo `q₀` (`New.Data.placeClass_of_mem_bPlaces`) and it is sparse (`New.Data.sparse`).


### `fixes_emb_of_fixes_rootsOfUnity`

 The field `D.E` of the data `D` lies in the cyclotomic field of order
`D.cyclotomicConductor = q₁ d`. So an element `g` of `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)` that fixes every `ζ` in
`ℚ̄_ℓ` with `ζ ^ D.cyclotomicConductor = 1` has `g (e x) = e x` for every embedding `e : D.E → ℚ̄_ℓ`
and every `x`. 

### `map_sqrtNegDInE_eq_cmSign_mul`

 A complex embedding `σ` sends `√-d` to `cmSign σ` times the chosen square root of `-d`. 

### `map_zeta_eq_zpow_cmSign`

 Let `E = K(ζ)` with `K = ℚ(√-d)` and `ζ = P.ζ D.towerExp` a root of unity. For an infinite place
`w` of `E`, `Φ w` is the embedding at `w` that belongs to the CM type, the one that sends `√-d` to
the chosen complex root. For a complex embedding `σ` with place `w`, `Φ w` sends `ζ` to
`σ ζ ^ cmSign σ`. 

### `placeClass_eq_cmSign_mul_pow`

 Let `P` be the parameters of the data `D`, `ζ = P.ζ D.towerExp` the root of unity of order `q₁`
in `E`, `e : E → ℚ̄_ℓ`, and `g`, `g'` in `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)`, with complex embeddings
`σ = complexEmbeddingOf e g = ι⁻¹ ∘ g⁻¹ ∘ e` and `σ' = ι⁻¹ ∘ g'⁻¹ ∘ e` for the fixed `ι : ℂ ≃ ℚ̄_ℓ`.
Suppose `g' * g⁻¹` raises `e ζ ^ ℓ ^ a` to the power `ℓ ^ n`. Let `y` be the ratio of the places of
`σ` and `σ'` in the group `P.Φ D.towerExp ≃ (ℤ/q₁)ˣ` of infinite places of `E`. For `m ∣ q₁` prime
to `ℓ ^ a`, the reduction `P.placeClass hm y` of `y` modulo `m` is
`cmSign σ * cmSign σ' * ℓ ^ n`. 

### `notMem_bPlaces_of_short_arc`

 Spacing of the b-places `D.bPlaces`, the sparse set of infinite places of `E` of weight `b` in
the data `D`. Let `e : E → ℚ̄_ℓ` for a prime `ℓ ≤ D.k * D.t = (D.r + 1 - D.m) * (5 * D.r)`, and let
`0 < i < n < l₀ s`, where `s = D.towerExp` and `l₀ s` is the least power of `3` above `27 s`. Let
`g' * g⁻¹` and `g' * g₁⁻¹` in `Gp ℓ` raise `e ζ ^ ℓ ^ a` to the powers `ℓ ^ n` and `ℓ ^ i`, where
`ζ = P.ζ s` generates `E` over `K = ℚ(√-d)`. Each `γ` in `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)` gives the complex
embedding `complexEmbeddingOf e γ = ι⁻¹ ∘ γ⁻¹ ∘ e`, for the fixed `ι : ℂ ≃ ℚ̄_ℓ`. If the embeddings
given by `g` and `g'` lie over b-places, then the one given by `g₁` does not. 

### `cmSign_eq_of_mem_bPlaces`

 Let the prime `ℓ` divide `D.cyclotomicConductor = q₁ d`, let `e : E → ℚ̄_ℓ`, and let `g`, `g'`
be in `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)`. Suppose the complex embeddings
`complexEmbeddingOf e g = ι⁻¹ ∘ g⁻¹ ∘ e` and `ι⁻¹ ∘ g'⁻¹ ∘ e`, for the fixed `ι : ℂ ≃ ℚ̄_ℓ`, both
lie over b-places: members of the set `D.bPlaces` of infinite places of `E` of weight `b`, all of
class `-1` modulo `q₀`. Then both or neither belong to the CM type, so their signs `cmSign`
agree. 

 ## Cocycles obeying the relations among the u(g) − 1, and summands of a lift 

### `ribetCocyclesIn`

 The cocycles `c : G → B ^ d` for `ρ`, with values in any `O`-module `B`, that obey the linear
relations among the families `(u x g - 1)_x`: for finitely supported `θ : G → O`, if
`∑ θ g • (u x g - 1) = 0` for all `x`, then `∑ θ g • c g = 0`. 

### `ribetCocycles`

 The cocycles `c : G → (O / a) ^ d` for `ρ` that obey the linear relations among the families
`(u x g - 1)_x`: the case `B = O / a` of `ribetCocyclesIn`. 

### `ribetCocycles.exists_graph_subrepresentation`

 For finite `X` and noetherian `O`, a cocycle `c : G → (O/a)^d` in `ribetCocycles u ρ a` extends
to an equivariant map on a submodule: for some `k` there is a subrepresentation `Y` of (families of
matrices) × `(O/a)^d`, with `g` acting by left multiplication with `(u x g)_x` and through `ρ`
(`actionRep`), whose points are determined by their first component and which contains
`((u x g - 1)_x + a ^ k • v, c g)` for all `g` and all families `v`.

This is a consequence of the Artin–Rees lemma for the principal ideal `(a)`: with `I` the span of
the families `(u x g - 1)_x`, the elements of `I` divisible by `a ^ k` lie in `a • I` for some
`k`. 

### `SummandCoordIndex`

 The index sets of the summands of a lift: `r` for the main summand, and one point for each of
the `t` characters, which are `1 × 1` summands. 

### `instance {r : Type} [inst : Fintype r] {t : ℕ} : ∀ i : Option (Fin t), Fintype (SummandCoordIndex r i)`

 Each index set `SummandCoordIndex r i` is finite if `r` is. 

### `instance {r : Type} [inst : DecidableEq r] {t : ℕ} : ∀ i : Option (Fin t), DecidableEq (SummandCoordIndex r i)`

 Each index set `SummandCoordIndex r i` has decidable equality if `r` has. 

### `summandRep`

 The summands of a lift: `T` on the main summand, and on the summand of `e : Fin t` the Tate
twist `O(-e)`, the `e`-th power of the inverse cyclotomic character. 


## Crystalline conditions above ℓ as relations on cocycles, and crystalline colength

* `New.Selmer.localChart`: a chosen identification of the decomposition group at `v` with a subgroup
  of `Gal(ℚ̄_ℓ / ℚ_ℓ)`.

A relation is a finitely supported matrix-valued `f`, and `c` obeys it if `∑ γ, f γ • c γ = 0`.
`New.relationsOn Z` is the set of relations that hold on `Z`, `New.obeying R B` the module of
functions with values in `Bⁿ` that obey the relations `R`, and `New.relLength S T` the length of
`S / (S ⊓ T)`.


### `localChart`

 A chosen embedding Ω → ℚ̄_ℓ that induces the chosen place of Ω above v, together with the
homomorphism to Gal(ℚ̄_ℓ over ℚ_ℓ) from the decomposition group of that place that goes with it in
the sense of `New.GaloisRep.InducesPlace`. 

### `coefficientEmbedding`

 For g in Gal(ℚ̄_ℓ over ℚ_ℓ), the embedding of the coefficient ring O in ℂ_ℓ sending x to
g(x). 

### `crysCocyclesAt`

 The O-module Z_f at v: crystalline cocycles (`New.Period.crysCocycles`) of the decomposition
group of the chosen place above v, with values in O^n acted on through u. 

### `crysRelations`

 The linear relations that hold on the crystalline cocycles `New.Selmer.crysCocyclesAt v u` for
some v above ℓ, extended by zero from the decomposition group to relations on functions on
Gal(Ω/E). 

### `crystallineColength`

 The crystalline colength of the summand `u` modulo `ℓ ^ M`, with respect to a family `w` of
matrix representations of Gal(Ω/E): the length of the module of cocycles for `u` with values in
`(O/ℓ^M)^n` that obey every linear relation among the `(w x g - 1)_x` (`New.Selmer.ribetCocycles`),
modulo those that also obey the relations `New.Selmer.crysRelations u` of the crystalline cocycles
above `ℓ`. 

### `obeying_crysRelations`

 Let `E` be a CM field in the algebraic closure `Ω` of `ℚ` with a primitive `5040`-th root of
unity, `O` the ring of integers of a finite Galois extension of `ℚ_ℓ` in `ℚ̄_ℓ`, and `u` a matrix
representation of `Gal(Ω/E)` over `O`. A function `c : Gal(Ω/E) → (O/a)^n` obeys the relations
`New.Selmer.crysRelations u` if and only if, for every place `v` of `E` above `ℓ`, its restriction
to the decomposition group of the chosen place over `v` obeys every linear relation
(`New.relationsOn`) that holds on the crystalline cocycles `New.Selmer.crysCocyclesAt v u`. 


## Embeddings at a place above ℓ, local degree and Tate twists

`New.Selmer.IsCompletionGroup e j` says that `j` is an open embedding onto the elements that fix
`e E`.


### `coefficientEmbedding_surjective`

 Every `ℤ_ℓ`-algebra map `O → ℂ_ℓ` is the restriction of an element of `Gp ℓ`, the Galois
group of `ℚ̄_ℓ` over `ℚ_ℓ`: it equals `coefficientEmbedding O g` for some `g`. 

### `tateTwist_smul`

 Let `emb` be an embedding `Ω → ℚ̄_ℓ` that induces the place `A` of `Ω`, with its map
`emb.toGp` from the decomposition group of `A` to `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)`. An element `g` of this
group acts on `O` through the Tate twist `tateTwist ℓ E O c`, the `c`-th power of the inverse
cyclotomic character, as the power `-c` of the local cyclotomic character at `emb.toGp g`. 

### `IsCompletionGroup.complexEmbeddingOf_eq_iff`

 Let `j : Γ → Gp ℓ` be an open embedding whose image is the group of elements that fix `e E`
pointwise (`IsCompletionGroup e j`). Then `g` and `g'` give the same complex embedding
`ι⁻¹ ∘ g⁻¹ ∘ e` if and only if `g * g'⁻¹` is in the image of `j`. 

### `IsCompletionGroup.index_eq_card_range`

 Let `j : Γ → Gp ℓ` be an open embedding whose image is the group of elements that fix `e E`
pointwise. The index of this image is the number of distinct complex embeddings
`complexEmbeddingOf e g = ι⁻¹ ∘ g⁻¹ ∘ e`, for `g` in `Gp ℓ`. 

### `eq_of_complexEmbeddingOf_localChart_eq`

 Let `E` be a CM field in the algebraic closure `Ω` of `ℚ` with a primitive `5040`-th root of
unity, and `ι : ℂ ≃ ℚ̄_ℓ` the isomorphism fixed by `PadicIso ℓ`. Let `v` and `w` be places of `E`
above the prime `ℓ`, and `e_v`, `e_w` the restrictions to `E` of the embeddings `Ω → ℚ̄_ℓ` of their
charts `localChart`. If `ι⁻¹ ∘ g⁻¹ ∘ e_v = ι⁻¹ ∘ g'⁻¹ ∘ e_w` for some `g` and `g'` in
`Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)`, then `v = w`: a complex embedding determines its place above `ℓ`. 

### `sum_complexEmbeddingOf_le`

 Let `E` be a CM field in the algebraic closure `Ω` of `ℚ` with a primitive `5040`-th root of
unity, and `ι : ℂ ≃ ℚ̄_ℓ` the isomorphism fixed by `PadicIso ℓ`. For each place `v` of `E` above the
prime `ℓ`, the chart `localChart ℓ E v` has an embedding `Ω → ℚ̄_ℓ` that induces a place above `v`.
Its restriction `e` to `E` gives the complex embeddings `complexEmbeddingOf e g = ι⁻¹ ∘ g⁻¹ ∘ e`,
for `g` in `Gp ℓ = Gal(ℚ̄_ℓ/ℚ_ℓ)`. For distinct `v` these sets of embeddings are disjoint, so the
sums of `a` over them add up to at most the sum of `a` over all complex embeddings of `E`. 
