---
{
  "module": "proof/consequences/GraphProblems/Engine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Engine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Engine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The counting engine

The machine for #k-SAT of proof/consequences/CountKSat/ is `Stepped.mapIn dU (…)`: a reader `dU` of
the input word, followed by a machine cut into steps whose input is the pair (N in unary, formula
with natural
numbers as variables). This file takes that second machine out (`engine`) and shows that it is
polynomial-time when its parts are (`isPolyT_engine`). It also holds `reaches_of_mapIn`
and `runs_of_mapIn`, which turn a run of `Stepped.mapIn f M` into a run of `M`, and `exists_toN`,
which writes a formula whose variables are below N as `Decode.toN φ` for a formula φ
on N variables. With these, a reduction to #k-SAT only has to produce the pair (N in unary,
formula). 

### `engine`

 The counting machine of `proof/consequences/CountKSat/Defs.lean` without its reader. 

### `reaches_of_mapIn`

 The converse of `Stepped.mapIn_runs`. 

### `isPolyT_engine`

 The engine is `IsPolyT` if `step` is polynomial-time and M is `IsPolyT`. This is
`CountKSat.Poly.isPolyT_countMK` without its last line. 

### `exists_toN`

 A formula whose variables are below N is `toN φ` for a formula φ on N variables. 
