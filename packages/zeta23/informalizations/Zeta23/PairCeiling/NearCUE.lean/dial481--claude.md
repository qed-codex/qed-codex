---
{
  "module": "Zeta23/PairCeiling/NearCUE.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/NearCUE.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PairCeiling/NearCUE.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/PairCeiling/NearCUE.lean — the stability constants for grid laws whose pair rows are those of the sine process up to τ.

If the grid form factor S : ℕ → ℝ (atom masses s_j = S(j)/N at j/N) satisfies |N·S(j) − j| ≤ τ for 0 < j < N — the closed-band
row S(N) being free — then the integrated discrepancy E = ∫₀ˣ D of Defs.lean obeys, on all of [0,1],
      |E(x)| ≤ 1/(6N²) + τ/(2N),
in particular |E(1)| ≤ 1/(6N²) + τ/(2N); the free row enters only D(1) = Σ_j s_j − 1/2.  (Exact computation on each cell
[m/N, (m+1)/N]: with N·x = m + θ,  N³·E(x) = (−m + 3mθ(1−θ) − θ³)/6 + (perturbation of size ≤ m(m+1)τ/2), and
−(m+1) ≤ −m + 3mθ(1−θ) − θ³ ≤ 0.)  Consequently THEOREM 1′ (Stability.lean) holds for every such law with the constants
e₁ = M = 1/(6N²) + τ/(2N):  v ≤ p + d₁·|r(1)| + (1/(6N²) + τ/(2N))·(|r′(1)| + ∫₀¹|r″|)  for every certificate (c₀, r) with
c₀ + Σ_j s_j r(j/N) ≤ p and |D(1)| ≤ d₁.
-/
```

 ## 1. The row hypothesis propagated to the partial sums T and U 

### `NearCUE`

 **near-CUE rows.** 

### `abs_T_sub_le`

 N·T_m = m(m+1)/2 up to m·τ, for m ≤ N − 1 (only rows j < N enter). 

### `abs_U_sub_le`

 N·U_m = (m³ − m)/6 up to m(m−1)τ/2, for m ≤ N. 

 ## 2. E on a closed cell 

### `ii_Dfun`

 integrability of D on any subinterval of [0,1]. 

### `Efun_cell`

 **E on the cell [m/N, (m+1)/N]** (m < N):  E(x) = E(m/N) + (T_m/N)(x − m/N) − (x³ − (m/N)³)/6. 

 ## 3. The sup bound 

### `cubic_bounds`

 the cubic on a cell: −(m+1) ≤ −m + 3mθ(1−θ) − θ³ ≤ 0 for 0 ≤ θ ≤ 1, m ≥ 0. 

### `abs_Efun_le_of_nearCUE`

 **the integrated discrepancy of a near-CUE law**: |E| ≤ 1/(6N²) + τ/(2N) on [0,1]. 

### `abs_Efun_one_le_of_nearCUE`

 in particular at x = 1. 

 ## 4. Theorem 1′ for near-CUE laws 

### `ceiling_nearCUE`

 **CEILING FOR A NEAR-CUE GRID LAW.**  Let S be any grid form factor with |N·S(j) − j| ≤ τ for 0 < j < N (atom masses
s_j = S(j)/N at j/N; the row j = N free), and |D(1)| ≤ d₁.  For every certificate (c₀, r) — r ∈ C¹[0,1] with r′ =: g differentiable
off a countable set with integrable derivative h — that is valid against the law, c₀ + Σ_{j=1}^N s_j r(j/N) ≤ p, one has
      c₀ + ∫₀¹ r(x)·x dx ≤ p + d₁·|r(1)| + (1/(6N²) + τ/(2N))·|r′(1)| + (1/(6N²) + τ/(2N))·∫₀¹|r″|. 
