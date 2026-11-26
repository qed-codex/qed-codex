---
{
  "module": "src/Lib/Cohomology/PointClass/ProjectiveSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/ProjectiveSpace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/ProjectiveSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projective space as a functor, and injective pull-back along Noether normalisation

Projective space `ℙ^d` over a field `k` is defined as a functor on `k`-algebras. It is the test
variety on which the Hodge–Tate map is shown not to kill the class of a point.

## Main definitions and results

* `New.Variety.projSpace`: `A ↦` unimodular vectors in `A ^ (d + 1)` modulo units of `A`.
* `New.Variety.projSpace.stdChart`, `New.Variety.projSpace.hasAtlas`: the `d + 1` standard charts
  form an atlas.
* `New.Variety.projSpace.lineProductMap`: a map `ℙ^d × ℙ¹ → ℙ^(d+1)`, used for induction on the
  dimension; `New.Variety.projSpace.isUnit_mul_sum_of_mul_eq_zero` and
  `New.Variety.projSpace.exists_eq_map_affinePoint_of_mul_eq_zero` describe the points where all
  its coordinates but the first vanish.
* `New.Variety.CutsOutLocus.IsNoetherNormalization.pullback_injective`: pull-back along the
  projection to `ℙ^d` of a subfunctor of `Y × ℙ^d` that contains the graph of a Noether
  normalisation is injective on cohomology of `p`-adic tests.

Notions from other files:
* `New.Variety.unimodular`: the subfunctor of affine `d`-space of vectors whose entries generate
  the unit ideal.
* `New.Variety.IsCoordsWithUnit L x v`: `v` is a vector of homogeneous coordinates, for the line
  bundle `L`, of the point `x` of `Y`, and some entry of `v` is a unit.
* `New.Variety.CutsOutLocus.IsHomogeneousSolution k g v`: every homogeneous polynomial over `k` that
  vanishes at `g` vanishes at `v`.
* `New.Variety.CutsOutLocus.IsNoetherNormalization Λ g`: the values at `g` of the linear forms
  `Λ 0, …, Λ d` satisfy no non-zero homogeneous relation, and the cone of `g` is integral over them.
* `New.Variety.IsTest`: a test ring: reduced, absolutely integrally closed, and any `a`, `b`
  admit an idempotent `e` with `a ∣ e * b` and `b ∣ (1 - e) * a`.

## Relation to the literature

Known; see `Lib.Cohomology.PointClass.LinearIndependence` for sources.


 ## Projective space as a functor, standard charts and a product map 

 ### Points of projective space 

### `New.Variety.projSpace`

 Projective `d`-space over `k`: the functor sending `A` to the unimodular vectors in
`A ^ (d + 1)` modulo units of `A`. These are the points of the scheme `ℙ^d` whose line bundle is
trivial; no sheafification is made. 

### `exists_isUnit_of_span_eq_top`

 Over a local ring `A`, a vector whose entries generate the unit ideal has a unit entry. 

### `mk`

 For `v` in `A ^ (d + 1)` whose entries generate the unit ideal (`h`), the point
`[v 0 : … : v d]` of projective `d`-space. 

### `mk_eq_mk_iff_exists_unit`

 The points `[v]` and `[w]` of projective `d`-space agree iff `u • v = w` for a unit `u` of
`A`. 

### `mk_eq_mk_iff_cross_mul`

 For unimodular vectors `v` and `w` in `A ^ (d + 1)`, the points `[v]` and `[w]` of projective
`d`-space are equal iff `v a * w b = w a * v b` for all indices `a` and `b`. In other words, all
2 × 2 minors of the matrix with rows `v` and `w` vanish. 

### `affinePoint`

 For `v` in `A ^ d`, the point of projective `d`-space with coordinate `1` in place `i` and the
entries of `v` in the other places. 

### `mk_mem_stdChart_iff`

 The point `[v]` lies in the image of the `i`-th standard chart iff `v i` is a unit. The chart
is the point over the polynomial ring with coordinate `1` in place `i` and the variables in
the other places. 

### `map_mk`

 The image of the point `[v]` under a map `f` of `k`-algebras is `[f ∘ v]`. 

 ### The map `ℙ^d × ℙ¹ → ℙ^(d+1)` 

### `exists_isUnit_coord_of_mul_eq_zero`

 Let `v`, `u` be unimodular vectors over a local algebra over a field of characteristic `0`, with
`(u 1 - i * u 0) * v i = 0` for all `i`. Then for some `j`, `v j` and `u 0` are units,
`j * u 0 = u 1`, and `v i = 0` for `i ≠ j`. 

### `isUnit_mul_sum_of_mul_eq_zero`

 Let `v`, `u` be unimodular vectors over a local algebra over a field of characteristic `0`,
of lengths `d + 1` and `2`, with `(u 1 - i * u 0) * v i = 0` for all `i`. Then the first
coordinate `u 0 * ∑ i, v i` of `New.Variety.projSpace.lineProductMap` at `([v], [u])` is a unit. 

### `exists_eq_map_affinePoint_of_mul_eq_zero`

 Let `v`, `u` be unimodular vectors over a local algebra over a field of characteristic `0`, with
`(u 1 - i * u 0) * v i = 0` for all `i`. Then, with the points `affinePoint` taken over `k` and
carried to `A` by `structureMap` (the map `k → A`), for some `j` the point `[v]` is the `j`-th
coordinate point and `[u] = [1 : j]`. 

### `isUnit_and_exists_eq_affinePoint_of_mul_eq_zero`

 Let `v`, `u` be unimodular vectors over a local algebra over a field of characteristic `0`, with
`(u 1 - i * u 0) * v i = 0` for all `i`. Then `u 0 * ∑ i, v i` is a unit, and for some `j` the point
`[v]` is the `j`-th coordinate point and `[u] = [1 : j]`. 

### `stdChart`

 For `i : Fin (d + 1)`, the standard chart of projective `d`-space where the `i`-th coordinate is
invertible, on the polynomial ring in `d` variables. The chart point is `affinePoint i X` with
coordinates `X`. It is injective on points, and its image is open: the locus where the `i`-th
coordinate is a unit. 

### `hasAtlas`

 Projective `d`-space has an atlas of dimension `d`: finitely many charts whose images contain
every field-valued point, and for any two points an ideal whose vanishing locus is where they agree.
The standard charts `New.Variety.projSpace.stdChart` contain every field-valued point. Two points
`[v]` and `[w]` agree exactly where all `v a * w b - w a * v b` vanish, so the space is
separated. 

### `span_range_cons_mul_eq_top`

 In characteristic 0: if `v` and `u` are unimodular, so is the vector with entries
`u 0 * ∑ i, v i` and `(u 1 - i * u 0) * v i`. 

### `lineProductMap`

 In characteristic `0`, the map `ℙ^d × ℙ¹ → ℙ^(d+1)` that sends `([v], [w 0 : w 1])` to the
point with coordinates `w 0 * ∑ i, v i` and `(w 1 - i * w 0) * v i` for `i = 0, …, d`. 


## Injectivity of pull-back along a Noether normalisation

The proof of `New.Variety.CutsOutLocus.IsNoetherNormalization.pullback_injective` is a transfer
argument (`New.Variety.exists_transfer_map`) over the Galois hull
`New.Variety.CutsOutLocus.IsNoetherNormalization.exists_galois_closure`; its two density conditions
are checked near each maximal ideal of a test ring.


### `New.Variety.CutsOutLocus.exists_geometric_point_near_prime`

 A test ring `A` over `k` with a prime `m` has a geometric point `κ` that sees `A` near `m`:
finitely many equations that hold under `κ` hold in `A` after multiplication by one element
outside `m`. 

### `New.Variety.CutsOutLocus.exists_lift_near_prime`

 Let `f : k[X] → B` be finite and injective, `A` a test ring (reduced, absolutely integrally
closed, and any `a`, `b` admit an idempotent `e` with `a ∣ e b` and `b ∣ (1 − e) a`) with a prime
`m`, and `w` a point of affine space over `A`. Near `m` the point lifts to `B`: there are `a ∉ m`
and a map of sets `s : B → A` such that, for each `ψ : A → C` that inverts `a`, `ψ ∘ s` is a
`k`-algebra map `v` with `v ∘ f ∘ X = ψ ∘ w`. 

### `New.Variety.CutsOutLocus.exists_point_of_isUnit_coord`

 Suppose that some solution `v` of the homogeneous equations of `g` has `v i ≠ 0`. Then every
solution `u` whose coordinate `u i` is a unit is a coordinate vector of a point of `Y`. 

### `New.Variety.CutsOutLocus.galoisCover`

 The Galois cover of a Noether normalisation, as a functor on `k`-algebras. A point over `A` is
a family `y` of points of `Y` indexed by `G` with a map `v : B → A` of `k`-algebras, such that
`v ∘ b σ` is a coordinate vector of `y σ` with a unit entry for each `σ`, and the values
`v (f (X j))` generate the unit ideal. 

### `New.Variety.CutsOutLocus.exists_cover_point_near_prime`

 Let `L` embed `Y` in projective space, and let `ξ` be an `F`-point of `Y` with coordinates `g`,
some `g i` a unit. Take a prime `m` of a test ring `A`, i.e. `A` is reduced and absolutely
integrally closed, and any `a, b` admit an idempotent `e` with `a ∣ e b` and `b ∣ (1 − e) a`. A
point `[w]` of projective space, with `w` generating the unit ideal, lifts near `m` to the Galois
cover of a Noether normalisation. Here `f : k[X₀, …, X_d] → B` is finite and injective, and each
`b σ` solves the homogeneous equations of `g` and is taken by `Λ` to `f ∘ X`. For some `a ∉ m`,
after every `ψ : A → C` that inverts `a`, there are `v : B → C` with `v ∘ f ∘ X = ψ ∘ w` and points
of `Y` with coordinate vectors `v ∘ b σ`. 

### `New.Variety.CutsOutLocus.exists_map_mul_eq_map_near_prime`

 Near a prime `m` of a test ring `A` (reduced, absolutely integrally closed, and any `a`, `b`
admit an idempotent `e` with `a ∣ e b` and `b ∣ (1 − e) a`), two families of points over one point
of projective space differ by a shift in the finite group `G`, given that `h_conj` says this at
geometric points. If `u • v₀ ∘ f ∘ X = v₁ ∘ f ∘ X` for a unit `u`, and `y₀ σ`, `y₁ σ` are points of
`Y` with coordinate vectors `v₀ ∘ b σ`, `v₁ ∘ b σ`, then for some `a ∉ m` and `τ ∈ G`, `y₀ (τ * ρ)`
and `y₁ ρ` agree after every `ψ : A → C` that inverts `a`. 

### `New.Variety.injective_H_map_of_comp_eq_nsmul`

 Let `ν ≫ α = n • l` for maps `α : N' ⟶ N`, `ν : Q ⟶ N'` and `l : Q ⟶ N` of abelian functors,
where `n ≠ 0` and `l` is an equivalence for a coefficient functor `F` (`IsCohomEquiv`: each
`H.map F l m`, pull-back on the cohomology `H^m(·, F)`, is bijective) on which the field `k` of
characteristic zero acts. Then pull-back along `α` is injective on `H^m(·, F)`. 

### `New.Variety.CutsOutLocus.IsNoetherNormalization.pullback_injective`

 Pull-back along a Noether normalisation is injective on cohomology. Let `Y` be embedded in
projective space by `L`, `ξ` a point of `Y` over a field with coordinates `g`, and `Λ` a Noether
normalisation of `g`. Let `O ⊆ Γ ⊆ Y × ℙ^d` contain `(x, [Λ(v)])` for every coordinate vector `v` of
`x` solving the homogeneous equations of `g` (`hO`). Then pull-back along `O → ℙ^d` is injective on
`H^n` on `p`-adic tests with coefficients `genericCoeff` (a test with ring R ↦ R[1/p]), taking the
free abelian groups on points with values in `genericOver` (R ↦ R[1/p] as a `k`-algebra). 
