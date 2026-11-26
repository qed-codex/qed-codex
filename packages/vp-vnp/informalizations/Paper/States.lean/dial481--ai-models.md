---
{
  "module": "Paper/States.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/States.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/States.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Two crossing wires": states


### `stateCount`

 The number P(E) of states of energy at most E. 

### `mem_states`

 "A state is a pair (I, J) of finite subsets of ℕ = {0, 1, …} with |I| = |J|; this number is its size, and its energy is
∑_{i∈I} (2i+1) + ∑_{j∈J} (2j+1)." The theorem says which pairs are counted by P(E): the states of energy at most E. 

### `lem_count_interleave`

 Proof of Lemma lem:count: "Interleave k states: put ki+r into I for i ∈ I_r, and kj+k−1−r into J for j ∈ J_r. This is
injective and multiplies the total energy by k, so P(k²E) ≥ P(E)^k." 

### `lem_count_sets`

 Proof of Lemma lem:count: "Let 0 < t < 1. The number of sets S with ∑_{i∈S} (2i+1) ≤ E is at most
t^(−E) ∏_i (1 + t^(2i+1)) ≤ t^(−E) e^(1/(1−t))." 

### `lem_count_upper`

 Proof of Lemma lem:count: "as a state is a pair of such sets, 1 − t = 1/(2√E) gives ln P(E) ≤ 10√E for E ≥ 1." 

### `lem_count`

 **Paper: Lemma lem:count.** "There is κ > 0 with ln P(E) ≤ κ√E for all E and ln P(E) ≥ (κ − o(1))√E for E → ∞." 
