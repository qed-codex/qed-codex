---
{
  "module": "src/Lib/ClassField/Places/GaloisDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/GaloisDefs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/GaloisDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vocabulary of Galois theory: places, decomposition, Frobenius elements and inertia

This file sets up the vocabulary of Galois theory used by the cohomology files. A Galois group is an
abstract group `Γ` acting on a field `Ω`, and a place of `Ω` is a valuation subring `A`.
`New.IsFrob A q σ` says that `σ` stabilises `A` and that `σ • x - x ^ q` lies in the maximal ideal
for every `x` in `A`. Inertia is the case `q = 1`.

* `New.IsProGalois`, `New.IsLocalGalois`: `Γ` is the profinite Galois group of `Ω / K`; in the local
  case `Ω` is moreover algebraically closed of characteristic `0`, `Γ` stabilises `A`, and `A ∩ K`
  (`New.valRingBelow`) is a discrete valuation ring with finite residue field.
* `New.decompGroup`, `New.inertiaGroup`, `New.IsFrob`, `New.IsPlaceOver`: decomposition group,
  inertia group, Frobenius elements, and places over a nonzero prime of the ring of integers
  `𝓞 K` of a field `K`.
* `New.IsComplexConj`, `New.cyclotomicChar`, `New.cyclotomicCharIn`: complex conjugations and the
  `l`-adic cyclotomic character.

Notions from Mathlib used in the statements:
* `A : ValuationSubring Ω`: a subring that contains `x` or `x⁻¹` for every nonzero `x`, with its
  valuation `A.valuation`; `A.valuation x ≤ 1` means `x ∈ A`, and `< 1` means `x` lies in the
  maximal ideal.
* `IsGaloisGroup Γ K Ω`: `Γ` acts faithfully on `Ω`, fixing `K`, and the elements of `Ω` fixed by
  `Γ` are those of `K`.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.


### `Ω`

 The field `Ω` is an algebraic closure of `ℚ`: it has characteristic zero, is algebraically
closed and is algebraic over `ℚ`. 

### `ClosurePlace`

 The type of valuation subrings of `New.Ω`, the algebraic closure of `ℚ`. 

### `IsComplexConj`

 The element c of Γ is a complex conjugation: for some embedding j : Ω → ℂ, j(cx) is the
complex conjugate of j(x) for all x. 

### `DiscreteUnits`

 The multiplicative group Ω^×, written additively; it is given the discrete topology. 

 ### Profinite and local Galois groups 

### `IsProGalois`

 The profinite group Γ acts on the Galois extension Ω/K as its Galois group, with open
stabilisers. 

### `IsProGalois.isOpen_stabilizer`

 The stabiliser of every element of `Ω` is open in `Γ`. 

### `scoped instance : CoeFun (ValuationSubring Ω) (Ω → ·.ValueGroup)`

 A place `A` of `Ω` is read as its valuation: `A x`. 

### `decompGroup`

 The decomposition group of a valuation subring A of Ω: the elements of Γ mapping A onto
itself. 

### `valuationVia`

 For a valuation subring A of Ω and x in K, the value of the image of x in Ω under the
multiplicative valuation attached to A. 

### `valRingBelow`

 The valuation subring A ∩ K of K. 

### `IsLocalGalois`

 Γ = Gal(Ω/K) with Ω algebraically closed of characteristic 0 stabilises A, and A ∩ K is a
discrete valuation ring with finite residue field. The field K need not be complete. 

### `IsLocalGalois.mem_decompGroup`

 Every element of `Γ` maps the valuation ring `A` to itself. 

### `IsLocalGalois.isDiscreteValuationRing`

 The valuation ring of `K` under `A` is a discrete valuation ring. 

### `IsLocalGalois.finite_residue`

 The residue field of the valuation ring of `K` under `A` is finite. 

### `unitsRep`

 The ℤ-linear representation of Γ on Ω^× (written additively) coming from the action of Γ on
the field Ω by ring automorphisms. 

 ### Frobenius elements, places and inertia 

### `IsFrob`

 `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal ideal for all
`x ∈ A`. For `q` the order of the residue field of the base this is an arithmetic Frobenius;
for `q = 1` it is membership in the inertia group `New.inertiaGroup`. 

### `IsPlaceOver`

 The valuation subring `A` of `Ω` lies over the nonzero prime `v` of the ring of integers `𝓞 K`:
an element of `𝓞 K` is in the maximal ideal of `A` exactly when it lies in `v`. 

### `IsFrob.valuation_sub_pow_lt_one`

 A Frobenius element for `q` sends each `x` of `A` to `x ^ q` modulo the maximal ideal of `A`. 

### `decompGroup.map`

 Let `j : Ω → Ω'` be a ring map and `φ : Γ' → Γ` a map with `j (φ g • x) = g • j x`
(`h_equivariant`). If `s` stabilises `A'`, then `φ s` stabilises the pulled-back subring
`A'.comap j`. 

### `IsFrob.map`

 Let `j : Ω → Ω'` be a ring map and `φ : Γ' → Γ` a map with `j (φ g • x) = g • j x`
(`h_equivariant`). If `s` is a Frobenius element for `q` at `A'`, then `φ s` is one at the
pulled-back subring `A'.comap j`. 

 ### The calculus of Frobenius elements 

### `IsFrob.conj`

 If `σ` is a Frobenius element for `q` at `A`, then `g * σ * g⁻¹` is one at `g • A`. 

### `IsFrob.mul_iff`

 Let `σ` be a Frobenius element for `q` at `A`. Then `σ τ` is a Frobenius element for `q * q'`
if and only if `τ` is one for `q'`. 

### `inertiaGroup`

 The inertia group of A: the σ in Γ stabilising the valuation subring A with σx − x in the
maximal ideal for every x in A. 

### `IsFrob.inv_mul_mem_inertiaGroup`

 Two Frobenius elements `σ`, `τ` for the same `q` at `A` differ by inertia: `σ⁻¹ τ` lies in the
inertia group. 

### `cyclotomicChar`

 The `l`-adic cyclotomic character Γ → ℤ_l^× of a group Γ acting on the field Ω by ring
automorphisms. 

### `cyclotomicCharIn`

 The `l`-adic cyclotomic character of Γ composed with ℤ_l^× → O^×, for a commutative
ℤ_l-algebra O. 
