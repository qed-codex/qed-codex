---
{
  "module": "src/Lib/ClassField/Places/DecompositionCyclotomic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/DecompositionCyclotomic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/DecompositionCyclotomic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decomposition and inertia groups, and cyclotomic characters at Frobenii and inertia

This file studies decomposition and inertia groups of valuation subrings in a Galois group, and the
values of cyclotomic characters at Frobenius elements and on inertia groups. For a valuation subring
`A` of `Ω`, `New.decompGroup Γ A` is the stabiliser of `A`. `New.inertiaGroup Γ A` consists of the
elements of `New.decompGroup Γ A` that act trivially modulo the maximal ideal.
`New.cyclotomicCharMod Ω N : Γ →* (ZMod N)ˣ` and `New.cyclotomicChar Ω l : Γ →* ℤ_[l]ˣ` give the
action on the `N`-th roots of unity and on the roots of unity of `l`-power order, and
`New.IsFrob A q σ` says that `σ` preserves `A` and acts as `x ^ q` modulo its maximal ideal.

## Main definitions and results

* `New.cyclotomicCharMod_eq_iff`: the value at `g` is `a` iff `g • ζ = ζ ^ a` whenever `ζ ^ N = 1`.
* `New.IsFrob.cyclotomicCharMod_eq`, `New.IsFrob.cyclotomicChar_eq`: the value at a Frobenius for
  `q` is `q`, away from `N` or `l`; the case `q = 1` is inertia. The reason is
  `New.eq_of_val_sub_lt_one`: distinct `N`-th roots of unity stay distinct modulo the maximal ideal.
* `New.cyclotomicCharMod_surjective`: for the Galois group of `New.Ω` over `ℚ`, the character modulo
  `N` is onto.

Notions from other files:
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K as its Galois group, with
  open stabilisers.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.



## Decomposition and inertia groups in a Galois group

Here `Γ` is the Galois group of `Ω / K` (`New.IsProGalois`) and `A` is a valuation subring of `Ω`.


### `isClosed_decompGroup`

 For the Galois group `Γ` of `Ω / K`, the decomposition group of `A` is closed. 

### `decompGroup.val_smul`

 For `Γ` the Galois group of `Ω / K`, an element `σ` of the decomposition group of `A` preserves
the valuation of `A`: `σ • x` and `x` have the same valuation for every `x` in `Ω`. 

### `isClosed_inertiaGroup`

 For the Galois group `Γ` of `Ω / K`, the inertia group of `A` is closed. 


## Cyclotomic characters modulo N and ℓ-adic at Frobenii and inertia

Here a group `Γ` acts on a field `Ω` by ring automorphisms. `A N = 1` says that `N` is a unit of
`A`.


 ### Roots of unity modulo a valuation 

### `eq_of_pow_eq_one_of_val_sub_lt`

 Let `A` be a valuation subring of a field `Ω` and `x`, `y` in `Ω` with `x ^ N = y ^ N = 1`. If
the multiplicative `A`-valuation of `x - y` is strictly smaller than that of `N`, then `x = y`. 

### `eq_of_val_sub_lt_one`

 If `N` is a unit of `A` (`hN`), two `N`-th roots of unity that are congruent modulo the maximal
ideal are equal. 

 ### The character modulo `N` 

### `smul_eq_pow_cyclotomicCharMod`

 `g` acts on an `N`-th root of unity `ζ` as the power of `ζ` given by the character modulo
`N`. 

### `cyclotomicCharMod_eq_of_isPrimitiveRoot`

 If `g • ζ = ζ ^ a` for a primitive `N`-th root of unity `ζ`, then the character modulo `N`
takes the value `a` at `g`. 

### `cyclotomicCharMod_eq_iff`

 Let `Ω` be algebraically closed of characteristic zero and `N ≠ 0`. The character modulo `N`
takes the value `a` at `g` if and only if `g • ζ = ζ ^ a` for every `N`-th root of unity `ζ`. 

### `cyclotomicCharMod_eq_of_dvd`

 If `M ∣ N`, a value of the character modulo `N` is also its value modulo `M`. 

### `cyclotomicCharMod_eq_one_of_dvd`

 If `M ∣ N`, the kernel of the character modulo `N` lies in that of the character modulo `M`. 

### `cyclotomicCharMod_eq_iff_unitsRep`

 `New.cyclotomicCharMod_eq_iff` for the units of `Ω` written additively (`DiscreteUnits Ω`, on
which `g` acts by `New.unitsRep`): the value at `g` is `a` if and only if `g` acts on the
`N`-torsion as multiplication by `a`. 

### `cyclotomicCharMod_eq_one_iff`

 `g` is in the kernel of the character modulo `N` if and only if it fixes the `N`-torsion of
the units of `Ω`. 

### `IsFrob.cyclotomicCharMod_eq`

 Let `σ` be a Frobenius for `q` at `A` (`h_frob : IsFrob A q σ`) and let `N` be a unit of `A`
(`hN : A N = 1`). Then the character modulo `N` takes the value `q` at `σ`. 

### `IsFrob.mem_ker_cyclotomicCharMod_iff`

 Let `Ω` be algebraically closed of characteristic zero, `N ≠ 0` a unit of `A` (`hN`), and `σ`
stabilise `A` with `σ x ≡ x ^ q` on `A` (`h_frob`). Then `σ` fixes the `N`-th roots of unity if
and only if `q ≡ 1 [MOD N]`. 

### `cyclotomicCharMod_eq_one_of_mem_inertiaGroup`

 An element of the inertia group of `A` lies in the kernel of the character modulo any `N` that
is a unit of `A`. 

### `zmod_eq_natCast_val`

 A residue modulo `N` is the cast of its natural representative. 

### `map_cyclotomicCharMod_mul`

 Every additive map from `ZMod N` to the units of `Ω` is equivariant, when `g` acts on `ZMod N`
through the character. 

 ### The `l`-adic character 

### `cyclotomicCharMod_prime_pow_eq`

 The character modulo `l ^ r` is the reduction of the `l`-adic character. 

### `pow_dvd_cyclotomicChar_sub_iff`

 `l ^ r` divides `χ_l(σ) - q` in `ℤ_l` if and only if the character modulo `l ^ r` takes the
value `q` at `σ`; here `χ_l` is the `l`-adic cyclotomic character `New.cyclotomicChar Ω l`. 

### `map_cyclotomicChar_smul`

 Let `Ω` be algebraically closed of characteristic `0`, let `A` be a `ℤ_l`-module (here not the
valuation subring) and `f : A → B` additive with image killed by `l ^ r` (`h_kill`). Then
`f (χ_l(σ) • x) = χ_{l^r}(σ) • f x`, where `χ_l` is the `l`-adic and `χ_{l^r}` the mod `l ^ r`
cyclotomic character. 

### `IsFrob.cyclotomicChar_eq`

 Let `Γ` act on the algebraically closed field `Ω` of characteristic `0`, let `σ ∈ Γ` be a
Frobenius for the natural number `q` at the valuation subring `A` of `Ω`, and let the prime `l` be
a unit of `A`. Then the `l`-adic cyclotomic character takes the value `q` at `σ`. 

### `cyclotomicChar_eq_one_of_mem_inertiaGroup`

 An element of the inertia group of `A` lies in the kernel of the `l`-adic cyclotomic character
when the prime `l` is a unit of `A`. 

### `cyclotomicCharMod_eq_of_equivariant`

 Let `Γ`, `Γ'` act on algebraically closed fields `Ω`, `Ω'` of characteristic `0`, let `g ∈ Γ`,
`g' ∈ Γ'` and let `N` be a non-zero natural number. If the ring homomorphism `j : Ω → Ω'`
intertwines `g` and `g'` (`h_comm`), the characters modulo `N` agree at `g` and `g'`. 

### `cyclotomicChar_eq_of_equivariant`

 Let `Γ`, `Γ'` act on algebraically closed fields `Ω`, `Ω'` of characteristic `0`, and let
`j : Ω → Ω'` be a ring homomorphism with `j (g • x) = g' • j x` for all `x` (`h_comm`). Then the
`l`-adic cyclotomic characters at `g` and `g'` agree, for the prime `l`. 

### `continuous_cyclotomicChar`

 For the Galois group `Γ` of `Ω / K`, with `l` a prime natural number, the `l`-adic cyclotomic
character is continuous. 

### `isOpen_ker_cyclotomicCharMod`

 For the Galois group `Γ` of `Ω / K`, with `Ω` algebraically closed of characteristic `0` and
`N ≠ 0` a natural number, the kernel of the character modulo `N` is open. 

 ### Roots of unity and the cyclotomic field 

### `rootPowHom`

 An injective additive map from ℤ/N to Ω^× (written additively) whose image is the set of
elements killed by N. It sends a to ζ^a for a chosen primitive N-th root of unity ζ. Here `Ω` is
algebraically closed of characteristic 0, and `N ≠ 0`. 

### `cycloGalGroup`

 The subgroup of Gal(ℚ̄/ℚ) = `Gal(New.Ω/ℚ)` fixing all N-th roots of unity, for a natural number
`N ≠ 0`: the absolute Galois group of ℚ(ζ_N). 

### `cycloField`

 The cyclotomic field ℚ(ζ_N) inside ℚ̄, defined as the fixed field of `New.cycloGalGroup N`. 

### `instance : IsCyclotomicExtension {N} ℚ (cycloField N)`

 `New.cycloField N` is the cyclotomic extension of `ℚ` generated by the `N`-th roots of unity. 

### `cyclotomicCharMod_surjective`

 For a natural number `N ≠ 0` and the Galois group of `New.Ω` (ℚ̄, an algebraically closed field
of characteristic `0`) over `ℚ`, the character modulo `N` is surjective. 
