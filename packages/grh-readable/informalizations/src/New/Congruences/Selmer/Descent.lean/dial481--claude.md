---
{
  "module": "src/New/Congruences/Selmer/Descent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Descent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Descent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The descent

Primes are added as long as this makes the tied Selmer groups modulo `ϖ ^ k`, `1 ≤ k ≤ e`, shorter.
When no prime does, reciprocity bounds the dual Selmer group at the level given by the exponent of
the tied group, and the comparison of the lengths of the two groups gives the bound for the tied
group. All data are treated at once: a prime that is added for one datum has slope `0` for the
others, which means that their classes stay unramified there. Lengths count composition factors, so
that each step lowers the sum of the lengths by at least `1`.

* `New.Selmer.tilting`: off few residues of `a`, the kernel of `a • evγ - evφ` is short.
* `New.Selmer.exists_slope_totalTiedLength_lt`: one step of the descent.
* `New.Selmer.SelmerDatum.length_tiedSelmer_pow_le`: the bound when no step is possible.
* `New.Selmer.exists_isTiedPrimes_card_le_and_length_le`: boundedly many new primes with slopes make
  the tied Selmer groups of finitely many data short.

Throughout, `E` is a number field with a chosen embedding into the algebraic closure `Ω` of `ℚ`
(`New.EmbeddedNumberField`). From the first prime on, `E` is a CM field, `ℓ` is a prime
(`New.ThePrime`) and `S₀` is a finite set of finite places of `E`; for the Selmer data, `O` is the
integer ring of a finite extension of `ℚ_ℓ` (`New.PadicIntegerRing`).

Notions from other files:
* `New.selmerModule ρ S K B`: locally constant cocycles for `ρ` with values in `Bⁿ`, unramified
  outside `S` and obeying the linear relations `K`; `New.QuotSpan a` is the ring `O / a`.
* `New.Selmer.SelmerDatum ℓ S₀ g₀ O n`: a Galois lattice `T = Oⁿ` with local conditions, unramified
  outside a set `T.places ⊆ S₀`, on which `det(g - 1) ≠ 0` for `g = g₀, g₀^{-c}`.
  `T.tiedSelmer R J x i a` is its Selmer group modulo `a`, unramified outside `T.places ∪ R ∪ R̄`,
  with the ties `z(γ) = s • z(φ)` at the primes of `J` and their conjugates, `s` the slope of datum
  `i`. It is `Sel(J)` for `R = J` and `Sel^𝔮(J)` for `R = J ∪ {𝔮}`. The global term `T.globalTerm`
  is the supremum over `a ≠ 0` of the lengths of `Hom_G(T / a, (T / a)^{*c})`, and `T.placesTerm` is
  the sum `lt_S(T)` of the local terms at the places of `T.places` prime to `ℓ`.
* `New.Selmer.IsTiedPrimes ℓ S₀ V W N P₀ J x`: a set `J` of primes outside `S₀ ∪ S̄₀` with places,
  Frobenius elements `φ`, tame generators `γ`, characters to `ℤ / ℓ ^ N` and slopes, all recorded in
  `x`. The first prime `P₀ ∈ J` has slope `0` and its Frobenius element in the set `W`, and `V i`
  holds at `φ` and `φ^{-c}` where the slope for datum `i` is not zero.
* `New.Selmer.IsNewAuxiliaryPrime ℓ V S₀ J P₀ x i P l`: the prime `P` with data `l` may be added to
  `J` with any slope for datum `i`. In particular `P` and `P̄` lie outside `S₀ ∪ J`, and `V i` holds
  at `φ = l.frob` and `φ^{-c}`.
* `New.Selmer.evalConjPair g`: the evaluation `ev_g` of a function at `g` and at `g^{-c}`, the
  inverse of the complex conjugate of `g`.

## Relation to the literature

Lowering Selmer groups mod ℓ^n by new local conditions at Chebotarev primes with trivial Frobenius
is known in the literature. Related work: Fakhruddin–Khare–Patrikis, Relative deformation theory,
relative Selmer groups, and lifting irreducible Galois representations, 2021; Mazur–Rubin,
Diophantine stability, 2018; Darmon–Diamond–Taylor, Fermat's Last Theorem, 1995.


 ### Tilting 

### `tilting`

 Tilting. Let `evγ, evφ` be linear maps to `(O / I) ^ m`, of finite length, and let `C` be a
submodule of their source. For `a` outside at most `card m` residue classes, the kernel of
`a • evγ - evφ` on `C` is no longer than the part of the kernel of `evγ` on `C` that `evφ` maps into
`evγ C`. 

 ### Levels and the exponent of a Selmer group 

### `exists_injective_quotSpan_onto_torsion`

 Let `b = a c` with `a, c ≠ 0`. Multiplication by `c` identifies `O / a` with the `a`-torsion of
`O / b`. 

### `isUnit_of_pow_smul_ne_zero`

 Let `ϖ` be a uniformizer of `O`. An element of `O / ϖ ^ (i + 1)` that `ϖ ^ i` does not kill is a
unit. 

### `exists_length_selmerModule_pow_le`

 Passage to the exponent. Let `E` be a number field embedded in the algebraic closure `Ω` of `ℚ`,
and let `ϖ` be a uniformizer of `O`. The Selmer module modulo `ϖ ^ k` consists of the locally
constant cocycles `z` for `ρ` with values in `(O / ϖ ^ k) ^ n` that are unramified outside `S` and
obey the relations `K`: for each finite family of matrices `f ∈ K` indexed by `Gal(Ω/E)`, the sum
`∑ g, f g • z g` is zero. For some `i ≤ k` this module is no longer than the module modulo `ϖ ^ i`,
and if `i ≠ 0` the latter has a member with a value with a unit coordinate, that is, a member of
order `ϖ ^ i`. 

 ### Room for slopes 

### `exists_unit_residue_notMem`

 In a local ring whose residue field has `q` elements, a set of fewer than `q - 1` residues
misses the residue of some unit. 

### `sum_lt_sum_of_ne_top`

 Strict monotonicity of finite sums in `ℕ∞`: if `f ≤ g` on `s`, the terms of `g` are finite and
`f b < g b` for some `b ∈ s`, then the sum of `f` is smaller than the sum of `g`. 

 ### The first prime 

### `exists_isTiedPrimes_singleton`

 Let `g₀` be inertial at a place of `S₀` prime to `ℓ`, and let `W` be a neighbourhood of `g₀`.
Then there is a prime `P₀` with data `l`, whose norm no prime of `S₀` divides, such that `{P₀}`,
with all slopes `0`, satisfies `IsTiedPrimes`. That is, `P₀` has prime norm, differs from its
complex conjugate `P̄₀`, both lie outside `S₀`, and the conditions on later primes are empty. The
condition on the norm lets the Greenberg–Wiles count keep its extra primes away from `P₀` and
`P̄₀`. 

 ### Adding a prime 

### `finite_tiedSelmer`

 Let `T` be a Selmer datum over `O`, the integer ring of a finite extension of `ℚ_ℓ`. A tied
Selmer group of `T` modulo a divisor `a` of `ℓ ^ M` is finite. 

### `selmerModule_inf_ker_le`

 Let `J` satisfy `IsTiedPrimes ℓ S₀ V W N P₀ J x`: its primes lie outside `S₀ ∪ S̄₀` and come
with a place, a Frobenius element, the tame generator `γ_v = (x v).1.tameGenerator`, a character to
`ℤ / ℓ ^ N` and slopes. Let `a ∣ ℓ ^ M`, let `R` be any finite set of places and `K` any set of
linear relations between the values of a function on `Gal(Ω/E)`. If a locally constant cocycle with
values in `(O / a) ^ n` satisfies the relations `K`, is unramified outside `T.places ∪ J ∪ J̄` and
vanishes at `γ_v` and `γ_v^{-c} = (conjGal γ_v)⁻¹` for all `v ∈ J \ R`, then it is unramified
outside `T.places ∪ R ∪ R̄`. 

### `tiedSelmer_le_of_slope_eq_zero`

 Slope `0` means unramified. Let `T` be a Selmer datum: a lattice `O ^ n` with Galois action
`T.ρ`, unramified outside `T.places`. The relations `T.classRelations` are its local conditions
above `ℓ` and vanishing at `T.γ`, a fixed inertia element acting by a scalar, which picks one
cocycle in each class. Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: `J` is a set of auxiliary primes
outside `S₀` with first prime `P₀`. For each `v ∈ J`, `x v` gives a tame generator `γ_v`, a
Frobenius element `φ_v`, a character to `ℤ / ℓ ^ N` and slopes `(x v).2 i`. Let `a ∣ ℓ ^ M`. The
group `T.tiedSelmer J J x i a` consists of the cocycles `z` modulo `a` that obey `T.classRelations`,
are unramified outside `T.places ∪ J ∪ J̄` (first `J`) and satisfy the ties
`z(γ_v) = slope • z(φ_v)` at the primes `v ∈ J` and their conjugates (second `J`). If the slopes
`(x v).2 i` of datum `i` are all `0`, so that the ties read `z(γ_v) = 0`, then these cocycles are
unramified outside `T.places`: they lie in `selmerModule T.ρ T.places T.classRelations (QuotSpan
a)`, the Selmer group without auxiliary primes. 

### `tiedSelmer_insert_inf_ker_le`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: `J` is a set of primes outside `S₀` with data and
slopes `x` to level `ℓ ^ N`, first prime `P₀` of slope `0` with Frobenius element in `W`, and `V j`
true at Frobenius elements where the slope for `j` is not zero. Let `P` with data `l` be a new
auxiliary prime for a datum `i`: it may be added to `J` with any slope for `i`. Let `a ∣ ℓ ^ M` and
`γ = l.tameGenerator`. Consider a cocycle modulo `a` with the local conditions of `T` and the ties
`z(γ_v) = slope • z(φ_v)` of datum `j` at `v ∈ J` and `v̄`, unramified outside
`T.places ∪ J ∪ J̄ ∪ {P, P̄}`. If it vanishes at `γ` and at `γ^{-c} = (conjGal γ)⁻¹`, then it is
unramified at `P` and `P̄`, hence lies in the tied Selmer group of `J`. 

### `tiedSelmer_update_le`

 Add a prime `𝔮 = P` outside `J`, with Frobenius element `l.frob`, tame generator
`l.tameGenerator` and slopes `s`. The tied Selmer group `Sel(J)` of the Selmer datum `T` modulo
`a` for the index `j` consists of the cocycles with the local conditions of `T`, unramified outside
`T.places ∪ J ∪ J̄`, with `z(γ_v) = slope • z(φ_v)` at `v ∈ J` and `v̄`. A member `z` of the new
group `Sel(J ∪ {𝔮})` lies in `Sel^𝔮(J)` (ties only at `J`, ramification allowed also at `𝔮` and
`𝔮̄`) and satisfies the tie `ev_γ z = s j • ev_φ z`, where `ev_g = evalConjPair g` evaluates at `g`
and at `g^{-c} = (conjGal g)⁻¹`, the inverse of its complex conjugate. 

### `exists_length_tiedSelmer_insert_le`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold. Let `𝔮 = P` with data `l` be a new auxiliary prime
for datum `i`: it can be added to `J` with any slope for `i`. Let `φ = l.frob`,
`γ = l.tameGenerator`, `g^{-c}` the inverse of the complex conjugate of `g`, and `a ∣ ℓ ^ M`. For
units `u` outside at most `2 · rank T` (`= 2 · card n`) residue classes, adding `𝔮` with slope `u⁻¹`
gives a tied Selmer group no longer than the part of the old group `Sel(J)` in `T.frobInTameImage`:
the `z` whose values at `φ, φ^{-c}` are the values at `γ, γ^{-c}` of a class with the ties of `J`
that may ramify also at `𝔮` and `𝔮̄`. 

 ### The end of the descent 

### `length_tiedSelmer_le_of_isUnit`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: primes outside `S₀` with data and slopes to level
`ℓ ^ N`, the first one `P₀` with slope `0` and Frobenius element in `W`, and `V i` at Frobenius
elements with nonzero slope for `i`; here `V i g` says that `g` acts trivially on `T / ℓ ^ M`. Let
`M < N` and `a ∣ ℓ ^ M`. The tied Selmer group `Sel(J)` consists of the cocycles modulo `a` with the
local conditions of `T`, unramified outside `T.places ∪ J ∪ J̄`, with the ties
`z(γ_v) = slope • z(φ_v)` at `v ∈ J` and `v̄`. Suppose that some member has a value with a unit
coordinate, and that for every new auxiliary prime `P` (one that can be added to `J` with any slope
for `i`), with Frobenius element `φ` and tame generator `γ`, each member lies in
`T.frobInTameImage`: its values at `φ, φ^{-c}` are the values at `γ, γ^{-c}` of a class with the
ties of `J` that may ramify also at `P` and `P̄`. Then `Sel(J)` has length at most `T.globalTerm`
plus `T.placesTerm`. 

### `length_tiedSelmer_pow_le`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: primes outside `S₀` with data and slopes to level
`ℓ ^ N`, the first one `P₀` with slope `0` and Frobenius element in `W`, and `V i` at Frobenius
elements with nonzero slope for `i`; here `V i g` says that `g` acts trivially on `T / ℓ ^ M`. Let
`M < N` and let `ϖ` be a uniformizer with `ϖ ^ e ∣ ℓ ^ M`. The tied Selmer group `Sel(J)` consists
of the cocycles with the local conditions of `T`, unramified outside `T.places ∪ J ∪ J̄`, with the
ties `z(γ_v) = slope • z(φ_v)` at `v ∈ J` and `v̄`. Suppose that modulo `ϖ ^ k`, for all `1 ≤ k ≤ e`
and all new auxiliary primes `P` (those that can be added to `J` with any slope for `i`), each
member lies in `T.frobInTameImage`: its values at the Frobenius element `φ` and at `φ^{-c}` are the
values at the tame generator `γ` and at `γ^{-c}` of a class with the ties of `J` that may ramify
also at `P` and `P̄`. Then `Sel(J)` modulo `ϖ ^ e` has length at most `T.globalTerm` plus
`T.placesTerm`. 

 ### The loop over all data and levels 

### `totalTiedLength`

 The sum of the lengths of the tied Selmer groups `Sel(J)` of `T i` modulo `ϖ ^ k`, over all data
`i` and all levels `1 ≤ k ≤ i₀`. 

### `exists_slope_totalTiedLength_lt`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: primes outside `S₀`, the first one `P₀` with
Frobenius element in `W`, with slopes and with data in `AuxPrimeData E (ℓ ^ N)`. Let `P` with data
`l` be a new auxiliary prime for `i`: one that can be added to `J` with any slope for `i`, so
`P, P̄ ∉ S₀ ∪ J` and `V i` holds at `l.frob`. Let `ϖ ^ e ∣ ℓ ^ M` and let the residue field be
finite with more than `2 · card (n i) · e + 1` elements. Suppose that, for some `1 ≤ k ≤ e`, some
member of the tied Selmer group of `T i` modulo `ϖ ^ k` does not lie in `frobInTameImage`: its
values at `φ, φ^{-c}` (`φ = l.frob`) are not the values at `γ, γ^{-c}` (`γ = l.tameGenerator`) of a
class with the ties of `J` that may ramify also at `P` and `P̄`. Then `P` can be added, with a unit
slope for datum `i` and slope `0` for the others, so that `totalTiedLength`, the sum over all data
and all levels `ϖ ^ m`, `1 ≤ m ≤ e`, of the lengths of the tied Selmer groups, drops. 

### `exists_isTiedPrimes_length_tiedSelmer_le`

 Let `IsTiedPrimes ℓ S₀ V W N P₀ J x` hold: primes outside `S₀` with data and slopes to level
`ℓ ^ N`, the first one `P₀` with slope `0` and Frobenius element in `W`, and `V i` at Frobenius
elements with nonzero slope for `i`; here `V i g` says that `g` acts trivially on `T i / ℓ ^ M`. Let
`M < N`, let `ϖ` be a uniformizer with `ϖ ^ e ∣ ℓ ^ M`, and let the residue field be finite with
more than `2 · card (n i) · e + 1` elements for all `i`. Then there are tied primes `J'` with data
`x'` and the same `P₀` whose number is at most `#J + totalTiedLength`, the latter summing the
lengths of the tied Selmer groups for `J` over all data and all levels `ϖ ^ k`, `1 ≤ k ≤ e`, and
whose tied Selmer groups modulo `ϖ ^ e` have length at most `globalTerm` plus `placesTerm`. 

### `exists_totalTiedLength_le`

 Let `ϖ ^ e ∣ ℓ ^ M`, and fix any `V` and `W`. `IsTiedPrimes ℓ S₀ V W N P₀ J x` says that the
primes of `J` lie outside `S₀` and carry slopes `(x v).2` and data in `AuxPrimeData E (ℓ ^ N)`
(place, Frobenius element `φ_v`, tame generator `γ_v`, character to `ℤ / ℓ ^ N`), with `φ_v ∈ W`
for `v = P₀` and `V i` at `φ_v` where the slope for `i` is not zero. A tied Selmer group consists of
the cocycles with the local conditions of its datum, unramified outside its places, `J` and `J̄`,
with `z(γ_v) = slope • z(φ_v)` at `v ∈ J` and `v̄`. If all slopes are `0`, the sum
`totalTiedLength` of the lengths of these groups for all data `T i` modulo `ϖ ^ k`, `1 ≤ k ≤ e`,
has a finite bound `b` that depends neither on `N` nor on `P₀`, `J` and `x`. The proof takes the
sum of the lengths of the groups `Sel(∅)` without auxiliary primes. 

### `exists_isTiedPrimes_card_le_and_length_le`

 Descent. Let `E` be a CM field, `Gal(Ω/E)` the Galois group of the algebraic closure `Ω` of
`ℚ` over it, `ℓ` a prime, `O` the integer ring of a finite extension of `ℚ_ℓ`, and `T i` finitely
many Selmer data: Galois lattices `O ^ (n i)` of rank `card (n i)` with local conditions, unramified
outside the finite set `S₀` of places, on which `det(g - 1) ≠ 0` for `g = g₀, g₀^{-c}`, where
`g^{-c}` is the inverse of the complex conjugate of `g`. Let `g₀` be inertial at a place of `S₀`
prime to `ℓ`, let `W` be a neighbourhood of `g₀`, and let the residue field have more than
`2 · card (n i) · v(ℓ ^ M) + 1` elements for all `i`. There is an integer `s` such that for every
`N > M` there is a set `J` of at most `s` primes that satisfies `IsTiedPrimes` and whose tied
Selmer groups modulo `ℓ ^ M` have length at most `globalTerm + placesTerm`.

`IsTiedPrimes` says that the primes `v ∈ J` have prime norm, that they and their conjugates are
distinct and outside `S₀`, and that each carries slopes `(x v).2` and data `(x v).1` (place,
Frobenius element `φ_v`, tame generator `γ_v`, character to `ℤ / ℓ ^ N`); the first prime `P₀` has
slope `0` and `φ_v ∈ W`, no other prime of `J` or `S₀` divides its norm, the characters take
prescribed values at the Frobenius elements of the later primes, and `φ_v` and `φ_v^{-c}` act
trivially on `T i / ℓ ^ M` where the slope for `i` is not zero.

The tied Selmer group `(T i).tiedSelmer J J x i (ℓ ^ M)` consists of the classes `z` modulo `ℓ ^ M`
that satisfy the local conditions, are unramified outside `(T i).places ∪ J ∪ J̄`, and satisfy the
ties `z(γ_v) = (x v).2 i • z(φ_v)` between tame generator and Frobenius element at the primes
`v ∈ J` and their conjugates. For a datum `T`, `T.globalTerm` is the supremum over `a ≠ 0` of the
lengths of `Hom_G(T / a, (T / a)^{*c})`, with `*c` the dual twisted by complex conjugation, and
`T.placesTerm` is the sum, over the places of `T.places` prime to `ℓ`, of the supremum over
`a ≠ 0` of the excess length of the local cocycles over `T / a`. 
