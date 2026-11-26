---
{
  "module": "Nc/Price/Hyper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Hyper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Hyper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The exponent of a unit tensor; hyperedges are convex

For a spectral point F over the parties I and a map π : A → I, the number `hexp F π` is the exponent g of the unit tensor
with one leg at π a for every a in A (a hyperedge): F has the value n ^ g at the one of size n. This file has the simple
facts on g (it depends only on the set of parties, it is a distance for two parties, legs can be moved along edges), and the
lemma "hyperedges are convex": if every leg is moved to the midpoint of two places, g is at most the mean of the two values.


### `unit_eq_rpow_hexp`

 A spectral point has the value n ^ g at the unit tensor of size n ≥ 1 with
the legs at π. 

### `unit_two_eq_rpow_hexp`

 The case n = 2 of the definition of g. 

### `hexp_nonneg`

 The exponent of a unit tensor is not negative. 

### `hexp_congr_range`

 The exponent of a unit tensor depends only on the set of the parties that hold
a leg. 

### `hexp_pair`

 For two legs the exponent of the unit tensor is the distance. 

### `hexp_const_le`

 If all legs are at one party, the exponent of the unit tensor is at most 0. 

### `hexp_le_of_two`

 If all legs are at the two parties p and q, the exponent of the
unit tensor is at most the distance of p and q. 

### `hexp_le_move`

 If the leg a is moved from π' a to π a, the exponent of the unit tensor grows at most
by the sum of the distances. 

### `hexp_pull`

 The exponents of unit tensors for a pull-back of a spectral point. 
