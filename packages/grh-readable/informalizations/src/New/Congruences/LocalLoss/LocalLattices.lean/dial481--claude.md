---
{
  "module": "src/New/Congruences/LocalLoss/LocalLattices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/LocalLattices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/LocalLattices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tame classes from roots of unity and lattices read at a place above ℓ

This file passes local properties of an ℓ-adic representation R of the Galois group of E to lattices
over a coefficient ring O. Classes of polynomials defined by roots of unity are shown to be tame.
Conjugate self-dual representations of given level are shown to be trivial on inertia away from ℓ, M
and their level, where M = p₀p₁ is the product of the primes p₀, p₁ of the data.

## Main definitions and results

* `New.Selmer.isTameType_of_roots`: a class of polynomials containing those that vanish on a given
  multiset of at most N roots of unity of orders dividing ℓ^a - 1, 1 ≤ a ≤ r, is
  `New.Lift.IsTameType`.
* `New.Selmer.localLattice`: a lattice restricted to the decomposition group at a place above ℓ.
* `New.Selmer.IsConjSelfDualOfLevel.hasJumps_localLattice`: a lattice in a conjugate self-dual
  representation of given level has the jumps of the representation at a place above ℓ.
* `New.Selmer.IsConjSelfDualOfLevel.inClass_localLattice`: a lattice in a conjugate self-dual
  representation of given level inherits admissibility at a place above ℓ and, if the place divides
  M, the polynomials that kill inertia.

Notions from other files:
* `New.Data.E`: The field E = K(ζ), ζ a primitive root of unity of order q₁ = 3^c 2^s q₀, for the
  exponent s of the data.
* `New.Selmer.AbsGal`: The absolute Galois group of the field E of the data D: automorphisms of an
  algebraic closure of E fixing E.
* `New.CoeffRing`: Rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`.
* `New.Selmer.IsConjSelfDualOfLevel`: R is conjugate self-dual, and at every place outside the level
  S or above ℓ M it is of finite type, has the prescribed jumps, and is good away from M.
* `New.Lift.InClass`: a lattice over O at a place above ℓ is admissible along the supremum of a
  given filter and the filter near 1, has its jumps in given sets, and inertia elements are killed
  on its periods by given polynomials.

## Relation to the literature

See `New.Congruences.FirstOrder.RibetElement` for related work.


### `isTameType_of_roots`

 Let M be a multiset of at most N elements of ℚ̄_ℓ, each a root of X^(ℓ^a − 1) − 1 for some
1 ≤ a ≤ r, and K a property of polynomials over O that holds for all those vanishing on M. Then
`IsTameType ℓ r (N * r) K` holds, that is, K holds for X^e − 1, with e the least common multiple of
the ℓ^i − 1 for 1 ≤ i ≤ r, and for (the image over O of) some monic polynomial over ℤ_ℓ of degree
at most Nr. 

### `localLattice`

 The lattice of `ρ` restricted to the decomposition group at the place `v` above `ℓ`. 

### `IsLatticeIn.exists_equivariant_embedding`

 Let u be a lattice in R, that is, conjugate to R over ℚ̄_ℓ. Then there is an injective map F
from Oⁿ to ℚ̄_ℓⁿ that is semilinear for the inclusion `O.val.val` of O, sends the standard basis to
a basis, and carries the action of u to that of R. 

### `IsLatticeIn.isAdmissible_localLattice`

 Let u be a lattice in R over O, w a place of E above ℓ, and 𝓕 a filter on the decomposition
group at w that is coarser than `nearOne`, the filter of neighbourhoods of 1 pulled back from
Gal(ℚ̄_ℓ/ℚ_ℓ). A representation on T is admissible along 𝓕 if the elements of B_max ⊗ T fixed by
𝓕-almost all group elements span it over B_max. If R at w is admissible along 𝓕, then so is u at
w. 

### `IsLatticeIn.isKilledBy_localLattice`

 Let u be a lattice in R over O and w a place of E above ℓ. Let (s, m) be a Weil pair: s, in the
decomposition group at w, acts on the residue field of ℚ̄_ℓ as x ↦ x^(1/ℓ^m). A polynomial kills (s,
m) on a representation ρ on T (`IsKilledBy`) if ρ is potentially crystalline and the polynomial
vanishes at the B_max-linear operator on B_max ⊗ T that extends φ^m s ⊗ ρ(s), with φ the Frobenius,
from the elements fixed by all g near 1. If the polynomial Q over O, read in ℚ̄_ℓ, kills (s, m) on R
at w, then Q kills (s, m) on u at w. 

### `IsConjSelfDualOfLevel.eq_one_of_mem_inertiaAbove`

 Fix an isomorphism ℂ ≅ ℚ̄_ℓ (`PadicIso ℓ`), let p₀, p₁ be the primes of the data D and M = p₀p₁,
so that `placesAboveM D` is the set of places of E above p₀ or p₁. Let R be a conjugate self-dual
representation of level S: R is conjugate self-dual up to a twist given by t, and local conditions
hold at the places outside S or dividing ℓM, among them the jumps τ, read through this isomorphism.
Then R is trivial on every inertia group above a place of E that is outside S and does not divide
ℓM. 

### `complexEmbeddingAt`

 The complex embedding ι⁻¹ ∘ g⁻¹ ∘ e of E, where e : E → ℚ̄_ℓ is the embedding attached to the
place w above ℓ, g is in Gal(ℚ̄_ℓ/ℚ_ℓ), and ι is the isomorphism ℂ ≅ ℚ̄_ℓ of `PadicIso ℓ`. 

### `crystallinityFilter`

 The filter `⊥` if the place w above ℓ lies above p₀ or p₁, and `⊤` otherwise. A conjugate
self-dual representation of given level is admissible at w along its supremum with the filter near
1: potentially crystalline in the first case, crystalline in the second. 

### `KillsAboveM`

 The place w lies above one of the primes p₀, p₁ of the data, and the polynomial Q over O kills
the pair (s, 0) on every representation in the class 𝓡, restricted to the decomposition group at w
(`New.Period.IsKilledBy`). 

### `jumpSetAt`

 The set of members of τ at `complexEmbeddingAt w g`, for a chosen g in Gal(ℚ̄_ℓ/ℚ_ℓ) that
induces the embedding γ of O. 

### `IsConjSelfDualOfLevel.hasJumps_localLattice`

 Fix an isomorphism ι : ℂ ≅ ℚ̄_ℓ (`PadicIso ℓ`). Let R be a conjugate self-dual representation of
given level with jumps τ, u a lattice in R over O, w a place of E above ℓ with its chosen embedding
e : E → ℚ̄_ℓ, and g in Gal(ℚ̄_ℓ/ℚ_ℓ). Then the Hodge–Tate jumps of u at w, at the embedding x ↦ g(x)
of O in ℂ_ℓ and with multiplicity, are the value of τ at the complex embedding ι⁻¹ ∘ g⁻¹ ∘ e of E
(`complexEmbeddingAt w g`). 

### `IsConjSelfDualOfLevel.inClass_localLattice`

 Fix an isomorphism ℂ ≅ ℚ̄_ℓ (`PadicIso ℓ`), and let p₀, p₁ be the primes of the data D. Let R be
a conjugate self-dual representation of level S with jumps τ that belongs to a class 𝓡 of
representations, u a lattice in R over O, and w a place of E above ℓ. Then u at w satisfies the
three conditions of `New.Lift.InClass`.
* It is potentially crystalline, and crystalline unless w lies above p₀ or p₁.
* At each embedding γ of O in ℂ_ℓ, its Hodge–Tate jumps lie in `jumpSetAt τ w γ`: the set of members
  of the multiset τ at the complex embedding `complexEmbeddingAt w g`, for a chosen g in
  Gal(ℚ̄_ℓ/ℚ_ℓ) that induces γ.
* Suppose w lies above p₀ or p₁ and s is in the inertia group at w. Let Q be a polynomial over O
  such that every member of 𝓡 is potentially crystalline at w and Q vanishes at its operator of s,
  the B_max-linear map on B_max ⊗ T that extends the action of s on the elements fixed by some open
  subgroup of the Galois group (`KillsAboveM 𝓡 w s Q`; T is the space of the representation, B_max
  the period ring `Bmax`). Then Q vanishes at the operator of s for u. 

### `hasJumps_and_inClass_localLattice`

 Let R be a conjugate self-dual representation of level S with jumps τ that belongs to a class 𝓡
of representations, u a lattice in R over O and w a place of E above ℓ. Then for each g in
Gal(ℚ̄_ℓ/ℚ_ℓ) the Hodge–Tate jumps of u at w, at the embedding x ↦ g(x) of O, are the value of τ at
`complexEmbeddingAt w g`. Also u at w satisfies `New.Lift.InClass`: it is potentially crystalline,
and crystalline unless w lies above one of the primes p₀, p₁ of the data; its jumps lie in the sets
`jumpSetAt τ w` of members of τ; and if w lies above p₀ or p₁, a polynomial over O that kills an
inertia element on every member of 𝓡 kills it on u. 
