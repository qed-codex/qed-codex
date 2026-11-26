---
{
  "module": "Paper/Postpone.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Postpone.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Postpone.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales": constants are postponed


### `postponed`

 The instance z_e of the paper: run p on the argument and accept exactly the runs whose bill uses each name the
prescribed number of times. 

### `lem_postpone`

 **Paper: Lemma lem:postpone.** "Let all runs of a program p on an argument halt, the accepting ones within T < 2^J
steps and with names among the leaves of a binary trie with Q′ nodes and height η; let its leaves stand for powers
λ_1, λ_2, … Its value is ∑_e λ^e sum(z_e) over the vectors e with one entry in {0, …, 2^J−1} for every leaf, where the
instance z_e accepts exactly the runs of p whose bill uses each name the prescribed number of times. It is plain within
O(T(J + η + 1) + Q′J) steps, and its size is that of p and the argument plus O(Q′J)." The trie is L and L.budg J lists
the exponent vectors e with their λ^e. "Accepts exactly": the accepting runs of z_e, in their order, are those of p with ok e bill (every counter of e is 0
after the bill), with the same weights; pv(z_e) is therefore the sum of these weights. 
