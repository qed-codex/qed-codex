---
{
  "module": "proof/consequences/FreeCode/Behind.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Behind.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/FreeCode/Behind.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definition 6 with the code that does not depend on k: from a procedure on (n in unary, formula) to a Turing machine on codes

No sentence of the paper stands behind this file; the paper fixes no code and counts operations.
* `stBehindReader` (= `FreeCode.StBehindReader`): a procedure that decides w-SAT on (N in unary,
  formula), put behind any reader of the code, decides w-SAT on codes, within the same number of
  steps and the same sizes.
* `overhead_le`: for a k-CNF on n variables with code x, and states of size at most c·(n+2)^c, the
  factor (|x| + S + 1)^q of `SplitSat.Simulates` is at most a constant times a power of n + 2.
* `decidesTM_of_simulates`: if the machine decides w-SAT on codes with the exponent δ/2, every
  Turing machine that simulates it decides w-SAT within ⌊C·2^{δn}⌋ steps. The computation is that of
  `SplitSat.decidesTM_of_simulates`, for this code. 

### `stBehindReader`

 **For every reader and every procedure D** that decides w-SAT on (N in unary, formula) with the
exponent δ: D behind the reader decides w-SAT on the code, within the same number of steps. This is
the statement `FreeCode.StBehindReader`. 

### `decidesFree_mono`

 `DecidesFree Ms w δ c` stays true when δ and c are made larger. 

### `overhead_le`

 The factor of the simulation that is polynomial: for the code x of a k-CNF on n variables and S =
c·(n+2)^c, (|x| + S + 1)^q ≤ (2^k·(k+1) + 2 + c)^q·(n+2)^((k+1+c)·q). 

### `decidesTM_mono`

 A machine that decides k-SAT on codes in time t decides it in every larger time. 

### `decidesTM_of_simulates`

 If Ms decides w-SAT on codes with the exponent δ/2 and the constant c, and the Turing machine M
simulates Ms with polynomial overhead, then M decides w-SAT on codes within ⌊C·2^{δn}⌋ steps, for
some C ≥ c. 
