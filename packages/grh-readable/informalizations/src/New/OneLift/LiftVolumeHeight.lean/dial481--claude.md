---
{
  "module": "src/New/OneLift/LiftVolumeHeight.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cost of one lift: a height bound for Z_j(1)/Z_j(ξ^j)

The comparison operators `U_ϑ = n_Aut hk² glue_ϑ glue_ϑ*` take lifts to forms orthogonal to the
false lifts. A tight frame of integral tuples writes them as sums of operators of rank one, so they
keep integrality away from `Q` and `U_1` is short (`IsComparisonOperator`). The product
`Z_j (ϑ) det (pr U_ϑ)` depends on the twist `ϑ` only through Hecke values. Eigenvalue bounds control
the denominator of `det (pr U_ϑ)` at `ι` and the conjugates of `det (pr U_1)`; this bounds the
height of `Z_j (1) / Z_j (ξ_ι ^ j)`, for m-fold twists `ξ_ι`.

Notions from other files:
* `D : Data P` fixes a CM field `E = D.E`, weights at its infinite places, a level, and the ranks:
  `m = D.m` lifts, from hermitian spaces `W_j = D.spaceW j` (`1 ≤ j ≤ m`) of rank `r = D.r` to the
  standard definite space `V_j` of rank `r + t`, where `t = D.t = 5 r`. The datum of the lift at a
  twist `ϑ` is `D.descentPair ϑ j`, and its `FormV` is the space of forms on `V_j`.
* `D.goodLift ϑ j` is the lift at the twist `ϑ` on the good forms on `W_j` (the range of the
  idempotent `D.e₀`), with values in the forms on `V_j`. `D.liftDeterminant ξ j`, written
  `Z_j (ξ ^ j)` for an m-fold twist `ξ`, is, at `ϑ = ξ ^ j`, the Gram determinant of this lift.
* `IsOrthogonalToFalseLifts O D.e₀ Z φ` says that the form `φ` is orthogonal to the false lifts: the
  forms that satisfy the conditions on a lift from `D.e₀` and lie in `Z`, here the complement of the
  lifts.
* `glue j ϑ` is the gluing map `glue_ϑ` from tuples of forms on `V°` (`FormTuples j`) to forms on
  `V_j`; `periodLift j` is `twistFactor j 1` times its adjoint after the lift, at the trivial twist.
  Here `V°` is the standard definite space with basis `D.SecondFactorIndex`.
* `heckeValueProd j ϑ` is a product of three real numbers `Exchange.lValueProd` (norms of places
  times squared moduli of partial Hecke `L`-values at integers), for the three characters of
  `exchangePair j` twisted by `ϑ` or its inverse.

## Relation to the literature

Bounding the norm of a lift by an integral form and a congruence denominator is known in the
literature for one eigenform.

Related work: Böcherer–Dummigan–Schulze-Pillot, Yoshida lifts and Selmer groups, 2012; X. Zhang,
Special L-values and Selmer groups of Siegel modular forms of genus 2, 2018; Hida, Congruences of
cusp forms and special values of their zeta functions, 1981.


### `normDet_sq_mul_det_compression`

 Let `u : U → V` be an injective linear map of finite-dimensional complex inner product spaces,
`pr` the orthogonal projection of `V` to the range of `u`, and `T` an operator on `V`. The
determinant of `pr T` on the range of `u`, times `u.normDet ^ 2 = det (u* u)`, is `det (u* T u)`. 

### `norm_map_det_le_pow`

 A determinant is the product of the eigenvalues. So if `‖f α‖ ≤ B` for every eigenvalue `α` of
`u` (`h_eigen`), then `‖f u.det‖ ≤ B ^ finrank ℂ L`, for the ring map `f : ℂ →+* K` into a normed
field. 

### `_root_.New.LevelPlaces.LevelForm.normSqAt_smul`

 Multiplying a form on the space `V` of a descent pair `O` by `c` multiplies its squared norm
`normSqAt` at an automorphism `σ` of `ℂ` by `‖σ c‖ ^ 2`. 

### `_root_.New.LevelPlaces.LevelForm.normSqAt_nonneg`

 The squared norm `φ.normSqAt σ` of a form (the weighted sum over classes of the squared norms
of the values after applying `σ`) is not negative. 

### `_root_.New.LevelPlaces.LevelForm.normSqAt_pos`

 Let `E` be a CM field with a CM type and Weil data, and `O` a descent pair over `E`: the datum
of a lift from a hermitian space `W` with basis indexed by `r` to the standard space `V` with basis
indexed by `n`. For `φ ≠ 0` in `O.FormV`, the algebraic forms on `V` of the weight and level of `O`,
the squared norm `φ.normSqAt σ` is positive at every automorphism `σ` of `ℂ`. 

### `_root_.New.DescentPair.exists_smul_mem_integralForms_maximal`

 A nonzero form `φ` in the space `O.FormV` of forms on `V` of a descent pair `O` over the CM
field `E` can be scaled to valuation `0` at a place `ι` (an embedding `ι.ιₚ` of `ℂ` into `ℂ_[l]`):
there is `c ≠ 0` such that `c • φ` is integral at `ι`, and `α • c • φ` is integral only if
`‖ι.ιₚ α‖ ≤ 1`. 

### `IsComparisonOperator`

 A comparison operator for the lift from `W_j`: a family of operators `U_ϑ` on the forms on `V_j`
through which the lifts `Θ_ϑ = D.goodLift ϑ j` at the twists `ϑ` are compared with the untwisted
one. In the bound, `f = D.f` is the number of infinite places, `m = D.m` the number of lifts in the
chain and `b = D.b`, with `log b = D.logB`, the weight at the infinite places in `D.bPlaces`. 

### `IsComparisonOperator.ratio_ne_zero`

 The ratio of the twisted to the untwisted Hecke values of the lift is not `0`. 

### `IsComparisonOperator.exists_inner_eq`

 `⟨Θ_ϑ y', U_ϑ Θ_ϑ y⟩` is this ratio times `⟨y', U° y⟩`, for a positive definite operator `U°`
  on the good forms that does not depend on `ϑ`. The shape of the ratio is given by
  `exists_heckeValueProd_eq_mul_prod_ratio`. 

### `IsComparisonOperator.isOrthogonalToFalseLifts`

 `U_ϑ` takes lifts to forms that are orthogonal to the false lifts
  (`IsOrthogonalToFalseLifts`). 

### `IsComparisonOperator.mem_integralForms`

 `U_ϑ` keeps integrality above every prime that does not divide `ϑ.normQ`, the product
  of the norms of the places in the set `Q` of `ϑ`. 

### `IsComparisonOperator.normSqAt_le`

 `U_1` multiplies norms at every `σ` by at most `exp (3 f m b log² b)`. 

### `comparisonOp`

 The operator `U_ϑ = n_Aut hk² glue_ϑ glue_ϑ*` on the forms on `V_j`. Here `glue_ϑ = glue j ϑ`
is the linear map that builds a form on `V_j` from a tuple of forms on `V°`,
`hk = hookNumberMinus j` is the hook number of the diagram `μ⁻` (the weight of the forms on `V°`),
and `n_Aut = D.chosenGroupOrder` is a multiple of the orders of all stabilisers. 

### `heckeValueProd_div_eq`

 The ratio of the twisted to the untwisted product of Hecke values (`heckeValueProd`) is
`|c′_1|² / |c′_ϑ|²`, where `c′_ϑ = twistFactor j ϑ` is the nonzero scalar that normalises the
series of the gluing at the twist `ϑ`. 

### `adjoint_glue_goodLift`

 The adjoint of the gluing map `glue j ϑ` takes the lift of `y` at the twist `ϑ` to
`c′_ϑ⁻¹ Θ° y`, where `c′_ϑ = twistFactor j ϑ` and `Θ° = periodLift j`. 

### `inner_goodLift_comparisonOp`

 Let `D` be the data of the chain of lifts, `1 ≤ j ≤ D.m`, `ϑ` a twist, and `y'`, `y` good forms
on the hermitian space `W_j = D.spaceW j`. Let `Θ_ϑ = D.goodLift ϑ j` be the theta lift to forms on
the definite space `V_j`, and `glue_ϑ = glue j ϑ` the linear map that builds a form on `V_j` from a
tuple of forms on the smaller definite space `V°`, with adjoint `glue_ϑ*`. For
`U_ϑ = comparisonOp j ϑ = n_Aut hk² glue_ϑ glue_ϑ*` we have `⟨Θ_ϑ y', U_ϑ Θ_ϑ y⟩ = n_Aut hk²
|c′_ϑ|⁻² ⟨Θ° y', Θ° y⟩`. Here `n_Aut = D.chosenGroupOrder` is a multiple of the orders of all
stabilisers, `hk = hookNumberMinus j` is the hook number of the weight of the forms on `V°`, and
`c′_ϑ = twistFactor j ϑ` is the nonzero scalar for which `c′_ϑ glue_ϑ* Θ_ϑ` does not depend on `ϑ`;
this common map is `Θ° = periodLift j`. 

### `isOrthogonalToFalseLifts_comparisonOp`

 Let `D` be the data of the chain of lifts, `1 ≤ j ≤ D.m` and `ϑ` a twist. Let `z` be a lift: a
form on `V_j` in the range of the theta lift `D.goodLift ϑ j` of the good forms on `W_j`;
`D.descentPair ϑ j` is the datum of this lift. Then the image of `z` under `comparisonOp j ϑ`, a
positive multiple of the gluing map `glue j ϑ` after its adjoint, is orthogonal to the false
lifts. 

### `TightFrameIndex`

 The index set of the frame of tuples of forms on `V°`: an index `ChoiceIndex j` of a component
of the tuple (a matrix modulo `D.piM ^ 2` with a row choice), a class of `U(V°)` at principal level
`D.piM ^ 2`, and a basis tensor of the shape `μ⁻ = (untwistedDescentPair j).colsMinus`, the column
counts of the negative sign for the descent pair at the trivial twist. 

### `exists_frame_weightRep_eq_intCast`

 Let `V° = stdSpace D.E D.SecondFactorIndex` be the standard definite hermitian space over the CM
field `D.E` of the data `D`, with basis `D.SecondFactorIndex`. Let `γ` be an element of its rational
unitary group `U (stdSpace D.E D.SecondFactorIndex).J`. Let
`μ⁻ = (untwistedDescentPair j).colsMinus` be the family of Young diagrams, one at each infinite
place and given by its column counts. The group acts by `weightRep μ⁻ 0` on coordinate vectors
indexed by the standard fillings `WeylIndex` of `μ⁻`. There is a tight frame of such vectors `η T`,
one for each filling `T` of `μ⁻` with increasing columns (`ColumnFilling`): (a)
`∑ T, ⟨η T, ξ⟩ η T = hk² ξ` for all `ξ`, where `hk = hookNumberMinus j` is the hook number of `μ⁻`
and `⟨·, ·⟩ = gramForm` is the Hermitian form of the integer Gram matrix; (b) `γ` takes the complex
conjugate of each `η T` to an integer vector; (c) each has squared norm (`weylNormSq`, for that
form) at most `hk²` after every automorphism of `ℂ`. 

### `exists_tight_frame_formTuples`

 A tuple (`FormTuples j`) has one form for each `i` in the finite set `ChoiceIndex j`, given by
its values at the classes `c` in `D.SecondFactorClasses`, the double cosets of `U(V°)(𝔸_f)` by the
rational points and a principal congruence subgroup. The values are coordinate vectors, indexed by
standard fillings (`WeylIndex`), of the representation `weightRep` whose weight is the family of
Young diagrams `μ⁻ = (untwistedDescentPair j).colsMinus`. Let `δ c` be an element of the rational
unitary group of `V°` for each class `c`. There are tuples `f a`, for `a` in `TightFrameIndex j`,
with (a) `∑ a, ⟨f a, ζ⟩ f a = hk² ζ` for all `ζ`, where `hk` is the hook number of `μ⁻`; (b) `δ c`
takes the complex conjugate of the value of `f a` at `(i, c)` to an integer vector; (c) squared norm
(`formTupleNormSq`) at most `hk²` at every automorphism of `ℂ`. 

### `comparisonOp_eq_sum`

 The operator `U_ϑ = comparisonOp j ϑ` is a sum of operators of rank one: if the tuples `f a`
satisfy `∑ a, ⟨f a, ζ⟩ f a = hk² ζ` for all tuples `ζ` of forms on `V°`, with the hook number
`hk = hookNumberMinus j`, then `U_ϑ φ = ∑ n_Aut ⟨φ′, φ⟩ φ′`. Here `n_Aut = D.chosenGroupOrder` and
`φ′` runs over the glued forms `glue_ϑ (f a) = glue j ϑ (f a)`. 

### `comparisonOp_mem_integralForms`

 Let `ϑ` be a twist (a tame character of `U(1)`, ramified at a finite set `Q` of places), `l` a
prime that does not divide the product `ϑ.normQ` of the norms of the places in `Q`, and `ι` a ring
homomorphism `ℂ → ℂ_[l]`. A form on `V_j`, the target of the `j`-th lift, is integral at `ι`
(`integralForms ι`) if for every `g` the vector `g⁻¹ ι (φ g)` has coordinates of norm at most `1`.
The operator `comparisonOp j ϑ`, an integer multiple of the gluing map `glue j ϑ` after its adjoint,
takes integral forms to integral forms. 

### `card_prod_mul_card_tightFrameIndex_mul_sq_le`

 A tuple of forms on the definite space `V°` has one value for each pair of an index in
`ChoiceIndex j` and a class in `D.SecondFactorClasses`. The number of these pairs, times the square
of `#(TightFrameIndex j) n_Aut hk²`, is at most `exp (2 f m b log² b)`. Here `TightFrameIndex j` is
the set of such pairs together with a filling with increasing columns of the Young diagrams `μ⁻`
that give the weight of the forms on `V°`, `hk = hookNumberMinus j` is the hook number of `μ⁻` and
`n_Aut = D.chosenGroupOrder` is a multiple of the orders of all stabilisers; `f = D.f` is the number
of infinite places, `m = D.m` the number of lifts in the chain and `b = D.b`, with `log b = D.logB`,
the weight at the infinite places in `D.bPlaces`. 

### `normSqAt_comparisonOp_le`

 Let `φ` be a form on `V_j`, the target of the `j`-th lift at the trivial twist `1`, and
`φ.normSqAt σ` the weighted sum over classes of the squared norms of its values after applying an
automorphism `σ` of `ℂ`. The operator `U_1 = comparisonOp j 1`, a multiple of the gluing map
`glue j 1` after its adjoint, multiplies this number by at most `exp (6 f m b log² b)`. Here
`f = D.f` is the number of infinite places, `m = D.m` the number of lifts and `b = D.b` the weight
parameter, with `log b = D.logB`. 

### `isComparisonOperator_comparisonOp`

 The operators `U_ϑ = comparisonOp j ϑ = n_Aut hk² glue_ϑ glue_ϑ*` on the forms on `V_j`, one for
each twist `ϑ`, satisfy `IsComparisonOperator`. Here `glue_ϑ = glue j ϑ` builds a form on `V_j` from
a tuple of forms on `V°`, `n_Aut = D.chosenGroupOrder` and `hk = hookNumberMinus j`. That is, for
the theta lift `Θ_ϑ = D.goodLift ϑ j` and the nonzero ratio
`ρ_ϑ = heckeValueProd j ϑ / heckeValueProd j 1` of Hecke values,
`⟨Θ_ϑ y', U_ϑ Θ_ϑ y⟩ = ρ_ϑ ⟨y', U° y⟩` with `U°` positive definite and independent of `ϑ`. Also,
`U_ϑ` takes lifts to forms orthogonal to the false lifts, which are the forms orthogonal to the
lifts with the same idempotent and Hecke conditions at a split place. `U_ϑ` keeps integrality above
the primes that do not divide `ϑ.normQ`, and `U_1` multiplies norms by at most
`exp (3 f m b log² b)`, with `f = D.f`, `m = D.m` and `b = D.b`. 

### `finrank_range_goodLift`

 The lift `D.goodLift ϑ j` is injective, so the lifts have the dimension of the good forms on
`W_j`. 

### `range_goodLift_le_range_inf_ker`

 For a split place `w` off the level, the lifts lie in the image of the idempotent `e₀ = D.e₀`
that cuts out the good forms and are killed by the Hecke polynomial `heckePolyOnForms` at
`liftHeckeRoot w`, a power of the norm of `w` times a power of the value of the Weil data's
character at `w`. 

### `normSqAt_starProjection_range_goodLift_le`

 Let `y` be a form on `V_j` that is orthogonal to the false lifts. Then the orthogonal projection
of `y` to the lifts has norm (`normSqAt`) at most that of `y`, at every automorphism `σ` of `ℂ`. 

### `liftCompression`

 For operators `U_ϑ` on the forms on `V_j`, the operator `pr U_ϑ` on the lifts (the range of
`D.goodLift ϑ j`), with `pr` the orthogonal projection to them. 

### `IsComparisonOperator.exists_normDet_sq_mul_det_eq`

 Let `Θ_ϑ = D.goodLift ϑ j` be the theta lift at the twist `ϑ` to the forms on `V_j`. Its source
is the good forms (the image of the idempotent `D.e₀`, a space of dimension `d`) on the hermitian
space `W_j = D.spaceW j`. Let `ρ_ϑ` be the ratio of the values at `ϑ` and at `1` of
`heckeValueProd j`. Let `U` be a comparison operator, so that `⟨Θ_ϑ y', U_ϑ Θ_ϑ y⟩ = ρ_ϑ ⟨y', U° y⟩`
with `U°` positive definite. Then the Gram determinant `Θ_ϑ.normDet ^ 2 = det (Θ_ϑ* Θ_ϑ)`, times the
determinant of `pr U_ϑ = liftCompression U ϑ`, is `C ρ_ϑ ^ d` for a constant `C ≠ 0` that does not
depend on `ϑ`. 

### `IsComparisonOperator.norm_padic_det_liftCompression_le`

 Let `ϑ` be a twist, ramified at a finite set `Q` of places with product of norms `ϑ.normQ`, and
`ι` an isomorphism of `ℂ` with `ℚ̄_l` for a prime `l` that does not divide `ϑ.normQ`. Let `U` be a
comparison operator: `U_ϑ` takes lifts to forms orthogonal to the false lifts and keeps integrality
at `ι`. Let `ClearsProjection` hold with `β`: for some operator `Λ` on the lifts with
`|ι (det Λ)| ≥ exp (-d r β)` and the orthogonal projection `pr` to the lifts, `Λ (pr y)` is integral
at `ι` for all integral `y` orthogonal to the false lifts. Then `det (pr U_ϑ)`, with
`pr U_ϑ = liftCompression U ϑ`, has norm at most `exp (d r β)` at `ι`, with `d` the dimension of the
good forms on `W_j = D.spaceW j` and `r = D.r` the rank of `W_j`. 

### `IsComparisonOperator.norm_map_det_liftCompression_le`

 Let `U` be a comparison operator on the forms on `V_j`, the target of the `j`-th lift, and
`pr U_1 = liftCompression U 1` its compression to the range of the untwisted lift. The image of
`det (pr U_1)` under every ring automorphism `σ` of `ℂ` has modulus at most
`exp (3 d f m b log² b)`. Here `d` is the dimension of the good forms on `W_j = D.spaceW j`,
`f = D.f` the number of infinite places, `m = D.m` the number of lifts in the chain and `b = D.b`,
with `log b = D.logB`, the weight at the infinite places in `D.bPlaces`. 

### `mFoldTwist_one_pow`

 The `j`-th power of the trivial `m`-fold twist, formed as a tame character (`TameChar.pow`), is
the trivial tame character `TameChar.one`. 

### `heightLe_liftDeterminant_ratio`

 The cost of one lift: for a family of twists `ξ_ι = θ ι` as in `IsRegularFamily`, the ratio
`Z_j (1) / Z_j (ξ_ι ^ j)` has height at most `d k (log b · denominatorBudget - directionAmount)`.
Here `d = D.targetDim` is the dimension of the good forms, `k = D.k = D.r + 1 - D.m`,
`log b = D.logB` is a parameter, `denominatorBudget = D.denominatorBudget` is the budget for
denominators and `directionAmount = D.directionAmount` is the sum over the infinite places `σ`, of
weight `κ = D.weight σ`, of `D.jetSize κ = log κ! + κ log (M / Ω)`, the size of a derivative of
order `κ`, less the prime sum `D.primeSum κ σ` that measures its divisibility. 
