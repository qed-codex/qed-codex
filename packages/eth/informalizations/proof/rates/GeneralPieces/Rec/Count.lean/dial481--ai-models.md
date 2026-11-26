---
{
  "module": "proof/rates/GeneralPieces/Rec/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Rec/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The count of operations in the proof of part (b) of Theorem A, as arithmetic

Here a number of operations is rendered as a padding string of that many ones (Appendix E), and the
induction for part (b) bounds the exponent of its length. The text counts operations. This file
checks
the arithmetic of the text's count, as the text has it: the two inequalities of the display «So the
total number of operations is at most …», in real variables, with arbitrary natural numbers for C₁,
C₂, C₃.
The constant C₄, which the text does not write out, is (c+4)C₁ + C₂ + C₃ + c + 4 in the exponent of
the first inequality; the second takes it as a parameter. 

### `count_first`

 The first inequality of the display, in real variables: X = Ξ, s = 2^{2N/K}, u = 2^{cλ}, a = |𝓘|^{|R|}
≤ Ξ^A, κ = K^g ≤ Ξ^G, q = (2|𝓘|+2)·2^{cλ} ≤ Ξ^{c+1}τ, τ = u·Ξ^{C₂}, D₁ = (c+4)C₁. Every sum of two
numbers is bounded by Ξ times the larger bound («a sum of numbers that are at least 2 is at most
their product»). 

### `count_second`

 The second inequality of the display, in real variables: x = e(ρ+3ζ)N, y = 2N/K + cλ, z =
e_{ℓ+1}N, A = cg⁴/4, G = g, k2 = K², Z = (c+5)C₀K². 
