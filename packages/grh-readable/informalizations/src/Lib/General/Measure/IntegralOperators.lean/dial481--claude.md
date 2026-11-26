---
{
  "module": "src/Lib/General/Measure/IntegralOperators.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IntegralOperators.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IntegralOperators.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Product measures, layer cake bounds, cocompact subgroups and L² bounds of integral operators

This file rearranges the coordinates of finite powers of a σ-finite measure space, bounds integrals
of negative powers under polynomial volume growth by a layer cake argument, shows that continuous
functions on a group G that are left invariant under a cocompact subgroup Γ are integrable for
finite measures on G, and passes L² bounds of integral operators with measurable, integrable kernels
to finite products. It also contains Tonelli's theorem for finite products, products of cocompact
subgroups, and two small constructions, `New.padTuple` and `New.unitOrOne`.

Among the imported notions in the statements are `Subgroup.FixesLeft Γ F`, meaning `F (γ g) = F g`
for `γ ∈ Γ`, and the following.

* `Subgroup.IsCocompact Γ`: some compact set `C ⊆ G` meets every orbit `Γg`.

## Main definitions and results

* `New.lintegral_rpow_neg_le_of_measure_sublevel_le`: if the sublevel sets `{u ≤ R}` of a measurable
  function `u ≥ 1` have measure at most `(K R^e)^d V`, with `K ≥ 0`, then the integral of `u^(-A)`
  has an explicit bound for `A > e d`. The measure is arbitrary, so the result also bounds sums
  (counting measure). For finite `V`, `New.integrable_rpow_neg_of_measure_sublevel_le` and
  `New.integral_rpow_neg_le_of_measure_sublevel_le` are the forms for the Bochner integral;
  `New.DiscreteSeries.integral_rpow_neg_le_of_measure_le` joins them.
* `New.integrable_of_isCocompact`: continuous left Γ-invariant functions are integrable for finite
  measures on G.
* `New.IsL2Contraction`: a finite family of kernels defines an operator of norm at most one between
  two `L²` spaces, tested on bounded measurable functions. By `New.IsL2Contraction.pi`, the bound
  passes to the product of finitely many such families, for σ-finite measures and measurable kernels
  that are integrable in the last variable.


 ## Regrouping, currying and flipping coordinates of product measures 

### `New.measurePreserving_sigma`

 For a bijection `e` from the disjoint union of the finite types `n i` onto `Y`, the regrouping
map `α^Y → ∏ i, α^(n i)`, `x ↦ (x (e ⟨i, j⟩))_{i, j}`, preserves the product volume measures. 

### `New.measurePreserving_curry`

 Currying, `α^(ι × κ) → (α^κ)^ι`, preserves the product volume measures. 

### `New.measurePreserving_flip`

 Exchanging the two indices, `(α^κ)^ι → (α^ι)^κ`, preserves the product volume measures. 

 ## A layer cake bound for negative powers 

### `New.lintegral_Ioc_rpow_sub_one`

 For an exponent `p > 0`, the Lebesgue integral of `t^(p-1)` over `(0, 1]` is `1/p`. 

### `New.lintegral_rpow_neg_le_of_measure_sublevel_le`

 Layer cake bound for a negative power. Let `u ≥ 1` be measurable and suppose that
`ν {u ≤ R} ≤ (K R^e)^d V` for all `R ≥ 1`, where `K ≥ 0`. If `e d < A` and `A ≤ c (A - e d)`, then
the Lebesgue integral of `u^(-A)` is at most `K^d c V`. 

### `New.integrable_rpow_neg_of_measure_sublevel_le`

 Let `u ≥ 1` be measurable and suppose that `ν {u ≤ R} ≤ (K R^e)^d V` for all `R ≥ 1`, where
`K ≥ 0` and `V` is finite. Then `u^(-A)` is integrable for `A > e d`. 

### `New.integral_rpow_neg_le_of_measure_sublevel_le`

 Let `u ≥ 1` be measurable and suppose that `ν {u ≤ R} ≤ (K R^e)^d V` for all `R ≥ 1`, where
`K ≥ 0` and `V` is finite. If `e d < A` and `A ≤ c (A - e d)`, then `∫ u^(-A) dν ≤ K^d c V`. 

### `New.DiscreteSeries.integral_rpow_neg_le_of_measure_le`

 Let `u ≥ 1` be measurable and suppose that `ν {u ≤ R} ≤ (K R^e)^d V` for all `R ≥ 1`, where
`K ≥ 0` and `V` is finite. If `e d < A` and `A ≤ c (A - e d)`, then `u^(-A)` is integrable and
`∫ u^(-A) dν ≤ K^d c V`. 

 ## Cocompact subgroups 

### `New.integrable_of_isCocompact`

 If the subgroup `Γ` of `G` is cocompact (some compact set meets every orbit `Γg`), then a
continuous function `F : G → ℂ` with `F (γ g) = F g` for `γ ∈ Γ` is integrable for every finite
measure on `G`. 

### `New.isCocompact_prod`

 If `Γ ≤ G` and `Δ ≤ H` are cocompact (some compact set meets every orbit of left
multiplication), then `Γ × Δ` is cocompact in `G × H`. 

 ## Tonelli for products, L² contractions, padded tuples and units 

### `lintegral_pi_prod`

 Tonelli's theorem for a finite product: the integral of `∏ i, f i (x i)` over the product
measure is the product of the integrals, for σ-finite measures and measurable `f i` with values
in `[0, ∞]`. 

### `enorm_toReal_smul_le`

 The bound `‖x.toReal • v‖ₑ ≤ x * ‖v‖ₑ`; for `x = ∞` the left side is `0`. 

### `integrable_toReal_smul`

 Let `φ` be measurable with values in `[0, ∞]` and `F` almost everywhere strongly measurable.
If `∫⁻ φ ‖F‖` is finite, then `φ • F` is integrable (`φ = ∞` is read as `0`). 

### `measurable_integral`

 If `f` is jointly measurable in `(x, y)` and `μ` is s-finite, then `x ↦ ∫ y, f x y ∂μ` is
measurable. 

 ### `L²` bounds of integral operators 

### `IsL2Contraction`

 The finite family of kernels `k i : X → Y → ℂ`, integrated against `μ`, satisfies the bound
`∫ ∑ᵢ |∫ φ(y) kᵢ(x, y) dμ(y)|² dm(x) ≤ ∫ |φ|² dn` for every bounded measurable `φ : Y → ℂ`.
For measurable kernels that are integrable in `y`, this says that the integral operator from
`L²(Y, n)` to `L²(X, m)^I` has norm at most one on bounded functions. 

### `IsL2Contraction.prod`

 Let `k` and `k'` be finite families of measurable kernels, integrable in the last variable
against `μ` and `μ'`, each satisfying `IsL2Contraction`. For `k` this means
`∫ ∑ i, |∫ φ y * k i x y dμ|² dm ≤ ∫ |φ|² dn` for every bounded measurable `φ`. Then, for s-finite
measures, the family of products `k i x y * k' i' x' y'`, indexed by `I × I'`, satisfies the same
bound for the product measures `m.prod m'`, `μ.prod μ'` and `n.prod n'`. 

### `IsL2Contraction.of_comp_equiv`

 The bound `New.IsL2Contraction` is unchanged by renaming the indices of the family and by
measure preserving measurable equivalences in the two variables. 

### `IsL2Contraction.pi_fin`

 The case of `New.IsL2Contraction.pi` in which the factors are indexed by `Fin N`. Suppose that,
for each `j`, the finite family of kernels `k j i : X → Y → ℂ` is jointly measurable, integrable in
`y` against `μ j`, and an L² contraction for the σ-finite measures `m j`, `μ j`, `n j`; an L²
contraction means `∫ ∑ᵢ |∫ φ(y) kᵢ(x, y) dμ(y)|² dm(x) ≤ ∫ |φ|² dn` for every bounded measurable
`φ`. Then the product kernels `(x, y) ↦ ∏ j, k j (i j) (x j) (y j)`, indexed by `i : ∀ j, I j`, form
an L² contraction for `Measure.pi m`, `Measure.pi μ`, `Measure.pi n`. 

### `IsL2Contraction.pi`

 On common spaces `X` and `Y`, let each `k v` be a finite family of measurable kernels,
integrable in the last variable, whose integral operator has `L²` norm at most one
(`New.IsL2Contraction` for σ-finite measures `m v` on `X` and `μ v`, `n v` on `Y`). Then the
same holds for the family of products `∏ v, k v (i v) (x v) (y v)` and the product measures. 

 ### Padded tuples and units 

### `padTuple`

 The sequence indexed by `ℕ` that is the tuple `c` at indices below `n`, `t` at index `n`, and
`1` at indices above `n`. 

### `unitOrOne`

 The element `c` as a unit if it is invertible, and the unit `1` otherwise. 

### `continuousAt_unitOrOne`

 If the units are open in `A` and carry the subspace topology, then `unitOrOne` (an element as a
unit, or `1` if it is not invertible) is continuous at every unit `c`. 
