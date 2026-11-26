---
{
  "module": "ThreeSumApsp/Sec5/Corollary40/RoundingThreshold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/RoundingThreshold.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec5/Corollary40/RoundingThreshold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 40, "General τ", Conjecture 5.12: rounding does no harm for large t₁

Proof of Corollary 40: "we use the same blocks, which requires n^{τ₁} ≤ n^{ετ₂}".  The hint
dimensions are the integers t₁ = ⌊n^{τ₁}⌋ and t₂ = ⌊n^{τ₂}⌋, and the condition of the data
structure, t₁ ≤ t₂^ε, can fail for some n although τ₁ < ε τ₂.  It holds as soon as t₁ exceeds a
constant: then n is so large that n^{ετ₂ − τ₁} ≥ 2, and t₂^ε ≥ n^{ετ₂}/2 ≥ n^{τ₁} ≥ t₁.  Below that
constant the data structure does not need the condition, because it answers queries by inner
products.


### `two_le_rpow_of_pow_lt_hintSize`

 If t₁ exceeds 4^K with K ≥ τ₁/δ, then n is so large that n^δ ≥ 2. 

### `rpow_rpow_le_two_mul_hintSize_rpow`

 Rounding t₂ down loses at most a factor 2: (n^τ₂)^ε ≤ 2 t₂^ε for 0 ≤ ε ≤ 1. 

### `exists_hint_threshold`

 For τ₁ < ε τ₂ there is a threshold M such that t₁ ≤ t₂^ε whenever ⌈log₄ t₁⌉ ≥ M. 
