---
{
  "module": "src/New/OneLift/TestedForms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Point forms, Hecke adjoints and false lifts on the definite space of a descent pair

This file studies algebraic forms on the definite space `V = I_n` of a descent pair `O`
(`New.DescentPair`). The pair gives a space `W` of rank `r`, an embedding `O.incl` of `r` into `n`,
and places indexed by `O.ChosenIndex` (the set M of chosen places) and `O.TwistIndex` (the set Q of
the twist). For each `σ ∈ Aut ℂ`, `New.LevelPlaces.LevelForm.innerAt σ` is `σ⁻¹` of the inner
product of the `σ`-conjugates of two forms. Point forms, supported on one class, have explicit inner
products and descents, and the Hecke polynomial `H_w(X)` at a split place has an explicit adjoint
for these pairings. Let `Z` (in use, the space of lifts) lie in the image of a central idempotent
`e₀` and be killed by `H_w(X_*)`, where `X_* = O.liftHeckeRoot w`. On forms orthogonal to the false
lifts, the orthogonal projection (for `σ = 1`) to `Z` does not increase the norm at any `σ`.

## Main definitions and results

* `New.Rows.IsPointLift`, `New.Rows.exists_isPointLift`, `New.Rows.pointLift`: an element `A` of the
  integral level with prescribed columns at `O.ChosenIndex` and rows at `O.TwistIndex`.
* `New.Rows.pointForm`: the point form at `h A`; `New.Rows.inner_pointForm` and
  `New.Rows.normalizedDescent_pointForm` compute its inner products and its descent
  `New.DescentPair.normalizedDescent`, whose finite datum is `New.Rows.pointFormDatum`.
* `New.LevelPlaces.LevelForm.innerAt_heckePolyOnForms` computes the adjoint of `H_w(X)` for the
  pairing `innerAt σ`.
* `New.DescentPair.falseLiftsAt`, `New.DescentPair.IsOrthogonalToFalseLifts`,
  `New.DescentPair.IsTestForm`: false lifts, the forms orthogonal to them, and the integral ones
  among these for a fixed `e₀` and `Z = ker O.normalizedDescent`.
* `New.Selmer.DenominatorLe`: a bound on the ℓ-adic denominator of the projection to a subspace Z.
* `New.DescentPair.normSqAt_starProjection_le`: on forms orthogonal to the false lifts the
  projection to Z does not increase the norm at σ.

Notions from other files:
* `New.DescentPair`: A descent pair: places M and Q, a space W of rank r with numbered basis
  vectors, an embedding of the index set r into the larger index set n, weights k⁺ and k⁻, and a
  character μ whose tame part is trivial off these places.
* `New.DescentPair.FormV`: the algebraic forms on V = I_n with the weight, level and character of
  the pair; the level sits at two finite sets of split places, M and Q.
* `New.DescentPair.heckePolyOnForms`: the operator H_w(X) = ∑_i (−X)^i q^{i(i−1)/2} T_{w,i} on
  forms, for a split place w that, with its conjugate, is off M and Q;
  `New.DescentPair.liftHeckeRoot` w is the value X_* at which it is taken.
* `New.DescentPair.normalizedDescent`: the descent, a linear map from forms Ξ on V to functions on
  U(W)(𝔸): its value at g is the class sum over h, for `New.DescentPair.levelGroup`, of
  `New.DescentPair.conjKernel` at g and h applied to Ξ(h). It is adjoint to the lift from W
  (`New.DescentPair.inner_thetaLift`).
* `New.LevelPlaces.placeAt`: the chosen places and the places of Q as one family, indexed by
  `O.ChosenIndex ⊕ O.TwistIndex`.

## Relation to the literature

See `New.OneLift.ComparisonOperator.GluingMaps` and `New.OneLift.LiftVolumeHeight` for related
work.



## Point forms with prescribed finite datum: inner products and descent

Moving the point by an element `A` of the integral level changes the block datum `Ψ(T)` of the
descent to `Ψ(A⁻¹ T)`.


### `IsPointLift`

 The element `k` of the integral level `New.stdLevel` has component 1 at every finite place
other than those of M and Q (the set `O.places`) and their conjugates, its reductions at the chosen
places `O.placeAt (Sum.inl i)` have the columns `Y i` at the indices `O.incl`, and its reductions at
the places `O.placeAt (Sum.inr i)` of the twist have unit vectors in the rows `e`. Columns are
selected by `inclMatrix R u`, the matrix whose columns are the unit vectors at the indices `u`. 

### `IsPointLift.mem_supportedOn`

 `k` is supported on the places of `O` and their conjugates. 

### `IsPointLift.columns_eq`

 At a place of `O.ChosenIndex` the columns `O.incl` of the reduction of `k` form `Y i`. 

### `IsPointLift.rows_eq`

 At a place of `O.TwistIndex` the row `e j` of the reduction of `k` is the unit vector
  `O.incl j`. 

### `exists_isPointLift`

 Given matrices `Y i` of full column rank over the residue fields at the places of
`O.ChosenIndex` and `r` distinct rows `e`, there is an element `k` of the integral level
`New.stdLevel` with `IsPointLift Y e k`: it is supported on the places of `O`, has the columns `Y i`
at `O.ChosenIndex`, and has unit vectors in the rows `e` at `O.TwistIndex`. 

### `classForm`

 The map sending `v` to the form `δ_h (v)` on `V = I_n` (`New.deltaForm`), supported on the class
of the point `h` of the finite unitary group `Gf E n`: its value at `y` is the sum of
`O.levelChar (h⁻¹ γ y) • ρ γ⁻¹ v` over the rational `γ` (embedded by `embFin`) with `h⁻¹ γ y` in the
level group of `O`. Here `ρ` is the representation whose highest weight is given by `O.columnCount`
and the determinant exponents `O.detExp`, and `WeylIndex n O.columnCount` indexes the coordinates of
its vectors. 

### `inner_eq_stdClassSum_gramForm`

 The inner product of two forms on `V` is the class sum of the pairings of their values under
`gramForm`, the hermitian form `(ξ, η) ↦ ξ* G η` of the integral Gram matrix `G` of the weight. The
class sum `stdClassSum` of a function `f` for the level group of `O` is the sum of
`f (g_c) / #Aut (g_c)` over the double cosets `c` of the rational points and that group. 

### `inner_classForm`

 Let `h` be a point of the finite unitary group `Gf E n` of `V`. The inner product of the form
`δ_h (v) = classForm O h v`, supported on the class of `h`, with a form `φ` is the Gram pairing
`gramForm` of `v` with the value of `φ` at `h`. 

### `normalizedDescent_classForm`

 Let `h` be a point of the finite unitary group `Gf E n` of `V` and `g` a point of the adelic
unitary group `G E O.signs` of the space `O.W` of rank `r`. The descent `O.normalizedDescent` is the
linear map, adjoint to the theta lift from `O.W`, that takes forms on `V` to functions on that
group. Its value at `g` on the form `δ_h (v) = classForm O h v`, supported on the class of `h`, is
the complex conjugate of the theta kernel `modKernel` of the pair `(O.W, V)` at `(g, h)`, twisted
by the characters `O.charW`, `O.charV`. Its polynomial is `O.fockPoly (star v)`, the polynomial in
the Fock variables attached linearly to the conjugate weight vector. Its datum is a function of a
matrix `T` modulo `O.levelModulus 2`: it applies `O.residueBlockDatum` to the reductions
`levelResidueAt i` of `T` at the places `i` of M = `O.ChosenIndex` and Q = `O.TwistIndex`. That
datum is 0 unless each reduction at M is the inclusion matrix of `O.incl`, and is then the product
over the places w of Q of `O.tamePart w`, a character of the residue field, at the determinant of
the rows `O.incl`. 

### `pointLift`

 For matrices `Y i` of full column rank and `r` distinct rows `e`, a chosen element of the
integral level `New.stdLevel` as in `exists_isPointLift`. Its properties are stated in
`isPointLift_pointLift`. 

### `pointForm`

 The point form: the map sending `v` to the form `δ_{h A} (v)`, supported on the class of `h A`,
where `A = pointLift hY e`. The finite datum of its descent is `1[T = Y i]` at `O.ChosenIndex` and
`ψ (det T_e)` at `O.TwistIndex`, with `T_e` the rows `e` of `T` (`pointFormDatum`,
`normalizedDescent_pointForm`). 

### `inner_pointForm`

 The inner product of the point form made from `v` with a form `φ` is the Gram pairing `gramForm`
of `v` with the value of `φ` at the point `h A`, where `A = pointLift hY e`. 

### `pointFormDatum`

 The finite datum of the descent of a point form, as a function of families `X` of matrices over
the residue fields at the places of `O`. If `X` equals `Y` at every place of `O.ChosenIndex`, it is
the product over the places `w` of `O.TwistIndex` of `O.tamePart w` of the determinant of the rows
`e` of `X` at `w`; otherwise it is `0`. Here `O.tamePart w` is the character of the residue field at
`w` given by `O`. 

### `residueBlockDatum_inv_pointLift_mul`

 Let `Y i` be matrices of full column rank at the places of M = `O.ChosenIndex` and `e` an
injection choosing `r` rows. Let `A = pointLift hY e` be the chosen integral element whose
reductions have the columns `Y i` at `O.incl` over M, and unit vectors in the rows `e` over
Q = `O.TwistIndex`. Let `X` be a family of matrices over the residue fields at M and Q.
`O.residueBlockDatum` is 0 unless the matrices at M are the inclusion matrix of `O.incl`, and is
then the product over w in Q of `O.tamePart w`, a character of the residue field, at the determinant
of the rows `O.incl`. At the family `A⁻¹ X` it equals `pointFormDatum Y e X`, the same expression
with `Y i` for the inclusion matrix and the rows `e` for `O.incl`. 

### `normalizedDescent_pointForm`

 Let `Y i` be matrices of full column rank at the places of M = `O.ChosenIndex`, `e` a choice of
`r` rows, and `h` a point of the finite unitary group of `V`. The point form `pointForm h hY e v`
is the form with vector `v` supported on the class of `h A`, where `A = pointLift hY e` is an
integral element with columns `Y i` over M and unit vectors in the rows `e` over
Q = `O.TwistIndex`. Its descent `O.normalizedDescent` (adjoint to the theta lift from `O.W`), at a
point `g` of the adelic unitary group `G E O.signs` of `O.W`, is the complex conjugate of the theta
kernel `modKernel` of the pair `(O.W, V)` at `(g, h)`, twisted by the characters `O.charW`,
`O.charV`. Its polynomial is `O.fockPoly (star v)`, the polynomial in the Fock variables attached
linearly to the conjugate weight vector. Its datum applies `pointFormDatum Y e` to the reductions
`levelResidueAt i` of a matrix modulo `O.levelModulus 2`: this is 0 unless they are `Y i` at M,
and is then the product over w in Q of `O.tamePart w`, a character of the residue field, at the
determinant of the rows `e`. 

 ## The adjoint of the Hecke polynomial at a split place 

### `DescentPair.exists_invariant_pairing_eq_innerAt`

 The σ-conjugate pairing `New.LevelPlaces.LevelForm.innerAt σ` on forms on V is the restriction
of a pairing `B` of all smooth forms of the same weight, semilinear for σ⁻¹ ∘ conj ∘ σ in the first
variable, that is invariant under right translation `New.Space.formTranslation`. 

### `LevelPlaces.LevelForm.innerAt_heckePolyOnForms`

 Let w ≠ w̄ be a finite place such that w and w̄ are off the level, that is, outside the places
of M and Q and their conjugates. The operator H_w(X) = `O.heckePolyOnForms` on forms on V is the
polynomial ∑ (−X)^i q^{i(i−1)/2} T_{w,i} in the Hecke operators at w, q the norm of w. Its adjoint
for the σ-conjugate pairing `New.LevelPlaces.LevelForm.innerAt` is H_{w̄}(X'), with
X' = σ⁻¹(conj(σX)). 


## False lifts, denominators of lifts and the norm bound for projections

Orthogonal complements and projections refer to the inner product `innerAt 1`.


### `groupAlgAction`

 The operator by which e₀, in the group algebra of ∏_{w ∈ M} GL_r(k_w), acts on forms on V
through the representation `New.DescentPair.formAction`. 

### `falseLiftsAt`

 The false lifts for a split place `w` off the level: the forms in the image of `e₀` that are
killed by the Hecke polynomial operator `H_w`, at the value `O.liftHeckeRoot w`, and lie in `Z`. In
use `Z` is the orthogonal complement of a space of lifts, or the kernel of the descent
`O.normalizedDescent`. 

### `IsOrthogonalToFalseLifts`

 The form `y` on `V` is orthogonal to the false lifts `O.falseLiftsAt hw hS e₀ Z` for every split
place `w` off the level. 

### `IsTestForm`

 The form Ξ is integral above l (at every embedding ℂ → ℂ_l, all values of Ξ have gauge at
most 1: `integralForms`) and orthogonal to the false lifts
(`New.DescentPair.IsOrthogonalToFalseLifts`) for e₀ and Z. Here e₀ is `tupleIdem` at X − 1, that is,
the tensor product over w ∈ M of the idempotents `labelIdem` of GL_r(k_w) attached to the polynomial
X − 1; for W of rank one it is the mean over ∏_{w ∈ M} GL_1(k_w). The space Z is the kernel of the
descent `O.normalizedDescent`, the adjoint of the lift from W. 

### `_root_.New.PadicPlace.ofIso`

 The `ℓ`-adic place of `ℂ` given by an isomorphism `ι : ℂ ≃ ℚ̄_ℓ`, followed by `ℚ̄_ℓ ⊆ ℂ_ℓ`. 

### `_root_.New.PadicPlace.ιₚ_ofIso`

 The place `PadicPlace.ofIso ι` is `ι` followed by `ℚ̄_ℓ ⊆ ℂ_ℓ`. 

### `_root_.New.Selmer.DenominatorLe`

 The projection `pr` to `Z` has denominator at most `exp β` per dimension and row at `ι`: there
is an operator `Λ` on `Z` with `log |ι (det Λ)| ≥ -dim Z * #r * β` such that, for every form `y`
that is integral at `ι` and has `O.IsOrthogonalToFalseLifts e₀ Zᗮ y`, the form `Λ (pr y)` is
integral at `ι`, and its inner product with every form that is integral at every embedding `ℂ → ℂ_ℓ`
has absolute value at most 1 at `ι`. A form is integral (`integralForms`) at an embedding if all its
values have gauge at most 1 there. 

### `isOfFinOrder_prod_tamePart_det`

 For g in ∏_{w ∈ M} GL_r(k_w), the number ∏_w χ_w(det g_w) is a root of unity, where
χ_w = `O.tamePart w` is the tame part at w of the character μ of `O`, a character of the residue
field k_w. 

### `innerAt_formAction`

 Let M = `O.ChosenIndex` be the set of chosen places w of the pair, with residue fields k_w, and
ψ_w = `O.tamePart w` the tame part at w of the character μ of `O`, a character of k_w. In the
action `O.formAction` of ∏_{w ∈ M} GL_r(k_w) on forms on V, an element g acts as ∏_w ψ_w(det g_w)
times right translation by an integral element that reduces at each w in M to the matrix equal to
g_w on the indices `O.incl` and to 1 on the others, and to 1 at the places of Q. For every
automorphism σ of ℂ this action preserves the σ-conjugate pairing: ⟨gx, gy⟩_σ = ⟨x, y⟩_σ. 

### `range_groupAlgAction_mem_invtSubmodule`

 An operator f on forms on V that commutes with the action `New.DescentPair.formAction` of
∏_{w ∈ M} GL_r(k_w) preserves the image of every element e₀ of the group algebra. 

### `heckePolyOnForms_comm`

 The Hecke polynomial operators `New.DescentPair.heckePolyOnForms` at two split places w and u
off the level commute: H_w(X) H_u(Y) y = H_u(Y) H_w(X) y for all complex X, Y and all forms y on V.
The places may be equal or conjugate. 

### `innerAt_groupAlgAction`

 A central idempotent e₀ of the group algebra of ∏_{w ∈ M} GL_r(k_w) acts on forms on V
self-adjointly for the pairing `innerAt σ`, for every σ: ⟨e₀x, y⟩_σ = ⟨x, e₀y⟩_σ. 

### `exists_adjoint_heckePolyOnForms_comm`

 The Hecke polynomial operator H_w(X) at a split place w off the level is normal for the pairing
`innerAt σ`: it has an adjoint `A'` with which it commutes. 

### `innerAt_heckePolyOnForms_eq_zero`

 The image of the Hecke polynomial operator H_w(X) is orthogonal to its kernel for the pairing
`innerAt σ`. 

### `orthogonal_range_heckePolyOnForms_le_ker`

 A form orthogonal to the image of the Hecke polynomial operator H_w(X) lies in its kernel. 

### `normSqAt_eq_re_innerAt`

 The squared norm ‖v‖²_σ = `normSqAt v σ`, defined as the class sum of the squared Gram norms of
the vectors σ(v(g)), is the real part of σ(⟨v, v⟩_σ), where ⟨v, v⟩_σ = `innerAt σ v v`. 

### `normSqAt_le_add_of_innerAt_eq_zero`

 If ⟨x, z⟩_σ = 0, then ‖z‖²_σ ≤ ‖z + x‖²_σ for the squared norm `normSqAt`, the class sum of the
squared Gram norms of the σ-conjugated values of a form. 

### `mem_sup_ker_sup_range_of_isOrthogonalToFalseLifts`

 Let e₀ be a central idempotent of the group algebra of ∏_{v ∈ M} GL_r(k_v), M the chosen places
of the pair, acting on forms on V through `O.formAction`, and let Z be a space of forms. For a place
w ≠ w̄ off the level let H_w(X_*) be the Hecke polynomial operator at the explicit number
X_* = `O.liftHeckeRoot w`, built from the norm of w and a character of the Weil data. A false lift
for e₀ and Z^⊥ is a form in Z^⊥ and in the image of e₀ that such an operator kills. If y is
orthogonal to all false lifts, then for every such w it lies in the sum of Z, the kernel of e₀ and
the image of H_w(X_*). 

### `normSqAt_starProjection_le`

 Let e₀ be a central idempotent of the group algebra of ∏_{v ∈ M} GL_r(k_v), M the chosen places
of the pair: an idempotent whose coefficients form a class function. Let Z be a space of forms in
the image of e₀ killed by the Hecke polynomial operator H_w(X) = ∑ (−X)^i q^{i(i−1)/2} T_{w,i} at
the explicit number X = X_* = `O.liftHeckeRoot w`, for one place w ≠ w̄ off the level, q its norm.
Let y be orthogonal to the false lifts. Then the orthogonal projection of y to Z (for σ = 1) has
squared norm `normSqAt` at most that of y, at every σ. 
