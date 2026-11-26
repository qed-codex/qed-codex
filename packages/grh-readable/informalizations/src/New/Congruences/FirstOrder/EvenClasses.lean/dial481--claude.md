---
{
  "module": "src/New/Congruences/FirstOrder/EvenClasses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/EvenClasses.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/EvenClasses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Even classes and auxiliary places for Selmer cocycles

The file concerns cocycles of `Gal(Ω/E)` in the twists `O/ℓ^ν(-e)`. Here `Ω` is the algebraic
closure of `ℚ`, `E ⊆ Ω` is a CM field containing the `5040`-th roots of unity
(`New.CMFieldWithRoot5040`), and `O` is the ring of integers of a finite Galois extension of `ℚ_ℓ`
(`New.CoeffRing`). Further, `cyc` is the `ℓ`-adic cyclotomic character (`New.cyclotomicChar`),
`cyc mod N` is the one modulo `N` (`New.cyclotomicCharMod`), and `g^c = conjGal g` is the conjugate
of `g` by the chosen complex conjugation. The reciprocity law for even classes is in
`New.Congruences.FirstOrder.KummerMaps`.

## Main definitions and results

* `New.Selmer.evenClasses`: the even classes, that is the cocycles unramified off `ℓ` and a set of
  places and its conjugate that are invariant under `g ↦ g^c` and zero on the kernel of
  `cyclotomicChar` in the decomposition groups above `ℓ`.
* `New.Selmer.IsTameGeneratorFamily`: places `w j` off `ℓ`, tame generators `τ j`, and `φ j` fixing
  `μ_{ℓ^ν}`; `New.Selmer.withConjInv f` doubles a family by the `(f j ^ c)⁻¹`, which serve the
  conjugate places.
* `New.Selmer.IsPrimeTriangle`: an even class that kills the earlier elements `τ i`, and `φ i` of
  the same exponent, is killed at `τ j` up to a bounded power of `ℓ`.
* `New.Selmer.IsAuxTwist`: an auxiliary set of places with an anticyclotomic character whose values
  at tame generators are not too close to `1`.
* `New.Selmer.IsTameGeneratorFamily.mem_selmerModule_of_tame_eq_zero`: killing the doubled tame
  generators removes the ramification at the places `w j` and their conjugates.
* `New.Selmer.eq_zero_of_forall_mem_Z1_of_mem_evenClasses`: to show that an element `b` of
  `O / ℓ ^ ν` vanishes, given an even class `c`, it is enough to test `b` with the additive maps `u`
  to `ℤ/ℓ ^ ν` for which `u ∘ c` is a cocycle of the twist `-e`; in fact every `u` has this
  property.

Notions from other files:
* `New.selmerModule ρ S L B`: the locally constant cocycles of `ρ` with values in `B` that
  are unramified outside `S` and satisfy the relations `L`.
* `New.Selmer.tateTwist ℓ E O e`: the character `cyclotomicInv ℓ E O ^ e` as `1 × 1` matrices, where
  `cyclotomicInv` is `cyc⁻¹` with values in `O`.
* `New.Selmer.shaLocalSet ℓ E 1`: the elements of decomposition groups above `ℓ` with `cyc = 1`.
* `New.Z1` and `New.charRep`: the continuous cocycles of a representation, and the representation
  given by scalars through a character.


### `evenClasses`

 The even classes of exponent `e` for a set `S` of places: the locally constant cocycles
`c : Gal(Ω/E) → O/ℓ^ν(-e)` (values indexed by `Unit`) that are unramified outside the places above
`ℓ`, `S` and its conjugate, satisfy `c (conjGal g) = c g` (where `conjGal g` is the conjugate of `g`
by complex conjugation), and vanish on the elements with trivial cyclotomic character of the
decomposition groups above `ℓ` (`shaLocalSet ℓ E 1`). 

### `IsTameGeneratorFamily`

 The `τ j` are tame generators at the places `w j` of `E`, with auxiliary elements `φ j`: each
`w j` is a finite place not above `ℓ`, `φ j` fixes the `ℓ ^ ν`-th roots of unity, and `τ j` is the
chosen generator of tame inertia at some place of the algebraic closure `Ω` over `w j`. 

### `withConjInv`

 The family indexed by two copies `J × Bool` of `J`, with value `τ j` at `(j, true)` and
`(conjGal (τ j))⁻¹` at `(j, false)`; see `withConjInv_true` and `withConjInv_false`. 

### `IsPrimeTriangle`

 A triangle of primes: places `w j` off `ℓ`, with elements `τ j` and `φ j`, indexed by a finite
linear order `J`. The place `w j` serves the exponent `ty j`, where `0 < ty j < t` and `ty` is
monotone, and `a` is a fixed element of `Gal(Ω/E)`. In the application `a` generates this group
modulo the kernel of the cyclotomic character, and `φ j` is a Frobenius element at the place of the
tame generator `τ j`.
* `exists_test_points`: a finite set `s` of elements with trivial cyclotomic character, with
`(#J + #s + 1) * h ≤ c`, detects together with `a` the cocycles unramified off `ℓ`; for each
exponent and each `g` in `s`, the even classes unramified off `ℓ` take at some `φ j` of that
exponent twice their value at `g`.
* `prod_dvd`: the element `a` separates the powers `u ^ e`, `e < t`, of
`u = cyclotomicChar Ω ℓ a⁻¹`, up to `ℓ ^ h`. 

### `IsPrimeTriangle.isTameGeneratorFamily`

 The `w j` are places off `ℓ` with tame generators `τ j`, and the `φ j` fix the `ℓ ^ ν`-th
  roots of unity (`New.Selmer.IsTameGeneratorFamily`). 

### `IsPrimeTriangle.exists_test_points`

 There is a finite set `s` of test points with trivial cyclotomic character and
  `(#J + (#s + 1)) h ≤ c`. A locally constant cocycle in `O/ℓ^ν(-e)` unramified off `ℓ` that
  vanishes at `a` and on `s` is zero, for all `O` and `e`. For each exponent `e` and each `g` in `s`
  there is a `j` of exponent `e` with `z (φ j) = 2 z(g)` for all even classes `z` unramified off
  `ℓ`. 

### `IsPrimeTriangle.prod_dvd`

 For `e < t` and `u = cyclotomicChar Ω ℓ a⁻¹`, the product in `ℤ_[ℓ]` of `u ^ e - u ^ k` over
  `k < t`, `k ≠ e`, divides `ℓ ^ h`. 

### `IsPrimeTriangle.pow_smul_eq_zero`

 If an even class `z` of exponent `ty j` for the places `w` kills `τ i` for all `i < j`, and
  `φ i` for the `i < j` with the same exponent as `j`, then `ℓ ^ h` kills `z (τ j)`. 

### `IsPrimeTriangle.four_mul_sq_dvd`

 For `0 < e < t`, the element `4 (cyclotomicInv ℓ E O a ^ e - 1)²` of `O` divides `ℓ ^ h`. 

### `IsAuxTwist`

 The set of places `Q` is auxiliary for `S` (`New.IsAuxiliary`: its places have prime norm, they
and their conjugates are off `S`, and their conjugates are off `Q`), no place of `Q` lies above `ℓ`,
and `ψ` is anticyclotomic of modulus `Q` (`New.IsFromU1`: it comes from the norm-one torus).
Moreover, for some choice of tame generators `σ P` at places over the `P` in `Q`, the sum of the
`ℓ`-adic valuations of `ψ (σ P) - 1` is at most `c`. 

### `four_dvd_cyclotomicChar_sub_one`

 Let `ℓ` be a prime and `E` a CM field, embedded in the algebraic closure `Ω` of `ℚ`, that
contains the `5040`-th roots of unity. The value of the `ℓ`-adic cyclotomic character at any element
`a` of `Gal(Ω/E)` is congruent to `1` modulo `4` in `ℤ_[ℓ]`. 

### `tateTwist_eq_one_of_cyclotomicChar_eq_one`

 The Tate twist `cyc^(-e)` with values in a `ℤ_[ℓ]`-algebra `Λ` is trivial on the kernel of the
`ℓ`-adic cyclotomic character `cyc`. 

### `IsTameGeneratorFamily.cyclotomicInv_withConjInv_eq_one_and_dvd`

 Let the places `w j` of `E` be off `ℓ`, each `τ j` a generator of tame inertia at `w j`, and
each `φ j` an element fixing the `ℓ ^ ν`-th roots of unity (`hw`). Then the inverse `ℓ`-adic
cyclotomic character with values in `O` is trivial on `withConjInv τ`, and all its powers are
congruent to `1` modulo `ℓ ^ ν` on `withConjInv φ`. 

### `IsTameGeneratorFamily.mem_selmerModule_of_tame_eq_zero`

 Killing tame generators removes ramification. Let `E` be a CM field in the algebraic closure `Ω`
of `ℚ`, let the places `w j` of `E` be off the prime `ℓ`, with generators `τ j` of tame inertia
(`hw`), and let the representation `ρ` over `Λ` be trivial on those elements of inertia groups off
`S` that have trivial `ℓ`-adic cyclotomic character. The Selmer module `selmerModule ρ T L B`
consists of the locally constant cocycles `c` of `ρ` with values in `B ^ n` that are unramified off
`T` and obey the linear relations `∑ g, r g • c g = 0` for `r` in `L`. Let `c` be such a cocycle
modulo `ℓ ^ e`, where `T` is contained in the union of `S`, the `w j` and their complex conjugates.
If `c` vanishes at the `τ j` and the `(conjGal (τ j))⁻¹` (`conjGal` is conjugation by complex
conjugation), then `c` is unramified off `S`, so it lies in the Selmer module of `S` and `L`. 

 ## Detecting even classes modulo ℓ^ν 

### `New.Selmer.eq_zero_of_forall_mem_Z1_of_mem_evenClasses`

 Let `c` be an even class of exponent `e`: a locally constant cocycle of `Gal(Ω/E)` in
`O / ℓ ^ ν` for the `-e`-th power of the cyclotomic character, unramified outside `ℓ`, `S` and their
conjugates, invariant under conjugation by complex conjugation, and zero on the kernel of the
cyclotomic character in the decomposition groups above `ℓ`. If an element `b` of `O / ℓ ^ ν` is
killed by every additive map `u` to `ℤ/ℓ ^ ν` for which `u ∘ c` is a continuous cocycle (`New.Z1`)
for the `-e`-th power of the cyclotomic character modulo `ℓ ^ ν`, then `b = 0`. 
