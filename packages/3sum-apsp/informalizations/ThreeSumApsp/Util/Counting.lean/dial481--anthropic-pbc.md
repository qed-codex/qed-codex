---
{
  "module": "ThreeSumApsp/Util/Counting.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Counting.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/Counting.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cardinalities of finite sets

General facts about finite sets.

* A product with one value on `S` and another elsewhere (`Finset.prod_ite_mem_const`); two products
  that vanish unless one set lies in another (`Finset.prod_ite_ite_subset`,
  `Finset.prod_ite_ite_superset`); the number of sets of `k` elements inside a set or around a set
  (`Finset.sum_powersetCard_ite_subset`, `Finset.card_powersetCard_superset`).
* At most `c` elements of a set have a given quotient by `c` under an injective function
  (`Finset.card_filter_div_eq_le`).
* A finite subset of `Fin L` has `j` elements below its `j`-th lowest element
  (`Finset.card_filter_lt_orderEmbOfFin`, from `Finset.card_filter_lt_map` for any increasing
  sequence).

* A function `f : ι → α` has a property `p` at the place `i` if `p (f i)` holds. The number of
  functions `f` with `f i ∈ A i` that have `p` exactly at the places of a set `S` is a product over
  the places (`Finset.card_pi_places_eq`). The number of those that have `p` at exactly `k` places
  is the sum of these products over the sets `S` of `k` places (`Finset.card_pi_places_card`).
  Without the restriction to `A` it is a binomial coefficient times two powers
  (`Finset.card_places_card`).


### `prod_ite_mem_const`

 A product that takes the value `a` on `S` and `b` elsewhere. 

### `prod_ite_ite_subset`

 A product with the factors `1` on `S ∩ Q`, `0` on `S \ Q`, `c` on `Q \ S` and `1` elsewhere: it
is `0` unless `S ⊆ Q`. 

### `prod_ite_ite_superset`

 A product with the factor `0` on `T \ S` and `1` elsewhere: it is `0` unless `T ⊆ S`. 

### `sum_powersetCard_ite_subset`

 The number of sets of `k` elements inside `Q`, each counted `c` times. 

### `card_powersetCard_superset`

 The number of sets of `k` elements that contain `T`: choose the complement outside `T`. 

### `card_filter_div_eq_le`

 At most `c` elements `x` of `s` have `⌊f x / c⌋ = k`, if `f` is injective on `s`: their values
lie in `[kc, kc + c)`. 

 ## The elements below a bound 

### `card_filter_lt_map`

 An increasing sequence has `j` members below its member number `j`. 

### `card_filter_lt_orderEmbOfFin`

 The number of elements of `s` below its `j`-th lowest element is `j`. 

 ## Functions by the set of places with a property 

### `card_pi_places_eq`

 The number of functions `f` with `f i ∈ A i` whose set of places with `p` is exactly `S`: choose
a value with `p` at each place of `S` and one without `p` at every other place. 

### `card_pi_places_card`

 The number of functions `f` with `f i ∈ A i` that have `p` at exactly `k` places, as a sum over
the possible sets of these places. 

### `card_places_card`

 The number of functions `ι → α` that have `p` at exactly `k` places. 
