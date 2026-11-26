---
{
  "module": "proof/consequences/SizeCircuit/Circuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Circuit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/SizeCircuit/Circuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: «a circuit with O(n) gates of two inputs tests whether |S| = s»

`testsSize_sizeGates`: the circuits `sizeGates n s` of
proof/consequences/SizeCircuit/CircuitDefs.lean have at most 6·(n+1) gates, their gates read earlier
wires only, and on a word of length n ≥ 1 their output is 1 exactly if the word has s ones. From the
addition (Addition.lean) and the comparison (Compare.lean), applied to the values of the wires on
the input. 

### `sum_toNat`

 The sum of the bits of a word is the number of its ones. 

### `onesAmong_inputs`

 The number of input wires that are 1 is the number of ones of the input. 

### `testsSize_sizeGates`

 **«a circuit with O(n) gates of two inputs tests whether |S| = s».** For all n ≥ 1 and all s,
`sizeGates n s` has at least one and at most 6·(n+1) gates, every gate reads earlier wires only, and
on a word of length n the output is 1 exactly if the word has s ones. 
