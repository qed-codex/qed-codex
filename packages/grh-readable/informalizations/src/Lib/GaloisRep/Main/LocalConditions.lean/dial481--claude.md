---
{
  "module": "src/Lib/GaloisRep/Main/LocalConditions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/LocalConditions.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/LocalConditions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local conditions on ℓ-adic Galois representations and their passage to retracts

This file defines local conditions on an `ℓ`-adic representation `r` of `Gal(Ω/E)` (`New.GalRep`) at
a place `A` of `Ω`, that is a `ClosurePlace`: a valuation subring of the fixed field `Ω`, with
valuation `A.valuation`. For `A` above `ℓ`, each condition is stated along the local data
`New.GaloisRep.PadicPlaceEmbedding E A ℓ`. These data consist of an embedding of `Ω` in `ℚ̄_ℓ` that
induces `A`, and a map with open image from the decomposition group to the Galois group of `ℚ_ℓ`.
This map respects Frobenius elements, inertia and the cyclotomic character. Finite type and killing
polynomials pass from a representation to one that embeds in it near the identity. This covers
subrepresentations, restriction to open subgroups and conjugation by automorphisms of `Ω`.

## Main definitions and results

* `New.GaloisRep.IsGoodAt`: unramified, or crystalline.
* `New.GaloisRep.IsFiniteTypeAt`: trivial on an open part of inertia, or potentially crystalline.
* `New.GaloisRep.PolyKillsAt`: the polynomial `P` kills `s`.
* `New.GaloisRep.JumpsRelAt`, `New.GaloisRep.HasJumpsAt`: the Hodge–Tate jumps compared with
  multisets `J`.
* `New.GaloisRep.IsSphericalAbove`: the three conditions that hold at a spherical place `w` of `E`.
* `New.GaloisRep.isFiniteTypeAt_of_retract`, `New.GaloisRep.polyKillsAt_of_retract`,
  `New.GaloisRep.jumpsRelAt_of_retract` (under an extra hypothesis), bundled in
  `New.GaloisRep.local_clauses_of_retract`: finite type, killing polynomials and jumps pass from
  `r'` to a representation `r` that embeds in `r'` near the identity.

Notions from other files:
* `New.Gp`: The absolute Galois group G_p = Gal(Q̄_p over Q_p).
* `New.Period.IsCrystalline`: The elements of B⊗T fixed by the whole group (for
  `New.Period.IsPotentiallyCrystalline`: by the elements near 1) span B⊗T over the period ring B.
* `New.Period.IsWeilPair`: (s, m) with s in G_p acting on the residue field as x ↦ x^(1/p^m).
* `New.Period.IsKilledBy`: T is potentially crystalline and P(β_{s,m}) = 0 on B⊗T, where β_{s,m} is
  the operator `New.Period.linearFrob` of the pair (s, m).
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.inertiaGroup`: the σ with `New.IsFrob A 1 σ`.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank` and `Lib.ClassField.Places.LocalFields` for sources.



## Local conditions at a place

All conditions except those on jumps also have a clause for `A` not above `ℓ` (`A.valuation ℓ = 1`).


### `_root_.New.GalRep`

 A homomorphism from Gal(Ω/E) to the invertible matrices over ℚ̄_ℓ with rows and columns
indexed by m; continuity is not part of the definition. 

### `PadicPlaceEmbedding`

 An embedding of Ω in ℚ̄_ℓ that induces the place A, together with a homomorphism with open image
from the decomposition group of A to Gal(ℚ̄_ℓ/ℚ_ℓ) that goes with it (j(g)(e x) = e(g x) for g in
the decomposition group, the valuation ring of ℚ̄_ℓ pulls back along e to A, and j is an open
embedding) in the sense of `New.GaloisRep.InducesPlace`. 

### `PadicPlaceEmbedding.e`

 The embedding of Ω in ℚ̄_ℓ. 

### `PadicPlaceEmbedding.inducesPlace`

 The embedding induces the place A, and the map of the decomposition group goes with it. 

### `decompRep`

 The restriction of r to the decomposition group of A, acting on column vectors over ℚ̄_ℓ. 

### `IsGoodAt`

 The representation r is good at the place A of Ω: r is trivial on the inertia group of A if ℓ
is a unit at A, and its restriction to the decomposition group of A is crystalline along every
local datum `New.GaloisRep.PadicPlaceEmbedding E A ℓ` (an embedding in Q̄_ℓ inducing A). 

### `IsFiniteTypeAt`

 r is trivial on the inertia elements in a neighbourhood of 1 if ℓ is a unit at A, and
potentially crystalline along every embedding in Q̄_ℓ inducing A.

This corresponds to the classical condition that the Weil–Deligne representation of r at A is
defined and has zero monodromy operator (Grothendieck, Fontaine, Berger). 

### `PolyKillsAt`

 The polynomial P kills the element s of Gal(Ω/E) at the place A for r: P(r(s)) = 0 if ℓ is a
unit at A, and `New.Period.IsKilledBy` holds for every Weil pair (j s, k) with s in the
decomposition group, along every local datum (e, j) at A.

Of the Weil–Deligne representation of r at A (Fontaine's, for A above ℓ), this records only which
polynomials kill a Weil group element; for `A` above `ℓ` the monodromy operator does not enter. 

### `JumpsRelAt`

 Comparison of the Hodge–Tate jumps of `r` at `A` with given multisets `J τ`. For each local
datum at `A` with embedding `e`, each `γ` that agrees with an element `g` of `Gal(ℚ̄_ℓ/ℚ_ℓ)`, and
each integer `u`, the relation `R` holds between two multiplicities. The first is the multiplicity
of `u` in `J` at the embedding `ιℓ⁻¹ ∘ g⁻¹ ∘ e` of `E` in `ℂ`. The second is the multiplicity of `u`
as a jump of `r` at `γ`. For `R = (· = ·)` the jumps are exactly `J` (`New.GaloisRep.HasJumpsAt`).
For `R = New.GaloisRep.OccursIn` every member of `J` is a jump. The condition holds vacuously if
there is no local datum at `A`. Here `ιℓ : ℂ ≃+* ℚ̄_ℓ` is the isomorphism fixed by `New.PadicIso ℓ`,
and `New.Period.jump` is the dimension of the space of Hodge–Tate maps of weight `u`. 

### `HasJumpsAt`

 For each local datum at `A` with embedding `e` and each `g` in `Gal(ℚ̄_ℓ/ℚ_ℓ)`, the Hodge–Tate
jumps of `r` at `g`, with multiplicity, are `J` at the embedding `ιℓ⁻¹ ∘ g⁻¹ ∘ e` of `E` in `ℂ`. 

### `OccursIn`

 Occurrence, as a relation between multiplicities: if m is nonzero, so is n. 

### `IsSphericalAbove`

 At every place A of Ω above the finite place w of E (`New.IsPlaceOver A w`): r is good at A
(`New.GaloisRep.IsGoodAt`), its jump multiplicities are related to J by R, and P kills every
geometric Frobenius s at A, that is every s whose inverse is an arithmetic Frobenius for the
residue field size `w.q` of w. 


## Local embeddings and Frobenii, inertia and the cyclotomic character

Take the data `New.GaloisRep.PadicPlaceEmbedding E A ℓ`. The map of the decomposition group of `A`
into Gal(ℚ̄_ℓ over ℚ_ℓ) respects Frobenius elements
(`New.GaloisRep.PadicPlaceEmbedding.isFrob_iff`). It respects inertia
(`New.GaloisRep.PadicPlaceEmbedding.isWeilPair_zero_iff`). It respects the cyclotomic character
(`New.GaloisRep.PadicPlaceEmbedding.cyclotomicGp_eq_cyclotomicChar`).


### `isFrob_iff`

 Let the local datum h at A consist of the embedding e of Ω in ℚ̄_ℓ and the map j = `h.toGp` of
decomposition groups. Then s in the decomposition group of A is an arithmetic q-Frobenius at A
exactly when j(s) is one for the valuation ring of ℚ̄_ℓ. 

### `isWeilPair_zero_iff`

 Let j = `h.toGp` be the map of decomposition groups of the local datum h at A. For s in the
decomposition group of A, (j s, 0) is a Weil pair, that is j s lies in the inertia group of ℚ̄_ℓ,
exactly when s lies in the inertia group of A. 

### `cyclotomicGp_eq_cyclotomicChar`

 Let j = `h.toGp` be the map of decomposition groups of the local datum h at A. For g in the
decomposition group of A, the cyclotomic character of Gal(ℚ̄_ℓ/ℚ_ℓ) at j g equals the ℓ-adic
cyclotomic character of Gal(Ω/E) at g. 


## Passage of local conditions to retracts and open embeddings

`New.GaloisRep.isFiniteTypeAt_of_retract`, `New.GaloisRep.jumpsRelAt_of_retract` and
`New.GaloisRep.polyKillsAt_of_retract` move local conditions from a Galois representation `r'` to a
representation `r` that embeds in it near the identity (for jumps, isomorphically near the
identity), possibly over another number field. They also cover isomorphic representations.


### `Matrix.eq_zero_of_mulVec_eq_zero_of_mul_eq_one`

 If `P' * P = 1`, then `P *ᵥ x = 0` only for `x = 0`. 

 ### Local data read through conjugation by an automorphism `c` of `Ω` 

### `apply_mem_decompGroup_iff`

 Let `φ : Gal(Ω/E') → Gal(Ω/E)` be conjugation by the automorphism `c` of `Ω`, that is
`φ g (c x) = c (g x)`. Then `φ g` lies in the decomposition group of `A` exactly when `g` lies in
that of `A.comap c`. 

### `mem_inertiaGroup_comap_of_apply_mem_inertiaGroup`

 For `φ` conjugation by `c` as in `New.GaloisRep.apply_mem_decompGroup_iff`: if `φ g` lies in
the inertia group of `A`, then `g` lies in that of `A.comap c`. 

### `decompComap`

 For `φ` conjugation by `c`, the map `g ↦ φ g` from the decomposition group of `A.comap c` in
`Gal(Ω/E')` to that of `A` in `Gal(Ω/E)`. 

### `PadicPlaceEmbedding.inducesPlace_comp`

 Let `L` be a local datum at `A`, with embedding `e` and map `j` of decomposition groups, and
`φ` conjugation by `c`. Then `e ∘ c` induces `A.comap c`, with map `j ∘ decompComap c hφ` of
decomposition groups. 

### `PadicPlaceEmbedding.isOpenEmbedding_comp`

 The map `j ∘ decompComap c hφ` of decomposition groups that goes with the embedding `e ∘ c`
(`L` has embedding `e` and map `j`) is an open embedding. 

### `PadicPlaceEmbedding.comap`

 The local datum at `A.comap c` given by a local datum `L` at `A` (embedding `e`, map `j`) and
conjugation `φ` by `c`: the embedding `e ∘ c` and the map `j ∘ decompComap c hφ`. 

### `PadicPlaceEmbedding.map_nearOne_comap`

 The map `decompComap c hφ` carries the filter of elements near `1` (along `L.comap c hφ`) to
that along `L`. 

### `toLin'_decompRep_comp_of_mem`

 Let `r' g * P = P * r (φ g)` for `g` in `S`. Then multiplication by `P` carries
`decompRep (r ∘ φ) B` to `decompRep r' B` at the elements of `S` in the decomposition group of
`B`. 

### `PadicPlaceEmbedding.eventually_toLin'_decompRep`

 With `P` and `S` as in `New.GaloisRep.toLin'_decompRep_comp_of_mem` and `S` a neighbourhood of
`1`: the same holds at the elements near `1` along the local datum `L.comap c hφ`. 

### `PadicPlaceEmbedding.isPotentiallyCrystalline_decompRep_of_comap`

 Let `P' * P = 1` and `r' g * P = P * r (φ g)` on a neighbourhood `S` of `1`. If `r'` is
potentially crystalline on the decomposition group of `A.comap c` along `L.comap c hφ`, then `r`
is potentially crystalline on that of `A` along `L`. 

### `PadicPlaceEmbedding.isKilledBy_decompRep_of_comap`

 With `P`, `P'` and `S` as in `isPotentiallyCrystalline_decompRep_of_comap`, let `s ∈ S` lie in
the decomposition group of `A.comap c`. If `Q` kills the Weil pair `(j' s, k)` on `r'` along
`L.comap c hφ` (map `j'`), then `Q` kills the Weil pair `(j (φ s), k)` on `r` along `L`
(map `j`). 

### `PadicPlaceEmbedding.jump_decompRep_comap`

 With `P`, `P'` and `S` as in `isPotentiallyCrystalline_decompRep_of_comap`, and also
`P * P' = 1`: the multiplicity of the Hodge–Tate jump `u` at `γ` is the same for `r'` along
`L.comap c hφ` and for `r` along `L`. 

### `valuation_comap_eq_one`

 If `ℓ` is a unit at `A`, it is a unit at `A.comap c`, for an automorphism `c` of `Ω`. 

### `isFiniteTypeAt_of_retract`

 Let `φ : Gal(Ω/E') → Gal(Ω/E)` be conjugation by the automorphism `c` of `Ω`
(`φ g (c x) = c (g x)`), an open embedding. Let `P` have the left inverse `P'`, and let
`r' g * P = P * r (φ g)` for `g` in a neighbourhood `S` of `1`. If `r'` is of finite type at
`A.comap c`, then `r` is of finite type at `A`. 

### `jumpsRelAt_of_retract`

 Let `φ`, `P`, `P'` and `S` be as in `New.GaloisRep.isFiniteTypeAt_of_retract`, without asking
`φ` to be open, let also `P * P' = 1`, and let `i : E → E'` satisfy `c (i x) = x` on `E`. If the
jumps of `r'` at `A.comap c` are related by `R` to `J` read on the restrictions `σ ∘ i`, then
the jumps of `r` at `A` are related by `R` to `J`. 

### `polyKillsAt_of_retract`

 Let `φ`, `P`, `P'` and `S` be as in `New.GaloisRep.isFiniteTypeAt_of_retract`, without asking
`φ` to be open, and let `s ∈ S`. A polynomial `Q` that kills `s` for `r'` at `A.comap c` kills
`φ s` for `r` at `A`. 

### `New.GaloisRep.local_clauses_of_retract`

 Let `c` be an automorphism of `Ω` that carries `i : E → E'` to the inclusion of `E`, and let
`φ : Gal(Ω/E') → Gal(Ω/E)` be conjugation by `c`, an open embedding. Let `P` have a left inverse
`P'` and intertwine `r ∘ φ` with `r'` on a neighbourhood `S` of `1`. Put `A' = c⁻¹ A`. Then: (a) if
`r'` is of finite type at `A'` (trivial on inertia near `1` if ℓ is a unit there, potentially
crystalline otherwise), so is `r` at `A`; (b) if also `P * P' = 1`, a relation `R` between the
multiplicities in `J` and those of the Hodge–Tate jumps passes from `r'` (with `J` read on the
restrictions `σ ∘ i` of the embeddings `σ` of `E'` in `ℂ`) to `r`; (c) a polynomial that kills
`s ∈ S` for `r'` at `A'` (`PolyKillsAt`) kills `φ s` for `r` at `A`.

This is the form in which the compatibility of Weil–Deligne representations and Hodge–Tate weights
with subrepresentations, restriction and conjugation is used; it goes from `r'` to `r` only. 
