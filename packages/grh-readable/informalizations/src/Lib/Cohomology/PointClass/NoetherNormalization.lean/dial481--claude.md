---
{
  "module": "src/Lib/Cohomology/PointClass/NoetherNormalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/NoetherNormalization.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cohomology/PointClass/NoetherNormalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Projective Noether normalisation and homogeneous coordinates of embedded points

Let k be a field. For a tuple `g : ι → L`, `New.Variety.CutsOutLocus.IsHomogeneousSolution k g w`
says that every homogeneous polynomial over k that vanishes at g also vanishes at w. The file proves
projective Noether normalisation by linear forms in characteristic zero and constructs its Galois
closure.

## Main definitions and results

* `New.Variety.CutsOutLocus.IsNoetherNormalization Λ g`: the linear forms `Λ₀, …, Λ_d` are a Noether
  normalisation of the cone, that is, their values at `g` are independent and the cone is integral
  over them.
* `New.Variety.CutsOutLocus.exists_isNoetherNormalization`: such forms exist for a non-zero finite
  tuple `g` over a field `k` of characteristic zero.
* `New.Variety.CutsOutLocus.IsNoetherNormalization.GaloisClosure`,
  `New.Variety.CutsOutLocus.IsNoetherNormalization.nonempty_galoisClosure`: the Galois closure of
  the normalisation, a finite algebra `B` over `k[X₀, …, X_d]` with points `b σ` of the cone,
  indexed by a finite group.
* `New.Variety.IsCoordsWithUnit.exists_universal_chart`,
  `New.Variety.IsCoordsWithUnit.exists_mem_open_of_isUnit`: a point ξ over a field F with
  coordinates g spreads out and specialises to the vectors w with w i (resp. aeval w b) a unit that
  satisfy the homogeneous relations of g.
* `New.Variety.IsCoordsWithUnit.exists_app_eq_algebraMap_of_isHomogeneousSolution`: over an
  algebraically closed k, a global function takes one constant value on all such specialisations.

Notions from other files:
* `New.LineBundle.IsHomogeneousCoords`: v is a vector of homogeneous coordinates of the point t for
  L: t lands in U_j exactly when v_j is a unit, and then g_jk(t) = v_k/v_j.
* `New.Variety.IsOpenSubfunctor`: V is an open subfunctor of X: each x ∈ X(A) has an ideal I of A
  such that, for φ: A → B, φ(x) ∈ V(B) iff φ(I)B = B.

## Relation to the literature

Known; see `Lib.Cohomology.PointClass.LinearIndependence` for sources.



## Noether normalisation of a cone by linear forms

Noether normalisation is stated for coordinate vectors instead of varieties. A tuple `g : ι → L`
stands for the cone cut out by the homogeneous polynomials over `k` that vanish at `g`.


 ### The cone of a coordinate vector 

### `IsHomogeneousSolution`

 The point `v` lies on the cone of `g`: every homogeneous polynomial over `k` that vanishes at
`g` vanishes at `v`. The two tuples may have entries in different `k`-algebras. 

### `evalForms`

 The tuple of values of the polynomials `Λ j` at `v`. 

### `aeval_smul_of_isHomogeneous`

 A homogeneous polynomial of degree `n` takes at `u • v` the value `u ^ n` times that at `v`. 

### `IsHomogeneousSolution.of_ker`

 If `χ` kills the kernel of `φ` and `φ ∘ v` lies on the cone of `g`, then so does `χ ∘ v`. 

### `IsHomogeneousSolution.aeval_eq_zero_of_transcendental`

 If `t` is transcendental over the ring `B` of the entries of `g`, every polynomial that
vanishes at `t • g`, homogeneous or not, vanishes at each point `v` of the cone of `g`. 

### `isIntegralElem_of_valuationSubring`

 An element of a field `L` that lies in every valuation ring containing the image of `f` is
integral over that image. 

 ### Noether normalisation 

### `IsNoetherNormalization`

 Λ is a Noether normalisation of g: the Λ_0, …, Λ_d are linear forms, the values Λ_j(g) have no
non-zero homogeneous relation, and every field-valued point v of the cone of g is integral over
any image of a `k`-algebra that contains the values Λ_j(v). 

### `exists_algHom_comp_eq_of_integral`

 Let `φ : A → C` be integral and `ψ : A → L` a map to an algebraically closed field whose
kernel contains that of `φ`. Then `ψ = χ ∘ φ` for some map `χ : C → L` of `k`-algebras. 

### `exists_galois_hull`

 Finitely many elements of an algebraically closed field, integral over a noetherian normal
domain `A` of characteristic zero, lie in a finite `A`-algebra `B` whose ring of invariants is
`A`. 

### `aeval_eq_zero_of_eliminated_forms`

 Elimination step of Noether normalisation. If the values of the linear forms `Λ` at `g` satisfy
a homogeneous relation `f`, and `a` is a point with `f a ≠ 0` and `a 0 ≠ 0`, then on the cone of `g`
a common zero with entries in a field `K` of the forms `Λ (j + 1) - (a (j + 1) / a 0) • Λ 0` is a
common zero of `Λ`. 

### `isIntegralElem_of_no_common_zero`

 If linear forms `Λ` have no non-trivial common zero on the cone of a finite tuple `g` over any
field, then a point `v` of the cone with `Λ v = φ ∘ p` has coordinates integral over the image of
`φ`. 

### `exists_isNoetherNormalization`

 Noether normalisation. Let `g` be a non-zero tuple, indexed by a finite type `ι`, in a field `L`
over a field `k` of characteristic zero. Then there are linear forms `Λ₀, …, Λ_d` over `k` with
`Λ₀(g) ≠ 0` that form a Noether normalisation of `u • g` for every unit `u` of `L`. This means the
values `Λ_j(u • g)` satisfy no non-zero homogeneous polynomial relation over `k`, and every
field-valued point `v` on the cone of `u • g` is integral over any image of a `k`-algebra that
contains the values `Λ_j(v)`. 

### `exists_algEquiv_of_comp_eq`

 Let `A` be the ring of invariants of the finite group of `A`-automorphisms of `B`. Two maps
of `k`-algebras from `B` to a field (`k` of characteristic zero) that agree on `A` differ by such an
automorphism. 

### `ker_aeval_le_ker_aeval_smul_of_transcendental`

 Let `t` be transcendental over `L`, `j : B → Ω` a map of `k`-algebras with zero kernel, and `b`
a tuple over `B` with `j ∘ b = t • w` for a tuple `w` of elements of `Ω` integral over `L`. Every
polynomial relation of `b` holds for `u • φ ∘ b`, for every map `φ` of `k`-algebras from `B` to a
field `K` and every `u`: the relation splits into homogeneous relations of `w`, which `b`
satisfies. 

### `isIntegral_aeval_of_evalForms_eq`

 Let `f : k[X₀, …, X_d] → B` be finite and `b` a family of tuples over `B` such that `Λ` takes
the tuple `b σ₀` to `f ∘ X`. Then `aeval b` is integral: composed with the substitution of the
forms `Λ` in the variables `(σ₀, i)`, it is `f`. 

### `exists_algHom_comp_eq_smul`

 Let `t` be transcendental over `L`, `j : B → Ω` a map of `k`-algebras with zero kernel, and each
tuple `t⁻¹ • j ∘ b σ` integral over `L`. Let `B` be finite over `k[X₀, …, X_d]` by `f`, with
`Λ` taking `b σ₀` to `f ∘ X`. Then for every map `φ` from `B` to an algebraically closed field
and every `u`, some map `χ` from `B` has `χ ∘ b σ = u • φ ∘ b σ` for all `σ`. 

### `IsNoetherNormalization.GaloisClosure`

 The Galois closure of a Noether normalisation `Λ` of a finite tuple `g`: a finite group `G`, a
finite injective map `f : k[X₀, …, X_d] → B` of `k`-algebras and tuples `b σ` over `B`, `σ ∈ G`, on
the cone of `g`, that `Λ` takes to the variables and that `G` permutes up to proportionality. 

### `IsNoetherNormalization.GaloisClosure.G`

 The finite group that permutes the tuples `b σ`. 

### `IsNoetherNormalization.GaloisClosure.B`

 The algebra over `k[X₀, …, X_d]` in which the tuples lie. 

### `IsNoetherNormalization.GaloisClosure.fintype`

 The group `G` is finite. 

### `IsNoetherNormalization.GaloisClosure.f`

 The map from `k[X₀, …, X_d]`. 

### `IsNoetherNormalization.GaloisClosure.b`

 The tuples, indexed by `G`. 

### `IsNoetherNormalization.GaloisClosure.isHomogeneousSolution`

 Each `b σ` lies on the cone of `g`. 

### `IsNoetherNormalization.GaloisClosure.evalForms_eq`

 The forms `Λ` take each `b σ` to the variables: `Λ j (b σ) = f (X j)`. 

### `IsNoetherNormalization.GaloisClosure.finite`

 The map `f` is finite. 

### `IsNoetherNormalization.GaloisClosure.injective`

 The map `f` is injective. 

### `IsNoetherNormalization.GaloisClosure.exists_shift`

 If `φ`, `ψ` map `B` to an algebraically closed field and `ψ (f (X j)) = u φ (f (X j))` for
  all `j`, then for some `τ ∈ G`, `ψ (b σ) = u φ (b (τ σ))` for all `σ`. 

### `IsNoetherNormalization.nonempty_galoisClosure`

 A Noether normalisation `Λ` of a finite tuple `g` with entries in a field `L`, over a field `k`
of characteristic zero, has a Galois closure
(`New.Variety.CutsOutLocus.IsNoetherNormalization.GaloisClosure`). 

### `IsNoetherNormalization.exists_galois_closure`

 The Galois closure of a Noether normalisation `Λ` of a finite tuple `g` with entries in a field
`L`, over a field `k` of characteristic zero. There are a finite group `G`, a map of `k`-algebras
`f : k[X₀, …, X_d] → B` and tuples `b σ` over `B`, `σ ∈ G`, such that: (a) each `b σ` lies on the
cone of `g`, and `Λ j` takes the value `f (X j)` at it; (b) `f` is finite and injective; (c) if `φ`,
`ψ` map `B` to an algebraically closed field and `ψ (f (X j)) = u φ (f (X j))` for all `j`, then for
some `τ ∈ G` we have `ψ (b σ) = u φ (b (τ σ))` for all `σ`. 


## Homogeneous coordinates of points of an embedded variety

Points of a scheme Y over Spec R with values in k-algebras A (`New.Variety.PointsIn`) are described
by homogeneous coordinates for a line bundle L that embeds Y (`New.LineBundle.IsProjEmbedding`,
finite index set ι).


### `IsCoordsWithUnit`

 The vector v in A^ι is a vector of homogeneous coordinates, for L, of the A-point x of Y,
and some coordinate v_i is a unit. 

### `IsCoordsWithUnit.exists_chart_coords`

 If étale charts of dimension d cover Y (`IsChartCovered`), a point x over a field comes, along
some κ, from the universal point of such a chart that has coordinates with a unit entry. 

### `IsCoordsWithUnit.exists_unit_smul_eq`

 Two vectors of coordinates with a unit entry of the same point `x` differ by a unit of `A`. 

### `IsCoordsWithUnit.map_unit_smul`

 If `v` is a vector of coordinates with a unit entry of `x`, `φ : A ⟶ B` is a map of
`k`-algebras and `u` is a unit of `B`, then `u • φ ∘ v` is a vector of coordinates with a unit entry
of the image of `x` under `φ`. 

### `IsCoordsWithUnit.ext`

 Two `A`-points of `Y` with the same vector `v` of coordinates with a unit entry are equal. 

 ### Points over a field: descent, spreading out and specialisation 

### `IsCoordsWithUnit.exists_descend_of_injective`

 Descent. Let ξ be a point over a field F with coordinates g, and φ : A → F injective. If
g = g_i φ(v) for a vector v over A, then ξ comes from a point over A with coordinates v. 

### `IsCoordsWithUnit.exists_universal_chart`

 Spreading out. Let ξ be a point over a field F with coordinates g, and let v_i ≠ 0 for some v
satisfying the homogeneous relations of g. Then there are a k-algebra D, a point y over D, a map j :
D → F and polynomials G_d (d ∈ D) with two properties. (a) j is injective and ξ = j(y). (b) Let w
over a k-algebra C satisfy the homogeneous relations of g, with w_i a unit. Then some φ : D → C has
φ(d) associated to G_d(w) for all d, and φ(y) has coordinates w. 

### `IsCoordsWithUnit.exists_app_eq_algebraMap_of_isHomogeneousSolution`

 Let `Y` be a scheme over `Spec R` with a line bundle `L` embedding it in projective space, and
let `k` be an algebraically closed `R`-algebra. Let `ξ` be an `F`-point of `Y` over a field `F ⊇ k`
with `L`-coordinates `g`, one of them a unit, and let `f` be a map from the functor `A ↦ Y(A)` on
`k`-algebras to the affine line. Then there is `c ∈ k` such that `f(x) = c` for every point
`x ∈ Y(A)` over a nonzero `k`-algebra `A` whose `L`-coordinates `v` have a unit entry and lie on the
cone of `g`, i.e. every homogeneous polynomial over `k` vanishing at `g` vanishes at `v`. 

### `IsCoordsWithUnit.exists_mem_open_of_isUnit`

 Let ξ be a point over a field F with coordinates g, lying in an open subfunctor V. Some
polynomial b with b(g) ≠ 0 has the property: every w that satisfies the homogeneous relations
of g and makes b(w) a unit is a vector of coordinates of a point of V. 
