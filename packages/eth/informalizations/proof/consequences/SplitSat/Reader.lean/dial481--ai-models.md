---
{
  "module": "proof/consequences/SplitSat/Reader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Reader.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SplitSat/Reader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 5: the reduction on the code of a k-CNF

No sentence of the paper stands behind this file: the paper does not fix a code of formulas as
words. `REDUCE k τ D` is the reader `CountKSat.decU k` followed by `reduceCore`. The reader turns
the code `SatK.enc k φ` of a k-CNF on n variables into (n in unary, φ with numbers as variables)
(`CountKSat.stDecU`).
The code has at least n + 1 bits, so a bound c·(n+2)^c on the sizes of the states is a bound
c·(length of the code + 1)^c. `stReduce` proves `SplitSat.StReduce` from `stReduceCore`. 

### `decides_of_decidesW`

 A machine that decides k-SAT on (n in unary, formula), in the sense of `DecidesW k`, decides
k-SAT on codes, in the sense of `Eight.ViaGrouping.Decides`, when the reader `decU k` is put in
front of it; the exponent and the constant stay. 

### `stReduce`

 The reduction with the reader of the input in front decides k-SAT with the exponent δ, for every
procedure D: the statement `SplitSat.StReduce`. 
