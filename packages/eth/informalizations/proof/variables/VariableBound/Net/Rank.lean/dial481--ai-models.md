---
{
  "module": "proof/variables/VariableBound/Net/Rank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Rank.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Rank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «The total»: ranks of subsets

«Within a profile, replace the string of the marks of the t_(a,b,κ) objects, in a fixed order, by
its position in the list of all strings of this length with μ_(a,b,κ) ones.» Proved here:

* `rank_lt`, `rank_inj`: the position is below C(t, μ), and two strings of the same length with as
  many ones and the same position are equal;
* `stLab`: the label that a shows to b has c_(a,b) bits, and the labels of two settings of the
  profile agree if and only if the two settings give the same marks to every object with the test
  {a, b}.
  With this, Ψ_(a,b) factors through c_(a,b) bits. 

### `count_false_cons`

 A bit 0 in front does not change the number of ones. 

### `rank_lt`

 The position of a string is below the number C(t, μ) of strings of its length t with as many
ones, μ. 

### `rank_inj`

 Two strings of the same length with as many ones and the same position are equal. 

### `tst_comm`

 The objects with the test {a, b} are those with the test {b, a}. 

### `mu_comm`

 μ_(a,b,κ) = μ_(b,a,κ). 

### `length_str`

 The string of marks has one bit for each object with the test. 

### `labD_eq`

 The label is the word of kind 0 followed by the word of kind 1. 

### `rank_lt_two_pow`

 The position of a string of t bits with μ ones can be written with ⌈log C(t, μ)⌉ bits. 

### `toWord_rank_inj`

 The words of ⌈log C(t, μ)⌉ bits of the positions of two strings of t bits with μ ones agree if
and only if the strings agree. 

### `stLab`

 Step 3, «The total»: the labels have c_(a,b) bits; two settings of the profile (the strings have
μ ones) have the same label if and only if they give the same marks to every object with the test
{a, b}. 
