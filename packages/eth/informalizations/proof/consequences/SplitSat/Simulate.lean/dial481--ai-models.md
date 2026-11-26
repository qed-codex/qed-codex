---
{
  "module": "proof/consequences/SplitSat/Simulate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Simulate.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Simulate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: from steps to time

No sentence of the paper stands behind this file; the paper counts operations. `exists_simulates`: a
machine cut into polynomial-time steps, with a bit as result, is simulated by a Turing machine of
Mathlib with finite alphabets, in the sense of `SplitSat.Simulates`: the overhead is
q·(T+1)·(|x|+S+1)^q.
This is the host for a word as output (`CountKSat.stHostW`) on the machine that returns its bit as a
word of one bit.
`decidesTM_of_simulates`: if the machine decides k-SAT with the exponent δ/2, every Turing machine
that simulates it decides k-SAT within ⌊C·2^{δn}⌋ steps. The code of an instance has length below
(k·2^k+1)·(n+2)^(k+1), so the overhead is a polynomial in n, which is at most a constant times
2^{(δ/2)n}. 

### `decides_mono`

 `Decides M k δ c` stays true when δ and c are made larger. 

### `exists_simulates`

 A machine cut into polynomial-time steps, from words to a bit, is simulated with polynomial
overhead by a Turing machine of Mathlib with finite alphabets. 

### `decidesTM_of_simulates`

 If Ms decides k-SAT with the exponent δ/2 and the constant c, and the Turing machine M simulates
Ms with polynomial overhead, then M decides k-SAT within ⌊C·2^{δn}⌋ steps, for some C ≥ c. 
