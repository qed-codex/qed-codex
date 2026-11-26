---
{
  "module": "src/Lib/ClassField/GreenbergWiles/SplitPrimeReciprocity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SplitPrimeReciprocity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GreenbergWiles/SplitPrimeReciprocity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trivialised cocycles and power residue relations at split primes

Let `G` act on a discrete module `V`. A trivialised cocycle is a pair `(f, z)` of a continuous map
`z : G → V` vanishing on `I` and a map `f : X → V` with `g • f x = f (g • x) + z g`; when `X` is
nonempty, `z` is then a cocycle. At split primes off `N`, the values of such cocycles on tame
generators `γ i` of inertia satisfy linear relations.

## Main definitions and results

* `New.DiscreteModule.trivialisedCocycles`: pairs `(f, z)` of a continuous `z : G → V` vanishing on
  `I` and `f : X → V` with `g • f x = f (g • x) + z g`; so `z` is the coboundary of `f x` on the
  stabiliser of `x`.
* `New.DiscreteModule.trivialisedCocycles.exists_mem_of_orbit_reps`,
  `New.DiscreteModule.trivialisedCocycles.corestrict_mem`: such pairs are built from data at one
  point per orbit, and by corestriction.
* `New.DiscreteModule.trivialisedCocycles.hasFewCocycles_of_isShortExact`: the bound `(#V) ^ k` for
  the number of such pairs (`New.DiscreteModule.HasFewCocycles`) passes from the ends of a short
  exact sequence to the middle term.
* `New.IsLargeLevel.SplitPlaces.exists_powerResidueSymbols` (as one conjunction,
  `power_residue_reciprocity`): the `m`-th power residue symbols of the `N`-units of the field of
  `U` give linear relations among these values when `V` is trivial on `U`. If the field of `U` is
  totally complex, solutions of the relations give such cocycles.

Notions from other files:
* `New.DiscreteModule R G`: an `R`-module `V` with the discrete topology and a continuous `R`-linear
  action `ρ` of `G`; `New.DiscreteModule.restrictTo` restricts the action to a subgroup.
* `New.Z1`: the `R`-module of continuous 1-cocycles of `ρ`, that is, of continuous maps
  `f : G → M` with `f (g * h) = f g + ρ g (f h)`.
* `New.IsLargeLevel.SplitPlaces`: Split places for `U`. The subgroup `U` fixes the `m`-th roots of
  unity, and `m` divides `N`.
* `New.IsLargeLevel.fixedSUnits`: The N-units of the fixed field of U; `fixedSUnitsRep` is the
  action of G / U on them.
* `New.IsTameGeneratorFor`: γ lies in the inertia group of A, and γy/y is the root of unity
  `New.rootPowHom Ω m 1` for some m-th root y of some uniformiser π of K for A.

## Relation to the literature

Known; see `Lib.ClassField.GreenbergWiles.CocycleCounts` for sources.


 ## Cocycles trivialised at places and corestriction 

### `trivialisedCocycles`

 Trivialised cocycles: pairs of f : X → V and continuous z : G → V vanishing on I, with
g f(x) = f(gx) + z(g) for all g, x. 

### `mem_trivialisedCocycles`

 Membership in `New.DiscreteModule.trivialisedCocycles`, written out. 

### `HasFewCocycles`

 There are finitely many trivialised cocycles, at least one and at most `#V ^ k`. 

### `map`

 For an equivariant map u : A → B, the additive map between the groups
`New.DiscreteModule.trivialisedCocycles` of A and B that composes both components of a pair of
functions with u. 

### `card_eq_of_isShortExact`

 For a discrete `G`-module `V` over `R`, a `G`-set `X` and `I ⊆ G`, the trivialised cocycles
`V.trivialisedCocycles X I` are pairs of a map `f : X → V` and a continuous `z : G → V` vanishing on
`I`, with `g • f x = f (g • x) + z g` for all `g`, `x`. For a short exact sequence
`0 → A → B → C → 0` of discrete `G`-modules with maps `ι`, `π`, the number of trivialised cocycles
of `B` equals the number for `A` times the size of the image of the map `map X I π` that `π` induces
into those of `C`. 

### `snd_mem_Z1`

 If `X` is nonempty, the second component `z` of a trivialised cocycle `(f, z)` is a continuous
1-cocycle. 

### `exists_mem_of_orbit_reps`

 Let the points `x i` represent the orbits of `G` on `X`, and let `z` be a cocycle that vanishes
on `I`. If `m i` trivialises `z` on the stabiliser of `x i` for each `i`, then `z` has a
trivialisation `f` on all of `X` with `f (x i) = m i`. 

### `out_inv_mul_mul_out_mem`

 With `x.out` the chosen representative of a coset `x ∈ G / H`, the element
`x.out⁻¹ * g * (g⁻¹ • x).out` lies in `H`. 

### `corestrict_mem`

 Corestriction. Let `P` be an open subgroup of finite index that contains `I`, let `I` be
stable under conjugation, and let `(f, c)` be a trivialised cocycle for `P` and `I`.
With `s x = x.out` the chosen representative of the coset `x ∈ G / P`, the pair of
`y ↦ ∑ x, s x • f ((s x)⁻¹ • y)` and `g ↦ ∑ x, s x • c ((s x)⁻¹ * g * s (g⁻¹ • x))`
is a trivialised cocycle for `G` and `I`. 

### `hasFewCocycles_of_isShortExact`

 Let `0 → A → B → C → 0` be a short exact sequence such that `A` and `C` have few trivialised
cocycles. Then so has `B`. If the count for `B` reaches its bound `#B ^ k`, then every trivialised
cocycle of `C` lifts to `B` and the count for `A` reaches its bound `#A ^ k`. 


## Power residue relations among values on inertia at split primes

Fix primes `s.v i` off `N` with places `s.valuationSubring i` of `Ω`, Frobenii `s.φ i` in the open
normal subgroup `U` of `G = Gal(Ω/K)`, and tame generators `γ i` of inertia at
`s.valuationSubring i`. We describe the values `z (γ i)` of cocycles `z` that are trivialised above
`N` and infinity and vanish on the inertia `I` at all other primes off `N`.

`New.DiscreteUnits Ω` is `Ωˣ` written additively (as the discrete module `unitsModule G`;
`(unitsModule G).H0` is its `G`-invariants, and `ofBase` maps the units of the fixed field onto
them), so `m • r = y` means `r ^ m = y`, `unitsRep g r - r` is `g r / r`, and `New.rootPowHom Ω m a`
is `ζ ^ a` for a fixed primitive `m`-th root of unity `ζ`, and `cyclotomicCharMod Ω m g` is the
`c : ZMod m` with `g ζ = ζ ^ c`.


### `eq_one_or_isComplexConj`

 Let `G` act on `Ω` as the Galois group of `Ω` over a field `L`. An element `g` of `G` that fixes
an infinite place `u` of `Ω` is `1` or a complex conjugation. 

### `IsTameGeneratorFor.exists_apply_eq_nsmul`

 Let `A` lie over a prime `v` not dividing `m`, and let `γ` in the inertia group of `A` move an
`m`-th root of a uniformiser by the primitive root `ζ`. A locally constant map `f` to a group
killed by `m` that is additive on inertia takes there only multiples of `f γ`. 

### `IsLargeLevel.SplitPlaces.apply_inertia_eq_zero`

 Let `G` be the Galois group of the algebraic closure `Ω` over `K`, and let `V` be killed by `m`
and fixed by `U`. A cocycle that vanishes at a tame generator `γ` at `s.valuationSubring i`
vanishes on the inertia group of every place `A` of `Ω` over the prime `v = s.v i`. 

### `kummer_eq_zero_of_mem_inertiaGroup`

 The Kummer character `κ x` of an element `x` of valuation one vanishes on inertia at a place
that does not divide `m`. 

### `IsTameGeneratorFor.kummer_apply_conj`

 Let `γ` move an `m`-th root of a uniformiser at `A` by the fixed root of unity, and let `U`
contain the decomposition group of `g • A`. At `g γ g⁻¹` the Kummer character of an element `x` of
the fixed field of `U` is the order of `x` at the prime `u ∤ m` under `g • A`, times
`cyclotomicCharMod Ω m g`. 

### `exists_kummer_root`

 If `K` contains the `m`-th roots of unity, every continuous character `χ : G → ℤ/m` is the
Kummer character of an element `x = r ^ m` of `K`. 

### `IsKummerMap`

 A Kummer map for `U`: an additive map `κ` from the `U`-invariants of `Ωˣ` to the characters
`U → ℤ/m` with `ζ ^ κ x q = q r / r` whenever `r ^ m = x`. 

### `liftToFixedField`

 The split family `s` over the field of `U`: the index `(i, g)` names the place
`g⁻¹ • s.valuationSubring i`, the prime of the field of `U` below it, and the Frobenius
`g⁻¹ (s.φ i) g`, where `g` is the chosen representative of the coset. 

### `kummer_conj_liftToFixedField`

 For `θ = (i, g)`, the Kummer character of an element `x` of the field of `U` takes at
`g⁻¹ (γ i) g` the value `cyclotomicCharMod Ω m g⁻¹` times the order of `x` at the prime
`(liftToFixedField s).v θ`. 

### `IsLargeLevel.SplitPlaces.kummer_frob_liftToFixedField`

 For `θ = (i, g)`, the Kummer character of an `N`-unit `x` takes at the Frobenius
`(liftToFixedField s).φ θ` the value `cyclotomicCharMod Ω m g⁻¹` times the symbol `b` of `g x` at
`i`. 

### `snd_trivialisedCocycles_eq_zero_of_smul_eq`

 A trivialised cocycle `(f, z)` for the places above `N` and infinity vanishes at each
element of `U` that fixes such a place, since `U` acts trivially on `V`. 

### `snd_trivialisedCocycles_eq_zero_of_isComplexConj`

 A trivialised cocycle `(f, z)` for the places above `N` and infinity vanishes at each complex
conjugation in `U`: it fixes the infinite place of `Ω` that it conjugates. 

### `snd_eq_zero_of_mem_decompGroup`

 A trivialised cocycle `(f, z)` for the places above `N` and infinity vanishes on the
decomposition groups in `U` of the primes above `N`. 

### `IsLargeLevel.SplitPlaces.snd_eq_zero_of_snd_generators_eq_zero`

 Part (b) of `New.IsLargeLevel.SplitPlaces.power_residue_reciprocity`: a trivialised cocycle
`(f, z)` for the places above `N` and infinity, with `z` zero at all `γ i`, vanishes on `U`. 

### `IsLargeLevel.SplitPlaces.sum_ord_smul_kummer_frob_eq_zero`

 Artin's law for the character `χ = κ y / m` of an `N`-unit `y` of the field `F` of `U` and an
element `x` of `F` with an `m`-th root `r`. Let `r` be fixed by the complex conjugations in `U`, by
the decomposition groups above `N`, and by the elements of `U` in `I`. Then
`∑ θ, ord(x) • χ (S.φ θ) = 0`, where `S = liftToFixedField s` and the order is taken at `S.v θ`. 

### `IsLargeLevel.SplitPlaces.sum_symbol_smul_snd_generators_eq_zero`

 Part (c) of `New.IsLargeLevel.SplitPlaces.power_residue_reciprocity`: for a trivialised
cocycle `(f, z)` for the places above `N` and infinity, each `N`-unit `y` gives the relation
`∑ b (g y) i • g⁻¹ z (γ i) = 0`, summed over `i` and `g ∈ G / U`. It is Artin's law for the
character `κ y` and the idele of an `x` in the field of `U` whose Kummer character is `l ∘ z`. 

### `IsLargeLevel.SplitPlaces.exists_mem_trivialisedCocycles_of_valuation`

 The cocycle of part (d) of `New.IsLargeLevel.SplitPlaces.power_residue_reciprocity`. Let `x` in
the field of `U` be a local `m`-th power above `N`, a unit at the other primes outside the lifted
family `liftToFixedField s`, and of order `cyclotomicCharMod Ω m g * f (i, g)` at its prime of index
`(i, g)`. Then `z = κ x • a` is trivialised at the places above `N` and infinity, and its
corestriction to `G` has the values `z (γ i) = ∑ g, g (f (i, g) • a)`. 

### `IsLargeLevel.SplitPlaces.exists_mem_trivialisedCocycles_of_sum_symbol_mul_eq_zero`

 Part (d) of `New.IsLargeLevel.SplitPlaces.power_residue_reciprocity`: let the field of `U` be
totally complex. A family `f` that satisfies the relations of the symbols `b` gives, for each
`a : V`, a trivialised cocycle with `z (γ i) = ∑ g, g (f (i, g) • a)`. The hypothesis `h_idele` is
the converse half of Kummer theory for `κ` (`New.exists_kummer_chars`) at the primes above `N`: an
idele whose Artin symbol is killed by `κ u` for all `N`-units `u` is principal times an `m`-th power
above `N` that is a unit off `N`. 

### `IsLargeLevel.SplitPlaces.PowerResidueSymbols`

 Power residue symbols `b` of the `N`-units of the field of `U` at the split primes of `s`, with
what they say about the values `z (γ i)` at tame generators `γ i` of the cocycles `z = P.snd` of
the pairs `P` trivialised above `N` and infinity. 

### `IsLargeLevel.SplitPlaces.PowerResidueSymbols.rootPowHom_apply`

 `ζ ^ b y i = s.φ i r / r` whenever `r ^ m = y`. 

### `IsLargeLevel.SplitPlaces.PowerResidueSymbols.snd_eq_zero_of_forall_snd_eq_zero`

 A trivialised cocycle that vanishes at every `γ i` vanishes on `U`. 

### `IsLargeLevel.SplitPlaces.PowerResidueSymbols.sum_smul_eq_zero`

 Each `N`-unit `y` gives the relation `∑ b (g y) i • g⁻¹ z (γ i) = 0`, over `i` and
  `g ∈ G / U`. 

### `IsLargeLevel.SplitPlaces.PowerResidueSymbols.exists_mem_trivialisedCocycles`

 Over a totally complex field of `U`, a solution `f` of the relations gives, for each `a`, a
  trivialised cocycle with `z (γ i) = ∑ g, g (f (i, g) • a)`. 

### `IsLargeLevel.SplitPlaces.exists_powerResidueSymbols`

 Power residue reciprocity at split primes. Let `U` act trivially on the `ℤ/m`-module `V`, and
let `γ i` be tame generators of inertia at `s.valuationSubring i`. Then some power residue symbols
`b` have the properties of `New.IsLargeLevel.SplitPlaces.PowerResidueSymbols`. Cosets act on `V`
through their representatives `out`. The proof is by Kummer theory (`New.exists_kummer_chars`) and
Artin's law.

The Greenberg–Wiles bounds on cocycle counts in this development use this statement in place of
Poitou–Tate duality. 

### `IsLargeLevel.SplitPlaces.power_residue_reciprocity`

 `New.IsLargeLevel.SplitPlaces.exists_powerResidueSymbols` as one conjunction: its clauses
(a)–(d) are the four fields of `New.IsLargeLevel.SplitPlaces.PowerResidueSymbols`, in order. Here
`s.φ i` is a Frobenius element in `U` at a place over the `i`-th split prime. A pair `P` is a map
`f` on the places of `Ω` above `N` and infinity together with a continuous `z = P.snd` vanishing on
`I`, with `g f(x) = f(g x) + z g`.

Clauses (c) and (d) are an explicit substitute for the Poitou–Tate duality behind the
Greenberg–Wiles formula, for modules fixed by `U` at auxiliary split primes, pairing trivialised
cocycles with `N`-units by power residue symbols. 
