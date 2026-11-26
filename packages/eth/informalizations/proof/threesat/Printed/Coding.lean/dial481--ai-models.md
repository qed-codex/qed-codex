---
{
  "module": "proof/threesat/Printed/Coding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Coding.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/Coding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Between Definition 3's tables and the tables of this development: proofs

Definition 3: «A setting z_w is encoded by concatenating its K − 1 strings z_w(w')». This
development writes the same setting as the list of K strings with the empty string at w.
* `copyAt_flatten_ofFn`, `length_flatten_ofFn`: concatenating the K strings gives a string of (K − 1)λ
  bits whose copy at w' is the string number w';
* `flatten_copies`: cutting a string of (K − 1)λ bits into its copies and concatenating them gives
  the string back;
* `stAskServes`, `stCliqueValue`, `stToLists`: the three statements of CodingDefs.lean. 

 ### Concatenating the K strings 

### `sum_lengths`

 The first i of the K strings, of which the one at w is empty and the others have λ bits, have
i·λ bits together, or (i − 1)·λ if w is among them. 

### `map_length_ofFn`

 The lengths of the K strings. 

### `take_sum`

 The number of bits of the first i strings. 

### `length_flatten_ofFn`

 The concatenation has (K − 1)λ bits. 

### `copyAt_flatten_ofFn`

 The copy at u of the concatenation is the string number u. 

 ### Cutting a string into its copies 

### `eq_of_blocks`

 Two strings of r·λ bits with the same r blocks of λ bits are equal. 

### `flatten_copies`

 Definition 3, «encoded by concatenating its K − 1 strings»: the copies of a string of (K − 1)λ
bits, concatenated, give the string back. 

### `toLists_eq`

 The query made from (w, z) in this development: the list of the function w' ↦ z_w(w'). 

### `stToLists`

 Cutting a setting into its strings, and back. 

 ### The value 

### `stCliqueValue`

 The value of the network of Definition 3 reads the tables only at strings of (K − 1)λ bits;
there the two ways to write a setting name the same entry. Then the sentence after Definition 3,
«only the terms in which the two copies on every edge agree contribute, and the value is the sum,
over all choices of one string in {0,1}^λ per edge, of ∏_{w∈[K]} W_w evaluated at the strings on the
edges at w» (`Value.stCliqueValue`, proof/networks/Value/Clique.lean). 

 ### One query, one step 

### `size_ofFn_le`

 The size of a list of K strings of at most λ bits. 

### `size_entry`

 An entry below 2^B has size at most B + 1. 

### `stAskServes`

 The procedure `askTable`, with the tables built in, answers every well-formed query of this
development in one step. 
