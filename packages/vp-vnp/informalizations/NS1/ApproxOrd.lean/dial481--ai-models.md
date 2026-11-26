---
{
  "module": "NS1/ApproxOrd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxOrd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxOrd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Laurent polynomials in ε: orders, spans, rescaling

Used for approximate accelerators, whose constants are Laurent polynomials in ε.


### `OrdGE`

 All coefficients of exponents below `r` are 0: the polynomial lies in ε^r E[ε]. 

### `Span`

 All exponents that occur lie between `-n` and `n`. 

### `OrdGE.prod_sub`

 A product of approximations approximates the product. 

### `rescale`

 ε ↦ ε^r. 

### `Thin`

 The powers of `c` have few terms, as few as those of a polynomial of span `Δ`. 

### `All`

 All constants satisfy `P`. 

### `span_budg`

 **The orders of the products of powers of the constants**, for all budgets with `J` digits. 
