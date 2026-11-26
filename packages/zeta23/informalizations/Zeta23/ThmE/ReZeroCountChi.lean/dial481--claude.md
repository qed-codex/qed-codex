---
{
  "module": "Zeta23/ThmE/ReZeroCountChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ReZeroCountChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/ReZeroCountChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/ReZeroCountChi.lean — the Jensen half of Backlund's bound for L(s,χ): the number of
zeros of Re L(σ+iT,χ) on σ ∈ [1/2,2] is ≪_χ log|T|.
This is the analogue of Zeta23/RvM/ReZeroCount.lean (same route and proof) for L(s,χ), using the
symmetrised function g(z) := (L(z+iT,χ) + L(z−iT,χ⁻¹))/2 (entire; = Re L(σ+iT,χ) on ℝ by
LFunction_conj), growth for χ and χ⁻¹ from LFunction_growth_right, and no pole
bookkeeping — hence two-sided in the height T.
-/
```

### `symL`

 the symmetrised function g_T(z) := (L(z+iT,χ) + L(z−iT,χ⁻¹))/2; equals Re L(σ+iT,χ) for real σ. 

### `symL_ofReal`

 for real σ, g_T(σ) is the real number Re L(σ + iT, χ). 

 ## The q-UNIFORM Jensen count and Backlund bound (absolute constants) 

### `reZeroSetL_card_le_uniform`

 **(J), q-uniform** (the per-χ `reZeroSetL_card_le` below is its corollary):
#{σ ∈ [1/2,2] : Re L(σ+iT,χ) = 0} ≤ C·log(q(|T|+3)) with an absolute C,
for every modulus q, every χ ≠ 1 mod q and every real T. 

### `backlund_horizontalChi_uniform`

 **Backlund's bound for L(s,χ), q-uniform** (absolute C; all q, all χ ≠ 1, all T). 

 ## Per-χ forms 

### `reZeroSetL_card_le`

 **(J) the Jensen half of Backlund's bound for L(s,χ)**: #{σ ∈ [1/2,2] : Re L(σ+iT,χ) = 0} ≪_χ log |T|
(per-χ form; from the q-uniform bound, since q(|T|+3) ≤ |T|² once |T| ≥ 2q + 6). 

### `backlund_horizontalChi`

 **Backlund's bound for L(s,χ)**: two-sided in T; constants depend on χ. 
