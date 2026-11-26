---
{
  "module": "proof/rates/ClauseBound/Inst/HalfIfc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfIfc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfIfc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The pieces with ρ = 1/√2 as programs: the interface lemmas, as propositions

Definitions `St… : Prop`; nothing is proved and nothing is assumed here. One file proves
`theorem … : St…`; the file that needs such a lemma takes `(h : St…)` as a hypothesis, and the final
assembly feeds the proofs in. Throughout, h is the least number ≥ 2 with p(h) ≥ 2^λ, the table is
that of all partitions of 0, …, 4h, and |s| ≤ 2h. 

### `ell`

 The list of the parts of the partition of h that the string x stands for. 

### `valK`

 The value, as an entry of the matrix of an operator, of one of the two functions of a
factorization at the label that stands for the pair p = (j, τ); α and β are the lists of the two
strings. 

### `StWords`

 A sum over all words of c bits of a product of two functions of the entry of a list with at most
2^c entries is the sum over the list. 

### `StLabs`

 The list of the labels: its length, sums over it, its members. 

### `StEnc`

 The encoding: a string stands for a listed partition of h, and different strings for different
partitions. 

### `StVal`

 The values: with a pad that is long enough, the program returns the entry of the matrix at the
pair that the label stands for, and 0 if the label stands for no pair. 

### `Cst`

 What the two constants have to satisfy at the length λ. 

### `StFact`

 The two factorizations of the piece number i < 4h + 1, by the two programs. 

### `StSpec`

 The specification of the pieces at every length at which the two constants satisfy `Cst`. 
