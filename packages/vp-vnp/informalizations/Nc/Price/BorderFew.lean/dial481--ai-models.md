---
{
  "module": "Nc/Price/BorderFew.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/BorderFew.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/BorderFew.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The choice among a few terms

A spectral point at a sum of |J| terms, exact or up to ε: the choice of the term costs |J| only to the exponent of
the unit tensor on the parties that hold legs. Proof: tensor powers, types of words, N-th roots.


### `few_hexp_nonneg`

 The exponent of a unit tensor is not negative. 

### `wordType`

 The number of times a word uses each letter. 

### `exists_perm_of_wordType`

 Words of one type differ by a permutation of the places. 

### `le_type_bound`

 For r orders ρ m of the places, the sum over m of the images of a
product, with the places in the order ρ m, is one image of the product times the unit tensor of size r on the
parties that hold legs. So a spectral point is at most (E + 1) ^ #parties · r ^ g · ∏ at the coefficient of ε ^ E. 

### `le_of_pow_le_poly`

 A bound for all powers with a factor polynomial in N holds without the
factor. 

### `pow_le_few`

 The N-th power of the value at t is at most the number of types times the
factor of the extraction times (|κ| ^ g · M) ^ N. 

### `few`

 The choice among |κ| terms, exact or up to ε, costs only the exponent of the unit tensor on
the parties that hold legs: if t is a sum of restrictions of the b k up to ε, every b k has value at most M, and
outside the range of π all legs of t are trivial, then t has value at most |κ| ^ g · M. 

### `BSum.of_sumRestr`

 An exact sum of restrictions is a sum up to ε with denominators 1. 
