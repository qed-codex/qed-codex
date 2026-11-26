---
{
  "module": "Ov/Duality/Abstract.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Abstract.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Ov/Duality/Abstract.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Gauges on a commutative monoid with a covering relation

Let M be a commutative monoid (the tensors up to equivalence) with a relation "t is covered by the finite
family b" (t is a sum of restrictions of the members of b). A gauge is a function p ≥ 0 on M with p(1) = 1,
p(st) ≤ p(s)p(t), and p(t) ≤ ∑ p(b) whenever b covers t. This file has the definitions, infima of directed families of
gauges (`isPre_iInf`, `keeps_iInf`), and the first facts on the numbers a with p(tⁿ) ≤ C·aⁿ (`IsPre.rad`). The proof of
Proposition prop:gauge is in Paper/Gauges.lean.


### `Cover`

 A covering relation between elements and finite families of elements: reflexive, transitive,
and compatible with multiplication by an element. 

### `Cover.cov`

 the element is covered by the family 

### `IsPre`

 The function p is a gauge: p ≥ 0, p(1) = 1, submultiplicative,
and subadditive under covers. 

### `Keeps`

 The inequality p(tx) ≤ c·p(ty) for all t. 

### `le_iInf_add`

 For finitely many elements, one member of a directed family is close to its infimum. 

### `isPre_iInf`

 A directed infimum of functions P i is a gauge if each of them is, where instead of
P i (st) ≤ P i (s)·P i (t) it is enough that P j (st) ≤ P i (s)·P i (t) for some j. 

### `rad`

 The numbers a > 0 for which there is a C with p(t^m) ≤ C·a^m for all m. Their infimum is the
spectral radius of p at t. 

### `prod_bound`

 The bound for a product of powers, by the bounds for the powers. 
