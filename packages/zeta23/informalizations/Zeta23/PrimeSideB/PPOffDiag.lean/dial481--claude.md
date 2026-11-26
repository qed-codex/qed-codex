---
{
  "module": "Zeta23/PrimeSideB/PPOffDiag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PPOffDiag.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/PPOffDiag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
  Part of the Zeta23 formalization of the paper
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
  Bracketed labels ([prop:cross], [eq:Msplit], …) and section numbers (§5.4, …) refer to that paper.
-/
```


# [prop:PP] — the off-diagonal term 𝒪₁ (§5.4)

Consumed by `Zeta23/PrimeSideB/PP.lean` .  Everything needed is in
`Zeta23/PrimeSideB/PPKernel.lean`:
* `sub_mul_Aminus_eq` : for θ = y−y' ≠ 0,  θ·A⁻(y,y') = explicit combination of 8 terms
    trig(θ·cT)·M(y or y'),  trig ∈ {sin,cos}, c ∈ {1,2}, M ∈ {Cp,Sp,Cm,Sm} (half-line moments of Φ²);
* `abs_Cp_le` … `abs_Sm_le` : |M(y)| ≤ ∫Φ²;
* `MV_real` : |Σ_{n≠m} u_n v_m trig(c(y_n−y_m))/(y_n−y_m)| ≤ C·√(Σ2n u_n²)·√(Σ2n v_n²)  (H-MV + [eq:deltan]);
* `MV_size_le` : with {u,v} = {a, a·w}, |w| ≤ W:  that bound ≤ 2·C·W·Σ_{n≤X}Λ(n)².
So: split the sum below into the 8 MV-shaped sums (after dividing `sub_mul_Aminus_eq` by θ = log n − log m,
nonzero for n ≠ m ≥ 1 by injectivity of log), bound each by 2·C·(∫Φ²)·ΣΛ², total 16·C·(∫Φ²)·ΣΛ².
(Then PP.lean uses [eq:cheb1] ΣΛ(n)² ≪ X log X = XL and ∫Φ² = 2πbL ≤ 2πL to get 𝒪₁ ≪ L²X.)


### `O1_bound`

 **[prop:PP], 𝒪₁** (§5.4, "Hence |𝒪₁| ≪ L²X" — here in the pre-Chebyshev form):
for T ≥ 0, continuous Φ with Φ² integrable, and H-MV with constant C ≥ 0,
  |Σ_{n≠m≤X} a_n a_m A⁻(log n, log m)| ≤ 16·C·(∫_ℝ Φ²)·Σ_{n≤X} Λ(n)².
(A⁻ = `Aminus`, the difference-frequency half of 𝓜[cos(·y_n),cos(·y_m)], see PPKernel.) 
