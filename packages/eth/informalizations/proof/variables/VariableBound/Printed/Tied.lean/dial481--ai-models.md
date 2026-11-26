---
{
  "module": "proof/variables/VariableBound/Printed/Tied.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/Tied.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/Tied.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The end of this proof, tied to its functions: the machine and the counting statement

* `tied_of_alg`: the padding machine (`StPaddedW`), run on an algorithm (A, e) followed by a
  polynomial-time `post`, is a machine as in `TiedOut A e post`, with the clause of `StPaddedW`
  kept in the conclusion; the constant is the largest of q and the two constants of the bounds.
* `count_of_tied`: the statement that names no function follows by forgetting that clause. 

### `mul_pow_mono`

 q·y^q grows with q, for y ≥ 1. 

### `tied_of_alg`

 For an algorithm (A, e) for the rates rn, rm ≥ 0 and a polynomial-time function `post`: one
machine and one constant such that the machine runs `post` after A on every input, with the pad of
2^(e x) units, and puts out
`post` of the count within the three bounds. The padding machine is a hypothesis. 

### `count_of_tied`

 A machine that runs A on every input and counts within the three bounds is a machine that counts
within the three bounds. This statement names no function. 
