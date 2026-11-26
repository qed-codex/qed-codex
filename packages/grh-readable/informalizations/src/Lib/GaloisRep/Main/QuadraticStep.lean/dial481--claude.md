---
{
  "module": "src/Lib/GaloisRep/Main/QuadraticStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/QuadraticStep.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/QuadraticStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Split places over ℚ(√−d) and quadratic steps with prescribed splitting

Let `K = ℚ(√-d)` (`New.QuadField` d, d ≡ 3 mod 4). For a CM field `E` containing `K`, we study the
places of `E` above split places of `K` prime to `d` (`New.GaloisRep.IsSplitPrimeToDisc`). For
stably unramified `E`, above each such place of `K` one can be chosen so that neither it nor its
conjugate equals one of two given places. We also construct a quadratic step `E'` over any stably
unramified CM field `E` (`New.HasPrimitiveRoot5040`: `E` contains a primitive 5040th root of unity).
The field `E'` contains `ℚ(√-D)` and has prescribed behaviour at the places over a given integer
`n`.

## Main definitions and results

* `New.GaloisRep.IsSplitPrimeToDisc.isSplit_of_below`: such a place differs from its complex
  conjugate.
* `New.GaloisRep.IsSplitPrimeToDisc.exists_place_above_ne`: if E satisfies
  `New.HasPrimitiveRoot5040`, each such place of K has a place of E above it such that neither it
  nor its conjugate equals one of two given places.
* `New.GaloisRep.exists_isQuadraticStep`, `New.GaloisRep.exists_isStep_hasQuadSubfield`: the step
  `E' = stepField χ`, for a character `χ` of `Gal(Ω/E)`, with the idele character of `χ`
  (`New.GaloisRep.IsQuadraticStep`).

Notions from other files:
* `New.GaloisRep.IsSplitPrimeToDisc`: The prime u of ℚ(√−d) contains an element x = (1 + √−d)/2 − b,
  b ∈ ℤ, that is coprime to its conjugate x̄.
* `New.IsStep`: A step `E'/E`: `E` is stably unramified, and `E'` is a CM field Galois over `E` of
  prime degree.
* `New.QZChar`: Continuous characters of a group with values in `New.QZ` = ℚ/ℤ; `QZ.mk r` is the
  class of `r : ℚ`, so `QZ.mk 2⁻¹` is `1 / 2`.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank` for sources.



## Places above split primes of ℚ(√−d)

`star w` is the complex conjugate of a place `w`, `New.FinPlace.q w` its norm and
`New.FinPlace.below w` the place below it; `w.IsSplit` says that `star w ≠ w`.


### `IsSplitPrimeToDisc.isSplit_of_below`

 A place `w` of `E` above a split place of `ℚ(√−d)` prime to `d`
(`New.GaloisRep.IsSplitPrimeToDisc`) is split: it differs from its complex conjugate. 

### `eventually_notMem_star_notMem`

 For a finite set S of finite places of the CM field E and a nonzero natural number ℓ, almost all
finite places w satisfy three conditions. Neither w nor its complex conjugate lies in S, and ℓ does
not lie in the prime ideal of w. 

### `IsSplitPrimeToDisc.exists_place_above_ne`

 Let E contain a primitive 5040th root of unity and contain K = ℚ(√−d), let u be a split place of
K prime to d (`New.GaloisRep.IsSplitPrimeToDisc`), and let a, b be places of E. Then some place v of
E lies above u such that neither v nor its conjugate equals a or b. 


## Existence of a quadratic step

`New.QZChar.stepField χ` is the field cut out by the character `symmetrise χ : g ↦ χ g + χ gᶜ`,
where `gᶜ` is the conjugate of `g` by complex conjugation `cmConj` on `Ω`, an algebraic closure of ℚ
into which `E` is embedded (`EmbeddedNumberField E`).


### `exists_norm_uniformiser`

 For `R ≠ 0` divisible by `4` and `n ≠ 0` there is `D ≡ -1 (mod R)` that is a norm `α * star α`
from `𝓞 E` and such that `-D` is a uniformiser at some place `P` prime to `n`. 

### `apply_sqrt_eq_or_eq_neg`

 If `c ^ 2` lies in `E`, then every `g ∈ Gal(Ω/E)` sends `c` to `c` or to `-c`. 

### `exists_qzChar_of_sq_eq`

 The quadratic character of `E(b)`, where `b ≠ 0` and `b ^ 2 ∈ E`: its value at `g` is `0` if
`g b = b` and `1 / 2` otherwise. 

### `apply_sqrt_eq_self_of_mem_pow`

 Local test: let `A` be a place of `Ω` over the place `w` of `E`. If `c ^ 2 = x` and
`1 - x * u ^ 2` lies in a power of `w` that does not contain `4`, then the decomposition group at
`A` fixes `c`. 

### `exists_real_twist`

 Gluing at the places over `n`: let `α * star α = D` with `D ≡ -1 (mod w ^ k)` for all `w ∣ n`.
Then there is a nonzero real `t` such that at every `w ∣ n` either `α * t` is the inverse of a
square modulo `w ^ k`, or `star w = w` and `w` is prime to `2 * α * t`. 

### `IsSplitPrimeToDisc.of_mem`

 A place of `ℚ(√-D)` that contains `(D + 1) / 4` is split and prime to `D`. 

### `inertiaGroup_le_decompGroup`

 The inertia group at a place `A` of `Ω` lies in the decomposition group at `A`. 

### `apply_eq_of_mem_inertiaGroup_of_sq_eq`

 Let `b ^ 2 = α * t`, and let `A` be a place of `Ω` over the place `w` of `E`, where `4 ∉ w ^ k`.
Suppose that `1 - α * t * u ^ 2 ∈ w ^ k` for some `u`, or that `star w = w`, `α * t ∉ w` and
`2 ∉ w`. Then the inertia group at `A` fixes `b`: by `apply_sqrt_eq_self_of_mem_pow` in the first
case, and because `b ^ 2` and `2` are units at `A` in the second. 

### `apply_eq_of_mem_decompGroup_of_sq_eq`

 Let `b ^ 2 = α * t`, and let `A` be a place of `Ω` over the place `w` of `E`, where `4 ∉ w ^ k`.
Suppose that `1 - α * t * u ^ 2 ∈ w ^ k` for some `u`, or that `star w = w`, `α * t ∉ w` and
`2 ∉ w`. If `w` is split (`star w ≠ w`), which excludes the second case, then the decomposition
group at `A` fixes `b`. 

### `sq_eq_neg_natCast_of_sq_eq_mul`

 Let `i * i = -1`, let `t ≠ 0` be real, let `α * star α = D`, and let `b ^ 2 = α * t` and
`cmConj b ^ 2 = star (α * t)`. Then `y = (i / t) * b * cmConj b` is a square root of `-D`. 

### `symmetrise_apply_eq_zero_iff`

 Let `χ` be the quadratic character of `E(b)` (`hχ`), where `b ≠ 0`, `b ^ 2 = x` and
`cmConj b ^ 2 = star x`, and let `c ≠ 0` in `E`. Then `symmetrise χ` vanishes at `g` exactly when
`g` fixes `c * b * cmConj b`: both say that `g` has the same sign on `b` and on `cmConj b`. 

### `exists_mul_mem_ker_symmetrise_inf_ker`

 Let `E` be a CM field and `χ` the character of `Gal(Ω/E)` that is `0` at the `g` with `g b = b`
and `1 / 2` elsewhere. Let `symmetrise χ` be `g ↦ χ g + χ gᶜ`, where `gᶜ` is the conjugate of `g` by
complex conjugation `cmConj` on `Ω`, an algebraic closure of ℚ into which `E` is embedded
(`EmbeddedNumberField E`). Let `P` be a finite place with `n ∉ P`, let `σ` lie in the inertia group
at `placeOver P` (a chosen place of `Ω` over `P`) with `symmetrise χ σ ≠ 0`, and let the subgroup
`H` contain the inertia groups at all places of `Ω` above finite places of `E` prime to `n` of norm
`q` at most that of `P`; then every `g` has some `h ∈ H` with `g * h` in the kernels of both
`symmetrise χ` and `χ`. 

### `four_notMem_pow_absNorm_span_four`

 Let `k` be the norm of the ideal `(4)`. No power `w ^ k` of a finite place `w` contains `4`:
else `N(w) ^ k` would divide the norm of `4`, whose absolute value is `k`, while
`N(w) ^ k ≥ 2 ^ k > k`. 

### `exists_mem_inertiaGroup_smul_eq_neg`

 Let `x ≠ 0` in `𝓞 E` be a uniformiser at the place `P`, and let `y ^ 2 = x`. Then some `σ` in
the inertia group at `placeOver P` (a place of `Ω` over `P`) sends `y` to `-y`. 

### `IsQuadraticStep`

 A `ℚ/ℤ`-valued character `χ` of `Gal(Ω/E)` and a natural number `D` form a quadratic step over
`E` for the integer `n`. Here `symmetrise χ` is `g ↦ χ g + χ gᶜ`, with `gᶜ` the conjugate of `g` by
complex conjugation, and `stepField χ`, the fixed field of its kernel, contains `ℚ(√-D)`. 

### `IsQuadraticStep.isStep`

 `stepField χ`, with the idele character of `χ`, is a step over `E`. 

### `IsQuadraticStep.exists_mul_mem_of_inertiaAbove_subset`

 For some `m`, every subgroup that contains the inertia groups at the places prime to `n` of
  norm at most `m` generates `Gal(Ω/E)` together with `ker (symmetrise χ) ⊓ ker χ`. 

### `IsQuadraticStep.isSplitPrimeToDisc_below`

 The places of `stepField χ` over `n` lie over split places of `QuadField D` prime to `D`. 

### `IsQuadraticStep.decompGroup_le_ker_symmetrise`

 At a place over `n`, the decomposition group fixes `stepField χ`. 

### `IsQuadraticStep.inertiaGroup_le_ker_inf`

 At a place over `n`, the inertia group fixes `stepField χ`, and `χ` vanishes on it. 

### `IsQuadraticStep.decompGroup_le_ker_inf_of_isSplit`

 At a split place over `n`, the same holds for the whole decomposition group. 

### `exists_isQuadraticStep`

 For `E` a CM field containing a primitive 5040th root of unity (`HasPrimitiveRoot5040 E`) and
`n ≠ 0`, there are a `ℚ/ℤ`-valued character `χ` of `Gal(Ω/E)` and `D ≡ 3 (mod 4)` with the following
properties. The field `stepField χ`, the fixed field of the kernel of `g ↦ χ g + χ gᶜ` (`gᶜ` is the
conjugate of `g` by complex conjugation), contains `ℚ(√-D)`. Moreover `χ` and `D` form a quadratic
step over `E` for `n` (`New.GaloisRep.IsQuadraticStep`): `stepField χ` is a step over `E` with
prescribed splitting and ramification at the places over `n`. 

### `exists_isStep_hasQuadSubfield`

 For `E` a CM field with `HasPrimitiveRoot5040 E` and `n ≠ 0` there are a character `χ` of
`G_E = Gal(Ω/E)` and `D ≡ 3 (mod 4)` such that `E' = stepField χ` contains `ℚ(√-D)` and has the
properties (a)–(d) below, where `U` is the kernel of `symmetrise χ` and `N = U ⊓ ker χ`;
`inertiaAbove S` holds the inertia groups at the places of `Ω` above places in `S`. These are the
fields of `New.GaloisRep.IsQuadraticStep`, written out. 
