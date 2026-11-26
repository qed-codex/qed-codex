---
{
  "module": "Zeta23/ThmDE/Endgame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Endgame.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmDE/Endgame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmDE/Endgame.lean — the §6 endgame for L(s,χ) with the
Montgomery–Taylor ratio constant: paper [thm:E], last clause ("Theorem D holds likewise.").

A mirror of Zeta23/ThmD/Endgame.lean (thmD_abstract / thmD_BC_core / thmD_simple_abstract /
thmD_dist_abstract) with the χ-substitutions of Zeta23/ThmE/AssemblyQ.lean:
  * (H : PaperInputs Z) ↦ (hRvM : ThmE.RiemannVonMangoldtChi q Z) — the only use of H there was
    H.RvM (growth of N(T,2T)): tendsto_N_atTop ↦ ThmE.tendsto_N_atTop_chi,
    isLittleO_N_of_isLittleO_Tl ↦ ThmE.isLittleO_N_of_isLittleO_Tl_chi,
    eventually_N_ge ↦ ThmE.eventually_N_ge_chi;
  * TracesBoundsD ↦ ThmDE.TracesBoundsDChi P q (cRatio taken at λ_{1,χ} = ThmE.lam1q P q T);
  * the prime-side matrix/traces (P.atD T).Gp / trGtilde / trGtildeSq ↦ ThmE.GpChi /
    trGtildeChi / trGtildeSqChi of (P.atD T) (rtrace_tilde_GpChi, frobSq_tilde_GpChi,
    GpChi_isHermitian).
Everything else (seamA, seamA_BC, N0star_lower_c, nplus_lower, nplus_ge_explicit, err_isLittleO,
eps_form_of_isLittleO, the o-calculus) is q-independent and reused verbatim.  Conclusions carry
the constants 2 − 1/c∞, 2c∞ − 1, c∞ for an abstract limit c∞ of cRatio(λ_{1,χ}(T); a_T, b_T, J_T).
-/
```

### `thmDChi_abstract`

 **Theorem D for L(s,χ), Thm-A line, at fixed λ ∈ (0,1), abstract zero configuration and abstract
D-traces.**  If the D-trace package holds for data (a_T, b_T, J_T, trG̃, trG̃²) against N(T,2T),
the ratio constant cRatio(λ₁(T); a_T, b_T, J_T) tends to c∞ > 0, a_T ∈ [1/2, 1] eventually, and
the zero-side inputs hold for the window-realizing family P.atD T whose prime-side traces and
taper constant ARE (trG̃, trG̃², a_T), then for every ε > 0, eventually
N₀*(T,2T) ≥ (2 − 1/c∞ − ε) N(T,2T). 

### `thmDChi_BC_core`

 **Theorem D for L(s,χ), Thm-B/C lines, at fixed λ ∈ (0,1) — common core** (mirror of
'Assembly.thmBC_core' with F(λ₁) ↦ cRatio(λ₁; a_T, b_T, J_T) → c∞): there is R = o(N) with,
eventually in T, (2c∞ − 1)N − 2R ≤ N₀ˢ(T,2T) and c∞·N − R ≤ N_d(T,2T). 

### `thmDChi_simple_abstract`

 **Theorem D for L(s,χ), Thm-B line** (fixed λ, abstract): N₀ˢ(T,2T) ≥ (2c∞ − 1 − ε) N(T,2T) eventually. 

### `thmDChi_dist_abstract`

 **Theorem D for L(s,χ), Thm-C line** (fixed λ, abstract): N_d(T,2T) ≥ (c∞ − ε) N(T,2T) eventually. 
