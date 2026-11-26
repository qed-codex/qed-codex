---
{
  "module": "proof/variables/VariableBound/Top/ArithNat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithNat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Top/ArithNat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 4, the arithmetic of the exponent: natural numbers, for an arbitrary β

The bounds of Step 4 in natural numbers, derived from `Net.StBounds` (the bounds of Step 3 on the
total U and on g·P, in closed form), which is a hypothesis here. The same kind of arithmetic as in
proof/sparsification/UniformInK/Top/ArithNat.lean, whose lemmas `two_le_D` and `WofU_ge` are used.
β is any natural number, under some of the hypotheses 1 ≤ β, k ≤ β, β + 3 ≤ 2^β. Notation as in
proof/variables/VariableBound/Top/ArithDefs.lean: Δ = D = 2^β, b = β + 3, g = 3K⁸, Y = size K, W =
b²·D·Y. 

### `UbD_le`

 The bound of Step 3 on the total U, in closed form, for Δ = 2^β: U ≤ 140·k·n·(β+1) + 18·K^16,
for β ≥ 1 and n ≥ 1, given `Net.StBounds`. 

### `gPD_le`

 The bound of Step 3 on g·P, in closed form, for Δ = 2^β: g·P ≤ n·2^β·(842·(β+3) + 4·size n), for
β ≥ 1, n ≥ 1 and g = 3K⁸ ≤ n, given `Net.StBounds`. 

### `g_le_n`

 Step 4, «g ≤ n»: 3K⁸ ≤ n, for 2 ≤ K and K^17 ≤ n. 

### `gPD_le_W`

 g·P ≤ G·W·n, where G = `GD C₀`, for β ≥ 1, 2 ≤ K and K^17 ≤ n < K^(17·C₀). 

### `bitsS_eq`

 The bound B' = `bitsS` for the bit length of the entries of the rebalanced instance, for g = 3K⁸
and K ≥ 1: B' = P·6K⁷ + B·(6K⁸ + 36K^15). The paper's B' is ⌈2gP/K⌉ + g²·B = 6K⁷·P + 9K^16·B. 

### `argD_le`

 Step 4, «the numbers L and B' are polynomial in n»: K·(λ + B') ≤ 2^(5·17·C₀·Y + 16), for k ≤ β,
β + 3 ≤ 2^β ≤ n + 1, 2 ≤ K and K^17 ≤ n < K^(17·C₀). 

### `size_objMax_le`

 The bit length of the bound for the number of objects, for Δ = 2^β: at most 2β + size n + 10. 

### `size_lists_le`

 The bit length of the bound for the list of checks, for Δ = 2^β: at most 3β + 2·size n + 17. 

### `lowerD`

 Step 4, «all these are o(en)», first half: the parts of lower order of the exponent, each
multiplied by K, are at most a number times W·n; the number depends on C₀ only, except 19 + 140·k +
G, where G = `GD C₀`, for the part
(K − 1)·λ; for 1 ≤ β, k ≤ β, 2 ≤ K and K^17 ≤ n < K^(17·C₀), given `Net.StBounds`. 

### `stUbD`

 The bound of Step 3 on the total U, for Δ = 2^β, from the bounds in closed form. 

### `stArgD`

 Step 4, «the numbers L and B' are polynomial in n», from the bounds in closed form. 

### `stLowerD`

 Step 4, «all these are o(en)», first half, from the bounds in closed form. 
