---
{
  "module": "src/Lib/GaloisRep/Hilbert90/UnitaryGroups.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Hilbert90/UnitaryGroups.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Hilbert90/UnitaryGroups.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hilbert 90 for unitary groups over profinite rings and for finite ideles

This file proves Hilbert 90 for the unitary group over a profinite ring, with a congruence modulo
`m`. On the way it constructs fixed units in `O[X]/Q`
(`New.exists_fixed_isUnit_pow_mul_one_add_mul_eq_pow`) and orthonormal frames fixed by `τ` for
invertible hermitian matrices (`New.exists_fixed_orthonormal_frame`). It also proves Hilbert 90 for
the finite ideles of `L`, for an automorphism `σ` of `L/K` acting through `New.adeleMap`. This
follows from Galois descent for the semilinear map `x ↦ u * σ x`, together with the fact that two of
its fixed points have a common divisor that is again fixed.

The main results `New.exists_fixed_orthonormal_frame` and `New.unitary_hilbert90_at_level` share
these hypotheses: `New.IsProfiniteRing O` (`O` is profinite); `New.IsTameAtLevel τ p 0`, which says
that `τ ^ p = 1`, `0 < p` and some element has trace `1`; `τ` commutes with `star` and fixes `c`,
and `c - star c` is a unit.

The lemmas before them concern the polynomial `X * (-w) ^ k`, for an inverse `w` of `1 + m X` modulo
`Q`, and endomorphisms of `O[X]/Q`; they state their own hypotheses.

## Main definitions and results

* `New.unitary_hilbert90_at_level`: Hilbert 90 for the unitary group, with a congruence modulo `m`.
* `New.hilbert90_finite_idele`: Hilbert 90 for the finite ideles, for an automorphism of `L/K`.

Notions from other files:
* `New.IsTameAtLevel σ p m`: `σ ^ p = 1` with `0 < p`, `σ m = m`, some element has trace `1` modulo
  `m`, and no `σ ^ i` with `0 < i < p` is trivial modulo a prime not containing `m`.
* `New.IsProfiniteRing R`: every sequence has a unique limit modulo each natural number `M ≠ 0`,
  along the hyperfilter.

## Relation to the literature

Known; see `Lib.GaloisRep.Hilbert90.TameActions` for sources.



## Hilbert 90 for unitary groups over profinite rings


### `exists_adjoinRoot_map_comp`

 Let `g` be a ring endomorphism of `O` and `s` a polynomial such that `Q` divides
`(Q.map g).comp s`. Then `q ↦ (q.map g).comp s` passes to a ring endomorphism `θ` of `O[X]/Q`. 

### `aeval_X_mul_neg_pow_eq_of_mul_one_add_smul_pow_eq`

 If `w` inverts `1 + m X` modulo `Q`, that is `a * Q + w * (1 + m X) = 1`, and `k ≤ 1`, then at
a root `B` of `Q` in an `O`-algebra `A`, any `C` with `C * (1 + m B) ^ k = (-1) ^ k * B` is the
value of `X * (-w) ^ k` at `B`. 

### `iterate_mk_eq_mk_map_pow`

 If `θ` acts on `O[X]/Q` by applying `τ` to the coefficients, then its `i`-th iterate applies
`τ ^ i`. 

### `isTameAtLevel_adjoinRoot_of_forall_mk_eq_mk_map`

 If `θ` acts on `O[X]/Q` by applying `τ` to the coefficients and `τ` is tame at level `x`
(`New.IsTameAtLevel`), then `θ` is tame at level `x`, viewed as a constant of `O[X]/Q`. 

### `dvd_map_comp_X_mul_neg_pow_of_charpoly_eq`

 Let `Q = charpoly Y`, let `w` invert `1 + m X` modulo `Q`, and let
`Yᴴ * (1 + m Y) ^ k = (-1) ^ k * Y` with `k ≤ 1`. Then `Q` divides `Q̄ ∘ (X * (-w) ^ k)`, where `Q̄`
applies `star` to the coefficients of `Q`: the value of `X * (-w) ^ k` at `Y` is `Yᴴ`, whose
characteristic polynomial is `Q̄`, and `charpoly Y` divides `(charpoly q(Y)).comp q` for every `q`.


### `commute_of_forall_mk_eq`

 In `O[X]/Q`, let `θ` apply `τ` to the coefficients, and let `ρ` apply `star` to the
coefficients and send `X` to `X * (-w) ^ k`, where `w` inverts `1 + m X` and `τ m = m`. If `τ`
commutes with `star`, then `θ` and `ρ` commute. 

### `sq_eq_one_of_forall_mk_eq`

 Let `ρ` apply `star` to the coefficients of `O[X]/Q` and send `X` to `X * (-w) ^ k`, where
`k ≤ 1`, `w` inverts `1 + m X` and `star m = m`. Then `ρ` is an involution. 

### `exists_fixed_isUnit_pow_mul_one_add_mul_eq_pow`

 Descent in the `θ`-fixed part of the profinite ring `O[X]/Q`, for `τ` tame at level `0` fixing
`c` (with `c - star c` a unit), `m` fixed by `τ` and `star`, and `k ≤ 1`. Here `θ` applies `τ` to
the coefficients, and the involution `ρ`, commuting with `θ`, applies `star` to them and sends `X`
to `X * (-w) ^ k`, where `w` inverts `1 + m X`. Some `θ`-fixed unit `g`, the class of
`1 + m X ^ (1 - k) y` with `y` fixed by `θ`, has `g ^ (1 - k) * (1 + m X) * ρ g = g ^ k`. 

### `IsTwistedRoot`

 The polynomials `y`, `z`, `z'` over `O` solve the norm equations of
`New.exists_isTwistedRoot_of_charpoly_eq` at an element `B` of an `O`-algebra `A` with `star`. Write
`T` for the value of `1 + m X ^ (1 - k) y` at `B`. 

### `IsTwistedRoot.aeval_map_eq`

 `y` and `τ y` have the same value at `B`. 

### `IsTwistedRoot.aeval_mul_eq_one`

 If `τ` is tame at level `m`, then `1 + m z'` is a left inverse of `1 + m z` at `B`. 

### `IsTwistedRoot.aeval_twistedNorm_eq`

 If `τ` is tame at level `m`, then `T` is the value of the twisted norm of `1 + m z`. 

### `IsTwistedRoot.pow_mul_star_eq_pow`

 If `B⋆ (1 + m B) ^ k = (-1) ^ k B`, then `T ^ (1 - k) (1 + m B) T⋆ = T ^ k`. 

### `exists_isTwistedRoot_of_charpoly_eq`

 Roots in `O[X]/Q`. Let `O` be profinite, let `τ` be tame at level `0` (`τ ^ p = 1`, `0 < p`,
and some element has trace `1`), commute with `star` and fix `c`, with `c - star c` a unit. Let `m`
be fixed by `τ` and `star`, let `1 + m Y` be invertible, with `Y` hermitian (`k = 0`) or with
`Yᴴ (1 + m Y) = -Y` (`k = 1`), and let `Q = charpoly Y` be fixed by `τ`. Then some polynomials
`y`, `z`, `z'` satisfy `New.IsTwistedRoot τ p m k B y z z'` at every root `B` of `Q` in an
`O`-algebra `A` with a compatible `star`. 

### `exists_fixed_orthonormal_frame`

 Orthonormal frame. Let `O` be profinite, let `τ` be tame at level `0` (`τ ^ p = 1`, `0 < p`,
and some element has trace `1`), commute with `star` and fix `c`, with `c - star c` a unit. Then an
invertible hermitian matrix `h` fixed by `τ` has an orthonormal frame fixed by `τ`: a matrix `g`
with `gᴴ h g = 1` and `g.map τ = g`, of the form `g = 1 + W (h - 1)`. 

### `unitary_hilbert90_at_level`

 Hilbert 90 for the unitary group `U 1` (matrices with `gᴴ g = 1`) at level `m`. Let `O` be
profinite, let `τ` be tame at level `0` and at level `m`, commute with `star` and fix `c`, with
`c - star c` a unit, and let `star m = m`. Tame at level `m` means: `τ m = m`, `τ ^ p = 1`, `0 < p`,
some `e` has `∑ i < p, τ^i e ≡ 1` mod `m`, and every prime modulo which some `τ^i` with `0 < i < p`
is the identity contains `m`. If the unitary `s` is `1 + m Y` and its twisted norm
`s · τ s ⋯ τ^{p-1} s` is `1` (`mapEnd hτ` applies `τ` to the entries), then `s · τ g = g`, that is
`s = g · (τ g)⁻¹`, for a unitary `g = 1 + m W`. 


## Hilbert 90 for finite ideles

`New.hilbert90_finite_idele` is Hilbert's Theorem 90 for the finite adeles of `L` and an
automorphism `σ` of `L/K`, acting through `New.adeleMap`. It follows from Galois descent for the
semilinear map `x ↦ u * σ x`, together with the fact that two of its fixed points have a common
divisor that is again fixed.


### `adeleMap_gal_pow`

 The `i`-th iterate of the action of `σ` on finite adeles is the action of `σ ^ i`. 

### `exists_dvd_dvd_mul_adeleMap_eq`

 Let `a` and `b` be finite adeles of `L` that solve `u * σ x = x`, where `σ` acts through
`New.adeleMap`. Then some solution `c` divides both: at each place take whichever of `a`, `b` has
the larger valuation. 

### `hilbert90_finite_idele`

 Hilbert's Theorem 90 for finite ideles. Let `σ ∈ Gal(L/K)` have order `n`, and let the finite
adele `u` of `L` have norm `∏_{i < n} σ ^ i u = 1`. Then `u * σ c = c` for some invertible finite
adele `c`. 
