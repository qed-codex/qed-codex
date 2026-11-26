---
{
  "module": "Paper/Transfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Transfer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Transfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, appendices A and B: constants in KK


### `lem_transfer`

 **Paper: Lemma lem:transfer.** "Let a polynomial with integer coefficients have a circuit with S gates over a field
of characteristic p. It has one with S gates over KK." Here KK is any algebraically closed field of that
characteristic. 

### `lem_transfer_approx`

 **Paper: Lemma lem:transfer-approx.** "An approximating circuit for a polynomial with integer coefficients, over a
field of characteristic p, gives one of the same size with constants in KK[ε,ε⁻¹] and output in f + εKK[ε][x]": the
constants are cut off, and the argument of Lemma lem:transfer is applied to their coefficients. 
