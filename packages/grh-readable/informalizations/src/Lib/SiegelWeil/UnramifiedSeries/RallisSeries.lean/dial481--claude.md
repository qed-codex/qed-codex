---
{
  "module": "src/Lib/SiegelWeil/UnramifiedSeries/RallisSeries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/UnramifiedSeries/RallisSeries.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/UnramifiedSeries/RallisSeries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The series of translates weighted by the coefficients of the vacuum

This file extends the bound on the coefficients of the vacuum to all sets of places, by induction
over the weights `New.SiegelWeil.stepWeight`. For `2 n < m` it proves that the coefficients are
absolutely summable and that the series `New.SiegelWeil.rallisSeries` converges uniformly. It proves
that the series keeps levels and forms, is multiplicative over the places and is injective. The last
section defines the sum of the coefficients `New.SiegelWeil.vacuumSum` and writes it as a product
over the pairs of conjugate places.

Let `G_f` be the finite adelic unitary group of rank `n` over the CM field `E`, and let `A` be a set
of finite places. The series `∑ mc(γ) R(γ) y` runs over the cosets `γ` of the points integral at
`A`; here `R` is right translation and `mc(γ)` is the coefficient of the vacuum for a second space
of rank `m`, of modulus `[γ L : L ∩ γ L] ^ (-m / 2)` for the standard lattice `L`. In the inner
product formula `A` is the set of the places off the level and its conjugate. For `2 n < m` the
coefficients are absolutely summable, and, if the character in `mc` is unramified on `A`
(`IsUnramifiedOn`: `b ∘ det` is trivial on the integral points supported on `A` and its conjugate),
the series is an injective operator on the bounded functions fixed by the integral points supported
on `A` and its conjugate.

Both facts come from counting lattices through neighbours. A lattice other than `L` is brought
nearer to `L` by a step at a place `w`. The weight `s_w` is the number of steps at `w` times
`q_w ^ (-m / 2)`, where `q_w` is the order of the residue field at `w`. For `2 n < m` it is at most
`1 / (q_w - 1)`, and at most `1 / ((q_w - 1) √q_w)` if `w` is split. If the `s_w` over `A` and its
conjugate add up to `ϱ ≤ 1 / 3`, the nontrivial cosets contribute at most `ϱ + ϱ ^ 2 + ⋯ ≤ 1 / 2`,
so the series is close to the identity. This holds for one place and its conjugate, because
`q_w ≥ 4` (under `WeilData E`, `E` has a primitive root of unity of order `5040`, hence the third
and fourth roots of unity), and for the places outside a finite set, because `∑ s_w` converges. The
series is multiplicative over the places, which gives all `A`. The last section writes the sum of
the coefficients as a product over the pairs of conjugate places.

## Main definitions and results

* `New.SiegelWeil.summable_norm_vacuumCoeff`: the coefficients are absolutely summable.
* `New.SiegelWeil.exists_form_eq_rallisSeries`: the series keeps forms and their levels.
* `New.SiegelWeil.rallisSeries_union`: the series is multiplicative over the places.
* `New.SiegelWeil.eq_zero_of_rallisSeries_eq_zero`: a function with series `0` is `0`.

Notions from other files:
* `localLevel n A`: the points of `G_f` integral at the places of `A`; `stdLevel E n`: the points
  integral at all finite places; `supportedOn n A`: the points with component `1` outside `A` and
  its conjugate, whose union is `A.conjClosure`.
* `HasLevel y K`: right translation by each point of `K` fixes the function `y` on the adelic points
  `G E s`, the products of a point of `GInf E s` (the real points, the only part that depends on the
  signs `s : n → ℤˣ`) and a point of `Gf E n`.
* `New.SiegelWeil.rallisSeries M b A y`: the series `∑ mc(q) R(q) y`, with coefficient
  `New.SiegelWeil.vacuumCoeff M b` and right translation taken at `New.SiegelWeil.cosetRep q`.
* `New.SiegelWeil.stepWeight n M w`: the number of steps at `w` to a neighbouring lattice times
  `q_w ^ (-M / 2)`.
* `New.SiegelWeil.IsUnramifiedOn`: `b ∘ det` is trivial on the integral finite points supported on
  `A` and its conjugate.

## Relation to the literature

Part of a known result: non-vanishing of theta lifts in large rank. See
`Lib.SiegelWeil.RallisInner.SharpData`. The series is the contribution of the unramified places to
Rallis' inner product formula, left as a sum over cosets instead of being evaluated as an L-value;
for the constant `1` in rank one it is evaluated in `New.vacuumSum_eq_L_div_eulerProd`. The count of
lattices uses neighbours in Kneser's sense; see M. Greenberg and J. Voight, Lattice methods for
algebraic modular forms on classical groups (2014), §5.


 ### From few steps to all places 

### `induction_on_stepWeight`

 Induction over sets of places. Let `2 * card n < M`, and let `stepWeight n M w` be the number of
steps at `w` (lines in the `n`-space over the residue field, with a neighbour class) times
`q_w ^ (-M / 2)`. A property `P` of arbitrary (possibly infinite) sets of finite places holds for
all sets if two conditions hold: it holds for every `A` whose weights `stepWeight n M w`, summed
over `A` and its conjugates, add up to at most `1 / 3`; and it passes from `A₁` and `A₂` to
`A₁ ∪ A₂` whenever `A₂` is disjoint from `A₁` and its conjugate. 

 ### Convergence, level and forms 

### `summable_norm_vacuumCoeff`

 For `2 * card n < card m`, consider the numbers `vacuumCoeff (card m) b g = (b(det g) *
finMultiplier g ^ card m)⁻¹`. This is the factor by which `g` changes the vacuum matrix coefficient
when the second space has rank `m`. These numbers are absolutely summable over the representatives
`cosetRep q` of the cosets `q` of `Gf E n` modulo `localLevel n A`, the points integral at `A`. 

### `tendstoUniformly_rallisSeries`

 For `2 * card n < card m` and `y` bounded, the series `rallisSeries` converges uniformly: its
partial sums over finite sets of cosets tend to it uniformly. 

### `norm_rallisSeries_le`

 For `2 * card n < card m` and `y` bounded by `C`, the series `rallisSeries` is bounded by `C`
times the sum of the moduli of the coefficients of the vacuum. 

### `continuous_rallisSeries`

 For `2 * card n < card m` and `y` continuous and bounded, the series `rallisSeries` is
continuous. 

### `rallisSeries_comp_mul_left`

 The series `rallisSeries M b A y` is `∑_q vacuumCoeff M b (cosetRep q) · R(cosetRep q) y`, a sum
of right translates of a function `y` on the adelic points `G E s`. The sum runs over the cosets
`q`, in the finite points, of the subgroup of points integral at `A`, with representatives supported
on `A` and its conjugate. The series commutes with left translations with no convergence hypothesis:
applied to `g' ↦ y (x * g')` and evaluated at `g`, it equals `rallisSeries M b A y` at `x * g`. 

### `rallisSeries_comp_mul_right`

 For a natural number `M`, a character `b : AutChar E` and a set `A` of finite places,
`rallisSeries M b A y` is the series `∑ mc(q) R(q) y` of right translates of `y`. The sum runs over
the cosets `q` of the subgroup of finite points integral at `A`, and the coefficient
`vacuumCoeff M b` and the right translation are taken at the representative `cosetRep q`. The series
commutes with right translation: if the finite part `x.2` of `x` has component `1` at every place of
`A`, then the series of `g' ↦ y (g' * x)` at `g` equals the series of `y` at `g * x`. 

### `rallisSeries_mul_of_mem_localLevel`

 Let `b ∘ det` be trivial on the integral points supported on `A` and its conjugate, and let `y`
be fixed by these points. A finite point `k` integral at `A` that fixes `y` also fixes
`rallisSeries M b A y`, the series of translates of `y` weighted by the coefficients of the
vacuum. 

### `hasLevel_rallisSeries`

 The series `rallisSeries M b A y` (the sum over cosets `q` of the points integral at `A` of the
right translates `R(cosetRep q) y`, weighted by `vacuumCoeff M b (cosetRep q)`) keeps the level. Let
`b ∘ det` be trivial on the integral points supported on `A` and its conjugate (`IsUnramifiedOn`).
Let the subgroup `J` of the finite points contain those points and lie in `localLevel n A`, the
points integral with integral inverse at each place of `A`; then if `y` is right invariant under
`J`, so is `rallisSeries M b A y`. 

### `hasSum_integral_mul_rallisSeries`

 The series `rallisSeries` may be integrated term by term. Let `2 * card n < card m`, let `y` be
bounded and measurable, `f` integrable and `j` measurable. The integral of `f z` times the series
at `j z` is the sum over the cosets `q` of the coefficient of the vacuum at `u = cosetRep q` times
the integral of `f z * y (j z * u)`. 

### `realConv_rallisSeries`

 For `2 * card n < card m` and `y` bounded and measurable, the series `rallisSeries` commutes
with `realConv κ`, the right convolution by an integrable function `κ` on the real points. 

### `hasSum_petersson_rallisSeries`

 The Petersson product with the series `rallisSeries` may be taken term by term. Let `S` be a
hermitian space of rank `card n` over `E` with signs `s` and adelic points `G E s`, and let
`⟨y', z⟩ = S.petersson y' z` be the integral of `conj (y' g) * z g` against `S.quotMeasure`, the
measure that computes integrals over the quotient by the rational points of `S`. Let
`2 * card n < card m`, let `y` be bounded and strongly measurable, let `y'` be integrable for this
measure, let `x` be an adelic point, and write `R(x) z` for the translate `g ↦ z (g * x)`.
Let `q` run over the cosets of `localLevel n A`, the finite points integral at `A`, with
representatives `u = cosetRep q`. Then the numbers `vacuumCoeff (card m) b u * ⟨y', R(x u) y⟩`,
where `vacuumCoeff M b u = (b(det u) * finMultiplier u ^ M)⁻¹`, have sum `⟨y', R(x) z⟩` for the
series `z = rallisSeries (card m) b A y = ∑ vacuumCoeff (card m) b u * R(u) y`. 

### `isAutomorphic_rallisSeries`

 Let `2 * card n < card m` and let `b ∘ det` be trivial on the integral points supported on `A`
and its conjugate (`IsUnramifiedOn`). The series `rallisSeries` of a bounded automorphic function
fixed by these points is automorphic: continuous, invariant on the left by the rational points of
`S` and fixed by an open subgroup of the finite points. 

### `isForm_rallisSeries`

 The series `rallisSeries (card m) b A y` is the sum, over the cosets `q` of the finite points
modulo those integral at `A`, of the right translates of `y` by a representative of `q`, each
weighted by the vacuum coefficient `vacuumCoeff (card m) b`; it keeps the forms of each type. Let
`2 * card n < card m` and let `b ∘ det` be unramified on `A`. Let `y` be a form of type `e` for the
hermitian space `S`, meaning it is automorphic, bounded and, if `e` is integrable, fixed by
convolution with `e` over the real points, and let it be right invariant under the integral points
supported on `A` and its conjugate. Then `rallisSeries (card m) b A y` is a form of type `e` for
`S`. 

### `exists_form_eq_rallisSeries`

 The series `rallisSeries (card m) b A` keeps the forms of each type and level for a hermitian
space `S : Space E n s`. This series is `∑ mc(q) R(q) y`, summed over the cosets `q` of the finite
points integral at `A`, with coefficient `vacuumCoeff (card m) b` and right translation taken at
`cosetRep q`. Let `2 * card n < card m`, let `b ∘ det` be unramified on `A`, and let `J` consist of
points integral at `A` and contain the integral points supported on `A` and its conjugate; then the
series of a form `y` of type `e` for `S` (automorphic, bounded and, if `e` is integrable, fixed by
convolution with `e`) that is fixed by `J` is again a form of type `e` for `S` fixed by `J`. 

 ### Injectivity 

### `rallisSeries_union`

 The series is multiplicative over the places. Let `2 * card n < card m`, let `A₂` be disjoint
from `A₁` and its conjugate, let `b ∘ det` be unramified on `A₁ ∪ A₂`, and let `y` be bounded and
fixed by the integral points supported on `A₁ ∪ A₂` and its conjugate. The series of `y` at
`A₁ ∪ A₂` is the series at `A₁` of the series of `y` at `A₂`. 

### `tsum_compl_one_norm_vacuumCoeff_le`

 Let `2 * card n < card m` and let `A` be a set of finite places. The weight
`stepWeight n (card m) w` is the number of neighbour steps at `w` times `q_w ^ (-card m / 2)`, where
`q_w` is the order of the residue field at `w`. Suppose the weights over the places of `A` and their
conjugates add up to at most `1 / 3`. Let `q` run over the cosets other than that of `1` of
`localLevel n A`, the points integral at `A`, in the finite adelic unitary group `Gf E n`. Then the
moduli of the coefficients `vacuumCoeff (card m) b u = (b(det u) * finMultiplier u ^ card m)⁻¹` at
the representatives `u = cosetRep q` add up to at most `1 / 2`. 

### `eq_zero_of_rallisSeries_eq_zero_of_tsum_le`

 The series `rallisSeries (card m) b A y` is the sum, over the cosets `q` of the finite points
modulo those integral at `A`, of the right translates of `y` by a representative of `q`, each
weighted by the vacuum coefficient `vacuumCoeff (card m) b`. This series is injective where it is
close to the identity. Let `2 * card n < card m`, let `b ∘ det` be unramified on `A`, and let the
sum of the weights `stepWeight` over the places `w` of `A` and its conjugate be at most `1 / 3`;
here `stepWeight` is the number of neighbour steps at `w` times `q_w ^ (-card m / 2)`. Then a
bounded function `y` on `G E s` that is right invariant under the integral points supported on `A`
and its conjugate, and whose series is `0`, is itself `0`. 

### `hasLevel_rallisSeries_of_disjoint`

 Let `A₂` be disjoint from `A₁` and its conjugate, and let `y` be fixed by the integral
points supported on `A₁` and its conjugate. These points also fix the series of `y` at `A₂`. 

### `eq_zero_of_rallisSeries_eq_zero`

 Let `2 * card n < card m` and let `b ∘ det` be unramified on `A`. A bounded function fixed by
the integral points supported on `A` and its conjugate whose series `rallisSeries`, the sum of its
translates weighted by the coefficients of the vacuum, is `0` is itself `0`. 

 ### The sum of the coefficients as a product over the places 

### `vacuumSum`

 The sum `∑ mc(q)` of the coefficients of the vacuum `mc = vacuumCoeff M b` over the cosets `q`,
in the finite points, of the subgroup of the points integral at `A`, taken at the representatives
`cosetRep q`. It is the value of the series of the constant function `1` (`rallisSeries_const`),
and it is `0` if the terms are not summable. 

### `rallisSeries_const`

 Translations fix a constant function, so its series is the constant times the sum of the
coefficients of the vacuum. 

### `vacuumCoeff_cosetRep_mk`

 Let `b ∘ det` be unramified on `A`. The coefficient of the vacuum at the chosen representative
of the coset of a point `u` supported on `A` and its conjugate is the coefficient at `u`. 

### `vacuumSum_eq_tsum`

 Let `b ∘ det` be unramified on `A`. The sum `vacuumSum` may be computed with any points `r γ`
that are supported on `A` and its conjugate and represent the cosets of the points integral at
`A`. 

### `vacuumSum_empty`

 Over the empty set of places there is one coset, and the sum `vacuumSum` is `1`. 

### `vacuumSum_union`

 The sum `vacuumSum` is multiplicative over the places. Let `2 * card n < card m`, let `A₂` be
disjoint from `A₁` and its conjugate, and let `b ∘ det` be unramified on `A₁ ∪ A₂`. The sum at
`A₁ ∪ A₂` is the product of the sums at `A₁` and at `A₂`. 

### `tendsto_vacuumSum_inter`

 Let `2 * card n < card m`, and let `b ∘ det` be trivial on the integral finite points supported
on `A` and its conjugate (`IsUnramifiedOn`). Let `vacuumSum n (card m) b A` be the sum, over the
cosets `q` in the finite adelic unitary group `Gf E n` of the points integral at `A`, of the vacuum
coefficients `(b(det g) * finMultiplier g ^ card m)⁻¹` at the representatives `g = cosetRep q` (and
`0` if the sum is not summable). Then, as the finite set `R` of places grows, `vacuumSum` at `A ∩ R`
tends to `vacuumSum` at `A`. 

### `vacuumSum_eq_of_hasProd`

 Let `vacuumSum n (card m) b A` be the sum, over the cosets `q` in `Gf E n` of the points
integral at `A`, of the vacuum coefficients `(b(det g) * finMultiplier g ^ card m)⁻¹` at
`g = cosetRep q`. It is a product over the pairs of conjugate places: let `2 * card n < card m`, let
`A` be stable under conjugation, and let `b ∘ det` be unramified on `A`; let the factors `loc w` be
`1` off `A` and have product `L`. If for each `w` in `A` the sum at `{w, w̄}` is `loc w * loc w̄` (a
single factor when `w = w̄`), then the sum at `A` is `L`. 
