---
{
  "module": "proof/threesat/Printed/CodingDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/CodingDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/CodingDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Between Definition 3's tables and the tables of this development (definitions and statements only)

Definition 3 writes a setting z_w as ONE string of (K − 1)λ bits; the programs and theorems of this
development write it as the list of K strings with the empty string at w (`Paper.Tables`,
`Groundwork.Prog.ServesInst`). These three statements carry everything across; the files on
Definition 4, Lemma 1 and Proposition 3 use them and nothing else about the coding.
This file has no proofs. 

### `listTables`

 Tables as Definition 3 has them (argument: one string), read as tables of this development
(argument: one string for every node, the empty string at w itself): the strings are concatenated. 

### `StAskServes`

 The query machine `askTable`, closed over the tables `tables K lam W`, is a procedure that
answers every well-formed query of this development in ONE step. 

### `StCliqueValue`

 The value of the clique as the network of Definition 3 is the sum over one string per edge for
the tables read as lists of strings (`listTables`). 

### `StToLists`

 Cutting a setting into its strings: the query (w, z) of Definition 3 becomes the query with the
strings z_w(w') used here; and concatenating them gives z back. 
