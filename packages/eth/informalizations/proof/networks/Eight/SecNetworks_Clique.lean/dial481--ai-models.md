---
{
  "module": "proof/networks/Eight/SecNetworks_Clique.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Clique.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Clique.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 3 «Networks»: lemmas on the (K, λ)-clique of Definition 3

Lemmas on the (K, λ)-clique of Definition 3, which is defined in `Eight/SecNetworks_Defs.lean`: the
places of the copies z_w(w') in a setting of node w, sums over the encoded settings of a node,
the strings at one node of a choice of one string per edge, the tables as functions of the encoded
settings, and bounds on the sizes of strings, nodes and the values 0 and 1. 

 ### The copies held at a node 

### `copyAt_eq_block`

 z_w(w') is the block number `place w w'` of the λ-bit blocks of z_w. 

### `place_lt`

 The places of the nodes other than w are below K − 1. 

### `place_inj`

 Two nodes other than w have different places. 

### `place_surj`

 Every place below K − 1 is taken by a node other than w. 

### `length_copyAt`

 In a setting of (K − 1)λ bits every copy has λ bits. 

### `sum_settings`

 Definition 3, «A setting z_w is encoded by concatenating its K − 1 strings z_w(w')»: a sum over
all strings of (K − 1)λ bits of a function of the K − 1 copies is the sum over all (K − 1)-tuples of
strings of λ bits.
A tuple is a function on all K nodes with the empty string at w itself. 

 ### A choice of one string per edge 

### `star_mem`

 The strings of a choice of one string per edge on the edges at v form a (K − 1)-tuple of strings
of λ bits. 

 ### The tables as functions of the encoded settings, and sizes 

### `tablesOn`

 The tables as functions of the encoded settings: W_w(z_w) is the entry at the K − 1 copies cut
out of z_w. 

### `size_word`

 The size of a string of n bits is 2n + 1. 

### `size_fin`

 A node of [K] is not larger than K. 

### `size_ite_le`

 The numbers 0 and 1 have size at most 2. 
