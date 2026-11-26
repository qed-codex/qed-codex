---
{
  "module": "proof/consequences/Consequences/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Consequences/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a machine cut into steps that computes a number from a graph to a Turing machine of Mathlib, and a lemma on binary words

* `tm_of_counts`: a machine cut into polynomial-time steps that returns a number computed from a
  graph within c·2^{(δ/2)n} steps is simulated by a Turing machine of Mathlib that writes `post` of
  the number, for a polynomial-time `post`, within ⌊C·2^{δn}⌋ steps: the host theorem of
  proof/consequences/GraphProblems/, `GraphProblems.tm_of_stepped`.
* `ofWord_binary_lt`: a number below 2^(N+1), written in N + 1 bits and read back, is itself. 

### `tm_of_counts`

 From a machine cut into polynomial-time steps that returns f(G, s) within c·2^{(δ/2)n} steps to
a Turing machine with finite alphabets that, started on the code of (G, s), s ≤ n, halts with
`post (f n G s)` within ⌊C·2^{δn}⌋ steps, for every polynomial-time `post` from numbers to words. 

### `ofWord_binary_lt`

 A number below 2^(N+1), written in N + 1 bits and read back, is itself. 
