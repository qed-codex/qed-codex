---
{
  "module": "Zeta23/ThmD/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Final.lean — **Theorem D** (the paper §8.1 [thm:D], the Montgomery–Taylor optimal
window), headline forms.

  thmD₀        : ∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, (HD 1 − ε) · N(T,2T) ≤ N₀*(T,2T)         — NO hypotheses,
  thmD₀_simple : … (2·c₁* − 1 − ε) · N(T,2T) ≤ N₀ˢ(T,2T),
  thmD₀_dist   : … (c₁* − ε) · N(T,2T) ≤ N_d(T,2T),
with c₁* = cStar 1 = √2 tan(1/√2)/(1 + tan(1/√2)/√2) [eq:vstar] and
HD 1 = 2 − 1/c₁* = 3/2 − cot(1/√2)/√2 (Zeta23.ThmD.HD_one); cumulative (liminf over (0,T]) forms;
and the fixed-λ forms at every λ ∈ (0,1) with constants HD λ = 2 − 1/c*(λ), 2c*(λ) − 1, c*(λ).
(Numerically 0.67250…, 0.50659…, 0.75329… — decimals are not formalized; the constants enter exactly.
The last two are the Cauchy–Schwarz forms; the paper's [thm:D] states the multiplicity-aware
constants 2 − 1/c₁* = 0.67250… for N₀ˢ and (3 − 1/c₁*)/2 = 0.83625… for N_d, proved in
Zeta23/ThmD/Mult.lean.)

Assembly: the D-prime side 'tracesBoundsD_concrete' (Zeta23/ThmD/Concrete.lean, from PaperInputs and
BridgeD's eventual LocalHypsCore for φ_D), the zero side for the window-realizing family 'P.atD T'
(Zeta23/ThmD/ZeroSideD.lean), the limit cRatio(λ₁; a_D, b_D, J_D) → c*(λ) (Zeta23/ThmD/Limit.lean), the
§6 endgame with abstract ratio constant (Zeta23/ThmD/Endgame.lean), then ζ: Z := zetaZeroConfig with
'paperInputs_zeta' (Zeta23/Final.lean: Weil EF, RvM, MV, Γ all proved), λ → 1⁻ (Limit.eps_form_*),
and dyadic summation (Main.cumulative_of_dyadic).
-/
```

### `thmD_lam_abstract`

 **Theorem D at fixed λ ∈ (0,1), abstract zero configuration with the paper's inputs** —
all three lines, constants HD λ = 2 − 1/c*(λ), 2c*(λ) − 1, c*(λ). 

 ## ζ: fixed λ, then λ → 1⁻, then cumulative — NO hypotheses 

### `thmD_lam`

 **Theorem D at fixed λ ∈ (0,1)**, Thm-A line, UNCONDITIONAL:
N₀*(T,2T) ≥ (2 − 1/c*(λ) − ε) N(T,2T) for all large T. 

### `thmD_simple_lam`

 fixed λ, Thm-B line, UNCONDITIONAL: N₀ˢ(T,2T) ≥ (2c*(λ) − 1 − ε) N(T,2T). 

### `thmD_dist_lam`

 fixed λ, Thm-C line, UNCONDITIONAL: N_d(T,2T) ≥ (c*(λ) − ε) N(T,2T). 

### `thmD₀`

 **Theorem D** [thm:D], UNCONDITIONAL: for every ε > 0 and all large T,
N₀*(T,2T) ≥ (2 − 1/c₁* − ε) N(T,2T), where 2 − 1/c₁* = HD 1 = 3/2 − cot(1/√2)/√2 (= 0.6725…):
at least that proportion of the nontrivial zeros of Mathlib's riemannZeta with T < Im ρ ≤ 2T, counted
with multiplicity, are matched by DISTINCT zeros on the critical line. 

### `thmD₀'`

 **Theorem D**, the constant written out: (3/2 − cot(1/√2)/√2 − ε) N(T,2T) ≤ N₀*(T,2T). 

### `thmD₀_simple`

 **Theorem D**, simple-zeros line [thm:D], UNCONDITIONAL: N₀ˢ(T,2T) ≥ (2c₁* − 1 − ε) N(T,2T)
(= 0.5065…): at least that proportion are SIMPLE zeros ON the line. 

### `thmD₀_dist`

 **Theorem D**, distinct-zeros line [thm:D], UNCONDITIONAL: N_d(T,2T) ≥ (c₁* − ε) N(T,2T)
(= 0.7532…). 

### `thmD₀_cumulative`

 **Theorem D**, cumulative, UNCONDITIONAL: liminf_{T→∞} N₀*(T)/N(T) ≥ 2 − 1/c₁*. 

### `thmD₀_simple_cumulative`

 cumulative simple-zeros line: liminf N₀ˢ(T)/N(T) ≥ 2c₁* − 1. 

### `thmD₀_dist_cumulative`

 cumulative distinct-zeros line: liminf N_d(T)/N(T) ≥ c₁*. 
