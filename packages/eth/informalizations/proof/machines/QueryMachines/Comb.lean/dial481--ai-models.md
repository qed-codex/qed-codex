---
{
  "module": "proof/machines/QueryMachines/Comb.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Comb.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Comb.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Building in the oracle commutes with every construction

The lemmas `close_…` say that building in the oracle (`close`) commutes with every construction of
proof/machines/QueryMachines/CombDefs.lean. So a machine built there, with the oracle built in, is
the step machine built in the same way from the parts with the oracle built in; and every bound
proved for such step machines is a bound on own steps plus queries (`StClose`). 

### `ofOption_runs`

 Where g has a value, `ofOption g` returns it in one step. 

### `close_lift`

 A step machine stays what it is. 

### `close_query`

 A single query becomes one step that looks the answer up. 

### `close_mapAsk`

 Rewriting the queries is rewriting the oracle. 

### `close_mapIn`

 `close` commutes with `mapIn`. 

### `close_mapOut`

 `close` commutes with `mapOut`. 

### `close_bind`

 `close` commutes with `bind`. 

### `close_foldWhile`

 `close` commutes with the loop. 

### `close_branch`

 `close` commutes with `branch`. 

### `close_both`

 `close` commutes with `both`. 

### `close_ite`

 `close` commutes with `ite`. 

### `close_const`

 A constant stays what it is. 

### `close_optBind`

 `close` commutes with `optBind`. 

### `close_foldRange`

 `close` commutes with `foldRange`. 

### `close_sumRange`

 `close` commutes with `sumRange`. 

### `close_prodRange`

 `close` commutes with `prodRange`. 

### `close_gated`

 `close` commutes with `gated`. 
