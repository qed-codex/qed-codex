---
{
  "module": "proof/variables/VariableBound/Params/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Params/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Setting and parameters of Appendix D: the computed parameters are those of the text

Each of `nbD`, `rbD`, `tbD` is made from a count: the number of the numbers below a bound at which a
property that is closed upwards does not hold yet (r̄ and t̄ are this count c, and n̄ = 2^(c − 1)).
If the
property holds somewhere up to the bound, the count is the least number with the property
(`count_spec`). For n̄ the property is (2Δ)^(2^a) > 2^n, which holds at a = ⌊log₂ n⌋ + 1; for r̄ it
is 3^j·2^β < 4^j, which holds at j = 3β + 1 because 54 < 64; for t̄ it is
m·(15n̄+16)^r̄ ≤ 2^c·(15n̄)^r̄, which holds at c = size m + r̄ if n̄ ≥ 2, because then 15n̄ + 16 ≤
2·15n̄. 

### `length_filter_range`

 If p holds below N exactly at the numbers below k, it holds at min N k numbers below N. 

### `count_spec`

 Let P be closed upwards and hold at some number j ≤ N, and let p decide «not P». Then the number
of j < N with p j is the least number at which P holds. 

### `nb_count`

 What `count_spec` gives for n̄: the count a of `nbD` is the least number with 2^n < (2Δ)^(2^a),
for Δ ≥ 1. 

### `isNb_nbD`

 The computed n̄ is the n̄ of the text, if Δ ≥ 1 and 2Δ ≤ 2^n. 

### `two_le_nbD`

 The computed n̄ is at least 2, if Δ ≥ 1 and (2Δ)² ≤ 2^n. 

### `isRb_rbD`

 The computed r̄ is the r̄ of the text. 

### `tb_iff`

 The condition on c in the definition of t̄, with the denominators cleared; for n̄ ≥ 1. 

### `isTb_tbD`

 The computed t̄ is the t̄ of the text, if n̄ ≥ 2. 

### `stParamSpec`

 «Setting and parameters»: the computed n̄ (for Δ ≥ 1 and 2Δ ≤ 2^n; it is at least 2 if (2Δ)² ≤
2^n), r̄ and t̄ (for n̄ ≥ 2) are the numbers that the text defines. 
