---
{
  "module": "src/New/Determinant/Norms/AdjointThetaLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The lift Θ_W, its adjoint and its norm

For a descent pair (`New.DescentPair`, a descent datum) with spaces W and V, the lift Θ_W is the
theta lift from forms on W to algebraic forms on V. The descent `New.DescentPair.normalizedDescent`
maps forms on V to functions on the adelic group of W; it is defined as a class sum and shown here
to be the adjoint of Θ_W. Both commute with the finite group of the chosen places. The finite datum
of the lift is the block datum modulo `π_M Q` times the vacuum, and the block datum is sharp for the
level `J_M`. For the pair `New.Data.descentPair D ϑ j`, which is `(W_j, V_j)` with a tame character
ξ = `ϑ`, the lift Θ_{j,ξ} = `New.Data.singleLift` goes from the forms of level `J_M` on W_j to the
definite space V_j.

## Main definitions and results

* `New.DescentPair.thetaLift`: the lift Θ_W from forms on W to forms on V. It is the lift
  `New.formLift` by the datum `New.DescentPair.fockDatum` of the highest vector, read as an
  algebraic form.
* `New.Data.singleLift`: the lift Θ_{j,ξ} on `New.Data.principalForms` on W_j. It is Θ_W for the
  pair `New.Data.descentPair` when 1 ≤ j ≤ m and 0 otherwise.
* `New.DescentPair.inner_thetaLift`: `New.DescentPair.normalizedDescent` is adjoint to
  `New.DescentPair.thetaLift`, for the Petersson product on `W` and the class sum product on `V`.
* `New.Data.coe_adjoint_singleLift`, `New.Data.normalizedDescent_eq_zero_iff`: the adjoint of
  Θ_{j,ξ} is the descent θ, so θ kills exactly the forms orthogonal to the lifts.
* `New.Data.singleLift_injective`, `New.Data.exists_hasSum_rallisTerm_inner_singleLift`: Θ_{j,ξ} is
  injective, and its Gram form is a constant `A` times the factor `New.DescentPair.gramFactor` of
  the pair times the sum of the terms `New.Data.rallisTerm`.
* `New.Data.exists_hasSum_inner_singleLift`: the same Gram form as a constant `c` times
  `New.DescentPair.twistFactor` times the sum of the terms `cosetTerm`.

Notions from other files:
* `New.Data.descentPair`: the pair of W_j, of rank r, and the definite space V_j, of rank r + t,
  with the character χ_j ξ = `New.Data.liftChar` of weight −κ_j and the places
  `New.Data.levelPlaces`.
* `New.Data.principalForms`: the forms of parameter λ^Y (twice it is `New.Data.paramW`) and level
  `J_M`, which is principal at the chosen places and maximal elsewhere.

## Relation to the literature

For every tame twist, the theta lift from U(W_j) to a definite unitary group of much larger rank is
injective, and its Gram form is a non-zero twist-free constant times an explicit count at the level
and the twist's conductor times a sum of Hecke operators. The Rallis inner product in the convergent
range, with small-support data giving injectivity at a level, is known in the literature. Related
work: J.-S. Li, Non-vanishing theorems for the cohomology of certain arithmetic quotients, 1992;
Cossutta–Marshall, Theta lifting and cohomology growth in p-adic towers, arXiv 1106.2765, 2011;
Rallis, Injectivity properties of liftings associated to Weil representations, 1984; Rallis,
L-functions and the oscillator representation, 1987.



## The theta lift of a descent pair as an equivariant map of forms

* `New.DescentPair.normalizedDescent_mul_eq_normalizedDescent_formAction`: the descent θ turns the
  action `New.DescentPair.formAction` into right translation by the stabiliser of the standard
  lattice.
* `New.DescentPair.thetaLift`, `New.Data.singleLift`: the lifts, with their equivariance.


### `DescentPair.omega_fockDatum_eq_inv_prod_smul`

 The pair `(k, k')` scales the datum. Let `k` lie in the stabiliser of the standard lattice in
the finite adelic group of `W`, let `s` be its reduction at the chosen places of the pair, and let
`k'` be the lift to the finite adelic group of `V` of the family `diag(s_w, 1)`. The representation
`O.pairThetaKernel.ω` is the Weil representation of `U(W) × U(V)` on the Schwartz space of
`Hom(W, V)`, and `O.fockDatum ξ` is the vector of that space made of the Fock polynomial of `ξ` at
the real places and the block datum at the finite places. Here `ξ` is any vector of the
representation of weight `O.columnCount`, in coordinates indexed by `WeylIndex n O.columnCount`.
Then `(k, k')` multiplies `O.fockDatum ξ` by `χ(s)⁻¹`, where `χ(s) = ∏_w ψ_w(det s_w)` and
`ψ = O.tamePart` is the tame part of the character of the pair. 

### `DescentPair.coe_formAction`

 An element `s` of the finite group of the chosen places acts on a form on `V` as
`∏_w ψ_w(det s_w)` times translation by the lift of the family `diag(s_w, 1)`, whose block `s_w`
sits on the rows `O.incl`, the embedding of the indices of `W` into those of `V`. Translation is the
representation `algFormRep` on algebraic forms of weight `O.columnCount`, twisted by the power
`O.detExp` of the determinant. 

### `DescentPair.normalizedDescent_mul_eq_normalizedDescent_formAction`

 Equivariance of the descent θ = `O.normalizedDescent`, which maps forms on V to functions on the
adelic group of W. Let k lie in the stabiliser of the standard lattice in the finite adelic group of
W, and let s be its reduction at the chosen places of the pair. Then (θΞ)(gk) = θ(ρ(s)Ξ)(g) for
ρ = `O.formAction`, every form Ξ on V and every adelic point g. 

### `DescentPair.FitsParams.isArrow_fockDatum`

 If the parameter `l` on `W` fits the pair, the datum of the highest vector is an arrow from `W`
to `V`: the theta lift by it takes forms of parameter `l` to forms of parameter `O.paramV`. 

### `DescentPair.FitsParams.isArrow_swap_fockDatum`

 If the parameter `l` on `W` fits the pair, the datum of the highest vector is an arrow from `V`
to `W` between the conjugate types, for the transposed theta kernel. 

### `DescentPair.thetaLift`

 The lift `Θ_W` from forms on `W`, of any level and of a parameter `l` that fits the pair, to
algebraic forms on `V`: the theta lift by the datum `O.fockDatum` of the highest vector, read as an
algebraic form. That `l` fits the pair (`New.DescentPair.FitsParams`) means that it corresponds to
the parameter `O.paramV` on `V` and to the numbering and column multiplicities of the pair;
`O.signs` are the signs of `W` and `typeKernel l O.signs` is the type of parameter `l` there. 

### `DescentPair.ofAlgForm_thetaLift`

 The function on the adelic group of `V` attached to the algebraic form `Θ_W y` is the theta lift
of `y` by the datum of the highest vector. 

### `DescentPair.coe_thetaLift`

 The algebraic form underlying `Θ_W y` is the image under `New.Space.toAlgForm` of the theta
lift of `y` by the datum of the highest vector. 

### `DescentPair.thetaLift_formRep`

 Let `y` be a form on `W` of a parameter `l` that fits the pair (`O.FitsParams l`). Let `k` lie
in the stabiliser of the standard lattice in the finite adelic group of `W`, with reduction `s` at
the chosen places. Then the lift `Θ_W` of the translate of `y` by `k` is `O.formAction s` applied to
`Θ_W y`. 

### `DescentPair.hasHeckePolynomial_thetaLift`

 Let `w` be a split place such that neither `w` nor `w̄` is a chosen place or a place of the
twist, and let `y` be a form on `W` of a parameter `l` that fits the pair (`O.FitsParams l`). If `y`
is spherical at `w` and the Hecke polynomial at `X` acts on it by `p(X)`, then its lift `Θ_W y` is
spherical at `w` and the Hecke polynomial at `X` acts on it by
`∏_{i<t}(1 − q^i α X) · p(q^t α β⁻¹ X)`. Here `q` is the norm of `w`, `t` is the rank of `V` minus
the rank of `W`, and `α`, `β` are the values `New.AutChar.frobValue` at `w` of the characters
`O.charW` of `W` and `O.charV` of `V`, respectively. 

### `Data.singleLift`

 The lift `Θ_{j,ξ}`, for the tame character `ξ = ϑ`, from the forms of level `J_M` on `W_j` to
the forms on `V_j`. It is the restriction of the lift `Θ_W` of the pair `D.descentPair ϑ j`, and `0`
for `j` outside `1, …, m`. 

### `Data.singleLift_apply`

 For `1 ≤ j ≤ m`, the lift `D.singleLift ϑ j` is the theta lift of the pair
`D.descentPair ϑ j`. 


## Formulas for lift and descent, and the block datum

`M` is the family `chosenPlace` of chosen places and `Q` the family `twistPlace` of the places of
the twist.

* `New.DescentPair.blockFn`: the block datum as a function modulo `π_M Q`.
* `New.DescentPair.blockDatum_eq_vacuumDatum`: `New.DescentPair.blockDatum` is the vacuum datum of
  `New.DescentPair.blockFn`.
* `New.DescentPair.isSharpFn_blockFn`, `New.DescentPair.gramFactor_div_card`: the block datum is
  sharp, and the index of the level on `V` times its mass `New.DescentPair.blockMass` is `c_Q` times
  a factor of the chosen places.


### `DescentPair.inner_thetaLift`

 The descent `O.normalizedDescent` is adjoint to the lift `Θ_W = O.thetaLift hfit`: for a form
`y` on `W` whose parameter fits the pair `O` and a form `Ξ` on `V`, the inner product of `Θ_W y` and
`Ξ` on `V` equals the Petersson product of `y` and `O.normalizedDescent Ξ` on `W`. 

### `DescentPair.isForm_normalizedDescent`

 If the parameter `l` on `W` fits the pair (`New.DescentPair.FitsParams`), the descent
`O.normalizedDescent Ξ` of a form `Ξ` on `V` is a form of parameter `l` on `W`. 

### `DescentPair.integrable_smul_vectorKernelForm`

 For a form `y` on `W` whose parameter fits the pair, the function `g ↦ y(g) θ_W(g, ·)` with
values in the forms on `V` is integrable on `[U(W)]`. Here `θ_W(g, ·) = O.vectorKernelForm g`. 

### `DescentPair.ofAlgForm_vectorKernelForm`

 For the descent pair `O` and a point `g` of `U(W)(𝔸)`, `O.vectorKernelForm g` = `θ_W(g, ·)` is
an algebraic form on the definite space `V = stdSpace E n`, and `ofAlgForm O.paramV 1` turns it
into a function on `U(V)(𝔸)` (all signs `1`). This function is the theta kernel
`h ↦ θ(ω(g, h) φ_W)` of the pair, with the characters `O.charW` of `W` and `O.charV` of `V`, where
`φ_W` is the datum `O.fockDatum` of the highest weight vector of weight `O.columnCount`. 

### `DescentPair.thetaLift_eq_integral`

 Let the parameter `l` on `W` fit the descent pair `O`, and let `y` be a form on `W` of the type
`typeKernel l O.signs` of parameter `l` at the real places. Then the theta lift
`Θ_W y = O.thetaLift hfit y` is `∫ y(g) θ_W(g, ·) dg` over `[U(W)]`. Here
`θ_W(g, ·) = O.vectorKernelForm g`, the measure is that of the Petersson product, and the integral
has values in the forms on `V`. 

 ### The block datum and the constant in the Gram form 

### `card_isUnit_submatrix`

 Over a finite commutative ring `R`, the number of `n × r` matrices whose square block on the
rows `ι` is invertible is `card (GL r R) · (card R) ^ ((card n − card r) · card r)`: the block is an
element of `GL r R`, and the other rows are free. 

### `DescentPair.blockFn`

 The block datum as a function of `n × r` matrices `x` modulo `π_M Q = O.levelModulus 1`: with
`x_w` the reduction of `x` at `w` (`levelResidueAt`), it is `0` unless at every chosen place `x_w`
is the inclusion matrix of `O.incl`, the embedding of the indices of `W` into those of `V`, and then
it is `∏ ψ_w (det x'_w)` over the places `w` of the twist, with `x'_w` the block on the rows
`O.incl` (`New.DescentPair.residueBlockDatum`). 

### `DescentPair.blockDatum_eq_vacuumDatum`

 The finite datum `O.blockDatum` of the theta kernel, defined modulo `π_M² Q`, is also the datum
given by the function `O.blockFn` modulo `π_M Q = O.levelModulus 1` and the vacuum elsewhere. 

### `star_mulChar_det_mul_self`

 For a complex multiplicative character `χ` of a finite field and a square matrix `X` over that
field, the squared modulus of `χ(det X)` is `1` if `X` is invertible and `0` otherwise. 

### `DescentPair.bijective_map_levelResidueAt`

 Chinese remainder theorem for matrices: a matrix modulo `π_M Q = O.levelModulus 1` is the same
as the family of its reductions at the chosen places and the places of `Q`. 

### `DescentPair.blockFn_normSq`

 The squared norm of the block datum `O.blockFn`: the sum of `|O.blockFn x|²` over the `n × r`
matrices `x` modulo the product `π_M Q = O.levelModulus 1` of the chosen places `M` and the places
`Q` of the twist, two finite families of places that come with the pair. The function is `0` unless
`x` is the inclusion matrix of `O.incl` at every chosen place, and is then a product over `w ∈ Q` of
characters of the determinant of the block on the rows `O.incl`. So it counts one matrix at each
chosen place; at `w ∈ Q`, of norm `q_w`, it counts the matrices whose block on those rows is
invertible, the other `O.rankDiff` rows being free. The sum is thus the order of
`O.TwistGL r = ∏_w GL_r(k_w)` times `(∏_w q_w) ^ (O.rankDiff * r)`. 

### `DescentPair.exists_reductionGL_eq_submatrix_of_blockFn_ne_zero`

 Let `x` be an `n × r` matrix modulo the product `π_M Q = O.levelModulus 1` of the chosen places
`M` and the places `Q` of the twist, and suppose that the block datum `O.blockFn` does not vanish at
`x`: at each chosen place `x` is the inclusion matrix of `O.incl : r ↪ n`, and at each place of the
twist its block on those rows is invertible. Then this block is the reduction modulo `π_M Q`
(`reductionGL`) of an integral point `k` of the finite adelic group of `W` that lies in the level
`J_M = levelOf O.chosenPlace ⊥` of the integral points that reduce to `1` at every chosen place. 

### `DescentPair.isSharpFn_blockFn`

 Let `π_M Q = O.levelModulus 1` be the product of the chosen places and the places of the twist.
The block datum `O.blockFn`, which on matrices modulo `π_M Q` is the indicator of the inclusion
matrix at the chosen places times characters of the determinant of the block on the rows `O.incl` at
the places of the twist, is sharp for the level `J_M = levelOf O.chosenPlace ⊥`, principal at the
chosen places and maximal elsewhere. 

### `DescentPair.blockMass`

 The mass `c_Ψ` of the block datum: the sum of `|O.blockFn x|²` over the `n × r` matrices `x`
modulo `π_M Q` (`New.DescentPair.blockFn_normSq`), divided by the number of these matrices and by
the index `∏_{w ∈ M} |GL_r(k_w)|` of the level `J_M`. 

### `DescentPair.isSharp_blockDatum`

 Suppose that the signs of `W` agree or that `π_M Q ≠ (1)`. Then the finite datum `O.blockDatum`
is sharp (`New.SiegelWeil.IsSharp`) for the level `J_M = levelOf O.chosenPlace ⊥`, off the places of
`π_M Q` and their conjugates, and its mass is `c_Ψ = O.blockMass`. 

### `DescentPair.gramFactor`

 The index of the level on `V`, times the sum of `|O.blockFn x|²` over the matrices `x` modulo
`π_M Q` (`New.DescentPair.blockFn_normSq`), over the index of the level `J_M` on `W`. Divided by the
number of these matrices, it is the index of the level on `V` times the mass `c_Ψ` of the block
datum (`New.DescentPair.stdLevelIndex_mul_blockMass`), and this is `c_Q` times a factor of the
chosen places (`New.DescentPair.gramFactor_div_card`). 

### `DescentPair.twistFactor`

 The constant `c_Q = (Nm Q) ^ (r t) ∏_{w ∈ Q} ∏_{i = t + 1}^{t + r} (1 - q_w ^ (-i))`. Here `r`
is the rank of `W`, `t = O.rankDiff`, so that `V` has rank `r + t`, `q_w` is the norm of `w`, and
`Nm Q` is the product of the `q_w` over `w ∈ Q`. 

### `DescentPair.chosenFactor`

 The contribution of the chosen places to the norm of one lift: the product over the chosen
places `w` of `∏_{i = t + 1}^{t + r} (1 - q_w ^ (-i))` divided by the order of `GL_r(k_w)`, with
`r` the rank of `W` and `t = O.rankDiff`. 

### `DescentPair.chosenFactor_ne_zero`

 The factor of the chosen places is not zero, since `q_w ^ i ≠ 1` for `i ≥ 1`. 

### `DescentPair.stdLevelIndex_levelGroup_mul_card`

 The index of the level on `V`, times the order of `∏_{w ∈ Q} GL_r(k_w)`, is the product over all
places `w` of `M` and `Q` of the index in `GL_n(k_w)` of the group that fixes the basis vectors
indexed by `O.incl`. 

### `DescentPair.gramFactor_div_card`

 The constant `O.gramFactor` of the Gram form of the lift for the descent pair `O`, divided by
the number of `n × r` matrices modulo `π_M Q = O.levelModulus 1`, the product of the chosen places
`M` and the places `Q` of the twist, is `O.chosenFactor * O.twistFactor`. With
`t = O.rankDiff = n - r` and `f(q) = ∏_{i = t + 1}^{t + r} (1 - q ^ (-i))`, the first is
`∏_{w ∈ M} f(q_w) / |GL_r(k_w)|` and the second is `c_Q = (Nm Q) ^ (r t) ∏_{w ∈ Q} f(q_w)`, where
`q_w` is the norm of `w` and `k_w` its residue field. 


## The lift from W_j, adjoint to the descent

`Θ_{j,ξ}` with `ξ = ϑ`, or `Θ_j` for short, is the lift `D.singleLift ϑ j`, and
`J_M = levelOf D.chosenPlace ⊥` is the level of the forms `D.principalForms`.


### `rallisTerm`

 The term of a coset `γ` in Rallis' formula for two forms `y'`, `y` of principal level on a space
`V` of rank `r`, such as `W_j`. It is `mc(γ)⟨y', R(γ)y⟩` (`New.SiegelWeil.cosetTerm`), with the
vacuum coefficient `mc` (the matrix coefficient of the vacuum vector of the Weil representation) for
the rank `r + t = card (D.Y 1)` of `V_j` and the second character `(D.descentPair ϑ j).charV` of the
pair, divided by the number of `(r + t) × r` matrices modulo `π_M Q = D.twistModulus ϑ 1`. Here
`γ` is a coset of finite points modulo those that are integral away from the places of `π_M Q` and
their conjugates. 

### `liftSeries`

 The series `∑_γ mc(γ) γ` of Rallis' formula for the `j`-th lift with the tame character `ϑ`, on
functions on the adelic points of a unitary group of rank `r` with signs `s`. It is
`New.SiegelWeil.rallisSeries` for the rank `r + t = card (D.Y 1)` of `V_j`, the character
`(D.descentPair ϑ j).charV`, and the places off `π_M Q = D.twistModulus ϑ 1` and its conjugate. 

### `two_mul_card_rowIndex_lt`

 The rank `r + t` of `V_j` exceeds twice the rank `r` of `W_j`. 

### `exists_principalForms_eq_liftSeries`

 The series `D.liftSeries ϑ j` of a form of level `J_M` on a space `V` of rank `r` is a form of
level `J_M` on `V`. 

### `hasSum_cosetTerm_of_eq_liftSeries`

 Fix a tame character `ϑ`, a lift index `j` and a space `V` of rank `r` with signs `s`. The forms
`D.principalForms V` are those on `V` of the fixed parameter of `D` and of the level `J_M`,
principal at the chosen places and maximal elsewhere. Let `x`, `y`, `z` be such forms, with `z` the
series `D.liftSeries ϑ j y = ∑_γ mc(γ) γ y`. Here `γ` runs over the finite points of `U(V)` modulo
those integral away from `D.twistModulus ϑ 1` (the product of the chosen places and the places of
`ϑ`) and its conjugate, taken at representatives supported away from these places, and
`mc(γ) = vacuumCoeff (r + t) charV γ = (charV(det γ) · finMultiplier(γ) ^ (r + t))⁻¹`, for the rank
`r + t = card (D.Y 1)` of `V_j` and the character `charV` on that side of the `j`-th pair. Then
`⟨x, z⟩` is the sum of the terms `mc(γ) ⟨x, γ y⟩` (`New.SiegelWeil.cosetTerm`). 

### `exists_end_eq_liftSeries`

 For every `j`, every tame character `ϑ` and every space `W` of rank `r` with signs `s` there is
a linear endomorphism `R` of the forms of level `J_M` on `W` that sends every form `y` to the series
`D.liftSeries ϑ j y = ∑_γ mc(γ) γ y` of the formula for the inner product of two theta lifts
(Rallis' formula). The sum is over the finite points of `U(W)` modulo those integral away from the
chosen places, the places of `ϑ` and their conjugates; `γ` acts by right translation, and
`mc(γ) = (charV(det γ) · finMultiplier(γ) ^ (r + t))⁻¹`, for the rank `r + t` of `V_j` and the
character `charV` on that side of the `j`-th pair. 

### `rallisOperator`

 The operator `Ral_{j,ξ}` on the forms of level `J_M` on a space `V` of rank `r`: it sends a form
to its series `D.liftSeries ϑ j` (`New.Data.coe_rallisOperator_apply`). 

### `hasSum_inner_rallisOperator`

 The matrix coefficient `⟨x, R y⟩` of `R = D.rallisOperator ϑ j V` is the sum of the terms
`mc(γ) ⟨x, γ y⟩` (`New.SiegelWeil.cosetTerm`). 

### `inner_singleLift`

 Adjointness for 1 ≤ j ≤ m: the class sum inner product of the lift `D.singleLift ϑ j y` with a
form Ξ on V_j equals the Petersson product on W_j of y with the descent θΞ, the class sum
`(D.descentPair ϑ j).normalizedDescent Ξ` for the pair (W_j, V_j). 

### `coe_adjoint_singleLift`

 The adjoint of the theta lift `D.singleLift ϑ j` sends a form `Ξ` on `V_j` to the form on `W_j`
whose function on the adelic group `U(W_j)(𝔸)` is `θ Ξ`: at `g` it is the sum, over the classes `h`
of `U(V_j)` at the level of `Ξ`, of the conjugate theta kernel at `(g, h)` applied to `Ξ(h)`, each
class divided by the order of its automorphism group. 

### `adjoint_singleLift_apply`

 The descent is the inner product with the kernel: for a form `φ` on `V_j` and `g` in
`U(W_j)(𝔸)`, the value at `g` of the adjoint of the lift applied to `φ` is the inner product of the
form `New.DescentPair.vectorKernelForm` at `g` with `φ`. 

### `singleLift_eq_integral`

 The lift is integration against the kernel: the lift of a form `y` of level `J_M` on `W_j` is
the integral over `g` in `[U(W_j)]` of `y(g)` times the form `New.DescentPair.vectorKernelForm` at
`g`. 

### `normalizedDescent_eq_zero_iff`

 For `1 ≤ j ≤ m`, a form `Ξ` on `V_j` has descent `θ Ξ = 0` exactly when it is orthogonal to the
lifts of all forms of level `J_M` on `W_j`. 

### `ofAlgForm_singleLift`

 The function `ofAlgForm` on the adelic group of `V_j`, applied to the algebraic form
`D.singleLift ϑ j y`, is the theta lift `formLift` of `y`. 

### `singleLift_injective`

 Let `ϑ` be a tame character, that is a weight `0` character of `U(1)(𝔸)` that is at most tamely
ramified, at a finite set of places, and let `j` lie in `D.LiftIndex`, the integers `1, …, m` for
the number `m = D.m` of lifts of the data. Then the theta lift `D.singleLift ϑ j` by the `j`-th pair
twisted by `ϑ` is injective. 

### `exists_hasSum_rallisTerm_inner_singleLift`

 For `1 ≤ j ≤ m` there is a constant `A ≠ 0` such that for every tame character `ϑ` the Gram form
`⟨Θ_j x, Θ_j y⟩` of the theta lift `Θ_j = D.singleLift ϑ j` on the forms of level `J_M` on `W_j` is
`A` times `gramFactor` times the sum over `γ` of `mc(γ)⟨x, γ y⟩ / #matrices`. Here
`π_M Q = D.twistModulus ϑ 1` is the product of the chosen places and the places of `ϑ`. The index
`γ` runs over the finite points (`Gf`) of `U(W_j)` modulo the subgroup `localLevel` of those that
are integral away from the places of `π_M Q` and their conjugates. The coefficient is
`mc(γ) = (charV(det γ) · finMultiplier(γ) ^ (r + t))⁻¹`, with `r + t` the rank of `V_j` and
`#matrices` the number of `(r + t) × r` matrices modulo `π_M Q`. 

### `exists_hasSum_inner_singleLift`

 The Gram form of one lift, term by term: for `1 ≤ j ≤ m`, on the forms of level `J_M` on the
rank `r` space `W_j` of the data `D`, `⟨Θ_j x, Θ_j y⟩ = ∑_γ c_j c_Q mc(γ) ⟨x, γ y⟩`, with
`Θ_j = D.singleLift ϑ j` the theta lift to the definite space `V_j` of rank `r + t`. The constant
`c_j ≠ 0` does not depend on the tame character `ϑ`. With `Q` the places of `ϑ`, `c_Q` is
`New.DescentPair.twistFactor`. The sum runs over the finite points of `U(W_j)` modulo those that are
integral away from the places of `π_M Q = D.twistModulus ϑ 1` and their conjugates. As in
`New.SiegelWeil.cosetTerm`, a coset is represented by a point `γ` supported away from these places,
which acts by right translation. Its coefficient `mc(γ) = (charV(det γ) · finMultiplier(γ) ^
(r + t))⁻¹` (`New.SiegelWeil.vacuumCoeff`) is that by which `γ` changes the matrix coefficient of
the unramified vector of the Weil representation, for the character
`charV = (D.descentPair ϑ j).charV` on the side of `V_j`. 

### `exists_adjoint_singleLift_comp_eq`

 **Norm of one lift.** For `1 ≤ j ≤ m` there is a constant `c_j ≠ 0` such that for every tame
character `ϑ` the lift `Θ_j = D.singleLift ϑ j` satisfies `Θ_j^* Θ_j = c_j c_Q R` on the forms of
level `J_M` on `W_j`. Here `c_Q` is `New.DescentPair.twistFactor` and `R` is the series of Rallis'
formula (`New.Data.rallisOperator`). 

### `hasLiftHeckePolynomial_singleLift`

 Let `ϑ` be a tame character, let `1 ≤ j ≤ m`, and let `y` be a form of level `J_M` on `W_j` in
`D.eigenPart (D.spaceW j) p`: each `D.heckeOperator (w, i)`, which is `T_{w,i}` at a split place `w`
not above `M` and `0` elsewhere, acts on `y` by `p (w, i)`. Then at each split `w` with `w`, `w̄`
off the chosen places and those of the twist, the lift `D.singleLift ϑ j y` is spherical. Its Hecke
polynomial is the q-Pochhammer polynomial of rank `t` times the rank `r` polynomial of the
eigenvalues `p (w, ·)`, both at rescaled variables. 

### `heckePolyOnForms_liftHeckeRoot_singleLift_eq_zero`

 Let `ϑ` be a tame character, let `1 ≤ j ≤ m`, and let `w` be a split place such that `w` and
`w̄` are neither chosen places nor places of the twist. The Hecke polynomial operator
`H_w(X) = ∑_i (−X)^i q^{i(i−1)/2} T_{w,i}` on the forms on `V_j`, at the value `X = (α q^{t−1})⁻¹`,
kills the lift `D.singleLift ϑ j y` of every form `y` of level `J_M` on `W_j`. Here `q` is the norm
of `w` and `α` is the Frobenius value at `w` of the character `(D.descentPair ϑ j).charW`, the
character of the pair on the side of `W_j`. 

### `singleLift_principalRep`

 The lift `D.singleLift ϑ j` commutes with the finite group `D.chosenGL = ∏ GL_r(k_w)` of the
chosen places, which acts on the forms on `W_j` by `New.Data.principalRep` and on the forms on `V_j`
by `New.DescentPair.formAction`. 
