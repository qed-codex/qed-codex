---
{
  "module": "proof/rates/ClauseBound/Alg/Descend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Descend.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Descend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemmas for the descent through all levels

`descendG P pad sched I` starts from the state «sum 0, factor 1, work list [I]» and applies the
steps of the schedule. A step multiplies the sum and the factor by the factor d^R of its
level, adds the terms that are evaluated at once, and replaces every instance of the work list by
its children. `solveG` evaluates the instances that are left by brute force, adds
the sum, and divides by the factor. This file holds lemmas for the bookkeeping of these steps: two
facts on sums over lists, a bound on the length of the word of a state
(whose first budget in `FitsG` says that the current state fits under the pad), and bounds on the
sizes of the sum and of the factor after a step.


 ### Lists 

### `natAbs_sum_map_le`

 A sum of k integers of absolute value at most c has absolute value at most k·c. 

### `sum_fst_add_sum_snd`

 If D·Z(a) is the first component of e(a) plus the sum of z over the second, for every member a
of w, then D times the sum of Z over w is the sum of all first components
plus the sum of z over all second components. 

 ### The length of the word of a state 

### `fitsG_head`

 The first budget of `FitsG`: the current state fits under the pad. 

### `len_state_le`

 The word of a state with at most cnt well-formed instances, and a sum and a factor below 2^z. 

 ### The sizes of the sum and of the factor after a step 

### `pow_le_two_pow_size`

 d^R ≤ 2^(R · number of binary digits of d). 

### `two_pow_size_le`

 2^(number of binary digits of n) ≤ 2n for n ≥ 1. 

### `factor_lt`

 The factor after a step. 

### `sum_lt`

 The sum after a step: the old sum a times D, plus b, the sum of at most cnt terms below
2^(digits of n + E). 
