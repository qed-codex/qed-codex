---
{
  "module": "proof/consequences/SplitSat/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: the steps of the reduction are polynomial time

No sentence of the paper stands behind this file; the paper counts operations. `stReduceCert` proves
`SplitSat.StReduceCert`. The proof follows `Groundwork.Prog.SatTopK.isPolyT_satMK`
(proof/consequences/WidthK/Top/Poly.lean). Its pieces: splitting the long clauses is polynomial time
(`Eight.Width.widthP_polyT`), one step of the tree is (`WidthK.Prog.certStep`), the reader of the
input is (`CountKSat.stCertDecU`). 

### `stepN_polyT`

 The step of the tree with n carried along is polynomial time if the step of the tree is. 

### `reduceCore_polyTimeSteps`

 The steps of the reduction without its reader are polynomial time, if the step of the tree is
polynomial time and the steps of D are. 

### `stReduceCert`

 The steps of the reduction are polynomial time if those of D are: the statement
`SplitSat.StReduceCert`. 
