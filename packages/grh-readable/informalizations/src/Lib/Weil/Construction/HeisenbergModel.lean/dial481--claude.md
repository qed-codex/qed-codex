---
{
  "module": "src/Lib/Weil/Construction/HeisenbergModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/HeisenbergModel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/HeisenbergModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Heisenberg cocycles, vacua, the reproducing model and Schur's lemma

This file sets up an abstract setting for the Weil representation that covers the real places
and the adeles. The data are a topological abelian group `W` with a measure `μ`, a Heisenberg
cocycle `β` on `W`, and a vacuum `e` for it. It also defines multiplier actions of a group `G` on
`W`. The vacuum defines a space of integrable functions reproduced by a kernel, on which `W` acts
by a Heisenberg representation `ρ`. The file proves superposition and Schur's lemma for this model.

## Main definitions and results

* `New.Heisenberg W`: a continuous alternating bicharacter `β`, the cocycle of a Heisenberg group.
* `New.Heisenberg.IsVacuum`: a function `e` on `W` that plays the part of the matrix coefficient of
  a vacuum vector (a Gaussian, or a lattice indicator times a semicharacter).
* `New.Heisenberg.MultiplierAction`: a group `G` acting on `W` by symmetries, with a multiplier `Δ`
  that turns a double integral of `e` and `β` attached to the action into a given `c` (by default
  `1`).
* `New.Heisenberg.IsVacuum.Model`: integrable v with v x = ∫ v y β(y, x) e(x - y), a Banach space
  for the L¹ norm, with the representation `New.Heisenberg.IsVacuum.heisenbergRep`, the vector
  `New.Heisenberg.IsVacuum.vacElem` and the form `New.Heisenberg.IsVacuum.modelInner`.
* `New.Heisenberg.IsVacuum.form_eq_mul_modelInner`,
  `New.Heisenberg.IsVacuum.eq_smul_one_of_commute`: Schur's lemma. An invariant form is a multiple
  of the inner product, and a bounded operator that commutes with the representation is a scalar.
  `New.Heisenberg.IsVacuum.integral_form_eq_mul_modelInner` treats a form given as an integral.

## Relation to the literature

Known; see `Lib.Weil.Construction.WeilOperators` for sources.



## Heisenberg cocycles, representations, vacua and multiplier actions

* `New.Heisenberg.Rep`: isometric operators `ρ x` with `ρ x ∘ ρ y = β x y • ρ (x + y)`.


### `New.Heisenberg`

 A continuous function β on W × W, W an abelian group with a topology, with values of modulus
one, multiplicative in each variable, and β(x,x) = 1. 

### `New.Heisenberg.β`

 The bicharacter `β x y`, a complex-valued function on `W × W`. 

### `New.Heisenberg.add_left`

 `β` is multiplicative in its first variable. 

### `New.Heisenberg.add_right`

 `β` is multiplicative in its second variable. 

### `New.Heisenberg.self_eq_one`

 `β` is alternating: it is `1` on the diagonal. 

### `New.Heisenberg.norm_eq_one`

 The values of `β` have modulus one. 

### `New.Heisenberg.cont`

 `β` is jointly continuous on `W × W`. 

### `Rep`

 A representation of the Heisenberg datum `H`: linear isometries `ρ x`, `x : W`, of a complex
normed space `X`, with `ρ x ∘ ρ y = β x y • ρ (x + y)` and `(x, v) ↦ ρ x v` continuous. 

### `Rep.ρ`

 The operator `ρ x` on `X` attached to the vector `x` of `W`. 

### `Rep.mul`

 The Heisenberg relation `ρ x ∘ ρ y = β x y • ρ (x + y)`. 

### `Rep.norm_map`

 Each `ρ x` is an isometry. 

### `Rep.cont`

 The map `(x, v) ↦ ρ x v` is jointly continuous on `W × X`. 

### `IsVacuum`

 The function e: W → ℂ is a vacuum for β and μ: continuous, integrable, even, real-valued,
e(0) = 1, and ∫ e(z)e(x−y−z)β(z,y)β(z+y,x) dμ(z) = e(y)e(x). 

### `IsVacuum.cont`

 `e` is continuous. 

### `IsVacuum.apply_zero`

 `e` is normalized to take the value `1` at the origin. 

### `IsVacuum.apply_neg`

 `e` is even. 

### `IsVacuum.conj_apply`

 `e` is real-valued. 

### `IsVacuum.twisted_conv`

 The key identity: the convolution of `e` with itself at `x - y`, twisted by
  `β z y * β (z + y) x`, is `e y * e x`. 

### `IsVacuum.integrable`

 `e` is integrable for `μ`. 

### `MultiplierAction`

 The action of G on W preserves β and μ, and a continuous multiplier Δ: G → ℂ has Δ(1) = 1,
Δ(g⁻¹) = conj Δ(g), Δ(g)Δ(h)Δ((gh)⁻¹) ∬ e(hx)e(ghy)β(x,y)e(x+y) = c(g,h). 

### `MultiplierAction.beta_smul`

 The action of `G` on `W` preserves `β`. 

### `MultiplierAction.measurePreserving`

 The action of `G` on `W` preserves the measure `μ`. 

### `MultiplierAction.Δ`

 The multiplier `Δ`, a complex-valued function on `G`. 

### `MultiplierAction.continuous_delta`

 The multiplier is continuous. 

### `MultiplierAction.Δ_one`

 The multiplier is `1` at the identity. 

### `MultiplierAction.Δ_inv`

 The multiplier takes inverses to complex conjugates. 

### `MultiplierAction.cocycle`

 The double integral of `e (h • x) * e ((g * h) • y) * β x y * e (x + y)` times
  `Δ g * Δ h * Δ (g * h)⁻¹` is the prescribed value `c g h` (by default `1`). 


## First properties of cocycles, representations and vacua

* `New.Heisenberg.IsVacuum.integral_norm_sq_eq_one`, `New.Heisenberg.IsVacuum.norm_le_one`: a vacuum
  has `L²` norm one and is bounded by one.


### `Rep.rho_zero_apply`

 In a Heisenberg representation, `ρ 0` is the identity. 

### `IsVacuum.integral_norm_sq_eq_one`

 A vacuum has `L²` norm one. 

### `IsVacuum.norm_le_one`

 A vacuum is bounded by one in absolute value. 


## A Heisenberg representation twisted by a group element

A group `G` acting on `W` and preserving the bicharacter `β` (a part of
`New.Heisenberg.MultiplierAction`) twists any Heisenberg representation: `New.Heisenberg.Rep.moveBy`
is `x ↦ ρ (g • x)`.


### `moveBy`

 The representation `x ↦ R.ρ (g • x)`; it is again a representation of `H` because `g` preserves
`β`. 


## The L¹ reproducing model of a vacuum and Schur's lemma

* `New.Heisenberg.Rep.integrated`: the integrated action ∫ v y • R.ρ y f on any representation R.
* `New.Heisenberg.IsVacuum.map_eq_integral`, `New.Heisenberg.IsVacuum.hom_ext` (superposition):
  every v is the integral of the translates of the vacuum against v, so these translates determine
  bounded maps.
* `New.Heisenberg.IsVacuum.integrated_eq_smul`: in the model itself, the integrated action of v on
  w is w(0) • v.


 ### The space and its norm 

### `IsVacuum.norm_beta_mul_le_one`

 The kernel β(y, x) e(x - y) of the reproducing identity of a vacuum e has norm at most one. 

### `IsVacuum.norm_mul_beta_mul_le`

 Multiplication by the kernel β(y, x) e(x - y) does not increase the absolute value. 

### `IsVacuum.integrable_mul_kernel`

 For an integrable f, the function y ↦ f(y) β(y, x) e(x - y) (f times the kernel of the
reproducing identity) is integrable: the kernel is continuous and has norm at most one. 

### `IsVacuum.modelSubmodule`

 The complex subspace of integrable functions v on W satisfying the reproducing identity v(x) = ∫
v(y) β(y,x) e(x−y) dμ(y) for every x. 

### `IsVacuum.Model`

 The space of integrable v with v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y), as a type; it carries the
L¹ norm. 

### `IsVacuum.toL1`

 The complex-linear map sending a function in the reproducing space to its class in L¹(W, μ). 

### `norm_eq_integral_norm`

 For a vacuum `e` of `H` and `μ`, the model `Model H` is the space of integrable `v` with
v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y). The norm of the model is the L¹ norm ∫ ‖v x‖ dμ. 

### `Model.integral_mul_beta_mul_eq`

 The reproducing identity of an element v of the model: ∫ v(y) β(y, x) e(x - y) dμ(y) = v(x). 

### `norm_apply_le`

 An element of the model is bounded by its L¹ norm. 

### `continuous`

 Let e be a vacuum for β and the measure μ. Every element of `Model H`, the space of
integrable v with v(x) = ∫ v(y) β(y,x) e(x−y) dμ(y), is a continuous function on `W`. 

 ### The representation, the vacuum vector and the inner product 

### `heisenbergRep`

 The Heisenberg representation on the model: y acts by the L¹ isometry that sends v to
x ↦ β(y, x) v(x - y), see `New.Heisenberg.IsVacuum.heisenbergOp_apply`. 

### `heisenbergOp`

 For `x` in `W`, the bounded operator on the reproducing space sending `v` to the function
`z ↦ β x z * v (z - x)`. 

### `vacElem`

 The function e itself, viewed as an element of the reproducing space it defines. 

### `valueAt`

 The continuous linear functional on `Model H` that evaluates an element at the point `x`. 

### `kernelIntegral`

 For σ an isometric ring endomorphism of ℂ and strongly continuous linear contractions K(y):
X → Y, the bounded σ-semilinear map v ↦ (x ↦ ∫ σ(v(y)) K(y)x dμ(y)) on the reproducing
space. 

### `modelInner`

 The bounded sesquilinear form on the reproducing space sending (v, w) to ∫ conj(v) w dμ,
conjugate-linear in the first argument. 

### `integrable_norm_sq`

 The function ‖v(·)‖² is integrable for v in the model: v is integrable and bounded by its
norm. 

### `conj_modelInner`

 The inner product is Hermitian: conj ⟨v, w⟩ = ⟨w, v⟩. 

### `modelInner_heisenbergOp`

 The Heisenberg operators preserve the inner product of the model. 

### `modelInner_heisenbergOp_vacElem`

 Reproducing property: for v in the reproducing space of a vacuum e and x in W, the inner
product ⟨ρ(x)vac, v⟩ equals v(x). 

### `eq_zero_of_modelInner_self`

 The inner product of the model is definite: if ⟨v, v⟩ = 0, then v = 0. 

### `instance : CompleteSpace he.Model`

 The model is complete, hence a Banach space. 

 ### The integrated action 

### `Rep.integrated`

 The integrated action of the model on a representation R in a complex Banach space X: the
bounded bilinear map (v, f) ↦ ∫ v(y) • R.ρ y f dμ(y), see `New.Heisenberg.Rep.integrated_apply`. 

### `Rep.map_integrated_eq_integral`

 A bounded operator T passes under the integral that defines the integrated action. 

### `Rep.integrated_heisenbergOp`

 The integrated action turns the operator ρ(x) of the model into the operator R.ρ x. 

### `Rep.map_integrated`

 A bounded operator T from X to Y that intertwines the representations R and R' commutes with
their integrated actions. 

 ### Bounded maps and invariant forms on the model 

### `integrated_apply_eq_integral`

 For a representation R on the model itself, the value at x of the integrated action of v on w
is ∫ v(y) (R.ρ y w)(x) dμ(y). 

### `integrated_vacElem`

 Integrating the translates ρ(y) vac of the vacuum against v gives back v: the reproducing
identity in operator form. 

### `map_eq_integral`

 Superposition: for a bounded linear map T from the reproducing space to a complex Banach space
and any v in the reproducing space, Tv = ∫ v(y) T(ρ(y)vac) dμ(y). 

### `hom_ext`

 Two bounded operators from the model to a Banach space that agree on the translates ρ(y) vac
of the vacuum are equal. 

### `integrated_eq_smul`

 For v, w in the reproducing space of a vacuum e, with its Heisenberg representation ρ, one
has ∫ v(y) ρ(y)w dμ(y) = w(0)·v.

A special case of the Moyal identity (orthogonality relations for the Heisenberg representation), in
operator form with one vector the vacuum. 

### `eq_smul_one_of_commute`

 Schur's lemma for the model: a bounded operator that commutes with the Heisenberg operators is a
scalar, namely the value at `0` of the image of the vacuum. 

### `exists_lift`

 A bounded continuous K from W to a Banach space X yields a bounded linear map L from the model
to X (in the proof, L v = ∫ v y • K y) that behaves as if it sent the translate
`heisenbergOp y vacElem` of the vacuum to K y: if bounded maps M, N into the Banach space Y satisfy
M (K y) = N (heisenbergOp y vacElem) for all y, then M ∘ L = N. 

### `integral_form_eq_mul_modelInner`

 Uniqueness of the invariant form, a form of Schur's lemma for the Heisenberg representation. Let
W be a locally compact, second countable abelian group with Haar measure μ, and let e be a vacuum
for the bicharacter β of `H` and μ. Let `Model H` be the space of integrable v with v(x) = ∫ v(y)
β(y,x) e(x−y) dμ(y), and let ρ(x) = `heisenbergOp x` send v to z ↦ β(x,z) v(z−x). If B_z (z ∈ Z) are
bounded sesquilinear forms on `Model H`, each z ↦ B_z(v,w) is ν-integrable, and ∫B_z dν is invariant
under all ρ(x), then ∫B_z(v,w) dν = (∫B_z(e,e) dν)·⟨v,w⟩, where ⟨v,w⟩ = ∫ conj(v) w dμ. 

### `form_eq_mul_modelInner`

 Schur's lemma for a single form: if W is locally compact, a bounded sesquilinear form B on the
reproducing space that is invariant under all ρ(x) is B(vac, vac) times the inner product. 
