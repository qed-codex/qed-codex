---
{
  "module": "proof/consequences/CircuitLowerBound/Alg/Parse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Parse.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Alg/Parse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): circuits as words

The guess of the nondeterministic algorithm is a circuit, written as a word: the number W of bits of
a wire in unary (1^W 0), then for each gate its four values and the numbers of its two wires with W
bits each, lowest bit
first. The decoder `decC` reads every word as a list of gates (what is left over at the end is not
read); `wfB` tests whether every gate reads inputs and earlier gates only. Every list of gates whose
wires have numbers
below 2^W is read back from its code (`decC_encC`). Both functions are polynomial-time. 

### `gateW`

 A gate as a word: its four values, then the numbers of its two wires with W bits each. 

### `encC`

 A list of gates as a word. 

### `gateOfW`

 The gate written by a word of 4 + 2W bits. 

### `decC`

 The list of gates written by a word. 

### `wfB`

 Does every gate read inputs and earlier gates only? 

### `ones_unary_append`

 The number of ones at the start of 1^P 0 y. 

### `rest_unary_append`

 What follows 1^P 0 in 1^P 0 y. 

### `length_gateW`

 The word of a gate has 4 + 2W bits. 

### `gateOfW_gateW`

 A gate is read back from its word. 

### `block_flatten`

 The j-th block of a concatenation of words of length ℓ. 

### `length_flatten_gateW`

 The words of the gates have |C|·(4 + 2W) bits together. 

### `length_encC`

 The length of the code. 

### `decC_encC`

 A list of gates whose wires have numbers below 2^W is read back from its code. 

### `wfB_iff`

 The test is right. 

 ### Polynomial time 

### `ones_unary`

 The number of ones at the start of a word, in unary. 

### `ones_polyT`

 The number of ones at the start of a word. 

### `rest_polyT`

 The word after its first ones and the zero that ends them. 

### `gateOfW_polyT`

 The gate written by a word. 

### `decC_polyT`

 The decoder. 

### `wfB_polyT`

 The test. 
