---
{
  "module": "src/Lib/Adelic/AutomorphicForms/HeckeEigenforms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/HeckeEigenforms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/HeckeEigenforms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Algebraic modular forms: delta forms, unitary translation and spanning by Hecke eigenforms

This file concerns algebraic modular forms. These are functions on a group that transform on the
left by a representation of a group `Γ` embedded in it, and on the right by a character of a level.
`New.levelSpace π K χ` is the space of vectors on which `K` acts through `χ`.

## Main definitions and results

* `New.deltaForm`: the form supported on one double coset, made from a vector. Its values are sums
  over the finite sets `New.transporter` (`New.deltaForm_apply`); `New.classSum_deltaForm` gives the
  class sum of its values under an invariant family of additive maps `W →+ ℂ`.
* `New.freeLevelEquiv`, `New.finrank_levelSpace_smoothFormRep`: at a sufficiently small level, also
  called free (all `New.classAut` trivial), forms are arbitrary families of values, so the dimension
  is the class number times `finrank ℂ W`.
* `New.Space.exists_isUnitary_formTranslation`: right translation `New.Space.formTranslation` on the
  forms `New.Space.forms` of weight `κ` has an invariant positive definite scalar product.
* `New.Space.finite_formTranslation_levelSpace`: the eigenforms of an open level for
  `New.Space.formTranslation` form a finite-dimensional space.
* `New.hasHeckePolyAt_iff`: a form has a Hecke polynomial at a split place exactly when it is
  spherical there and an eigenvector of the Hecke operators there, the polynomial being formed from
  the eigenvalues.
* `New.le_span_isSphericalOff`: a finite-dimensional Hecke-stable space of forms fixed by the
  integral points trivial at `S` is spanned by simultaneous eigenforms.

Notions from other files:
* `New.Space E n ε`: a hermitian space with a point, given by a matrix J over a field E with a CM
  structure (`CMType E`) and x in GL_n(𝔸) with xᴴJx equal to diag(ε) at the infinite places and 1 at
  the finite places; the signs `ε = 1` give the definite spaces.
* `New.Space.forms`: Algebraic modular forms of weight κ on a definite space V: functions f on G_f
  with open right stabiliser and f(γg) = ρ_κ(γ)f(g) for rational γ, ρ_κ = `New.Space.weightRep` for
  a weight κ : `New.Weight E`; values lie in `WeylIndex n κ.1 → ℂ`.
* `New.HasFiniteType Γ K`: `K` is compact and open, `Γ \ G / K` is finite and every group
  `New.classAut Γ K g`, which is `Γ ∩ g K g⁻¹`, is finite.
* `New.classSum Γ K f`: the sum over the classes `c`, with representative `g_c`, of
  `f g_c / #(Γ ∩ g_c K g_c⁻¹)`.

## Relation to the literature

Known result: Finite dimension of spaces of algebraic modular forms and the Hecke eigenforms
spanning them. Related files: `Lib.Adelic.AutomorphicForms.SmoothAlgebraicForms` and, for congruence
subgroups and level structures, `Lib.Adelic.Unitary.CongruenceLevels`.



## Algebraic forms of a level: delta forms, values on classes, dimension

Algebraic forms on a group `G` are defined for a homomorphism `e : Γ →* G` (assumed injective from
the delta forms on), a representation `ρ` of `Γ` on a complex vector space `W`, a level `K ≤ G` and
a character `χ` of `K`. They are the vectors of `New.levelSpace` for the representation
`New.smoothFormRep` of `G` by right translation. Each form is a smooth function `φ : G → W`. For an
element `φ` of the subtype `levelSpace (smoothFormRep e ρ) K χ`, `φ.val.val` is the function.


### `levelSpace_smoothFormRep_apply`

 Let `φ : G → W` be a smooth form (left equivariant for `e` and `ρ`, with open right stabiliser)
on which `K` acts by right translation through `χ`. Then `φ (e γ * g * k) = χ k • ρ γ (φ g)`. 

### `levelSpace_ext_doubleCosets`

 Let `e : Γ →* G` be a homomorphism, `ρ` a representation of `Γ` on `W` and `χ` a character of
the subgroup `K`, and let `r` be a system of representatives of the double cosets `e(Γ) \ G / K`.
Two forms of level `(K, χ)`, that is, smooth `φ : G → W` with `φ (e γ * g * k) = χ k • ρ γ (φ g)`,
are equal if they agree at every representative `r c`. 

### `evalClassReps`

 For points `r c` of `G` indexed by the double cosets `c` in `e(Γ) \ G / K`, the linear map
sending a form `φ` of level `(K, χ)` to the family of its values `c ↦ φ (r c)`. 

### `evalClassReps_injective`

 Evaluation of forms of level `(K, χ)` at representatives `r c` of the double cosets `c` in
`e(Γ) \ G / K` is injective. 

### `instance : Fact ((1 : K →* ℂ) =ᶠ[nhds 1] 1)`

 The trivial character is trivial near `1`. 

### `mem_smoothFunctions_of_eigen`

 Let `K` be an open subgroup of `G` and `χ` a character of `K` that is trivial near `1` (given as
a `Fact`). A function `f : G → W` on which each `k ∈ K` acts by right translation (`rightRegular`)
as multiplication by `χ k` is smooth, that is, has an open right stabiliser. 

 ### Forms supported on one class 

### `transporter`

 For injective `e` and `K` of finite type for `e(Γ)`, the finite set of the `γ : Γ` with
`x⁻¹ * e γ * y ∈ K`. 

### `mem_transporter_iff_and_card`

 The two properties of `transporter K e x y` given by `exists_transporter`: its elements and
their number. 

### `card_transporter`

 Let `e` be injective and `(e(Γ), K)` of finite type. Then the set `transporter K e x y` of the
`γ : Γ` with `x⁻¹ * e γ * y ∈ K` has as many elements as the stabiliser
`classAut e.range K x = e(Γ) ∩ x K x⁻¹` if `x` and `y` lie in the same double coset. It is empty
otherwise. 

### `deltaFun`

 The function `y ↦ ∑ χ (x⁻¹ * e γ * y) • ρ γ⁻¹ v`, summed over the `γ` with
`x⁻¹ * e γ * y ∈ K`, as a linear map in `v`. 

### `deltaFun_apply`

 The value of `deltaFun e ρ χ x v` at `y`, as a sum over the `γ` with `x⁻¹ * e γ * y ∈ K`. 

### `rightRegular_deltaFun`

 Right translation by `k ∈ K` multiplies `deltaFun e ρ χ x v` by `χ k`. 

### `deltaFun_map_mul`

 The function `deltaFun e ρ χ x v` is left equivariant under `Γ`. 

### `deltaForm`

 The linear map sending `v` to the form of level `(K, χ)` supported on the double coset
`e(Γ) x K` whose value at `y` is the sum of `χ (x⁻¹ * e γ * y) • ρ γ⁻¹ v` over the `γ` with
`x⁻¹ * e γ * y ∈ K`. With `γ⁻¹` in place of `γ`, this is the sum of `χ (x⁻¹ * e γ⁻¹ * y) • ρ γ v`
over the `γ` with `x⁻¹ * e γ⁻¹ * y ∈ K`. 

### `deltaForm_apply`

 The value at `y` of `deltaForm e ρ χ x v`, the form of level `(K, χ)` supported on `e(Γ) x K`,
is a sum over the `γ` in `transporter K e x y`, the finite set of `γ : Γ` with `x⁻¹ * e γ * y ∈ K`.
The summand is `χ (x⁻¹ * e γ * y) • ρ γ⁻¹ v`. 

### `sum_deltaForm_apply_rep`

 If every stabiliser `classAut e.range K g = e(Γ) ∩ g K g⁻¹` is trivial (a free level) and `r` is
a system of representatives of `e(Γ) \ G / K`, the sum over the classes `c` of the forms
`deltaForm e ρ χ (r c) (f c)` supported on `c` takes the value `f d` at `r d`. 

### `freeLevelEquiv`

 If every stabiliser `classAut e.range K g` is trivial, evaluation at representatives `r c` of
the double cosets `c` in `e(Γ) \ G / K` is a linear isomorphism from the forms of level `(K, χ)` to
the `W`-valued functions on the double cosets. The inverse sends `f` to the sum of the forms
`deltaForm e ρ χ (r c) (f c)`. 

### `freeLevelEquiv_apply`

 `freeLevelEquiv` sends a form to its values at the representatives `r c`. 

### `freeLevelEquiv_symm_apply`

 The inverse of `freeLevelEquiv` sends `f` to the sum over the classes `c` of the forms
`deltaForm e ρ χ (r c) (f c)`. 

### `classSum_deltaForm`

 Let `e` be injective, `χ` trivial near `1` and `K` of finite type for `e(Γ)`
(`New.HasFiniteType`). If additive maps `L g : W →+ ℂ` satisfy
`L (e γ * x * k) (χ k • ρ γ v) = L x v` for all `γ` and `k`, then the class sum (`New.classSum`,
over `e(Γ) \ G / K`, weighted by the inverse orders of the stabilisers) of `g ↦ L g (δ g)` is
`L x v`, where `δ = deltaForm e ρ χ x v` is the form supported on `e(Γ) x K` made from `v`. 

 ### Dimension 

### `finite_levelSpace_smoothFormRep`

 Forms embed in the `W`-valued functions on the finite set of classes, by their values at
representatives, so they span a finite-dimensional space. 

### `finrank_levelSpace_smoothFormRep`

 Let `e : Γ →* G` be injective, `K` a level of finite type for `e(Γ)` (`New.HasFiniteType`), `χ`
a character of `K` trivial near `1` and `ρ` a finite-dimensional representation of `Γ` on `W`. If
all stabilisers `classAut e.range K g = e(Γ) ∩ g K g⁻¹` are trivial, the space of smooth
`φ : G → W` with `φ (e γ * g * k) = χ k • ρ γ (φ g)` has dimension the number of double cosets
`e(Γ) \ G / K` times the dimension of `W`. 

 ## Unitarity of right translation and finiteness at open level 

### `exists_isUnitary_formTranslation`

 For a definite hermitian space `V` and a weight `κ`, the forms of weight `κ` on `V` carry a
sesquilinear form `B` that is positive definite and invariant under right translation by the finite
adelic unitary group (`New.IsUnitary`). 

### `finite_formTranslation_levelSpace`

 For an open subgroup K of the finite adelic points and a character χ of K, the forms of
weight κ on a positive definite V on which K acts through χ form a finite-dimensional
complex vector space. 


## Hecke polynomials and spanning by eigenforms for forms spherical off a finite set

The forms here live on a definite unitary space and have maximal level off a finite set `S`.

`New.Gf` is the finite adelic unitary group, `New.stdLevel` its integral points,
`New.maxCompactAt n w` those supported at `w, w̄`, `New.Gf.trivialOn n S` the elements trivial at
`S`.

* `New.exists_inf_trivialOn_le`: an open subgroup contains the integral points trivial at some
  finite set `S`, which avoids each `w, w̄` for which the subgroup contains `maxCompactAt n w`.


### `exists_inf_trivialOn_le`

 For an open subgroup `H` of the finite adelic unitary group there is a finite set `S` of
places such that (a) neither `w` nor its conjugate is in `S` when `H` contains `maxCompactAt n w`,
the integral points supported at `w, w̄`, and (b) `H` contains all integral points (`stdLevel E n`)
that are trivial at `S`. 

### `eventually_maxCompactAt_le`

 An open subgroup `K` of the finite adelic group contains `maxCompactAt n v`, the integral
elements supported at `v` and its conjugate, for almost all places `v`. 

### `hasHeckePolyAt_iff`

 A form f has Hecke polynomial P at a split place w (`New.HasHeckePolyAt`) if and only if f is in
`sphericalAt` at w (is fixed by the integral points K_w supported at w, w̄) and there are scalars
t_j with T_{w,j} f = t_j f for the Hecke operators T_{w,j} = `heckeSplit (V.formTranslation κ) hw j`
at w acting on forms (they commute with the inclusion of forms in functions) and P = Σ_{j ≤ N}
(−1)^j q_w^{j(j−1)/2} t_j X^{N−j} with N = `Fintype.card n`, which is `heckePoly w.q N t`. 

### `offPartComap`

 For a split place `w` and an open subgroup `H`, the preimage of `H` under the endomorphism of
the finite adelic unitary group that replaces the components at `w` and `w̄` by `1`. 

### `le_span_isSphericalOff`

 Let `V` be a definite hermitian space, `κ` a weight, `S` a finite set of finite places and `M` a
finite-dimensional space of forms of weight `κ` on `V`. Suppose that the integral points trivial at
`S` (`stdLevel E n ⊓ trivialOn n S`) fix `M` pointwise, and that `M` is stable under the Hecke
operators `T_{w,j} = heckeSplit _ hw j` at all split `w` with `w, w̄ ∉ S`. Then `M` is spanned by
its elements f with `IsSphericalOff S f P` for some `P`: f is nonzero, fixed by
`stdLevel E n ⊓ trivialOn n S`, and has a Hecke polynomial `P w` at each such `w`. 
