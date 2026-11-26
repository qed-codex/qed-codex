---
{
  "module": "src/Lib/Adelic/AutomorphicForms/SmoothAlgebraicForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/SmoothAlgebraicForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/SmoothAlgebraicForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Algebraic forms on definite unitary groups, their pairing and Harish-Chandra parameters

This file studies forms on the definite unitary group of a hermitian space. A weight `(κ, e)`
records, at each infinite place `τ`, the number `κ τ h` of columns of height `h` of a Young diagram
and the power `e τ` of the determinant.

## Main definitions and results

* `New.AlgForm`: functions `φ` on the finite adelic points `New.Gf` with `φ(γ g) = ρ(γ) φ(g)` for
  rational `γ`, where `ρ = New.Space.weightRep`, whose stabiliser under right translation is open;
  `New.algFormRep` is right translation.
* `New.algFormCoeff`, `New.ofAlgForm`: from a form `φ` to the function `(x, g) ↦ L (ρ(x⁻¹) φ(g))`,
  `ρ = New.conjWeylRep`, for any linear form `L` and for the pairing with `New.highestVector`.
* `New.smoothPairing`, `New.smoothPairing_formTranslation`: a pairing B of coefficient vectors
  invariant under `New.Space.weightRep` gives a pairing of forms, by integration over Γ\G_f,
  invariant under G_f.
* `New.IsHCParam.eq_hcParameter`, `New.IsHCParam.exists_decreasingPosition_eq`: the entries of a
  parameter `l` are those of `New.hcParameter`, in the decreasing order of `l`;
  `New.IsHCParam.lowestKType_eq`: the highest weight that `l` determines.
* `New.highestVector_cyclic`: for injective `l w` and signs all 1, the highest vector
  `New.highestVector` of `New.conjWeylRep` is cyclic (`New.span_translate_highestVector_eq_top`),
  and so is its dual (`New.span_gramForm_highestVector_comp_eq_top`).
* `New.IsHCParam.prod_formalDegree`: the product of the formal degrees `New.HCParam.formalDegree` is
  the dimension.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.Space.embFin`: For a space (J, x), the homomorphism U(J)(E) → G_f sending γ to the finite
  part of x^{-1} γ x.
* `New.conjWeylRep`: The complex linear representation of weight (κ, e) of the product over places
  of the unitary groups of signs s, acting by the matrices `New.conjWeylMatrix`.
* `New.IsHCParam`: `l` lists twice the Harish-Chandra parameter of the weight `(κ, e)`, in some
  order: at each place `w` the numbers `l w i` are distinct, and each of them is
  `hcParameter κ e (card n) w p` for some position `p < card n`.
* `New.HCParam.dsCoeff`: The function c_λ(g) = Ξ(a, a⁻¹g) of a complex matrix g, with a the block
  diagonal part of g and Ξ the normalised integral `New.HCParam.flenstedJensen`.

## Relation to the literature

Known result: algebraic modular forms on definite unitary groups, their invariant pairing and
Harish-Chandra parameters. Source: B. Gross, Algebraic modular forms, Israel J. Math. 113 (1999).



## Smooth forms for a group with rational points

Smooth forms for a group `G` with rational points `e : Γ →* G` and a representation `ρ` of `Γ` on
`V`.


### `SmoothForm`

 Smooth forms: functions φ : G → V with φ(e(γ)g) = ρ(γ)φ(g) whose stabiliser under right
translation is open. 

### `smoothFormRep`

 The representation of G on smooth forms by right translation. 


## Algebraic forms and a p-adic gauge of their values

The spaces of algebraic modular forms on the definite unitary group of the sum of `n` norms
(`New.stdSpace`), and the measure of their `p`-adic integrality.

* `New.weylGauge`: the largest `p`-adic size of a coordinate of the translate of a value `ξ` by
  the inverse of a finite adelic point `g`.

Values are coordinate vectors indexed by `New.WeylIndex`, on which matrices over any commutative
ring act by `New.weylRep`.


### `Space.weightRep`

 The representation of the rational unitary group U(J)(E) on coordinate vectors of weight
(κ, e), through its components at the infinite places and `New.conjWeylRep`. A component acts
through its entrywise conjugate, which for signs all 1 is its inverse transpose. 

### `AlgForm`

 Smooth algebraic forms of weight (κ, e) on the standard space `New.stdSpace E n`: functions φ on
the finite adelic unitary group with φ(γg) = ρ(γ)φ(g) for rational γ whose stabiliser under right
translation is open. 

### `algFormRep`

 The representation of the finite adelic unitary group on the space of algebraic forms of
weight (κ,e), by right translation. 

### `weylGauge`

 The gauge of ξ at g: the largest p-adic absolute value of a coordinate of g⁻¹·ι(ξ), where
ι = `ιₚ` maps ℂ to the p-adic field and g⁻¹ acts in weight (κ, e), at τ through the p-adic
component given by the embedding `weightEmbedding ιₚ τ`, x ↦ ι(Φ_τ(x̄)). So g acts through its
conjugate, the inverse transpose of g, and the gauge is the multiplicative form of the least
valuation of a coordinate. 

### `integralAbove`

 The subgroup of finite adelic unitary points whose components at all primes above p are
integral invertible matrices. 


## From algebraic forms to functions on the adelic points

* `New.algFormCoeff`, `New.ofAlgForm`: the scalar function on all adelic points of a form.


### `algFormCoeff`

 For a linear functional L on vectors of weight (κ, e), the linear map sending an algebraic form
φ to the function g ↦ L(ρ(g_∞⁻¹) φ(g_f)) on G, with ρ = `New.conjWeylRep`. 

### `ofAlgForm`

 The linear map φ ↦ F_φ from algebraic forms of weight (κ, e) to functions on G, F_φ(g) = ⟨v⁺,
ρ(g_∞⁻¹) φ(g_f)⟩, with v⁺ = `New.highestVector` for l, a vector built from the decreasing order of
the entries of l (a unit vector for ⟨·,·⟩ = `New.gramForm` when each l w is injective). 

### `Space.IsStd.std_induction`

 Induction principle for standard spaces (all signs `1`, point the identity matrix). To prove a
statement about every standard space with its proof of standardness, it suffices to prove it for
`New.stdSpace` with signs `1`. 


## The invariant pairing of smooth algebraic forms

Here V is a definite hermitian space (`New.Space` with all signs 1), and Γ is the image of the
rational unitary group in G_f under `New.Space.embFin`. A weight κ of type `New.Weight` is a pair:
κ.1 counts the columns of each height and κ.2 gives the powers of the determinant.

* `New.Space.forms`: the functions on G_f fixed by an open subgroup under right translation that
  transform on the left by the weight κ representation `New.Space.weightRep`.
* `New.Space.formTranslation`: the action of G_f on forms by right translation.

`New.classIntegral` is the integral over Γ\G_f normalised by vol K₀ = 1, with K₀ = `New.stdLevel`.


### `Space.forms`

 Algebraic modular forms of weight κ on a definite space V: functions f on G_f with open
right stabiliser and f(γg) = ρ_κ(γ)f(g) for rational γ, ρ_κ = `New.Space.weightRep`. 

### `Space.formTranslation`

 The representation of the finite adelic unitary group on forms of weight κ on V by right
translation. 

### `pairing_mem_smoothInvariants`

 For forms φ and ψ of weight κ = (κ.1, κ.2) (column counts and determinant powers) on the
definite space V, and B invariant under `New.Space.weightRep`, the function g ↦ B(φ(g), ψ(g)) is
left invariant under the group `V.Γf` of rational points and fixed by an open subgroup under right
translation, so that `New.classIntegral` applies to it. 

### `smoothPairing`

 For a σ-sesquilinear B invariant under the weight κ action of U(J)(E), this is the pairing (φ,
φ') ↦ ∫ B(φ(g), φ'(g)) dg of forms on the definite space V, over Γ\G_f with vol K₀ = 1. 

### `smoothPairing_apply`

 The value of `New.smoothPairing` at two forms is the integral of their pointwise pairing. 

### `smoothPairing_formTranslation`

 The pairing `New.smoothPairing` of forms of weight κ on the definite space V, by a form `B`
invariant under `New.Space.weightRep`, is unchanged when both forms are translated on the right by
the same finite adelic point `a`. 


## Harish-Chandra parameters, formal degrees and dimension

Facts on `New.IsHCParam κ e l`: the vector `l` lists, at each place and in some order, twice the
Harish-Chandra parameter `λ + ρ` of the weight `(κ, e)` of the compact group `U(n)`.
`New.hcParameter` is that vector as a decreasing sequence, and `New.decreasingPosition` is the
position of an index in it.


 ### Existence of parameters, and cyclicity of the highest vector 

### `isHCParam_hcParameter`

 Index the entries of the decreasing sequence `hcParameter κ e (card n) w` by `n` through the
enumeration `Fintype.equivFin n`. The resulting vector satisfies `IsHCParam κ e`. 

### `hcParameter_eq_of_steps`

 Let L be a sequence of integers with L(p) − L(p+1) = 2κ_w(p+1) + 2 whenever p + 1 < N. If L
agrees with `New.hcParameter κ e N w` at one index q < N, then it agrees with it at every p < N.
That sequence is the decreasing parameter for rank N, and it has these same steps. 

### `apply_eq_zero_of_mul_gramForm_highestVector`

 Let each `l w` be injective, v⁺ = `New.highestVector`, ρ = `New.conjWeylRep` and
⟨·,·⟩ = `New.gramForm`. If f(ρ(x) v⁺) ⟨v⁺, ρ(x⁻¹) u⟩ = 0 for all x in the compact group (`USign 1`
at each place), then f(u) = 0. 

### `eq_zero_of_forall_gramForm_translate_eq_zero`

 Let each `l w` be injective, so that it orders the indices and gives the vector
`v⁺ = New.highestVector κ l`. A vector `u` is zero if all its translates ρ(x)u are orthogonal to
v⁺ for the form `New.gramForm`. Here x runs over the compact group (`USign 1` at each place) and
ρ = `New.conjWeylRep` is its representation of weight (κ, e). 

### `eq_zero_of_forall_map_translate_highestVector_eq_zero`

 Let each `l w` be injective, and let v⁺ = `New.highestVector κ l`. A linear form that kills all
translates ρ(x)v⁺ under the compact group (`USign 1` at each place, acting in weight (κ, e) by
ρ = `New.conjWeylRep`) is zero. 

### `span_translate_highestVector_eq_top`

 Let each `l w` be injective, and let v⁺ = `New.highestVector κ l`. The translates ρ(x)v⁺ under
the compact group (`USign 1` at each place, acting in weight (κ, e) by ρ = `New.conjWeylRep`) span
the space of coordinate vectors. 

### `span_gramForm_highestVector_comp_eq_top`

 Let each `l w` be injective, and let v⁺ = `New.highestVector κ l`. The linear forms
u ↦ ⟨v⁺, ρ(x)u⟩ span the dual space. Here ⟨·,·⟩ = `New.gramForm`, and x runs over the compact
group (`USign 1` at each place), acting in weight (κ, e) by ρ = `New.conjWeylRep`. 

### `highestVector_cyclic`

 Let each `l w` be injective. For any determinant twist `e`, the highest vector
v⁺ = `New.highestVector κ l` and its dual ⟨v⁺, ·⟩ for `New.gramForm` are cyclic under the compact
group (`USign 1` at each place, acting by ρ = `New.conjWeylRep`): the vectors ρ(x)v⁺ span the
representation, and the linear forms u ↦ ⟨v⁺, ρ(x)u⟩ span its dual. Both facts are consequences of
the irreducibility of the Schur module. 

 ### Positions in the decreasing order 

### `exists_decreasingPosition_eq_of_injective`

 For an injective integer vector `a` indexed by `n`, every position `q < card n` in the
decreasing order of `a` is taken by some index. Here `decreasingPosition a i` counts the indices k
with a i < a k, so positions start at 0. 

### `decreasingPosition_lt_card_of_lt`

 If `x < a i`, then the number of entries of `a` that exceed `x` is larger than the position of
`i` in the decreasing order of `a`. 

 ### Consequences of `New.IsHCParam` 

### `IsHCParam.eq_hcParameter`

 Here `hcParameter κ e N w p` = 2μ_p + N − 1 − 2p is entry p of twice μ + ρ in rank N, for the
highest weight μ_p = e_w + Σ_{p<h<N} κ_w(h) at the place `w`. If `l` lists twice the Harish-Chandra
parameter of `(κ, e)` in some order, then `l w i` is the entry of `hcParameter` at the position of
`i` in the decreasing order of `l w`, that is, the number of `j` with `l w i < l w j`. 

### `IsHCParam.exists_decreasingPosition_eq`

 For a parameter `l` of `(κ, e)`, every position q < |n| is taken: some index i is at position q
in the decreasing order of `l w`, its entry is entry q of the parameter, and for each x below that
entry more than q entries of `l w` exceed x. 

### `IsHCParam.image_eq`

 The entries of `l w` are the first `card n` entries of the decreasing parameter. 

### `IsHCParam.hasGap`

 For a parameter `l` of `(κ, e)` and every natural number `c`, the vector `l w` satisfies
`New.HCParam.HasGap c`: its entries are distinct and of the parity of `card n - 1`, and the gap
condition is empty as all signs are `1`. 

### `IsHCParam.lowestKType_eq`

 Let `κ` give column multiplicities at each place w (κ_w(h) columns of height h) and let `e` give
an integer e_w at each w, and suppose l is twice the Harish-Chandra parameter of the weight (κ, e).
Then for signs all 1, the entry at i of `New.HCParam.lowestKType` of l_w equals e_w + Σ_{p<h<|n|}
κ_w(h), where p is the number of j with l_w(j) > l_w(i). Here `New.HCParam.lowestKType` is the
highest weight of the lowest K-type, with K = U(n). The sum is `New.diagramWeight` at (w, p), with
`rankAt` giving the rank |n| at every place. 

### `IsHCParam.gramForm_conjWeylRep_eq_dsCoeff`

 Let `κ` give column multiplicities at each place w (κ_w(h) columns of height h) and let `e` give
an integer e_w at each w; together (κ, e) is the weight whose entry at position p of place w is
e_w + Σ_{p<h<|n|} κ_w(h). Suppose l is twice the Harish-Chandra parameter of (κ, e)
(`New.IsHCParam`), and take x in the product over w of U(n) = U(diag 1). Then the matrix coefficient
⟨v⁺, ρ(x)v⁺⟩ at the highest vector v⁺ = `New.highestVector` is ∏_w conj ψ_{l_w}(x_w), where
ρ = `New.conjWeylRep` is the representation on coordinate vectors of weight (κ, e),
ψ = `New.HCParam.dsCoeff` and ⟨·,·⟩ = `New.gramForm`. 

### `IsHCParam.prod_formalDegree`

 If l is twice the Harish-Chandra parameter of (κ, e), the product over w of the formal degrees
`New.HCParam.formalDegree` of l_w for the compact group U(n) equals the dimension of the
representation of weight (κ, e), the number of elements of its basis `New.WeylIndex`. The formal
degree is the reciprocal of the mean of the squared modulus of `New.HCParam.dsCoeff`.

This is a case of the Schur orthogonality relations, for one matrix coefficient of the
representation of weight (κ, e) of a product of compact groups U(n). 
