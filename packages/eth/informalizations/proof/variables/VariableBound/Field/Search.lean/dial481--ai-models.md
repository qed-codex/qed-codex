---
{
  "module": "proof/variables/VariableBound/Field/Search.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Search.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Search.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «An irreducible polynomial of degree s is found by search» (proof of Lemma 13, Appendix D)

The programs of Defs.lean compute in the ring `FW g` of residues modulo X^s + g (`decW_xorW`,
`decW_mulW`, `decW_powW`). The test `irrW g`, «every word other than 0 has an inverse», holds
exactly if
X^s + g is irreducible (`irrW_iff`). `modW s` is found by a search with this test over the words of
s bits; as an irreducible polynomial of every degree s ≥ 1 exists, it has s bits and X^s + `modW s`
is irreducible (`modW_spec`). 

 ### The programs compute in the ring of residues 

### `decW_xorW`

 `xorW` is the sum of residues, for words of the same length. 

### `decW_zeroW`

 The word 0 stands for the residue 0. 

### `decW_oneW`

 The word 1 stands for the residue 1. 

### `decW_mulW`

 `mulW g` is the product of residues, for a word x as long as g and any word y. 

### `decW_powW`

 `powW g` is the power of residues, for g not empty and any word u. 

 ### The test 

### `irrW_eq_true`

 What the test says: every word x as long as g is the word 0 or has a word y as long as g with
x·y = 1. 

### `irrW_iff`

 For a word g of s ≥ 1 bits, the test holds exactly if X^s + g is irreducible. 

 ### The search 

### `modW_spec`

 For s ≥ 1 the search succeeds: `modW s` is a word of s bits, and X^s + `modW s` is irreducible. 
