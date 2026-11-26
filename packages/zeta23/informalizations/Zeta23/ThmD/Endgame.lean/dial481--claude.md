---
{
  "module": "Zeta23/ThmD/Endgame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Endgame.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Endgame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Endgame.lean — the §6 endgame for the Montgomery–Taylor window.  Mirror of
Zeta23/Assembly.lean's 'thmA_abstract_err' (Thm A line) and 'thmBC_core' (Thm B/C lines) with

  * the flat-top ratio constant F(λ₁) = (1/λ₁ + λ₁/3)⁻¹ replaced by the window-general
    c := cRatio λ₁ a b J = λ₁a²/(b + λ₁²J) of [eq:ratio-general] (Zeta23/ThmD/AssemblyD.lean), fed by
    the D-trace package 'TracesBoundsD' (tr1 / ratio / frhat) instead of 'TracesBounds';
  * the algebraic step "H(λ₁) ≥ H(λ) − 1/(λl)" replaced by an abstract limit hypothesis
    'cRatio(λ₁(T), a_T, b_T, J_T) → c∞' (discharged in Zeta23/ThmD/Limit.lean with c∞ = c*(λ) =
    cStar λ of [eq:vstar]), so the conclusions carry the constants 2 − 1/c∞, 2c∞ − 1, c∞;
  * the zero side (prop:block, prop:tail, the H-EF bridge) taken for the window-realizing
    parameter family 'P.atD T' of Zeta23/ThmD/ParamsD.lean, whose window at height T is exactly φ_D
    and whose L, X, λ₁, d, τ_k, 𝓔_T are P's definitionally.

Paper: §7.1 [thm:D] ("The argument of §6 applies verbatim with (1/λ₁ + λ₁/3) replaced by
1/c_λ(φ) …").
-/
```

### `thmD_abstract`

 **Theorem D, Thm-A line, at fixed λ ∈ (0,1), abstract zero configuration and abstract
D-traces.**  If the D-trace package holds for data (a_T, b_T, J_T, trG̃, trG̃²) against N(T,2T),
the ratio constant cRatio(λ₁(T); a_T, b_T, J_T) tends to c∞ > 0, a_T ∈ [1/2, 1] eventually, and
the zero-side inputs hold for the window-realizing family P.atD T whose prime-side traces and
taper constant ARE (trG̃, trG̃², a_T), then for every ε > 0, eventually
N₀*(T,2T) ≥ (2 − 1/c∞ − ε) N(T,2T). 

### `thmD_BC_core`

 **Theorem D, Thm-B/C lines, at fixed λ ∈ (0,1) — common core** (mirror of
'Assembly.thmBC_core' with F(λ₁) ↦ cRatio(λ₁; a_T, b_T, J_T) → c∞): there is R = o(N) with,
eventually in T, (2c∞ − 1)N − 2R ≤ N₀ˢ(T,2T) and c∞·N − R ≤ N_d(T,2T). 

### `thmD_simple_abstract`

 **Theorem D, Thm-B line** (fixed λ, abstract): N₀ˢ(T,2T) ≥ (2c∞ − 1 − ε) N(T,2T) eventually. 

### `thmD_dist_abstract`

 **Theorem D, Thm-C line** (fixed λ, abstract): N_d(T,2T) ≥ (c∞ − ε) N(T,2T) eventually. 
