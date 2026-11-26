---
{
  "module": "Nc/Final/CClasses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Final/CClasses.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Final/CClasses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The classes VP and VNP

Valiant's classes over a commutative semiring: families of polynomials with polynomially many variables,
polynomial degree and circuits of polynomial size; and sums of such polynomials over all values 0, 1 of some of
the variables.


### `Family`

 A family of polynomials, with finitely many variables for every n. 

### `Family.X`

 the variables 

### `Family.fin`

 finitely many 

### `Family.poly`

 the polynomials 

### `VP`

 VP: the families with polynomially many variables, polynomial degree and circuits of polynomial size. 

### `bits`

 Substitute the bits e for the variables of the second kind. 

### `VNP`

 VNP: the families p n (x) = ∑ q n (x, e), the sum over all e in {0, 1} ^ m n, for a family q in VP (so m is
polynomially bounded). 

### `Computes.map`

 Circuits over a larger ring. 

### `Computes.rename`

 Circuits with renamed variables. 

### `Computes.join`

 Two circuits side by side, and one more gate. 

### `CSize`

 The polynomial has circuits with s gates and degree at most d. 
