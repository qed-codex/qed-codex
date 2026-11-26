---
{
  "module": "proof/consequences/FreeCode/Random.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Random.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Random.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # After Definition 6: «A deterministic algorithm is a randomized algorithm that uses no random bits, so allowing randomness can only make s_k smaller»

The statements are in KSatFreeCodeStatement.lean.
* `deterministicIsRandomized`: a machine that decides k-SAT in time t is a randomized algorithm with
  no random bits and no error. There is one string of no bits; on it the input is the code alone.
* `inTimeRand_of_inTime`: so «in time O(2^{δn})» passes from deterministic to randomized algorithms
  with any error p ≥ 0: the same machine and constant, and ⌊0·2^{0·n}⌋ = 0 random bits.
* `randomnessHelps`: «so allowing randomness can only make s_k smaller».
«and Corollary 5 holds under each of these conventions» is in proof/consequences/FreeCode/Main.lean. 

### `noBits`

 With no random bits the input is the code alone: if M halts on the word x with the bit b within
t steps, it does so for every string of no bits behind x, and the number of such strings, 1, is at
least (1 − 0)·2^0. 

### `deterministicIsRandomized`

 «A deterministic algorithm is a randomized algorithm that uses no random bits»: a machine that
decides k-SAT in time t is a randomized algorithm with no random bits and no error. 

### `decidesRandTM_mono`

 An algorithm with error at most p has error at most p', if p ≤ p'. 

### `inTimeRand_of_inTime`

 If a deterministic algorithm decides k-SAT in time O(2^{δn}), so does a randomized algorithm
with error at most p, for every p ≥ 0: the same machine, with no random bits. 

### `randomnessHelps`

 «so allowing randomness can only make s_k smaller». 
