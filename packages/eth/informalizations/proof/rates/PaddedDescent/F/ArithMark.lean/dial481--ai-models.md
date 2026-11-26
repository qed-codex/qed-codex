---
{
  "module": "proof/rates/PaddedDescent/F/ArithMark.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithMark.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/ArithMark.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The profiles and the layers fit under the pad (the fields `prof` and `lay` of `MarkFits`)

One evaluation runs through `Mark.nProf g m (R + 2)` = (m+1)^(g·g·(R+2)) numbers as profiles, and
the division of the clauses into layers is a word of length
at most `layLen k n m R`. Here: for s = `sOf n` ≥ 1, g = 3·K⁸ with K = `Kseq (depthOf s)`, R =
`layersOf s`, every width k ≤ s and m = Δ·n clauses with any Δ ≤ 2^β, β = `betaOf s`, both numbers
are
at most every F with 2^(C₀·(⌊n/2^s⌋+1)) ≤ F, for C₀ ≥ 1; F is the length of the pad, the padding
string given to the algorithm with its input. No programs occur here. 

### `clauses_succ_le`

 The number of clauses of a sparsified formula, plus one, is at most 2^(β + size n). 

### `prof_exponent_le`

 The logarithm of the number of profiles is at most ⌊n/2^s⌋, for s = sOf n ≥ 1. 

### `nProf_le`

 The field `prof` of `MarkFits`: the pad has a unit for every number that is tried as a profile. 

### `layLen_le`

 The field `lay` of `MarkFits`: the word of the layers fits under the pad. 
