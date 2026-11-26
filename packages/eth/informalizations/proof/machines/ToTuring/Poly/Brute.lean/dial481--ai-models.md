---
{
  "module": "proof/machines/ToTuring/Poly/Brute.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Brute.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/ToTuring/Poly/Brute.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 `brute`: brute force for the sum Z (the value of a clique, as in Definition 3 of the paper), the
sum over all labellings of the product over
the K nodes of the answers of a given machine `R`. If every step of `R` is polynomial-time
(`IsPolyT`), so is every step
of `brute`. 

### `bruteLen_unary`

 The number of bits of a labelling is given in unary if the length of a label is. 

### `bruteBound_polyT`

 The number of labellings is polynomial-time. 

### `bruteQuery_polyT`

 The query sent to `R` is polynomial-time. 

### `IsPolyT.brute`

 Brute force over the 2^(K(K-1)/2·lam) labellings, as a sum of products of K calls of `R`, is
`IsPolyT` if `R` is. 

### `bruteE_keeps`

 The brute-force evaluator `bruteE K` keeps `IsPolyT`: applied to an `IsPolyT` machine for the
tensors it gives one. 
