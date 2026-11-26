---
{
  "module": "Zeta23/ThmE/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/Main.lean — Theorem E: [thm:E]'s bounds at fixed λ modulo the
χ-traces package and the χ-EF bridge.

Mirror of Zeta23/Main.lean's thm{A,B,C}_lam_of_traces for a primitive Dirichlet character: the
zero-side/tail/taper inputs are discharged from the SAME Z-generic project files
(ZeroSide, Tail, Taper — nothing ζ-specific in them), while the two genuinely
χ-arithmetic inputs stay explicit named hypotheses:
  hTr   — [thm:traces] for ν_{X,χ} (ThmTracesHypChi),
  hGzGp — the [eq:Gdef]-identity for L(s,χ) (zero side = prime side, from H-EF(χ)).
-/
```

### `tailPackageChi`

 [prop:tail] package for a χ-configuration (mirror of `Tail.eventually_tailPackage`, whose only
use of `PaperInputs` is the local count — here taken from `RiemannVonMangoldtChi`). 

### `NIIChi`

 boundary count for a χ-configuration (from the two-sided local count). 

### `thmE_A_lam_of_traces`

 **Theorem E, first bound, at fixed λ ∈ (0,1), modulo the χ-traces package and the χ-EF
bridge** ([thm:E]; the analogue of Zeta23.thmA_lam_of_traces). 

### `thmE_B_lam_of_traces`

 **Theorem E, second bound (simple on-line zeros) at fixed λ, modulo the χ inputs** ([thm:E]). 

### `thmE_C_lam_of_traces`

 **Theorem E, third bound (distinct zeros) at fixed λ, modulo the χ inputs** ([thm:E]). 

 ## The seam discharged (Zeta23/ThmE/SeamL.lean): the gates without the `LSeam` hypothesis 

### `thmE_A_lam_of_traces'`

 Theorem E bound 1 at fixed λ, for a PRIMITIVE χ mod q > 1;
remaining hypotheses: RvM(χ), the χ-traces package, the χ-EF bridge, 𝓔 → 0. 

### `thmE_B_lam_of_traces'`

 Theorem E bound 2, seam discharged. 

### `thmE_C_lam_of_traces'`

 Theorem E bound 3, seam discharged. 

### `GzGpChi_at`

 the χ-EF bridge at FIXED T (the eventual form below is this plus
two asymptotic side conditions). Conditions: 0 < L(T) and 8w ≤ L(T). 

### `eventually_GzGpChi`

 the χ-EF bridge, eventual-in-T form (`Gz_eq_GpChi` + the Taper side conditions;
mirror of Main.lean's `eventually_side_conditions` first component). 

### `thmE_A_lam_final`

 **Theorem E bound 1 at fixed λ**: remaining inputs are
exactly the χ-arithmetic trio (EF(χ) paper form, RvM(χ), traces(χ)). 

### `thmE_B_lam_final`

 same, bound 2 (simple on-line). 

### `thmE_C_lam_final`

 same, bound 3 (distinct). 

 ## RvM(χ) discharged (Zeta23.ThmE.rvmChi): remaining inputs are
(EF(χ) paper form, traces(χ)). 

### `thmE_A_lam₂`

 **Theorem E bound 1 at fixed λ, TWO hypotheses** (EF-bridge side conditions, 𝓔 → 0 and
RvM(χ) all discharged). 

### `thmE_B_lam₂`

 bound 2, two hypotheses. 

### `thmE_C_lam₂`

 bound 3, two hypotheses. 

 ## thm:traces(χ) discharged via `thm_traces_chi`: Theorem E at ONE hypothesis 

### `coeffUnimodular_of_primitive`

 the coefficient sequence of a primitive character is unimodular-on-coprime
(values of norm ≤ 1 everywhere, = 1 on units, 0 off units; Mathlib's
`DirichletCharacter.norm_le_one` / `unit_norm_eq_one` / `MulChar.map_nonunit` +
`ZMod.isUnit_iff_coprime`). 

### `parity_le_one`

 parity is ≤ 1 by construction. 

### `PaperInputsChi.of_EF`

 **PaperInputsChi from the χ-EF alone**: every other field is a theorem
(rvmChi, chebyshevMertens, chebyshevMertensCoprime, mvDiag_thirteen, gammaFactsChi). 

### `thmE_A_lam₁`

 **Theorem E bound 1 at fixed λ, ONE hypothesis** — everything but the χ-explicit formula
(paper form) is a theorem. 

### `thmE_B_lam₁`

 bound 2, one hypothesis. 

### `thmE_C_lam₁`

 bound 3, one hypothesis. 
