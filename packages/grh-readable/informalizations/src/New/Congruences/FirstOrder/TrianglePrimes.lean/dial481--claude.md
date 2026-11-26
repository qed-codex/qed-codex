---
{
  "module": "src/New/Congruences/FirstOrder/TrianglePrimes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TrianglePrimes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TrianglePrimes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Taylor–Wiles places in a triangle for the even classes, with prescribed Frobenii

Auxiliary (Taylor–Wiles) places that cut down the even classes of the Tate twists, with Frobenius
data in a prescribed set.

The places are indexed by an exponent e > 0 and a test point, and are chosen one after another. Step
1 finds a new Kummer map (`New.Selmer.IsKummerMap`) and an element that the earlier maps kill and at
which the value of the new map is a given product. Step 2 gets from Chebotarev's theorem a place
whose Frobenius element has twice these values under the maps, and at which even classes take twice
their value at the test point. Step 3 applies the reciprocity law of each Kummer map at its own
place and the later ones.

Throughout, ℓ is a prime, Ω is the algebraic closure of ℚ, and E is a CM field embedded in Ω that
contains a primitive 5040-th root of unity (`New.CMFieldWithRoot5040`); F is its maximal real
subfield, and `New.Selmer.primeBelowPlus` w is the prime of F below a prime w of E.
`New.cyclotomicChar` (written cyc) is the ℓ-adic cyclotomic character; G_ν is the kernel of its
reduction `New.cyclotomicCharMod` modulo ℓ^ν, and `New.conjGal` is the conjugation of Galois
elements by complex conjugation. The letter γ denotes a Galois element that separates the exponents;
in `New.Selmer.exists_isPrimeTriangle` it generates the Galois group modulo the kernel of cyc, and
the triangle is stated for γ⁻¹.

* `New.Selmer.exists_isPrimeTriangle`: for each ν > 0 there are Taylor–Wiles places of level ℓ^ν,
  indexed by one finite ordered set, that satisfy `New.Selmer.IsPrimeTriangle` and have their
  Frobenius data in a prescribed set.

Notions from other files:
* `New.CoeffRing`: The coefficient rings: rings of integers of the finite Galois extensions of ℚ_ℓ
  inside its algebraic closure.
* `New.Selmer.evenClasses`: The even classes: cocycles c in (O/ℓ^ν)(−e), O a coefficient ring,
  unramified off ℓ and a given set of places with their conjugates, with c(`conjGal` g) = c(g), that
  vanish on the elements of trivial cyc in the decomposition groups above ℓ.
* `New.Selmer.IsNuSplitPlace`: A condition on Frobenius data (w, A, σ), which consist of w of prime
  norm, A a place of Ω above w and σ a geometric Frobenius at A: w is not above ℓ, σ fixes μ_{ℓ^ν}.
* `New.Selmer.HasKummerType`: A continuous map to ℤ/ℓ^ν, an odd homomorphism on G_ν, that
  conjugation by a multiplies by cyc(a)^(e + 1); Kummer maps of exponent e have it.
* `New.Selmer.IsKummerMap`: A Kummer map of exponent e for a finite family x of split places, off a
  finite set T of primes of F: the restriction to Gal(Ω/E) of a relation over F. It has the Kummer
  type of exponent e and is unramified off T. For a finite family w of split places above distinct
  primes of F outside T it satisfies a reciprocity law: a linear relation among the values of a
  cocycle over F at the tame generators of w, with the values of the map at the Frobenius elements
  of w as coefficients. The cocycle must satisfy local conditions at the primes above ℓ and below
  the places of x.
* `New.Selmer.IsPrimeTriangle`: Ordered places whose tame generators and Frobenius elements cut down
  the even classes one after another, up to given powers of ℓ.
* `New.mostFrobenii`: The filter of most Frobenii. A set X of data (w, A, σ) belongs to it if each
  nonempty open set of Galois elements has a nonempty open part U such that, for almost all w, X
  contains every datum with σ ∈ U.
* `New.mostFrobeniiAt`: The filter of most Frobenii near g: the same filter, refined by the
  condition that σ lies near g.

## Relation to the literature

Taylor–Wiles primes, equally many at every ℓ-power level, are chosen in triangular form by means of
a count over the real subfield, which gives reciprocity laws for even classes in Tate twists. Each
new Frobenius kills the earlier Kummer maps but not the new one, and their reciprocity laws remove
the even classes. No bound for the even classes is needed; for small ℓ congruences between the
twists cost a power of ℓ for each prime. Tame ramification governed by Frobenius in the Kummer field
of units and the inductive choice of primes at every level are known. Related work: Gras–Munnier,
Extensions cycliques T-totalement ramifiées, 1998; Hajir–Maire–Ramakrishna, Tame Z/pZ-extensions
with prescribed ramification, 2022; Taylor–Wiles, Ring-theoretic properties of certain Hecke
algebras, 1995; Darmon–Diamond–Taylor, Fermat's Last Theorem (2.19), 1995; Dotto–Thorne, Residually
reducible representations of rank 2, 2026.


### `New.Selmer.mul_prod_pow_sub_pow_dvd`

 Let `u` be a unit of `ℤ_ℓ` such that every `u ^ a - 1` with `0 < a < t` divides `ℓ ^ h`, and
let `t + 2 ≤ y`. If `n` divides `ℓ ^ (3 * h)`, then `n` times the product of the `u ^ a - u ^ k`
over the `k < t` other than a given `a < t` divides `ℓ ^ (y * h)`. 

### `New.Selmer.linearIndependent_of_notMem_span_Iio`

 A family of vectors, none of which lies in the span of the earlier ones, is linearly
independent. 

### `New.Selmer.surjective_of_linearIndependent_cast`

 Let `ν > 0`, and let the maps `ψ i` from a group to `ℤ/ℓ^ν` send products to sums. If their
reductions modulo `ℓ` are linearly independent, then together they take every family of values (by
Nakayama's lemma). 

### `New.Selmer.exists_isKummerMap_notMem_span`

 Let `ℓ` be a prime, `Ω` the algebraic closure of `ℚ`, and `E ⊆ Ω` a CM field with a primitive
`5040`-th root of unity and at least four infinite places. Let `ν > 0`, and let `G_ν ≤ Gal(Ω/E)` be
the subgroup that fixes the `ℓ ^ ν`-th roots of unity. Let `x` be a finite family of split places
above distinct primes of the real subfield `F`, and let `v i : G_ν → ℤ/ℓ` be any maps with the same
indices. Then for some finite set `T` of primes of `F` that contains `familyPrimes ℓ x` (the primes
above `ℓ` or below the `x i`), some Kummer map `ψ` of exponent `e` for `x` off `T` has its reduction
`G_ν → ℤ/ℓ` outside the span of the `v i`. 

### `New.Selmer.exists_apply_eq_prod_mul`

 Conjugation separates the exponents. Let `cyc` be `cyclotomicCharMod Ω (ℓ ^ ν)`, with `Ω` the
algebraic closure of `ℚ`, and let `G_ν` be its kernel. For a finite set `s` of exponents below `t`
and `g ∈ G_ν` there is `g' ∈ G_ν` at which every map `ψ` of exponent `d` takes the value
`∏_{a ∈ s} (cyc γ ^ d - cyc γ ^ a) · ψ g`. 

### `New.Selmer.exists_separating_element`

 The separating element for the auxiliary places. Let `ν > 0`, let `ψ i` be maps of exponent
`ty i` and `ψ₀` a map of exponent `e`. Suppose the reductions modulo `ℓ` (`reductionModL`) of the
`ψ i` with `ty i = e` are linearly independent, and the reduction of `ψ₀` is not in their span. Then
some `u` with `cyclotomicCharMod Ω (ℓ ^ ν) u = 1` has `ψ i u = 0` for all `i` and
`ψ₀ u = ∏_{k ≠ e} (cyc γ ^ e - cyc γ ^ k)` over the `k < t`. Here `cyc` is
`cyclotomicCharMod Ω (ℓ ^ ν)` and `Ω` is the algebraic closure of `ℚ`. 

### `New.Selmer.additive_apply_pow_mul_conj`

 Let `δ, g` have trivial cyclotomic character, let `u` fix `μ_{ℓ^ν}`, and let `f`, with values in
`ℤ/ℓ^ν`, satisfy `f (a * b) = f a + f b` whenever `a` has trivial cyclotomic character and `b` fixes
`μ_{ℓ^ν}`. In its value at `δ ^ ℓ ^ ν * (g * conjGal g * (u / conjGal u))` the first factor
contributes `ℓ ^ ν • f δ = 0`, which leaves a signed sum of the values at
`g, conjGal g, u, conjGal u`. 

### `New.Selmer.HasKummerType.eventually_eq_two_mul`

 Let `Ω` be the algebraic closure of `ℚ`, let `δ, g : Gal(Ω/E)` have trivial `ℓ`-adic cyclotomic
character `cyc`, and let `u` lie in the group `G_ν` that fixes `μ_{ℓ^ν}`. Near
`δ ^ ℓ ^ ν * (g * conjGal g * (u / conjGal u))`, where `conjGal` is conjugation by complex
conjugation, a map `ψ` of exponent `e` takes the value `2 * ψ u`. 

### `New.Selmer.evenClasses_eventually_eq_two_nsmul`

 Let `Ω` be the algebraic closure of `ℚ`, let `δ, g : Gal(Ω/E)` have trivial cyclotomic character
and let `u` fix `μ_{ℓ^ν}`; let `conjGal` be conjugation by complex conjugation. Near
`δ ^ ℓ ^ ν * (g * conjGal g * (u / conjGal u))` all even classes `c` of exponent `e` unramified off
`ℓ`, for all coefficient rings `O`, take the value `2 • c g`. 

### `New.Selmer.exists_forall_of_wellFoundedLT`

 Choice along a well-founded order: if, for every `f` whose values before `j` satisfy `P` with
their predecessors, some value satisfies `P j` with the values of `f` before `j`, then some function
satisfies `P` at every index with its values at the earlier ones. 

### `New.Selmer.TriangleEntry`

 What is chosen at one index of the triangle: a split place of `E`, a map from `Gal(Ω/E)` to
`ℤ/ℓ^ν` (`Ω` is the algebraic closure of `ℚ`), and a finite set of primes of the real subfield that
this place and the later ones have to avoid. 

### `New.Selmer.TriangleEntry.frobeniusDatum`

 The place with its Frobenius element. 

### `New.Selmer.TriangleEntry.isNuSplitPlace`

 The place is not above `ℓ` and its Frobenius element fixes the `ℓ^ν`-th roots of unity. 

### `New.Selmer.TriangleEntry.avoidedPrimes`

 The primes to avoid. 

### `New.Selmer.TriangleEntry.kummerCandidate`

 The map, a Kummer map once the entry follows earlier ones. 

### `New.Selmer.TriangleEntry.MayFollow`

 The entry `q` of exponent `e` may follow the entries `f i` of exponents `ty i`: its map is a
Kummer map for the earlier places of exponent `e` and new modulo `ℓ`, and its place is a new one in
`W`, at whose Frobenius element the earlier maps vanish, twice the value of the new map divides the
loss `n`, and the even classes of exponent `e` unramified off `ℓ` take twice their value at the test
element `g`. 

### `New.Selmer.TriangleEntry.MayFollow.isKummerMap`

 The new map is a Kummer map of exponent `e` off `q.avoidedPrimes`: the restriction of a
  relation over the real subfield that is unramified off `q.avoidedPrimes` and whose reciprocity law
  holds at split primes off `q.avoidedPrimes`, for cocycles with local conditions above `ℓ` and
  below the earlier places of exponent `e`. 

### `New.Selmer.TriangleEntry.MayFollow.familyPrimes_subset`

 The primes to avoid include the primes of the real subfield above `ℓ` or below an earlier
  place of exponent `e`. 

### `New.Selmer.TriangleEntry.MayFollow.notMem_span`

 Modulo `ℓ` the new map is independent of the earlier maps of exponent `e`. 

### `New.Selmer.TriangleEntry.MayFollow.two_mul_dvd`

 At the new Frobenius element the new map is nearly a unit: twice its value divides `n`. 

### `New.Selmer.TriangleEntry.MayFollow.apply_eq_zero`

 At the new Frobenius element the earlier maps vanish. 

### `New.Selmer.TriangleEntry.MayFollow.even_apply`

 At the new Frobenius element the even classes of exponent `e` unramified off `ℓ` take twice
  their value at `g`. 

### `New.Selmer.TriangleEntry.MayFollow.primeBelowPlus_ne`

 The new place lies above a new prime of the real subfield. 

### `New.Selmer.TriangleEntry.MayFollow.notMem_earlier`

 It avoids the primes excluded by the earlier maps. 

### `New.Selmer.TriangleEntry.MayFollow.notMem`

 It avoids the primes excluded by the new map. 

### `New.Selmer.TriangleEntry.MayFollow.mem`

 The new place, with its Frobenius element, is allowed. 

### `New.Selmer.eventually_primeBelowPlus_notMem`

 Almost all places of `E` lie neither above `ℓ` nor above a prime in a given finite set `T` of
primes of the real subfield. 

### `New.Selmer.TriangleEntry.exists_mayFollow`

 Let `ℓ` be a prime and `E` a CM field with a primitive `5040`-th root of unity and at least four
infinite places. Let `ν > 0`, `t + 2 ≤ y` and `4 ∣ ℓ ^ (3 h)`, let `cyc γ ^ a - 1` divide `ℓ ^ h`
for `0 < a < t`, let `g` have trivial cyclotomic character `cyc`, and, for every `g'`, let `W`
contain most Frobenii near `δ ^ ℓ ^ ν * g'` for some `δ` with trivial cyclotomic character. Let
finitely many entries `f i` lie above distinct primes of `F`, let their maps have exponents `ty i`,
and let those of exponent `e` be independent as maps `G_ν → ℤ/ℓ` (`reductionModL`). Then some entry
`q` may follow them (`MayFollow`): its map is a Kummer map of exponent `e` for the earlier places of
exponent `e`, off a set `q.avoidedPrimes` that contains the primes above `ℓ` and below these places,
and is outside the span modulo `ℓ` of the earlier maps of exponent `e`; the prime of `F` below its
place is none of the earlier ones and lies in none of the sets of primes to avoid; its datum lies in
`W`; at its Frobenius element the earlier maps vanish, twice the value of the new map divides the
loss `ℓ ^ (y * h)`, and the even classes of exponent `e` unramified off `ℓ` take twice their value
at `g`. 

### `New.Selmer.TriangleEntry.nonempty`

 Some entry exists: at a split place, with the zero map and no primes to avoid. 

### `New.Selmer.TriangleEntry.exists_forall_mayFollow`

 Let `ℓ` be a prime, `E` a CM field with a primitive `5040`-th root of unity and at least four
infinite places, inside the algebraic closure `Ω` of `ℚ`, and `cyc` the `ℓ`-adic cyclotomic
character. Along a finite linear order `J`, with exponents `ty j` and test elements `g j` of trivial
`cyc`, entries `f j` can be chosen so that each may follow the earlier ones (`MayFollow`): its map
is a Kummer map of exponent `ty j` for the earlier places of this exponent, off its set of primes to
avoid, and is independent of their maps modulo `ℓ` on the elements fixing `μ_{ℓ^ν}`; the prime of
`F` below its place is new and avoided by none of the maps up to it; its Frobenius datum is in `W`;
at its Frobenius element the earlier maps vanish, twice the value of its map divides the loss
`ℓ ^ (y * h)`, and the even classes of exponent `ty j` unramified off `ℓ` take twice their value at
`g j`. As in `New.Selmer.TriangleEntry.exists_mayFollow`, it is assumed that `ν > 0`, that
`t + 2 ≤ y`, that `cyc γ ^ a - 1` divides `ℓ ^ h` for `0 < a < t`, that `4 ∣ ℓ ^ (3 h)` unless `J`
is empty, and that for every `g'` there is a `δ` of trivial `cyc` such that `W` contains most
Frobenii near `δ ^ ℓ ^ ν * g'` (`mostFrobeniiAt`). 

### `New.Selmer.TriangleEntry.primeBelowPlus_injective_of_mayFollow`

 If the entries `f j` are indexed by a finite linear order and each may follow the earlier ones
(`MayFollow`), then their places lie above distinct primes of the real subfield. 

### `New.Selmer.TriangleEntry.isTameGeneratorFamily`

 The places of entries, with their tame generators and Frobenius elements, form a tame generator
family (`New.Selmer.IsTameGeneratorFamily`): they are not above `ℓ`, the Frobenius elements fix
`μ_{ℓ^ν}`, and the tame generators are the chosen ones at places of `Ω` above them. 

### `New.Selmer.TriangleEntry.nsmul_tameGenerator_eq_zero_of_mayFollow`

 Let the entries `f j`, of exponents `ty j`, be indexed by a finite linear order `J`, and suppose
that each may follow the earlier ones with test element `g j`, loss `n` and Frobenius data in `W`.
Let `z` be an even class of exponent `ty j`: a cocycle on `Gal(Ω/E)` in `(O/ℓ^ν)(-ty j)`, written as
a function with values in `Unit → O/ℓ^ν`, invariant under complex conjugation and trivial on the
elements of trivial cyclotomic character in the decomposition groups above `ℓ`, here allowed to
ramify at `ℓ`, at the places of the entries and at their conjugates. Let it vanish at the tame
generators of the places before `j` and at the Frobenius elements of those among them of exponent
`ty j`. Then `n` kills the value of `z` at the tame generator of the `j`-th place. 

### `New.Selmer.IsNuSplitPlace.prime_pow_dvd_q_sub_one`

 If the datum `x` is `ν`-split (`IsNuSplitPlace`: its prime is not above `ℓ` and its Frobenius
element fixes `μ_{ℓ^ν}`), then `ℓ ^ ν` divides `x.place.q - 1`, i.e. the norm `q` of its place is
`1` modulo `ℓ ^ ν`. 

### `New.Selmer.isConjApart_of_injective_primeBelowPlus`

 Places of prime norm above distinct primes of the real subfield are distinct from each other and
from all their conjugates. 

### `New.Selmer.exists_isPrimeTriangle`

 Let `ℓ` be a prime, `cyc` the `ℓ`-adic cyclotomic character, and `E` a CM field with a primitive
`5040`-th root of unity and at least four infinite places, inside the algebraic closure `Ω` of `ℚ`,
that lies in the cyclotomic field of level `N > 0`. Let `N + t < y`, let `γ` generate `Gal(Ω/E)`
topologically modulo the kernel of `cyc`, let `cyc γ ^ a - 1` divide `ℓ ^ h` for `0 < a < t`, let
`ℓ ≤ y ^ 2` or `h = 0`, and suppose that for all `ν` and `g` there is a `δ` of trivial `cyc` such
that `W` contains most Frobenii near `δ ^ ℓ ^ ν * g`. Then there is a finite linear order `J` with a
monotone map `ty` (the exponent) to the `e` with `0 < e < t` such that for each `ν > 0` some
Taylor–Wiles places `Q` of level `ℓ ^ ν` indexed by `J` have their Frobenius data in `W` and satisfy
`IsPrimeTriangle` for `γ⁻¹` with bounds `b = y * h` and `c = y ^ 22 * h`. This says, with `τ j` the
chosen generator of tame inertia and `φ j` the Frobenius element at the `j`-th place:
* the `φ j` fix `μ_{ℓ^ν}` and the places are not above `ℓ`;
* there is a finite set `s` of test points of trivial `cyc` with `(#J + #s + 1) * b ≤ c`, such that
  a cocycle unramified off `ℓ` that vanishes at `γ⁻¹` and on `s` is zero, and for each exponent `e`
  and each point of `s` some `φ j` of exponent `e` is where the even classes unramified off `ℓ` take
  twice their value at that point;
* if an even class of exponent `ty j`, allowed to ramify at the places and their conjugates,
  vanishes at the earlier `τ i` and at the earlier `φ i` of the same exponent, then `ℓ ^ b` kills
  its value at `τ j`;
* `∏_{k ≠ e} (cyc γ ^ e - cyc γ ^ k)` and, for `e > 0`, `4 (cyc γ ^ e - 1) ^ 2` divide `ℓ ^ b`. 
