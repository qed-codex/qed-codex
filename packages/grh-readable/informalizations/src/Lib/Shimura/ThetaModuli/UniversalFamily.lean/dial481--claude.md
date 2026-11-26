---
{
  "module": "src/Lib/Shimura/ThetaModuli/UniversalFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/UniversalFamily.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaModuli/UniversalFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence of the universal theta family over a smooth projective base

`New.Variety.ThetaNull.nonempty_universalFamily` shows, when `R` is a localization of `𝓞 E` at a
submonoid of non-zero-divisors and every maximal ideal of `R` lies over a good prime for `D`
(`IsGoodOver D R`), that the type `New.Variety.UniversalFamily D R` of universal objects is
nonempty. A universal object is a family of theta-embedded abelian schemes for the PEL data `D`
(`New.ThetaFamily`) over a projective `R`-scheme that is smooth of relative dimension
`card D.Index - 1`. Its fibres at a dense set of complex points are the theta tori
(`New.ThetaTori.ThetaTorus`) of all analytic families (`New.Variety.AnalyticFamily`). Its
uniformisations are holomorphic in the parameter and in the fibre.

The base is the reduced closure of the theta coordinates of the level points in a product of
projective spaces. `New.Variety.exists_thetaFamily_of_points` puts a family on it, using good
reduction at the level points. Smoothness comes from the immersion of the balls and the tangent
bound.

Notions from other files:
* `New.ThetaObject.TorusModel`: a model of a fibre of the family on the complex torus of a polarised
  period map, with its uniformisation and its theta functions `θ`.
* `LineBundle.IsHomogeneousCoords L t v`: `v` are homogeneous coordinates of the point `t` for `L`:
  `t` lies in the chart `j` of `L` exactly when `v j` is a unit, and there the transition function
  to the chart `k` is `v k / v j`. For a linear system (`IsLinearSystem`), the transition functions
  are regular on the charts and give homogeneous coordinates.
* `ReducedClosure`: the reduced Zariski closure `W` of a family of tuples of complex points in a
  product of schemes, with its complex points `point a`, which are dense.
* `PEL.IsGoodAt D w`: the prime `w` of `𝓞 E` is good for the data `D`: it contains neither
  `D.paddedNorm` nor the order of `D.dualTorsion`, and it contains a prime number `p` and `D.β - b`
  for an integer `b` with `D.β - b` coprime to `star D.β - b`, and two further conditions hold
  (see its definition).

## Relation to the literature

Known result: Moduli of abelian varieties by theta values via theta-null embedding and universal
family. Here the base is the closure of the theta values at the level points of PEL tori, not a
locus cut out by quartic relations; the family on it comes from
`New.Variety.exists_thetaFamily_of_points`. Source: D. Mumford, On the equations defining abelian
varieties II, Invent. Math. 3 (1967) 75-135; theta groups in part I, Invent. Math. 1 (1966) 287-354.


### `IsGoodOver`

 The datum `D` is good at every closed point of `Spec R`: for each maximal ideal `m` of the
`𝓞 E`-subalgebra `R` of `E`, the datum `D` is good at the contraction of `m` to `𝓞 E`. 

### `isUnit_star_sub_and_card_of_isGoodOver`

 If the maximal ideals of the `𝓞 E`-subalgebra `R` of `E` lie over good primes, then `β̄ - β`
and the order of `D.dualTorsion` are units of `R`. 

### `HasPeakCharts`

 The charts of the bundles `c l`, for `l` in `D.dualTorsion` seen inside the larger
`D.levelTorsion` that indexes the level points, cover the point `t` in the pattern of the largest
theta constants: for each `s` there is `o` such that `t` lands in the chart `k` of `c l` whenever
`l + k` is `o`, `-o` or `s - o`. 

### `hasPeakCharts_of_hasGoodReduction`

 The peak pattern at the closed point of an arc. Let `x` have good reduction for `v`, with
`v (#T) = 1`. Let `p ω` be the theta coordinates of the level point `ω` of `x`, taken at its lift
`x.torsionLift ω` to `V`, divided by the nonzero coordinate `i ω`, and let their residues be
homogeneous coordinates, for `c ω`, of the closed point of `α`. Then the charts of the `c ω` cover
that point in the pattern of the largest theta constants (`New.Variety.ThetaNull.HasPeakCharts`). 

### `exists_isCutOutAt_and_hasPeakCharts`

 Good reduction along an arc. Let `α` be a map to `S` from the spectrum of the valuation ring of
`v`, where `ρ : 𝓞 E → v.valuationSubring` agrees with the complex embedding `Φ v₀` of `E` and the
prime of `𝓞 E` below the maximal ideal is good for `D`. Let each bundle `c ω` be a linear system,
and let the theta coordinates of the level point `ω` of `x` be homogeneous coordinates of the
generic point of `α` for `c ω`. Then at the closed point of `α` the bundles `c` cut out some set `Z`
(`New.Variety.ThetaNull.IsCutOutAt`): in each chart, the ideal of `Z` is cut out by the affine
coordinates there, with ranks `thetaRanks`. Also, their charts cover that point in the pattern of
the largest theta constants (`New.Variety.ThetaNull.HasPeakCharts`): for each `s` some `o` puts it
in chart `k` of `c l` whenever `l + k` is `o`, `-o` or `s - o`. 

### `FamilyParameter`

 A parameter is an analytic family together with a point of the space containing its domain. 

### `FamilyParameter.torus`

 The theta torus of the family `a.1` at the point `a.2`. 

### `FamilyParameter.levelCoords`

 The theta coordinates of the level point `ω` of the theta torus at the parameter `a`. 

### `exists_isHomogeneousCoords_levelCoords`

 For a parameter `a` and a level point `ω`, some complex point `t` of projective space over `R`
lies over the complex point `specOver R ℂ` of `Spec R` and has the theta coordinates of `ω` at `a`
as homogeneous coordinates for the hyperplane bundle. 

### `levelPoint`

 The complex point of projective space over `R` whose homogeneous coordinates are the theta
coordinates of the level point `ω` at the parameter `a`. 

### `isHomogeneousCoords_levelPoint`

 The theta coordinates of the level point `ω` at `a` are homogeneous coordinates of
`levelPoint R ω a`. 

### `ThetaClosure`

 The reduced closure, in a product of projective spaces over `R` indexed by the level torsion,
of the theta coordinates of the level points at the parameters `y b`. 

### `coordBundle`

 The hyperplane bundle of the factor `ω`, pulled back to the closure. 

### `complexPoint`

 The complex point of the closure at the parameter `y b`. 

### `toIntegers`

 The structure map of the closure to `Spec (𝓞 E)`. 

### `isHomogeneousCoords_complexPoint`

 The theta coordinates of the level point `ω` at the parameter `y b` are homogeneous
coordinates of the complex point at `b` for the bundle of the factor `ω`. 

### `hasProjEmbedding`

 The morphism `C.scheme.hom` has a projective embedding, obtained via `C.incl` into a product of
projective spaces. 

### `isProjEmbedding_pi_coordBundle`

 The product of the bundles `C.coordBundle ω` over all `ω` embeds the closure in projective
space over `R`. 

### `exists_arc_isGoodAt`

 Let `R` be a noetherian `𝓞 E`-subalgebra of the CM field `E`, with the PEL data `D` good at its
maximal ideals. If finitely many points `j i` are dense in the closure `C`, then every point `z`
specialises to the centre of an arc through one of them, and the arc lies over a good prime. 

### `HasThetaFibres`

 The family `X` over the closure has the theta tori as fibres: at each point `b` there is a model
of the fibre on the torus at `y b` whose theta coordinates are those of the torus. 

### `exists_hasThetaFibres`

 Let `R` be a noetherian `𝓞 E`-subalgebra of the CM field `E`, the localisation of `𝓞 E` at `M`,
with the PEL data `D` good at its maximal ideals. Let `C` be the reduced closure, in a product over
the level torsion of projective spaces over `R`, of the theta coordinates of the level points at the
parameters `y b`. If the complex points of `C` at finitely many parameters `y (j i)` are dense, then
there is a theta family `X` over `C` (via its structure map to `Spec 𝓞 E`) such that for every `b`
the fibre at the complex point `b` has a model on the theta torus at `y b` with the same theta
coordinates. 

### `holomorphicAt_complexPoint`

 In an analytic family `F` the point of the closure depends holomorphically on the parameter. 

### `holomorphicAt_uniformisation`

 Let `m a` be a model of the fibre of `X` at the parameter `a` on the theta torus at `a`, whose
theta functions `(m a).θ` are those of the torus (`hθ`). Then for a point `b` of the domain of an
analytic family `F`, the uniformisations `(m (F, b')).uniformisation` of the fibres, followed by the
maps to the total space, are holomorphic in the parameter `b'` and the fibre variable together. 

### `point_eq_of_isLevelIso`

 Let `R` be a Dedekind domain, the localisation of `𝓞 E` at `M`, with `D` good at its maximal
ideals. Parameters `x = (F, b)` and `x'` whose moduli points `F.ballPoint 0 (b, 0)` are isomorphic
at level `D.level` (by `z`, which lies in the level group `levelGU D.Index D.level` and matches
their reflections) have the same point in the closure. 

### `IsGenericParameter`

 The point `b` of the domain of `F` is generic: the point of the closure at `b` specialises to
the points at all parameters in the domain of `F`. 

### `exists_finite_isDenseFamily`

 The generic points of finitely many analytic families are dense in the closure. 

### `exists_smooth_near_arc`

 Let `X` have the theta tori as fibres and `a` be a generic parameter. Let `α` be an arc whose
generic point is the complex point at `a` and whose closed point lies over a prime good for `D`.
Then some open `U` through which `α` factors is smooth of relative dimension `card D.Index - 1`
over `Spec R`. 

### `nonempty_universalFamily`

 Existence of the universal family. Let `R` be the localisation of `𝓞 E` at a submonoid of
non-zero-divisors, and let `D` be good (`New.PEL.IsGoodAt`) at the contraction to `𝓞 E` of every
maximal ideal of `R`. Then there is a theta family (an abelian scheme with `𝓞 E`-action, a line
bundle with point-separating coordinates and level points) over an `R`-scheme `S`, projective and
smooth of relative dimension `card D.Index - 1`. It comes with a dense set of complex points indexed
by pairs of an analytic family of tori `f` and a parameter `b`, at which the fibres are uniformised
by the tori, holomorphically in `b` on the domain of `f`. 
