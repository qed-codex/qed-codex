---
{
  "module": "src/New/Determinant/Chain/NormOfChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The volume of ι on the target forms as a product of volumes of theta lifts

The volume of a linear map `u` between finite-dimensional Hilbert spaces is
`det (u* u) = u.normDet ^ 2`. For data `D`, the good forms (`New.Data.goodForms`) are the image of
the idempotent `New.Data.e₀`, and the target forms are the good forms on `Y₀`. `D.goodLift ϑ j` is
the restriction of the lift `D.singleLift ϑ j` to the good forms on `W_j`; its range is the space of
lifts.

* `New.Data.liftDeterminant`, `New.Data.chainDeterminant`: the volumes of the lift on the good forms
  and of `ι` on the target forms.
* `New.Data.exists_normDet_goodLift_sq_eq`: the volume of one lift in terms of the determinant on
  the target forms of the series of Rallis' formula.
* `New.Data.exists_adjoint_chain_comp_eq_smul_rallisProduct`: on the target forms `ι* ι` is the
  product `New.Data.rallisProduct` of these series times `c_Q ^ m`, up to a factor `c ϑ`, where the
  absolute value of `c ϑ` is a product of ratios of Hecke values, a power of the norm of the modulus
  of `ϑ` and a positive constant.
* `New.Data.exists_div_chainDeterminant_one_eq`: the resulting formula for
  `chainDeterminant ϑ / chainDeterminant 1`;
  `New.Data.exists_chainDeterminant_pos_and_div_chainDeterminant_one_eq` joins it with the
  positivity of the volumes.
* `New.Data.range_goodLift_le`: the space of lifts is spanned by lifts of good eigenforms.

Notions from other files:
* `New.Data.MFoldTwist`: a twist `ϑ` whose first `m` powers are twists.
* `New.Data.principalForms`: the forms of the fixed parameter on a space that are fixed by the
  principal level at the chosen places.
* `New.Data.singleLift`: the lift from principal forms on `W_j` to algebraic forms on `V_j`.
* `New.DescentPair.twistFactor`: the constant `c_Q` in the norm of one lift.
* `New.Data.lowerChainAtLevel`: the map `ι` from forms of principal level on `Y₀` to algebraic forms
  on `Y_m` of the last level of the twist.
* `New.Data.HasAbsUpToNormPower`: `D.HasAbsUpToNormPower c f` says that `‖c ϑ‖²` is `(f ϑ)²` times a
  constant, possibly zero, and a fixed integral power of the norm of the modulus of `ϑ`.
* `New.Data.quotientRatio`: `D.quotientRatio i j ϑ` is the product of the ratios of Hecke values of
  `D.untwistedLiftChar j / D.untwistedLiftChar i` at the twist `ϑ ^ (j - i)`.

## Relation to the literature

See `New.Determinant.Chain.ChainNorms` for related work.


### `_root_.New.normDet_sq_eq_pow_mul_det`

 Let `u : U →ₗ[ℂ] V` be a linear map between finite-dimensional complex inner product spaces `U`
and `V`, and `S` an endomorphism of `U` with `⟪u x, u y⟫ = a ⟪x, S y⟫` for all `x`, `y`. Then
`u.normDet ^ 2`, the volume det(u* u), equals `a ^ finrank ℂ U * S.det`. 

### `liftDeterminant`

 The volume `liftDeterminant ϑ j` = det(u* u) = `u.normDet ^ 2` of the lift u = `singleLift` at
`j` for the twist ϑ^j, restricted to the good forms on U(W_j) (`New.Data.goodLift`). 

### `normDet_goodLift_sq_pos`

 For `1 ≤ j ≤ m` and every tame character `ϑ`, the volume `det(u* u) = u.normDet ^ 2` is
positive, where `u` is the lift from `W_j` for `ϑ`, restricted to the good forms: the lift is
injective. 

### `liftDeterminant_pos`

 For `1 ≤ j ≤ m` the volume of the lift from `W_j` for the twist `ϑ ^ j`, restricted to the good
forms, is a positive real number. 

### `Θ`

 The map ι_ϑ (`New.Data.lowerChainAtLevel`) restricted to the target forms, that is to the good
forms on Y₀. It takes values in the algebraic forms on Y_m whose weight has `columnsY` columns of
each height and last entry `lastEntry m`, and whose level is given by `lastResidueLevel` (trivial at
the chosen places, block upper triangular at the places of the twist) with the character
`lastLevelChar` made of the tame characters of the lifts on the diagonal blocks. 

### `chainDeterminant`

 The volume `chainDeterminant ϑ` = det(u*u) of u = ι_ϑ (`New.Data.lowerChainAtLevel`), the map
from forms of principal level on Y₀ to forms on Y_m, restricted to the target forms (the good forms
on Y₀). 

### `chainDeterminant_pos`

 For every m-fold twist `ϑ : D.MFoldTwist`, `D.chainDeterminant ϑ` is a positive real number.
This is the volume det(u* u) of the map u = ι_ϑ from forms on Y₀ to forms on Y_m, restricted to the
target forms. So this map is injective. 

### `exists_normDet_goodLift_sq_eq`

 For `j : D.LiftIndex`, so `1 ≤ j ≤ m`, there is a constant `A ≠ 0` with the following property.
For every tame character `ϑ`, let `u = D.goodLift ϑ j` be the lift `singleLift` restricted to the
good forms on `W_j = D.spaceW j`. Then its volume `normDet ^ 2 = det(u* u)` is `(A c_Q) ^ targetDim`
times a determinant, where `targetDim` is the dimension of the target forms. That determinant is the
one of `rallisOnGood`, the series of Rallis' formula for the `j`-th lift for `ϑ`, acting as a
spherical Hecke operator on the target forms, the good forms on `Y₀ = D.spaceY 0`. Here `c_Q` is the
constant `New.DescentPair.twistFactor` of `D.descentPair ϑ j`, the pair of spaces and the data of
that lift. 

### `rallisProduct`

 The product, in the order `j = 1, …, m`, of the operators `rallisOnGood` on the target forms for
the twists `ϑ ^ j` and the indices `j`. The `j`-th one is the series of Rallis' formula for the
`j`-th lift at `ϑ ^ j`, which acts as a spherical Hecke operator. 

### `exists_inner_weightedChain_eq`

 The squared norm of the weighted chain of lifts. The triangle of lifts is a triangular array of
spaces of forms, with theta lifts `triangleLift` from position `(i, n)` to position `(i, n + 1)`;
the flag `false` picks one of the two triangles, the one whose characters are twisted by powers of
`ϑ`. The chain of its first `m` lifts from `Y₀`, each times its weight `triangleGLCard`
(`Exchange.weightedChain`), is taken on the target forms. Its Gram form is `κ ϑ` times a ratio of
group orders, divided by the `m`-th power of the number of matrices modulo `D.twistModulus ϑ 1`
indexed by `D.Y 1 × D.RowIndex`, times the form of `New.Data.rallisProduct`. Here
`triangleGLCard false ϑ n` is the order of the general linear group in the `n`-th place of the
triangle over the residue ring of its modulus, and `D.twistModulus ϑ 1` is the product of the chosen
places and the places of the twist. The statement `HasAbsUpToNormPower κ f` says
`‖κ ϑ‖² = C (normQ ϑ)^k (f ϑ)²` with `C` and `k` independent of `ϑ`; here `f` is the product over
`1 ≤ i < j ≤ m` of `quotientRatio i j`, the ratios of Hecke values of the quotient of the `j`-th and
`i`-th lift characters at `ϑ ^ (j - i)`. 

### `exists_inner_chain_eq`

 The Gram form of the chain. For an `m`-fold twist `ϑ` let `Θ = D.Θ ϑ` be the chain of lifts from
forms on `Y₀` to forms on `Y_m`, restricted to the target forms. There are numbers `c ϑ`, a real `C`
(possibly `0`) and an integer `k` such that for all `ϑ`
* `‖c ϑ‖ ^ 2 = C (Nm Q) ^ k (∏_{1 ≤ i < j ≤ m} quotientRatio i j ϑ) ^ 2` (`HasAbsUpToNormPower`),
* `⟪Θ x, Θ y⟫ = c ϑ * c_Q ^ m * ⟪x, R y⟫` for all target forms `x` and `y`.

Here `Q` is the set of places of `ϑ` and `Nm Q = ϑ.normQ` the product of their norms `q_w`. The
operator `R = D.rallisProduct ϑ` is the product over `1 ≤ j ≤ m` of the series of Rallis' formula
for the `j`-th lift at `ϑ ^ j`. The number `c_Q = (D.descentPair ϑ 1).twistFactor` is
`(Nm Q) ^ (r t) ∏_{w ∈ Q} ∏_{t < i ≤ t + r} (1 - q_w ^ (-i))`, and `quotientRatio i j ϑ` is the
product of the ratios of Hecke values of the quotient of the `j`-th and `i`-th lift characters at
`ϑ ^ (j - i)`. 

### `isRamifiedRatio_of_mem_sigma`

 Let `ij = (i, j)` be a pair with `1 ≤ i < j ≤ m` and `χ_j = D.untwistedLiftChar j` the character
of the `j`-th lift without twist. Then `quotientRatio i j`, the product of the ratios of Hecke
values of `χ_j / χ_i`, is a ramified ratio: for some fixed `1 ≤ n ≤ m` and some ramified pair (a
character ramified at the chosen places and an integer `z`, the ratios taken at `1, …, z`), its
value at a twist `ϑ` is the product of the ratios of Hecke values of that pair at `ϑ ^ n`. 

### `card_sigma_Ioc_le`

 There are at most `m²` pairs `1 ≤ i < j ≤ m`. 

### `prod_quotientRatio_one`

 At the trivial twist the product of the ratios `quotientRatio i j` over `1 ≤ i < j ≤ m` is
`1`. 

### `prod_quotientRatio_nonneg`

 At every m-fold twist `ϑ : D.MFoldTwist`, the product of the ratios `D.quotientRatio i j ϑ` over
`1 ≤ i < j ≤ m` is nonnegative. 

### `HasAbsUpToNormPower.exists_norm_div_eq_mul_prod_quotientRatio`

 Let `c` satisfy `HasAbsUpToNormPower c f`, that is `‖c ϑ‖² = C (normQ ϑ)^k (f ϑ)²` with `C` and
`k` independent of `ϑ`, where `f` is the product of the ratios of Hecke values `quotientRatio i j`
over `1 ≤ i < j ≤ m`, and let `c 1 ≠ 0`. Then `‖c ϑ / c 1‖` is `normQ ϑ ^ (e / 2)` times the product
of the `quotientRatio i j ϑ`, for an integer `e` independent of the twist `ϑ`. 

### `exists_adjoint_chain_comp_eq_smul_rallisProduct`

 **Norm of the chain.** For an `m`-fold twist `ϑ` let `Θ = D.Θ ϑ` be the chain of lifts from
forms on `Y₀` to forms on `Y_m`, restricted to the target forms. There are a constant `C > 0`, an
integer `e` and numbers `c ϑ` such that for all `ϑ`
* `‖c ϑ‖ = C (Nm Q) ^ (e / 2) ∏_{1 ≤ i < j ≤ m} quotientRatio i j ϑ`, and
* `Θ* Θ = c ϑ * c_Q ^ m * R`.

Here `Q` is the set of places of `ϑ` and `Nm Q = ϑ.normQ` the product of their norms `q_w`. The
operator `R = D.rallisProduct ϑ` is the product over `1 ≤ j ≤ m` of the series of Rallis' formula
for the `j`-th lift at `ϑ ^ j`. The number `c_Q = (D.descentPair ϑ 1).twistFactor` is
`(Nm Q) ^ (r t) ∏_{w ∈ Q} ∏_{t < i ≤ t + r} (1 - q_w ^ (-i))`, and `quotientRatio i j ϑ` is the
product of the ratios of Hecke values of the quotient of the `j`-th and `i`-th lift characters at
`ϑ ^ (j - i)`. 

### `exists_chainDeterminant_eq_pow_mul_prod_liftDeterminant`

 There are a constant `C > 0` and an integer `e` such that for every `m`-fold twist `ϑ` `det (Θ*
Θ) = (C (Nm Q) ^ (e / 2) ∏_{1 ≤ i < j ≤ m} quotientRatio i j ϑ) ^ d ∏_{1 ≤ j ≤ m} λ_j`. Here
`Θ = D.Θ ϑ` is the chain of lifts from forms on `Y₀` to forms on `Y_m`, restricted to the target
forms (the good forms on `Y₀`, of dimension `d = D.targetDim`), and `det (Θ* Θ)` is
`D.chainDeterminant ϑ`. The number `λ_j = D.liftDeterminant ϑ j` is `det (u* u)` for the `j`-th
single lift `u` at `ϑ ^ j` on the good forms (`goodLift`), `Nm Q = ϑ.normQ` is the product of the
norms of the places of `ϑ`, and `quotientRatio i j ϑ` is the product of the ratios of Hecke values
of the quotient of the `j`-th and `i`-th lift characters at `ϑ ^ (j - i)`. 

### `exists_div_chainDeterminant_one_eq`

 There is an integer `e` such that, for every twist `ϑ` whose first `m` powers are twists, the
ratio `chainDeterminant ϑ / chainDeterminant 1` is `(normQ ϑ ^ (e / 2) * ∏_{1 ≤ i < j ≤ m}
quotientRatio i j ϑ) ^ targetDim` times the product over `1 ≤ j ≤ m` of the ratios
`liftDeterminant ϑ j / liftDeterminant 1 j`. 

### `exists_chainDeterminant_pos_and_div_chainDeterminant_one_eq`

 **Factorization of the determinant.** For the data `D`, let `ϑ` be an `m`-fold twist
(`MFoldTwist`): a twist whose tame part has `ψ_wⁿ` nontrivial for all `w` in `Q` and `1 ≤ n ≤ m`.
Let `Θ = D.Θ ϑ` be the chain of lifts restricted to the target forms, and `u = goodLift` the lift at
`1 ≤ j ≤ m` for `ϑ ^ j`, restricted to the good forms on W_j. Then the volumes
`chainDeterminant ϑ` = det(Θ* Θ) and `liftDeterminant ϑ j` = det(u* u), with * the adjoint, are
positive. The ratio `chainDeterminant ϑ / chainDeterminant 1` is `(normQ ϑ ^ (e / 2) * ∏_{i < j}
quotientRatio i j ϑ) ^ targetDim` times the product of the ratios
`liftDeterminant ϑ j / liftDeterminant 1 j`, with an integer `e` independent of `ϑ`. 

### `HasSmallRatios.heightLe_inv_rpow_mul_prod_quotientRatio`

 Let `θ` be a family of twists indexed by the isomorphisms `ι : ℂ ≃ ℚ̄_l` for primes `l`, with
small ratios: `normQ (θ ι)`, the product of the norms of the places of the twist, is prime to `l`,
and for every ramified pair the inverse ratios of L-values at the powers `(θ ι) ^ (±j)`,
`1 ≤ j ≤ m`, have height at most `D.x₁`, the second cut-off of the data. Then the inverses of `normQ
^ (e / 2) * ∏_{1 ≤ i < j ≤ m} quotientRatio i j` at the `θ ι` form a family of height at most
`m² * D.t * D.x₁`. 

### `range_tupleIdem_le`

 Let `f` be a representation of the group algebra of `D.chosenGL`, the product of the finite
general linear groups at the chosen places, on a complex inner product space `U`. Let `c` be a good
tuple family: one of the finitely many admissible labellings of the chosen places by polynomials
over their residue fields. Then the range of the idempotent `tupleIdem D.RowIndex c` under `f` lies
in the range of `New.Data.e₀`, the sum of these idempotents over all good tuple families. 

### `singleLift_asAlgebraHom`

 The theta lift `D.singleLift ϑ j`, for a tame character `ϑ` and `1 ≤ j ≤ m`, commutes with the
group algebra of `D.chosenGL`, the product of the groups `GL_r` over the residue fields of the
chosen places. An element `x` acts through `principalRep` on `principalForms`, the forms on the
hermitian space `W_j = D.spaceW j` fixed by the principal level at the chosen places. It acts by
`groupAlgAction` on the forms on the larger space of `D.descentPair ϑ j`, the datum of the lift. 

### `range_goodLift_le`

 Let `ϑ` be a tame character and `1 ≤ j ≤ m`. The range of `D.goodLift ϑ j`, the lift
`singleLift` restricted to the good forms on `W_j = D.spaceW j`, is spanned by the lifts of good
eigenforms whose lifts lie in the range of the idempotent of a good tuple family. A good tuple
family `c` is one of the finitely many admissible labellings of the chosen places by polynomials
over their residue fields. `tupleIdem D.RowIndex c` is the tensor product of the idempotents
labelled by these polynomials in the group algebra of the finite groups at the chosen places, which
acts on forms by `groupAlgAction`. A good form is a form of principal level at the chosen places
that lies in the image of `e₀`, the sum of these idempotents over all good tuple families.
Precisely, let a subspace `N` of the forms `FormV` on the larger space of the pair
`D.descentPair ϑ j` contain the lift `singleLift ϑ j y` for every good form `y` in `eigenPart p`
whose lift lies in the range of some `tupleIdem D.RowIndex c`. Here `eigenPart p` is the joint
eigenspace of the Hecke operators for a system `p`. Then `N` contains the range of
`goodLift ϑ j`. 
