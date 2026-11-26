---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Ev.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Ev.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Ev.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One evaluation is exact

`stEvW : StEvW`, from the interface statements on the network of marks (its value, the sum over the
profiles, that the programs present it, its size) and on the evaluation of any network on
3K⁸ nodes through a clique solver. One evaluation `evW` is the sum over the admissible profiles of a
weight times the number that the solver returns for the network of marks of the profile. The
solver returns the value of that network, because the size of the network is at most `PbOL` and its
total at most `UbOL` (`StMarkSized`; the two bounds grow with the number of variables, the cap
and the number of layers, which are at most 7n, 11n and 3) and the pad is long enough (`StValS`).
Then `ClauseBound.TopN.EvalW.evalV_truncW_ctx` gives the product form `truncW`. 

### `length_rep`

 The length of n in unary. 

### `Ub_mono`

 The bound for the total of the network of marks grows with the number of variables, the cap and
the number of layers. 

### `Pb_mono`

 The bound for the size of the network of marks grows with the number of variables. 

### `sized_mono`

 A network of size P is a network of every larger size. 

### `evalV_valS`

 One evaluation is exact; the numbers of nodes and of variables, the cap and the two code
parameters are the lengths of any lists of units, and U₀ and P₀ are any bounds for the total and the
size of the networks. 

### `stEvW`

 One evaluation is exact on three layers (or two) of clauses of 1 to k + 1 literals on n + r
variables in which no variable occurs too often. 
