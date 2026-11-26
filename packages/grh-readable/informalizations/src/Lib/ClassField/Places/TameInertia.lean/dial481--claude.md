---
{
  "module": "src/Lib/ClassField/Places/TameInertia.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/TameInertia.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/TameInertia.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tame inertia, Frobenius on roots of unity over ℚ_p, the cyclotomic character, Weil pairs

This file studies how inertia and Frobenius elements act on roots of unity and on roots of a
uniformiser over a henselian local field, and in particular over `ℚ_p`. Over `ℚ_ℓ`, with `G_ℓ`
(`New.Gp ℓ`) its absolute Galois group, a Frobenius for `q` raises roots of unity of order prime to
`ℓ` to the `q`-th power, and inertia fixes them. For Weil pairs, degrees add under products and are
determined by the Galois element.

## Main definitions and results

* `New.Cohomology.exists_inertia_smul_eq_of_orbit_subset`,
  `New.IsLocalGalois.exists_inertia_smul_eq_of_pow_eq`: inertia is transitive on the roots of an
  Eisenstein polynomial, in particular on the `n`-th roots of `π`.
* `New.IsLocalGalois.tame_inertia`: the tame theorem. Characters of inertia of order prime to the
  residue characteristic are governed by the action on an `n`-th root `y` of a uniformiser `π`.
  Its three parts are `New.IsLocalGalois.stabilizer_le_ker_of_pow_eq_one`,
  `New.IsLocalGalois.exists_map_eq_pow_of_isPrimitiveRoot` and
  `New.IsLocalGalois.map_conj_eq_pow_of_isFrob`.
* `New.Selmer.apply_eq_pow_of_isFrob`: a Frobenius for `q` (`New.IsFrob`) raises a root of unity of
  order prime to `ℓ` to the `q`-th power.
* `New.Selmer.exists_inertia_cyclotomicGp_eq`: every natural number prime to `p` is a value of the
  `p`-adic cyclotomic character on inertia. Inertia permutes the primitive `p ^ (k + 1)`-th roots of
  unity transitively, and `New.Selmer.exists_cyclotomicGp_eq_of_isClosed` passes to the limit by
  compactness.
* `New.Period.IsWeilPair.eq_pow_of_isFrob`: for a homomorphism `j` from a group `Γ` to the absolute
  Galois group of `ℚ_p` and a Weil pair `(j s, m)`, the element `j s` determines `p ^ m`.

Notions from other files:
* `New.IsLocalGalois`: Γ = Gal(Ω/k), with Ω algebraically closed of characteristic 0, stabilises A,
  and A ∩ k is a discrete valuation ring with finite residue field. So k is a henselian local field.
* `New.IsUniformiser`: `π` is a uniformiser of `K` for `A`: an element of `K` lies in the maximal
  ideal of `A` exactly when its valuation is at most that of `π`.
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.

## Relation to the literature

Known; see `Lib.ClassField.Places.LocalFields` for sources.



## Tame characters of inertia and roots of a uniformiser

`A` is a valuation ring of the algebraically closed field `Ω`; `A x` means `A.valuation x`, and
`valuationVia k A π` is `A` of the image of `π` in `Ω`, and `A.valuation` is written
multiplicatively: value `1` means a unit of `A`, value below `1` the maximal ideal.


 ### Inertia and roots of order prime to the residue characteristic 

### `valuation_smul_div_sub_one_lt_one`

 For `s` in inertia and a unit `w` of `A`, `s • w / w ≡ 1` modulo the maximal ideal. 

### `inertia_fixes_root_of_unit`

 Let `s` lie in the inertia group of `A` and let `n` be a unit of `A`. If `w ^ n = u` is a unit
of `A` fixed by `s`, then `s` fixes `w`. 

### `ne_zero_of_tame_root`

 If `n` is a unit of `A` and `y ^ n = π`, then `y ≠ 0` and `n ≠ 0`. 

### `smul_root_eq_ratio_mul`

 Let `n` be a unit of `A`, that is, prime to the residue characteristic, and `y ^ n = π`
(the section hypotheses `hn`, `hy`). An element `s` of inertia (`hs`) multiplies all `n`-th roots
of `π` by the same `s • y / y`. 

### `inertia_pow_smul_div`

 Let `s` lie in the inertia group of `A` (`hs`), `n` be a unit of `A` (`hn`) and `y ^ n = π`
with `π` in `kˣ` (`hy`). Then `s ^ i • y / y = (s • y / y) ^ i` for every natural number `i`. 

 ### Transitivity of inertia on roots of a uniformiser 

### `IsLocalGalois.exists_valuation_pow_inertia_index`

 For `y ≠ 0` whose orbit under inertia has `m` elements (the index of its stabiliser), the
valuation of `y ^ m` is an integral power of that of the uniformiser `π` (the section hypothesis
`hπ : IsUniformiser A π`). 

### `Cohomology.exists_inertia_smul_eq_of_orbit_subset`

 Eisenstein's criterion over the fixed field of inertia: if `x ^ n` has the valuation of the
uniformiser `π` (the section hypothesis `hπ`) and the inertia orbit of `x` lies in a set `T` of at
most `n` elements, then every `y` in `T` is `g • x` for some `g` in inertia. 

### `IsLocalGalois.exists_inertia_smul_eq_of_pow_eq`

 Let `Γ` be the Galois group of `Ω / k`, where `Ω` is algebraically closed of characteristic 0,
`Γ` stabilises the valuation subring `A`, and `A ∩ k` is a discrete valuation ring with finite
residue field (`IsLocalGalois`), and let `π` be a uniformiser of `k` for `A`. For `n > 0`, if
`x ^ n = π` and `y ^ n = x ^ n`, then some element `g` of the inertia group of `A` satisfies
`g • x = y`, so inertia acts transitively on the `n`-th roots of `π`.

This is the surjectivity in the structure theorem for tame inertia, at each finite level `n > 0`, in
characteristic 0. 

### `IsLocalGalois.stabilizer_le_ker_of_pow_eq`

 Let `f` be a homomorphism on inertia with open kernel of index dividing `n ^ M`, with
`f g ^ n = 1` for all `g`; let `n` be a unit of `A` and `y₁ ^ (n ^ M * n) = π` for the
uniformiser `π` (the section hypothesis `hπ`). Then every element of inertia that fixes `y₁` lies
in the kernel of `f`. 

 ### The tame theorem 

### `IsFrob.conj_mem_inertiaGroup`

 A `q`-Frobenius normalises inertia: it stabilises `A`, so it conjugates inertia into itself. 

### `map_eq_pow_of_smul_div_eq`

 If `f` is trivial on the stabiliser of `y` in inertia (where `y ^ n = π`), then `f g = f s ^ i`
whenever `g` moves `y` by the `i`-th power of the ratio by which `s` moves it. 

### `IsLocalGalois.stabilizer_le_ker_of_pow_eq_one`

 First part of the tame theorem. Let `k` be a local field (`New.IsLocalGalois Γ k A`), `π` a
uniformiser of `k`, `n` a unit of `A` and `y ^ n = π`. A homomorphism `f` on inertia with open
kernel and `f g ^ n = 1` for all `g` is trivial on the stabiliser of `y` in inertia, so `f g`
depends only on `g y / y`. 

### `IsLocalGalois.exists_map_eq_pow_of_isPrimitiveRoot`

 Second part of the tame theorem. Assume `IsLocalGalois Γ k A`: `Γ` is the Galois group of an
algebraically closed field `Ω` of characteristic 0 over `k`, it stabilises the valuation subring
`A`, and `A ∩ k` is a discrete valuation ring with finite residue field. Let `π` be a uniformiser of
`k` for `A`, `n` a natural number that is a unit of `A`, `y ^ n = π`, and `f` a monoid homomorphism
on the inertia group of `A` with open kernel and `f g ^ n = 1` for all `g`. If `s` is in inertia and
`s • y / y` is a primitive `n`-th root of unity, then every value `f g` is a power `f s ^ i`. 

### `IsLocalGalois.map_conj_eq_pow_of_isFrob`

 Third part of the tame theorem. Assume `IsLocalGalois Γ k A`: `Γ` is the Galois group of an
algebraically closed field `Ω` of characteristic 0 over `k`, it stabilises the valuation subring
`A`, and `A ∩ k` is a discrete valuation ring with finite residue field. Let `π` be a uniformiser of
`k` for `A`, `n` a natural number that is a unit of `A`, `y ^ n = π`, and `f` a monoid homomorphism
on the inertia group of `A` with open kernel and `f g ^ n = 1` for all `g`. If `s` is in inertia and
`φ` is a `q`-Frobenius (it stabilises `A` and `φ • x ≡ x ^ q` modulo the maximal ideal for all
`x ∈ A`), then `φ s φ⁻¹` is in inertia and `f (φ s φ⁻¹) = f s ^ q`. 

### `IsLocalGalois.tame_inertia`

 The tame theorem. Let `k` be a local field (the section instance `IsLocalGalois Γ k A`), `n` be
a unit of `A`, `y ^ n = π` a uniformiser of `k`, and `f` a homomorphism on inertia with open kernel
and `f g ^ n = 1` for all `g`. Then (a) `f` is trivial on the stabiliser of `y`, so `f g` depends
only on `g y / y`; and for `s` in inertia, (b) if `s y / y` is a primitive `n`-th root of unity,
every `f g` is a power of `f s`; (c) if `φ` is a `q`-Frobenius, `φ s φ⁻¹` is in inertia and
`f (φ s φ⁻¹) = f s ^ q`. The three parts are `New.IsLocalGalois.stabilizer_le_ker_of_pow_eq_one`,
`New.IsLocalGalois.exists_map_eq_pow_of_isPrimitiveRoot` and
`New.IsLocalGalois.map_conj_eq_pow_of_isFrob`.

Here `hπ`, `hn` and `hy` are the section hypotheses. The theorem treats one `n` at a time and does
not construct the map onto the inverse limit of roots of unity.

This is a finite-level form of the structure of tame inertia (Serre, Local Fields, IV §2), stated
for homomorphisms with open kernel that are killed by `n`. 


## Roots of unity of order prime to ℓ over ℚ_ℓ

`G_ℓ` (`New.Gp ℓ`) is the absolute Galois group of `ℚ_ℓ`, and `New.intQpBar ℓ` is the valuation ring
of the algebraic closure of `ℚ_ℓ`; `intQpBar ℓ x` is the valuation of `x` for this ring.


### `isUniformiser_ell`

 `ℓ` is a uniformiser of `ℚ_ℓ` for the valuation ring `intQpBar ℓ` of `ℚ̄_ℓ`: an element of `ℚ_ℓ`
has valuation below `1` exactly when its valuation is at most that of `ℓ`. 

### `valuation_natCast_eq_one`

 A natural number prime to `ℓ` is a unit of the valuation ring of `ℚ̄_ℓ`. 

### `apply_eq_pow_of_isFrob`

 Let `φ` in `G_ℓ` be a Frobenius for `q` in the sense of `New.IsFrob`. Then `φ` sends every
`M`-th root of unity `z` to `z ^ q`, provided `M` is prime to `ℓ`. 

### `exists_apply_eq_pow`

 Every element `g` of `G_ℓ` raises an `M`-th root of unity `z`, with `M` prime to `ℓ`, to some
power `ℓ ^ n`. 


## The p-adic cyclotomic character on inertia

`[ThePrime p]` fixes `p` as a prime; `New.cyclotomicGp` is the `p`-adic cyclotomic character of
`Gal(ℚ̄_p/ℚ_p)` and `New.inertiaGroup _ (New.intQpBar p)` its inertia group.


### `exists_cyclotomicGp_eq_of_isClosed`

 Let `S ⊆ G_p` be closed and `a` a natural number. If for every `k` each primitive
`p ^ (k + 1)`-th root of unity `ζ` is sent to `ζ ^ a` by some element of `S`, then the `p`-adic
cyclotomic character `cyclotomicGp` takes the value `a` at some `g ∈ S`. 

### `exists_inertia_cyclotomicGp_eq`

 Every natural number `a` prime to `p` is the value of the `p`-adic cyclotomic character at some
element of the inertia group of `G_p`; that is, the extension of `ℚ_p` by all `p`-power roots of
unity is totally ramified. 


## Weil pairs: products, powers and uniqueness of the degree

`New.Period.IsWeilPair s m` says that `s` in the absolute Galois group of `ℚ_p` acts on the residue
field of `ℚ̄_p` as `x ↦ x ^ (1 / p ^ m)`. The lemmas concern elements `j s`, where `j` is a
homomorphism from a group `Γ` to this Galois group.


### `mul`

 Weil pairs multiply: the degrees add. 

### `pow`

 If `(j s, m)` is a Weil pair, then so is `(j (s ^ n), n * m)`. 

### `eq_pow_of_isFrob`

 If `(j s, m)` is a Weil pair and `(j s)⁻¹` acts on the residue field as `x ↦ x ^ q`, then
`q = p ^ m`. 


## Inertia and roots of unity of order prime to p

Over `ℚ_p`, inertia fixes the roots of unity of order prime to `p`
(`New.Selmer.apply_eq_self_of_mem_inertiaGroup`). For `f ≠ 0` the natural number `p ^ f - 1` is such
an order: it is nonzero (a `NeZero` instance) and prime to `p` (`New.Selmer.not_dvd_pow_sub_one`).


### `apply_eq_self_of_mem_inertiaGroup`

 Every element of the inertia group of `ℚ̄_p` over `ℚ_p` fixes the `f`-th roots of unity in
`ℚ̄_p`, for `f` prime to `p`. 

### `not_dvd_pow_sub_one`

 For `f ≠ 0`, the prime `p` does not divide `p ^ f - 1`. 
