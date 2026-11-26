---
{
  "module": "src/Lib/GaloisRep/Hilbert90/TameActions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Hilbert90/TameActions.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Hilbert90/TameActions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hilbert 90 for GL_n and units under tame actions on Artinian, finite or profinite rings

This file gives versions of Hilbert's theorem 90, with congruence conditions, for a ring
endomorphism `σ` of finite order of a finite, Artinian or profinite ring. It proves Hilbert 90 for
`GL n` and for units at level `m`, and the surjectivity of the norm onto fixed units `≡ 1 mod m`.
`New.IsTameAtLevel σ p m` means: `σ ^ p = 1` with `0 < p`, `σ m = m`, some element has trace `1`
modulo `m`, and no `σ ^ i` with `0 < i < p` is trivial modulo a prime not containing `m`.
`New.IsProfiniteRing R` means: every sequence `x` has a unique `L` with `x N ≡ L` modulo each
natural number `M ≠ 0`, for `N` in a set of the hyperfilter.
`New.twistedNorm τ p δ` is the twisted norm `δ · τ δ ⋯ τ^(p-1) δ` of `δ` in a monoid.

## Main definitions and results

* `New.IsTameAtLevel.hilbert90_gl`, `New.IsTameAtLevel.hilbert90_unit`: a cocycle `≡ 1 mod m` is a
  coboundary of an element `≡ 1 mod m`, for `GL n` and for units.
* `New.IsTameAtLevel.exists_prod_range_pow_apply_eq`: a fixed unit `≡ 1 mod m` is the norm of a unit
  `≡ 1 mod m`.
* `New.IsProfiniteRing.exists_algHom_semiconj`, `New.IsProfiniteRing.finite_quotient_natCast`,
  `New.isTameAtLevel_quotientNatMap`, bundled in
  `New.IsTameAtLevel.exists_algHom_semiconj_quotientNatMap`: a limit map from the finite quotients
  `R ⧸ (N !)` reduces the profinite case to the finite one.

## Relation to the literature

Known result: Hilbert 90 for GL_n and norm surjectivity on units, cyclic action, congruence level.
This is done over Artinian, finite or profinite rings, where the action need only be free away from
an invariant element m and have an element of trace one modulo m. Cocycles, coboundaries and units
are congruent to 1 modulo m. Source: A. Speiser 1919;
J.-P. Serre, Corps locaux, 1962, Ch. X §1 Prop. 3 and Ch. V §2; S. Chase, D. Harrison, A. Rosenberg,
Galois theory and Galois cohomology of commutative rings, Mem. AMS 52, 1965; for the norm on O[γ],
P. Scholze, The Langlands-Kottwitz approach for some simple Shimura varieties, 2013, Lemma 2.2.


 ### The five conditions of a tame action 

### `IsTameAtLevel.exists_dvd_sum_sub_one`

 For a tame action at level `m`, some `e` has trace `∑ i < p, (σ ^ i) e` congruent to `1`
modulo `m`. 

### `IsTameAtLevel.mem_of_forall_sub_mem`

 No inertia away from the level: if `0 < i < p` and `σ ^ i` is the identity modulo a prime `P`,
then `m ∈ P`. 

 ### Norms, traces and examples of tame actions 

### `map_prod_range_eq_self_of_periodic`

 If `τ` sends each `a i` to `a (i + 1)` and `a p = a 0`, then `τ` fixes the product of the
`a i` with `i < p`. 

### `fixed_sum`

 If `τ` sends each `a i` to `a (i + 1)` and `a p = a 0`, then `τ` fixes
the sum of the `a i` with `i < p`. 

### `iterate_mul_apply`

 For a ring endomorphism `σ` of `R`, an element `m` and `p : ℕ`, the `p`-th iterate of
`y ↦ m * σ y` sends `x` to the norm `∏ i < p, (σ ^ i) m` times `(σ ^ p) x`. 

### `isTameAtLevel_gal`

 If Gal(L/K) is finite, every K-automorphism σ of the field L is tame (`New.IsTameAtLevel`) at
level 1, with exponent the order of σ. 

### `IsTameAtLevel.of_sq_eq_one_of_isUnit_sub`

 If a ring endomorphism `σ` of a commutative ring `R` has `σ ^ 2 = 1`, some `x - σ x` is a unit,
and `σ m = m`, then `σ` acts tamely (`New.IsTameAtLevel`) at level `m` with exponent `2`. 

 ### Profinite rings 

### `isProfiniteRing_intAdeles`

 The ring of integral finite adeles of a number field E satisfies the profiniteness condition
`New.IsProfiniteRing`. 

### `IsProfiniteRing.of_retract`

 If `R` is profinite (`New.IsProfiniteRing`) and `B` is an additive retract of `R`, through
additive maps `i : B → R` and `r : R → B` with `r (i x) = x`, then `B` is profinite. 

### `IsProfiniteRing.of_addEquiv_pi`

 If `R` is profinite (`New.IsProfiniteRing`), so is every ring `B` that is isomorphic as an
additive group to `n → R`, through `coords`, for a finite type `n`. 

### `IsProfiniteRing.eqLocus`

 If `R` is profinite (`New.IsProfiniteRing`) and `σ` is tame at level `0`, so that `σ ^ p = 1`
and some element of `R` has trace `1`, then the subring `σ.eqLocus 1` of elements fixed by `σ` is
profinite. 

 ### Passing to finite quotients and descent at a prime 

### `IsTameAtLevel.of_semiconj`

 Tameness passes along a ring homomorphism `f : R →+* B` that intertwines `σ` with an
endomorphism `θ` of `B`, provided `θ ^ p = 1`; the level becomes `f m`. 

### `quotientNatMap`

 The ring endomorphism of `R ⧸ (N)` induced by `σ`, for a natural number `N`. 

### `IsProfiniteRing.exists_algHom_semiconj`

 Let `R` be profinite (`New.IsProfiniteRing`) and `σ` a ring endomorphism of `R`. Some
`R`-algebra map `Λ` from the families of residues modulo `N !` to `R` carries the maps
`quotientNatMap σ (N !)` to `σ`. 

### `IsProfiniteRing.finite_quotient_natCast`

 Each quotient `R ⧸ (N)` of a profinite ring `R` by a natural number `N ≠ 0` is finite. 

### `isTameAtLevel_quotientNatMap`

 If `σ` is tame at level `m`, the map `quotientNatMap σ N` it induces on `R ⧸ (N)` is tame at
the residue of `m`. 

### `IsTameAtLevel.exists_algHom_semiconj_quotientNatMap`

 Let `R` be profinite (`New.IsProfiniteRing`) and `σ` tame at level `m`. Then some
`R`-algebra map `Λ` from the families of residues modulo `N !` to `R` carries the maps
`quotientNatMap σ (N !)` to `σ`, and each quotient `R ⧸ (N !)` is finite, with
`quotientNatMap σ (N !)` tame at the residue of `m`. 

### `IsTameAtLevel.exists_smul_mem_span_fixedPoints`

 Galois descent at a prime. Let `σ` be tame at level `m`, meaning `σ m = m`, `σ ^ p = 1` with
`0 < p`, some `e` has `∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime ideal modulo
which `σ ^ i` is the identity contains `m`. If `τ` is a `σ`-semilinear map on `V` with `τ^[p] = id`
and `P` is a prime not containing `m`, then some `r ∉ P` multiplies `V` into the span of the vectors
fixed by `τ`. 

 ### Hilbert 90 and norms at level `m` 

### `IsTameAtLevel.exists_fixed_separating`

 Let `R` be Artinian, `σ` tame at level `m`, `d ≡ 1 mod m`, and let the ideal `M` contain every
`(σ ^ i) d`. Then some `σ`-fixed multiple `N` of `m` is `≡ 1 mod M` and lies in each prime that
does not contain `d`. 

### `IsTameAtLevel.exists_fixed_det_notMem`

 Let `σ` be tame at level `m`: `σ m = m`, `σ ^ p = 1` with `0 < p`, some `e` has trace
`∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime modulo which `σ ^ i` is the identity
contains `m`. Let `τ v = c * σ v` be a `σ`-semilinear map of period `p` on `n × n` matrices over
`R`, and let `P` be a prime not containing `m`. Then some `τ`-fixed matrix has determinant outside
`P`. 

### `IsTameAtLevel.exists_fixed_eq_one_add_smul`

 Let `σ` be tame at level `m`: `σ m = m`, `σ ^ p = 1` with `0 < p`, some `e` has trace
`∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime modulo which `σ ^ i` is the identity
contains `m`. Let `τ v = c * σ v` be a `σ`-semilinear map on `n × n` matrices over `R`, where
`c = 1 + m • Y` and `τ^[p]` is the identity. Then some `τ`-fixed matrix is `≡ 1 mod m`, that is, of
the form `1 + m • W`. 

### `IsTameAtLevel.hilbert90_gl_of_isArtinianRing`

 Hilbert 90 for `GL n` at level `m` over an Artinian ring `R`, the main case of
`New.IsTameAtLevel.hilbert90_gl`. Let `σ` be tame at level `m`, meaning `σ m = m`, `σ ^ p = 1` with
`0 < p`, some `e` has `∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime ideal modulo
which `σ ^ i` is the identity contains `m`. If `c = 1 + m • Y` is invertible with
`c · σ c ⋯ σ^(p-1) c = 1` (`σ` applied entrywise), then `c · σ k = k` for an invertible
`k = 1 + m • W`. 

### `IsTameAtLevel.hilbert90_gl`

 Hilbert 90 for `GL n` at level `m`. Let `R` be Artinian or profinite, and let `σ` be tame at
level `m`, meaning `σ m = m`, `σ ^ p = 1` with `0 < p`, some `e` has `∑ i < p, (σ ^ i) e ≡ 1 mod m`,
and for `0 < i < p` every prime ideal modulo which `σ ^ i` is the identity contains `m`. If
`c = 1 + m • Y` is invertible with `c · σ c ⋯ σ^(p-1) c = 1` (`σ` applied entrywise), then
`c = k · (σ k)⁻¹`, written `c · σ k = k`, for an invertible `k = 1 + m • W`. 

### `IsTameAtLevel.hilbert90_unit`

 Hilbert 90 for units at level `m`: let the commutative ring `R` be Artinian or profinite
(`IsProfiniteRing`: every sequence has a unique limit along the hyperfilter for the topology of the
ideals `(M)`). Let `σ` be tame at level `m` (`IsTameAtLevel σ p m`: `σ m = m`, `0 < p`, `σ ^ p = 1`,
some `e` has trace `∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime ideal modulo
which `σ ^ i` is the identity contains `m`). Then every unit `x ≡ 1 mod m` of norm
`x · σ x ⋯ σ^(p-1) x = 1` is `g / σ g`, i.e. `x * σ g = g`, for a unit `g ≡ 1 mod m`. 

### `IsTameAtLevel.exists_norm_of_finite`

 The case of `New.IsTameAtLevel.exists_prod_range_pow_apply_eq` where `R` is finite. Let `σ` be
tame at level `m`, meaning `σ m = m`, `σ ^ p = 1` with `0 < p`, some `e` has
`∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime ideal modulo which `σ ^ i` is the
identity contains `m`. Then every `σ`-fixed unit `x ≡ 1 mod m` is the norm `∏ i < p, (σ ^ i) z` of a
unit `z` with `z ≡ 1 mod m` and `z⁻¹ ≡ 1 mod m`. 

### `IsTameAtLevel.exists_prod_range_pow_apply_eq`

 Norms for a tame action at level `m`, meaning that `σ m = m`, `σ ^ p = 1` with `0 < p`, some `e`
has trace `∑ i < p, (σ ^ i) e ≡ 1 mod m`, and for `0 < i < p` every prime modulo which `σ ^ i` is
the identity contains `m`. If the commutative ring `R` is finite or profinite, every `σ`-fixed unit
`x ≡ 1 mod m` is the norm `z · σ z ⋯ σ^(p-1) z` of a unit `z` with `z ≡ 1` and `z⁻¹ ≡ 1 mod m`. 
