---
{
  "module": "proof/variables/VariableBound/Field/Alg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Alg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Field/Alg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What a word of bits stands for

`decR r w` is b_0 + b_1·r + … + b_(n−1)·r^(n−1) for the word w = (b_0, …, b_(n−1)) and an element r
of a commutative ring. With r = X it is a polynomial over the field with two elements (`polyW`);
`modP g` is the polynomial X^s + g, where s is the length of g; `FW g` is the ring of residues
modulo it, and `decW g w` the residue that the word w stands for. 

### `bitR`

 A bit as an element of a ring. 

### `decR`

 b_0 + b_1·r + … + b_(n−1)·r^(n−1), by Horner's rule. 

### `polyW`

 The polynomial over the field with two elements whose coefficients are the bits of w. 

### `modP`

 The polynomial X^s + g, where s is the length of g. 

### `FW`

 The ring of residues of polynomials over the field with two elements modulo X^s + g. 

### `decW`

 The residue that the word w stands for. 
