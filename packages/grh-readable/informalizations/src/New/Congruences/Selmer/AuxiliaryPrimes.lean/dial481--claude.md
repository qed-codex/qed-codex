---
{
  "module": "src/New/Congruences/Selmer/AuxiliaryPrimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/AuxiliaryPrimes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/AuxiliaryPrimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Auxiliary primes, anticyclotomic characters, slopes and ties

The setting is a CM field `E` and anticyclotomic characters of `Gal(Ω/E)` with values in `ℤ/q`. The
file defines data at auxiliary primes and sets of auxiliary primes. Chebotarev's theorem yields
auxiliary primes carrying such data.

## Main definitions and results

* `New.IsAuxPrimeDataAt`: a prime `P ≠ P̄` of norm `≡ 1 mod q` outside `T`, with a Frobenius
  element, a generator of tame inertia and a character to `ℤ/q` that comes from an idele class
  character of level `P` (`New.IsFromU1`).
* `New.IsAuxiliary`: finite sets of primes of prime norm, disjoint from their conjugates, with
  neither the primes nor their conjugates in `S`.
* `New.Selmer.exists_anticyclotomicChar_of_frob_fixes_roots`: a Galois character that sends the tame
  generator above a prime `P` to the generator `1 ∈ ℤ/q` and comes from an idele class character of
  level `P`.
* `New.Selmer.exists_isAuxPrimeDataAt`: an auxiliary prime `P` of `E` of prime norm with data
  `New.Selmer.AuxPrimeData`. These include a Frobenius element close to a given element of the
  normal closure of the inertia groups at the places of a finite set `R` outside `S ∪ S̄` and not
  above `ℓ`, and a character of `Gal(Ω/E)` to `ℤ/ℓ^N` that is trivial at this Frobenius element. The
  data satisfy `New.IsAuxPrimeDataAt` for every `T` contained in `S ∪ {v ∣ ℓ}`.
* `New.Selmer.IsTiedPrimes`: a set `J` of auxiliary primes with their data (place, tame generator
  `γ = tameGenerator`, Frobenius `φ = frob`, character, slopes) and a first prime `P₀`.
* `New.Selmer.tieRelations`: the relations `z γ = s • z φ` imposed on cocycles at the primes of `J`
  and their conjugates.

Notions from other files:
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.IsPlaceOver.tameGenerator`: a chosen generator of tame inertia at a place above `w`, as an
  element of the inertia group.
* `New.idOrConjInv`: `g` if `b` is true, and `g^{-c} = (conjGal g)⁻¹` if `b` is false.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` and `New.Congruences.Selmer.Descent` for related work.



## Auxiliary prime data and auxiliary sets of primes


### `Selmer.AuxPrimeData`

 The data at an auxiliary prime of a CM field `E` inside `Ω`, the algebraic closure of `ℚ`: a
place `place` of `Ω`, two elements `tameGenerator` and `frob` of `Gal(Ω/E)`, and a homomorphism
`character` from `Gal(Ω/E)` to `ℤ/q`. 

### `Selmer.AuxPrimeData.place`

 A place of `Ω`, meant to lie over the auxiliary prime. 

### `Selmer.AuxPrimeData.tameGenerator`

 The element meant to be the tame generator of inertia at `place`. 

### `Selmer.AuxPrimeData.frob`

 The element meant to be a Frobenius at `place`. 

### `Selmer.AuxPrimeData.character`

 The character to `ℤ / q` attached to the prime. 

### `IsAuxPrimeDataAt`

 For auxiliary prime data `l`: `P ≠ P̄` has norm `≡ 1 mod q` and lies outside `T`, `l.frob` is a
Frobenius and `l.tameGenerator` the chosen tame generator at the place `l.place` over `P`, and the
character `l.character` to `ℤ/q` comes from an idele class character of level `P` (`New.IsFromU1`
for `T` and `{P}`) and takes the value `1 ∈ ℤ/q` at `l.tameGenerator`. 

### `IsAuxPrimeDataAt.norm_modEq`

 The norm of `P` is congruent to `1` modulo `q`. 

### `IsAuxPrimeDataAt.isPlaceOver`

 The valuation subring `l.place` of `Ω` lies over `P`. 

### `IsAuxPrimeDataAt.isFrob`

 `l.frob` is an arithmetic Frobenius at `l.place`: it stabilises `l.place` and acts on residues
  as the power `P.q`. 

### `IsAuxPrimeDataAt.notMem`

 The prime `P` does not lie in `T`. 

### `IsAuxPrimeDataAt.star_ne`

 The prime `P` is not its own conjugate. 

### `IsAuxPrimeDataAt.tame_gen`

 `l.tameGenerator` lies in the inertia group of `l.place`, `l.character` sends it to
  `1 ∈ ℤ/q`, and it is the chosen generator of tame inertia at `l.place`. 

### `IsAuxiliary`

 A finite set `I` of places is auxiliary for `S` if every place of `I` has prime norm, neither it
nor its conjugate lies in `S`, and its conjugate lies outside `I`. 


## An anticyclotomic character ramified at a new prime with prescribed Frobenius

`P` comes from Chebotarev's theorem so that, for a suitable finite set `T` of places, all `T`-units
are `ℓ^N`-th powers modulo `P`. The discrete logarithm at `P` then descends to idele classes.


### `New.Selmer.exists_discreteLog`

 A discrete logarithm at `P`: let `P.q = 1 + q * k` be prime and let the residue of the local
unit `u` generate the units of the residue field. Then some character of `E_Pˣ` to `ℤ/q` sends `u`
to the generator `1` and is trivial on every `t` with `t ≡ 1` or `t ^ k ≡ 1` modulo `P`. 

### `New.Selmer.valuation_pow_sub_one_lt_one_of_isFrob`

 Let `σ` be a Frobenius at a place above `P`, with `P.q = 1 + n * k`. If `σ` fixes an `n`-th root
of a `T`-unit `u`, where `P ∉ T`, then `u ^ k ≡ 1` modulo `P`. 

### `New.Selmer.exists_ideleClassChar_of_local`

 Let the principal ideles and the `T`-ideles (those that are units off `T`) generate all finite
ideles. A continuous character `lg` of `E_Pˣ` that kills the `T`-units extends to a continuous
character of the idele classes which on `T`-ideles is `lg` of the component at `P`. 

### `New.Selmer.exists_anticyclotomicChar_of_frob_fixes_roots`

 Let `E` be a CM field, `Ω` the algebraic closure of `ℚ` containing it, and `T` a set of finite
places such that the ideles that are units off `T` (the `T`-ideles) and the principal ideles
generate all finite ideles. Let `P ∉ T`, `P ≠ P̄`, have prime norm `1 + q * k`, and let a Frobenius
`σ` at a place `A` over `P` fix a `q`-th root of each element of a finite set `s` that generates the
`T`-units. Then there is a continuous character `χ` of `Gal(Ω/E)` with values in `ℤ/q` that takes
the value `1` at `hA.tameGenerator`, the generator of tame inertia at `A` fixed in
`New.IsPlaceOver.tameGenerator`. It satisfies `χ (Art x) = θ (x / x̄)` for the Artin map `Art` and a
character `θ` of the finite ideles that is trivial on `Eˣ` and on the `T`-ideles congruent to `1` at
`P`. 

### `New.Selmer.mem_ker_inf_stabilizer_of_mem_normalClosure`

 Let `q` be a unit at all places off `T`, let the places of `R` lie off `T`, and let `y x` be a
`q`-th root of `x`. Then an element of the normal closure of the inertia groups above `R` fixes the
`q`-th roots of unity and the roots `y u` of each element `u` of a set `s` of `T`-units. 

### `New.Selmer.exists_isAuxPrimeDataAt`

 Chebotarev gives auxiliary primes with prescribed Frobenius. Let `E` be a CM field in `Ω`, the
algebraic closure of `ℚ`, `ℓ` a prime (`New.ThePrime`), `S` and `R` finite sets of places of `E`,
and `W` a neighbourhood of an element `z` of the normal closure of the inertia groups at the places
of `R` that are outside `S ∪ S̄` and not above `ℓ`. Then there are a prime `P ∉ R ∪ R̄` of prime
norm and data `auxData`, made of a place `place` of `Ω`, elements `tameGenerator` and `frob` of
`Gal(Ω/E)` and a `character` to `ℤ / ℓ ^ N`, such that (a) `frob ∈ W` and `character` is trivial at
`frob`, and (b) `New.IsAuxPrimeDataAt` holds for every `T ⊆ S ∪ {v ∣ ℓ}`. 


## Auxiliary primes with slopes, and ties

Statements about a prime and its conjugate are indexed by `b : Bool` through `New.idOrConjInv`.

* `New.Selmer.pointChar`: the character `g ↦ ∏ j, y j ^ h j g` for `q`-th roots of unity `y j`.


### `unionWithConj`

 The set `S ∪ J ∪ J̄` of places, for finite sets `S` and `J`. 

### `pointChar`

 The character `g ↦ ∏ j, y j ^ h j g` of `G`, for characters `h j` to `ℤ/q` and `q`-th roots of
unity `y j`. 

### `reduceModPow`

 The reduction of the matrix representation `ρ` modulo `l ^ M`. 

### `IsTiedPrimes`

 A set of tied primes for the finite set `S₀` of places records the auxiliary primes chosen so
far: a set `J` that consists of a first prime `P₀`, whose Frobenius element lies in `W`, and later
primes. Each prime `v ∈ J` carries the data `(x v).1` (place, Frobenius element, tame generator,
character to `ℤ / ℓ ^ N`) and a slope `(x v).2 i` for each datum `i`. One set `J` serves all data:
the primes chosen for datum `i` are those with a nonzero slope, and there the Frobenius elements
satisfy the given condition `U i` (typically: they act trivially on the datum `i`). 

### `IsTiedPrimes.auxiliary`

 `J` is a set of auxiliary primes for `S₀`. 

### `IsTiedPrimes.first_mem`

 The first prime `P₀` lies in `J`. 

### `IsTiedPrimes.isAuxPrimeDataAt`

 At each `v ∈ J` the first component is a place over `v`, a Frobenius, the tame generator
  and the character attached to them. 

### `IsTiedPrimes.char_frob_eq_ite`

 For `v ≠ P₀` in `J`, the Frobenius at `v` has value `1` in `ℤ / ℓ ^ N` under the character of
  `P₀` and value `0` under the characters of the other primes of `J`. 

### `IsTiedPrimes.first_frob_mem`

 The Frobenius element of the first prime lies in `W`. 

### `IsTiedPrimes.first_slope`

 The first prime has slope `0` for every datum. 

### `IsTiedPrimes.notMem_placesDividing`

 The primes of `S₀` and the later primes do not divide the norm of the first prime, so that the
  Greenberg–Wiles count can choose its extra primes away from the first prime. 

### `IsTiedPrimes.frob_of_slope_ne_zero`

 Where the slope for datum `i` at `v` is not zero, `U i` holds at `φ_v = (x v).1.frob` and at
  `φ_v^{-c}`. 

### `IsTiedPrimes.apply_idOrConjInv_of_slope_ne_zero`

 If a tied prime has a nonzero slope, its Frobenius `φ_v` and the inverse `φ_v^{-c}` of its
conjugate satisfy the chosen condition. 

### `tieRelations`

 The ties `z(γ_w) = s • z(φ_w)` of datum `i`, for `v ∈ J` with slope `s = (x v).2 i` and
`w = v, v̄`, as formal combinations of group elements with matrix coefficients, where
`γ_v = (x v).1.tameGenerator` and `φ_v = (x v).1.frob`; at `v̄` the elements are `γ_v^{-c}` and
`φ_v^{-c}`. 

### `idOrConjInv_mem_inertiaAbove`

 If `τ` is inertial at a place over `P` and `S` contains `P` and its conjugate, then `τ` and
`τ^{-c}` (the two values of `New.idOrConjInv b τ`) lie in inertia groups above `S`. 
