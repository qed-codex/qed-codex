---
{
  "module": "src/Lib/Weil/DualPair/TwoEdges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/TwoEdges.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/TwoEdges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Two edges V → V′ → V″ joined into one datum of the pair (V′, V⁻ ⊕ V″)

This file joins data on two consecutive edges V → V′ → V″ into one datum of the pair
(V′, V⁻ ⊕ V″), where V⁻ ⊕ V″ is `New.Seesaw.flipSum`. A datum on `Hom(V, V′)` is carried by the
adjoint to `Hom(V′, V⁻)` and multiplied with a datum on `Hom(V′, V″)`. The joining map is
compatible with the theta functional `New.Space.θ`, with translations and with the Weil actions,
which become `New.Seesaw.tripleWeil`. On the finite parts `New.Space.finitePart`, the spans of the
finite translates of the vacuum, it induces an injective map from the tensor product onto the
finite part.

## Main definitions and results

* `New.Seesaw.arrowProduct`: for two consecutive edges V → V′ → V″, the bounded bilinear map that
  joins data on Hom(V, V′) and Hom(V′, V″) into one datum of the pair (V′, V⁻ ⊕ V″). It is
  compatible with the theta functional up to a nonzero constant (`New.Seesaw.theta_arrowProduct`)
  and with the Weil actions (`New.Seesaw.arrowProduct_twistedPairWeil`).
* `New.Seesaw.homHeisenbergOp_arrowProduct`, `New.Seesaw.finHeisenbergOp_arrowProduct`: the
  joining map is compatible with translations.
* `New.Seesaw.arrowTensor`: the induced map on the tensor product of the finite parts. It is
  injective (`New.Seesaw.injective_arrowTensor`), with a left inverse
  (`New.Seesaw.leftInverse_arrowTensor`), and its range is the finite part
  (`New.Seesaw.range_arrowTensor`).
* `New.Seesaw.theta_tripleWeil_rat_mul`: `θ` of `New.Seesaw.tripleWeil` is invariant under rational
  points in the first two groups.

Notions from other files:
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄; its restriction to the norm-one ideles is
  `New.WeilData.upsilonU1`.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.pairWeil`: The action ω_{a,b}(g, h) = χ_{a,b}(g, h) ω(x ↦ hxg⁻¹) on 𝒮(Hom(S, T)), where
  χ_{a,b}(g, h) = a(det h) b(det g)⁻¹ is `New.pairChar`. The theta kernel `New.pairTheta` S T a b f
  (g, h) is θ(ω_{a,b}(g, h) f), where θ is the theta functional `New.Space.θ`.
* `New.Seesaw.flipSpace` (in `Lib.Weil.DualPair.Flip`): the opposite space V⁻ of V, with matrix −J
  and the opposite signs.

## Relation to the literature

Known; see `Lib.Weil.DualPair.ThetaLiftConvergence` for sources.


### `flipSum`

 For hermitian spaces V and V'', the orthogonal sum V⁻ ⊕ V'' of the opposite space
V⁻ = `New.Seesaw.flipSpace V` and V''. 

### `arrowProduct`

 The bounded bilinear map combining data on Hom(V,V') and Hom(V',V'') into one datum on
Hom(V', V⁻ ⊕ V''), the first being carried to Hom(V', V⁻) by a scaled adjoint. 

### `tripleWeil`

 For g = (g₁,g₂,g₃), the Weil operator of (g₂, g₁ ⊕ g₃) on Hom(V', V⁻ ⊕ V''), times the product
of `pairChar` for `rankTwist a` at (g₁,g₂), `pairChar` for `rankTwist b` at (g₂,g₃) and `pairChar`
for (υ^{rk V'}, υ^{rk V}) at (g₂,g₁). 

### `arrowTensor`

 The linear map induced by `New.Seesaw.arrowProduct` from the tensor product of the finite parts
𝒮_f of Hom(V,V') and Hom(V',V'') to the data on Hom(V', V⁻ ⊕ V''). 

### `liftWeilFin`

 The Weil representation of the finite adelic U(V) × U(V') on finite data for Hom(V,V'),
normalised by the characters `rankTwist a` for the ranks of V and V'. 

### `arrowProduct_apply`

 `New.Seesaw.arrowProduct` applied: the product of the flip of f with f'. 

### `matrixToVec_fromRows_comp_inl`

 The entries of a block matrix `fromRows A B` over the first block of rows are those of A. 

### `matrixToVec_fromRows_comp_inr`

 The entries of a block matrix `fromRows A B` over the second block of rows are those of B. 

 ### Compatibility of the joining map with `θ`, translations and the Weil action 

### `theta_arrowProduct`

 There is a constant `z ≠ 0` such that the theta functional of the joined datum
`New.Seesaw.arrowProduct f f'` is `z` times the product of the theta functionals of `f` and `f'`. 

### `homHeisenbergOp_arrowProduct`

 Translating the joined datum by the block matrix with rows `w*` (the adjoint of `w`) and `w'`
is the same as translating `f` by `w` and `f'` by `w'` before joining. 

### `finHeisenbergOp_arrowProduct`

 The finite Heisenberg operator of `y` on the joined datum acts on `f'` by the second block of
`y` and on `f` by `normNegOne` (the fixed unit u of Ô with ūu = −1) times the conjugate transpose of
the first block. The scalar is `stdLattice.semichar` of the first block, squared. 

### `arrowProduct_twistedPairWeil`

 Acting on `f` by `(g, g')` and on `f'` by `(g', g'')` and then joining is the same as joining
and then acting by `New.Seesaw.tripleWeil` at `(g, g', g'')`. 

 ### The joining map on finite parts 

### `eq_zero_of_forall_theta_rho_eq_zero`

 The point evaluations separate the finite part: a vector u of the finite part of the data on
Hom(V, V′) with θ(ϱ(x) u) = 0 for every point x is zero. 

### `injective_arrowTensor`

 The induced map `New.Seesaw.arrowTensor` on the tensor product of the finite parts is
injective. 

### `range_arrowTensor`

 The range of `arrowTensor`, the linear map induced by `arrowProduct` from 𝒮_f(Hom(V,
V')) ⊗ 𝒮_f(Hom(V', V'')) to 𝒮(Hom(V', V⁻ ⊕ V'')), is exactly the finite part 𝒮_f of the target. Here
V⁻ ⊕ V'' = `flipSum V V''`, with V⁻ the opposite space of V. 

### `arrowTensor_map_liftWeilFin`

 `New.Seesaw.arrowTensor` intertwines the normalised Weil representations
`New.Seesaw.liftWeilFin` of finite adelic points on the two factors with `New.Seesaw.tripleWeil`
at the same points, for characters `a` and `b`. 

### `theta_tripleWeil_mul_mul_eq_of_mem_Gamma`

 The theta functional of `tripleWeil a b (g, g', k) f` is unchanged when `g` is multiplied on the
left by a rational point `γ` of `U(V)` and `g'` by a rational point `δ` of `U(V')`. 

### `theta_tripleWeil_rat_mul`

 The function `F x = θ (tripleWeil a b x f)` of a triple of adelic points is unchanged when the
first point is multiplied on the left by a rational point `γ` of `U(V)` and the second by a rational
point `δ` of `U(V')`. 
