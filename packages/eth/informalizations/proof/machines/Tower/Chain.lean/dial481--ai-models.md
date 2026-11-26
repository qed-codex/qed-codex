---
{
  "module": "proof/machines/Tower/Chain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Chain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Chain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The tower as a machine that calls itself: what its activations compute

Fix an outermost instance (c0, f0) and the cost tq of a query to its tables. An activation carries
the list env of the contexts through which its table queries run up. `tabs env` are the tables that
these queries see, `parent env` is the
context of the instance that owns them, `Chain env` says that every context of env is a permitted
call of the one below it, `price env` is what a query to `tabs env` costs. With these, `nGood`,
`nval`, `ndep`, `nT` are the good
inputs, the values, the depths and the costs for `SelfCallRuns`. 

### `tabs`

 The tables seen by queries that run up through env. 

### `parent`

 The context of the instance that owns these tables. 

### `Chain`

 Every context of env is a permitted call of the instance below it. 

### `price`

 The cost of a query to `tabs env`. 

### `callCost`

 The price of a call made at depth l, if a query to the tables of the caller costs t. 

### `cost_eq`

 The cost of the tower at depth l is the cost of the solver with the price of a call made at
depth l. 

### `nGood`

 The good inputs. 

### `nval`

 The values. (Where an entry is missing: some element of A.) 

### `ndep`

 The depths. 

### `nT`

 The costs. 

### `callOracle_call`

 A call of a good input of smaller depth is answered by its value. 

### `chain_facts`

 Along a chain: the instance is well formed, the depths add up, the list is small. 

### `up_ok`

 A query y that runs up through env, asked by the activation x: it has the answer that `tabs env`
or gl gives, at the price `price env` or wg. 
