---
{
  "module": "proof/rates/ClauseBound/Boson/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Boson/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Bounds on `big h`, for the constant c of pieces with ρ = 1/√2

Elementary lemmas on the number `big h` of proof/rates/ClauseBound/Boson/Half.lean, of the kind
needed to choose the constant c of pieces with parameters (1/√2, c) (Definition 7, Appendix B); here
h is any natural number.
If h ≤ c₀·λ² and the partitions of the integers up to 4h are at most 2^(c₂·λ), then big h ≤ (2λ)^c
for c = c₁ + 4 + 40(c₀ + 1)² + c₂ (`big_le`); moreover 4h + 1 ≤ big h and h! < 2^(big h).
A factorization with values below b is also one with values below any larger bound
(`factorsThrough_mono`). 

### `factorsThrough_mono`

 A factorization with values below b is one with values below any b' ≥ b. 

### `big_le`

 If h ≤ c₀·λ² and the partitions of the integers up to 4h are at most 2^(c₂·λ), then big h ≤
(2λ)^c for c = c₁ + 4 + 40(c₀ + 1)² + c₂. 

### `four_mul_add_one_le_big`

 4h + 1 ≤ big h. 

### `factorial_lt_two_pow_big`

 h! < 2^(big h). 
