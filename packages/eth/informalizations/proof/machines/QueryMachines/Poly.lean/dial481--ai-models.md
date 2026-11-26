---
{
  "module": "proof/machines/QueryMachines/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Polynomial-time steps
`IsPolyQ` (proof/machines/QueryMachines/Kernel.lean) is kept by the constructions of
proof/machines/QueryMachines/CombDefs.lean and by `subst`; `IsPolyT` by `plug` and `close`, and it
holds for the step machine underneath a machine with `IsPolyQ`.
The fields init, step, out say that the start, one step and the read-out of the step machine
underneath are polynomial-time, as for `IsPolyT` (proof/machines/ToTuring/Poly); `ask` and `resume`
say that asking a query and taking in its answer are polynomial-time. 

### `under`

 The step machine underneath has polynomial-time steps. 

### `lift`

 A step machine with polynomial-time steps, seen as a machine that asks nothing. 

### `query`

 A single query, if the query is computed in polynomial time from the input. 

### `mapAsk`

 Queries rewritten by a polynomial-time function. 

### `mapIn`

 A polynomial-time function applied to the input. 

### `mapOut`

 A polynomial-time function applied to the result. 

### `bind`

 One machine after the other. 

### `foldWhile`

 The loop, if its body has polynomial-time steps and `start`, `nxt`, `g`, `c₀` are
polynomial-time. 

### `branch`

 A choice between two machines by a polynomial-time function of the input. 

### `both`

 Two machines on one input. 

 ## Constructions made from the ones above 

### `ite`

 A choice by a polynomial-time test. 

### `const`

 A constant. 

### `optBind`

 `optBind`, if the default is polynomial-time. 

### `foldRange`

 The loop over a range, if the range, `g` and `c₀` are polynomial-time. 

### `sumRange`

 The sum over a range. 

### `prodRange`

 The product over a range. 

### `gated`

 A machine behind a test. 

 ## The three ways to answer the queries 

### `ofOption_isPolyT`

 One step that looks a value up, if the look-up is polynomial-time. 

### `close_isPolyT`

 The oracle built in, if it is computed in polynomial time from the query. 

### `plug_step_poly`

 The step of `plug` is polynomial-time. 

### `plug_isPolyT`

 Queries answered by a step machine with polynomial-time steps. 

### `subst_isPolyQ`

 Queries answered by a machine with query access and polynomial-time steps. 

### `stPolyPlug`

 `StPolyPlug` holds: `plug` of a machine with query access and polynomial-time steps and a step
machine with polynomial-time steps has polynomial-time steps. 

### `stPolySubst`

 `StPolySubst` holds: queries answered by a machine with query access and polynomial-time steps
give a machine with query access and polynomial-time steps. 

### `stPolyClose`

 `StPolyClose` holds: a machine with query access and polynomial-time steps, with an oracle built
in that is computed in polynomial time from the query, has polynomial-time steps. 
