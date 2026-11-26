---
{
  "module": "proof/consequences/SplitCount/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The time of a Turing machine that simulates a machine cut into steps

Let M be a machine cut into steps that writes the number of satisfying assignments of a k-CNF on n
variables within c·2^{(δ/2)n} steps, on states of size polynomial in the length of the input, and
let N be a Turing machine that simulates M with the overhead q·(T+1)·(|x|+S+1)^q. The length of the
input is polynomial in n, so N counts within ⌊C·2^{δn}⌋ steps: `counts_of_simulation`.
Here the Turing machine is the given one, and not only some Turing machine that exists, so that the
statement `StTiedTM` can tie it to M. 

### `counts_of_simulation`

 If N simulates M with the overhead q·(T+1)·(|x|+S+1)^q, the code of a k-CNF on n variables has
length + 1 at most a·(n+2)^d, and M writes the number of satisfying assignments within c·2^{(δ/2)n}
steps on states of size at most c·(length + 1)^c, then N counts the satisfying assignments of k-CNFs
within ⌊C·2^{δn}⌋ steps, for some C. 
