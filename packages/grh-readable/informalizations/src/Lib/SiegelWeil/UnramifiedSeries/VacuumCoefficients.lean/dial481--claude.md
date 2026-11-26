---
{
  "module": "src/Lib/SiegelWeil/UnramifiedSeries/VacuumCoefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/UnramifiedSeries/VacuumCoefficients.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/UnramifiedSeries/VacuumCoefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vacuum coefficients, coset representatives and the weight of steps through neighbours

This file defines the coefficients of the vacuum `New.SiegelWeil.vacuumCoeff`, the representatives
`New.SiegelWeil.cosetRep` of the cosets of `localLevel n A` and the series
`New.SiegelWeil.rallisSeries`. It shows that the coefficients and the cosets are multiplicative over
two sets of places with disjoint supports. It bounds sums along a walk (`New.tsum_le_of_walk`) and
shows that every residue field has at least four elements if `E` contains a primitive root of unity
of order `5040` (`New.FinPlace.four_le_q`). It defines the weight `New.SiegelWeil.stepWeight` of the
steps at a place to a neighbouring lattice and bounds it for `2 * card n < M`. If these weights over
`A` and its conjugate add up to at most `1 / 3`, it bounds the sum of the moduli of the coefficients
(`New.SiegelWeil.tsum_ofReal_norm_vacuumCoeff_le`).

## Main definitions and results

* `New.SiegelWeil.vacuumCoeff`, `New.SiegelWeil.cosetRep`, `New.SiegelWeil.rallisSeries`: the
  coefficients, the representatives of the cosets and the series.
* `New.SiegelWeil.stepWeight`: the number `stepWeight n M w`, with the bounds
  `New.SiegelWeil.tsum_stepWeight_conjClosure_singleton_le` and
  `New.SiegelWeil.summable_stepWeight`.

Notions from other files:
* `localLevel n A`: the points of `Gf E n` integral at the places of `A`; `stdLevel E n`: the points
  integral at all finite places.
* `supportedOn n A`: the points with component `1` outside `A` and its conjugate, whose union is
  `A.conjClosure`; `trivialOn n A`: the points with component `1` at `A`.
* `finMultiplier`: the multiplier of a finite point; its squared modulus is the index
  `[L : L ∩ γ⁻¹ L] = [γ L : L ∩ γ L]` at the point `γ`.
* `AutChar E`: the characters `b` of the norm-one adeles of `E` trivial on the norm-one elements of
  `E`; `detFin 1 g`: the determinant of the finite point `g`, as such an adele with component `1` at
  the infinite places.
* `HasLevel y K`: right translation by each point of `K` fixes the function `y` on the adelic points
  `G E s`, the products of a point of `GInf E s` (the real points, the only part that depends on the
  signs `s : n → ℤˣ`) and a point of `Gf E n`.

## Relation to the literature

Known; see `Lib.SiegelWeil.UnramifiedSeries.RallisSeries` for sources.


 ### Vacuum coefficients and coset representatives 

### `finMultiplier_mul_mul_of_mem_stdLevel`

 For `g` in the finite adelic unitary group, the multiplier `finMultiplier g` is the
`glMultiplier` of its underlying matrix in GL_n(𝔸_f). It is unchanged by multiplying `g` on either
side by integral finite points: `finMultiplier (k * g * k') = finMultiplier g` for all `k, k'` in
`stdLevel E n` = G_f ∩ GL_n(Ô). 

### `finMultiplier_mul_of_forall_atPlace_eq_one_or`

 The multiplier of a product of two finite points of which, at each place, one has component
`1` is the product of their multipliers. 

### `vacuumCoeff`

 The number `(b(det g) * finMultiplier g ^ M)⁻¹` for a finite point `g`. For `M` the rank of
the second hermitian space of a pair it is the factor by which `g` changes the matrix coefficient
of a vacuum (`New.SiegelWeil.weilMatrixCoeff_mul`). 

### `cosetRep`

 For a coset `γ` of `localLevel n A`, the finite points integral at `A`, the component above
`A` and its conjugate of a chosen element of `γ`. It represents `γ` (`mk_cosetRep`) and is
supported on `A` and its conjugate. 

### `IsUnramifiedOn`

 The character `b ∘ det` is trivial on `stdLevel E n ⊓ supportedOn n A`, the integral finite
points whose component is `1` at every place outside `A` and its conjugate. 

### `_root_.New.AutChar.HasWeight.isUnramifiedOn`

 If `b` has weight `γ` at the infinite places and a tame part `ψ` (the characters of the residue
fields through which `b` acts on integral units) that is trivial at `A` and its conjugate, then
`b ∘ det` is trivial on the integral finite points supported there. 

### `vacuumCoeff_mul_mul_of_mem`

 Let `b ∘ det` be trivial on the integral points supported on `A` and its conjugate. The
coefficient of the vacuum is invariant on both sides under these points. 

### `vacuumCoeff_eq_one_of_mem`

 Let `b ∘ det` be trivial on the integral finite points whose component is `1` outside `A` and
its conjugate (`IsUnramifiedOn`). Then for every `M : ℕ`, the coefficient of the vacuum `vacuumCoeff
M b k = (b(det k) · finMultiplier k ^ M)⁻¹` equals `1` at each such point `k`. 

### `vacuumCoeff_mul_of_atPlace`

 The coefficient of the vacuum is multiplicative on two finite points of which, at each place,
one has component `1`. 

### `rallisSeries`

 The series `∑ mc(q) R(q) y` of right translates of a function `y` on the adelic points. The sum
is over the cosets `q`, in the finite points, of the subgroup of the points integral at `A`. The
coefficient of the vacuum `mc = vacuumCoeff M b` and the right translation `R` are taken at the
representative `cosetRep q`, which is supported on `A` and its conjugate; see
`mk_eq_mk_iff_of_supportedOn` for the cosets among such points and
`vacuumCoeff_mul_apply_cosetRep` for conditions under which the choice does not matter. The value
is `0` where the terms are not summable. 

### `mk_eq_mk_iff_of_supportedOn`

 Two finite points supported on `A` and its conjugate lie in the same coset of the points
integral at `A` exactly when they lie in the same coset of the integral points with such support. 

### `inv_mul_cosetRep_mem`

 The chosen representative of the coset of a point `u` supported on `A` and its conjugate differs
from `u` on the right by an integral point with such support. 

### `vacuumCoeff_mul_apply_cosetRep`

 The terms of `rallisSeries` do not depend on the representatives. Let `b ∘ det` be trivial on
the integral points supported on `A` and its conjugate, and let `y` be fixed by these points. The
term of the coset of a point `u` supported on `A` and its conjugate may be computed at `u`. 

### `norm_vacuumCoeff`

 The modulus of the coefficient of the vacuum at `g` is `‖finMultiplier g‖ ^ (-M)`; it does not
depend on the character. 

### `finMultiplier_cosetRep_mk`

 The multiplier of the chosen representative of the coset of a point `u` supported on `A` and its
conjugate is the multiplier of `u`. 

### `norm_vacuumCoeff_cosetRep_one`

 The coefficient of the vacuum has modulus `1` on the trivial coset. 

 ### Sums bounded by a walk 

### `_root_.New.tsum_ite_lt_succ_le_of_walk`

 One stage of summation along a walk. Suppose that each point `x ≠ x₀` has a step `σ` that lowers
its height and satisfies `f x ≤ c σ * f (step σ x)`, and that each step is injective. Then the sum
of `f` over the points of height below `N + 1` is at most `f x₀` plus `∑ c` times the sum over the
points of height below `N`. 

### `_root_.New.tsum_le_of_walk`

 Summation along a walk. Suppose that each point `x ≠ x₀` has a step `σ` that lowers its height
and satisfies `f x ≤ c σ * f (step σ x)`, and that each step is injective. Then `∑ f ≤ B` for
every `B` with `f x₀ + (∑ c) * B ≤ B`, such as `f x₀` times the geometric series of ratio `∑ c`. 

 ### Two sets of places with disjoint supports 

### `supportedOn_le_trivialOn_right`

 If `A₂` is disjoint from `A₁` and its conjugate, the points supported on `A₁` and its conjugate
are trivial at `A₂`. 

### `supportedOn_le_trivialOn_left`

 If `A₂` is disjoint from `A₁` and its conjugate, the points supported on `A₂` and its conjugate
are trivial at `A₁`. 

### `mk_mul_eq_mk_iff`

 Let `A₂` be disjoint from `A₁` and its conjugate, and let `u₁`, `u₂` be supported on `A₁`, `A₂`
and their conjugates. Then `u₁ * u₂` represents the coset of `g` at `A₁ ∪ A₂` exactly when `u₁`
represents it at `A₁` and `u₂` represents it at `A₂`. 

### `bijective_mk_cosetRep_mul`

 Let `A₂` be disjoint from `A₁` and its conjugate. The cosets at `A₁ ∪ A₂` are the products of a
coset at `A₁` and a coset at `A₂`. 

### `vacuumCoeff_mul_of_disjoint`

 For `M : ℕ` and a character `b`, `vacuumCoeff M b g = (b(det g) · finMultiplier g ^ M)⁻¹` is the
factor by which a finite point `g` changes the matrix coefficient of a vacuum when `M` is the rank
of the second hermitian space. If `A₂` is disjoint from `A₁` and its conjugate, then `vacuumCoeff M
b (u₁ * u₂) = vacuumCoeff M b u₁ * vacuumCoeff M b u₂`. This holds whenever `u₁` is a finite point
supported on `A₁` and its conjugate, and `u₂` is one supported on `A₂` and its conjugate; supported
means having component `1` at every other place. 

### `summable_norm_vacuumCoeff_union`

 Let `A₂` be disjoint from `A₁` and its conjugate. If the coefficients of the vacuum are
absolutely summable over the cosets at `A₁` and at `A₂`, they are so over the cosets at
`A₁ ∪ A₂`. 

 ### The number of steps at a place 

### `_root_.New.FinPlace.four_le_q`

 If the CM field `E` contains a primitive root of unity of order `5040`, hence the third and
fourth roots of unity, the order `w.q` of the residue field at a finite place `w` is at least
`4`. 

### `NeighbourStep`

 The steps at `w` from a lattice to a neighbour: a line in the `n`-space over the residue field
and one of the classes in `neighbourResidues w`, which tell apart the neighbours that belong to the
same line. 

### `stepWeight`

 The number of steps at `w` (see `NeighbourStep`) times `q_w ^ (-M / 2)`, where `q_w = w.q` is
the order of the residue field at `w`. A step at `w` towards the standard lattice multiplies the
modulus of the coefficient of the vacuum `vacuumCoeff M b` by at least `q_w ^ (M / 2)`. 

### `stepWeight_le_card_div`

 For `2 n < M` the weight of the steps at `w` is at most the number of classes in
`neighbourResidues w` divided by `(q_w - 1) √q_w`: there are at most `q_w ^ n / (q_w - 1)` lines. 

### `stepWeight_le_of_isSplit`

 For `2 n < M` and `w` split, that is, different from its conjugate, the weight of the steps at
`w` is at most `1 / ((q_w - 1) √q_w)`. 

### `stepWeight_le`

 For `2 n < M` the weight of the steps at any place `w` is at most `1 / (q_w - 1)`, where
`q_w` is the order of the residue field at `w`. 

### `tsum_stepWeight_conjClosure_singleton_le`

 For `2 n < M` the weights `stepWeight n M` of the steps at a place `w` and its conjugate add up
to at most `1 / 3`, since every residue field of `E` has at least four elements. 

### `stepWeight_le_two_mul_rpow_of_isSplit`

 For `2 n < M` and `w` split the weight of the steps at `w` is at most `2 q_w ^ (-3 / 2)`. 

### `stepWeight_le_two_mul_inv_minFac_sq`

 For `2 n < M` and `w` not split the weight of the steps at `w` is at most `2 / p ^ 2`, where
`p` is the least prime factor of `q_w`: the residue field at such a place is not of prime order. 

### `summable_stepWeight`

 For `2 n < M` the weights of the steps are summable over all finite places. 

 ### The walk through neighbours 

### `exists_steps_q_mul_norm_finMultiplier_le`

 One step of the walk through neighbours. For every set `A` of finite places there are elements
`ρ σ` of the finite adelic unitary group `Gf E n`, one for each step `σ` (a line in the `n`-space
over the residue field at `w` and a neighbour class) at a place `w` of `A` or its conjugate, with
the following property. Every nontrivial coset `q` of `localLevel n A` (the points integral at `A`)
has a step `σ` at some `w` such that
`q_w * ‖finMultiplier (cosetRep (ρ σ • q))‖ ^ 2 ≤ ‖finMultiplier (cosetRep q)‖ ^ 2`. Here
`finMultiplier` is the multiplier Δ_f (`glMultiplier` of the underlying matrix). 

### `norm_vacuumCoeff_le_of_mul_sq_le`

 If `r > 0` and `r * ‖finMultiplier g'‖ ^ 2 ≤ ‖finMultiplier g‖ ^ 2`, then the coefficient of
the vacuum at `g` is at most `r ^ (-M / 2)` times the one at `g'` in modulus. 

### `tsum_ofReal_norm_vacuumCoeff_le`

 The weight `stepWeight n M w` is the number of steps at `w` (a line in the `n`-space over the
residue field, together with a neighbour class) times `q_w ^ (-M / 2)`. If these weights, over the
places of `A` and their conjugates, add up to at most `1 / 3`, then the moduli of the vacuum
coefficients `vacuumCoeff M b g = (b(det g) * finMultiplier g ^ M)⁻¹` add up to at most
`1 / (1 - 1 / 3) = 3 / 2`, where `g = cosetRep q` runs over the representatives of the cosets `q` of
`localLevel n A` (the points integral at `A`) in the finite adelic unitary group `Gf E n`. 
