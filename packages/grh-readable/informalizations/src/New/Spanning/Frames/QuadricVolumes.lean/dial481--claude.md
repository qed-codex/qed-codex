---
{
  "module": "src/New/Spanning/Frames/QuadricVolumes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/QuadricVolumes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/QuadricVolumes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Volumes on quadrics and on sections

The equation of a quadric is solved in a block of orthonormal coordinates: the other coordinates
are free, and the points of size j of the fibres have mass bounded in terms of j. A section
⟨e_a, y⟩ = c of an isotropic cone, for a unit c, is an orbit of a Heisenberg group. The letters
G^(l), U_(<l) and Y^(l) are those of the head of `New.Spanning.Frames.Lengths`.

## Main definitions and results

* `New.Floors.Gauge.exists_isSolvedIn`: the quadric of a floor is solved in a block.
* `New.Floors.Gauge.setLIntegral_orthonormalPart_le`: integrals of functions of the orthonormal
  coordinates.
* `New.Floors.Gauge.lintegral_heisenbergMeasure_le`: integrals over a Heisenberg group.
* `New.Floors.sectionPoint`, `New.Floors.PlaceData.lintegral_floorQuadricMeasure_eq`,
  `New.Floors.Gauge.setLIntegral_sectionMeasure_le`: sections and their measures.

Notions from other files:

* `Γ.ofSize j`, `Γ.vecsOfSize j`: the numbers of size j and the vectors whose entries have size j.
  The powers of the number `Γ.loss` bound moduli |u| = `modulus u` and volumes.
* `F.floorBasis b`: a basis of V_b, the span of the basis vectors of floor at least b (a space of
  representatives of Y^(b)), made of hyperbolic pairs and orthonormal vectors indexed by ι. The
  orthonormal vectors whose index lies in the range of `F.freeIndex : F.FreeIndex → ι` span X'.
* `IsSolvedIn blk ρ S B`: the measure ρ is the volume in the coordinates off the block `blk` times
  measures in the block, each of mass at most B on the vectors with coordinates in S.
* `heisenbergElem a (ω, β)`: the element of the Heisenberg group of floor a with vector part ω and
  skew part β.
* `CongrBelow l ω ω'`: the vectors ω and ω' differ by a combination of the e_b with b < l.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


### `mem_vecsOfSize_of_floorBasis_mulVec`

 If the vector with coordinates x in the basis `F.floorBasis b` of V_b has size j (all its
entries do), then x has size j + 4. 

### `exists_blocks`

 The orthonormal basis vectors, indexed by ι, contain two blocks `blk₁`, `blk₂` of `F.blockRank`
distinct vectors each, disjoint from each other and from the basis of X', which `F.freeIndex`
indexes: the three index maps together form an injective map. 

### `exists_isSolvedIn`

 Let ρ be the volume `FloorGroups.floorVolume b` of V_b or the measure `F.floorQuadricMeasure b`
of a quadric in V_b. In the coordinates of the basis `F.floorBasis b`, ρ is solved in every block of
`F.blockRank` distinct orthonormal basis vectors. That is, the other coordinates are free, and over
each of their values the points of the block with all coordinates in `Γ.ofSize j` have mass at most
Λ^(`F.blockRank` (j+1)), where Λ = `Γ.loss` is the constant of the gauge Γ. 

### `volume_pow_mul_le`

 The volume of `Γ.ofSize j` is raised to the number of coordinates of V_b lying outside X' and
outside one block of `F.blockRank` vectors. This power, times the bound Λ^(`F.blockRank` (j+1)) for
the mass in that block, is at most Λ^(99 n (j+2)), where Λ = `Γ.loss` and n = `𝔰.n`. 

### `setLIntegral_map_floorBasis_le`

 Passage to coordinates in the basis `F.floorBasis b` of V_b: the integral of `Φ` over
`Γ.vecsOfSize j` against the image of `ρ` under x ↦ `F.floorBasis b *ᵥ x` is at most the integral of
`Φ (F.floorBasis b *ᵥ x)` over x in `Γ.vecsOfSize (j + 4)` against `ρ`. 

### `setLIntegral_orthonormalPart_le`

 Let ρ be the volume of V_b, the span of the basis vectors of floor at least b, or the measure
`F.floorQuadricMeasure b` of a quadric in V_b. Let Λ = `Γ.loss`, n = `𝔰.n`, and let X' be the span
of the columns of `F.orthonormalPart`. If φ is measurable and has integral at most B over the
vectors of size j + 4 of X', then φ(y_X) has ρ-integral at most Λ^(99 n (j+6)) B over the vectors y
of size j. Here y_X = `F.orthonormalPartᴴ *ᵥ T.splitGram *ᵥ y` is the vector of the products of the
basis vectors of X' with y. 

### `skewMeasure_le_of_sub_mem_ofSize`

 Let S be a set of skew elements and u a unit such that (β - β') / u has size j + 1 for all β, β'
in S. Then S has Haar measure at most |u|^(1/2) Λ^(j+2), where |u| is the modulus of u and
Λ = `Γ.loss`. 

### `lintegral_heisenbergElem_skewMeasure_le`

 The integral over the skew variable in the Heisenberg group of floor a, with points
n = `heisenbergElem a (ω, β)`; a vector part such as ω is extended by zero to the floors at most a
(`inclMatrix`). Suppose that at each n with Φ(n) ≠ 0, w / u has size j for some w congruent to
(n⁻¹ - 1) e*_a modulo the e_b with b < a, and Φ(n) ≤ C Ψ(ω / u). Then for ω = u v the integral of Φ
over β is at most |u|^(1/2) `Γ.loss`^(j+2) C Ψ(v), and it vanishes unless v has size j. 

### `lintegral_heisenbergMeasure_le`

 The integral over the Heisenberg group of floor a, with points n = `heisenbergElem a (ω, β)`,
where ω is extended by zero to the floors at most a (`inclMatrix`). Suppose that at each n with
Φ(n) ≠ 0, v / u has size j for some v congruent to (n⁻¹ - 1) e*_a modulo the e_b with b < a, and
Φ(n) ≤ C Ψ(ω / u). Let Ψ be measurable, with integral at most I over the vectors of size j for the
volume of V_(a+1). Then the integral of Φ for `heisenbergMeasure a` is at most C B for any
B ≥ |u|^(r + 1/2) Λ^(j+2) I. Here Λ = `Γ.loss`, r is the number of coordinates of ω, and
|u|^(r + 1/2) is `F.floorModulus a u`. 

 ### Sections of the isotropic cones 

### `sectionPoint`

 The vector c n⁻¹ e*_a. For n in the Heisenberg group of floor a it is a point of the section
⟨e_a, y⟩ = c of the isotropic cone of Y^(a). 

### `sectionMeasure`

 The measure dy / dc = |c|^r dn of the section ⟨e_a, y⟩ = c, where r is the rank of Y^(a+1),
|c| = `modulus c`, and dn is `heisenbergMeasure a` carried over by `sectionPoint a c`. 

### `orbitPoint_floorWeyl_inv_mul`

 Let w = `floorWeyl a c` be the Weyl element of floor a that sends e_a to c e*_a, for a unit c.
Then the point (w⁻¹ n)⁻¹ e_a of the orbit of e_a is c n⁻¹ e*_a = `sectionPoint a c n`. 

### `PlaceData.lintegral_floorQuadricMeasure_eq`

 The measure `F.floorQuadricMeasure a.castSucc` of the isotropic cone of Y^(a) is dc times the
measures `sectionMeasure T a c` of its sections ⟨e_a, y⟩ = c, where the product is that of the form
`T` over `A` and e_a is the a-th isotropic basis vector. 

### `exists_sectionPoint_heisenbergElem_eq`

 The coordinates of a point of a section: for the Heisenberg element n = `heisenbergElem a t`
with t = (ω, β), the point c n⁻¹ e*_a is c (e*_a - ω) plus a multiple of c e_a. Here ω is extended
by zero to the floors at most a. 

### `sectionPoint_apply_eq_zero_of_floorOf_lt`

 If n fixes the basis vectors of floor below a, the coordinates of floor below a of the vector
c n⁻¹ e*_a = `sectionPoint a c n` vanish. 

### `Size.sectionPoint_mem_vecsOfSize`

 Let the isometry n of the form `T` fix the basis vectors of floor below a (`floorGroup a`), and
let z be congruent to the point c n⁻¹ e*_a = `sectionPoint a c n` modulo the e_b with b < a
(`CongrBelow a`). If all entries of z have size j for the scale `S` (`S.vecsOfSize j`), then so
have those of the point, whose coordinates of floor below a vanish. 

### `weylElem_mulVec_eStar`

 Let p be a sequence of units and a < l. The Weyl element w_p = `weylElem l p` sends e_a to
p_a e*_a, so the coordinate of w_p v at e*_a (index `eStar a`) is p_a times the coordinate of v at
e_a (index `inl a`). 

### `orbitPoint_weylElem_mul`

 For the Weyl element w_p = `weylElem (a + 1) p` of the first a + 1 hyperbolic pairs and an
isometry σ, the point (w_p σ)⁻¹ e_a of the orbit of e_a is (star p_a) σ⁻¹ e*_a. 

### `congrBelow_sectionPoint_orbitPoint`

 For n in G^(a) = `floorGroup a`, ν in U_(<a) = `unipotentBelow a` and the Weyl element
w_p = `weylElem (a + 1) p`, the vector (w_p n ν)⁻¹ e_a is congruent to
(star p_a) n⁻¹ e*_a = `sectionPoint a (star p_a) n` modulo the e_b with b < a. 

### `CongrBelow.orthonormalPart_conjTranspose_mulVec_eq`

 If ω and ω' are congruent modulo the e_b with b < l, where l ≤ ϱ, then they have the same
products with the basis vectors of X', the columns of `F.orthonormalPart`. 

### `Gauge.sectionPoint_mem_vecsOfSize_of_isNear`

 Let the head p of length a + 1 be adapted to the scale. Let y be in the box `F.boxSet`, n in the
Heisenberg group `floorUnipotent a` of floor a, and ν in U_(<a) = `unipotentBelow a`. Suppose w_p n
ν y is near at a + 1 (`F.IsNear`), that is, R^(a+1) w_p n ν y meets the box. Then the point (star
p_a) n⁻¹ e*_a, which lies in the section of the vectors v with ⟨e_a, v⟩ = star p_a, has size
`20 * 𝔰.n`: all its entries lie in `Γ.ofSize (20 * 𝔰.n)`. Here w_p = `weylElem (a + 1) p`,
R^(a+1) = `partialUnitriangularGroup (a + 1)`, and the point is `sectionPoint a (star p_a) n`. 

### `Gauge.setLIntegral_sectionMeasure_le`

 Integration over a section. If φ is measurable and has integral at most B over the vectors of
size j + 5 of X', then φ(y_X) has integral at most |c|^(-1/2) Λ^(j+3) Λ^(99 n (j+7)) B over the
points y of size j of the section ⟨e_a, y⟩ = c, for a unit c. Here
y_X = `F.orthonormalPartᴴ *ᵥ T.splitGram *ᵥ y` is the vector of the products of the basis vectors
of X', which are indexed by `F.FreeIndex`, with y; the section carries `sectionMeasure T a c`;
|c| = `modulus c`, Λ = `Γ.loss` and n = `𝔰.n`. 
