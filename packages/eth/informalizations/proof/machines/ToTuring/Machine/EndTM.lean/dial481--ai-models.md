---
{
  "module": "proof/machines/ToTuring/Machine/EndTM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/EndTM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Machine/EndTM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 From step counts to a Turing machine, last part. A machine cut into polynomial-time steps
(`Stepped`, `IsPolyT`) that
decides 3-SAT within c·2^{(δ/2)n} steps, with states of polynomial size, gives a Turing machine of
Mathlib that decides
3-SAT within O(2^{δn}) steps (`InTimeTM δ`). The host of Machine/Host.lean needs (number of steps + 1)
· (a
polynomial in the length of the input) steps of its own. That length is polynomial in n, so
`exists_pow_le` bounds the second
factor by a constant times 2^{(δ/2)n}. 

### `exists_pow_le`

 A polynomial is below every exponential, up to a constant. 

### `inTimeTM_of_machine`

 Take a machine cut into polynomial-time steps that decides 3-SAT in at most c·2^{δn/2} steps,
with every state of size at
most c·(|input|+1)^c. It gives a Turing machine with finite alphabets that decides 3-SAT within
⌊C·2^{δn}⌋ steps, which is
`InTimeTM δ`. 
