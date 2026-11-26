---
{
  "module": "src/New/OneLift/ComparisonOperator/GluingMaps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluingMaps.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/GluingMaps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The first factors and the gluing maps

The first factors `φ″_{ϑ,i}` on `V″` are integral away from `Q` and small for `ϑ = 1`, and their
theta series satisfy `c′_ϑ Ξ_{ϑ,i} = c″ 𝖥_i` with functions `𝖥_i` that do not depend on the twist.
Gluing them to forms on `V°` gives the map `glue_ϑ` to forms on `V_j`. Its adjoint, the period,
satisfies `c′_ϑ glue_ϑ* Θ_{j,ϑ} = Θ°`, where `Θ°` does not depend on the twist and is injective,
because products span. The map `glue_ϑ` keeps integrality away from `Q`, is short for `ϑ = 1`, and
takes the image of `Θ°` to forms orthogonal to the false lifts. The comparison operator, an integer
multiple of `glue_ϑ glue_ϑ*`, is built from it in `New.OneLift.LiftVolumeHeight`.

In the code `φ″` is `firstFactor`, `Ξ` is `firstFactorPairing`, `𝖥` is `choiceFn`, `glue_ϑ` is
`glue j ϑ` and `Θ°` is `periodLift`. The integer `M` is `D.M`, its factor `ϖ` is `D.piM`, and `Q` is
the set of places of the twist `ϑ`.

Notions from other files:
* `descentPair ϑ j`: the spaces `W_j` and `V_j` with the characters and levels for the twist `ϑ`;
  `untwistedDescentPair j` is its untwisted form. The diagram of the values of the forms on `V″` is
  `μ⁺` (`colsPlus`), that on `V°` is `μ⁻` (`colsMinus`).
* `ChoiceIndex j`: the choices `i`, each a matrix `Λ` with a class `h♭` and constant rows.
* `FirstFactorIndex j` indexes the basis of `V″`, `D.SecondFactorIndex` that of `V°`, and
  `D.SecondFactorClasses` is the set of classes of `U(V°)` at the level `J (ϖ²)`.
* `goodLift ϑ j`: the theta lift `Θ_{j,ϑ}` from good forms on `W_j` to forms on `V_j`.
* `normalizedDescent`: the descent, which sends a form on `V_j` to a function on `U(W_j)` by pairing
  it with the theta kernel over the classes of `U(V_j)`.
* `weylGauge`, `weylNormSq`: the gauge at a place over `l` and the squared norm of a vector in a
  representation given by a diagram.

## Relation to the literature

Integral forms pairing with a lift to an explicit L-value (pullback, seesaw) are known in the
literature in low rank.

Related work: Böcherer–Dummigan–Schulze-Pillot, Yoshida lifts and Selmer groups, 2012; Y.-S. Lee,
Hida family of theta lift from U(1) to definite U(2), 2024; Prasanna, Integrality of a ratio of
Petersson norms and level-lowering congruences, 2006.


 ### Tuples of forms on `V°`, the splitting and the lattices 

### `hookNumberMinus`

 The hook number `hk` of the diagram `μ⁻`, which gives the weight of the forms on `V°`. 

### `SecondFactorFormValues`

 The values of the forms on `V°`, with the invariant metric. 

### `_root_.New.Data.FormTuples`

 `𝒜^⊕`: one copy of the forms on `V°` for each choice. The level `J (ϖ²)` is sufficiently small
(all stabilisers of classes are trivial), so a form is the table of its values at representatives
of the classes, and an inner product is a plain sum over the classes. 

### `IsIntegralFormTuple`

 A tuple of forms on `V°` is integral at the place `φ` over `l` if all its values are, that is,
have `weylGauge` at most `1`. A matrix acts on the values by its inverse transpose, so the gauge is
that of the conjugate vector at the conjugate place. 

### `formTupleNormSq`

 The squared norm `‖ζ‖_σ²` of a tuple of forms on `V°`: a plain sum over the classes. 

### `card_firstFactorIndex_le_two_mul_n`

 The rank `r + 9 m + 1` of `V″` is at most `2 n_m`. 

### `card_rowIndex_sum_fin_le_two_mul_n`

 The rank `r + t = 6 r` of `V_j` is at most `2 n_m`. 

### `nonempty_carrierIndex_embedding_firstFactorIndex`

 The basis of `V″` is large enough to hold the divided directions: `D.CarrierIndex` embeds in
`FirstFactorIndex j`. 

### `hasColumnsBelow_of_eq_zero`

 If `card N ≤ card n` and the diagram `κ` has no column of height at least `card N`, then
`HasColumnsBelow n N κ` holds. 

### `card_padIndex_sum_flatIndex_sum_secondFactorIndex`

 The indices of `V″ ⊕ V°` other than those of `W_j` in `V″` are `t` in number. 

### `hasColumnsBelow_colsPlus`

 For the `j`-th pair `W_j, V_j` and the summand `V″` of `V_j` with basis `FirstFactorIndex j`:
the rank of `V″` is at most that of `V_j`, and the diagram `μ⁺`, given by its numbers `colsPlus τ h`
of columns of height `h` at the infinite place `τ`, has no column whose height is at least the rank
of `V″` and below the rank of `V_j`. 

### `hasColumnsBelow_colsMinus`

 For `D.descentPair ϑ j`, its diagram `μ⁻` (`colsMinus`) satisfies `HasColumnsBelow`: the rank of
`V°` is at most that of `V_j` (`D.RowIndex ⊕ Fin D.t`), and `μ⁻` has no column whose height is at
least the rank of `V°` and below the rank of `V_j`. 

### `splittingV`

 The splitting `V_j = V″ ⊕ V°` of the basis, for the pair `descentPair ϑ j`. The indices of `W_j`
come first in `V″`. The divided directions are given by an arbitrary embedding of `D.CarrierIndex`
in `FirstFactorIndex j`. The splitting and both embeddings in `FirstFactorIndex j` do not depend on
the twist. 

### `gluingLevel`

 The level `J_Λ` on `V″` of a matrix `Λ` modulo `ϖ²`. It is `rowFixingLevel` for the rows of `Λ`
and of `ϖ • 1`: its elements are `1` modulo `ϖ` and fix `Λ` modulo `ϖ²`, and modulo `ϖ² Q`, for `Q`
the product of the twist places, their columns off the indices of `W_j` are those of the identity
matrix. 

### `classAut_gluingLevel_eq_bot`

 The level `J_Λ` (`gluingLevel`) is sufficiently small: at every point `g` the stabiliser
`classAut` is trivial. 

### `glueLattice`

 The lattice `L_Λ` of a choice `i` with matrix `Λ = i.1`, given by the matrix `𝗀` (the field
`point`) of a basis. It is chosen once, for the trivial twist, and read as a lattice for the twist
`ϑ`. 

### `isGlued_splittingV_of_isGlued`

 A lattice that is glued for the twist `ϑ'` is glued for the twist `ϑ`. 

### `isGlued_glueLattice`

 The lattice `glueLattice j ϑ i` is glued for the matrix `Λ = i.1` (`IsGlued`): the congruence
modulo `ϖ` that defines it is, after a translation by a unique element of `congruenceGroup`, a
pair of conditions on the blocks `V″` and `V°`, and its inverse is integral on most of `V″`. 

### `weilScalar_glueLattice`

 The scalar `c_𝗀` of the lattice `L_Λ` does not depend on the twist. 

 ### The first factors 

### `firstFactorScale`

 The constant `c″ ≠ 0` that makes the vectors `c″ Υ_{ϑ,i} (h)` integral away from `Q`, and small
for `ϑ = 1`. Here `Υ_{ϑ,i}` is `leftSideSeries`, a theta kernel times a class sum of theta kernels
formed from the choice `i`. The constant depends neither on the twist nor on the choice. 

### `firstFactor`

 The first factor `φ″_{ϑ,i}`, the complex conjugate of `c″ Υ_{ϑ,i}`, where `Υ_{ϑ,i}`
(`leftSideSeries`) is a function on the finite points of `U(V″)` and `c″ = firstFactorScale j`. 

### `firstFactorPairing`

 The theta series `Ξ_{ϑ,i} (g) = ⟨φ″_{ϑ,i}, θ″_{ϑ,Λ} (g, ·)⟩` on `U(W_j)`. It is the sum
(`kernelClassSum`) over the classes `h` of level `J_Λ` of the theta kernel `θ″_{ϑ,Λ}` of
`(W_j, V″)` at `(g, h)`, with datum given by the rows of `Λ` stacked over those of `ϖ • 1`
(`stackOverGenScalar`) and polynomial given by `φ″_{ϑ,i} (h)`. 

### `firstFactorPairing_eq_mul_thirdExchangeLeftSide`

 The series `Ξ_{ϑ,i}` is `c″` times the left side `thirdExchangeLeftSide` of the third exchange,
the class sum over `U(V″)` whose multiple by a number is the twist-free function `choiceFn`. 

### `mul_firstFactorPairing_mem_rapidFunctions`

 Let `y` be a good form on the hermitian space `W_j = D.spaceW j`. The theta series
`firstFactorPairing j ϑ i` on `U(W_j)` of a twist `ϑ` and a choice `i` is a finite combination of
theta kernels, so its product with `y` is a rapidly decreasing automorphic function. 

### `exists_mul_firstFactorPairing_eq`

 The theta series `firstFactorPairing j ϑ i` on `U(W_j)` depends on the twist `ϑ` only through a
scalar: there are numbers `c ϑ` such that `c ϑ` times the series is `firstFactorScale j` times the
function `choiceFn j i`, neither of which involves `ϑ`, for all choices `i`. Moreover `|c ϑ|²` is a
constant `C`, possibly `0`, divided by `heckeValueProd j ϑ`, a product of three Hecke L-value
factors twisted by `ϑ`. 

### `twistFactor`

 The number `c′_ϑ` with `c′_ϑ Ξ_{ϑ,i} = c″ 𝖥_i` for all `i`. 

### `exists_norm_twistFactor_sq_eq`

 There is a constant `C`, possibly `0`, with `|c′_ϑ|² = C / heckeValueProd j ϑ` for every twist
`ϑ`; the denominator is the product of the Hecke values of the three exchanges. 

### `twistFactor_mul_firstFactorPairing`

 The defining equation `c′_ϑ Ξ_{ϑ,i} (g) = c″ 𝖥_i (g)` of `twistFactor`, where `𝖥_i`
(`choiceFn`) is a function on `U(W_j)` that does not depend on the twist. 

### `isIntegralAndSmall_firstFactor`

 The values of the first factor `φ″_{ϑ,i}` are integral away from the level of `ϑ`, and, if `Q`
is empty, their conjugates have squared norm at most `exp (f m b log² b)` (`IsIntegralAndSmall`). 

### `weylGauge_firstFactor_le_one`

 Arithmetic of the first factors: the value of `φ″_{ϑ,i}` at `h` is integral (`weylGauge` at
most `1`) at a place above a prime `l` that does not divide the norm of the level of `ϑ`. 

### `weylNormSq_firstFactor_le`

 Arithmetic of the first factors: for the trivial twist, every conjugate
`σ ∘ firstFactor j 1 i h` of the values of `φ″_{1,i}` has squared norm (`weylNormSq`) at most
`exp (D.f * D.m * D.b * D.logB ^ 2)`. 

 ### The gluing map and the slices of lifts 

### `glue`

 The gluing map `glue_ϑ`. For `ζ` in the copy `i` of the forms on `V°` it is `M ^ l₁` times the
sum, over the classes `h` of level `J_Λ` and `h°` of level `J (ϖ²)`, of the forms supported on the
class of `(h, h°) 𝗀` formed from the product vector `φ″ (h) · ζ (h°)` (`productForm`). Here `𝗀`
is the matrix of `glueLattice j ϑ i`, `M = D.M`, and `l₁` is
`DividedSplitting.denominatorExponent`, the exponent that repays the denominators of `𝗀`. 

### `inner_adjoint_glue`

 The period is a sum of slices. Let `φ` be a form on `V_j = V″ ⊕ V°` and `ζ` a tuple of forms on
`V°`. The inner product of `ζ` with the adjoint of the gluing map `glue j ϑ` at `φ` is `M ^ l₁`
(`M = D.M`, `l₁ = denominatorExponent`) times the sum, over the choices `i` with matrix `Λ = i.1`,
the classes `c` of `U(V°)` with representative `h° = c.out` and the classes `h` of `U(V″)` of level
`J_Λ = gluingLevel j ϑ Λ` (`stdClassSum`), of `⟨φ″ (h) · ζ (i, c), φ ((h, h°) 𝗀)⟩` (`gramForm`).
Here `φ″ = firstFactor j ϑ i`, `ε` splits the basis of `V_j` into those of `V″` and `V°`, the
product of vectors is `cartanProduct ε 1`, the point `(h, h°)` is the block matrix
`U.block ε (h, h°)`, and `𝗀` is the matrix of the lattice `glueLattice j ϑ i`. 

### `firstFactorChar_mul_upsilonU1_zpow`

 The character of the lift to `V_j = V″ ⊕ V°`: the product of `ν″ = firstFactorChar` and
`ν° = ν_η ^ (m / 2 - j)` is the character `charV` of `descentPair ϑ j`. All are characters of
`U(1)`, and `ν_η = upsilonU1` is the restriction of the character `υ` to the norm-one ideles. 

### `goodForm_mul_liftMod_congruenceGroup`

 A good form on `W_j` is invariant under the lifts `liftMod 𝗎` of the elements `𝗎` of the group
`J̄¹` (`congruenceGroup`) of matrices modulo `ϖ²` that are `1` modulo `ϖ`, since these lifts lie in
the level `J (ϖ)` that fixes it. 

### `conj_normalizedDescent_glue`

 The descent to `U(W_j)` of the form `glue j ϑ ζ` on `V_j` glued from a tuple `ζ` of forms on
`V°` at the twist `ϑ`. Its conjugate at `g` is the sum, over the choices `i` and the matrices `u`
modulo `ϖ²` that are `1` modulo `ϖ` (`congruenceGroup`), of `M ^ l₁ c Ξ_i (g u) ⟨ζ_i, θ° (g u, ·)⟩`.
Here `M = D.M`, `l₁ = denominatorExponent`, `c` is the scalar `weilScalar` of the lattice of `i`,
`Ξ_i` is the theta series `firstFactorPairing j ϑ i`, the last factor is the pairing
`thetaKernelPairing` of the copy `i` of `ζ` with the theta kernel `θ°` of `W_j, V°`, and `g u` is
`g` times the lift `liftMod u`. 

### `inner_adjoint_glue_goodLift_eq_integral`

 Let `y` be a good form on `W_j`, `D.goodLift ϑ j y` its theta lift to `V_j` at the twist `ϑ`,
and `ζ` a tuple of forms on `V°`. The inner product of `ζ` with the adjoint of the gluing map
`glue j ϑ` at the lift is the integral, over `U(W_j)` modulo its rational points (`quotMeasure`), of
`y` against the conjugate of the descent `normalizedDescent` of `glue j ϑ ζ`, its pairing with the
theta kernel. 

### `mul_mul_thetaKernelPairing_mem_rapidFunctions`

 The product of a good form `y` on `W_j`, the series `Ξ_i = firstFactorPairing j ϑ i` and the
pairing `⟨ζ, θ° (g, ·)⟩` (`thetaKernelPairing`) is a rapidly decreasing automorphic function. 

### `inner_adjoint_glue_goodLift_eq_sum_integral`

 Let `y` be a good form on `W_j`, `D.goodLift ϑ j y` its theta lift to `V_j` at the twist `ϑ`,
and `ζ` a tuple of forms on `V°` with one copy `ζ_i` for each choice `i`. The inner product of `ζ`
with the adjoint of the gluing map `glue j ϑ` at the lift is the sum over `i` of
`M ^ l₁ c #J̄¹ ∫ y (g) Ξ_i (g) ⟨ζ_i, θ° (g, ·)⟩ dg`. Here `M = D.M` is the principal level,
`l₁ = denominatorExponent`, `c` is the scalar `weilScalar` of the lattice of `i` and `J̄¹`
(`congruenceGroup`) the group of matrices modulo `ϖ²` that are `1` modulo `ϖ`, all taken at the
trivial twist `1`. The series `Ξ_i` is `firstFactorPairing j ϑ i`, `thetaKernelPairing` pairs with
the theta kernel `θ°` of `W_j, V°`, and `quotMeasure` integrates over the quotient of `U(W_j)` by
its rational points. 

 ### Integrality and size of the gluing map 

### `glue_mem_integralForms`

 The gluing map `glue j ϑ`, from tuples of forms on `V°` to forms on `V_j`, keeps integrality.
Let `l` be a prime coprime to `ϑ.1.normQ`, the product of the norms of the places in the set Q of
the twist `ϑ`. Let `φ` be an embedding of `ℂ` in `ℂ_l` (`PadicPlace l`). If all values of the tuple
`ζ` are integral at `φ`, so are all values of `glue j ϑ ζ`. 

### `colsMinus_le`

 For the untwisted descent pair `untwistedDescentPair j`, at each infinite place `τ` and height
`i`, the number `colsMinus τ i` of columns of the diagram `μ⁻` is at most `D.gap`. 

### `card_secondFactorIndex_le`

 The rank of `V°` is at most `t = 5 r`. 

### `sum_mul_colsMinus_le`

 The diagram `μ⁻` has few boxes: at each place it has at most `D.gap` columns of each height, and
the heights are below the rank of `V°`, which is at most `t`. 

### `hookNumberMinus_le`

 The diagram `μ⁻` has few boxes, so its hook number (`hookNumberMinus`) is at most
`exp (x ^ 999)`, with `x = D.x` the length of the prime sum. 

### `card_columnFilling_colsMinus_le`

 The diagram `μ⁻` has few boxes, so the number of basis tensors of its shape with rows indexed by
the basis `D.SecondFactorIndex` of `V°` (`ColumnFilling`) is at most `exp (x ^ 999)`, with `x = D.x`
the length of the prime sum. 

### `card_stdClasses_le_exp_of_le`

 If the index type `n` has at most `2 * D.n D.m` elements, a level `K` that contains `J (ϖ²)`
(`principalLevel n (D.piM ^ 2)`) has at most `exp D.b` classes (`StdClasses K`). 

### `principalLevel_le_gluingLevel`

 At the trivial twist the level `J_Λ` (`gluingLevel`) of a choice, whose matrix `Λ` is its
first component, contains `J (ϖ²)`. 

### `M_pow_denominatorExponent_sq_mul_le_exp`

 The bound `(M ^ l₁)² · exp b · (n · exp b · G)² ≤ exp (f m b log² b)`. Here `M = D.M` is the
principal level, `l₁ = DividedSplitting.denominatorExponent` the exponent of `M` in the denominator
for the splitting `V_j = V″ ⊕ V°`, `exp b` bounds the numbers of classes of `U(V_j)` and `U(V″)`,
`n` the number of pairs of a choice and a class of `U(V°)`, `G = D.chosenGroupOrder` the bound on
the orders of the stabilisers, `f = D.f` the number of infinite places, `m = D.m` the number of
lifts and `b = D.b` the weight at the `b`-places, with `log b = D.logB`. 

### `weylNormSq_evalForm_productForm_le`

 One term of the gluing map at the trivial twist. Let `p = (i, c)` be a choice and a class of
`U(V°)`, `h` a finite point of `U(V″)` and `g` one of `U(V_j)`. Take the form on `V_j`
(`productForm`) supported on the class of `(h, c.out)` times the matrix of `glueLattice j 1 i`, made
from the product of the vectors `firstFactor j 1 i h` and `ζ p`. Let `σ` be a field automorphism of
`ℂ`. The squared norm (`weylNormSq`) of the value of this form at `g`, moved by `σ`, is at most
`A² exp (f m b log² b) ‖ζ‖_σ²`. Here `‖ζ‖_σ² = formTupleNormSq σ ζ`, `A = D.chosenGroupOrder` bounds
the orders of the stabilisers, `f` is the number of infinite places, `m` the number of lifts and `b`
the weight `exp D.logB`. 

### `piM_sq_mem_placeAt_descentPair_one`

 At the trivial twist `1`, every place `placeAt i` of the level of `V_j` (the places of
`descentPair 1 j`) contains `piM ^ 2`. 

### `normSqAt_glue_le`

 Norm bound for the gluing map at the trivial twist: for a tuple `ζ` of forms on `V°` and an
automorphism `σ` of `ℂ`, the squared norm `normSqAt σ` of the form `glue j 1 ζ` on `V_j` is at most
`exp (2 f m b log² b)` times `‖ζ‖_σ²` (`formTupleNormSq`). Here `f` is the number of infinite
places, `m` the number of lifts and `b` the weight `exp D.logB`. 

 ### Periods of false lifts 

### `hyperplaneSum_apply_eq_zero`

 Let `Ξ` be a form on `V_j`, for the pair `W_j, V_j` at the twist `ϑ` (`descentPair ϑ j`), in the
image of the idempotent `D.e₀` of the group algebra of `∏ GL_r (k_w)` over the residue fields `k_w`
of the chosen places `w`. Let `v` give a vector in `k_w ^ r` at each chosen place, not `0` at the
place `i`. Then `Ξ` is killed by the pure tensor of the elements `∑ χ_w (det h)⁻¹ h`, summed over
the invertible `h = 1 + u vᵀ` (`hyperplaneSum`), where `χ_w` is the residue character `tamePart`. 

### `normalizedDescent_eq_zero_of_mem_orthogonal`

 Let `Ξ` be a form on `V_j`, for the pair `W_j, V_j` at the twist `ϑ` (`descentPair ϑ j`). If `Ξ`
lies in the image of the idempotent `D.e₀` and is orthogonal to the theta lifts `D.goodLift ϑ j y`
of all good forms `y` on `W_j` (principal level, in the image of `D.e₀`), then its descent
`normalizedDescent Ξ`, the function on `U(W_j)` that pairs `Ξ` with the theta kernel, vanishes. 

### `tamePart_twistPlace_ne_one`

 For the pair `descentPair ϑ j`, its `tamePart` is not `1` at any place `twistPlace i`, that is,
at any place of its set `Q`. 

### `stdClassSum_gramForm_eq_zero_of_mem_falseLiftsAt`

 Periods of false lifts on `V_j` vanish, for the pair `W_j, V_j` at the twist `ϑ`. Let `Ξ` be a
false lift (`falseLiftsAt`): it lies in the image of `D.e₀`, is killed by the Hecke polynomial
operator for a split place `w` off the level at the value `liftHeckeRoot w`, and is orthogonal to
the lifts of good forms. Let `ε` split `V_j` as `V″ ⊕ V°`, with bases `N` and `l` and
`r + 2 rk V″ + 3 < t`. Let `h₁` be a finite point of `U(V″)` and `x` one of `U(V_j)` supported on
the places of the level and their conjugates. Let `κ` be a diagram given by column counts at the
infinite places, and `k` a function on the finite points of `U(V°)` with values vectors of weight
`κ`, whose coordinates, moved by the real points (`GInf`), are multiples of conjugate theta kernels
`pairTheta` of `W_j, V°` with Schwartz data `φ` fixed by the projection `Space.projOn` for the
places off the level. Let the conjugate-linear map `C` carry these vectors to the space of values of
`Ξ`, equivariantly for the representations `conjWeylRep` of `U(V°)_∞`. Then the pairing of `C (k h)`
with `Ξ ((h₁, h) x)` is left invariant under the rational points, and its class sum is zero at every
level `K` that fixes it. This is `stdClassSum_gramForm_eq_zero` for `descentPair ϑ j`. 

### `sum_slice_eq_zero_of_mem_falseLiftsAt`

 Slices of false lifts vanish. Let `w` be a split place (`star w ≠ w`) off the level of the pair
`descentPair ϑ j`, and let `Ξ` be a false lift at `w`: a form on `V_j = V″ ⊕ V°` in the image of the
projection `e₀` that is killed by the Hecke polynomial operator at `w` and is orthogonal to the
lifts of good forms. Let `h` be a finite point of `U(V″)`, `y` any vector of weight `μ⁺`
(`colsPlus`) on `V″` and `g` a point of `U(W_j)`. Then the sum, over the classes of `U(V°)` with
representative `h° = c.out`, of the pairing of `Ξ ((h, h°) 𝗀)` with the product (`cartanProduct`) of
`y` and `θ° (g, h°)` is `0`. Here `θ°`, the conjugate of `kernelVector`, is the theta kernel of
`W_j, V°` of weight `μ⁻` (`colsMinus`), any datum `Ψ` modulo `ϖ²` (`ϖ = D.piM`) and any character
`b`, and `𝗀 = L.point` is the matrix of a lattice `L` between `ϖ 𝒪ⁿ` and `𝒪ⁿ`. 

### `thetaKernelPairing_adjoint_glue_eq_zero`

 Let `Ξ` be a false lift on `V_j` at a split place `w` off the level of `descentPair ϑ j`: a form
in the image of `D.e₀` that is killed by the Hecke polynomial operator at `w` and is orthogonal to
the lifts of good forms. The adjoint of the gluing map `glue j ϑ` takes `Ξ` to a tuple of forms on
`V°`, one for each choice `i`, given by values at the classes `c`. Each of them has pairing `0` with
the theta kernel `θ° (g, ·)` of `W_j, V°` at every `g` in `U(W_j)`. 

 ### The map `Θ°`, the seesaw identity and the false lifts 

### `glueFactor`

 The number `c°_i = M ^ l₁ c_𝗀 #J̄¹ c″` of the choice `i`, with `c_𝗀` the scalar of the lattice,
`J̄¹` the group `congruenceGroup` and `c″ = firstFactorScale j`. It does not depend on the twist. 

### `twistFactor_mul_inner_adjoint_glue`

 Let `y` be a good form on `W_j` and `ζ` a tuple of forms on `V°`. Take the inner product of `ζ`
with the adjoint of the gluing map `glue j ϑ` at the theta lift of `y`, and multiply it by
`twistFactor j ϑ`, the scalar that carries the dependence of the series `firstFactorPairing` on the
twist `ϑ`. The result is the sum over the choices `i` of the number `glueFactor j i` times the
integral over `U(W_j)` modulo rational points of `y`, the function `choiceFn j i` and the pairing of
the copy `i` of `ζ` with the theta kernel of `W_j, V°`. 

### `periodLift`

 The map `Θ°` from the good forms on `W_j` to tuples of forms on `V°` whose copy `i` is
`c°_i ∫ y (g) 𝖥_i (g) θ° (g, ·) dg` (`inner_periodLift`). It is defined as `c′_1 glue_1* Θ_{j,1}`,
the left side of the seesaw identity at the trivial twist. 

### `inner_periodLift`

 The product of `Θ° y` with a tuple `ζ` is the sum over the choices `i` of `c°_i` times the
integral of `y 𝖥_i` against the pairing of `θ° (g, ·)` with the copy `i` of `ζ`. 

### `twistFactor_smul_adjoint_glue_comp`

 The seesaw identity `c′_ϑ glue_ϑ* Θ_{j,ϑ} = Θ°`: the number `twistFactor j ϑ` times the
composite of the lift `goodLift` with the adjoint of the gluing map `glue` is the map
`periodLift`, which does not depend on the twist. 

### `isOrthogonalToFalseLifts_glue_periodLift`

 For a good form `y` on `W_j`, the glued form `glue j ϑ (periodLift j y)` is orthogonal to the
false lifts at every split place off the level: the forms in the image of `e₀` that are killed by
the Hecke polynomial operator and are orthogonal to the lifts. 

 ### Injectivity of `Θ°` 

### `periodLift_injective`

 The map `periodLift j` from good forms on `W_j` to tuples of forms on `V°` is injective. 

### `twistFactor_ne_zero`

 The number `twistFactor j ϑ` is not `0`, since `Θ° = periodLift j` is injective and there is a
nonzero good form. 
