---
{
  "module": "proof/machines/ToTuring/Poly/Comb.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Comb.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Comb.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `IsPolyT` (start, step and output of a stepped computation are polynomial-time) is closed under
combinators of
StepMachines/Prog/Comb.lean, such as `branch`, `ite`, `const` and `optBind`. 

### `branch`

 The machine that runs `M₁` or `M₂`, as a polynomial-time `sel` decides from the input, is
`IsPolyT`. 

### `ite`

 The choice between `M` and `N` by a polynomial-time test `p` of the input is `IsPolyT`. 

### `const`

 The machine that always returns `b` is `IsPolyT`. 

### `optBind`

 Run `M`; on `some i` run `N` on the input paired with `i`, on `none` return the polynomial-time
`dflt` of the input.
This is `IsPolyT`. 

### `both`

 Running `M` and then `N` on the same input, and returning the pair of their outputs, is
`IsPolyT`. 

### `map2`

 Combining the outputs of `M` and `N` on the same input by a polynomial-time `f` is `IsPolyT`. 

### `mul2`

 The product of the integer outputs of `M` and `N` on the same input is `IsPolyT`. 
