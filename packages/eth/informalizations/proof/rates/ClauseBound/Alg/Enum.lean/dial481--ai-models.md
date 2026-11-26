---
{
  "module": "proof/rates/ClauseBound/Alg/Enum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Enum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Enum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A network evaluated by enumeration of its labels

Replacing every Ψ_jj' by its factorization gives Z_ι = Σ_θ ∏_j Σ_{z_j} W_j(z_j) ∏_{j' ≠ j}
f_jj'(z_j, θ_jj'), where θ consists of one string
θ_jj' = θ_j'j for each pair. `value_eq_sum_labels` is this identity for any network. `stEnum` says
that the function `enumF`, which runs through all θ written as one
word of U/2 bits, returns the value of the network N that the functions of `F` (its tables W and f
and the lengths n and cap) present, if the pad is at least as long as the number of these words and
as the number of
states of every node. 

 ### The identity 

### `value_eq_sum_labels`

 The value of a network is the sum, over all choices t of a label for every pair, of the product
over the nodes a of Σ_z W_a(z) ∏_{b ≠ a} f_ab(z, t_ab). 

### `sum_erase_eq_pairs`

 A sum over ordered pairs of distinct nodes, regrouped by unordered pairs. 

 ### The place of the pair (a, b) in the word of all labels 

### `pos`

 The number a·g + b of the pair (a, b). 

### `sum_range_eq_sum_pos`

 A sum over all numbers below g·g is a sum over all pairs. 

 ### The function 

### `cap_comm`

 The two lengths given for the labels of a pair agree. 

### `two_mul_enumBits`

 The word of all labels has U/2 bits. 

### `tuples_eq`

 The labels of all pairs are the tuples that have a word of the length of the chunk at every
place. 

### `sum_words_eq`

 A sum over all words of U/2 bits is a sum over these tuples: the entry at a place is the chunk
of that number. 

### `term`

 The term of one choice t of labels, written with the functions W and f of `F`. 

### `enumF_eq`

 With a long enough pad the function is the sum of the terms over all words of U/2 bits. 

### `stEnum`

 The function `enumF` returns the value of the network, and the word of all labels has U/2 bits. 
