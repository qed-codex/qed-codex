---
{
  "module": "src/New/Congruences/Selmer/StickelbergerSystems.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerSystems.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerSystems.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stickelberger systems

A Stickelberger system consists of elements `Θ_Q` of the group rings over `ℤ̄_ℓ` of the class groups
`Cl_Q` of norm-one finite ideles, one for each finite set `Q` of places. Their values under
characters for `Q` change by Euler factors when `Q` grows to an auxiliary set. A character for
`Q` is a Galois character with `IsFromU1 (placesDividing E ℓ) Q`; it is read on `Cl_Q` through
`y / ȳ ↦ Art y`. Its order is not assumed to be a power of `ℓ`.

* `New.Selmer.U1ClassGroup`, `New.Selmer.groupRingEval`: the group `Cl_Q`, and the value of a
  function on the Galois group at an element of its group ring.
* `New.Selmer.StickelbergerSystem`, `New.Selmer.StickelbergerSystem.β`: the systems and their
  constant.

Notions from other files:
* `New.Ω`: the algebraic closure of `ℚ` into which every number field in this file is embedded;
  `Gal(Ω/E)` is the absolute Galois group of `E`, and `New.ClosurePlace` is the type of places
  (valuation subrings) of `Ω`.
* `New.IsFromU1 S I χ`, for sets `S` and `I` of finite places of a CM field `E`: the Galois
  character `χ` is locally constant and satisfies `χ(Art y) = η(y / ȳ)` for an idele class
  character `η` that is trivial on the local components at `S` and its conjugates and has
  modulus `I` away from these places.
* `New.IsAuxiliary S Q`: the places of `Q` have prime norm, neither they nor their conjugates lie in
  `S`, and their conjugates lie outside `Q`.
* `New.ellVal`: the valuation `v` on `ℚ̄_ℓ` with `v ℓ = 1`, cut off below at `0`; `New.intQpBar ℓ`
  is the ring `ℤ̄_ℓ` of integral elements.
* `New.artinMap`: the Artin map from the finite ideles to the abelianised Galois group.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `IsFromU1.mono`

 Enlarging the modulus: let the character `χ` of the absolute Galois group `Gal(Ω/E)` satisfy
`χ(Art y) = η(y / ȳ)` for an idele class character `η` of modulus `I` that is trivial at the places
of `S` and their conjugates (`IsFromU1 S I χ`). Then the same holds for any modulus `I'` that
contains `I`. 

### `IsFromU1.map`

 Let the Galois character `χ` with values in a commutative monoid `C` satisfy
`χ(Art y) = η(y / ȳ)` for an idele class character `η` of modulus `I` that is trivial at the places
of `S` and their conjugates (`IsFromU1 S I χ`). For a homomorphism `f : C → C'` the same holds for
`f ∘ χ`, with `f ∘ η` in place of `η`. 

### `IsFromU1.one`

 The trivial Galois character comes from the trivial idele class character, so it satisfies
`IsFromU1 S I` for all sets `S` and `I` of places. 

### `IsFromU1.mul`

 If the Galois characters `χ` and `χ'` of `Gal(Ω/E)` both satisfy `IsFromU1 S I`, that is, they
come by `y ↦ y / ȳ` from idele class characters of modulus `I` that are trivial at the places of `S`
and their conjugates, then so does their product `χ * χ'`; it comes from the product of these idele
class characters. 

### `IsAuxiliary.mono`

 Let `I'` be a finite set of places of a CM field that is auxiliary for `S`: its places have
prime norm, neither they nor their conjugates lie in `S`, and their conjugates lie outside `I'`.
Then every subset `I` of `I'` is auxiliary for `S`. 

### `U1ClassGroup`

 The group `Cl_Q`: finite ideles `u` with `u ū = 1`, modulo those in `Eˣ` and the units that
are `≡ 1` at the primes of `Q`. 

### `divStarClass`

 The class of `y / ȳ` in `Cl_Q`, for a finite idele `y`. 

### `divStarClass_surjective`

 Let `E` be a CM field, with complex conjugation `y ↦ ȳ`, and `Q` a finite set of finite places
of `E`. The map `divStarClass Q`, which sends a finite idele `y` to the class of `y / ȳ` in `Cl_Q`,
is surjective, by Hilbert's Theorem 90 for finite ideles. 

### `galoisLift`

 A chosen element of the Galois group that lifts `Art y`, for a chosen finite idele `y` with
`y / ȳ` in the class `c`. 

### `_root_.New.IsFromU1.apply_galoisLift`

 Let `E` be a CM field, `Gal(Ω/E)` its absolute Galois group, and `Q` a finite set of places of
`E`. Let the character `χ` of `Gal(Ω/E)` satisfy `χ(Art y) = η(y / ȳ)` for an idele class character
`η` of modulus `Q` that is trivial at the places of `S` and their conjugates (`IsFromU1 S Q χ`). If
the image of `g` in the abelianised Galois group is the Artin symbol of the idele `y`, then `χ` has
the same value at `g` and at `galoisLift (divStarClass Q y)`, the chosen Galois element for the
class of `y / ȳ` in `Cl_Q`. 

### `groupRingEval`

 The value of a function `f` on the Galois group, read on `Cl_Q` through `galoisLift` and
extended linearly, at an element of the group ring of `Cl_Q`. 

### `map_groupRingEval`

 A linear map `L` commutes with the evaluation of group-ring elements: applying it to the value
of `f` gives the value of `L ∘ f`. 

### `groupRingEval_sum_single`

 The value of `f` at an element `∑ i ∈ s, c i • [u i]` of the group ring of `Cl_Q` is the sum
of the `c i • f (galoisLift (u i))`. 

### `eulerFactor`

 The product of the factors `1 - a ^ (±1) q ^ (-e)` over a list of integers `e` and both
signs. 

### `eulerFactor_zpow_units`

 The product of Euler factors at `a` is symmetric in `a` and `a⁻¹`. 

### `StickelbergerSystem`

 A Stickelberger system for a finite set `S₀` of places of the CM field `E` and an element `g₀`
of `Gal(Ω/E)` consists of a character `ϑ = twistChar` unramified outside `S₀` with `ϑ g₀ ≠ 1`, a
list of integers `exponents`, and an element `Θ_Q = element Q` of the group ring of `Cl_Q` over
`ℤ̄_ℓ` for every finite set `Q` of places, whose values under characters for `Q` change by Euler
factors when a place is added to `Q` such that the enlarged set is auxiliary for `S₀`. 

### `StickelbergerSystem.twistChar`

 The character `ϑ` by which the characters `ψ` are twisted in the Euler factors. 

### `StickelbergerSystem.continuous_twistChar`

 `ϑ` is continuous; so its values are `ℓ`-adic units. 

### `StickelbergerSystem.unramified`

 `ϑ` is unramified outside `S₀`. 

### `StickelbergerSystem.twistChar_apply_ne_one`

 `ϑ` is not trivial at `g₀`. 

### `StickelbergerSystem.exponents`

 The list of exponents `e` of `(N P)⁻¹` in the Euler factors. 

### `StickelbergerSystem.element`

 The element `Θ_Q` of the group ring of `Cl_Q` attached to a finite set `Q` of places. 

### `StickelbergerSystem.one_element_empty_ne_zero`

 The trivial character does not vanish at the element for the empty set. 

### `StickelbergerSystem.element_insert`

 The norm relation: for a character `ψ` for `Q`, adding a prime `P` to `Q` multiplies the
  value of `ψ` by the factors `1 - (ϑ ψ)(φ) ^ (±1) (N P) ^ (-e)`, where `φ` is any Frobenius
  element at `P`. As both signs occur, arithmetic and geometric Frobenius elements give the same
  product. 

### `β`

 For a Stickelberger system `Y`, the number `β = v(1(Θ_∅)) + ∑_e 2 v(ϑ(g₀) - 1)`. Here `v` is
the `ℓ`-adic valuation `ellVal`, `ϑ = Y.twistChar`, `g₀` is the Galois element at which the system
has `ϑ(g₀) ≠ 1`, `e` runs over the list `Y.exponents`, and `1(Θ_∅)` is the value of the trivial
character at the group-ring element `Θ_∅ = Y.element ∅`. 

### `norm_twistChar`

 The values of the character `Y.twistChar` (written `ϑ`), read in `PadicAlgCl ℓ`, have norm one,
as `ϑ` is continuous on a compact group. 

### `norm_groupRingEval_one_element_le_one`

 Let `Y` be a Stickelberger system, so `Θ_Q = Y.element Q` is an element of the group ring over
`ℤ̄_ℓ` of the group `Cl_Q` of norm-one idele classes. The value of the trivial character at `Θ_Q`
has norm at most one, as it is the image of an element of `ℤ̄_ℓ`. 

### `β_ne_top`

 For a Stickelberger system `Y` for `S₀` and `g₀`, the number
`β = v(1(Θ_∅)) + ∑_e 2 v(ϑ(g₀) - 1)` is finite. Here `v` is the `ℓ`-adic valuation, infinite only
at `0`, `ϑ = Y.twistChar`, `e` runs over `Y.exponents`, and `1(Θ_∅)` is the value of the trivial
character at the group-ring element `Y.element ∅`; by the axioms of the system this value is not
`0` and `ϑ(g₀) ≠ 1`. 

### `groupRingEval_element_union`

 The norm relation for several primes. Let `E` be a CM field with absolute Galois group
`Gal(Ω/E)`, and `Y` a Stickelberger system for a finite set `S₀` of places and `g₀ ∈ Gal(Ω/E)`: a
character `ϑ = Y.twistChar` unramified outside `S₀` with `ϑ g₀ ≠ 1`, a list `Y.exponents` of
integers, and group-ring elements `Θ_Q = Y.element Q` with a norm relation. Let `Q` and `I` be
disjoint with `Q ∪ I` auxiliary for `S₀`, let the Galois character `ψ` come from an idele class
character of modulus `Q` trivial above `ℓ` (`IsFromU1`), and for `v` in `I`, of norm `v.q`, let
`φ v` be a Frobenius element at a place (valuation subring) `A v : ClosurePlace` of `Ω` over `v`.
Then the value of `ψ` at `Θ_{Q ∪ I}` is its value at `Θ_Q` times the factors
`1 - (ϑ ψ)(φ v) ^ (±1) (v.q) ^ (-e)` for `v` in `I`, `e` in the list and both signs. 
