---
{
  "module": "Nc/CaseI/Multi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Multi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/CaseI/Multi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Multilinear parts of circuits

Variables (a, t), a < k (blocks), t ∈ T. `cf S P x` is the coefficient of the product of the variables
(a, x a), a ∈ S, in P. If a circuit with s gates computes P, then the part of P that is linear in each of
the k blocks is a sum, over the sets A of blocks with k/3 ≤ |A| ≤ 2k/3 and the gates, of products of a
function of the x a, a ∈ A, and a function of the other x a.


### `mono`

 The exponent of the product of the variables (a, x a), a ∈ S. 

### `cf`

 The coefficient of the product of the variables (a, x a), a ∈ S. 

### `bal`

 The balanced subsets of S. 

### `Dec`

 f is a sum of products of coefficients of gates for balanced sets A ⊆ S, and functions of the rest
of S. 

### `Dec.single`

 One term. 

### `Dec.mul`

 Products with functions of other blocks. 

### `dec_gate`

 The induction for one gate. 
