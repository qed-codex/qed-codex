---
{
  "module": "src/Lib/GaloisRep/Main/SplitCase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SplitCase.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SplitCase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Attached Galois representations in odd rank: the split case

This file proves that eigenforms on the definite space `New.stdSpace` of odd rank have attached
Galois representations in the split case. Here `E` is a CM field containing a primitive 5040th
root of unity and `ℚ(√−D)`, with `D ≡ 3 mod 4`. The spherical place `u` and the places above `ℓ`
lie over split primes of `ℚ(√−D)`. The proof is an ℓ-adic limit argument. For it, the file
constructs places apart from given places and levels of a given type at a split place.

## Main definitions and results

* `New.GaloisRep.sphericalCompat_of_split`: in odd rank, eigenforms have attached Galois
  representations compatible at a spherical place `u`, when `u` and the places above `ℓ` lie over
  split primes of `ℚ(√−D)`. The eigenvalues of f are ℓ-adic limits of combinations of eigenvalues
  of forms that satisfy the hypotheses of `New.GaloisRep.exists_rep_of_cuspidal_type`. The limit of
  the traces of their representations is the trace of a representation attached to f
  (`New.GaloisRep.Attached`), and the local properties at `u` pass to the limit.
* `New.GaloisRep.exists_isTypeLevel`: Let `v` and `x` be split places with `v` apart from `x` and
  its conjugate, `H` an open subgroup, and `ϑ` a character of the matrices `≡ 1` modulo `v` that is
  trivial on those `≡ 1` modulo `v ^ 2`. Then there is a level of type `ϑ` at `v` that lies in `H`
  away from `v` and `x`.

Notions from other files:
* `New.IsEigenform`: f ≠ 0, and almost all places w of prime norm are split and f has the Hecke
  polynomial P w at w.
* `New.GaloisRep.Attached` P r i: r is continuous with non-degenerate trace form, i (by default the
  identity) is an open map to Gal(Ω/E), and at most Frobenius elements the characteristic
  polynomials of r are ℓ-adically close to those given by P.
* `New.InducesPlacePair` w τ: the place of E that the ℓ-adic embedding belonging to the infinite
  place τ induces is w or its conjugate.
* `New.GaloisRep.IsSplitPrimeToDisc` u: the place u of ℚ(√−D) contains some (1 + √−D)/2 − b
  (b an integer) that is coprime to its conjugate; in particular u is split.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank` for sources.


### `New.GaloisRep.IsPlaceApart`

 The finite place `x` of `E` is induced by the `ℓ`-adic embedding `θ`, lies over the same split
place of `QuadField D` as `z`, and is apart from `y` and `u` up to conjugation. The infinite place
of the complex embedding `ιℓ⁻¹ ∘ θ` of `E` induces `x` or its conjugate, and induces neither `u` nor
its conjugate (`New.InducesPlacePair`). 

### `New.GaloisRep.IsPlaceApart.placeOfEmb_eq`

 The restriction of `θ` to `E` induces `x`. 

### `New.GaloisRep.IsPlaceApart.inducesPlacePair`

 The infinite place of `ιℓ⁻¹ ∘ θ` induces `x` or its conjugate. 

### `New.GaloisRep.IsPlaceApart.not_inducesPlacePair`

 The infinite place of `ιℓ⁻¹ ∘ θ` induces neither `u` nor its conjugate. 

### `New.GaloisRep.IsPlaceApart.isSplitPrimeToDisc`

 The place of `QuadField D` below `x` is split and prime to `D`. 

### `New.GaloisRep.IsPlaceApart.below_eq`

 The places `x` and `z` lie over the same place of `QuadField D`. 

### `New.GaloisRep.IsPlaceApart.ne_left`

 The place `x` is not `y`. 

### `New.GaloisRep.IsPlaceApart.star_ne_left`

 The conjugate of `x` is not `y`. 

### `New.GaloisRep.IsPlaceApart.ne_right`

 The place `x` is not `u`. 

### `New.GaloisRep.IsPlaceApart.star_ne_right`

 The conjugate of `x` is not `u`. 

### `New.GaloisRep.exists_place_apart`

 Let `z` lie above `ℓ` and over a split place of `QuadField D`, and let `y` and `u` be any places
of `E`. Over the place below `z` there is a place `x`, induced by an `ℓ`-adic embedding `θ`, that
is apart from `y` and `u` up to conjugation (`New.GaloisRep.IsPlaceApart`). 

### `New.HasHeckePolyAt.coeff_pred_mem`

 If `ιℓ` takes the values of a nonzero `f` into a field `L`, it does so with the coefficient
`a - 1` of a Hecke polynomial `Q` of `f`: the eigenvalues are sums of values divided by a
nonzero value. 

### `New.GaloisRep.exists_attached_of_isApproximatingMonoid`

 Let the continuous `r i` have characteristic polynomials `Q i` at most Frobenius elements. Let
the monoid `N` of an approximation (`New.IsApproximatingMonoid`: on it the first component is the
uniform limit of the combinations, with coefficients `t`, of the others) contain the pairs formed
by the coefficients of `P` and of the `Q i`, with the sign changed. If `P` is monic of degree `a`
and these coefficients of `P` in degree `a - 1` lie in a complete set, some `R` is attached to `P`,
and the pairs of the traces of `R` and of the `r i` lie in `N`. 

### `New.padicModel_one_ne_zero`

 The `ℓ`-adic model `padicModel κ κ 1 f` of a nonzero `f` (from weight `κ` to itself, with matrix
`1`; applying `weylRep κ` at the `ℓ`-adic components of `g` to it gives back `ιℓ ∘ f g`) is
nonzero. 

### `New.HasNoSmallRelations.const_add_mul`

 A free family of integers (`New.HasNoSmallRelations`: for small `d`, two choices of `d` entries
with repetition that have the same sum coincide) stays free when it is multiplied by `ε ≠ 0` and
shifted by `c`. 

### `New.HasNoSmallRelations.exists_mem_jumps`

 Let `κ_h` be the entries of the weight `κ` at the infinite place of `σ`. If the `a` integers
`-∑_{j < h < a} (κ_h + 1)`, for `j < a`, form a free family (`New.HasNoSmallRelations`), then the
jumps of `κ` at `σ` contain a free family of `a` integers. 

### `New.GaloisRep.exists_isLevel_of_localCongruence_hom`

 Let `v` be a split place, `V` an open subgroup, and `ϑ` a character of the matrices `≡ 1`
modulo `v` that is trivial on those `≡ 1` modulo `v ^ 2`. There are a level `K` and a character
`χ` of `K`, trivial near `1`, such that an integral point that is `1` at `v` lies in `K` exactly
when it lies in `V`, and is then killed by `χ`, while the matrices `≡ 1` modulo `v`, placed at `v`,
lie in `K` and `χ` is `ϑ` on them. 

### `New.GaloisRep.isCompatibleAt_of_isApproximatingMonoid`

 Let `N` be a closed monoid of pairs `(x, φ)` such that `∑ i, t η i * φ (η, i)` tends to `x`
uniformly on `N` as `η → 0`. Let `ρ` and the `r i` be continuous, let `ρ` have a non-degenerate
trace form, and let `N` contain the pairs of traces of `ρ` and of the `r i`. Let each `r i` be
spherical above `u` (good, with the jumps of `κ`, and `ιℓ (Q i)` kills geometric Frobenii), with
`Q i` of degree `a` if `u` is split. For each Hecke polynomial `X` of `f ≠ 0` at `u`, let `N`
contain a nonzero multiple of each pair of coefficients of `X` and the `Q i`. Then `ρ` is compatible
with `f` at every place `A` over `u` (`IsCompatibleAt`: unramified or crystalline, with the jumps of
`κ`, and `ιℓ X` kills geometric Frobenii). 

### `New.GaloisRep.exists_inf_trivialOn_le_offPartComap`

 Let `x` be a split place and `H` an open subgroup. There is a finite set `S` of places such that
the integral points trivial at `S` have their part off `x` (the point times the inverse of its
component at `x`, placed at `x`) in `H`. It avoids `x` and its conjugate, and also `w` and its
conjugate when `w` is apart from them and `H` contains `maxCompactAt _ w`. 

### `New.GaloisRep.IsTypeLevel`

 The level `K` with its character `χ` has the type `ϑ` at the split place `v`, lies in `H` away
from `v` and `x`, and is spherical off the finite set `U`, which contains `v` and avoids `x`. 

### `New.GaloisRep.IsTypeLevel.isLevel`

 The subgroup `K` is open and consists of integral points. 

### `New.GaloisRep.IsTypeLevel.eventuallyEq_one`

 The character `χ` is trivial near `1`. 

### `New.GaloisRep.IsTypeLevel.exists_eq_ofSplitPlace`

 The matrices `≡ 1` modulo `v`, placed at `v`, lie in `K`, and `χ` is `ϑ` on them. 

### `New.GaloisRep.IsTypeLevel.mem_of_atPlace_eq_one`

 An element of `K` that is `1` at `v` and at `x` lies in `H` and is killed by `χ`. 

### `New.GaloisRep.IsTypeLevel.exists_mem_of_trivialOn`

 The integral points trivial at `U` lie in `K` and are killed by `χ`. 

### `New.GaloisRep.IsTypeLevel.mem`

 The place `v` is in `U`. 

### `New.GaloisRep.IsTypeLevel.notMem`

 The place `x` is not in `U`. 

### `New.GaloisRep.IsTypeLevel.star_notMem`

 The conjugate of `x` is not in `U`. 

### `New.GaloisRep.IsTypeLevel.notMem_of_maxCompactAt_le`

 A place `w` apart from `v`, `x` and their conjugates, at which `H` contains the integral
  points, is off `U` with its conjugate. 

### `New.GaloisRep.exists_isTypeLevel`

 Let `v` and `x` be split places with `v` apart from `x` and its conjugate, `H` an open subgroup,
and `ϑ` a character of the matrices `≡ 1` modulo `v` that is trivial on those `≡ 1` modulo `v ^ 2`.
Then there is a level of type `ϑ` at `v` that lies in `H` away from `v` and `x`. 

### `New.GaloisRep.IsTypeLevel.levelSpace_le_span`

 For a level `K` with character `χ` that is spherical off `U`, the forms of type `χ` and weight
`μ` are spanned by those that are Hecke eigenforms off `U` (`New.IsSphericalOff`). 

### `New.GaloisRep.exists_rep_of_free_weight`

 Let `a` be odd, and let `v` and `x` lie over the split place of `QuadField D` below `z`, apart
from `u` and from each other. Let `u` lie over a split place of `QuadField D` prime to `D`, and let
`u = z` if `u` is above `ℓ`. Let the level `K` with character `χ` have the cuspidal type `ϑ` at `v`,
and let the form `g` of type `χ` and weight `μ` have Hecke polynomials `Q` off `U`. Let `μ` agree
with `κ` at the infinite places that induce `u` or its conjugate and be free at the others (the
integers `-∑_{j < h < a} (μ_h + 1)` satisfy `New.HasNoSmallRelations`). Then a continuous
representation has characteristic polynomials `Q` at most Frobenius elements and, if `u` and its
conjugate are off `U`, satisfies the spherical clause at `u` with the jumps of `κ`. 

### `New.GaloisRep.exists_attached_of_coeff_mem`

 Let `f` be an eigenform with polynomials `P`, and let the continuous `r i` have characteristic
polynomials `Q i` at most Frobenius elements. Let the monoid `N` of an approximation contain, at
each split place `w` prime to `ℓ` with `w` and its conjugate off `U`, the pairs formed by the
coefficients of the Hecke polynomial of `f` and of the `Q i w`, with the sign changed. Then some `R`
is attached to `P`, and the pairs of the traces of `R` and of the `r i` lie in `N`. 

### `New.GaloisRep.sphericalCompat_of_split`

 Let `E` be a CM field containing a primitive 5040th root of unity and `ℚ(√−D)`, with
`D ≡ 3 mod 4`, and let `a` be odd. Suppose `u` and every place above `ℓ` lie over primes of `ℚ(√−D)`
that split (`New.GaloisRep.IsSplitPrimeToDisc`). Then every eigenform of any weight on the standard
definite unitary group of rank `a` has an attached Galois representation. If the form is spherical
at `u`, every representation attached to its Hecke polynomials satisfies the local conditions
`IsCompatibleAt` at every place of `Ω` over `u` (`New.GaloisRep.SphericalCompat`): it is good there,
has the jumps of the weight and, if `u` is split, the Hecke polynomial kills geometric Frobenius. 
