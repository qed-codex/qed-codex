---
{
  "module": "src/New/Spanning/Frames/TopFloor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TopFloor.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/TopFloor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The density at the last entry

A finite set of finite places is read as one ring (`IntegralPlace`); the docstrings call it a finite
place. This file defines the pairing over a fibre and the density at the last entry. The pairing of
the scaled orbital integrals over the fixer of `z` in G^(ϱ), `PlaceData.fiberPairing`, is a function
of `e = l⁻¹ z` on the last vector quadric. At a large lattice datum it agrees there with a step
function. Its integral over the vectors `e` with a given pairing `⟨z, e⟩` is the density
`PlaceData.lastEntryDensity`. The file proves four things. This density is continuous. Its sums
against positive semidefinite matrices, over heads with one common last entry, are nonnegative. Its
Fourier transform in the last entry is the form of floor `𝔰.ϱ`. Finally, the file bounds, by the
fiber pairing at a point, the sums of the pairings of scaled orbital integrals over the congruence
cosets of the links that lie over that point.

## Main definitions and results

* `New.Floors.IntegralPlace.IsLargeLatticeData.sum_fiberPairing_nonneg`: At a large lattice datum
  `F` and at every vector `e`, the sum of the fiber pairings of the heads `ω a` against a positive
  semidefinite matrix `R` is a nonnegative real.
* `New.Floors.IntegralPlace.IsLargeLatticeData.floorForm_top_eq_integral_floorQuadric`: At a large
  lattice datum `F`, the form `F.floorForm 𝔰.ϱ` with the weight `ψ (ξ θ)` on the last diagonal entry
  `θ` of the frame Gram matrix is the integral, over the points `e` of the last vector quadric, of
  `ψ (ξ ⟨z, e⟩)` (`z` the last frame vector) times any continuous function `Φ` that extends the
  fiber pairing.

Notions from other files:
* `T.floorGroup l`, written G^(l), fixes the basis vectors of the floors below `l` in the unitary
  group `T.G`; `besselH` is `T.floorGroup 𝔰.n` with `𝔰.n = 𝔰.ϱ + 1`, which also fixes the last frame
  vector `z`, in position `𝔰.top`; `orbitPoint 𝔰.top l` is `l⁻¹ z`.
* Place data `F` give measures on these groups (`F.measureH` on `besselH`) and a congruence subgroup
  `F.congruenceSubgroup`; `P.IsLargeLatticeData F` says that they are large lattice data at a finite
  place `P`.
* `Z` is a group between `F.congruenceSubgroup` and the integral unitary group, and `Z.besselVector`
  is the vector of the finite Bessel functions of the cosets of `F.congruenceSubgroup` in `Z`.
* `weylElem 𝔰.ϱ p` is the Weyl element of a sequence `p` of units. An element `w_p l⁻¹` with `l` in
  the floor group has head `p` and link `l⁻¹`. The sequence is a head for a gauge `Γ` (a family of
  compact bounds on entries) if its inverse partial products are bounded by the gauge.
* `PlaceData.scaledOrbitalIntegral` (in `New.Spanning.Frames.TopCorrelation`) is the normalized
  orbital integral of the finite Bessel vector of `Z` at `w_p l⁻¹`, indexed by pairs of cosets.


### `PlaceData.fiberPairing`

 The pairing of the scaled orbital integrals of `Z` with heads `p` and `q` at `k * l`, integrated
over `k` in `besselH`, the fixer of the last frame vector `z` in the floor group G^(ϱ), as a
function of the vector `e = l⁻¹ z` for `l` in G^(ϱ); it is zero off the orbit of `z`. 

### `mul_inv_mem_besselH_of_orbitPoint_eq`

 Two elements `l`, `l'` of the floor group G^(ϱ) with `l'⁻¹ z = l⁻¹ z` differ on the left by an
element of `besselH`, the fixer in G^(ϱ) of the last frame vector `z`. 

### `PlaceData.fiberPairing_orbitPoint`

 For `l` in the floor group G^(ϱ) = `T.floorGroup 𝔰.ϱ`, the fixer of the hyperbolic pairs,
`fiberPairing Z p q` at `orbitPoint 𝔰.top l = l⁻¹ z` is the integral over `k` of the pairing of
`scaledOrbitalIntegral Z p (k * l)` and `scaledOrbitalIntegral Z q (k * l)`. Here `k` is integrated
against `F.measureH`, the measure of the place datum on `besselH`, the fixer of `z` in G^(ϱ). 

### `mulVec_mem_lastVectorQuadric`

 Every `l` in `T.floorGroup 𝔰.ϱ` maps `lastVectorQuadric T` into itself. Here
`lastVectorQuadric T` is the set of vectors with no component along the hyperbolic pairs and with
the norm of the last frame vector `z`. 

### `PlaceData.headSumNormSq`

 The pairings of the scaled orbital integrals of `Z` at `l`, for the heads `ω a`, summed against
a matrix `R`. If `R` is the Gram matrix of vectors `x a`, this is the squared norm of the sum over
`a` of the scaled orbital integrals tensored with the `x a`. 

### `PlaceData.headSumNormSq_eq_sum`

 Let `F` be a place datum and `Z` a group between the congruence subgroup `F.congruenceSubgroup`
and the integral unitary group. The sum `headSumNormSq Z R ω l` against `R` of the pairings of the
scaled orbital integrals with heads `ω a` splits over the coordinates `x` of these integrals, which
are pairs of cosets of `F.congruenceSubgroup` in `Z`: the term of `x` is `v^* R v` for the vector
`v a = scaledOrbitalIntegral Z (ω a) l x`. 

### `PlaceData.headSumNormSq_nonneg`

 The pairings of the scaled orbital integrals of `Z` at `l` for the heads `ω a`, summed against a
positive semidefinite matrix `R`, give a nonnegative real. 

### `orbitPoint_mem_lastVectorQuadric`

 For `l` in the floor group `T.floorGroup 𝔰.ϱ`, the vector `orbitPoint 𝔰.top l = l⁻¹ z` lies in
`lastVectorQuadric T`: it has no component along the hyperbolic pairs and has the norm of the last
frame vector `z`. 

### `two_le_card`

 If the form `T` of shape `𝔰` has a large lattice datum `F`, the index set `𝔰.κ` of the basis
vectors outside the hyperbolic pairs and the last frame vector has at least two elements. 

### `lintegral_headSumNormSq_eq`

 Let `F` be a large lattice datum, `R` a positive semidefinite matrix, and `l` in the floor group
G^(ϱ). Let `headSumNormSq Z R ω (g * l)`, the nonnegative sum against `R` of the pairings of scaled
orbital integrals, be integrated over `g` in `besselH`, the fixer in G^(ϱ) of the last frame vector
`z`. The integral is the sum against `R` of the fiber pairings of the heads `ω a` at `l⁻¹ z`. 

### `sum_fiberPairing_nonneg`

 If `F` is a large lattice datum (`P.IsLargeLatticeData F`) and `R` is positive semidefinite,
then for every vector `e` the sum `∑ a b, R a b * fiberPairing Z (ω a) (ω b) e` is a nonnegative
real. 

### `_root_.New.Floors.PlaceData.scaledOrbitalIntegral_mul_left`

 The scaled orbital integral of the finite Bessel vector of `Z` with head `r` does not change
when the inverse link `l` is multiplied on the left by an element of
`besselH ⊓ F.congruenceSubgroup`, the fixer of the hyperbolic pairs and the last frame vector in the
congruence subgroup. 

### `_root_.New.Floors.sum_indicator_mul_le_of_inv_mul_mem`

 Let the elements `β θ` of a group lie in distinct left cosets of a subgroup `K`, so that at most
one `g * β θ` lies in `K`. If `c θ ≤ b` whenever `g * β θ ∈ K`, then the sum of the `c θ` over the
`θ` with `g * β θ ∈ K` is at most `b`. 

### `sum_headSumNormSq_le_fiberPairing`

 Let `F` be a large lattice datum and `R` a positive semidefinite matrix. Let the elements `l θ`
of the floor group G^(ϱ) lie over one vector `e = (l θ)⁻¹ z` and in distinct right cosets of the
congruence subgroup `F.congruenceSubgroup`. Then the sums `headSumNormSq Z R ω (l θ)` against `R` of
the pairings of scaled orbital integrals, times the volume of the congruence subgroup in `besselH`,
the fixer of `z` in G^(ϱ), add up to at most the sum of the fiber pairings at `e` against `R`. 

### `fiberPairing_mulVec`

 At a large lattice datum `F`, the fiber pairing, as a function on the orbit of the last frame
vector `z` under the floor group G^(ϱ), is invariant under the matrices of
`besselH ⊓ F.congruenceSubgroup`, the fixer of the hyperbolic pairs and `z` in the congruence
subgroup. 

### `exists_isCompact_fiberPairing_support`

 At a large lattice datum `F` there is a compact subset `C` of the floor group `T.floorGroup 𝔰.ϱ`
such that `fiberPairing Z p q e` vanishes unless `e` is in the image of `C` under
`orbitPoint 𝔰.top`. 

### `exists_section_orbitPoint`

 Let the form `T` have a large lattice datum `F`, let the units of `A` be open, and let `z` be
the last frame vector. The map `l ↦ orbitPoint 𝔰.top l = l⁻¹ z` has local sections on
`lastVectorQuadric T`, the vectors without components in the hyperbolic planes that have the norm of
`z`. For `l` in `T.floorGroup 𝔰.ϱ`, there is a map `σ` tending to `1` at `l⁻¹ z`. Every point `x` of
the quadric near `l⁻¹ z` then has `σ x` in `T.floorGroup 𝔰.ϱ` and
`orbitPoint 𝔰.top (l * σ x) = x`. 

### `eventually_fiberPairing_eq`

 At a large lattice datum `F`, the fiber pairing `fiberPairing Z p q` is locally constant along
the last vector quadric `lastVectorQuadric T` at the points `orbitPoint 𝔰.top l = l⁻¹ z`, for `l` in
the floor group `T.floorGroup 𝔰.ϱ` and `z` the last frame vector. Near such a point it takes the
same value at every point of the quadric. 

### `exists_step_function_eqOn_fiberPairing`

 At a large lattice datum `F`, the fiber pairing agrees on the last vector quadric with a
function `Φ` of compact support that is invariant under small translations and under
`besselH ⊓ F.congruenceSubgroup`, the fixer of the hyperbolic pairs and the last frame vector in the
congruence subgroup. 

### `floorForm_top_eq_integral_floorQuadric`

 At a large lattice datum `F`, the form `F.floorForm 𝔰.ϱ` with the weight `ψ (ξ θ)` on the last
diagonal entry `θ` of the frame Gram matrix is the integral, over the points `e` of the last vector
quadric, of `ψ (ξ ⟨z, e⟩)` (`z` the last frame vector) times any continuous function `Φ` that
extends the fiber pairing. 

### `PlaceData.lastEntryDensity`

 The density at the last entry `t = p 𝔰.ϱ` of the head `p`: the integral of the fiber pairing of
the heads `p`, `q` over the vectors `e` of the last vector quadric with `⟨z, e⟩ = t` (`z` the last
frame vector), with `(modulus π)⁻¹` times the measure `dx / d⟨x, x⟩` on the sphere over `t`. It is
used with `π * star π = N`, so that this factor is `|N| ^ (-1/2)`, and for heads with `q 𝔰.ϱ = t`,
although the definition does not read `q 𝔰.ϱ`. 

### `integral_lastEntryDensity`

 Descent from the last entry. Let `π` be a unit with `π * star π = N`, and `F` a large lattice
datum of `latticeMiddleGram 𝔰 N`. This is the Gram matrix in the lattice basis of the sum of the
standard form on `𝔰.κ → A` and a line spanned by `z` of norm `-N`. The density
`lastEntryDensity π Z p q` is `(modulus π)⁻¹` times the integral of `fiberPairing Z p q` over the
vectors `e` of the last vector quadric with `⟨z, e⟩ = p 𝔰.ϱ`. Replace the entries `p 𝔰.ϱ`, `q 𝔰.ϱ`
by `unitOrOne t` (`t` if it is a unit, else `1`). Then the density times `P.ψ (ξ t)` is integrable
in `t`. Its integral is `F.floorForm 𝔰.ϱ p q Z.besselVector` with the weight `P.ψ (ξ θ)`, where `θ`
is the last diagonal entry of the frame Gram matrix. 

### `continuous_lastEntryDensity`

 Let `π` be a unit with `π * star π = N`, and let `F` be a large lattice datum of the lattice
form `latticeMiddleGram 𝔰 N`, whose last frame vector `z` has norm `-N`. Then the density
`lastEntryDensity π Z p q` is continuous as a function of the pair `(p, q)`. 

### `integrable_fiberPairing_vectorOfLastEntry`

 Let `π * star π = N`, and let `F` be a large lattice datum of `latticeMiddleGram 𝔰 N`. The fiber
pairing at `vectorOfLastEntry π t x = x - N⁻¹ t z` is integrable in `x` for
`P.normFiberMeasure 𝔰.κ (lastEntrySphereIndex π t)`, the fiber measure `dx / d⟨x, x⟩` of the sphere
`x* x = t t̄ / N - N`. 

### `_root_.New.Floors.PlaceData.sum_lastEntryDensity_eq`

 For heads `ω a` with a common last entry `t`, the sum of the densities against a matrix `R` is
`(modulus π)⁻¹` times the sum against `R` of the integrals of the fiber pairings over the sphere of
`t`. 

### `sum_lastEntryDensity_nonneg`

 Let `π * star π = N`, and let `F` be a large lattice datum of `latticeMiddleGram 𝔰 N`. Suppose
the heads `ω a` have a common last entry `ω a 𝔰.ϱ = t`, and `R` is a positive semidefinite matrix.
Then the sum `∑ a, ∑ b, R a b * lastEntryDensity π Z (ω a) (ω b)` is a nonnegative real. 

### `sum_lastEntryDensity_nonneg_and_eq_inv_mul_lintegral`

 Let `π * star π = N`, and let `F` be a large lattice datum of `latticeMiddleGram 𝔰 N`. Take
heads `ω a` (sequences of units) with a common last entry `ω a 𝔰.ϱ = t` and a positive semidefinite
matrix `R`. Then the sum of `lastEntryDensity π Z (ω a) (ω b)` against `R` is nonnegative. It is
`(P.modulus π)⁻¹` times the integral of the sums of `fiberPairing Z (ω a) (ω b)` against `R` at
`vectorOfLastEntry π t x = x - N⁻¹ t z`. Here `x` is integrated against
`P.normFiberMeasure 𝔰.κ (lastEntrySphereIndex π t)`, the fiber measure `dx / d⟨x, x⟩` of the sphere
`x* x = t t̄ / N - N`. 
