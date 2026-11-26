---
{
  "module": "ThreeSumApsp/ConditionalTimes/Corollary38.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Corollary38.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/ConditionalTimes/Corollary38.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 38 from Lemma 37 and Corollary 26

Lemma 37 turns the comparison counts into the wanted entries of one thin matrix product, and
Corollary 26 computes these.

1. For large `n` the parameters `s` and `D*` are admissible: `s ≥ 1`, `D'' ≤ D*`, `(D*)^18 ≤ n`
   (`Corollary38.exists_regime` and the lemmas on `Corollary38.Regime`).
2. The time of Corollary 26 and the time of Lemma 37, as `Claim.Lemma_37` has it, are together at
   most a constant times the bound of the corollary (`corollary_38_bound`).


### `conditional_corollary_38`

 The deduction of **Corollary 38** from Lemma 37 and Corollary 26: "Apply Lemma 37 with s :=
⌈n^{1-1/440}/d⌉ [...] and pad the product to the inner dimension D* [...] and Corollary 26 with N :=
n and D := D* computes (XY)[r,c] for all (r,c) ∈ P". `blockLen n d` is this s, and `Dstar n d` is D*
= ⌈3d²n^{1/440}⌉. 
