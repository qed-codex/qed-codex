---
{
  "module": "src/Lib/PadicHodge/Kisin/Bicommutant.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/Bicommutant.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/Bicommutant.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The ring S_B of a chart and extension of S-linear maps of A_inf to B^+

This file works in B^+ = `BPlus` = A_max[1/p], where A_max = `Amax` has image `amaxImage` in B^+.
It defines the ring S_B of a chart, the elements of B^+ whose multiplication commutes with all
`S`-linear maps of B^+ that keep `amaxImage`. It shows that S_B is the closure of `S[E/p]` with `p`
inverted, and that every `S`-linear map of A_inf extends to an S_B-linear map of B^+ that keeps
`amaxImage`. Most identities for the extensions are checked on A_inf by a density principle: an
additive map of B^+ that keeps `amaxImage` and kills A_inf is zero
(`New.Lift.Chart.eq_zero_of_map_ainfToBPlus_eq_zero`). The file ends with results on divisibility
by `z` in B^+.

## Main definitions and results

* `New.Lift.Chart.bicommutant`: the ring S_B of the elements of B^+ whose multiplication commutes
  with all S-linear maps B^+ → B^+ that keep the image of A_max.
* `New.Lift.Chart.extendToBPlus`: an S-linear map of A_inf extends to an S_B-linear map of B^+
  keeping the image of A_max.

Notions from other files:
* `New.Period.Amax`: Colmez's period ring A_max, the p-adic completion of A_inf[X]/(pX − ξ).
* `New.Period.FrobGal`: The monoid ℕ × G_p; the pair (n, g) acts on A_inf as φ^n g.
* `New.Lift.Chart.S`: the ring `S`, the image in A_inf of the chart's map Λ[[X]] → A_inf.
* `New.Lift.Chart.E`: the image `E` in `S` of the series X^e A + p; it equals ξ times a unit.
* `New.Lift.Chart.adicBasis`: a chosen (p, z)-adic topological basis of A_inf over `S`, whose
  coordinate at `New.Lift.Chart.oneIndex` is the identity on `S`.

## Relation to the literature

Known; see `Lib.PadicHodge.Kisin.PeriodMatrixFrame` for sources.


 ### Preliminaries on B^+ 

### `eq_zero_of_p_pow_amaxImage`

 An element `y` of B^+ that is `p ^ n` times an element of `amaxImage` (the image of A_max)
for every `n` is zero. 

### `map_p_pow_mul`

 An additive map `G` of B^+ commutes with multiplication by `p ^ n`. 

### `smul_mem_amaxImage`

 Each `m` in `FrobGal` (acting as `φ ^ n g`) keeps `amaxImage`, the image of A_max. 

### `ainfToBPlus`

 The structure ring homomorphism from A_inf to B^+. 

### `theta_z_dvd_p`

 θ(z) divides p in O_C. 

### `theta_z_ne_zero`

 θ(z) is not zero, as it divides `p`. 

### `bicommutant`

 The ring S_B of the chart: the elements of `BPlus` whose multiplication commutes with every
`c.S`-linear map of `BPlus` that keeps `amaxImage`, the image of A_max. By
`adjoinEDivPClosure_eq_bicommutant` this is the closure of `S[E/p]` in `BPlus` with `p` inverted. 

### `mem_bicommutant_iff`

 An element `y` of B^+ lies in S_B = `c.bicommutant` if and only if multiplication by `y`
commutes with every `c.S`-linear map `G` of B^+ that keeps `amaxImage`. 

### `exists_extendToBPlus`

 Every `c.S`-linear map `f` from A_inf to itself extends along `ainfToBPlus` to a `c.S`-linear
map from B^+ to itself that keeps `amaxImage`, the image of A_max in B^+. Here `c.S` is the subring
of A_inf that is the image of the chart's map Λ⟦X⟧ → A_inf, and `BPlus` is B^+ = A_max[1/p], with
A_max the period ring `Amax`. 

### `extendToBPlus`

 For a `c.S`-linear map `f` of A_inf, a chosen `c.S`-linear extension of `f` to B^+ that
keeps `amaxImage`; it is even linear over S_B = `c.bicommutant`
(`New.Lift.Chart.extendToBPlus_mul`). 

### `extendToBPlus_ainfToBPlus`

 On the image of A_inf the extension of `f` is `f`. 

### `extendToBPlus_mul`

 Let `f` be a `c.S`-linear endomorphism of A_inf, and let `c.extendToBPlus f` be its chosen
`c.S`-linear extension to B^+ = A_max[1/p] that preserves the image of A_max. This extension is
linear over S_B = `c.bicommutant` (the elements of B^+ whose multiplication commutes with all such
maps): it commutes with multiplication by every `y` in S_B. 

### `extendedCoord`

 For a chart and an index `i`, the extension to B^+ of the coordinate
`c.adicBasis.coord i : Ainf → c.S` followed by the inclusion into A_inf, as a `c.S`-linear map
B^+ → B^+. 

 ### The density principle and membership in S_B 

### `eq_zero_of_map_ainfToBPlus_eq_zero`

 Density: an additive map `G` from B^+ to itself that keeps `amaxImage` (the image of A_max)
and vanishes on the image of A_inf is zero at every `y`. 

### `smul_extendToBPlus_mem_bicommutant`

 Let `m = (n, g)` in `FrobGal` act as `φ ^ n g`. If `m • f a` lies in `c.S` for every `a` in
A_inf, then `m • c.extendToBPlus f y` lies in S_B = `c.bicommutant` for every `y` in B^+. 

### `extendedCoord_mem_bicommutant`

 For each index `i`, take the coordinate `c.adicBasis.coord i : A_inf → c.S` of the chosen
topological basis of A_inf over `c.S`, and extend it `c.S`-linearly to
`c.extendedCoord i : B^+ → B^+`, where B^+ = A_max[1/p]. This extension takes all its values in
S_B = `c.bicommutant`, the set of elements of B^+ whose multiplication commutes with every
`c.S`-linear endomorphism of B^+ that preserves the image of A_max. 

### `mem_bicommutant_of_mul`

 If `v ≠ 0` and `v * u` lie in S_B = `c.bicommutant`, so does `u`. 

### `exists_bicommutant_mul_p_eq_one`

 The inverse of `p` in B^+ lies in S_B = `c.bicommutant`. 

 ### Coordinates, Frobenius and decompositions on S_B 

### `extendedCoord_oneIndex_eq_self`

 Let B^+ = A_max[1/p], and let S_B = `c.bicommutant` be the set of elements of B^+ whose
multiplication commutes with every `c.S`-linear endomorphism of B^+ that preserves the image of
A_max. The coordinate at `c.oneIndex` of the chosen topological basis of A_inf over `c.S` is the
identity on `c.S`. Its `c.S`-linear extension `c.extendedCoord c.oneIndex` to B^+ fixes every `y` in
S_B. 

### `adjoinEDivP`

 The subring `S[E/p]` of `BPlus`: the `c.S`-algebra generated by `E / p`. It lies in
S_B = `c.bicommutant` (`adjoinEDivP_le_bicommutant`). 

### `adjoinEDivPClosure`

 The closure of `S[E/p]` in `BPlus` for the topology whose neighbourhoods of `0` are the
`p ^ n * amaxImage`, with `p` inverted: `y` lies in it when, for some `m` and every `n`,
`p ^ m * y` is an element of `S[E/p]` plus `p ^ n` times an element of `amaxImage`. It equals
S_B = `c.bicommutant` (`adjoinEDivPClosure_eq_bicommutant`). 

### `extendedCoord_oneIndex_aeval_mem_adjoinEDivP`

 For a chart `c` with ring `c.S` and element `E` (ξ times a unit in A_inf),
`c.extendedCoord c.oneIndex : B^+ → B^+` is the extension to B^+ of the coordinate of A_inf over
`c.S` that is the identity on `c.S`. It sends the image in B^+ of any polynomial over `Ainf`
evaluated at `Amax.xiDivP = ξ / p` into `S[E/p]` (`c.adjoinEDivP`), the subring of B^+ generated
over `c.S` by `E / p`. 

### `adjoinEDivPClosure_eq_bicommutant`

 The closure of `S[E/p]` in `BPlus` = A_max[1/p], for the topology with neighbourhoods of `0` the
`p ^ n * amaxImage`, with `p` inverted, equals `bicommutant`. Here `c.S` is the image in A_inf of
the chart's map Λ⟦X⟧ → A_inf, E ∈ S is the image of X^e A + p (e = `c.e`, A = `c.unitSeries`), and
`bicommutant` is the set of elements of `BPlus` whose multiplication commutes with every
`c.S`-linear self-map of `BPlus` that keeps `amaxImage`, the image of A_max. 

### `eventually_approx_sum_extendedCoord`

 For `y` in B^+ and `m : ℕ`, for all large enough finite sets `F` of indices,
`y - ∑ i ∈ F, b i • c.extendedCoord i y` is `p ^ m` times an element of `amaxImage`, the image of
the period ring A_max in B^+. Here `b i = c.adicBasis.b i` is the topological basis of A_inf
over `c.S`, and `c.extendedCoord i` extends its `i`-th coordinate to B^+. 

### `frobEnd_mem_bicommutant`

 The Frobenius of B^+ maps S_B = `c.bicommutant` into itself. 

### `exists_bicommutant_mul_phi_E_eq_one`

 The image of `φ E` in B^+ has an inverse in S_B = `c.bicommutant`. 

### `exists_pow_mul_extendedCoord_eq_add`

 Let `ν` in `c.S` have `ξ ∈ (p, ν)` in A_inf, and let `b` be in A_max. For every `M`, the
extended coordinate at `c.oneIndex` (the one that is the identity on `c.S`) satisfies
`p ^ M * c.extendedCoord c.oneIndex b = s + ν ^ M * w` with `s` in `c.S` and `w` in
S_B = `c.bicommutant`. 

### `eventually_exists_pow_mul_eq_add_z_mul`

 For every `y` in S_B = `c.bicommutant` and all large enough `m`, there are `w` in the ring
`WittFq c.f` of constants of the chart and `x` in S_B with `p ^ m * y = w + z * x`. 

 ### Divisibility by z 

### `z_dvd_sub`

 If `g` in G_p fixes the constants `WittFq c.f` pointwise and `y` is in S_B = `c.bicommutant`,
then `z` divides `g • y - y` in B^+. 

### `eq_zero_of_z_pow_dvd`

 An element of B^+ that is divisible by every power of z is zero. 

### `dvd_of_dvd_E_pow_mul`

 A_inf ∩ y B^+[1/E] = y A_inf, where `E = c.E` is ξ times a unit. Let `y` in A_inf not be
divisible by `p`, let ξ lie in the ideal `(p, y)`, and let `θ y ≠ 0`. If `a` is in A_inf and `y`
divides `E ^ k * a` in B^+, then `y` divides `a` in A_inf. 

### `z_dvd_of_dvd_E_pow_mul`

 Let `c` be a chart, `z = c.z` the image of `X` in A_inf and `E = c.E` the image of
`X ^ e * A + p`, which is ξ times a unit, and let `a` be in A_inf. If the image of `z` divides the
image of `E ^ k * a` in B^+, then `z` divides `a` in A_inf. 
