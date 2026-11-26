---
{
  "module": "proof/rates/GeneralPieces/Half/Consts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Consts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Consts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The constants of the programs for the pieces with ρ = 1/√2, from the numbers of Appendix B

The programs `halfF c₀ c` have two constants. What these have to satisfy at a length λ is the
structure `ClauseBound.Inst.Half.Cst`. `exists_cst2`: there are constants that satisfy it at every λ
≥ 1.
Here h is the least integer ≥ 2 with p(h) ≥ 2^λ, and Δ is the number of the partitions of 0, …, 4h.
The fields come from the proof of the theorem on the pieces with ρ = 1/√2 in Appendix B:
* the number 4h + 1 of pieces, d = h! and c^row_s + c^col_s ≤ 2√2·λ + c·log 2λ are read off that
  theorem itself, in the form without the running time (`AppHalfPieces.ThmHalfPiecesPure`, a
  hypothesis here; `numbers_of_thmHalfPieces`);
* h ≤ c₀·λ² is the sentence «Hence h = O(λ²)» (`GeneralPieces.Bits.exists_hOf_le`);
* the rest speaks of numbers of the programs that the appendix does not name: the cut-off 2cλ for
  each number of bits, the number 40(h+1)² + ⌈log Δ⌉ of bits of all values (the appendix has sizes
  2^{O(h²)}), and the number
  2^10·(h+2)^4·(Δ+1)² of units of the pad that is enough for them (the appendix has Δ^{O(1)}
  operations). These are bounded by elementary arithmetic (`cap_le`;
  `ClauseBound.Boson.Final.big_le`; `pad_le`) from the display on
  c^row_s + c^col_s, from h ≤ c₀·λ² and from the sentence «log Δ = O(λ)»
  (`GeneralPieces.Bits.exists_Delta_le`).
Both h = O(λ²) and log Δ = O(λ) rest on display (46), the bounds on log p(E) from the
Hardy–Ramanujan formula, in the form proved in Lean as `ClauseBound.Part.exists_bounds`. 

### `numbers_of_thmHalfPieces`

 What the theorem on the pieces with ρ = 1/√2 says about numbers only: |𝓘| = 4h + 1 ≤ (2λ)^c, d =
h! < 2^{(2λ)^c}, and c^row_s + c^col_s ≤ 4ρλ + c·log 2λ for |s| ≤ 2h. 

### `four_mul_rho_le`

 4ρ = 2√2 ≤ 3. 

### `cap_le`

 Two numbers of bits with a + b ≤ 4ρλ + c·log 2λ have a + b ≤ (3 + c)·λ, because 4ρ ≤ 3 and log
2λ ≤ λ. So the cut-off of the programs at 2c'λ bits is not active if 3 + c ≤ 2c'. 

### `pad_le`

 The pad of the programs: if h ≤ c₀·λ² and Δ ≤ 2^{c₂λ}, then 2^10·(h+2)^4·(Δ+1)² ≤
2^{(4c₀+2c₂+28)λ}. 

### `exists_cst2`

 The choice of the constants in the last sentence of the proof, «if c is large enough»: there are
constants c₀ and c that are large enough for the programs at every length. 
