---
{
  "module": "Zeta23/PairCeiling/Stability.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Stability.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/Stability.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/Stability.lean — the analytic half of the bandwidth-1 pair-correlation ceiling theorem:
the configuration-free Abel/integration-by-parts identities and the stability bound.
For weights s at the grid j/N (Defs: Csum, Cstep, Dfun, Efun) and a weight r with r′ = g continuous on [0,1]:
  (A)  ∫₀¹ g·C = C_N·r(1) − Σ_{j=1}^{N} s_j r(j/N)                                  [cellwise FTC + Abel summation]
  (1)  Σ_j s_j r(j/N) − ∫₀¹ r(x)·x dx = r(1)·D(1) − ∫₀¹ g·D                           [first-order identity]
and, if g is differentiable off a finite set with derivative h, h integrable, (E continuous, E′ = D off the grid):
  (2)  … = r(1)·D(1) − g(1)·E(1) + ∫₀¹ h·E                                            [second-order identity]
  (B)  |…| ≤ |r 1|·|D 1| + |g 1|·|E 1| + M·∫₀¹|h|   whenever |E| ≤ M on [0,1].         [ceiling stability]
No sign condition on s. Standard axioms.
-/
```

 ### 0. cell bookkeeping 

### `Cstep_ae_cell`

 a.e. on the cell (for the interval-integral measure), C = C_m. 

### `intervalIntegrable_gC_cell`

 g·C is interval-integrable on each cell when g is continuous there. 

 ### 1. (A): ∫₀¹ g·C via cells and Abel summation 

### `integral_cell`

 one cell: ∫ g·C = C_m (r(b) − r(a)). 

### `integral_gC_eq_sum`

 (A) summed: ∫₀¹ g·C = Σ_{m<N} C_m (r((m+1)/N) − r(m/N)). 

### `abel`

 Abel summation: Σ_{m<N} C_m (r_{m+1} − r_m) = C_N r(1) − Σ_{j=1}^{N} s_j r(j/N). 

### `integral_gC`

 (A): ∫₀¹ g·C = C_N r(1) − Σ_j s_j r(j/N). 

### `intervalIntegrable_gC`

 integrability of g·C on [0,1] (from the cells). 

 ### 2. first-order identity 

### `integral_r_mul_id`

 ∫₀¹ r(x)·x dx = r(1)/2 − ∫₀¹ g(x)·(x²/2) dx. 

### `abel_ibp_first`

 **(1) FIRST-ORDER IDENTITY.** Σ_{j=1}^N s_j r(j/N) − ∫₀¹ r(x)x dx = r(1)·D(1) − ∫₀¹ g·D. 

 ### 3. first-order bound 

### `first_order_bound`

 |Σ s_j r(j/N) − ∫₀¹ r x·x| ≤ |r 1|·|D 1| + M₁·∫₀¹|g| whenever |D| ≤ M₁ on [0,1]. 

 ### 4. E is continuous, and E′ = D off the grid 

### `grid`

 the grid {m/N : m ∈ ℕ}. 

### `measurable_Cstep`

 Cstep is measurable (a finite sum of scaled indicators). 

### `intervalIntegrable_Dfun`

 D is interval-integrable on [0,1]. 

### `continuousOn_Efun`

 E is continuous on [0,1]. 

### `exists_cell`

 off the grid, a point of (0,1) sits in an open cell (m/N, (m+1)/N) with m < N. 

### `Dfun_eqOn_cell`

 on an open cell D agrees with the continuous function C_m − t²/2. 

### `continuousAt_Dfun`

 D is continuous at every non-grid point of (0,1). 

### `hasDerivAt_Efun`

 E′ = D off the grid. 

 ### 5. second-order identity and the ceiling-stability bound 

### `abel_ibp_second`

 **(2) SECOND-ORDER IDENTITY.** If additionally g is differentiable off a countable set T ⊆ ℝ with derivative h,
h interval-integrable on [0,1]:  Σ s_j r(j/N) − ∫₀¹ r x·x = r(1)·D(1) − g(1)·E(1) + ∫₀¹ h·E. 

### `ceiling_stability`

 **CEILING STABILITY (L1).** With |E| ≤ M on [0,1]:
  |Σ_{j=1}^{N} s_j r(j/N) − ∫₀¹ r(x)x dx| ≤ |r 1|·|D 1| + |g 1|·|E 1| + M·∫₀¹|h|. 
