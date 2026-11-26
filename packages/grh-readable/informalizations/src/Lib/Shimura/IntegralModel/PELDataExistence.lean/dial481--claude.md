---
{
  "module": "src/Lib/Shimura/IntegralModel/PELDataExistence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/PELDataExistence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/IntegralModel/PELDataExistence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence of PEL data at levels good at all safe places, with the form ξ and a Lagrangian

PEL data (`New.PEL`) are the arithmetic input of the moduli problem; this file constructs them.

* `New.Variety.exists_lagrangian`: an isotropic set lies in a self-annihilating subgroup.
* `New.Variety.IsSafeGoodPEL`: PEL data of given rank, level and `β`, good at all safe places.
* `New.Variety.exists_pel`: PEL data of any nonzero rank at every nonzero level divisible by some
  `N` that lies in none of the places of a given finite set `B`, good at all safe places.

Conventions: `CMBase E` is a CM type `Φ` together with a base place `v₀`; `Φ v` is the embedding the
CM type picks at `v`, `ψf` the standard character of the finite adeles, `xiForm ξ x y = ξ yᴴ x`,
`Ô E` the integral finite adeles, and `torsionClass` the quotient map onto
`AdelicTorsion E (Fin n)`, whose kernel is the vectors with entries in `Ô E`.

Notions from other files:
* `New.HasPrimitiveRoot5040`: `E` contains a primitive root of unity of order `7! = 5040`.
* `New.Variety.IsSafe 𝔑 w` (for `ℚ(√−d)` in `E`): the place u of ℚ(√−d) below w contains some
  (1 + √−d)/2 − b, b ∈ ℤ, that is coprime to its conjugate, and 𝔑 lies neither in w nor in any place
  above ū.

## Relation to the literature

Known; see `Lib.Shimura.IntegralModel.TowerExistence` for sources.


### `exists_lagrangian`

 Existence of Lagrangians. For an alternating bimultiplicative pairing `e` on an abelian
group, every isotropic set lies in a subgroup equal to its own annihilator. 

### `eventually_hasPadding`

 For every integer `c` of the CM field `E`, all large enough natural numbers `r` admit a padding
of `c` (`New.Variety.HasPadding E r c`). A padding is a choice of `r - 3` integers `aₗ` of `E` that
span `𝓞 E` over `ℤ` and satisfy `r = c̄ c + 3 + ∑ₗ āₗ aₗ` in `𝓞 E`, where the bar is complex
conjugation. 

### `exists_star_eq_neg_and_im_pos`

 For `s ≠ 0` there is a purely imaginary `ξ` in the inverse different of `E`, with positive
imaginary parts under the CM type, that generates the inverse different at the primes of `s`. 

### `exists_cmBase_restrict_ne`

 For an embedding `σ` of `E ⊇ QuadField d`, some CM type picks `σ` at its base place and, at
every other place, an embedding whose restriction to `QuadField d` differs from that of `σ`. 

### `mapRingHom_algebraMap_eq`

 On integers, the map `𝓞 (QuadField d) → 𝓞 E` induced by the inclusion is the algebra map. 

### `pel_good_of_safe`

 PEL data with `β = (1 + √-d) / 2` are good at a place `w` that is safe for their level
(`New.Variety.IsSafe`) and contains neither `D.paddedNorm` nor the order of `D.dualTorsion`. 

### `ψf_xiForm_eq_one_of_torsionClass_eq_zero`

 If `ξ` lies in the inverse different, the `r`-torsion vectors are isotropic for the pairing
`ψf (r ^ 2 ξ yᴴ x)`. 

### `coprime_card_of_le_torsionBySet`

 A group of torsion vectors killed by `(s c - 1) (s + 1) ^ 2` has order prime to `s`. 

### `exists_lagrangian_xiForm`

 Let `ξ` be purely imaginary (`star ξ = -ξ`) and lie in the inverse different, and let `r : ℕ`.
The pairing `ψf (r ^ 2 ξ yᴴ x)` on `Fin n → 𝔸f E` is alternating and the `r`-torsion vectors are
isotropic for it, so they lie in a subgroup `Λ` that is its own annihilator. 

### `dualOfIntegral`

 The vectors `x` that pair trivially with every integral vector under `ψf (ξ zᴴ x)`: the dual of
the integral vectors for this pairing. 

### `map_dualOfIntegral_le_torsionBySet`

 Let `m` lie in the different of `E` with `m ξ = s c - 1`. Then `(s c - 1) r ^ 2` kills the image
in `AdelicTorsion E (Fin n)` of the dual of the integral vectors for `ψf (r ^ 2 ξ zᴴ x)`. 

### `re_Φ_eq_zero_of_star_eq_neg`

 A purely imaginary `ξ` (`star ξ = -ξ`) has real part `0` under every embedding `Φ v` of the
CM type. 

### `conjugate_comp_eq_of_comp_ne`

 If `Φ v` and `Φ v₀` restrict to different embeddings of `QuadField d`, the two restrictions
are complex conjugate. 

### `natCast_notMem_of_coprime`

 A finite place `w` whose norm divides `s` does not contain a natural number `N` prime to `s`:
otherwise `N` and the norm of `w`, which lies in `w`, would be coprime elements of `w`. 

### `IsSafeGoodPEL`

 PEL data `D` as `exists_pel` supplies them at the level `𝔑`: rank `n`, level `𝔑`,
`β = (1 + √-d) / 2`, and good reduction (`New.PEL.IsGoodAt`) at every place `w` that is safe for
`𝔑` (`New.Variety.IsSafe 𝔑 w`). 

### `IsSafeGoodPEL.rank_eq`

 The data have rank `n`. 

### `IsSafeGoodPEL.level_eq`

 The data have level `𝔑`. 

### `IsSafeGoodPEL.beta_eq`

 The element `β` of the data is the image of `(1 + √-d) / 2`. 

### `IsSafeGoodPEL.isGoodAt_of_isSafe`

 The data are good at every place that is safe for the level. 

### `exists_forall_dvd_exists_isSafeGoodPEL`

 Let the CM type of `E` pick, at every infinite place `v ≠ v₀`, an embedding whose restriction to
`QuadField d` differs from that of `Φ v₀`. Then for a finite set `B` of places some `N ≠ 0` lies in
no place of `B`, and every nonzero level `𝔑` divisible by `N` carries PEL data of rank `n` that are
good at every place safe for `𝔑` (`IsSafeGoodPEL`). 

### `exists_pel`

 Existence of PEL data. Let `d % 4 = 3`, let the CM field `E ⊇ QuadField d = ℚ(√-d)` satisfy
`HasPrimitiveRoot5040 E`, let `n ≠ 0`, `σ` an embedding `E →+* ℂ`, `B` a finite set of places. Some
CM type `Ψ` has `Ψ.Φ Ψ.v₀ = σ` and `Ψ.Φ v ≠ Ψ.Φ Ψ.v₀` on `QuadField d` for `v ≠ Ψ.v₀`, and some
`N ≠ 0` in no place of `B` is such that every nonzero level `𝔑` divisible by `N` carries PEL data as
in `IsSafeGoodPEL`: rank `n`, `β = (1 + √-d) / 2`, good at every place safe for `𝔑`. 
