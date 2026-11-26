---
{
  "module": "proof/consequences/SplitCount/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitCount/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The steps of the procedure of proof/consequences/SplitCount/ are polynomial time

A bound on the number of steps of a machine cut into steps says something only if each step takes
polynomial time (`PolyTimeSteps`). Here: the functions `stepPlain step`, `rootPlain`, `leafPlain`
are polynomial-time; `timesFreeAfter Cnt` has polynomial-time steps if Cnt has (the factor 2^{n'}:
`Occ.stTimesFreeCert`);
`engineBy step D` has them if `step` is polynomial-time and D has them (the width reduction:
`Eight.Width.widthP_polyT`; the walk that adds up: `CountKSat.isPolyT_walkSum`). The proof follows
`GraphProblems.isPolyT_engine` (proof/consequences/GraphProblems/Engine.lean). 

### `stepPlain_polyT`

 The step of the tree with n handed down is polynomial-time if the step of the tree is. 

### `rootPlain_polyT`

 The root with the empty side list is computed in polynomial time. 

### `leafPlain_polyT`

 What is counted at a node is computed in polynomial time. 

### `stCert`

 The steps of `timesFreeAfter Cnt` are polynomial time if those of Cnt are; the steps of
`engineBy step D` are polynomial time if `step` is polynomial-time and the steps of D are polynomial
time. 
