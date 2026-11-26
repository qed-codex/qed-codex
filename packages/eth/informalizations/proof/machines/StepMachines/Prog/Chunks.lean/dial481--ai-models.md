---
{
  "module": "proof/machines/StepMachines/Prog/Chunks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Chunks.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Prog/Chunks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Words (List Bool), counters, and cutting a word into chunks of given lengths.
sum_toWord: a sum over y < 2^ℓ of G(the ℓ-bit word of y) is the sum of G over all words of length ℓ.
sum_cut: a sum over all words of length Σ c i of F(the chunks) is the sum of F over all tuples of
words. 

### `toWord`

 The ℓ-bit word of y, lowest bit first. 

### `ofWord`

 The number written by a word, lowest bit first. 

### `words`

 All words of length ℓ. 

### `sum_toWord`

 A sum over the counter y < 2^ℓ is a sum over all words of length ℓ. 

 ### Cutting a word into chunks 

### `chunks`

 The chunks of lengths c₁, c₂, … of a word, as a list. 

### `cut`

 The chunks of a word, as a function: the indices in the list e get chunks of lengths c i, in
this order;
all other indices get d. 

### `glue`

 The inverse of cut: the words t i, i in e, one after the other. 

### `cut_eq_getD_beq`

 cut_eq_getD for any lawful ==, such as the one of a product type. 

### `sum_cut`

 A sum over all words of length Σ c i of F(the chunks) is the sum of F over all tuples of words.
e lists the indices i with P i, each once. 

### `sum_cut_toWord`

 sum_toWord followed by sum_cut: a sum over the counter y < 2^(Σ c i) of F(the chunks of the word
of y) is the sum
of F over all tuples of words. 

 ### Chunks of equal length, found by position 

### `block`

 The j-th block of ℓ bits of a word. 

### `sum_blocks`

 A sum over all words of r·ℓ bits of F(the blocks) is the sum of F over all tuples of words of ℓ
bits.
pos numbers the indices i with P i by 0, …, r-1. 

 ### Numbering the pairs a < b < K 

### `tri`

 The number of the pair a < b: pairs are listed by b, then by a. 

### `sum_blocks_pairs`

 A sum over all words of K(K-1)/2 · ℓ bits is a sum over all labellings of the pairs a < b in Fin
K. 
