---
{
  "module": "proof/rates/PaddedDescent/F/RebalG.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/RebalG.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/RebalG.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The rebalancing with a given label length

`rebalG` is `rebalF` with the label length β of the new instance as an argument and the test `goodG`
in place of `goodB`. `rebalG_spec` is the value statement, the
analogue of `RebalF.stR` for `goodG`, with the existence of a good colouring as a hypothesis; `stRG`
gets that from `exists_goodG` and is the interface statement `StRG`. 

### `rebalG_spec`

 The rebalancing with a given label length β: if some colouring below K^g is good for β and the
pad is long enough, `rebalG` returns an explicit instance on K nodes
with labels of β bits and the value of the network. 

### `pos_of_colOK`

 From `ColOK K g` and K ≥ 1: g is positive. 

### `stRG`

 The interface statement `StRG`: under `ColOK K g`, `exists_goodG` supplies a colouring below K^g
that is good for β, and `rebalG_spec` then gives the rebalanced instance and its value. 
