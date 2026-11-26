---
{
  "module": "ThreeSumApsp/Sec4/Corollary32.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary32.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Corollary32.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 32 and the proof of Theorem 25: the time for `|W| ≤ N²/D^κ` wanted entries

Corollary 32 asks one query of Corollary 31 for each of the `|W| ≤ N²/D^κ` wanted positions, which
gives the time `O(N² log² D (D^{-γ} + D^{q-κ}))`. This bound is "a saving of D^{min{γ, κ-q}}, up to
logarithmic factors" (`corollary_32_saving`). The proof of Theorem 25 does the same with Theorem 24
and `q := κ/2`; the sum of its two times is `Theorem25.time`, which `wordRam_theorem_25` uses.


### `corollary_32_saving`

 Corollary 32: `N² log² D (D^{-γ} + D^{q-κ})` is "a saving of D^{min{γ, κ-q}}, up to logarithmic
factors, over the size N² of the product":
`D^{-min{γ,κ-q}} ≤ D^{-γ} + D^{q-κ} ≤ 2 D^{-min{γ,κ-q}}`. 

### `Theorem25.time`

 Proof of Theorem 25: "As |W| ≤ N²/D^κ, this takes O(N² log² D/D^γ + |W| D^{κ/2} log D) = O(N²
log² D/D^{γ'}) time, where γ' := min{γ, κ/2}." 
