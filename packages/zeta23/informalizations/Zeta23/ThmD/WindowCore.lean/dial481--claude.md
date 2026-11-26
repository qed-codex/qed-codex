---
{
  "module": "Zeta23/ThmD/WindowCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/WindowCore.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/WindowCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/WindowCore.lean — the test-family facts of §5 for an ARBITRARY admissible window
(the generic half of "BridgeD").

Paper §7.1: "Propositions 5.1–5.5 hold verbatim for any even C_c² window with the same support
and derivative norms."  We package such a window as `AdmWindow v L w c` (even, `0 ≤ v ≤ 1`,
`C²`, `supp v ⊆ [−L/2, L/2]`, `‖v'‖₁, ‖(v²)'‖₁ ≤ 2`, `‖v''‖₁, ‖(v²)''‖₁ ≤ c/w`, `c ≥ 4`,
`1 ≤ w`, `8w ≤ L`) and derive, ONCE, everything `LocalHypsCore` asks of the data
`(v̂, (v²)^, v⋆v, v²⋆v², a, b)` — by the same generic lemmas (Zeta23/Poisson/PaperFT.lean,
Zeta23/Taper/{Strip,Decay,Fourier}.lean §Generic, Zeta23/Poisson.lean) that the flat-top facade
Zeta23/Taper.lean specializes to `Taper.phi`.  The Montgomery–Taylor window `ThmD.phiD` is an
`AdmWindow` with `c = cDT` (Zeta23/ThmD/BridgeD.lean); so is the flat window with `c = cRho ϱ`.
-/
```

### `AdmWindow`

 An admissible window for §5 (paper §2 test family minus the flat top; §7.1). 

 ## The data attached to a window 

### `vHat`

 `v̂` (paper Fourier convention), complex argument. 

### `vHatR`

 `v̂` restricted to ℝ (real-valued since `v` is real and even). 

### `VPhi`

 `V := (v²)^`. 

### `Av`

 `A_v := v ⋆ v`. 

### `gv`

 `g_v := v² ⋆ v²`. 

### `av`

 `a := L⁻¹ ∫ v²`, `b := L⁻¹ ∫ v⁴`. 

### `localFun`

 The abstract local data of the window (`LocalFun`). 

 ## Elementary consequences of admissibility 

 #### the ℂ-valued window and its square, as inputs to the PaperFT lemmas 

 #### `∫ v ≤ L`, `∫ v² ≤ L` 

 ## [eq:hfbound]-type pointwise bounds for `v̂` and `V` 

### `abs_vHatR_le_psiA`

 `|v̂| ≤ ψ_c` in the majorant spelling `psiA c p` (for any `p` with `p.L = L`, `p.w = w`). 

 ## Real / even / continuous; values at 0; `v̂² = Â_v`, `V² = ĝ_v`; inversion; Plancherel 

### `vHatR_sq_eq`

 `v̂² = (A_v)^` on ℝ. 

### `VPhiR_sq_eq`

 `V² = (g_v)^` on ℝ. 

 #### the autocorrelations 

 #### inversion (cosine form) and Plancherel 

 ## [lem:poisson] for the window 

### `hasSum_vHatR_mul`

 `Σ_{k∈ℤ} v̂(τ−τ_k) v̂(τ'−τ_k) = L · V(τ−τ')`, `τ_k = T + k·2π/L`. 

 ## [eq:abdef] without the flat top: `0 ≤ b ≤ a ≤ 1` 
