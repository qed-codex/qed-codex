---
{
  "module": "src/New/Spanning/Frames/FiniteDepth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiniteDepth.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FiniteDepth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Depth, heads and far positions at the finite places

This file proves the facts about a large lattice datum at the finite places that bound the local
Bessel kernels: the sets 𝔡_a are fractional ideals, the heads of a nonvanishing form have integral
leading products, and a position far from the identity forces a small ideal. Here `R = integers` is
the ring of integers of `A`, K is the group of integral points of the unitary group (in statements,
`K : ℕ` is an exponent), K(g) is its principal congruence subgroup of level `g = F.levelUnit`, and
`n = 𝔰.n = ϱ + 1`. In the gauge `Γ` of scale `α` an element `a` has size `i` if `α ^ i * a ∈ R`, and
losses are powers of `Γ.loss = 2 / modulus α`.

## Main definitions and results

* `New.Floors.IntegralPlace.IsLargeLatticeData.exists_ideal_depth_eq`: at a near point the products
  with the stable vectors form an ideal of `R`, and the depth is its index.
* `New.Floors.IntegralPlace.IsLargeLatticeData.prod_mem_of_formMajorant_ne_zero`: the forms vanish
  unless the leading products of both heads are integral.
* `New.Floors.IntegralPlace.IsLargeLatticeData.exists_gauge_of_formMajorant_ne_zero`: a scale
  adapted to two heads.
* `New.Floors.IntegralPlace.IsLargeLatticeData.exists_volume_stableProducts_le`: a large denominator
  of `(x - 1) / g` forces a deep vector.

Notions from other files:
* `New.Floors.IntegralPlace.IsLargeLatticeData`: the place data is given by a lattice, in a
  unimodular unitary group of large rank; its box `F.boxSet` is K.
* `New.Floors.PlaceData.stableProducts`: the set 𝔡_a of the products of e_a with the vectors that
  are stable at two points `x` and `x * y`.
* `New.Floors.PlaceData.IsNear`: `x` is near at `j` if a translate of `x` by
  `T.partialUnitriangularGroup j` lies in the box.
* `New.Floors.PlaceData.IntermediateGroup.besselVector`: for a group `Z` with K(g) ≤ Z ≤ K, the
  vector whose coordinate at the coset K(g) z is `extendedBesselChar F.levelUnit (y * z⁻¹)`.
* `New.Floors.PlaceData.formMajorant`: an integral of moduli of orbital integrals that bounds the
  form of two heads.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `inv_two_pow_le_groupMeasure`

 Let `F` be a large lattice datum, `R = integers` the ring of integers of `A` and `P.intUnits`
its set of units. The hypothesis `hB` has two parts: `B` is at least `2`, and the non-units of `R`
have volume at most `B⁻¹`. Then the group `K = unitaryLevel integers 1 T.splitGram` of integral
points of the unitary group has measure at least `2⁻¹ ^ 𝔰.n` for the measure `F.groupMeasure`. 

### `exists_stableProducts_eq_unit_mul_integers`

 For a large lattice datum, the set 𝔡_a = `F.stableProducts a x y` (the coordinates at the dual
of e_a of the vectors that are stable, `F.IsStable a`, at the points x and x y) is c R for some unit
c of A, where R = `integers`. 

### `stableProducts_subset`

 For a large lattice datum, let x be near at a + 1. Then the set 𝔡_a = `F.stableProducts a x y`,
the coordinates at the dual of e_a of the vectors that are stable at x and x y, lies in the ring of
integers. 

### `exists_ideal_depth_eq`

 **Depth at the finite places.** For a large lattice datum, let x be near at a + 1. Then the set
𝔡_a = `F.stableProducts a x y`, the coordinates at the dual of e_a of the vectors that are stable at
x and x y, is an ideal of the ring of integers, and the depth of e_a, the inverse of the volume of
this set, is the index of this ideal. 

### `exists_unit_mem_stableProducts`

 For a large lattice datum and a group Z between the congruence subgroup K(g) and the integral
group K, if the finite Bessel vectors `Z.besselVector` at two points x and z are not orthogonal,
then for each a and each y the set 𝔡_a = `F.stableProducts a x y` contains a unit c of A lying in
the ring `integers`, and has volume at most the modulus of c. 

### `exists_mem_boxSet_hasMatrixSize_of_inner_ne_zero`

 Let `F` be a large lattice datum with level unit `F.levelUnit`. Let `Z` be a group between the
congruence subgroup K(g) and the integral group K. Let `Γ` be a gauge, a notion of size together
with a scale. If the finite Bessel vectors `Z.besselVector x` and `Z.besselVector y` are not
orthogonal, there are u, v in the Bessel unipotent group `besselU` with (a) u x and v y in the box
`F.boxSet` of integral points, and (b) `Γ.HasMatrixSize 2` holding for (v y − u
x) / `F.levelUnit`. 

### `prod_mem_of_formMajorant_ne_zero`

 Let `F` be a large lattice datum, `Z` a group between the congruence subgroup K(g) and the
integral group K, `j ≤ ϱ`, and let `p`, `q` be sequences of units. If the majorant `F.formMajorant`
of their form of floor `j` (an integral of moduli of orbital integrals of the Bessel vector of `Z`)
is nonzero at a point `x`, then the products `p 0 ⋯ p (l - 1)` and `q 0 ⋯ q (l - 1)`, `l ≤ j`, lie
in the ring `integers`. 

### `exists_unit_multiple_of_prod_mem`

 Let `r` be a sequence of units of `A` all of whose products `r 0 ⋯ r (l - 1)`, `l ≤ j`, are
integral. Then some unit `β` of `A` lying in `integers` is an integral multiple of each of them and
of each `r i`, `i < j`, and the weight `finHeadWeight K j r` equals `√(genIndex β) ^ K`. Here
`genIndex β` is the inverse of the factor by which `β` scales Haar measure, and the weight is the
product of the numbers `√(genIndex (r 0 ⋯ r l)) ^ K` over `l < j`. 

### `two_div_modulus_pow_le_mul_sqrt_genIndex_pow`

 Let `g`, `β`, `γ` be units of `A` lying in `integers`, and `α` a unit with `modulus α = modulus
g * (modulus β * modulus γ) ^ 2`. If `4 E ≤ K`, then `(2 / modulus α) ^ E` is at most
`(2 / modulus g) ^ K` times `√(genIndex β) ^ K * √(genIndex γ) ^ K`. 

### `exists_gauge_of_formMajorant_ne_zero`

 Let `F` be a large lattice datum with level unit `g = F.levelUnit`, let `Z` be a group between
the congruence subgroup of level `g` and the group of integral points, let `j ≤ 𝔰.ϱ`, and let `p`,
`q` be sequences of units of `A`. Suppose that the majorant `F.formMajorant` of their form of floor
`j`, for the Bessel vector of `Z`, is not zero at some point. Then there is a unit `α` of `A`, lying
in `integers` and fixed by the involution, with the following properties in the gauge `Γ` of scale
`α`. The inverses of the products `p 0 ⋯ p (l - 1)` and `q 0 ⋯ q (l - 1)`, `l ≤ j`, have size 1
(`Γ.IsHead`); so have `g⁻¹` if `j ≠ 0` and `1 / p i - 1 / q i` for `i < j`; and if `4 E ≤ K`, then
`Γ.loss ^ E` is at most `(2 / modulus g) ^ K` times the weights `New.finHeadWeight K j` of `p` and
`q`. 

### `mem_positions_of_formMajorant_ne_zero`

 Let `F` be a large lattice datum with level unit `g`, let `Z` be a group between the congruence
subgroup K(g) = `F.congruenceSubgroup` and the group of integral points, and let `p`, `q` be any two
sequences of units. A point `x` at which the majorant `F.formMajorant` of their form of floor `j`,
for the Bessel vector of `Z`, does not vanish lies in `F.positions`, the set of products of a
conjugate of an element of the Bessel unipotent group `besselU` and an element of K(g). 

### `exists_star_eq_common_multiple`

 Let `d i`, `i < ϱ`, be units of `A` lying in `integers`, and let `σ ≤ 1` satisfy `σ ^ 2 ≤ |d i|`
for `j ≤ i`. Then the `d i` with `j ≤ i` have a common multiple `C` in `integers`, a unit of `A`
fixed by the involution, of modulus at least `σ ^ (4 n)`. 

### `exists_volume_stableProducts_le`

 Let `F` be a large lattice datum with level unit `g`, let `Z` be a group between the congruence
subgroup of level `g` and the group of integral points, let `n = 𝔰.n`, and let `Γ` be the gauge of
scale `α`, in which size 1 means that `α` times the element lies in `integers` and
`Γ.loss = 2 / modulus α`. Let `c` divide every common denominator in `integers` of the entries of
`(x - 1) / g`, let `σ < 1` satisfy `modulus c * Γ.loss ^ (10 n · 99 n) ≤ σ ^ (400 n²)`, let `p`, `q`
be heads of length `j ≤ ϱ` for `Γ`, and let `g⁻¹` have size 1 if `j ≠ 0`. Suppose that the Bessel
vectors of `Z` at `y` and `y * x` are not orthogonal and that these two points, moved back by the
Weyl elements `weylElem j p` and `weylElem j q`, are near at `j`. Then for some `i ≥ j` the set
`F.stableProducts i y x`, the coordinates at the dual of e_i of the vectors that are stable at `y`
and `y * x`, has volume at most `σ ^ 2`. 
