---
{
  "module": "src/Lib/Cyclotomic/Kolyvagin/ReciprocityComponentBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Kolyvagin/ReciprocityComponentBounds.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Kolyvagin/ReciprocityComponentBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reciprocity laws and Stickelberger and Kolyvagin bounds for odd-part cocycles

The file studies cocycles on `Gal(Ω/ℚ)`, with `Ω` an algebraic closure of ℚ. Here
`New.cyclotomicPowDirichlet l e ψ` is `cyc^e ψ` with `cyc` the `l`-adic cyclotomic character. The
module `New.OddPart.component l e ψ ν` consists of the cocycles for `(cyc^e ψ)⁻¹` with values in
`O / l^ν`, where `O` (`PadicIntegerRing O l`) is the integer ring of a finite extension of ℚ_l, that
satisfy three conditions. They are unramified off `l` over ℚ(μ_N), split at `l` over ℚ(μ_{N l^∞})
and zero at `New.cmConj`, a complex conjugation. Reciprocity laws at primes `q ≡ 1` relate the value
of one cocycle at a Frobenius element to the ramification of another. Using these laws and
Chebotarev's theorem, the file bounds these components in two ways. One bound is an annihilation
result analogous to Stickelberger's theorem. The other uses Kolyvagin's descent with the Euler
system of Gauss sums.

## Main definitions and results

* `New.OddPart.artin_reciprocity_of_mem_component`: Artin reciprocity over ℚ(μ_{N m}), where the
  prime q ≡ 1 splits completely, pairs a cocycle `x` with a number `y`; only the places above q
  contribute.
* `New.OddPart.reciprocity_mod_ell`: the same law modulo `l` for a cocycle κ for cyc^(e+1) ψ; if
  `2 (a ^ e - 1) x φ ≠ 0`, then κ vanishes on the inertia group of `B`.
* `New.OddPart.nsmul_component_eq_zero`: if `X` has the Stickelberger property
  (`New.OddPart.IsStickelbergerBound N e X`), `cyc^e ψ` is odd and `e ≠ 0`, then `4 X²` kills
  `New.OddPart.component l e ψ ν` (an analogue of Stickelberger's theorem).
* `New.OddPart.exists_detecting_points_component`: for large `l`, a cocycle in
  `New.OddPart.component l e ψ ν` is determined by its values at `v_l(X) + 1` elements (Kolyvagin's
  descent with the Euler system of Gauss sums).

Notions from other files:
* `New.cyclotomicPowDirichlet l e ψ`: the character `cyc^e ψ` of `Gal(Ω/ℚ)` with values in `Oˣ`; the
  Dirichlet character `ψ` is read through the action on the `N`-th roots of unity.
* `New.OddPart.vanishingCocycles χ M s`: the `O`-module of locally constant maps `x : Gal(Ω/ℚ) → M`
  with `x (g h) = x g + χ(g) x h` (cocycles for `χ`) that vanish on `s`.
* `New.IsFrob A q σ`: `σ` stabilises the place `A` and `σ • x ≡ x ^ q` modulo its maximal ideal for
  all `x ∈ A`.
* `New.ordRat K A`: the order `Ωˣ → ℚ` at the place `A`, normalised to be `1` on uniformisers of
  `K`. `New.cyclotomicCharMod Ω n` gives the action on the `n`-th roots of unity, in `(ℤ/n)ˣ`.

## Relation to the literature

Known result: Stickelberger annihilation and the Kolyvagin–Rubin bound for odd twisted components.
Here the value is taken at a negative integer instead of at zero, and for an integer X whose
multiples (a^(e+1) − 1) X, for a ≡ 1 mod N, are congruent modulo each m prime to a to 2w times the
Stickelberger sum at level N m, and which for each prime ℓ is divisible by (a^e − 1)(a^(e+1) − 1)
for some such a prime to ℓ, 4X² kills the odd component at every prime. For large primes ℓ, at most
v_ℓ(X)+1 Galois elements detect its classes. Source: J. Coates, W. Sinnott, An analogue of
Stickelberger's theorem for the higher K-groups, Invent. Math. 24 (1974); K. Rubin, Euler Systems,
2000, III.4, Thm 4.6.



## Reciprocity laws for Galois cocycles and finiteness

Places are valuation subrings of `Ω`, and the group Ω^× is written additively. `New.cycloGalGroup N`
is the Galois group over ℚ(μ_N). The cocycles in `New.OddPart.component l e ψ ν` vanish at
`New.cmConj`. Over ℚ(μ_N) they also vanish on inertia at places prime to `l` and on
`New.Selmer.shaLocalSet` above `l`.


### `apply_mul_of_mem_vanishingCocycles`

 A map `z` in `vanishingCocycles χ M s` satisfies the cocycle rule
`z (g h) = z g + χ(g) z h`. 

### `isLocallyConstant_of_mem_vanishingCocycles`

 A map `z` in `vanishingCocycles χ M s` is locally constant. 

### `apply_eq_zero_of_mem_vanishingCocycles`

 A map `z` in `vanishingCocycles χ M s` vanishes on `s`. 

### `mem_decompGroup_of_isFrob`

 A Frobenius element `σ` at the place `A` lies in the decomposition group of `A`. 

### `mem_decompGroup_of_mem_inertiaGroup`

 The inertia group of the place `A` lies in its decomposition group. 

### `cyclotomicPowDirichlet_smul_eq_self`

 Let `g` fix the `N m`-th roots of unity (`g ∈ cycloGalGroup (N * m)`) and let `m • y = 0`.
Then `cyc^e ψ (g)` and its inverse fix `y`. 

### `openCocycleKer`

 The open subgroup `{g | z g = 0}` of zeros of a map `z` in `vanishingCocycles χ M s` (given by
`hz`): it is a subgroup by the cocycle rule, and open since `z` is locally constant. 

### `not_cycloGalGroup_le_openCocycleKer`

 Let `z` be in `vanishingCocycles χ M s`, with `z γ = 0` and `(χ γ - 1) • z ≠ 0`. Then `z` does
not vanish on the Galois group over ℚ(μ_f), for any `f ≠ 0`. 

### `finite_vanishingCocycles`

 Let `M` be finite, let ℚ(μ_{N l^n}) trivialise the action through `χ`, and let `s` contain
the inertia over ℚ(μ_N) at all non-trivial places prime to `l`. Then there are finitely many
locally constant cocycles for `χ` that vanish on `s`. 

### `exists_inertia_cyclotomicPowDirichlet_eq`

 Let `B` be a place of `Ω` above `l`, and let `a ≡ 1 mod N` be prime to `l`. Then some element
`i` of the inertia group of `B` has `cyc^e ψ (i) = a ^ e`. 

### `apply_eq_zero_of_mem_inertiaGroup_of_valuation_eq_one`

 A cocycle `x ∈ component l e ψ ν` vanishes at every `g` that fixes the `N m`-th roots of unity
and lies in the inertia group of a place `A` of `Ω` prime to `l`, above the place `t` of `ℚ`. 

### `pow_sub_one_smul_apply_eq_zero_of_mem_decompGroup`

 Let `x ∈ component l e ψ ν` be killed by `m`, let `A` be a place of `Ω` above `l`, and let
`a ≡ 1 mod N` be prime to `l`. Then `(a ^ e - 1) • x g = 0` for every `g` that fixes the `N m`-th
roots of unity and lies in the decomposition group of `A`. 

### `apply_conj_eq_smul_of_cyclotomicCharMod_eq`

 Let `x ∈ component l e ψ ν` be killed by `m`, let `φ` fix the `N m`-th roots of unity, and let
`σ` act on them by `u ∈ (ℤ/N m)ˣ`. Then `x (σ⁻¹ φ σ) = (u ^ e ψ(u)) • x φ`. 

### `two_smul_apply_eq_zero_of_mul_self_eq_one`

 Let `x ∈ component l e ψ ν` be killed by `m`, and let `σ` fix the `N m`-th roots of unity and
satisfy `σ * σ = 1`. Then `2 • x σ = 0`. 

### `injective_of_forall_isPlaceOver_inv_smul`

 Let `s u ∈ Gal(Ω/ℚ)` act on the `N m`-th roots of unity by `u ∈ (ℤ/N m)ˣ`, and let the
decomposition group of the place `B` fix them. If `w u` is a place of `ℚ(μ_{N m})` below
`(s u)⁻¹ • B` for each `u`, then the places `w u` are pairwise distinct. 

### `mem_range_of_valuation_lt_one`

 Let `v` be a place of `ℚ` such that every place of `Ω` at which `v.q` is not a unit lies over
`v`, and let `B` be such a place. Let `s u ∈ Gal(Ω/ℚ)` act on the `N m`-th roots of unity by `u`,
and let `w u` be a place of `ℚ(μ_{N m})` below `(s u)⁻¹ • B`. Then every place `t` of `ℚ(μ_{N m})`
at which `v.q` is not a unit is one of the `w u`. 

### `artin_reciprocity_of_mem_component`

 Artin reciprocity over `K = ℚ(μ_{N m})` at a prime `q ≡ 1 mod N m`, with `φ` a Frobenius at `B`
above `q`. The space `component l e ψ ν` consists of cocycles `Gal(Ω/ℚ) → O/l^ν` for `(cyc^e ψ)⁻¹`
under local conditions, including vanishing at `cmConj` and on inertia over `ℚ(μ_N)` away from `l`.
Let `x` in it be killed by `m`, and let `a ≡ 1 mod N` be prime to `l`. Let `y ∈ Kˣ` be, at each
place prime to `l q`, a unit times the `m`-th power of an element fixed by inertia, unless `x` kills
the decomposition group there. With `s u` acting on `μ_{N m}` by `u`, the orders `k u` of `s u • y`
at `B`, weighted by `u ^ e ψ(u)`, sum to a scalar killing `2 (a ^ e - 1) x φ`. 

### `exists_apply_eq_galUnitsRep_sub`

 Hilbert 90 for a cocycle read through `L : M →+ Ωˣ`. Let `κ` be a cocycle for `cyc^(e+1) ψ` with
values in `M`, killed by `l`. Then on the Galois group over ℚ(μ_{N l}) the map `g ↦ L (κ g)` is a
coboundary: `L (κ g) = g • r - r` for some `r ∈ Ωˣ` (the group `Ωˣ` is written additively). 

### `eq_zero_of_forall_smul_equivFun_symm_eq`

 Let `z` be an element of `M`, let `b` be a basis of `O ∙ z` over `ZMod l`, and let `j ∈ ZMod l`.
Suppose that for every unit `u` modulo `N l` the vector with coordinates `m i u * j` in the basis
`b`, scaled by `u ^ e ψ(u)`, is `z`. Suppose also that each weighted sum `∑_u m i u u ^ e ψ(u)`
kills a nonzero `c`, and that the totient of `N l` is a unit of `O`. Then `z = 0`. 

### `reciprocity_mod_ell`

 Reciprocity modulo `l`, when the totient of `N l` is a unit of `O`. The space
`component l e ψ ν` consists of cocycles `Gal(Ω/ℚ) → O/l^ν` for `(cyc^e ψ)⁻¹` under local
conditions, including vanishing at `cmConj` and on inertia over `ℚ(μ_N)` away from `l`. Let `φ` be a
Frobenius at `B` above a prime `q ≡ 1 mod N l`. Let `l` kill `x ∈ component l e ψ ν` and a cocycle
`κ` for `cyc ^ (e + 1) ψ` zero on `inertiaOff N l T`: the elements over `ℚ(μ_N)` in the inertia
group of a place above neither `l` nor a prime of `T`. Let each place prime to `q` lie above no
prime of `T`, or have its decomposition group killed by `x`. If `2 (a ^ e - 1) x φ ≠ 0` for some
`a ≡ 1 mod N` prime to `l`, then `κ` vanishes on the inertia group of `B`. 


## Stickelberger and Kolyvagin bounds for the components

The proofs of `New.OddPart.nsmul_component_eq_zero` and
`New.OddPart.exists_detecting_points_component` use Chebotarev's theorem
(`New.OddPart.exists_isFrob_notMem`) to find a Frobenius element at which a cocycle does not vanish.
They also use the reciprocity laws.


### `exists_isFrob_notMem`

 If neither of the open subgroups `U`, `V` contains the Galois group over `ℚ(ζ_m)`, then some
Frobenius element at a place above a prime `q ≡ 1 mod m` lies outside both. 

### `IsTrivialAbove`

 The function `x` on the Galois group vanishes on the decomposition group of every place above
the prime `r`. 

### `sum_range_eq_sum_units_add`

 The sum `∑ ⌊a x / (N lⁿ⁺¹)⌋ x ^ e ψ(x)` over `x < N lⁿ⁺¹` splits into its part over the units
modulo `N lⁿ⁺¹` and `l ^ e ψ(l)` times the same sum at level `N lⁿ`. 

### `sum_floorDiff_dvd`

 Let `O` be the integer ring of a finite extension of `ℚ_l` (`PadicIntegerRing O l`), and let `X`
have the Stickelberger property `IsStickelbergerBound N e X`: for `a ≡ 1 mod N`, for some `w` that
does not depend on `m`, `(a ^ (e + 1) - 1) X` is congruent modulo every `m` prime to `a` to `2 w`
times the Stickelberger sum at level `N m`. Let `cyc ^ e ψ` be odd (`hc`: its value at the complex
conjugation `cmConj` is `-1`), let `e ≠ 0`, and let `a ≡ 1 mod N` be prime to `l`. Then in
`O / lⁿ O` the sum of `floorDiff a (u / (N lⁿ)) u ^ e ψ(u)` over the units `u` modulo `N lⁿ` divides
`(a ^ (e + 1) - 1) X`. Here `floorDiff a t = ⌊a ⟨t⟩⌋ - ⌊a ⟨-t⟩⌋`, where `⟨t⟩ ∈ [0, 1)` represents
`t ∈ ℚ/ℤ`. The multiples of `l` give the Euler factor `1 - l ^ e ψ(l)`, a unit modulo `lⁿ`. 

### `nsmul_component_eq_zero`

 An analogue of Stickelberger's theorem. Let `X` have the Stickelberger property
`IsStickelbergerBound N e X` (a divisibility for each prime and a congruence for the Stickelberger
sums), let `cyc ^ e ψ` be odd (its value at the complex conjugation `cmConj` is `-1`), and let
`e ≠ 0`. Then `4 X²` kills every cocycle `z` in `component l e ψ ν`, the locally constant cocycles
`Gal(Ω/ℚ) → O/l^ν` for `(cyc ^ e ψ)⁻¹` that vanish at `cmConj` and at the elements of
`Gal(Ω/ℚ(μ_N))` lying in an inertia group at a place prime to `l` or in `shaLocalSet l ℚ 1`. 

### `isUnit_totient_mul`

 For `l > N` the number `φ (N l) = φ(N) (l - 1)` is a unit of `O`: both factors lie strictly
between `0` and `l`. 

### `exists_modEq_one_forall_isUnit_pow_sub_one`

 For `l > N` some `a ≡ 1 mod N` prime to `l` (a primitive root modulo `l`) makes `a ^ k - 1` a
unit of `O` for all `0 < k < l - 1`. 

### `exists_modEq_one_coprime_isUnit_pow_sub_one`

 For `e ≠ 0` and `l > N + e + 3`, the numbers `a ^ e - 1` and `a ^ (e + 1) - 1` are units of `O`
for some `a ≡ 1 mod N` prime to `l`. 

### `mem_cycloGalGroup_and_valuation_eq_one`

 Let `i` lie in the inertia group of a place `A` above a prime `r ≡ 1 mod N l`. Then `i` fixes
the `N`-th roots of unity, and `A` is not above `l`. The last clause repeats `hi`, so that the
conclusion has the form of the membership condition of `inertiaOff`. 

### `exists_isFrob_forall_isTrivialAbove`

 Let `O` be the integer ring of a finite extension of ℚ_l, `ψ` a Dirichlet character mod `N` with
values in `O`, and `component l e ψ ν` the locally constant cocycles for `(cyc ^ e ψ)⁻¹` on Gal(Ω/ℚ)
with values in `O / l ^ ν` that vanish at `cmConj` and at those elements of Gal(Ω/ℚ(μ_N)) lying in
an inertia group at a place prime to `l` or in `shaLocalSet l ℚ 1`. At a place `A` above a prime
`r ≡ 1 mod N l` (`A.valuation r < 1`) there is a Frobenius element `σ` with this property: every
cocycle `x` in `component l e ψ ν` that is killed by `l` and zero at `σ` is trivial above `r`
(`IsTrivialAbove x r`: it vanishes on the decomposition group of every place above `r`). 

### `exists_ne_zero_forall_isTrivialAbove`

 Suppose no `m` points detect the cocycles in `component`: for every `γ : Fin m → Gal(Ω/ℚ)` some
non-zero `x` in `component` vanishes at all `γ i`. Then for every set `T` of at most `m` primes
`≡ 1 mod N l` some non-zero `z` in `component`, killed by `l`, is trivial above every prime of `T`
(it vanishes on the decomposition groups of the places above them). 

### `mem_vanishingCocycles_of_mem_insert`

 Reciprocity modulo `l`. Let `a ≡ 1 mod N` be prime to `l`, with `2`, `φ (N l)` and `a ^ e - 1`
units of `O`. Let `z` in `component`, killed by `l`, be trivial above every prime of `T` but not
above a prime `r ≡ 1 mod N l`. Then a dual cocycle `y` for `cyc ^ (e + 1) ψ`, killed by `l`, that
vanishes on `inertiaOff N l (insert r T)`, vanishes on `inertiaOff N l T`. 

### `isUnit_natCast_of_pow_factorization_succ_dvd`

 Let `v_l(X) = X.factorization l`. If `l ^ (v_l(X) + 1)` divides `X ≠ 0` in `O`, then `l` is a
unit of `O`: it divides the part of `X` prime to `l`. 

### `finite_vanishingCocycles_inertiaOff_empty`

 There are finitely many cocycles for `cyc ^ e ψ` modulo `l ^ m` that are unramified off `l`
over `ℚ(ζ_N)`. 

### `not_cycloGalGroup_le_openCocycleKer_of_ne_zero`

 If `cyc ^ e ψ` is odd (value `-1` at `cmConj`) and `2` is a unit of `O`, a non-zero cocycle `z`
in `component` does not vanish on the Galois group over `ℚ(ζ_f)`, that is, this group does not lie
in the open subgroup `openCocycleKer hz` of zeros of `z`. The reason: `z` is zero at `cmConj`, where
the character of `z` has the value `-1`, and `-1 - 1 = -2` is a unit. 

### `exists_finset_forall_exists_isFrob`

 Let `cyc ^ e ψ` be odd (value `-1` at `cmConj`) and `2` a unit of `O`. There is a finite set `Q`
of primes `≡ 1 mod f` with this property. Let `y` be a cocycle for the dual character
`cyc ^ (e + 1) ψ` with values in `O / l ^ m`, unramified off `l` over `ℚ(ζ_N)` and not zero on the
Galois group over `ℚ(ζ_f)`, and let `z` be a non-zero cocycle in `component`. Then at some
Frobenius element `σ` at a place above a prime of `Q` neither `y` nor `z` vanishes. 

### `apply_eq_zero_of_mem_inertiaGroup`

 A cocycle unramified off `l` over `ℚ(ζ_N)` vanishes on inertia above a prime `≡ 1 mod N l`. 

### `IsTight`

 A finite set `T` of primes is tight at level `m` when its primes are `≡ 1 mod N l` and every
cocycle for the dual character `cyc ^ (e + 1) ψ` with values in `O / l ^ m` that is killed by `l`
and vanishes on `inertiaOff N l T` (unramified over `ℚ(ζ_N)` off `l` and `T`) also vanishes on
`inertiaOff N l ∅` (unramified off `l`). 

### `IsTight.mem_vanishingCocycles_of_nsmul_eq_zero`

 For a tight set `T`, a dual cocycle killed by `l` and unramified off `l` and `T` is unramified
off `l`. 

### `IsTight.insert`

 Reciprocity keeps a set tight. Let `a ≡ 1 mod N` be prime to `l`, with `2`, `φ (N l)` and
`a ^ e - 1` units of `O`. If `T` is tight and some `z` in `component`, killed by `l`, is trivial
above every prime of `T` but not above a prime `r ≡ 1 mod N l`, then `insert r T` is tight. 

### `nsmul_mem_vanishingCocycles_of_isTight`

 Kolyvagin's descent. Suppose no `m` points detect the cocycles in `component l e ψ ν`; let
`a ≡ 1 mod N` be prime to `l` with `2`, `φ (N l)`, `a ^ e - 1` units. Let `κ` be a Kolyvagin system
for `cyc ^ (e + 1) ψ` in `O / l ^ m` over the primes of `Q` (all `≡ 1 mod a N l ^ m`), with
auxiliary prime `p`, zero at `γ` (`cyc ^ (e + 1) ψ (γ) - 1` a unit), and `hQ_frob` supplying
detecting Frobenius elements. If `i ≤ m` and `S ⊆ Q` has at most `i` primes with `insert p S` tight,
`l ^ i • κ S` is unramified off `l`. 

### `exists_detecting_points_component`

 The Kolyvagin–Rubin bound, from the Euler system of Gauss sums. Let `X ≠ 0` satisfy
`IsStickelbergerBound N e X`, a divisibility for each prime plus a congruence for the Stickelberger
sums. Let `cyc ^ e ψ` be odd (value `-1` at `cmConj`), `e ≠ 0` and `l > N + e + 3`. Then there are
`v_l(X) + 1` elements `γ i` of the Galois group, where `v_l(X) = X.factorization l`, such that a
cocycle in `component l e ψ ν` vanishing at all of them is zero. That space consists of cocycles
`Gal(Ω/ℚ) → O/l^ν` for `(cyc^e ψ)⁻¹` under local conditions.

It is used instead of the Iwasawa main conjecture proved by Mazur and Wiles: for l > N + e + 3 it
bounds, at finite level, the number of Galois elements needed to detect the cocycles. 
