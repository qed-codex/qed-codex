---
{
  "module": "proof/variables/VariableBound/Net/SizeSmall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeSmall.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/SizeSmall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The parameters», last sentence: the case m ≤ n̄

«If m ≤ n̄, the list is empty and there are only clauses: … every test costs at most one bit, so U ≤
2(k − 1)n̄ ≤ 2kn, and P = 2⌈n/g⌉(1 + Δ) and B = 1 will do.» With the empty list of checks no object
is an
incidence. So at most ⌈n/g⌉·Δ objects touch a node, W_a is 0, 1 or −1, and the number of all tests
is at most (k − 1)·m. 

### `length_tch_le`

 With the empty list of checks, at most ⌈n/g⌉·Δ objects touch a node, if g > 0, ψ is well formed
(`WfD`) and every variable occurs in at most Δ clauses. 

### `abs_WD_le`

 With the empty list of checks, |W_a| ≤ 2^1 for every node, profile, flag and word: condition (ii)
with B = 1. (In fact W_a is 0, 1 or −1.) 

### `U_le`

 With the empty list of checks, the number of all tests is at most (k − 1)·m, for ψ well formed
(`WfD`); as every test costs at most one bit, U ≤ 2(k − 1)·m. 

### `stSmall`

 Step 3, «The parameters», the case m ≤ n̄ as printed: for g > 0, the empty list of checks, ψ
well formed (`WfD`) with at most n̄ clauses, every variable in at most Δ of them, and an admissible
profile y, the
network of y satisfies conditions (i) and (ii) of the definition of a network with P = 2⌈n/g⌉(1 + Δ)
and B = 1, and U ≤ 2(k − 1)n̄. That the profile is admissible is not used. 
