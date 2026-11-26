---
{
  "module": "proof/networks/Eight/Level/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The arithmetic of the cost of a level

The arithmetic of the cost of one level for the pieces of Lemma 2 from the eight-square identity.
Proof of Proposition 3, «Cost»: with N = g⁴λ, a term costs 2^{e·U + (e + 2)·gP/K} times a
polynomial, where U ≤ ρN + N/g + 2g⁴, ρ = 11/12, and gP = N, and there are
(t + 1)^{|ℛ|} terms, t = ⌈λ/3⌉. `exponent_le`: the exponent is at most ((ρ + 2/K)e + 2/K)·N + 2e·g⁴,
because 1/g ≤ 1/K. `level_time`: the number of terms, the constant 2^{2e·g⁴} and all polynomial
factors are absorbed in
one number A₁. `level_size`: the sizes that occur in the loop over the terms add up to a polynomial;
this is `SingleBitPieces.Level.level_size`, which mentions neither ρ nor the number of pieces. 

### `exponent_le`

 «Cost»: «its exponent satisfies e(U + N/K) + 2N/K ≤ N((ρ + 2/K)e + 2/K) + 2eg⁴ = e'N + 2eg⁴»,
with N = g⁴λ and the bound ρN + N/g + 2g⁴ in place of U. 

### `level_time`

 Proof of Proposition 3, «Cost», the number of steps: the number (t + 1)^{Rn} of terms times the
cost of a term, plus two steps, is at most A₁·2^{((ρ + 2/K)e + 2/K)·(g²)²·λ}·(B + λ)^{A₁}·t. The
exponent is the paper's;
«2^{2eg⁴} is a constant» and «(t + 1)^{|ℛ|} ≤ (B + λ)^{g⁴/4}» go into A₁ (here t + 1 ≤ 2(B + λ) is
used). 

### `level_size`

 Proof of Proposition 3, «Cost», the sizes: the sum of the sizes that occur in the loop over the
terms is polynomial in sc + B + λ. Not in the paper, which counts operations only. This is
`SingleBitPieces.Level.level_size`, word for word. 
