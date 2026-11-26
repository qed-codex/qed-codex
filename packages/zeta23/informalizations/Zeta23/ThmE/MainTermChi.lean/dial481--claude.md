---
{
  "module": "Zeta23/ThmE/MainTermChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/MainTermChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/MainTermChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/MainTermChi.lean — the main term of N_χ(T,2T) (a piece of H-RvM(χ), see
Zeta23/ThmE/RvMChi.lean).
  |N_χ(T,2T) − (T/2π)·ell1q q T| ≤ C log T   (T ≥ T₀; C, T₀ depend on q).
The analogue of the RvM MainTerm.lean assembly for L(s,χ), with Λ_sym = completedLSym
(CountByIntegralChi/FoldChi), Γ/conductor side = gammaSideChi, Backlund for L (BacklundChi),
local count = localCountChi.

The assembly is proved once, q-uniformly (`mainChi_uniform_aux`, absolute constants, log scale
log(q(T+2))); the per-χ headline `mainChi` is its corollary.
-/
```

 ### window helpers 

### `exists_goodHeightL`

 zero-free ordinates for L are dense: every [a, a+1] contains one. 

 ### the split along the half-contour 

### `LFunction_ne_zero_on_segment'`

 L(σ + iT) ≠ 0 on the horizontal segment [1/2, 2] at a zero-free ordinate. 

### `continuousOn_logDeriv_LFunction`

 continuity of logDeriv L along a segment avoiding zeros (parametrised). 

### `halfContourChi_split`

 the half-contour split: logDeriv Λ_sym = logDeriv L + logDeriv arch along L. 

 ### The q-UNIFORM assembly (absolute constants) 

### `muq_le_log_uniform`

 q-uniform |μ_χ| ≤ (C+2)·log(q(τ+3)) for τ ≥ 1, from the bounded Stirling field. 

### `mainChi_uniform_aux`

 q-uniform main-term assembly, parametric in the uniform Backlund and H-Γ(χ)-bounded inputs
(shapes = RvMChiUniform's backlund_horizontalChi_uniform / gammaFactsChi_uniform). 

 ### Per-χ main term (from the q-uniform assembly) 

### `mainChi`

 **Main term for N_χ(T,2T)** (per-χ constant; from `mainChi_uniform_aux` instantiated with the q-uniform
Backlund bound and the bounded H-Γ(χ) facts: log(q(T+2)) ≤ (log q + log 2 + 1)·log T for T ≥ 3). 
