---
{
  "module": "src/Lib/General/NumberTheory/CoefficientRings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CoefficientRings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/CoefficientRings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient rings of ℓ-adic lattices, and length versus cardinality of modules

The coefficient rings over which ℓ-adic lattices are taken, and, for modules over an ℓ-adic
integer ring, a comparison of length with cardinality.

* `New.card_eq_pow_length`: over an ℓ-adic integer ring R with residue field k, a module of finite
  length has #k ^ length elements.
* `New.length_le_of_card_le`, `New.length_le_of_card_dvd`: an inequality of cardinalities (the
  smaller module being finite) or a divisibility of cardinalities gives an inequality of lengths.
* `New.CoeffRing ℓ`: the rings of integers O of finite Galois extensions of ℚ_ℓ inside ℚ̄_ℓ. Each is
  a finite ℤ_ℓ-module, compact, and a discrete valuation ring with divisibility read from the norm
  (`New.CoeffRing.dvd_iff_norm_le`).
* `New.CoeffRing.eventually_mem`: an element of norm at most 1 lies in all sufficiently large
  coefficient rings. That the rings are directed by inclusion is an instance.

Three imported notions occur in the statements:

* `New.ThePrime ℓ`: the class saying that ℓ is prime, which fixes the prime ℓ in scope;
* `New.DVR O`: O is an integral domain and a discrete valuation ring;
* `New.PadicIntegerRing R ℓ`: R is a discrete valuation ring of characteristic 0, finite and free
  over ℤ_ℓ, with finite quotients by nonzero ideals.


### `card_eq_pow_length`

 Let R be an ℓ-adic integer ring (`New.PadicIntegerRing R ℓ`: a discrete valuation ring of
characteristic 0, finite and free over ℤ_ℓ, with finite quotients by nonzero ideals) with residue
field k. An R-module X of finite length has #k ^ length X elements. 

### `PadicIntegerRing.finite_residueField`

 The residue field of an ℓ-adic integer ring R is finite: it is the quotient of R by a nonzero
ideal. 

### `length_eq_top_of_infinite`

 Over an ℓ-adic integer ring R (`New.PadicIntegerRing R ℓ`), an infinite module Y has infinite
length. 

### `length_le_of_card_le`

 Let R be an ℓ-adic integer ring, and let X and Y be R-modules. If X is finite and #X ≤ #Y, then
length X ≤ length Y. The inequality forces Y to be finite too, since `Nat.card X` is positive and
`Nat.card` is 0 for an infinite type. 

### `length_le_of_card_dvd`

 Let R be an ℓ-adic integer ring, and let X and Y be R-modules. If `Nat.card X` divides
`Nat.card Y`, then length X ≤ length Y. Since `Nat.card` is 0 for an infinite type, the hypothesis
says that either Y is infinite, or both modules are finite and #X divides #Y. 

### `length_le_of_card_dvd_or_le`

 Let R be an ℓ-adic integer ring (`New.PadicIntegerRing R ℓ`), and let X and Y be R-modules. If
#X divides #Y, or if #X ≤ #Y and X is finite, then length X ≤ length Y. Here `Nat.card` is 0 for an
infinite type, so finiteness of X is needed in the second case only. 

### `CoeffRing`

 The coefficient rings at ℓ: the ℤ_ℓ-subalgebras of ℚ̄_ℓ that are the ring of integers of some
finite Galois extension K of ℚ_ℓ inside ℚ̄_ℓ, that is, the elements of K of norm at most 1. 

### `CoeffRing.exists_mem_iff`

 A coefficient ring O is cut out by some finite Galois extension K of ℚ_ℓ: its elements are
those of K of norm at most 1. 

### `CoeffRing.norm_le_one`

 The elements of a coefficient ring have norm at most 1. 

### `isIntegral_padicInt_of_norm_le_one`

 An element of ℚ̄_ℓ of norm at most 1 is integral over ℤ_ℓ. 

### `instance : Module.Finite ℤ_[ℓ] O`

 A coefficient ring O, the ring of integers of a finite Galois extension of ℚ_ℓ inside ℚ̄_ℓ, is
a finite ℤ_ℓ-module. 

### `CoeffRing.dvd_iff_norm_le`

 In a coefficient ring, x divides y exactly when the norm of y is at most the norm of x. 

### `instance : DVR O`

 A coefficient ring O is a discrete valuation ring (`New.DVR O`: a domain and a DVR): it is a
Noetherian valuation ring, and it is not a field. 

### `CoeffRing.exists_mem_of_mem_adjoin`

 For a finite set s in ℚ̄_ℓ, some coefficient ring (the ring of integers of a finite Galois
extension of ℚ_ℓ inside ℚ̄_ℓ) contains all elements of ℚ_ℓ(s) of norm at most 1. 

### `instance : ContinuousSMul ℤ_[ℓ] (PadicAlgCl ℓ)`

 The action of ℤ_ℓ on ℚ̄_ℓ is continuous, ℤ_ℓ being the unit ball `PadicInt.subring ℓ` of ℚ_ℓ. 

### `instance : CompactSpace O`

 A coefficient ring O is compact, being finite over the compact ring ℤ_ℓ. 

### `instance : IsDirectedOrder (CoeffRing ℓ)`

 The coefficient rings are directed by inclusion. 

### `CoeffRing.eventually_mem`

 An element of ℚ̄_ℓ of norm at most 1 lies in all sufficiently large coefficient rings: the
rings of integers of finite Galois extensions of ℚ_ℓ inside ℚ̄_ℓ, ordered by inclusion. 
