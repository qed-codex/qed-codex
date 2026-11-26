---
{
  "module": "src/Lib/General/Measure/FibreMeasure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/FibreMeasure.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/FibreMeasure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measures below a fibre measure

Let `π : X → B` be a map, `μ` a measure on `X` and `ν` a measure on `B`. For a submersion of
manifolds with smooth positive measures, the fibre measures `dμ / dν` on the fibres of `π` are
determined by two properties: integrating over the fibres and then against `ν` is integrating
against `μ`, and the fibre integrals of a continuous function of compact support are continuous on
`B`. This file does not construct them. It defines the relation of being at most the fibre measure
over a point and proves that it is kept by the usual operations on measures and maps.

* `New.LeFibreMeasure`: a measure `l` is at most the fibre measure over a point `b`.
* `New.LeFibreMeasure.of_coordinates`: a parametrisation `ψ t p` of a part of `X` with
  `π (ψ t p) = t` and a weight `w t p`, both continuous at `t = b` and dominated by `μ`, give such a
  measure.
* `New.LeFibreMeasure.trans`: the relation for a pair of maps follows from the relations for the two
  steps, the second map being continuous.
* `New.LeFibreMeasure.map_prod`: the relation is kept by a family of maps that respect `π`.

## Relation to the literature

Fibre measures: Weil, Sur la formule de Siegel dans la théorie des groupes classiques, no. 6.


### `lowerSemicontinuousAt_lintegral`

 Fatou's lemma with a parameter: if `F x` is measurable for every `x` and `F · p` is lower
semicontinuous at `x₀` for almost every `p`, then `x ↦ ∫ F x dρ` is lower semicontinuous at
`x₀`. 

### `le_of_setLIntegral_le`

 Let `ν` be locally finite and positive on nonempty open sets. A function that is lower
semicontinuous at `b`, and whose mean for `ν` over every open set contained in some fixed
neighbourhood of `b` is at most `C`, is at most `C` at `b`. 

### `LeFibreMeasure`

 The measure `l` is at most the fibre measure `dμ / dν` of the map `π : X → B` over the point
`b`: for a lower semicontinuous `K ≥ 0`, a bound `∫_{π ∈ S} K dμ ≤ C ν(S)` for all open sets `S`
contained in some fixed neighbourhood of `b` gives `∫ K dl ≤ C`. 

### `of_coordinates`

 Let `(t, p) ↦ ψ t p`, for `t` in a neighbourhood `V` of `b`, parametrise a part of `X` so that
`π (ψ t p) = t` for almost every `p` with `w t p ≠ 0` and `μ` is at least `w t p dν(t) dρ(p)` there.
If `ψ` and `w` are continuous in `t` at `b` for almost every `p`, then the image of `w b p dρ(p)`
under `ψ b` is at most the fibre measure `dμ / dν` of `π` over `b`, in the sense of
`LeFibreMeasure`: a bound `C ν(S)` on the integrals over small `π ⁻¹' S` of a lower semicontinuous
`K ≥ 0` bounds its integral for this image by `C`. 

### `of_measurePreserving`

 If `μ` is the image of `ν × ρ` under a map `φ`, continuous in the first variable at `b`, with
`π (φ (t, p)) = t`, then the image of `ρ` under `φ (b, ·)` is at most the fibre measure
`dμ / dν` of `π` over `b`, in the sense of `LeFibreMeasure`: a bound `C ν(S)` on the integrals over
small `π ⁻¹' S` of a lower semicontinuous `K ≥ 0` bounds its integral for this image by `C`. 

### `mono`

 If `l` is at most the fibre measure `dμ / dν` of `π` over `b` (see `LeFibreMeasure`), then so is
every smaller measure `l'` for every larger measure `μ'`. 

### `congr`

 The relation `LeFibreMeasure`, of being at most the fibre measure, is kept when `π` is changed
on a `μ`-null set. 

### `smul`

 If `l` is at most the fibre measure `dμ / dν` of `π` over `b` (see `LeFibreMeasure`) and `c` is
finite, then `c • l` is at most the fibre measure `d(c • μ) / dν`. 

### `comp_homeomorph`

 If `l` is at most the fibre measure `dμ / dν` of `π` over `b` (see `LeFibreMeasure`) and the
homeomorphism `e` of the base carries `ν` to `ν'`, then `l` is at most the fibre measure
`dμ / dν'` of `e ∘ π` over `e b`. 

### `trans`

 Fibre measures in two steps. If `l` is at most the fibre measure `dμ / dν` of `π` over `b`, and
`l'` is at most the fibre measure `dl / dν'` of a continuous map `π₂` over `b'`, then `l'` is at
most the fibre measure `dμ / d(ν × ν')` of `(π, π₂)` over `(b, b')` (see `LeFibreMeasure`). 

### `map_prod`

 Let `x ↦ φ (p, x)` be a measurable family of continuous maps `X → X'` with
`π₀ (φ (p, x)) = π x`. If `l` is at most the fibre measure of `π` for `μ` over `b` (see
`LeFibreMeasure`), then the image of `ρ × l` under `φ` is at most the fibre measure of `π₀` for the
image of `ρ × μ` over `b`. 

### `map`

 If `l` is at most the fibre measure of `π₀ ∘ φ` for `μ` over `b` (see `LeFibreMeasure`), with
`φ` continuous, then the image of `l` under `φ` is at most the fibre measure of `π₀` for the image
of `μ` over `b`. 
