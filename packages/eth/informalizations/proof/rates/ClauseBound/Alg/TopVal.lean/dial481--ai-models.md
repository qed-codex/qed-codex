---
{
  "module": "proof/rates/ClauseBound/Alg/TopVal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/TopVal.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/TopVal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top level in m: correctness

Two statements of `proof/rates/ClauseBound/Alg/Interfaces.lean` and
`proof/rates/ClauseBound/Alg/Top.lean`. (1) The plain functions `satFk`, with the number g of nodes
and the width k in the context, present the
network of a formula (`stSatPresentsK`). (2) The function `AM` returns the number of satisfying
assignments of a k-CNF all of whose variables occur, as n + 1 bits, if the pad has length at
least 2^eM (`stCorrectM`), under the hypothesis that this network on 3K⁸ nodes, rebalanced to K
nodes with labels of `lamTopK` bits and handed to a correct clique solver, gives its value if the
pad has length at least 2^needTop;
`AM` counts exhaustively when that needs a pad at most as long as the clique solver's. The text
followed is the paper's network of a formula (Section 6) and the proof of part (c) of Theorem A. 

### `stSatPresentsK`

 The plain functions satFk, in the context ((g, k) in unary, ψ), present the network of ψ on g
nodes at width k. 

### `needTopC_eq`

 What the computation under a bound returns is the exponent needTop. 

### `stCorrectM`

 The function AM returns the number of satisfying assignments, as n + 1 bits, if the pad has
length at least 2^eM. 
