---
{
  "module": "src/New/Congruences/FirstOrder/KummerMaps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/KummerMaps.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/KummerMaps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kummer maps

Throughout, `ℓ` is a prime and `E` is a CM field in the algebraic closure `Ω` of `ℚ` that contains a
primitive `5040`-th root of unity (`New.CMFieldWithRoot5040`). We pass from `E` to its maximal real
subfield `F`. We write `G = Gal(Ω/E)` and `G_F = Gal(Ω/F)`, `c` for the chosen complex conjugation
and `G_ν` for the elements of `G` that fix the `ℓ ^ ν`-th roots of unity. A Kummer map is the
restriction to `G` of a relation over `F` for the module `ℤ/ℓ^ν` on which `G_F` acts by a power of
`cyc⁺`, the extension to `G_F` of the cyclotomic character of `G` that is `1` at `c`.

* `New.Selmer.IsNuSplitPlace`: a prime of degree one off `ℓ` with a Frobenius element in `G_ν`.
* `New.Selmer.IsKummerMap`, `New.Selmer.IsKummerMap.hasKummerType`: Kummer maps are odd
  homomorphisms on `G_ν`, and conjugation by `g` multiplies those of exponent `e` by
  `cyc(g) ^ (e + 1)`.
* `New.Selmer.IsKummerMap.sum_eq_zero`: the reciprocity law for Kummer maps and even classes;
  `New.Selmer.IsKummerMap.nsmul_apply_tameGenerator_eq_zero` is the case where one term is left.
* `New.Selmer.exists_card_lt_finrank_kummerReductions`: there are many Kummer maps modulo `ℓ`.

Notions from other files:
* `New.FrobeniusDatum`: a prime `w` of `E` of prime norm, a place `valuationSubring` of `Ω` above it
  and a geometric Frobenius element `frob` at that place.
* `New.RelationSetting`: a discrete Galois module with local conditions;
  `New.RelationSetting.relations` is the module of relations off a finite set `T` of primes, in
  place of dual cocycles; `New.Selmer.IsKummerMap` spells the notion out in the case used here.
* `New.Selmer.evenClasses`: for a coefficient ring `O` and a set `S` of primes of `E`, the even
  classes in `(O/ℓ^ν)(-e)` that are unramified off `ℓ`, `S` and `S̄` and vanish on
  `shaLocalSet ℓ E 1`, the elements of `ker cyc` in decomposition groups above `ℓ`.
* `New.cyclotomicCharMod`: the cyclotomic character modulo `N`; `New.cyclotomicChar` is the `ℓ`-adic
  one, written `cyc`.


### `IsNuSplitPlace`

 The datum `x` (a prime of degree one, a place above it and a Frobenius element) is `ν`-split if
its prime does not lie above `ℓ` and its Frobenius element fixes the `ℓ ^ ν`-th roots of unity. 

### `primeBelowPlus`

 The prime of the maximal real subfield `F` below a prime of `E`. 

 ### Passing to the maximal real subfield 

### `toGalPlus`

 The inclusion of `G = Gal(Ω/E)` in `G_F = Gal(Ω/F)`, for `F` the maximal real subfield of
`E`. 

### `conjPlus`

 The chosen complex conjugation `c` (`New.cmConj`) as an element of `G_F`. 

### `toGalPlus_mem_inertiaGroup_iff`

 The inertia group in `G` of a place `A` of `Ω` is the preimage of the one in `G_F`. 

### `notMem_range_toGalPlus`

 No complex conjugation lies in `Gal(Ω/E)`, because `E` is totally complex. 

### `exists_toGalPlus_eq_ite`

 Let `F` be the maximal real subfield of `E` and `G_F = Gal(Ω/F)`. For `σ ∈ G_F`, either `σ` or
`σ c` is the image of some `g` in `G = Gal(Ω/E)` under `toGalPlus E`, where `c` (`conjPlus E`) is
the chosen complex conjugation. 

### `ofGalPlus`

 The map from `G_F = G ∪ G c` to `G = Gal(Ω/E)` that sends `g` and `g c` to `g`, for `g ∈ G` and
`c` the chosen complex conjugation. 

### `continuous_ofGalPlus`

 Let `F` be the maximal real subfield of the CM field `E`, let `Ω` be the algebraic closure of
`ℚ` and `c` the chosen complex conjugation. The map `ofGalPlus : Gal(Ω/F) → Gal(Ω/E)`, which sends
`g` and `g c` to `g` for `g ∈ Gal(Ω/E)`, is continuous. 

### `ofGalPlus_mul_eq_or`

 The map `ofGalPlus` from `G_F = G ∪ G c` to `G = Gal(Ω/E)`, which sends `g` and `g c` to `g`,
is multiplicative up to replacing the second factor `s` by `conjGal s = c s c`. Here `c` is the
chosen complex conjugation. 

### `inertiaGroup_le_range_toGalPlus`

 Let `E` be a CM field in the algebraic closure `Ω` of `ℚ` that contains a primitive `5040`-th
root of unity, and let `F` be its maximal real subfield. Then `E / F` is unramified at the finite
places: the inertia group in `Gal(Ω/F)` of a place `A` of `Ω` above a prime `v` of `F` lies in the
image of the inclusion `toGalPlus E` of `Gal(Ω/E)` in `Gal(Ω/F)`. 

### `ofGalPlus_mem_inertiaAbove`

 Let `F` be the maximal real subfield of `E`, `G = Gal(Ω/E)` and `G_F = Gal(Ω/F)`. The map
`ofGalPlus : G_F → G`, a left inverse of the inclusion, sends the inertia groups above a set `W` of
primes of `F` into the inertia groups above the primes of `E` over `W`. 

### `cyclotomicPlus`

 The character `cyc⁺` of `G_F`: the cyclotomic character times the quadratic character that
cuts out `E`. It is `cyc` on `G` and `1` at `c`. 

### `cyclotomicPlus_eq_one_of_mem_inertiaAbove`

 The character `cyc⁺` is unramified off `ℓ`: it is `1` on the inertia groups above the primes of
`F` that do not divide `ℓ`. 

### `cyclotomicPlus_eq_one_of_isComplexConj`

 The character `cyc⁺` of `G_F` is `1` at every complex conjugation. 

### `cyclotomicKerPlus`

 The subgroup `G_ν` of the elements of `G` that fix the `ℓ ^ ν`-th roots of unity, as an open
normal subgroup of `G_F`. 

### `cyclotomicPlusMod`

 The character `cyc⁺` of `G_F` modulo `ℓ ^ ν`. 

### `tateTwistPlus`

 The module `ℤ/ℓ^ν` with `G_F` acting by `(cyc⁺) ^ (-e)`. 

### `tateTwistPlus_ρ_eq_one`

 An element of the kernel of `cyc⁺` modulo `ℓ ^ ν` acts trivially on `ℤ/ℓ^ν` twisted by
`(cyc⁺) ^ (-e)`. 

### `familyPlace`

 A place of `Ω` above each prime `u` of `F`; if `u` lies below a member of the family `x`, it is
the place of such a member. 

### `exists_familyPlace_eq`

 If the prime `u` of `F` lies below a member of the family `x`, then `familyPlace x u` is the
place of such a member. 

### `isPlaceOver_familyPlace`

 The place `familyPlace x u` of `Ω` lies above the prime `u` of `F`. 

### `exists_isFrob_familyPlace`

 If the prime `u` of `F` lies below a member of the family `x`, then for some `i` the inverse of
the geometric Frobenius element of `x i` is an arithmetic Frobenius element of `G_F` (for the norm
`u.q` of `u`) at `familyPlace x u`, the chosen place of `Ω` above `u`. 

### `familyPrimes`

 The set `S₀` of the primes of `F` above `ℓ` or below a member of the finite family `x`. 

### `cyclotomicPlusMod_eq_one_of_mem_decompGroup`

 Let `F` be the maximal real subfield of `E`, `x` a finite family of `ν`-split places and `u` a
prime of `F` off `ℓ` below a member of `x`. Then the decomposition group of `familyPlace x u`, the
chosen place above `u`, lies in the kernel of `cyc⁺` modulo `ℓ ^ ν`, because inertia and a Frobenius
element do. 

### `kummerSetting`

 The setting over `F` for the exponent `e` and a finite family `x` of `ν`-split places: the
module `ℤ/ℓ^ν` with the action `(cyc⁺) ^ (-e)`, the subgroup `G_ν`, and the set `S₀` of the primes
of `F` above `ℓ` or below `x`. The local condition at a prime `u` consists of the functions on the
decomposition group of `familyPlace x u` that vanish on its part in `ker cyc⁺` if `u` lies above
`ℓ`, and that vanish everywhere otherwise. 

### `IsKummerMap`

 A Kummer map of exponent `e` off `T` for the family `x` of `ν`-split places: the restriction to
`G` of a relation off `T` in `kummerSetting e hx`, where `n ∈ ℤ/ℓ^ν` stands for the character
`a ↦ a n / ℓ ^ ν` of `ℤ/ℓ^ν`. It vanishes outside `G_ν`.

Let `M` be `ℤ/ℓ^ν` with the action `(cyc⁺) ^ (-e)`. A relation off `T`
(`New.RelationSetting.IsRelation`) is a locally constant homomorphism `y : G_ν → Hom(M, ℚ/ℤ)`,
extended by zero to `G_F`, with `y (g u g⁻¹) = cyc(g) · y u ∘ g⁻¹`, zero on inertia at the primes
outside `T`, and such that `∑ p, y(φ_p)(z(γ_p)) = 0`. This sum runs over any finite family of
distinct primes `p ∉ T` of `F` with Frobenius elements `φ_p ∈ G_ν` and tame generators `γ_p`, and
`z` is any cocycle in `M` that satisfies the local conditions at `S₀`, vanishes at complex
conjugations and is unramified off `S₀` and the `p`. These are properties of the restriction to
`G_ν` of a dual cocycle, with ramification allowed at the possibly larger set `T`. 

### `HasKummerType`

 A function `ψ : G → ℤ/ℓ^ν` has the Kummer type of exponent `e` if it is locally constant and, on
the kernel `G_ν` of the cyclotomic character modulo `ℓ ^ ν`, it is a homomorphism that complex
conjugation negates and that conjugation by `g ∈ G` multiplies by `cyc(g) ^ (e + 1)`. 

### `HasKummerType.isLocallyConstant`

 `ψ` is continuous for the discrete topology. 

### `HasKummerType.map_mul`

 `ψ` is a homomorphism on `G_ν`. 

### `HasKummerType.map_conjGal`

 `ψᶜ = -ψ` on `G_ν`. 

### `HasKummerType.map_conj`

 `ψ (g a g⁻¹) = cyc(g) ^ (e + 1) ψ a` for `a ∈ G_ν`. 

### `map_inv`

 A function of Kummer type takes inverses to negatives on the elements that fix the
`ℓ ^ ν`-th roots of unity. 

### `map_pow`

 A function of Kummer type takes powers to multiples on the elements that fix the `ℓ ^ ν`-th
roots of unity. 

### `IsKummerMap.hasKummerType`

 Let `ψ` be a Kummer map of exponent `e` off `T`: the value at `g ∈ G` of a relation `y` is the
character `a ↦ a ψ(g) / ℓ ^ ν` of `ℤ/ℓ^ν`. Then `ψ` is locally constant, and on `G_ν` it is a
homomorphism that complex conjugation negates and that conjugation by `g ∈ G` multiplies by
`cyc(g) ^ (e + 1)`. 

### `comp_ofGalPlus_mem_Z1`

 Let `z` be a cocycle of `G` for `cyc ^ (-e)` modulo `ℓ ^ ν` that is invariant under complex
conjugation. Its extension `z⁺` to `G_F`, given by `z⁺ (g c) = z g`, is a cocycle for
`(cyc⁺) ^ (-e)`. 

### `two_nsmul_comp_ofGalPlus_mem_cocycles`

 Let `Ω` be the algebraic closure of `ℚ`, `F` the maximal real subfield of the CM field `E`, `x`
a finite family of `ν`-split places, `S₀` the set of primes of `F` above `ℓ` or below `x`, and `P` a
set of primes of `F` disjoint from `S₀`. Let `z : Gal(Ω/E) → ℤ/ℓ^ν` be a cocycle for `cyc ^ (-e)`
that is invariant under complex conjugation `c`, unramified off `ℓ` and the primes above `P`, zero
on the part in `ker cyc` of the decomposition groups above `ℓ`, and zero at the Frobenius elements
of `x`. Extend `z` to `z⁺ = z ∘ ofGalPlus` on `G_F = Gal(Ω/F)` by `z⁺ (g c) = z g`, and `cyc` to
`cyc⁺` by `cyc⁺ c = 1`. Then `2 z⁺` lies in `(kummerSetting e hx).cocycles P`: it is a cocycle of
`G_F` in `ℤ/ℓ^ν` for `(cyc⁺) ^ (-e)`, is unramified off `S₀ ∪ P`, vanishes at complex conjugations,
and for `u ∈ S₀` vanishes on the decomposition group of the chosen place `familyPlace x u` (only on
its part in `ker cyc⁺` if `u` lies above `ℓ`). 

### `primeBelowPlus_mem_of_mem_conjClosure`

 Let `F` be the maximal real subfield of `E`. If a prime `t` of `E` lies above `ℓ`, or is the
place of one of the `w j` or a complex conjugate of one, then the prime of `F` below `t`
(`primeBelowPlus t`) lies above `ℓ` or is below the place of one of the `w j`. 

### `IsKummerMap.sum_eq_zero`

 Let `x` and `w` be finite families of `ν`-split places and `T` a finite set of primes of `F`
containing those above `ℓ` or below `x`, such that the `w j` lie above distinct primes of `F`
outside `T`. Let `γ j` be tame generators at the `w j` normalised over `F`. Let `ψ` be a Kummer map
off `T`: it comes from an equivariant homomorphism from `G_ν` to the Cartier dual of a twist of
`ℤ/ℓ^ν` over `F`, unramified outside `T`, that satisfies reciprocity against the `ℤ/ℓ^ν`-valued
cocycles of `Gal(Ω/F)` in `(kummerSetting e hx).cocycles`. Let `z` be an even class of exponent `e`
for `w` that vanishes at the Frobenius elements of `x`. Then `∑ j, ψ(φ_j) · 2 z(γ_j) = 0`, where
`φ_j` is the Frobenius element of `w j`. 

### `exists_isTameGeneratorFor_toGalPlus`

 At a prime of degree one of `E` there is a tame generator in `G` normalised over `F`: an element
of inertia that moves an `m`-th root of a uniformiser of `F` by the fixed root of unity. 

### `exists_apply_eq_nsmul_of_mem_evenClasses`

 Let `w` consist of a prime of `E` of prime norm not above `ℓ`, a place of `Ω` above it and a
Frobenius element, and let `γ ∈ G` be a tame generator at that place, normalised over `F`. Let `O`
be the ring of integers of a finite Galois extension of `ℚ_ℓ` and `z` an even class for `S`: a
locally constant cocycle of `G` in `(O/ℓ^ν)(-e)`, invariant under complex conjugation, unramified
off `ℓ`, `S` and `S̄`, and zero on the elements of `ker cyc` in decomposition groups above `ℓ`; its
values are vectors of length one (indexed by `Unit`) over `QuotSpan (ℓ ^ ν) = O/ℓ^ν`. Then the value
of `z` at an element `τ` of the inertia group at that place is a multiple of `z γ`. 

### `IsKummerMap.nsmul_apply_tameGenerator_eq_zero`

 The reciprocity law `New.Selmer.IsKummerMap.sum_eq_zero` with one term left. Let `x` and `w` be
finite families of `ν`-split places. Let `T` contain the primes of `F` above `ℓ` or below `x`, and
let the `w i` lie above distinct primes of `F` outside `T`. Let `ψ` be a Kummer map off `T` that
vanishes at the Frobenius elements of `w` except at `w j`. Let `O` be the ring of integers of a
finite Galois extension of `ℚ_ℓ` and `z` an even class: a cocycle in `(O/ℓ^ν)(-e)` that is invariant
under complex conjugation, unramified off `ℓ`, the `w i` and their conjugates, and zero on the
elements of `ker cyc` in decomposition groups above `ℓ`. Suppose that `z` vanishes at the Frobenius
elements of `x`. Then every `n` divisible by `2 ψ(φ_j)` in `ℤ/ℓ^ν`, with `φ_j` the Frobenius element
at `w j`, kills the value of `z` at the chosen generator `(w j).isPlaceOver.tameGenerator` of tame
inertia at `w j`. 

### `reductionModL`

 The reduction `G_ν → 𝔽_ℓ` of a map to `ℤ/ℓ^ν`. 

### `kummerReductions`

 The space spanned by the reductions `G_ν → 𝔽_ℓ` of the Kummer maps of exponent `e` for the
family `x`, off `T`. 

### `natCast_dvd_sub_of_cast_eq`

 Elements of `ℤ/ℓ^ν` with the same image in `ℤ/ℓ` differ by a multiple of `ℓ`. 

### `exists_apply_toGalPlus_eq_ofZMod`

 Let `x` be a finite family of `ν`-split places, and let `y` be a relation off the finite set `T`
of primes of the maximal real subfield `F`: an equivariant homomorphism from `G_ν` to the characters
`ℤ/ℓ^ν → ℚ/ℤ`, extended by zero to `G_F = Gal(Ω/F)`, unramified outside `T` and subject to a
reciprocity law. There is a function `ψ : G → ℤ/ℓ^ν` such that the value of `y` at each `g ∈ G` is
the character `a ↦ a ψ(g) / ℓ ^ ν`. 

### `finite_kummerReductions`

 Let `ℓ` be a prime, `E` a CM field that contains a primitive `5040`-th root of unity, `G_ν` the
subgroup of `Gal(Ω/E)` that fixes the `ℓ ^ ν`-th roots of unity, `x` a finite family of `ν`-split
places and `T` a finite set of primes of the maximal real subfield `F`. The Kummer maps
`ψ : Gal(Ω/E) → ℤ/ℓ^ν` of exponent `e` off `T` come from the equivariant homomorphisms from `G_ν` to
the Cartier dual of a twist of `ℤ/ℓ^ν` over `F` that are unramified outside `T` and satisfy a
reciprocity law. Then `kummerReductions e hx T`, the span over `𝔽_ℓ` of the functions
`ψ mod ℓ : G_ν → 𝔽_ℓ`, is finite. 

### `card_reductions_le`

 Let `G_ν` be the subgroup of `G = Gal(Ω/E)` that fixes the `ℓ ^ ν`-th roots of unity, `x` a
finite family of `ν`-split places and `T` a finite set of primes of the maximal real subfield `F`.
Let `M*` be the group of characters `ℤ/ℓ^ν → ℚ/ℤ`. A relation off `T` is an equivariant homomorphism
`y : G_ν → M*`, extended by zero to `Gal(Ω/F)`, unramified outside `T` and subject to a reciprocity
law; its Kummer map `ψ : G → ℤ/ℓ^ν` is given by `y g a = a ψ(g) / ℓ ^ ν`. There are no more
reductions `Gal(Ω/F) → M* / ℓ M*` of relations than elements in the `𝔽_ℓ`-span of the reductions
`G_ν → 𝔽_ℓ` of Kummer maps, because the reduction of `y` is determined by that of `ψ`. 

### `exists_card_lt_finrank_kummerReductions`

 Let `ℓ` be a prime, `ν > 0`, `E` a CM field in the algebraic closure `Ω` of `ℚ` that contains a
primitive `5040`-th root of unity, `F` its maximal real subfield and `G_ν` the subgroup of
`G = Gal(Ω/E)` that fixes the `ℓ ^ ν`-th roots of unity. Let the `x i` be finitely many `ν`-split
places above distinct primes of `F`, and let `E` have at least four infinite places. A Kummer map
`ψ : G → ℤ/ℓ^ν` of exponent `e` off `T` comes from an equivariant homomorphism from `G_ν` to the
Cartier dual of a twist of `ℤ/ℓ^ν` over `F`, unramified outside `T` and subject to a reciprocity
law; conjugation by `g ∈ G` multiplies it by `cyc(g) ^ (e + 1)`. Then there is a finite set `T` of
primes of `F`, containing those above `ℓ` or below the `x i`, such that the functions
`ψ mod ℓ : G_ν → 𝔽_ℓ` span a space of dimension greater than the number of the `x i`. 
