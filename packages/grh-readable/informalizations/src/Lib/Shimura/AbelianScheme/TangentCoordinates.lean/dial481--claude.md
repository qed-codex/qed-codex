---
{
  "module": "src/Lib/Shimura/AbelianScheme/TangentCoordinates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/TangentCoordinates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/TangentCoordinates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Étale coordinates at zero, infinitesimal points and unramified torsion

Let A be a commutative group scheme over S with an action of a ring O. The file studies the tangent
space of A at 0 through coordinate functions evaluated at points that vanish modulo a square-zero
ideal.

## Main definitions and results

* `New.IsSqZeroExt`, `New.IsInfinitesimal`, `New.tangentCoords`: square-zero extensions ψ, points
  that vanish modulo ker ψ, and their coordinates z(y) − z(0).
* `New.IsEtaleChart`, `New.exists_isEtaleChart`: étale coordinates; they exist on a smooth scheme.
* `New.IsLieChart`, `New.exists_isLieChart`: coordinates at 0 that are additive on infinitesimal
  points and in which O acts by matrices.
* `New.HasSignature`, `New.HasSignature.of_points`: the rank-one signature condition for ρ, b, b' on
  these matrices passes from a jointly injective family of ring maps to every map φ into a local
  ring for which φ(ρ b − ρ b') is a unit.
* `New.Variety.eq_zero_of_nsmul_eq_zero_of_comp_eq_zero`: torsion of invertible order in an abelian
  scheme over a local ring is unramified. The ideal I cutting out the locus where the section
  vanishes satisfies I ≤ I² by
  `New.IsInfinitesimal.eq_zero_of_isUnit_and_nsmul_eq_zero_of_cast_eq_zero`, so I = 0 by Nakayama's
  lemma.

Notions from other files:
* `New.IsAbelianScheme`: a commutative group scheme A over S is abelian if it is smooth and proper
  over S and multiplication by every m ≠ 0 is surjective.

## Relation to the literature

Known; see `Lib.Shimura.AbelianScheme.IsogenyFlatness` and `Lib.Shimura.ThetaModuli.UniversalFamily`
for sources.



## Étale coordinates at 0, the Lie action and infinitesimal points

The tangent space at 0 of a commutative group scheme A over S, through coordinates. The coordinate
functions are sections over an open V. They are evaluated at ring-valued points through
`New.PointFn.ofSection`. `New.LandsIn t V` says that the point t lands in the open V, `AddObj A`
makes A a commutative group scheme over S (group structures on all Hom(T, A), functorial in T), and
`New.ModuleObj O A` is an action of the ring O on A (O-module structures on all groups Hom(T, A),
functorial in T).


 ### Square-zero extensions, charts and the conditions on the Lie action 

### `exists_isAffineOpen_landsIn`

 A point of X with values in a local ring B lands in some affine open of X. 

### `IsSqZeroExt`

 The ring homomorphism ψ is surjective and its kernel has square zero. 

### `IsSqZeroExt.coe_surjective`

 ψ is surjective. 

### `IsSqZeroExt.mul_eq_zero`

 The product of two elements of ker ψ is zero. 

### `IsInfinitesimal`

 For ψ : C → C', the C-point y of the group scheme A becomes 0 in A(C'). 

### `tangentCoords`

 For a C-point y of A over t : Spec C → S and functions z_i on the open V, the entry
z_i(y) − z_i(0) in C; a function takes the value 0 at a point that does not land in V. 

### `IsEtaleChart`

 The z_i are regular on V and étale coordinates for f: along square-zero extensions C → C',
points in V lift uniquely over S with any prescribed lifts of the values z_i. 

### `Variety.sqZeroReduction`

 The morphism Spec R → Spec(R ⊕ M) induced by the projection of the trivial square-zero
extension R ⊕ M onto R. 

### `isSqZeroExt_fstHom`

 The projection R ⊕ M → R of the trivial square-zero extension is a square-zero extension. 

### `IsLieChart`

 The functions z are coordinates at 0 over s : Spec B → S in which O acts by the matrices m:
(a) the z_i are étale coordinates on V; for every ring map φ : B → C, with t : Spec C → S the
induced point, (b) the zero C-point of A lies in V, and, for C-points y, x that vanish modulo a
square-zero ideal and dz = `New.tangentCoords z`, (c) dz(ay) = φ(m(a)) dz(y) for a in O and
(d) dz(y + x) = dz(y) + dz(x). 

### `HasSignature`

 The signature condition for a ring map ρ : O → R, elements b, b' of O and square matrices m(a)
over R: some vector X with a unit coordinate has m(a)X = ρ(a)X for all a in O, and
m(b) − ρ(b')·1 = Xξᵀ for some vector ξ. 

 ### Existence of charts; the signature condition 

### `IsSqZeroExt.surjective_and_mul_eq_zero`

 The two conditions of `New.IsSqZeroExt` as one conjunction. 

### `IsSqZeroExt.isNilpotent_ker`

 The kernel of a square-zero extension ψ is a nilpotent ideal: its square is zero. 

### `IsSqZeroExt.surjective_specMap`

 For a square-zero extension ψ : C → C', the map Spec C' → Spec C is surjective. 

### `IsSqZeroExt.landsIn_of_comp`

 For a square-zero extension ψ : C → C', a point y : Spec C → X lands in the open V if its
restriction along Spec C' → Spec C does. 

### `exists_isEtaleChart`

 If f : X → S is smooth of relative dimension d, every point x of X has an open neighbourhood
V on which some d functions are étale coordinates for f. 

### `HasSignature.of_points`

 Let `ρ : O → B` be a ring map, `b, b'` elements of `O`, and `m(a)` square matrices over `B`
indexed by `ι`. `New.HasSignature` means that some vector `X` with a unit coordinate has
`m(a)X = ρ(a)X` for all `a`, and `m(b) − ρ(b')·1 = Xξᵀ` for some vector `ξ`. If ring maps
`σ n : B → D` with jointly trivial kernel are such that this holds after applying each `σ n`, then
it holds after applying every `φ : B → C` with `C` local and `φ(ρ(b) − ρ(b'))` a unit. 

### `IsInfinitesimal.map_comp_left`

 A C-point y of A over t : Spec C → S that is infinitesimal for ψ : C → C' restricts to the zero
point along Spec C' → Spec C. 

### `IsInfinitesimal.precomp`

 Let y be a C-point of A over t : Spec C → S that is infinitesimal for ψ : C → C', and let a be
the morphism over S induced by a ring map χ : C → D. If φ : D → B and κ : C' → B satisfy
χ ≫ φ = ψ ≫ κ, the pull-back a ≫ y is infinitesimal for φ. 

 ### Points that vanish modulo a square-zero ideal 

### `existsUnique_tangentCoords_eq`

 Let z be étale coordinates on an open V of A containing the zero C-point (over
t : Spec C → S), and ψ a square-zero extension out of C. For every vector l with entries in ker ψ
there is exactly one C-point y that vanishes modulo ker ψ and has z(y) − z(0) = l. 

### `tangentCoords_comp`

 Let the open V contain the zero C-point, and let y be a C-point that is infinitesimal for a
square-zero extension ψ. For the morphism a over S induced by a ring map χ : C → D, the
coordinates z(a ≫ y) − z(0) are those of y mapped by χ. 

### `map_tangentCoords_eq_zero`

 The coordinates z(y) − z(0) of a C-point y that is infinitesimal for the square-zero extension
ψ lie in ker ψ; here z are étale coordinates on V, which contains the zero C-point. 

### `eq_zero_of_tangentCoords_eq_zero`

 A C-point y that is infinitesimal for the square-zero extension ψ and has coordinates
z(y) − z(0) = 0 is zero; here z are étale coordinates on V, which contains the zero C-point. 

 ### Coordinates at 0 

### `IsLieChart.isEtaleChart`

 The functions z of a chart at 0 (`New.IsLieChart`) are étale coordinates on V. 

### `IsLieChart.zero_landsIn`

 For a chart at 0 over s : Spec B → S and the point t = Spec φ ≫ s of a ring map φ : B → C,
the zero C-point of A lies in V. 

### `IsLieChart.tangentCoords_smul`

 For a chart at 0 over s with matrices m, the point t = Spec φ ≫ s, and a C-point y that is
infinitesimal for a square-zero extension ψ: dz(a y) = φ(m(a)) dz(y) for a in O, where
dz = `New.tangentCoords z`. 

### `IsLieChart.tangentCoords_add`

 For a chart at 0 over s, the point t = Spec φ ≫ s, and C-points y, x that are infinitesimal
for a square-zero extension ψ: dz(y + x) = dz(y) + dz(x), where dz = `New.tangentCoords z`. 

### `IsLieChart.of_isEtaleChart`

 The four conditions of a chart at 0, each with its own quantifiers, give `New.IsLieChart`. 

### `exists_isLieChart`

 Coordinates at 0 exist. Let `A` be a commutative group scheme over `S` with an action of `O`,
smooth of relative dimension `g`, and let `s : Spec B → S` with `B` local. Then there are an open
`V` of `A`, functions `z : Fin g → Γ(A, V)` and `g × g` matrices `m(a)` over `B` (for `a` in `O`)
such that, for every ring map `φ : B → C` with induced point `t = Spec φ ≫ s`, `New.IsLieChart`
holds with the matrices `φ(m(a))`: the `z_i` are étale coordinates on `V`, the zero `C`-point lies
in `V`, and on `C`-points vanishing modulo a square-zero ideal the differentials `dz` are additive
and `a` acts on them by `φ(m(a))`. 

### `IsInfinitesimal.eq_zero_of_isUnit_and_nsmul_eq_zero_of_cast_eq_zero`

 Let A → S be smooth of constant relative dimension, let t : Spec C → S factor through
s : Spec B → S with B local, let the C-point y of A vanish modulo the square-zero ideal ker ψ,
and let m ∈ ℕ. If m is invertible in C, my = 0 forces y = 0; if m = 0 in C, my = 0. 

### `IsInfinitesimal.eq_zero_of_nsmul_eq_zero`

 Let A → S be smooth of constant relative dimension, let t : Spec C → S factor through
s : Spec B → S with B local, and let the C-point y of A vanish modulo the square-zero ideal ker ψ.
If m is invertible in C, then my = 0 forces y = 0. 

### `IsInfinitesimal.nsmul_eq_zero`

 Let A → S be smooth of constant relative dimension, let t : Spec C → S factor through
s : Spec B → S with B local, and let the C-point y of A vanish modulo the square-zero ideal ker ψ.
If m = 0 in C, then my = 0. 

 ## Unramified torsion sections 

### `New.Variety.eq_zero_of_nsmul_eq_zero_of_comp_eq_zero`

 Let B be an abelian scheme of relative dimension g over a local ring R and m a natural number
invertible in R. A section x with mx = 0 that vanishes at some point of Spec R with values in a
nonzero ring K is zero. 
