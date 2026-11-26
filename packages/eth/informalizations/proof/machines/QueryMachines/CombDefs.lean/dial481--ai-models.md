---
{
  "module": "proof/machines/QueryMachines/CombDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/CombDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Building machines with query access (definitions only)

Every way to build step machines that the algorithms of the main text use
(proof/machines/StepMachines/Prog/Stepped.lean, Comb.lean, Range.lean; `gated` of
proof/networks/Eight/SecNetworks_LemGrouping.lean) is repeated here for machines with query access
(`QueryMachines.QueryMachine`, proof/machines/QueryMachines/Kernel.lean).
In each case the step machine underneath IS the construction for step machines, applied to the
parts' step machines; added is how `ask` and `resume` pass on to the running part.
`lift` (asks nothing) and `query` (asks one query) have no counterpart for step machines. That
building in the oracle (`close`) commutes with every construction is proved in
proof/machines/QueryMachines/Comb.lean. This file has no proofs. 

### `ofOption`

 One step: the value g a, if there is one; if there is none the machine stays where it is and
never halts. (This is what a single query becomes when the oracle is built in.) 

 ## The constructions 

### `lift`

 A step machine: it asks nothing. 

### `query`

 Ask the query h a and return the answer. No step of its own. 

### `mapAsk`

 The same machine with every query x written as h x. 

### `mapIn`

 M on g a. 

### `mapOut`

 g applied to the result of M. 

### `bind`

 M, then N on the input together with the result of M. 

### `foldWhile`

 The loop of `Stepped.foldWhile` with a body that may ask. 

### `branch`

 M₁ on x if sel a = inl x, M₂ on y if sel a = inr y. 

### `both`

 M, then N, on the same input; both results. 

 ## Made from these, as for step machines 

### `ite`

 M if p a, else N. 

### `const`

 The result b; one step. 

### `optBind`

 M; if its result is some i, then N on (a, i); if none, then dflt a. 

### `foldRange`

 The loop over y = 0, 1, …, N a − 1. 

### `sumRange`

 Σ_{y < N a} M(a, y). 

### `prodRange`

 ∏_{y < N a} M(a, y). 

### `gated`

 [M says yes]·N: first the test M; if it says yes, N; else 0. 
