---
{
  "module": "src/Lib/ClassField/Places/ValuationSubrings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ValuationSubrings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ValuationSubrings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Valuation subrings over primes, primes from p-adic embeddings, and the efg formula

Places of an extension `Ω` of a number field `K` are treated as valuation subrings of `Ω` lying over
primes of `𝓞 K`. An embedding `σ` of a number field `E` into an ultrametric normed field over `ℚ_p`
induces a prime of `E` above `p` and extends to the finite adeles of `E`. The formula
`g * (e * f) = [L : K]` is restated in terms of finite places.

## Main definitions and results

* `New.IsPlaceOver.isEquiv`, `New.IsPlaceOver.unique`: `A` induces the `v`-adic valuation up to
  equivalence, and determines `v`.
* `New.FinPlace.isPlaceOver_placeOver`, `New.exists_isPlaceOver_of_val_ne_one`: every `v` has a
  valuation subring of `New.Ω` over it; for `Ω/K` algebraic, every `A` whose valuation is not `1` at
  some nonzero element lies over some `v`.
* `New.finite_ramified`: almost all inertia groups lie in a given open subgroup of `Γ`.
* `New.IsPlaceOver.exists_smul`: the Galois group `Γ` is transitive on the `A` over `v`.
* `New.placeOfEmb`: the prime induced by `σ`; it consists of the integers with `‖σ x‖ < 1`
  (`New.mem_placeOfEmb`) and contains `p` (`New.natCast_mem_placeOfEmb`).
* `New.exists_placeOfEmb_extension`, `New.placeOfEmbExtension`: `σ` extends continuously to the
  completion of `E` at that prime.
* `New.adeleExtension`: the resulting ring homomorphism on finite adeles; it is continuous, extends
  `σ` and sends integral adeles to elements of norm at most one (`New.norm_adeleExtension_le_one`).

Notions from other files:
* `New.FinPlace K`: a nonzero prime of `𝓞 K`; `v.q` is its absolute norm; a `New.ClosurePlace` is a
  valuation subring of `New.Ω`, the algebraic closure of `ℚ`.
* `A x`, for a valuation subring `A` of `Ω`: the value `A.valuation x`; for `x : K`,
  `valuationVia K A x` is `A.valuation (algebraMap K Ω x)`.
* `New.IsProGalois Γ K Ω`: `Γ` is a profinite Galois group of `Ω / K` with open stabilisers.
* `New.inertiaGroup Γ A`: the `σ` in `Γ` that stabilise `A` and act trivially modulo its maximal
  ideal.
* `New.PadicField`: a normed field that is a normed algebra over `ℚ_p`, not necessarily complete.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.



## Places of extensions of number fields as valuation subrings over primes

Places of an extension `Ω` of a number field `K` are handled as valuation subrings `A` of `Ω`.
`New.IsPlaceOver A v` says that an integer of `K` is in the maximal ideal of `A` exactly when it
lies in the prime `v`. The tool is the centre `New.Cohomology.centrePrime K A`, a prime ideal of
`𝓞 K`.


 ### The centre of a valuation subring 

### `algebraMap_ringOfIntegers_mem`

 The image in `Ω` of an integer of `K` lies in every valuation subring `A` of `Ω`: it is
integral over `ℤ`, and a valuation subring is integrally closed. 

### `centrePrime`

 The centre of the valuation subring `A` on `K`: the ideal of those integers of `K` whose image
in `Ω` lies in the maximal ideal of `A`. 

### `instance {k : Type*} [Field k] [Algebra K k] [Algebra k Ω] [IsScalarTower K k Ω] : (A.valuation.comap <| algebraMap K _).HasExtension (A.valuation.comap (algebraMap k Ω))`

 For a tower `K ⊆ k ⊆ Ω`, the valuation of `A` on `k` extends the one on `K` (here
`algebraMap K _` is the map from `K` to `Ω`). 

### `isUniformiser_iff_of_isEquiv`

 If `A` induces on `K` a valuation equivalent to `w`, and `w` takes the value `exp (-1)`, then
the uniformisers for `A` in `K` (the `π` with `valuationVia K A x < 1 ↔ valuationVia K A
x ≤ valuationVia K A π` for all `x : K`) are the elements with `w π = exp (-1)`. 

 ### Properties of a valuation subring over a prime 

### `of_le_centrePrime`

 As `v` is maximal, `A` lies over `v` as soon as its centre contains `v`. 

### `isPlaceOver_below`

 If `A` lies over a prime `u` of `L`, it lies over the prime of `K` below `u`. 

### `centrePrime_liesOver`

 If `A` lies over `v`, then its centre in `𝓞 Ω` lies over the prime `v` of `𝓞 K`. 

### `isEquiv`

 If `A` lies over `v`, its valuation restricted to `K` is equivalent to the `v`-adic one. 

### `unique`

 A valuation subring lies over at most one prime of `K`. 

### `isUniformiser_iff`

 If `A` lies over `v`, its uniformisers in `K` are the elements of `v`-adic valuation
`exp (-1)`. 

### `smul`

 An element `g` of `Γ` whose action commutes with `K` carries a place over `v` to a place over
`v`. 

### `FinPlace.isPlaceOver_placeOver`

 The chosen place `placeOver v` of `New.Ω`, the algebraic closure of `ℚ`, lies over `v`. 

### `prime_span_natCast_rat`

 For a prime number `p`, the ideal `(p)` of `𝓞 ℚ` is prime, as its norm `p` is prime. 

### `ratPlace`

 The place of `ℚ` at a prime number `p`: the prime ideal `(p)` of `𝓞 ℚ`. 

### `valuation_eq_one_of_ne_ratPlace`

 `p` is a unit at every place of `ℚ` other than the place at `p`. 

### `valuation_ratPlace`

 `p` is a uniformiser at the place of `ℚ` at `p`. 

### `isPlaceOver_ratPlace_of_valuation_lt_one`

 Every `New.ClosurePlace` whose valuation at `p` is less than `1` lies over the place of `ℚ`
at `p`. 

### `exists_rat_place_of_prime`

 The place of `ℚ` attached to a prime number `p`: (a) it has norm `p`, and `p` is a unit at every
other place; (b) `p` is a uniformiser there; (c) every `New.ClosurePlace` whose valuation at `p` is
less than `1` lies over it. 

### `exists_isPlaceOver_of_val_ne_one`

 For `Ω / K` algebraic, a valuation subring `A` whose valuation is not `1` at some nonzero `x`
lies over a prime of `K`. 

 ### The action of the Galois group on places 

### `finite_ramified`

 Only finitely many places ramify in a finite extension: for an open subgroup `U` of `Γ`, for
all but finitely many primes `v` of `K` the inertia group of every `A` over `v` lies in `U`. Here
`Γ` is a profinite Galois group of the Galois extension `Ω / K` (`New.IsProGalois`). 

### `IsPlaceOver.exists_above`

 If `A` lies over the prime `v` of `K` (the section hypothesis `h : IsPlaceOver A v`), it lies
over some prime `u` of `L` above `v`, for `Ω / L` algebraic. 

### `IsPlaceOver.exists_smul`

 The Galois group acts transitively on the places over `v`: if `A` lies over `v` (the section
hypothesis `h : IsPlaceOver A v`) and so does `A'`, then `g • A = A'` for some `g` in `Γ`. Here
`Γ` is a profinite Galois group of `Ω / K` (`G : IsProGalois Γ K Ω`) and `Ω / K` is algebraic. 


## The prime induced by a p-adic embedding and its extension to finite adeles

Conventions: `New.FinPlace E` is the type of nonzero primes of `𝓞 E`, `New.LocField w` the
completion at `w` with valuation `v`, and `New.Ô E` the ring of integral finite adeles. The field
`F` is a normed field over `ℚ_p` (`New.PadicField F p`) whose norm is ultrametric.


 ### The prime induced by an embedding 

### `placeOfEmb`

 The prime of `E` induced by an embedding `σ : E →+* F` into an ultrametric normed field over
`ℚ_p`: the centre on the integers of `E` of the valuation ring `{x : E | ‖σ x‖ ≤ 1}`. An integer `x`
of `E` lies in it exactly when `‖σ x‖ < 1` (`New.mem_placeOfEmb`). 

### `isEquiv_placeOfEmb`

 The valuation `‖σ ·‖` on `E` is equivalent to the valuation of `E` at the prime
`New.placeOfEmb σ`. 

### `complexToCp`

 The ring homomorphism from `ℂ` to `ℂ_p` obtained by composing an isomorphism `ι` from `ℂ` onto
the algebraic closure of `ℚ_p` with the inclusion into `ℂ_p`. 

### `inducedPrime`

 The prime of `E` above `p` induced by the complex embedding `σ` followed by the isomorphism
`ιℓ` from `ℂ` to the algebraic closure of `ℚ_p` that `[PadicIso p]` fixes. 

### `natCast_mem_placeOfEmb`

 The prime `New.placeOfEmb σ` contains `p`, as `‖p‖ < 1` in `F`. 

### `instance : FiniteDimensional ℚ_[p] (adjoin ℚ_[p] (Set.range σ))`

 The subfield `ℚ_p(σ E)` of `F` generated over `ℚ_p` by the image of `σ` is finite over `ℚ_p`. 

 ### Extension to the completion and to finite adeles 

### `exists_placeOfEmb_extension`

 Let `F` be an ultrametric normed field of characteristic 0 that is a normed `ℚ_p`-algebra, not
necessarily complete. Let `σ` be an embedding of the number field `E` into `F`, and let
`New.placeOfEmb σ` be the prime of `E` made of the integers `x` with `‖σ x‖ < 1`. Then `σ` extends
to a continuous ring homomorphism `φ` on the completion of `E` at that prime. Its values lie in the
subfield `ℚ_p(σ E)` of `F`, and `‖φ x‖ ≤ ‖φ y‖` holds exactly when `v x ≤ v y` for the valuation
`Valued.v` of the completion. The chosen extension is `New.placeOfEmbExtension σ`. 

### `placeOfEmbExtension`

 The extension of `σ` to the completion of `E` at the prime `New.placeOfEmb σ`, chosen by
`New.exists_placeOfEmb_extension`: continuous, extending `σ`, with values in `ℚ_p(σ E)`. 

### `placeOfEmbExtension_mem_adjoin`

 The extension of `σ` to the completion takes values in the subfield `ℚ_p(σ E)` of `F`. 

### `valuation_comap_placeOfEmbExtension_isEquiv`

 The norm valuation of `F` pulled back along `New.placeOfEmbExtension σ` is equivalent to the
valuation `Valued.v` of the completion at `New.placeOfEmb σ`. 

### `adeleExtension`

 The extension of `σ` to the finite adeles of `E`: take the component at the prime
`New.placeOfEmb σ`, then apply `New.placeOfEmbExtension σ`. 

### `norm_adeleExtension_eq_iff`

 Two finite adeles `x` and `y` have images of the same norm under the extension of `σ`
exactly when their components at the prime `New.placeOfEmb σ` have the same valuation. 

### `norm_adeleExtension_le_one`

 The extension of `σ` sends every finite adele `x` that is integral at all primes to an element
of norm at most one. 

 ### Compatibility with complex conjugation 

### `placeOfEmb_comp_star`

 For a CM field `E`, the prime induced by `σ` composed with complex conjugation is the complex
conjugate of the prime induced by `σ`. 

### `adeleExtension_star`

 For a CM field `E`, applying the extension of `σ` to the complex conjugate of a finite adele
gives the extension of `σ` composed with complex conjugation. 

### `weightEmbedding`

 The embedding `x ↦ ι (Φ v (conj x))` of `E` into `F`, for `ι : ℂ →+* F` and an infinite
place `v` with chosen complex embedding `Φ v`. 


## The formula efg = n for Galois extensions of number fields

`New.FinPlace.ncard_mul_ramificationIdx_mul_inertiaDeg` restates Mathlib's formula
`g * (e * f) = [L : K]` for a finite place `w` of a Galois extension `L / K` of number fields,
counting places (`New.FinPlace`) over `w.below K` instead of prime ideals.


### `instance : w.asIdeal.LiesOver (w.below K).asIdeal`

 The place `w` of `L` lies over the place of `K` below it. 

### `New.FinPlace.ncard_mul_ramificationIdx_mul_inertiaDeg`

 For a Galois extension `L / K` of number fields and a finite place `w` of `L`: the number of
places of `L` over the place of `K` below `w`, times the ramification index and the inertia
degree of `w`, is `[L : K]`. 
