---
{
  "module": "proof/rates/CountedRecursion/EndBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndBounds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/EndBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bounds of Theorem A (b) for a larger constant

Plain arithmetic about `timeBound` = 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} and `sizeBound` =
(K_ℓ(λ+B))^{C₀K_ℓ}, for the last steps of the theorem, where several bounds are put into one with a
larger C₀. With X = K_ℓ(λ+B) ≥ 8:
* `timeBound_mono`, `sizeBound_mono`: they grow with C₀; `three_timeBound_le`: three times the bound
  for C₀ is at most the bound for C₀ + 1; `sizeBound_le_timeBound` (by e_ℓ ≥ 0, from «Clearly e_ℓ ≥
  ½ρ^ℓ» in the proof of part (a): `GeneralPieces.PartA.e_ge_half_pow`);
* `size_tableQuery`, `tableQuery_le`: a query to the tables with its answer has size at most K + 2Kλ +
  B + 3, which with 4 more is at most X², so at most `sizeBound` for every C₀ ≥ 1. 

### `base_ge`

 X = K_ℓ(λ + B) ≥ 8. 

### `timeBound_mono`

 The bound of the theorem grows with C₀. 

### `sizeBound_mono`

 The bound on the sizes grows with C₀. 

### `three_timeBound_le`

 Three times the bound for C₀ is at most the bound for C₀ + 1. 

### `sizeBound_le_timeBound`

 The bound on the sizes is at most the bound of the theorem: K_ℓ ≤ K_ℓ² and e_ℓ ≥ 0. 

### `size_tableQuery`

 A query to the tables that is answered, with its answer, has size at most K + 2Kλ + B + 3. 

### `tableQuery_le`

 With 4 more this is at most the bound on the sizes, for every C₀ ≥ 1. 
