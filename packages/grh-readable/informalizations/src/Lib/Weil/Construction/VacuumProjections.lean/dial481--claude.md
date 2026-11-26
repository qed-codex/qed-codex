---
{
  "module": "src/Lib/Weil/Construction/VacuumProjections.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vacuum projections and the finite part of the Weil representation

This file studies the projection P^S = `New.Space.projOn` S on the vectors that are vacua above a
set S of finite places. It shows that P^S is a self-adjoint projection and relates it to the
Heisenberg operators and to the Weil representation. It defines the finite part
`New.Space.finitePart` and shows that this subspace is stable under ϱ_f, under the projections and
under the finite unitary group. It also shows that the translates of the vacuum by representatives
modulo Ô^n form an orthonormal spanning family of the finite part.

The Weil representation ω of the adelic unitary group acts on 𝒮(V) = `New.𝒮`, together with the
Heisenberg operators ϱ(y) = `New.Space.ϱ` y. The operators of finite vectors,
ϱ_f = `New.Space.finHeisenbergOp`, are normalised to represent Ô^n = `New.stdLattice`:
ϱ_f(y) = `semichar` y • ϱ(`finVec` y), where finVec y has real part 0 and finite part αy (α the
finite idele of the Weil data) and `semichar` y is a root of unity, and vac = `New.Space.vacElem` is
the vacuum; ψ₀ = `selfDualAddChar E` is a character of 𝔸f E trivial on Ô, `half` is ½, and
`traceOneAdele` t satisfies t + t̄ = 1. For a set S of finite places of E, P^S = `New.Space.projOn`
S is the mean of ϱ_f(`idem` T • y) over y ∈ Ô^n, where `idem` T is the finite adele equal to 1 above
T and 0 elsewhere, for T = S ∪ S̄ = `Set.conjClosure` S; it projects onto the vectors that are vacua
above S. The finite part `New.Space.finitePart` is the span of the ϱ_f-translates of vac.

## Main definitions and results

* `New.Space.omega_projOn`, `New.Space.projOn_omega`: ω(g) commutes with P^S if g is integral on S;
  P^S ω(g) is a scalar on the image of P^S if g is supported above S.
* The finite part is stable under ϱ_f, under the projections `New.Space.projOn` and under the finite
  unitary group (`New.Space.omega_mem_finitePart`). The real vacuum projection `New.Space.projReal`
  fixes it.
* `New.Space.dataInner_finHeisenbergOp_rep_vacElem`, `New.Space.span_finHeisenbergOp_rep_vacElem`:
  the translates of vac by representatives of the classes modulo Ô^n are orthonormal and span the
  finite part.
* `New.Space.exists_eq_smul_omega_vacElem`: a vector of the finite part fixed by the lattice `g Ô^n`
  is a multiple of `ω(g) vacElem`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Space.vacElem`: The vacuum: the function e (Gaussian times twisted lattice indicator) as an
  element of 𝒮(V).

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` and `Lib.Weil.Fock.OscillatorPair` for sources.



## Projections on vacua above a set of places and at infinity

* `New.Space.projOn_projOn`, `New.Space.dataInner_projOn`, `New.Space.projOn_val`: P^S is a
  self-adjoint projection and multiplies values by an indicator function.

`New.Space.integrated` v f = v ⊗ f = ∫ v(y) ϱ(y) f over real vectors y, for v in Fock space. In the
statements, `v` is a vector of this Fock space. So is `w`, except where it is bound as a finite
place of E (as in `∀ w ∈ S`).


### `heisenbergRep_left_rho`

 On the real factor of the splitting `adelicSum E s` of adelic vectors into real coordinates (in
ℂ, indexed by infinite place × coordinate) and finite coordinates (n → 𝔸f E), the Heisenberg
representation acts at a real vector `y` by `ϱ (realVec y)`. 

### `heisenbergRep_right_rho`

 On the finite factor of the splitting `adelicSum E s`, the Heisenberg representation acts at a
finite vector `y` by `ϱ (finVec y)`. 

### `rho_finVec_rho_finVec`

 Two Heisenberg operators at finite vectors compose to the operator at the sum, times the
character value `selfDualAddChar E (half * star y ⬝ᵥ x)`. 

### `finHeisenbergOp_finHeisenbergOp`

 The normalised finite operators `finHeisenbergOp` compose to the operator at the sum, times the
character value `selfDualAddChar E (star traceOneAdele * star y ⬝ᵥ x)`. 

### `dataInner_finHeisenbergOp`

 The operator `finHeisenbergOp x` preserves the inner product `dataInner` of `𝒮 V`. 

### `semichar_ne_zero`

 The scalar `semichar x` that normalises `finHeisenbergOp x` is a value in the unit circle, so it
is not zero. 

### `exists_isOfFinOrder_finHeisenbergOp_eq_smul_rho`

 For a finite adelic vector `y`, the finite Heisenberg operator ϱ_f(y) = `finHeisenbergOp y`
equals ζ • ϱ(`finVec y`) for some complex number ζ of finite order. Here `finVec y` is the adelic
vector with zero real part and finite part αy, where α is the finite idele in the Weil data
`WeilData E`. 

### `finHeisenbergOp_eq_rho_of_dotProduct_self_eq_zero`

 For a finite adelic vector y with y* y = 0, the finite Heisenberg operator ϱ_f(y) on 𝒮(V) equals
the Heisenberg operator ϱ of the adelic vector `finVec y = (0, αy)`. This vector has zero real part
and finite part αy, where α is the finite idele of the Weil data. 

### `rho_swap`

 Two Heisenberg operators commute up to the square of the bicharacter `β` of the adelic
Heisenberg group. 

### `rho_integrated`

 A Heisenberg operator at a vector `y` with zero real part commutes with `integrated v`. 

### `integrated_realHeisenbergOp`

 Acting on the Fock vector by the real Heisenberg operator at `y` is acting on `integrated v f`
by `ϱ (realVec y)`. 

### `rho_integrated_realCoord`

 For `v` in the Fock space and `f` in 𝒮(V), `integrated v f` is the vector v ⊗ f = ∫ v(x) ϱ(x)f
dx, with x running over real vectors in Fock coordinates. The Heisenberg operator ϱ(y) of an adelic
vector `y` acts on it factor by factor:
ϱ(y)(v ⊗ f) = (`realHeisenbergOp (realCoord y)` v) ⊗ ϱ(0, y.snd) f. So the real coordinates
`realCoord y` act on `v` by the Fock Heisenberg operator, and the finite part of `y` acts on `f`. 

### `exists_rho_integrated_eq`

 A Heisenberg operator ϱ(y) acts on v ⊗ f through another real datum w and the finite operator
ϱ_f(α⁻¹y_f); the datum w does not depend on f. 

### `_root_.New.mulVec_finVec`

 A matrix over `𝔸 E` acts on the vector `finVec y` of finite adeles through its finite
components. 

### `adeleMatrix_map_snd`

 The finite components of the matrix of `g : G E s` form the matrix of its finite part. 

### `omega_finHeisenbergOp`

 The Weil representation intertwines the finite Heisenberg operators:
`ω g ∘ finHeisenbergOp x = finHeisenbergOp (g_f x) ∘ ω g`, where `g_f = g.snd` is the finite
component. 

### `_root_.New.Gf.mulVec_mem_integralBox`

 If the finite unitary `g` lies in `GL_n(O_w)` at every place `w` of `S`, then `g x` lies in
`integralBox n S`, the vectors that are integral at the places of `S`, exactly when `x` does. 

### `map_projOn_eq_integral`

 A bounded linear map `L` passes through the mean over the standard lattice that defines
`projOn S`. 

### `projOn_eq_integral`

 `projOn S f` is the mean of `finHeisenbergOp (idem S.conjClosure • y) f` over `y` in the
standard lattice. 

 ### The projection above a set of finite places 

### `map_projOn`

 If `L (finHeisenbergOp (idem S.conjClosure • y) f) = F y` for `y` in the standard lattice, then
`L (projOn S f)` is the mean of `F` over the lattice. 

### `projOn_rho`

 If `y` vanishes above `S ∪ S̄` in every coordinate, then `ϱ y` commutes with `projOn S`. 

 ### Real data and the vacuum 

### `integrated_integrated`

 Integrating against two real data in turn gives v ⊗ (w ⊗ f) = w(0)·(v ⊗ f). 

### `omega_integrated`

 For g = (g_∞, g_f), ω(g)(v ⊗ f) = `New.Fock.realWeil`(g_∞)v ⊗ ω(g_f)f, where ⊗ is
`New.Space.integrated`, `New.Fock.realWeil` is the Weil representation on Fock space, and g_∞ is
read as a unitary matrix on the real coordinates. 

### `dataInner_vacElem_smul_vacElem`

 The projection ⟨vac, f⟩ vac on the vacuum is the projection above all finite places followed
by the real vacuum projection. 

### `integrated_finHeisenbergOp`

 `integrated v` commutes with the finite Heisenberg operators. 

### `finHeisenbergOp_comm`

 Two finite Heisenberg operators commute up to the character value
`selfDualAddChar E (star y ⬝ᵥ x)`. 

### `finHeisenbergOp_add`

 The operators ϱ_f(x), x ∈ Ô^n, form a representation of the lattice Ô^n. 

### `map_projOn_eq_const`

 If `L (finHeisenbergOp (idem S.conjClosure • y) f)` is a constant `c` for `y` in the standard
lattice, then `L (projOn S f) = c`, as the standard lattice has measure `1` for
`latticeMeasure E n`. 

### `finHeisenbergOp_projOn`

 For `y` in the standard lattice, `finHeisenbergOp (idem S.conjClosure • y)` fixes
`projOn S f`. 

### `dataInner_projOn`

 For a hermitian space `V : Space E n s` over the CM field `E` and a set `S` of finite places of
`E`, let `projOn S` be the operator on 𝒮(V) that averages the finite Heisenberg operator
`finHeisenbergOp` at the components above S ∪ S̄ of y, over y ∈ Ô^n. It is self-adjoint for the
sesquilinear form `dataInner` ⟨c, c′⟩ = ∫ c̄ c′ over 𝔸^n, that is ⟨P^S f, f′⟩ = ⟨f, P^S f′⟩. 

### `val_eq_dataInner_rho_vacElem`

 The value of f at an adelic vector y is the pairing of the translate ϱ(y) vac with f. 

### `dataInner_finHeisenbergOp_vacElem_vacElem`

 The coefficient ⟨ϱ_f(y) vac, vac⟩ of the vacuum is the indicator of the standard lattice Ô^n
at y. 

### `finHeisenbergOp_vacElem`

 The vacuum is fixed by `finHeisenbergOp y` for every `y` in the standard lattice `Ô^n`. 

### `dataInner_omega_left`

 The adjoint of `ω g` for `dataInner` is `ω g⁻¹`. 

 ### Values of the projection, and the Weil operators on its image 

### `boxIndicator_eq_integral_selfDualAddChar`

 The indicator of the vectors y that are integral at every place of T is the integral of the
character x ↦ ψ₀(y_T* x) over the standard lattice, where y_T = `idem T • y` is the part of y
above T. 

### `projOn_finHeisenbergOp`

 Let P^S = `New.Space.projOn` S be the projection on vacua above the finite places S ∪ S̄, and
let ϱ_f(y) = `New.Space.finHeisenbergOp` y. If P^S f = f, then P^S ϱ_f(y)f is ϱ_f(y)f when y is
integral at every place of S ∪ S̄ (`New.boxIndicator` is its indicator), and 0 otherwise. 

### `exists_rho_vacElem_eq_integrated`

 The translate ϱ(y) vac of the vacuum by an adelic vector y is w ⊗ ϱ_f(y') vac for a vector w of
the real Fock space, where y' = `finCoord y` is the finite coordinate of y. 

### `projOn_finHeisenbergOp_vacElem`

 P^S is the operator on 𝒮(V) given by the mean over y in Ô^n of the finite Heisenberg operators
ϱ_f at the part of y above S ∪ S̄. It fixes the translate ϱ_f(y) vac of the vacuum if the finite
vector y is integral at every place of S ∪ S̄ (that is, y lies in `integralBox n S.conjClosure`),
and annihilates it otherwise. 

### `dataInner_finHeisenbergOp_vacElem_eq_zero_of_sub_notMem`

 The translates ϱ_f(y) vac and ϱ_f(y') vac of the vacuum are orthogonal when y − y' is not in
the standard lattice Ô^n. 

### `dataInner_finHeisenbergOp_rep_vacElem`

 Let r choose a representative of each class of finite adelic vectors modulo the standard
lattice Ô^n. Then the translates ϱ_f(r q) vac of the vacuum are orthonormal. 

### `projOn_val`

 P^S = `projOn S` multiplies the value of f at an adelic vector y by the indicator of the
condition that the finite coordinate `finCoord y` of y is integral above S ∪ S̄. 

### `projOn_union`

 The projection for S ∪ S′ is the projection for S after the projection for S′. 

### `projOn_projOn`

 P^S is the operator on 𝒮(V) given by the mean over y in Ô^n of the finite Heisenberg operators
ϱ_f at the part of y above S ∪ S̄. P^S is a projection: P^S(P^S f) = P^S f. 

### `omega_projOn`

 For a set S of finite places, P^S = `projOn S` is the operator on 𝒮(V) that averages
ϱ_f(y) = `finHeisenbergOp y` over y in the lattice Ô^n, keeping only the components of y above S ∪
S̄. Let g be in `G E s`, and suppose that at every place w of S the component of its finite part
lies in GL_n(O_w) = `New.localIntGL`. Then the Weil operator ω(g) commutes with P^S. 

### `map_eq_zero_of_map_integrated_eq_zero`

 Let P^S = `projOn S` be the operator on 𝒮(V) that averages the finite Heisenberg operators
ϱ_f(y) = `finHeisenbergOp y` over y in Ô^n, keeping only the components of y above S ∪
S̄ = `S.conjClosure`. Let `L` be a bounded linear map from 𝒮(V) to a Banach space `Y`, and let `f`
be a vector with P^S f = f. If `L` kills every vector v_P ⊗ ϱ_f(y) e = `integrated (polyVector
(realSigns E s) P) (finHeisenbergOp y vacElem)`, then L f = 0; here `P` runs over all complex
polynomials, v_P is the polynomial vector of Fock space, ⊗ is the integrated action v ⊗ f = ∫ v(x)
ϱ(x) f dx, e = `vacElem` is the vacuum (Gaussian times twisted lattice indicator), and `y` runs over
the finite adelic vectors that vanish above S ∪ S̄. 

### `projOn_omega`

 Let S be a set of finite places and P^S = `New.Space.projOn` S, the averaging operator on 𝒮(V)
given by the mean over y ∈ Ô^n of the finite Heisenberg operator at the part of y above S ∪ S̄. If
g ∈ G_f is supported on S ∪ S̄ (its component is 1 at all other places) and P^S f = f, then P^S
ω(g)f = Δ_f(g⁻¹)⁻¹ f. Here Δ_f = `New.finMultiplier` is the `glMultiplier` of g viewed as an
invertible matrix. 

### `omega_eq_self_of_mem_stdLevel`

 Let `g` be an element of the finite adelic unitary group that lies in K_0 = G_f ∩ GL_n(Ô), the
stabiliser of the standard lattice, and has component 1 at every place outside S ∪ S̄. Let `f` in
𝒮(V) be fixed by P^S = `projOn S`, the mean over y in Ô^n of the finite Heisenberg operators ϱ_f at
the part of y above S ∪ S̄. Then ω(g)f = f. 

### `omega_vacElem`

 For g in G_f, ω(g)vac = Δ_f(g)·ω(g)P ω(g⁻¹)vac, where P is the projection on vacua at all finite
places and Δ_f = `New.finMultiplier`. 

### `finHeisenbergOp_mulVec_add_vacElem`

 For `x`, `y` in the standard lattice with `g y` also in the lattice, the vector
`finHeisenbergOp (g x) vacElem` does not change when `x` is replaced by `x + y`. 

### `finHeisenbergOp_mulVec_out_vacElem`

 Let `g` be in the finite adelic unitary group `Gf E n`, and `q` a coset of the standard lattice
Ô^n modulo its elements x with gx in Ô^n. Then the vector `finHeisenbergOp (g *ᵥ x) vacElem`, the
operator ϱ_f(gx) applied to the vacuum of 𝒮(V), is the same for every representative `x` of `q` as
for `q.out`. This vector is the term of `omega_vacElem_sum` at `q`. 

### `omega_vacElem_sum`

 Let `Λ` be the standard lattice Ô^n, let g be in the finite adelic unitary group G_f, and let
Δ_f(g) = `finMultiplier g` be its multiplier. Then the Weil operator applied to the vacuum
e = `vacElem` (Gaussian times twisted lattice indicator) gives ω(g) e = Δ_f(g)/‖Δ_f(g)‖² times the
sum of ϱ_f(g y) e over representatives `y` of the cosets of `Λ ∩ g⁻¹ Λ` in `Λ`, where
ϱ_f = `finHeisenbergOp` is the finite Heisenberg operator. There are finitely many cosets, as `Λ` is
compact and `g⁻¹ Λ` is open, and the terms do not depend on the representatives
(`finHeisenbergOp_mulVec_out_vacElem`). 


## The finite part of the Weil representation

* `New.Space.isLocallyConstant_rho_finVec`, `New.Space.eventually_omega_eq_self`: vectors of the
  finite part are smooth for the finite Heisenberg group and for the finite unitary group.

A point of the unitary group is a pair (infinite, finite), so `V.ω (1, g)` is the action of a finite
point `g`.


### `finitePart`

 The finite part 𝒮_f: the subspace of 𝒮(V) spanned by the translates of the vacuum under the
finite Heisenberg operators `New.Space.finHeisenbergOp`. 

### `finHeisenbergOp_mem_finitePart`

 The finite part is stable under the operators ϱ_f(x) of finite adelic vectors x. 

### `span_finHeisenbergOp_rep_vacElem`

 Let r choose a representative of each class of finite adelic vectors modulo the standard
lattice Ô^n. Then the translates ϱ_f(r q) vac of the vacuum span the finite part 𝒮_f. They are
orthonormal by `New.Space.dataInner_finHeisenbergOp_rep_vacElem`. 

### `rho_finVec_mem_finitePart`

 The finite part is stable under the Heisenberg operators ϱ(x) of finite adelic vectors x. 

### `projReal_eq_self_of_mem_finitePart`

 For a hermitian space `V : Space E n s` over a CM field `E` with Weil data, the real vacuum
projection `V.projReal` (the operator f ↦ ∫ exp(−|y|²/2) ϱ(y)f dy over real vectors y in Fock
coordinates) fixes every vector `f` of the finite part `V.finitePart`. The finite part is the
subspace of 𝒮(V) spanned by the translates of the vacuum under the finite Heisenberg operators. 

### `isLocallyConstant_rho_finVec`

 For f in the finite part, the map x ↦ ϱ(x)f on finite adelic vectors x is locally constant. 

### `projOn_mem_finitePart`

 The finite part is stable under the projection P^S = `projOn` S. 

### `omega_mem_finitePart`

 The finite part is stable under ω(1, g) for finite adelic points g of the unitary group. 

### `exists_eq_smul_omega_vacElem`

 Let g be in G_f and f in the finite part 𝒮_f. If all operators `New.Space.finHeisenbergOp` at
gy, y in Ô^n, fix f, then f is a complex multiple of ω(g)vac. 

### `eventually_omega_eq_self`

 Vectors of the finite part are smooth: for f in 𝒮_f, ω(1,k)f = f for all k in a
neighbourhood of 1 in the finite adelic unitary group. 
