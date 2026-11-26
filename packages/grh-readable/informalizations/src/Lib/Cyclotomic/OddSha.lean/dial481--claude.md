---
{
  "module": "src/Lib/Cyclotomic/OddSha.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/OddSha.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/OddSha.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Detecting unramified cocycles and a uniform bound for a model of the odd part of Ш

Let E be a number field inside ℚ(μ_N) and let l be a prime. Polynomially many elements of the
absolute Galois group of E detect the locally constant cocycles of a Tate twist that take values in
O / lⁿ and are unramified outside l. For a CM field E inside ℚ(μ_N), this gives one integer X of
explicit size whose valuation bounds the length of a module of odd cocycles at every prime l.

## Overview of this theory

For a CM field `E` inside `ℚ(μ_N)`, and `O` the integers of a finite extension of `ℚ_ℓ` with enough
roots of unity for the characters mod `N`, `New.Selmer.shaOdd` is a module of cocycles of `Gal(Ω/E)`
with values in `O/ℓⁿ(-e)`, modelled on the odd part of `Ш¹(E, O/ℓⁿ(-e))`; no comparison with `Ш¹` is
proved. For `e = 0` it consists of the everywhere unramified homomorphisms. Here `ℓ` is a prime and
`e, n ≥ 0`.

* `New.exists_length_shaOdd_le`: for each `t ≥ 0` there is an integer `X`, depending on `E`, `N` and
  `t`, with `0 < X ≤ 2^(4T²⁷) h_E`. Here `T = N + t + 3` and `h_E` is the class number of `E`. The
  length of `New.Selmer.shaOdd` over `O` is at most `v_O(X)` for all `ℓ`, `O`, `n` and all `e < t`.

No equality of characteristic ideals (the main conjecture of Mazur and Wiles) is proved.

Proof outline: 1. `Voronoi`: `New.OddPart.exists_isStickelbergerBound` gives, for `e ≥ 1`, an
integer `0 < X ≤ 2^((N+e+3)⁶)` satisfying `New.OddPart.IsStickelbergerBound N e X`. This is a
bounded divisibility of twisted Stickelberger sums.

2. `Stickelberger`: `New.OddPart.exists_isJacobiFamily` fixes a prime `p`, a place `B` above `p` and
   any `c ∈ ℕ`. It builds a map `J` from `ℚ/ℤ` to units, a variant of Jacobi sums. For `p ≡ 1 mod M`
   and `Mx = 0`, `J(x)` is a unit at places not above `p`. It has absolute value one in every
   complex embedding. Its order at `B` is `New.OddPart.floorDiff c x`. It also satisfies Galois and
   product relations.
3. `Kolyvagin.DerivativeCocycles`: `New.OddPart.exists_isKolyvaginSystem` builds
   `cyc^(e+1)ψ`-cocycles `κ_S : G_ℚ → O/ℓⁿ`. Here `cyc` is the `ℓ`-adic cyclotomic character and `ψ`
   a Dirichlet character mod `N`. The sets `S` range over subsets of a finite set `P` of primes
   `≡ 1 mod cNℓⁿ`, and `p ≡ 1 mod Nℓⁿ∏P`. For `q ∈ P ∖ S` and a place `A` above `q`, the value of
   `κ_S` at a Frobenius at `A` is a value of `κ_{S∪{q}}` on inertia at `A`.
4. `Kolyvagin.ReciprocityComponentBounds`: take `e ≥ 1` and `cycᵉψ` odd. Then `4X²` kills
   `New.OddPart.component`, a set of cocycles `G_ℚ → O/ℓ^ν` attached to `cycᵉψ`
   (`New.OddPart.nsmul_component_eq_zero`, an analogue of Stickelberger's theorem). If moreover
   `ℓ > N + e + 3`, there are `v_ℓ(X) + 1` elements of `G_ℚ` with the following property: a cocycle
   in the component vanishing at all of them is zero
   (`New.OddPart.exists_detecting_points_component`).
5. `OddSha`: for `e > 0`, the group is split by characters `ψ`, and step 4 gives an integer killing
   `New.Selmer.shaOdd`. A bounded number of suitable elements of `G_E` suffice to test whether a
   cocycle is zero. For small `ℓ` this uses ray classes, and for large `ℓ` it uses step 4. Together
   these bound the length. For `e = 0`, the class number `h_E` serves.

## Main definitions and results

* `New.OddPart.exists_detecting_points_cocycles`: the detecting set and the bound on its size.
* `New.OddPart.nsmul_shaOdd_eq_zero_of_isStickelbergerBound`: an integer that kills
  `New.Selmer.shaOdd` for e ≠ 0, at every prime l.
* `New.OddPart.length_shaOdd_le_of_le_sq`, `New.OddPart.length_shaOdd_le_of_sq_lt`: the bounds on
  the length for small and for large primes l.

Notions from other files:
* `Ω`: the fixed algebraic closure of ℚ; `Gal(Ω/E)` is its group of automorphisms
  over `E`, the absolute Galois group of `E`.
* `New.Selmer.tateTwist`: the rank-one representation O(−e), the character cyc^{−e} with values in
  O, as 1 × 1 matrices.
* `New.conjGal`: the endomorphism g ↦ c g c of Gal(Ω / E), where c is `New.cmConj`, the complex
  conjugation fixed in Gal(Ω / ℚ); a cocycle z is odd if z (c g c) = -z g.

## Relation to the literature

For large `l` a bound of this kind follows from the Iwasawa main conjecture of Mazur and Wiles; only
an upper bound for the length at finite level, by an integer of explicit size, is proved here. One
non-zero integer serves at all primes, 2 included; small primes are handled by a crude count of
generators of the ray class group. Source: B. Mazur, A. Wiles, Class fields of abelian extensions of
Q, Invent. Math. 76 (1984); C. Greither, Ann. Inst. Fourier 42 (1992), Thm 3.2.


 ## Few Galois elements detecting unramified cocycles 

### `New.ncard_placesDividing_le_finrank`

 A number field `K` has at most `[K : ℚ]` places above a prime `l`. 

### `New.OddPart.classNumber_mul_index_idelesPowAt_le`

 For `K = ℚ(μ_M)`, the class number times the index of the ideles that are `M`-th powers above
the prime `l` is at most `2 ^ (M³ + 5 M² + M)`. 

### `totient_add_le_pow_twenty`

 The count of detecting points: let `M = N l²` with `2 < M`, `N ≤ y` and `l ≤ y ^ 2`. If
`c ≤ M ^ 3 + 5 M ^ 2 + M`, then `φ(M) + c ≤ y ^ 20`. 

### `card_le_of_prod_dvd_classNumber_mul_index`

 Let `K = ℚ(μ_M)` and `l` a prime. A finite family of integers `m i ≥ 2` whose product divides
the class number of `K` times the index of the ideles that are `M`-th powers above `l` has at
most `M ^ 3 + 5 M ^ 2 + M` members, since `2 ^ card ι ≤ ∏ m i`. 

### `tateTwist_smul_eq_self_of_nsmul_eq_zero`

 An element of `Gal(Ω/E)` with the same `l`-adic cyclotomic character as some `x` fixing `μ_M`
acts trivially, in the twist `tateTwist l E O e`, on the vectors over `O / lⁿ` killed by `M`. 

### `exists_notMem_placesDividing_isPlaceOver`

 If a place `v` of an intermediate field `K` of `Ω/ℚ` is prime to `l`, then so is some place of
`E` lying under the chosen valuation subring `placeOver v` of `Ω`. 

### `New.OddPart.exists_detecting_points_cocycles`

 Few points detect unramified cocycles. Let `E` be a number field whose image in the algebraic
closure `Ω` lies in `ℚ(μ_N)` (`h_sub`), and `l` a prime. There is a finite set `s` in `Gal(Ω/E)`
with (a) `#s ≤ y ^ 20` whenever `N ≤ y` and `l ≤ y ^ 2`; (b) for all `O` (the integers of a finite
extension of `ℚ_l`), `n`, `e`, a cocycle `z` in `selmerModule (tateTwist l E O e) (placesDividing E
l) ∅ (O / lⁿ)` (locally constant, for the character `cyc⁻ᵉ`, unramified off `l`) that vanishes on
`s` is zero.

This is a cocycle analogue, with the crude bound `y ^ 20`, of the class field theory bound on the
number of generators of the Galois group of the maximal pro-`l` extension unramified outside `l`. 

### `New.OddPart.exists_detecting_points_mem_ker`

 Few points in the kernel of the cyclotomic character detect. Let `E ⊆ ℚ(μ_N)` be a number
field, `l` a prime, and let `g₀` generate the absolute Galois group of `E` modulo the kernel of the
`l`-adic cyclotomic character. There is a finite set `s` of points such that (a) they lie in that
kernel; (b) their number is at most `y ^ 20` whenever `N ≤ y` and `l ≤ y ^ 2`; (c) a locally
constant cocycle with values in `O/l ^ n` twisted by `tateTwist l E O e`, unramified off `l`, that
vanishes at `g₀` and on `s` is zero. The same points serve for all `O`, `n` and `e`. 


## A uniform explicit bound on a model of the odd part of Ш for CM subfields of ℚ(μ_N)

For e = 0 the class number serves. For e > 0 a cocycle is split into components over ℚ by characters
mod N. The odd components are killed by an integer of Stickelberger type, and few points detect the
cocycle.

Conventions: `New.Selmer.shaOdd` is the module of locally constant cocycles that are unramified
outside l, vanish on `New.Selmer.shaLocalSet` above l and, for e ≠ 0, are odd.
`New.cyclotomicPowDirichlet l e ψ` is the character cyc ^ e · ψ of Gal(Ω / ℚ).
`New.OddPart.component` is the module of cocycles for its inverse with the matching local
conditions.


### `New.length_shaOdd_zero_le_addVal_classNumber`

 The case `e = 0`. Let `E` be a CM number field, `l` a prime, `O` a ring with
`PadicIntegerRing O l` (the integer ring of a finite extension of `ℚ_l`) and `n : ℕ`. The module
`shaOdd l E O 0 n` consists of the continuous homomorphisms `Gal(Ω/E) → O / lⁿ` that are unramified
at every place. Its length over `O` is at most `addVal O (classNumber E)`, the valuation in `O` of
the class number of `E`. 

### `four_mul_totient_smul_eq_zero_of_sum_eq`

 The last step of splitting by characters. Let `x` be odd: `x (conjGal g) = -x g`, where
`conjGal g = c g c` for the complex conjugation `c`. Let finitely many maps `z ψ` satisfy
`∑ ψ, z ψ (ι h) = φ(N) x (conjGal h) - φ(N) x h` for all `h`, `z ψ (ι (conjGal g)) = z ψ (ι g)`, and
`conjGal (conjGal g) = g`. Then `4 φ(N)` kills `x`. 

### `apply_eq_zero_of_toAlgAut_eq_conj`

 Let `x` on `Gal(Ω/E)` vanish on the inertia groups at places of `E` prime to `l` and on
`shaLocalSet l E e`, where `e ≠ 0`. Let `g` lie in an inertia group at a place prime to `l`, or in
`shaLocalSet l ℚ 1` (a decomposition group above `l`, with trivial cyclotomic character). Then `x`
vanishes at each `w` whose image in `Gal(Ω/ℚ)` is the conjugate `u g u⁻¹`. 

### `New.exists_character_components`

 Splitting by characters. Let `E ⊆ ℚ(μ_N)` be a CM field, `l` a prime, `e ≠ 0`, and `O` with
enough roots of unity for the characters mod `N`. `shaOdd l E O e n` is the module of odd locally
constant cocycles `Gal(Ω/E) → O/lⁿ(-e)` that are unramified outside `l` and vanish on
`shaLocalSet l E e`. `component l e ψ n` consists of cocycles on `Gal(Ω/ℚ)` for `(cyc^e ψ)⁻¹` with
local conditions: locally constant, and vanishing at `cmConj` and at elements fixing `μ_N` that lie
in inertia off `l` or in `shaLocalSet l ℚ 1`. There are `σ : (ZMod N)ˣ → Gal(Ω/ℚ)` and
`b : Gal(Ω/ℚ) → Gal(Ω/ℚ) → Gal(Ω/E)`, independent of the cocycle, with the following property. For
`x ∈ shaOdd l E O e n`, each `z ψ g = ∑ t, (cyc^e ψ)(σ t) • x (b (σ t) g)` lies in
`component l e ψ n`, and `4 * φ N` kills `x` once the odd `z ψ`
(`cyclotomicPowDirichlet l e ψ cmConj = -1`) vanish. 

### `prod_Ioo_pow_le_two_pow_of_le_two_pow`

 The size of the integer in `New.exists_length_shaOdd_le`. Let `y = N + t + 3` and let
`X e ≤ 2 ^ (N + e + 3) ^ 6` for `e ≠ 0`. Then the product over `0 < e < t` of `4 φ(N) · 4 (X e)²`,
raised to the power `y ^ 20`, is at most `2 ^ (4 y ^ 27)`: each factor is at most `2 ^ (4 y ^ 6)`,
and there are at most `y` factors. 

### `New.OddPart.nsmul_shaOdd_eq_zero_of_isStickelbergerBound`

 A Stickelberger bound kills `shaOdd`. Let `E ⊆ ℚ(μ_N)` be a CM field, `l` a prime, `O` with
`PadicIntegerRing O l` having enough roots of unity for the characters mod `N`, and `e ≠ 0`. Let `X`
satisfy `IsStickelbergerBound N e X`, a divisibility for each prime together with a congruence for
the Stickelberger sums. Then `4 φ(N) · 4 X²` kills every `z ∈ shaOdd l E O e n`, that is, every
continuous cocycle `Gal(Ω/E) → O / lⁿ(-e)` unramified outside `l`, vanishing on `shaLocalSet l E e`
and odd under `conjGal`: `4 X²` kills the odd character components of a cocycle, and `4 φ(N)` kills
a cocycle whose odd components vanish. 

### `New.OddPart.length_shaOdd_le_addVal_pow`

 An annihilator and detecting points bound the length. Let `E` be a CM field and `l` a prime. If
a natural number `m` kills `New.Selmer.shaOdd` with values in `O / lⁿ(-e)`, and only `0` vanishes
at all of the at most `k` points `p i`, then the length is at most the valuation of `m ^ k`:
evaluation at the points embeds the module in copies of the `m`-torsion of `O / lⁿ`. 

### `New.OddPart.length_shaOdd_le_of_le_sq`

 Small primes. Let `E ⊆ ℚ(μ_N)` be a CM field, `N ≤ y`, and `l` a prime with `l ≤ y ^ 2`. If a
natural number `m` kills `New.Selmer.shaOdd` with values in `O / lⁿ(-e)`, then its length is at
most the valuation of `m ^ y ^ 20`, as `y ^ 20` or fewer points detect the cocycles that are
unramified outside `l`. 

### `New.OddPart.length_shaOdd_le_of_sq_lt`

 Let `E ⊆ ℚ(μ_N)` be a CM field, `e ≠ 0`, `N + e + 3 ≤ y`, and `l` a prime with `y ^ 2 < l`; let
`O`, the integers of a finite extension of `ℚ_l`, have enough roots of unity for the characters mod
`N`. If `0 < X ≤ 2 ^ y ^ 6` satisfies `New.OddPart.IsStickelbergerBound N e X` (a divisibility at
each prime and a congruence for Stickelberger sums), then the length of `New.Selmer.shaOdd` (odd
continuous cocycles `Gal(Ω/E) → O / lⁿ(-e)` unramified outside `l`, vanishing on
`shaLocalSet l E e`) is at most the valuation of `(4 φ(N) · 4 X²) ^ y ^ 20`.

An upper bound of this kind is usually drawn from the main conjecture of Mazur and Wiles. Here it
comes from the points that Kolyvagin's derivative cocycles give for each odd character. 

### `New.exists_length_shaOdd_le`

 For a CM field `E` inside `ℚ(μ_N)` (`h_sub`) and `t : ℕ` there is an integer `X ≠ 0`, at most
`2 ^ (4 (N + t + 3) ^ 27) · h_E` (`h_E` the class number), such that the following holds for each
prime `l`, each `O` with `PadicIntegerRing O l` (a discrete valuation ring finite and free over
`ℤ_l`, with valuation `addVal O`) and enough roots of unity for the characters mod `N`, and each
`e < t` and `n`. The length over `O` of `shaOdd l E O e n` is at most `addVal O X`. For `e ≠ 0` this
is the module of continuous cocycles `Gal(Ω/E) → O / lⁿ(-e)`, not taken modulo coboundaries, that
are unramified off `l`, vanish on `shaLocalSet l E e` and are odd; for `e = 0` it is the everywhere
unramified continuous homomorphisms.

For large `l` a bound of this kind follows from the Iwasawa main conjecture of Mazur and Wiles; only
an upper bound for the length at finite level, by an integer of explicit size, is proved. 
