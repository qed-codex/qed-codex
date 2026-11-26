---
{
  "module": "proof/networks/Paper/SecCrossing_Crossing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecCrossing_Crossing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Paper/SecCrossing_Crossing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 4 of the paper, for a variant with other pieces: notation only

This file belongs to a variant of Section 4 of the paper that the paper does not print. The paper's
Lemma 2 cuts the strings into blocks of 3 bits and uses the eight-square identity, with ρ = 11/12;
the variant works bit by bit, with pieces A_0, …, A_λ and ρ = (log 12)/4.
The file holds only the notation of the variant.

How to read the Lean text.
* A bit is a `Bool` (`false` = 0, `true` = 1). A string in {0,1}^λ is `Bits lam = Fin lam → Bool`;
  `lam` stands for the
  paper's λ (`λ` is a reserved word of Lean), and the positions are t = 0, …, λ − 1 (the paper: 1,
  …, λ).
* ℤ[T] is `Polynomial ℤ`. `T` is the variable, and `C a` is the integer a as a constant polynomial. 
