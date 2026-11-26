---
{
  "module": "src/New/Congruences/Selmer/Line.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restriction to a line

For Selmer data and Stickelberger systems there is an integer `s₀` such that, for each radius `r`
with `0 < r` and `s₀ r < 1` and each large `N`, we find auxiliary primes `𝔮` and, for each datum and
each system, a polynomial `P` in variables `X_𝔮`. At a point `x = (ζ_𝔮 - 1)_𝔮` given by `ℓ ^ N`-th
roots of unity, `v(P(x))` bounds the length of the twisted Selmer group of a datum `T` if it is less
than `β_T + 1`, and `P(x)` is the twisted value of a system. At some point with coordinates of
valuation at least `r`, the valuation of `P` is at most `β + s₀ r`, where `β` is the number of the
datum or system. For a datum this point is taken on the line `X_{𝔮₀} = Y`, `X_𝔮 = s_𝔮 Y`, where `𝔮₀`
is the first prime and the `s_𝔮` are the slopes of the datum at the other primes.

For a datum, `v(P(x))` is bounded by `v(P⁰(y)) + v(P¹(y))` at the point `x` of the line with
`Y = y`. Here `P⁰` is the restriction to the line of a minor for the tied module that is sharp at
`0`, so that `v(P⁰(0)) ≤ β_T`, the polynomial `P¹` bounds the failure to be tied, and `y` is generic
for both.

* `New.Selmer.SelmerDatum.TwistedLengthLe`: a bound for the length of the twisted Selmer group.
* `New.Selmer.SelmerDatum.exists_boundsSelmer_and_eval_dvd`,
  `New.Selmer.SelmerDatum.exists_boundsSelmer_ellVal_eval_le`: the choice of `P⁰`, of `y` and of the
  polynomial `P` of a datum.
* `New.Selmer.IsTorsionLevel`: the power `ℓ ^ M` modulo which the Selmer modules are computed.
* `New.Selmer.TwistPolynomials`, `New.Selmer.exists_twistPolynomials`: the primes, polynomials and
  points.

Letters: for a set of tied primes (`New.Selmer.IsTiedPrimes`), `J` is the set `Q` of all auxiliary
primes, `P₀ ∈ J` is the first prime `𝔮₀`, and `d` attaches to `v ∈ J` a Frobenius element, a tame
generator, the homomorphism `λ_v = (d v).1.character` to `ℤ / ℓ ^ N` and the slopes `(d v).2 i`.

Notions from other files:
* `New.selmerModule ρ S L B`: the locally constant cocycles for `ρ` with values in `B ^ n` that are
  unramified outside `S` and obey the linear relations `L`. The coefficients `B` are
  `New.QuotSpan a = O / a` or `New.Selmer.DivisibleQuot O = Frac(O) / O`.
* `New.Selmer.SelmerDatum`: a lattice `T` with local conditions and the number `β_T`;
  `New.Selmer.SelmerDatum.tiedSelmer` is its tied Selmer group.
* `New.Selmer.StickelbergerSystem`: elements `Θ_Q` of the group rings of class groups `Cl_Q` with a
  norm relation, and the number `β`.
* `New.CoeffRing`: rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`;
  `New.CoeffRing.normLength` scales lengths so that `O / ℓ` has length `1`.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `exists_smul_eq_zero_of_mem_selmerModule`

 The Selmer group of locally constant cocycles for `ρ` that are unramified outside `S` and obey
`L`, with coefficients in `DivisibleQuot O = Frac(O) / O`, is a torsion module: a member `z` takes
finitely many values, so a common denominator kills it. 

### `length_selmerModule_divisibleQuot_le`

 Let `O` be a discrete valuation ring with valuation `v = addVal O` and let `a ∈ O` be nonzero.
Consider the Selmer groups of locally constant cocycles for `ρ` that are unramified outside `S` and
obey the relations `L`. If the group with coefficients in `QuotSpan a = O / a` has length less than
`v(a)`, then the group with coefficients in `DivisibleQuot O = Frac(O) / O` is no longer than it,
because `a` kills the second group. 

### `twistedSelmer`

 The Selmer group `Sel_Q(T ψ)` modulo `a` of a Selmer datum `T`, for a character `ψ` with values
in a ring `O'` over `O` (by the map `e`): the cocycles in `T ψ ⊗ O' / a` that vanish at the element
`γ_* = T.γ`, are unramified outside `S ∪ Q ∪ Q̄`, where `S = T.places`, and satisfy the
local conditions of `T`. If `ψ(γ_*) = 1`, each class has exactly one cocycle that vanishes at
`γ_*`. 

### `divisibleSelmer`

 The Selmer group `Sel_Q(T ψ)` of a Selmer datum `T` with divisible coefficients, for a character
`ψ` with values in a discrete valuation ring `O'` over `O` (by the map `e`): the cocycles in
`T ψ ⊗ Frac(O') / O'` that vanish at `γ_* = T.γ`, are unramified outside `S ∪ Q ∪ Q̄`,
where `S = T.places`, and satisfy the local conditions of `T`. 

### `divisibleLength`

 The length over `O'` of the Selmer group `Sel_Q(T ψ)` with coefficients in `Frac(O') / O'`. 

### `TwistedLengthLe`

 For all large coefficient rings `O' ⊇ O`, the character `ψ` has values in `O'` and the group
`Sel_Q(T ψ)` with coefficients in `Frac(O') / O'` has length at most `b`, normalised by
`len O' / ℓ = 1`. 

### `TwistedLengthLe.mono`

 A bound for the length of the twisted Selmer group may be weakened. 

### `tieRelations_union`

 Let `d` attach to each prime `w` a tame generator `γ_w` and a Frobenius element `φ_w` (first
component) and slopes `s` indexed by `ι` (second component). The ties `z(γ_w) = s • z(φ_w)` with the
slopes of index `i`, as relations by `n × n` matrices, at the primes of `I ∪ I'` are the ties at
the primes of `I` together with those at the primes of `I'`. 

### `BoundsSelmer`

 The polynomial `P` bounds the length of `Sel(x)`, the Selmer module modulo `ℓ ^ M` of the twist
of `ρ` by `ψ_x(g) = ∏ (1 + x_j) ^ (h_j g)`: we have `len Sel(x) ≤ v(P(x))` at all points `x` over
all discrete valuation rings of characteristic zero over `O`, not only where `ψ_x` is a
character. 

### `restrictToLine`

 The restriction of a polynomial to the line `X_j = a_j Y`. 

### `eval₂_restrictToLine`

 The value at `y` of the restriction of `P` to the line `X_j = a_j Y` is the value of `P` at the
point `(a_j y)_j`, with coefficients mapped by `e`. 

### `gaussVal_tiePolynomial_le`

 Let `d` attach a Frobenius element `φ_v` to each prime `v`, and let `P¹ = tiePolynomial ρ I d`
be the product of the polynomials `det ((1 + Y) ρ(g) - 1)` over `g = φ_v` and its conjugate inverse
`g = φ_v^{-c}` for `v ∈ I`. If `2 n #I ≤ s₀`, where `n` is the rank of `ρ`, then the Gauss valuation
of radius `r` satisfies `v_r(P¹) ≤ s₀ r`, because each of the `2 #I` factors has a unit coefficient
in degree `n`. 

### `coe_twistRep_pointChar`

 Let `λ_j = lam j` be homomorphisms to `ℤ / q` and `ζ_j` be `q`-th roots of unity. The twist of
`ρ` by the character `g ↦ ∏ ζ_j ^ (λ_j g)` is the twist by the value of
`ψ_X(g) = ∏ (1 + X_j) ^ (λ_j g)` at the point `x = (ζ_j - 1)_j`. 

### `reduceModPow_eq_one`

 The action on the lattice of a Selmer datum `T`, reduced modulo `ℓ ^ M`, is trivial on the
inertia groups above the places outside `S₀`. 

### `length_tiedSelmer_erase_le`

 Let `J` be a set of tied primes (`IsTiedPrimes`): auxiliary primes with a first prime `P₀ ∈ J`,
whose Frobenius element `(d P₀).1.frob` lies in `W`, and with Frobenius elements `φ_w`, tame
generators `γ_w` and slopes given by `d`. Let `M < N`. Suppose that the elements with the property
`V i` act trivially on `T` modulo `ℓ ^ M`, and that the Frobenius element of `P₀` and its conjugate
inverse act modulo `ℓ ^ M` as `g₀` and `g₀^{-c}` (`idOrConjInv`). If the Selmer group modulo `ℓ ^ M`
tied at all primes of `J` has length at most `globalTerm + placesTerm`, then the group tied only at
the primes other than `P₀` has length at most `β_T = globalTerm + placesTerm + firstPrimeTerm`. 

### `exists_boundsSelmer_and_eval_dvd`

 Let `O` be the ring of integers of a finite extension of `ℚ_ℓ` and `T` a Selmer datum: a lattice
`O ^ n` with an action `ρ` of `Gal(Ω/E)`, unramified outside `T.places ⊆ S₀`, with the relations
`T.classRelations`. Its number `β_T = T.β` is the sum of a global term, local terms at `T.places`
and a term for the element `g₀`. Let `J` be a set of auxiliary primes with first prime `P₀`
(`IsTiedPrimes`), where `d` gives each `v ∈ J` a Frobenius element `φ_v`, a tame generator `γ_v`, a
character to `ℤ / ℓ ^ N` and the slope `s_v = (d v).2 i` for the index `i` of `T`. A cocycle `z` is
tied at `v` if `z(γ_v) = s_v • z(φ_v)`, and likewise at the conjugate prime. Let `T` modulo `ℓ ^ M`
be trivial at the elements with the property `V i`, and let `N ≠ 0`, `r ≤ 1` and `M ≤ N r`. Suppose
that the Selmer group of `T` modulo `ℓ ^ M` that is tied at the primes of `J` other than `P₀` has
length at most `β_T`. Then there is a polynomial `P⁰ = lineBound` with `v(P⁰(0)) ≤ β_T` and the
following property. Let `e : O → O'` be a discrete valuation ring of characteristic zero over `O`
with a map `f` to `ℤ̄_ℓ = intQpBar ℓ` that reflects divisibility, let `y ∈ O'` with
`ellVal (f y) ≥ r`, and let `x = (a_v y)_{v ∈ J}`, where `a = lineDirection P₀ J d i` has
`a_{P₀} = 1` and `a_v = s_v` otherwise. Then some polynomial `P` bounds the length of the Selmer
module of the characters `(d v).1.character` at all points (`BoundsSelmer`), and `P(x)` divides
`P⁰(y) P¹(y)` in `ℤ̄_ℓ`. Here `P¹ = tiePolynomial` is the product of the `det ((1 + Y) ρ(g) - 1)`
over the Frobenius elements `g = φ_v` of the primes `v` of `J` other than `P₀` and their conjugate
inverses. 

### `divisibleLength_pointChar_le`

 Let `P` bound, at all points `x`, the length of the Selmer module `Sel(x)` modulo `ℓ ^ M` of the
twist of `T` at `x`, unramified outside `S ∪ J ∪ J̄` and with the relations `T.classRelations`
(`BoundsSelmer`), for characters `λ_v = lam v` to `ℤ / q`. Let `e : O → O'` be a ring map to a
discrete valuation ring `O'` of characteristic zero, with valuation `v = addVal O'`, and let the
`ζ_v ∈ O'` be `q`-th roots of unity. At `x = (ζ_v - 1)_v` the module `Sel(x)` is the Selmer group
`Sel_J(T ψ)` modulo `ℓ ^ M` for `ψ = ∏ ζ_v ^ λ_v` (`pointChar`). So if `v(P(x)) < v(ℓ ^ M)`, where
`P(x)` is `P` evaluated through `e`, then `v(P(x))` bounds the length of `Sel_J(T ψ)` with
coefficients in `Frac(O') / O'` (`divisibleLength`). 

### `exists_boundsSelmer_ellVal_eval_le`

 The choice of the polynomial `P` of a Selmer datum `T` over a coefficient ring `O`, the ring of
integers of a finite Galois extension of `ℚ_ℓ`, included in `ℤ̄_ℓ` by `O.toIntQpBar`. The datum is
a lattice `O ^ n` with Galois action, unramified outside `T.places ⊆ S₀`, with the relations
`T.classRelations` (local conditions above `ℓ` and vanishing at `T.γ`); `β_T = T.β` is the sum of a
global term, local terms at `T.places` and a term for the element `g₀`. Let `J` be a set of
auxiliary primes with first prime `P₀` (`IsTiedPrimes`), where `d` gives each `w ∈ J` a Frobenius
element `φ_w`, a tame generator `γ_w`, a character to `ℤ / ℓ ^ N` and the slope `s_w = (d w).2 i`
for the index `i` of `T`; a cocycle `z` is tied at `w` if `z(γ_w) = s_w • z(φ_w)`, and likewise at
the conjugate prime. Let `T` modulo `ℓ ^ M` be trivial at the elements with the property `V i`, and
let `N ≠ 0`, `2 rank(T) #J ≤ s₀`, `r ≤ 1` and `M ≤ N r`. If the Selmer group modulo `ℓ ^ M` that is
tied at the primes of `J` other than `P₀` has length at most `β_T`, then some `P` bounds the length
of the Selmer module of these characters at all points (`BoundsSelmer`), and
`v(P(x₀)) ≤ β_T + s₀ r` at a point `x₀` over `ℤ̄_ℓ` whose coordinates have valuation at least `r`.
Here `v = ellVal` has `v(ℓ) = 1`, and `normLength` multiplies the length `β_T` by the valuation of a
uniformiser of `O`. 

### `twistedLengthLe_pointChar`

 Let `T` be a Selmer datum over a coefficient ring `O`, for the set `S₀` of places and the
element `g₀`: a lattice with Galois action, unramified outside `S = T.places ⊆ S₀`. Let `P` bound,
at all points, the length of the Selmer module modulo `ℓ ^ M` of the twist of `T` by the characters
`λ_v = lam v` to `ℤ / q`, unramified outside `S ∪ J ∪ J̄` and with the relations `T.classRelations`,
the local conditions above `ℓ` and vanishing at `T.γ` (`BoundsSelmer`). Let the `ζ_v ∈ ℤ̄_ℓ` be
`q`-th roots of unity, `x = (ζ_v - 1)_v` and `ψ = ∏ ζ_v ^ λ_v` (`pointChar`). If `v(P(x)) < M`,
where `v = ellVal` has `v(ℓ) = 1`, then over all large coefficient rings the normalised length of
`Sel_J(T ψ)` with divisible coefficients is at most `v(P(x))` (`TwistedLengthLe`). 

### `SelmerDatum.eventually_reduceModPow_idOrConjInv_eq`

 For `g` near `g₀`, the element `g` (for `b = true`) or its conjugate inverse `g^{-c}` (for
`b = false`) acts on the lattice of a Selmer datum `T` modulo `ℓ ^ M` as `g₀` or `g₀^{-c}` does. 

### `IsTorsionLevel`

 `ℓ ^ M` is a suitable level of torsion for the Selmer data `T i`: the exponent `M` exceeds the
normalised numbers `β_T` by more than `1`, and the residue field of `O` is large. 

### `IsTorsionLevel.β_lt`

 `M > β_T + 1` for each datum, with `β_T` scaled so that `O / ℓ` has length `1`. 

### `IsTorsionLevel.lt_card_residueField`

 The residue field has more than `2 rank(T i) len(O / ℓ ^ M) + 1` elements, which leaves room
  for the choice of slopes. 

### `TwistPolynomials`

 Auxiliary primes, homomorphisms to `ℤ / ℓ ^ N`, and polynomials with points for Selmer data
`T i` and Stickelberger systems `Y k`, for an integer `s₀` and a radius `r`. Valuations are those
of `ellVal`, with `v(ℓ) = 1`. 

### `TwistPolynomials.auxPrimes`

 The set `Q` of primes. 

### `TwistPolynomials.auxiliary`

 `Q` is auxiliary for `S₀`. 

### `TwistPolynomials.two_mul_card_le`

 `Q` has at most `s₀ / 2` primes. 

### `TwistPolynomials.primeChar`

 The homomorphisms `λ_𝔮` to `ℤ / ℓ ^ N`, one for each prime `𝔮` of `Q`. 

### `TwistPolynomials.isFromU1_primeChar`

 `λ_𝔮` is continuous and `λ_𝔮(Art y) = η(y / ȳ)` for an idele class character `η` of tame
  level `𝔮` that is trivial above `ℓ`. So it is anticyclotomic, unramified outside `𝔮` and `𝔮̄`, and
  zero on the decomposition groups above `ℓ`. 

### `TwistPolynomials.exists_eq_ofAdd_one`

 `λ_𝔮` is onto on inertia at `𝔮`. 

### `TwistPolynomials.datumPoly`

 The polynomials of the data. 

### `TwistPolynomials.systemPoly`

 The polynomials of the systems. 

### `TwistPolynomials.datumPoint`

 The points of the data. 

### `TwistPolynomials.systemPoint`

 The points of the systems. 

### `TwistPolynomials.le_ellVal_datumPoint`

 The coordinates of the point of a datum have valuation at least `r`. 

### `TwistPolynomials.le_ellVal_systemPoint`

 The coordinates of the point of a system have valuation at least `r`. 

### `TwistPolynomials.ellVal_datumPoly_le`

 At the point of a datum, `v(P) ≤ β_T + s₀ r`. 

### `TwistPolynomials.ellVal_systemPoly_le`

 At the point of a system, `v(P) ≤ β + s₀ r`. 

### `TwistPolynomials.groupRingEval_eq_eval`

 For `ℓ ^ N`-th roots of unity `ζ_𝔮`, `ψ = ∏ ζ_𝔮 ^ λ_𝔮` and `x = (ζ_𝔮 - 1)_𝔮`, the value of `ψ`
  at the element `Θ_Q` of a system is `P(x)`. 

### `TwistPolynomials.length_le`

 For the same `ψ` and `x`, the group `Sel_Q(T ψ)` has length at most `v(P(x))` if
  `v(P(x)) < β_T + 1`. 

### `nonempty_twistPolynomials_of_isTiedPrimes`

 Let `T i` be Selmer data over a coefficient ring `O` and `Y k` Stickelberger systems. Let `J` be
a set of tied auxiliary primes with elements and slopes given by `d` and with a first prime `P₀`
whose Frobenius element lies in the set `W`, otherwise unused (`IsTiedPrimes`); where the slope for
`T i` is nonzero, the Frobenius element and its conjugate inverse act trivially on `T i` modulo
`ℓ ^ M`. Let the Selmer group of each `T i` modulo `ℓ ^ M` tied at all primes of `J` (`tiedSelmer`)
have length at most `globalTerm + placesTerm`, the global term of `T i` plus its local terms at the
places of `(T i).places` prime to `ℓ`; adding the term for `g₀` gives the number `β` of `T i`. Let
the Frobenius element `φ = (d P₀).1.frob` of `P₀` and its conjugate inverse act on each `T i` modulo
`ℓ ^ M` as `g₀` and its conjugate inverse do, and let `ϑ(φ) ≡ ϑ(g₀)` modulo `ℓ ^ M'` for the
character `ϑ = twistChar` of each `Y k`. Let `M > O.normLength β + 1` for each `T i` and
`M' > β + 1` for each `Y k`, where `β = v(1(Θ_∅)) + 2 m v(ϑ(g₀) - 1)`, `1(Θ_∅)` is the value of the
trivial character at the element `(Y k).element ∅` and `m` is the length of the list
`(Y k).exponents`. Let `c ≥ 1` bound the ranks of the `T i` and the lengths `m`, and let `s₀ ≥ 1`,
`2 c #J ≤ s₀`, `s₀ r < 1`, `M < N` and `M, M' ≤ N r`. Then `TwistPolynomials` is inhabited: there
are auxiliary primes (the proof takes `J`), homomorphisms to `ℤ / ℓ ^ N`, and for each datum and
system a polynomial `P` that controls its twists at roots of unity, with a point of valuation at
least `r` where `v(P) ≤ β + s₀ r`, with `O.normLength β` in place of `β` for the `T i`. 

### `exists_twistPolynomials`

 Let finitely many Selmer data `T i` and Stickelberger systems `Y k` be given, and let `g₀` lie
in an inertia group above a place of `S₀` prime to `ℓ`. Let `M > β_T + 1` for all data and let the
residue field of `O` have more than `2 rank(T i) len(O / ℓ ^ M) + 1` elements (`IsTorsionLevel`).
There is an integer `s₀ ≥ 1` such that for every rational `r > 0` with `s₀ r < 1` and every large
`N` the following exist (`TwistPolynomials`), where `v(ℓ) = 1` and `β_T` and the lengths of Selmer
groups are scaled so that `O / ℓ` has length `1`.
* A set `Q` of at most `s₀ / 2` primes of prime norm that lie outside `S₀`, with conjugates outside
  `S₀` and `Q` (`IsAuxiliary`).
* For each `𝔮 ∈ Q` a homomorphism `λ_𝔮` to `ℤ / ℓ ^ N` that is onto on inertia at `𝔮` and comes by
  `y ↦ y / ȳ` from an idele class character of modulus `𝔮` trivial above `ℓ` (`IsFromU1`).
* For each datum and each system a polynomial `P` over `ℤ̄_ℓ` in variables `X_𝔮`, and a point with
  coordinates of valuation at least `r` at which `v(P) ≤ β + s₀ r`, for the number `β` of that datum
  or system.

For `ℓ ^ N`-th roots of unity `ζ_𝔮` put `ψ = ∏ ζ_𝔮 ^ λ_𝔮` and `x = (ζ_𝔮 - 1)_𝔮`. For a system,
`P(x)` is the value of `ψ` at its element `Θ_Q`. For a datum `T` with `v(P(x)) < β_T + 1`, the
Selmer group `Sel_Q(T ψ)` with divisible coefficients has length at most `v(P(x))`. 
