---
{
  "module": "src/Lib/Cyclotomic/Kolyvagin/DerivativeCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Kolyvagin/DerivativeCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Kolyvagin/DerivativeCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Kolyvagin's derivative cocycles from Gauss sums, for one set of primes

The main result, `New.OddPart.exists_isKolyvaginSystem`, constructs Kolyvagin's cocycles `κ S` with
values in `O/lⁿ` from the Jacobi-type quotients `J` of `New.OddPart.exists_isJacobiFamily`. One
takes `lⁿ`-th roots `y` of `J`, forms the roots of unity `γ y / (g γ g⁻¹) y`, applies the derivative
operators at the primes of `S` and sums against `aᵉ ψ(a)`. The local properties are read modulo a
place, where roots of unity of order prime to it stay distinct.

* `New.OddPart.IsKolyvaginSystem`: the properties of the cocycles `κ S`.
* `New.OddPart.exists_isKolyvaginSystem`: a Kolyvagin system exists.
* `New.OddPart.derivativeSum`: the derivative operators followed by the character sum.

Conventions: `Ω = ℚ̄` is an algebraic closure of `ℚ`, and its places are valuation subrings
(`ClosurePlace`); `DiscreteUnits Ω` is `Ω^×` written additively, so `n • u` is `uⁿ`, and
`galUnitsRep g` is the action of `g` on it; `New.QZ.ofZMod M a` is `a/M` in `ℚ/ℤ`;
`QuotSpan (l ^ n : O)` is `O/lⁿ`; `floorDiff c x` is `⌊c ⟨x⟩⌋ - ⌊c ⟨-x⟩⌋`, where `⟨x⟩` is the
representative of `x` in `[0, 1)`.

Notions from other files:
* `New.OddPart.principalUnits B`: the units of `Ω` congruent to `1` modulo the maximal ideal of `B`,
  as an additive subgroup of `DiscreteUnits Ω`.
* `New.IsFrob B q σ`: `σ` stabilises `B`, and `σ x ≡ x ^ q` modulo the maximal ideal of `B` for
  every `x` in `B`; for `q = 1` this says that `σ` lies in the inertia group of `B`.
* `New.rootPowHom Ω m`: the map `ℤ/m → Ω^×`, `t ↦ ζᵗ`, for a fixed primitive `m`-th root of unity
  `ζ`; it is injective, and its image is the set of `m`-th roots of unity.
* `New.cyclotomicPowDirichlet l e ψ`: the character `cycᵉ ψ` of `Gal(ℚ̄/ℚ)` with values in `Oˣ`,
  where `cyc` is the `l`-adic cyclotomic character.

## Relation to the literature

Known result: Kolyvagin's derivative classes of the Euler system of Gauss sums. Here the classes
carry a Tate twist and a Dirichlet character and are cocycles over the rationals that vanish at one
fixed element. Their ramification, the relation between Frobenius and inertia, and the link between
the bottom class and the Stickelberger element are also covered. Source: K. Rubin, Kolyvagin's
system of Gauss sums, Arithmetic Algebraic Geometry (Texel 1989), Progr. Math. 89, 1991, 309-324;
with a Tate twist: G. Banaszak, W. Gajda, Euler systems for higher K-theory of number fields, J.
Number Theory 58 (1996).


### `_root_.New.IsFrob.sub_nsmul_mem_principalUnits`

 Let `g` act as the `a`-th power modulo the maximal ideal of `B` (`IsFrob B a g`), and let
the `m`-th power of `u` be a unit at `B`, where `m ≠ 0`. Then `g u / uᵃ` is a principal unit at
`B`. 

### `eq_of_mem_principalUnits`

 Roots of unity of order prime to the residue characteristic stay distinct modulo `B`. Let
`μ = New.rootPowHom Ω m` be the fixed map `t ↦ ζᵗ` from `ℤ/m` to `Ω^×`. If `m` is a unit at `B`
and `μ (a - b)` is a principal unit at `B`, then `a = b`. 

### `mem_cycloGalGroup_of_mem_inertiaGroup`

 Let `M = m a` with `a` a unit at `B`. An element `g` of the inertia group of `B` that fixes
the `m`-th roots of unity fixes the `M`-th roots of unity. 

### `exists_inertia_cyclotomicChar_eq`

 If `B` lies above the prime `l` and `a` is prime to `l`, some element of the inertia group of
`B` in `Gal(Ω/ℚ)` has `l`-adic cyclotomic character `a`. 

### `cyclotomicPowDirichlet_smul`

 If `g` raises the `(N m)`-th roots of unity to the power `a`, then on an element `x` of an
`O`-module with `m x = 0` the value `cyclotomicPowDirichlet l e ψ g` acts as the scalar
`aᵉ ψ(a)`. 

### `exists_monoidHom_units_zmod_eq_ofAdd_one`

 Discrete logarithm: for a prime `q ≡ 1 mod k` there is a homomorphism `L` from `(ℤ/q)ˣ` to
`ℤ/k` (written multiplicatively) that sends some unit `g` to `1`, so `L` is onto. 

### `galUnitsRep_conj_of_nsmul_eq_zero`

 An `m`-th root of unity `u` of `Ω` is moved alike by `γ` and by its conjugate `g γ g⁻¹`. 

### `shift_indep_of_distribution`

 Shifts do not matter. Let `Λ S d` be linear maps, for finite sets `S` of primes and shifts
`d`, such that adding a prime `q` to `S` first translates by `u/q` with weight `L q u - d q` and
sums over the units `u` mod `q` (`Λ_insert`), and `Λ S d G` reads only `G` and the shifts on `S`
when `S ⊆ I` (`Λ_congr`). If summing `F` over the translates by `b/r`, `r ∈ I ∖ S`, only changes
the shifts (`distr`), then for `S ⊆ I` the value `Λ S d F` does not depend on `d`. 

### `derivativeSum`

 Kolyvagin's derivative followed by the character sum, with values in `O/lⁿ`
(`QuotSpan (l ^ n : O)`). For each `q ∈ S`, a function on `ℚ/ℤ` is translated by `u/q` with weight
`L q u - d q` and summed over the units `u` mod `q`; the values of the result at `a / N lⁿ` are
then summed against `aᵉ ψ(a)` over the units `a` mod `N lⁿ`. 

### `derivativeSum_empty`

 With no primes, `derivativeSum` is the character sum: the value of `G` at `a / N lⁿ` is summed
against `aᵉ ψ(a)` over the units `a` mod `N lⁿ`. 

### `derivativeSum_insert`

 Adding a prime `q` to `S` applies the derivative at `q` first. 

### `cyclotomicPowDirichlet_smul_derivativeSum`

 Substituting `a u` for `u` in all the sums. Here `derivativeSum e ψ L S d G ∈ O/lⁿ` applies
Kolyvagin's derivative to `G : ℚ/ℤ → ZMod (lⁿ)`: for each `q ∈ S`, `G` is translated by `u/q` with
weight `L q u - d q` and summed over the units `u` mod `q`, and the values of the result at
`b / N lⁿ` are then summed against `bᵉ ψ(b)` over the units `b` mod `N lⁿ`. Let `M` be a multiple of
`N lⁿ` and of the primes of `S`, and let `a` be the cyclotomic character of `g` mod `N lⁿ`; if
`G x = G' (a x)` on the `M`-torsion of `ℚ/ℤ`, and `f q = L q v + d q` with `v ≡ a` mod `q` for each
`q ∈ S`, then `cycᵉ ψ (g)` (`cyclotomicPowDirichlet l e ψ g`) times `derivativeSum … d G` is
`derivativeSum … f G'`. 

### `derivativeSum_eq_of_prime`

 The case of a prime `r ≡ 1 mod N lⁿ` outside `S`, where `rᵉ ψ(r) = 1` in `O/lⁿ`. Let `M` be
a multiple of `N lⁿ` and of the primes of `S`. If `G x = G' (r x)` on the `M`-torsion of `ℚ/ℤ`,
then `derivativeSum` takes the same value on `d, G` as on `f, G'`, where `f q = L q r' + d q` for
the unit `r'` of `ℤ/q` that `r` gives. 

### `derivativeSum_congr`

 `derivativeSum` reads only the shifts at the primes of `S` and the values on the
`M`-torsion of `ℚ/ℤ`, where `M` is a multiple of `N lⁿ` and of the primes of `S`. 

### `exists_cyclotomicPowDirichlet_smul_derivativeSum`

 Equivariance of `derivativeSum` under `g`: only the shifts change. Let `M` be a multiple
of `N lⁿ` and of the primes of `S`, and let `a` be the cyclotomic character of `g` mod `M`. If
`G x = G' (a x)` on the `M`-torsion of `ℚ/ℤ`, then `cycᵉ ψ (g)` times `derivativeSum … d G` is
`derivativeSum … f G'` for some shifts `f`. 

### `sub_one_smul_sum_eq_zero`

 Let `M` be a multiple of `N lⁿ`, let the natural number `a` represent the cyclotomic character
of `g ∈ Gal(ℚ̄/ℚ)` mod `N lⁿ`, and let `s : ℚ/ℤ → ℤ` and `G : ℚ/ℤ → ℤ/lⁿ` satisfy
`G x = a s(x) - s(a x)` on the `M`-torsion. Suppose that the character sum
`∑_u G(u / N lⁿ) uᵉ ψ(u)` of `G` (`derivativeSum` for no primes) vanishes in `O/lⁿ`
(`QuotSpan (l ^ n : O)`), where `u` runs over the units mod `N lⁿ`. Then `cycᵉ⁺¹ ψ (g) - 1`
(`cyclotomicPowDirichlet l (e + 1) ψ g - 1`) kills the character sum `∑_u s(u / N lⁿ) uᵉ ψ(u)` of
`s` in `O/lⁿ`. 

### `commutatorLog`

 The exponent `t` with `γ y / (g γ g⁻¹) y = ζᵗ`, for the fixed primitive `m`-th root of unity
`ζ` of `New.rootPowHom`, when this quotient is an `m`-th root of unity (otherwise some value that
is of no use). 

### `rootPowHom_commutatorLog`

 If the commutator `γ⁻¹ (g γ g⁻¹)` moves `y` by an `m`-th root of unity, then `commutatorLog`
is the exponent of `γ y / (g γ g⁻¹) y`: `ζ ^ commutatorLog m γ y g = γ y / (g γ g⁻¹) y`. 

### `isLocallyConstant_commutatorLog`

 `commutatorLog m γ y g` is locally constant in `g`, since the orbit map `g ↦ (g γ g⁻¹) y` is. 

### `nsmul_exponent_eq_sub`

 The cocycle rule. Let `g` act on the `m`-th roots of unity by `a`, and let `g y / y'` be an
`m`-th root of unity. If `ζᵗ = γ y / (g' γ g'⁻¹) y`, `ζˢ = γ y' / (g g' γ (g g')⁻¹) y'` and
`ζ ^ s' = γ y' / (g γ g⁻¹) y'`, where `ζ ^ t` is `rootPowHom Ω m t`, then `a t = s - s'`. 

### `exists_inertia_smul_add_ofZMod`

 Let `B` lie above the prime `q` and let `M` be a unit at `B`. For a unit `v` mod `q` there is
an element `τ` of the inertia group of `B` whose cyclotomic character mod `q M`, acting on `ℚ/ℤ`,
sends `x + v u / q` to `x + u / q` for every `x` in the `M`-torsion and every `u` mod `q`. 

### `exponent_eq_of_inertia`

 Let `g` lie in the inertia group of a place `B` at which `m` is a unit, let `γ` act on the
`m`-th roots of unity by `a`, and let `g r / r = ζᵇ`. Suppose that `g y / y` and `γ y / y'` are
`m`-th roots of unity, and that `(y / rˢ)ᵐ` and `(y' / r ^ s')ᵐ` are units at `B`. If
`γ y / (g γ g⁻¹) y = ζᵗ`, then `t = a s b - s' b`. Here `ζ ^ t` is `rootPowHom Ω m t`. 

### `telescoping_mem_principalUnits`

 Let `τ` lie in the inertia group of `B` and let `φ` be a `q`-Frobenius at `B`. Let the `Y b`,
for `b` mod `q`, have `m`-th powers that are units at `B` and congruent to each other modulo `B`,
and let `lg (v u) ≡ lg u + 1 mod m` for the units `u` mod `q`. Then
`∏_b Y b / φ (Y 0) · ∏_u (τ Y(v u) / Y u) ^ lg u` is a principal unit at `B`. 

### `derivative_sub_frob_mem_principalUnits`

 The congruence behind the relation between Frobenius and inertia. Let `B` lie above `q`, let `τ`
lie in its inertia group, let `φ` be a `q`-Frobenius at `B`, and let `γ ∈ Gal(Ω/ℚ)` and `y ∈ Ωˣ`.
Let `Y : ℤ/q → Ωˣ` be such that at every place above `q`, `Y bᵐ` is a unit and `(Y b / Y 0)ᵐ` is a
principal unit. Let `v` be a unit mod `q` and `lg` satisfy `lg (v u) ≡ lg u + 1 mod m`. Suppose
`φ (Y 0) / y` and `τ Y(v u) / Y u` are `m`-th roots of unity, and `(∏_b Y b / y)ᵐ` is a root of
unity. Then `∏_u (γ Y u / τγτ⁻¹ Y u) ^ lg u ≡ γ y / φγφ⁻¹ y` modulo `B`, i.e. their quotient is a
principal unit at `B`. 

### `IsKolyvaginSystem`

 A Kolyvagin system for the character `χ`, the element `γ`, the prime `p` and the set of primes
`P`: cocycles `κ S`, one for each `S ⊆ P`, that are unramified over `ℚ(ζ_N)` away from `l`, `p` and
`S`, vanish at `γ`, and are linked by the relation between Frobenius and inertia at the primes of
`P`. 

### `IsKolyvaginSystem.mem_vanishingCocycles`

 `κ S` is a locally constant `χ`-cocycle that vanishes on inertia over `ℚ(ζ_N)` at the places
  above neither `l`, `p` nor a prime of `S`. 

### `IsKolyvaginSystem.apply_eq_zero`

 `κ S` vanishes at `γ`. 

### `IsKolyvaginSystem.exists_mem_inertiaGroup_eq`

 For `q ∈ P ∖ S` and a Frobenius `φ` at a place `A` above `q`, `κ S φ` is a value of
  `κ (S ∪ {q})` on inertia at `A`. 


## The cocycles at one level

In this section `y : ℚ/ℤ → Ω^×` is a family whose `lⁿ`-th powers `lⁿ • y` form a Jacobi family
(`New.OddPart.IsJacobiFamily`) at a level `M` (for `x` killed by `M`: `σ J(x) = J(a x)` if `σ` acts
on `μ_M` by `a`; `J x` is a unit at places prime to `p` and has order `floorDiff c x` at `B`), and
`commutatorLog (l ^ n) γ (y x) g` is the exponent `t` with `γ y(x) / (g γ g⁻¹) y(x) = ζᵗ`, for the
fixed primitive `lⁿ`-th root of unity `ζ`.


### `nsmul_galUnitsRep_sub_eq_zero_of_isJacobiFamily`

 Let `lⁿ • y` be a Jacobi family at level `M`. If `σ` raises the `M`-th roots of unity to the
power `a`, then `σ (y x) / y (a x)` is an `lⁿ`-th root of unity, for every `x` killed by `M`. 

### `rootPowHom_commutatorLog_of_isJacobiFamily`

 Let `lⁿ • y` be a Jacobi family at level `M` and let `x` be killed by `M`. Then `commutatorLog`
names the root of unity `γ y(x) / (g γ g⁻¹) y(x)`: its image under `rootPowHom Ω (l ^ n)` is this
quotient. 

### `sum_commutatorLog_add_ofZMod_eq_of_isJacobiFamily`

 The distribution relation for the exponents. Let `lⁿ • y` be a Jacobi family at level `M` and
let `r ∣ M` be a prime with `r ≡ 1 mod c`. Then, for every `x` killed by `M`, the exponents
`commutatorLog (l ^ n) γ (y ·) g` at the translates `x + b / r` sum to the exponent at `r x`. 

### `derivativeSum_commutatorLog_eq_of_isJacobiFamily`

 Let `lⁿ • y` be a Jacobi family at level `M`, with `N lⁿ ∣ M`, and let every prime of `I` divide
`M` and be `≡ 1 mod c N lⁿ`. For `S ⊆ I`, the derivative sum `derivativeSum e ψ L S d` of the
exponents `x ↦ commutatorLog (l ^ n) γ (y x) g` does not depend on the shifts `d` (the sum at
`q ∈ S` carries the weights `L q u - d q`). 

### `nsmul_floorDiff_mul_sub_commutatorLog_eq_of_isFrob`

 Let `lⁿ • y` be a Jacobi family at level `M` with `lⁿ ∣ M`, and let `g` lie in the inertia group
(`IsFrob A 1 g`) of a place `A` prime to `l`, fix the `M`-th roots of unity and have `g r / r = ζᵇ`.
If `y x ^ lⁿ` is a unit at `A` times `r ^ (lⁿ floorDiff c x)` for every `x` killed by `M`, then
`commutatorLog (l ^ n) γ (y x) g = (a floorDiff c x - floorDiff c (a x)) b` for such `x`, where `γ`
raises the `M`-th roots of unity to the power `a`. 

### `cyclotomicPowDirichlet_sub_one_smul_sum_eq_zero_of_isJacobiFamily`

 The relation for the character sum. Let `B` lie above `p ≡ 1 mod N lⁿ`, and let `lⁿ • y` be a
Jacobi family at level `N lⁿ` for `p`, `B` and `c`. If the derivative sum over no primes of the
exponents `x ↦ commutatorLog (l ^ n) γ (y x) τ` vanishes for every `τ` in the inertia group of `B`,
then `(Υ γ - 1) ∑ floorDiff c (a / N lⁿ) aᵉ ψ(a) = 0` in `O/lⁿ`, where `Υ = cyc^(e+1) ψ` and `a`
runs over the units mod `N lⁿ`. 

### `derivativeSum_commutatorLog_mul_eq_of_isJacobiFamily`

 The cocycle rule. Let `lⁿ • y` be a Jacobi family at level `M`, with `N lⁿ ∣ M`, and let every
prime of `I` divide `M` and be `≡ 1 mod c N lⁿ`. Write `Λ h` for `derivativeSum e ψ L I 0` of the
exponents `x ↦ commutatorLog (l ^ n) γ (y x) h`. Then `Λ (g g') = Λ g + Υ(g) Λ g'` for
`Υ = cyc^(e+1) ψ`. 

### `derivativeSum_commutatorLog_self_eq_zero_of_isJacobiFamily`

 The cocycles vanish at `γ`. Let `lⁿ • y` be a Jacobi family at level `M`, with `N lⁿ ∣ M` and
every prime of `I` dividing `M`. As `γ γ γ⁻¹ = γ`, every exponent `commutatorLog (l ^ n) γ (y x) γ`
is zero, and so is their derivative sum. 

### `derivativeSum_commutatorLog_mem_vanishingCocycles_of_isJacobiFamily`

 The cocycles at the level `M = N lⁿ ∏_{r ∈ I} r`, when `lⁿ • y` is a Jacobi family at level `M`
and the primes of `I` are `≡ 1 mod c N lⁿ`: `g ↦ derivativeSum e ψ L I 0 F_g`, where `F_g x` is the
exponent `commutatorLog (l ^ n) γ (y x) g`, is a locally constant cocycle for `Υ = cyc^(e+1) ψ` that
vanishes on inertia over `ℚ(ζ_N)` at the places above neither `l`, `p` nor a prime of `I`. 

### `sum_mul_commutatorLog_eq_of_isJacobiFamily`

 Frobenius and inertia for the exponents at one `x` killed by `M`: for a Frobenius `φ` at a place
`A` above `q` and `τ` in the inertia group of `A` whose cyclotomic character mod `q M` fixes the
`M`-torsion and sends `v u / q` to `u / q` (where `L q v = 1`), the exponents of `y (x + u/q)`
at `τ`, weighted by `L q u`, sum to the exponent of `y (q x)` at `φ`. Here `lⁿ ∣ M`, `q` is prime
to `M`, `q ≡ 1 mod c`, `p ≡ 1 mod q`, and `lⁿ • y` is a Jacobi family at levels `M` and `q M`. 

### `exists_mem_inertiaGroup_derivativeSum_insert_eq_of_isJacobiFamily`

 Frobenius and inertia for the derivative sums, at the level `M = N lⁿ ∏_{r ∈ I} r`: for a prime
`q ∉ I`, a place `A` above `q` and a Frobenius `φ` at `A`, some `τ` in the inertia group of `A` has
`Λ (I ∪ {q}) τ = Λ I φ`, with `Λ S h = derivativeSum e ψ L S 0 (commutatorLog (l ^ n) γ (y ·) h)`.
Here `p ≡ 1` mod `M` and mod `q`, `lⁿ • y` is a Jacobi family at every level `M' ∣ p - 1`, `q` and
the primes of `I` are `≡ 1 mod c N lⁿ`, and `L q v = 1` for some `v`. 

### `exists_isKolyvaginSystem`

 Kolyvagin's cocycles. Let `l` be a prime, `O` a `ℤ_l`-algebra, `ψ` a Dirichlet character mod
`N ≠ 0` with values in `O`, and `Υ = cyc^(e+1) ψ` (`New.cyclotomicPowDirichlet`) the character of
`Gal(ℚ̄/ℚ)` with `cyc` the `l`-adic cyclotomic character. Let `γ ∈ Gal(ℚ̄/ℚ)`, let `P` be a finite
set of primes `≡ 1 mod c N lⁿ`, and let `B` be a place of `ℚ̄` above a prime `p ≡ 1 mod N lⁿ ∏ P`.
Then there are maps `κ S` from `Gal(ℚ̄/ℚ)` to `O/lⁿ` (`QuotSpan (l ^ n : O)`), one for each finite
set `S` of primes, with two properties.
* They form a Kolyvagin system (`New.OddPart.IsKolyvaginSystem`). For `S ⊆ P`, `κ S` is a locally
  constant `Υ`-cocycle, is unramified over `ℚ(ζ_N)` away from `l`, `p` and `S`, and vanishes at
  `γ`. For `q ∈ P ∖ S`, the value of `κ S` at a Frobenius at a place `A` above `q` is a value of
  `κ (S ∪ {q})` on the inertia group of `A`.
* If `κ ∅` vanishes on the inertia group of `B`, then `Υ γ - 1` kills the twisted Stickelberger
  sum `∑ₐ m(a / N lⁿ) aᵉ ψ(a)` in `O/lⁿ`. Here `a` runs over the units mod `N lⁿ`, read as integers
  in `[0, N lⁿ)`; `ofZMod M a` is `a / M` in `ℚ/ℤ`; and `m(x) = ⌊c ⟨x⟩⌋ - ⌊c ⟨-x⟩⌋`
  (`New.OddPart.floorDiff c x`), where `⟨x⟩` is the representative of `x` in `[0, 1)`. 
