---
{
  "module": "Zeta23/ZeroSide/Mult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/Mult.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide/Mult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZeroSide/Mult.lean — the multiplicity-aware zero side: Lemma R (Zeta23/ZeroSide/RankTraceMult.lean) applied to the block
structure of Zeta23/ZeroSide.lean.  At the level of 𝒵(I′) (abstract ZeroBlockData, then the concrete Â = hat(A_z)):
   c = 2:  4·tr Â − ‖Â‖_F² − 2·N(I′) ≤ s₁                     (simple zeros on the line)
   c = 3:  6·tr Â − ‖Â‖_F² − 3·N(I′) ≤ 2·#𝒵(I′) = 2·N_d(I′)      (distinct zeros)
using only ‖v_ρ‖² ≤ aL² (the truncated Poisson sum, no edge leak) and n₊(Q) ≤ p.
-/
```

### `vhat`

 the normalized on-line vectors v_z/√c (c = aL²) over the on-line index subtype. 

### `mhat`

 the on-line multiplicities as reals. 

### `blockP_eq_Pmat`

 blockP c = Pmat (multiplicities) (normalized on-line vectors). 

### `xsq_vhat_le`

 ‖v_z/√c‖² ≤ 1 from the truncated Poisson bound Σ_k‖v_z k‖² ≤ c. 

### `card_onLine_m_eq_one`

 #{z on-line : m z = 1} = s₁. 

### `card_sub_filter`

 counting over the on-line SUBTYPE equals counting over the Finset. 

### `mult_two`

 **c = 2 at the block level**:  4·tr Â − ‖Â‖² − 2N(I′) ≤ s₁   (Â := c⁻¹·A = blockP + blockQ, c = aL²). 

### `mult_three`

 **c = 3 at the block level**:  6·tr Â − ‖Â‖² − 3N(I′) ≤ 2·#𝒵(I′). 

 ### the concrete Â = hat(A_z) 

### `hatAz_mult2`

 **c = 2**: 4·tr Â − ‖Â‖_F² − 2·N(I′) ≤ s₁(I′)   for Â = P.hat T (Z.Az P T). 

### `hatAz_mult3`

 **c = 3**: 6·tr Â − ‖Â‖_F² − 3·N(I′) ≤ 2·#𝒵(I′) = 2·N_d(I′). 
