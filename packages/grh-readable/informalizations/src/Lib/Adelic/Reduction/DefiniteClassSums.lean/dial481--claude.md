---
{
  "module": "src/Lib/Adelic/Reduction/DefiniteClassSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/DefiniteClassSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/DefiniteClassSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mahler's criterion for hermitian spaces and class sums for definite spaces

For a hermitian space `V : New.Space E n s`, the rational unitary group embeds in the adelic unitary
group `New.G E s` with image `V.Γ`, and in its finite part with image `V.Γf`. Mahler's criterion
follows from short bases, whose Gram matrices take finitely many values. It gives compactness modulo
the rational points when all signs agree. For the signs `1`, it also gives finiteness of classes.
For such a space, the integral over `Γ \ G` of a suitable invariant function is then a class
sum. Here `K₀` is `New.stdLevel`, and `New.classSum` sums over the double cosets `Γf \ G_f / K` with
weights `1 / #(Γf ∩ g K g⁻¹)`.

## Main definitions and results

* `New.Space.mahler_criterion`: Mahler's criterion; the `g` of bounded height lie in `V.Γ * C` for
  one compact set `C`.
* `New.Space.isCocompact_of_definite`: if all signs agree, the adelic group is compact modulo
  `V.Γ`. `New.Space.isCocompact_Gamma` is the case of the signs `1`.
* `New.Space.isCocompact_finitePart`: for the signs `1`, the finite part of the group is
  compact modulo `V.Γf`.
* `New.Space.hasFiniteType_of_isLevel`: for the signs `1`, finitely many classes with finite
  stabilisers.
* `New.Space.integral_quotMeasure_eq_classSum`: take a space with signs `1` and a continuous, left
  `Γ`-invariant function on `G`. Suppose that its average over the infinite places is fixed under
  right translation by an open `K ≤ K₀`. Then its integral over `Γ \ G` is `[K₀ : K]⁻¹` times the
  class sum of this average. `New.Space.classIntegral_eq_integral` is the case of functions of the
  finite part.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s), with s the signs, at the infinite places and 1 at the finite places.
* `New.Space.move`: the space `V.move g` is the space with the same J and the point x g; its lattice
  `baseLattice` is the lattice at `g`, and the norm of `archCoords u` is the length of u at `g`.
* `New.Space.height`: the height ht(g) = 1/λ, with λ the first minimum cut off at 1
  (`New.Space.firstMinimum`) of the moved space `V.move g`.
* `New.IsLevel`: an open subgroup of `K₀`, with index `New.stdLevelIndex` in `K₀`.

## Relation to the literature

Known; see `Lib.Adelic.Reduction.FiniteVolume` and `Lib.Adelic.QuotientMeasure.Basic` for sources.



## Mahler compactness, and finiteness of classes in the definite case

`V` is a matrix `J` over `E` with an adelic point `x`. `New.G E s` is the unitary group of the
standard form. `V.ratEmbed γ = x⁻¹ γ x` embeds `U(J)(E)` in it with image `V.Γ` (finite parts:
`V.Γf`), and `V.toRatCoords g = x g x⁻¹`.


### `exists_short_basis_matrix`

 For a hermitian space `V` with a point, there is a constant `c` such that for every `g` in
`G E s` some basis of `Eⁿ`, the columns of `Y`, lies in `(V.move g).latticeBall (c * V.height g)`.
That is, each column is a vector of the base lattice of the moved space `V.move g` (the same form
with the point `V.x * g`) whose length `‖archCoords y‖` in that space is at most `c * V.height g`.
Here `V.height g = 1 / λ`, where `λ` is the first minimum of `V.move g` cut off at `1`. 

### `exists_isCompact_of_bounded_frame`

 Points with a bounded rational frame from `H` are compact modulo the rational isometries in `H`:
for a compact set `C` of adelic matrices and a subgroup `H` of `GL n E` there is a compact
`K ⊆ G E s` such that, whenever `x g⁻¹ x⁻¹ r ∈ C` for some `r ∈ H` (`x` the point of `V`,
`V.toRatCoords g = x g x⁻¹`, `toAdele` embeds `E` in its adeles), some element `γ` of the group
`U V.J` of rational isometries lies in `H` and has `V.ratEmbed γ * g ∈ K`. 

### `mahler_criterion`

 One half of the Mahler–Godement compactness criterion, for the unitary group of a hermitian
space: for each real `R` there is a compact subset `C` of the adelic unitary group `G E s` such that
every `g` with `V.height g ≤ R` has `γ * g ∈ C` for some `γ` in the group `V.Γ` of rational points
(the elements `x⁻¹γx`, with `x` the point of `V` and `γ` in the rational unitary group of `V.J`).
Here `V.height g = 1/λ`, where `λ` is the first minimum of the moved space `V.move g` cut off at `1`
(`firstMinimum`). 

### `isCocompact_of_definite`

 If all signs `s i` are equal (the space is definite), then the adelic unitary group `G E s` is
compact modulo the group `V.Γ` of rational points: there is a compact `C` such that every `g` has
`γ * g ∈ C` for some `γ ∈ V.Γ`. The hypothesis `h_definite` may be omitted when `simp` proves it,
as for constant `s`.

A special case of the compactness theorem for anisotropic groups (Borel–Harish-Chandra,
Mostow–Tamagawa), part of the reduction theory. 

### `isCocompact_Gamma`

 If all the signs of `V` are `1`, then `G E 1` is compact modulo the group `V.Γ` of rational
points: some compact set meets every coset `V.Γ g`. 

### `isCocompact_finitePart`

 For a space with all signs `1`, the subgroup `V.Γf` of finite parts of the rational points is
cocompact in the finite adelic unitary group: some compact set meets every coset `V.Γf g`. 

### `hasFiniteType_of_isLevel`

 For a space with all signs `1` and a level `K` (an open subgroup of `stdLevel E n`), the pair
`(Γf, K)` has finite type (`HasFiniteType`): there are finitely many double cosets `Γf \ Gf / K`,
the stabilisers `Γf ∩ g K g⁻¹` are finite, and `K` is open and compact.

A special case of Borel's finiteness of class numbers. Only forms with an adelic orthonormal frame
are covered, at open subgroups of the standard level. 


## Unimodularity and the integral over [G] as a class sum

The Haar measures of `New.Gf` (finite points) and `New.G` (all adelic points) are right invariant.


### `instance : (volume : Measure (Gf E n)).IsMulRightInvariant`

 `Gf E n` is unimodular: the rational points of the standard space are a lattice in it. 

### `measureReal_eq_inv_stdLevelIndex`

 A level `K` (an open subgroup of `stdLevel E n`) has volume `1 / [stdLevel E n : K]`, as
`vol (stdLevel E n) = 1`. 

### `instance : IsMulCommutative (Gf E Unit)`

 The group `Gf E Unit` of `1 × 1` matrices is commutative. 

### `instance : (volume : Measure (G E s)).IsMulRightInvariant`

 `G` is unimodular, as a product of unimodular groups. 

### `integral_quotMeasure_integral`

 Unfolding on a space with all signs `1`: for `Φ` integrable on `G`, the sum
`g ↦ ∑ γ ∈ Γ, Φ (γ g)` over the rational points `Γ = V.Γ`, written as an integral for the counting
measure, is integrable on `[G]`, with the same integral as `Φ`. Integration on `[G] = Γ \ G` is by
`V.quotMeasure`. 

### `integral_indicator_univ_prod_coset`

 Let `f g` be the integral of `F` over `G_∞ × {g}` (`G_∞ = GInf E 1` is the group at the
infinite places), let the level `K` fix `f` under right translation (`rightStabilizer f`), and let
`u` be a finite point such that the indicator of `G_∞ × u K` times `F` is integrable. Then the
integral of `F` over `G_∞ × u K` is `[stdLevel E n : K]⁻¹ * f u`. 

### `integral_quotMeasure_eq_classSum`

 Let `V` be a space with all signs `1`: a hermitian matrix `J` over `E` and a point `x`. Write
`V.Γ` for its rational points `x⁻¹γx` (`γ ∈ U(J)(E)`) in `G = G_∞ × G_f`, and `V.Γf` for their
finite parts in `Gf E n`. Let `F` be a continuous left `V.Γ`-invariant function on `G` whose
integral over `G_∞` at `(·, g)` is `f g`, and let `K` be a level (an open subgroup of
`K₀ = stdLevel E n = G_f ∩ GL_n(Ô)`) that fixes `f` under right translation. Then the integral of
`F` over `V.Γ \ G` against `V.quotMeasure` (with `vol G_∞ = vol K₀ = 1`) is `[K₀ : K]⁻¹` times the
class sum of `f`, which is the sum over the double cosets `V.Γf g K` of
`f g / #(V.Γf ∩ g K g⁻¹)`. 

### `classIntegral_eq_integral`

 Let `V` be a space with all signs `1`. Write `V.Γ` for its rational points `x⁻¹γx`
(`γ ∈ U(J)(E)`) in `G = G_∞ × G_f` and `V.Γf` for their finite parts, and let `K` be a level, an
open subgroup of `K₀ = stdLevel E n = G_f ∩ GL_n(Ô)`. Let `y` on `G_f` be left `V.Γf`-invariant with
open right stabiliser. Then `classIntegral V.Γf K y` equals `[K₀ : K]` times the integral of
`g ↦ y g_fin` over `V.Γ \ G` against `V.quotMeasure` (with `vol G_∞ = vol K₀ = 1`), where
`classIntegral V.Γf K y` is the sum over the double cosets `V.Γf g K'` of
`y g / #(V.Γf ∩ g K' g⁻¹)`, with `K' = rightStabilizer y ⊓ K`, divided by `[K : K']`. 
