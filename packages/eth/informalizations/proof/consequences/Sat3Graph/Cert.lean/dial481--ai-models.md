---
{
  "module": "proof/consequences/Sat3Graph/Cert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Cert.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Sat3Graph/Cert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, Corollary 7: polynomial-time steps

Proof of `StCert` of proof/consequences/Sat3Graph/Defs.lean. The paper does not say this; it is what
makes a number of steps a time. Reading the input, writing Γ, striking out repeated clauses and
splitting long clauses are polynomial time, and so are the step, the root and the leaf of the tree
for Dominating Set (`GraphProblems.stCertDom`).
The certificates of the readers for cliques and vertex covers (`Complement.StReadersCert`) and of
the formula for independent sets (`Complement.StIndepAlone`) are hypotheses here; Main.lean puts
their proofs in. That the formula of the colorings is computed in polynomial time is proved here on
its own: proof/consequences/GraphProblems/ proves it only inside `GraphProblems.StCertForm`,
together with the same fact for its formulas for cliques and vertex covers. 

### `askSized_polyTimeSteps`

 The steps of `askSized gates D` are polynomial time if those of D are and the circuits are
computed in polynomial time. 

### `colorF_polyT`

 The formula of the colorings is computed in polynomial time from (n in unary, matrix). 

### `readC_behind_polyT`

 Behind a polynomial-time reader r of (n in unary, matrix), the reader for colorings is
polynomial time. 

### `readC_polyT_alone`

 The reader for colorings is polynomial time. 

### `stCert_of`

 **`StCert`**, from the certificates of the readers for cliques and vertex covers and of the
formula for independent sets: the steps of the five deciders are polynomial time if those of D are
and the circuits are computed in polynomial time. 
