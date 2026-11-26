---
{
  "module": "src/Lib/ClassField/Global/ArtinReciprocity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ArtinReciprocity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Global/ArtinReciprocity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Artin's reciprocity law and the sign law

Global reciprocity for a number field `K` with absolute Galois group `Γ`, on finite ideles.

## Overview of this theory

Class field theory, local duality and Hecke `L`-functions, in the cases that the proof uses. Here
`K` is a number field and `Γ` an absolute Galois group.

* `New.IsHeckeOfType.eulerProd_ne_zero`: for a Hecke character `ψ` of `K` whose infinity type is
  given by an integer at each infinite place, with `ψ ^ 2 ≠ 1`, and a finite set `S` of primes, the
  partial `L`-function `L^S(s, ψ)` is nonzero for real `s ≥ 1`.
* `New.IsLocalGalois.classOfInvariant_bijective`: for a henselian local field `k` of characteristic
  `0`, not necessarily complete, the map from `ℚ/ℤ` to `H²(Γ, k̄ˣ)` is bijective. So the Brauer
  group of `k` is `ℚ/ℤ`.
* `New.exists_comp_artinMap`: for totally complex `K`, a continuous homomorphism from the finite
  ideles `𝔸_fˣ` to a `T₁` group that is trivial on `Kˣ` factors continuously through `Art`.
* `New.card_mul_card_le_of_orthogonal`: let `k` be local with valuation ring `O`, `l` a prime with
  `#(O/l) = l ^ d`, and `M` a finite Galois module killed by `l ^ r`. Suppose `M` is fixed by a
  subgroup `Q` containing an `l`-power of every element. If groups of 1-cocycles `X` in
  `Hom(M, k̄ˣ)` and `W` in `M` are orthogonal under cup product, then `#X · #W ≤ #M ^ (2 + d)`.
* `New.RelationSetting.exists_card_cocycles_le`: let `K` be totally complex and `M` finite, killed
  by `ℓ ^ r`, unramified outside a finite set `S`, with local conditions at `S` that contain the
  coboundaries. Relations are equivariant homomorphisms from an open normal subgroup `U` to the dual
  of `M` that obey the reciprocity law at the primes split for `U`. If some element is central
  modulo `U`, fixes the roots of unity of `ℓ`-power order and fixes no nonzero vector, the number of
  relations is bounded from below by the number of Selmer cocycles and the local terms.

These replace local and global class field theory (finite ideles only, no Weil group), local Tate
duality and the Greenberg–Wiles formula (inequalities for cocycles; no perfect pairing, no dual
Selmer group), and the continuation of Hecke `L`-functions (infinity type given by integers, real
`s` only).

`Places` and `GaloisCohomology` give the setting. `Local` builds the invariant and the local Artin
map, and `LocalDuality` counts by Kummer theory and dévissage. In `Global`, prime densities from
`HeckeL` give the second inequality. This gives Chebotarev and, with Tate's index formula for
`S`-units, Albert–Brauer–Hasse–Noether. Norm and existence theorems come next. `GreenbergWiles`
counts cocycles by `S`-units and power residue reciprocity. `Grunwald`, `Avatar` and
`HeckeCharacter` hold applications. `New.exists_avatar` is in `Lib.PadicHodge.Characters`.

## This file

* `New.artin_reciprocity`: if the symbol `(ξ, x)` dies on an open subgroup containing the complex
  conjugations, the character `ξ` kills the Artin symbol of `x ∈ Kˣ`. This applies when `ξ` kills
  the conjugations (`New.abelianLift_artinMap_principalIdele_eq_one`) or `x` is totally positive
  (`New.artinMap_principalIdele_eq_one_of_isTotallyPositive`).
* `New.abelianLift_artinMap_principalIdele_eq_one_iff`: the sign law for characters nontrivial on
  all conjugations.

The case `K(μ_q)` is `New.artin_reciprocity_cyclotomic`. Characters `χ : New.QZChar Γ` are
continuous with values in `ℚ/ℤ`. `New.QZChar.abelianLift χ` is the induced map on the
abelianisation, written multiplicatively. `artinMap Γ (principalIdele x)` is the Artin symbol of the
finite idele of `x`. Only `Γ` is an explicit argument of `artinMap`; `ideleAt v` takes the component
at `v` of an idele. There are no components at the real places.

Notions from other files:
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K (Ω the fixed algebraic
  closure of ℚ; `EmbeddedNumberField K` puts the number field `K` inside Ω) as its Galois group,
  with open stabilisers.
* `New.cyclicClass`: The symbol (χ, w) = δχ ∪ w in H²(Γ, M) of a character χ : Γ → ℚ/ℤ and an
  invariant w; here M = Ωˣ (`New.unitsModule`), and `DiscreteUnits.ofBase` sends `x ∈ Kˣ` to an
  invariant of Ωˣ, and `resH2` restricts classes to a subgroup.
* `New.artinAt`: The local Artin map K_v^× → Γ^ab, through the decomposition group of the chosen
  valuation subring `New.placeOver v` over v.

## Relation to the literature

Known; see `Lib.ClassField.Global.AlbertBrauerHasseNoether` for sources.


### `valuation_smul_div_sub_natCast_lt_one`

 Let `s` be in the inertia group of `A` and send `ζ` (with `ζ ≡ 1` and `ζ ≠ 1`) to `ζ ^ a`. For
a unit `w` of `A` and `y = (ζ - 1) * w`, the quotient `s • y / y` is `≡ a` modulo the maximal
ideal. 

### `map_eq_one_iff_pos`

 A homomorphism `F` from `ℚˣ` to a monoid that is `1` at every prime and not `1` at `-1` is `1`
exactly at the positive rationals. 

### `abelianLift_artinAt_eq_toHom_iff_of_tame`

 The tame symbol at the place `v` of an odd prime `q = v.q` of `ℚ`. Let `ξ` be a character of
`Gal(Ω/ℚ)` whose kernel is that of the cyclotomic character modulo `q`, `ζ` a primitive `q`-th root
of unity with `ζ ≡ 1` at `placeOver v`, and `η` a unit there with `((ζ - 1) η) ^ (q - 1) = q`. For
`x ∈ ℚˣ` a unit at `v` equal to the integer `k` and `g ∈ Gal(Ω/ℚ)`, `ξ` of the local Artin symbol
of `x` is `ξ g` exactly when `k` is the cyclotomic character modulo `q` of `g`. 

### `artin_reciprocity_cyclotomic`

 Artin's law for `K(μ_q)`, `q` an odd prime. Some character `χ` (a) has the same kernel as the
cyclotomic character modulo `q`, and (b) kills the Artin symbol of the finite idele of `x ∈ Kˣ`
exactly when the norm of `x` to `ℚ` is positive. The norm carries the law down to `ℚ`, where `-1`
and the primes generate: `q = N (ζ - 1)`, and a unit at `q` multiplies `ζ - 1` by its residue. 

 ### The law in general 

### `exists_prime_dvd_orderOf`

 For a prime `l` and `a > 1` there is a prime `p > 2`, not dividing `a`, such that `l` divides
the order of `a` modulo `p`. 

### `exists_reciprocity_character`

 Artin's lemma: for a Frobenius `σ` at a place `A` of `Ω` over the finite place `v` of `K` (`v.q`
the size of its residue field), a prime `l` and `m ≠ 0`, some character `χ` that satisfies the
reciprocity law has `m • χ σ` of order not prime to `l`. 

### `finite_mulSupport_abelianLift_artinAt`

 The local symbol `χ (Art_v x)` is trivial at almost all places: there `χ` is unramified and `x`
is a unit. 

### `_root_.dvd_of_addOrderOf_dvd_of_forall_nsmul_ne_zero`

 Let `c` be an element of an additive monoid whose order divides `i`. If, for every prime
`l ∣ n`, no `a • n • c` with `a` prime to `l` vanishes, then `n ∣ i`. 

### `resH2_ker_cyclicClass_eq_zero`

 The local step of Artin's reciprocity law. Let `σ v` be a Frobenius at each place `v` of `K`,
and let `n v` be the order of `ξ` at the local Artin symbol of `x` at `v`. Let the symbol `(ξ, x)`
die on an open subgroup `U` that contains the complex conjugations, and let `χ` be a character such
that, for each `v` and each prime `l ∣ n v`, no `a • n v • χ (σ v)` with `a` prime to `l` vanishes.
Then `(ξ, x)` dies on the kernel of `χ`. 

### `abelianLift_artinAt_eq_of_cyclicClass_eq`

 `Ω` is an algebraic closure of `ℚ`, on which `Γ` acts as the Galois group of `Ω/K`.
If the symbols `(ξ, x)` and `(χ, y)` are equal in `H²(Γ, Ωˣ)`, then `ξ` at the local Artin
symbol of `x` equals `χ` at that of `y`, at every place `v`: both are minus the local invariant of
the symbol, and the local invariant map is injective. 

### `reciprocityChars`

 The characters `χ : Γ → ℚ/ℤ` that satisfy the reciprocity law over `K`: `χ` kills the Artin
symbol of the finite idele of every `y ∈ Kˣ`. 

### `QZChar.coprimeOrderSubgroup`

 For `g : Γ` and `n l : ℕ`, the characters `χ` for which `n • χ g` has order prime to `l`: some
`a` prime to `l` has `a • n • χ g = 0`. 

### `artin_reciprocity`

 Artin's reciprocity law for the number field `K`, with `Ω` an algebraic closure of `ℚ` and
`Γ` the Galois group of `Ω/K`. If the symbol `(ξ, x) = δξ ∪ x ∈ H²(Γ, Ωˣ)` restricts to zero on an
open subgroup `U` that contains the complex conjugations, then `ξ` kills the Artin symbol of the
finite idele of `x`. 

### `abelianLift_artinMap_principalIdele_eq_one`

 Artin reciprocity: if χ kills all complex conjugations, then χ kills the Artin image of the
principal finite idele of every x ∈ K^×, whatever the signs of x at the real places. 

### `artinMap_principalIdele_eq_one_of_isTotallyPositive`

 If `x ∈ Kˣ` is totally positive, the Artin symbol `artinMap Γ (principalIdele x)` of its finite
idele is trivial.

This is a case of Artin's global reciprocity law (triviality on principal ideles), for totally
positive elements and the map on finite ideles. 

### `abelianLift_artinMap_principalIdele_eq_one_iff`

 Sign law: let `χ` be a character of `Γ` that is nonzero on every complex conjugation. Then for
`b ∈ Kˣ`, `χ` kills the Artin symbol of `b` exactly when the norm of `b` to `ℚ` is positive.

This is a consequence of the global Artin reciprocity law; it describes `χ ∘ artinMap` only on
principal finite ideles and only for characters nonzero on every complex conjugation. 
