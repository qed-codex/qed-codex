---
{
  "module": "proof/rates/ClauseBound/Gen/Rate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Rate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Gen/Rate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas toward part (b) of the theorem on the general recursion, as an inequality for the exponent of the pad

Arithmetic facts on the numbers of one level of the recursion: K_ℓ and g_ℓ, the label length λ' one
level down, the number of patterns and the bit lengths that grow from level to level;
the bound Bd ρ c x₀ ℓ λ B = e_ℓ·K_ℓ²·λ + C·K_ℓ²·log(K_ℓ·(λ + B)), C = 6c + 14; and the exponent
needG at level ℓ + 1, written out. They are the pieces of an induction on ℓ for
  needG … ≤ size cnt + size (z + size cnt) + Bd ρ c x₀ ℓ λ B. 

 ### The numbers of a step 

### `c_pos`

 1 ≤ c. 

### `pow_mul_le_K`

 2^{x₀}·2^ℓ ≤ K_ℓ. 

### `pow_le_K`

 2^{x₀} ≤ K_ℓ. 

### `big_le_K`

 2^18 ≤ K_ℓ. 

### `K_le_g`

 K_ℓ ≤ g_ℓ. 

### `pow_le_g`

 2^{ℓ+5} ≤ g_ℓ. 

### `K_succ`

 K_{ℓ+1} = g_ℓ². 

 ### The label length one level down 

### `lamNext_eq`

 The label length one level down, written out. 

 ### The bound 

### `Bd`

 The bound on the exponent at level ℓ, without the part that depends on cnt and z. 

### `one_le_log`

 1 ≤ log(K_ℓ·(λ + B)). 

 ### The quantities of one level 

### `two_lam_le`

 2λ ≤ g²·(λ + B). 

### `nPat_eq`

 The number of patterns, written out. 

### `nPat_le`

 The number of patterns is at most X^(c·R). 

### `size_nPat_le`

 A crude bound on the bit length of the number of patterns. 

### `X_cast`

 X as a real number. 

### `pot_step`

 How Nat.size (z + Nat.size cnt) grows at one level. 

### `one_le_lamNext`

 1 ≤ λ'. 

### `bNext_eq`

 B', written out. 

### `zeta_le`

 ζ_ℓ ≤ 1/32. 

### `needG_succ`

 The exponent at level ℓ + 1, written out. 

 ### The quantities of one level, as real numbers 

### `pot_real`

 The bit length of z + Nat.size cnt one level down. 

### `Bd_succ`

 The bound at level ℓ + 1 in terms of g_ℓ. 

### `col_le`

 The budget of the colourings: g·Nat.size K ≤ g⁴. 
