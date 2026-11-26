---
{
  "module": "proof/consequences/FreeCode/Order.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Order.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Order.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # After Definition 6: «A k-CNF is also a (k+1)-CNF, so s_k ≤ s_{k+1}. Hence s_∞ = lim_{k→∞} s_k, and ETH is the same as s_3 > 0.»

The sentences are quoted from the paper; the statements are in KSatFreeCodeStatement.lean.
* `sameMachine`, `increasing`: «A k-CNF is also a (k+1)-CNF, so s_k ≤ s_{k+1}». A machine that
  decides (k+1)-SAT decides k-SAT in the same time, because the code does not depend on k; so the
  infimum for k is taken over more numbers δ.
* `henceForEverySequence`: the paper's «Hence», for every nondecreasing sequence in [0, ∞].
* `limitAndEth`: «Hence s_∞ = lim_{k→∞} s_k, and ETH is the same as s_3 > 0», from the two before.
* `supOneGivesPositive`, `sethGivesSomeK`: in the proof of Corollary 5, «s_∞ = 1 gives s_k > 0 for
  some k».
None of these proofs uses that the numbers s_k are 0. 

### `sameMachine`

 «A k-CNF is also a (k+1)-CNF»: a machine that decides (k+1)-SAT decides k-SAT, in the same time. 

### `increasing`

 «so s_k ≤ s_{k+1}.» 

### `henceForEverySequence`

 The paper's «Hence», for every nondecreasing sequence u in [0, ∞]: it tends to sup_{k≥3} u_k,
and u_k > 0 for all k ≥ 3 exactly if u_3 > 0. 

### `limitAndEth`

 «Hence s_∞ = lim_{k→∞} s_k, and ETH is the same as s_3 > 0.» 

### `supOneGivesPositive`

 For every sequence u in [0, ∞]: if sup_{k≥3} u_k = 1 then u_k > 0 for some k ≥ 3. 

### `sethGivesSomeK`

 «s_∞ = 1 gives s_k > 0 for some k». 
