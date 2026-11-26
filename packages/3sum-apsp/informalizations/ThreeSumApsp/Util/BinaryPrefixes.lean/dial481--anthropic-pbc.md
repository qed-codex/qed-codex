---
{
  "module": "ThreeSumApsp/Util/BinaryPrefixes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/BinaryPrefixes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Util/BinaryPrefixes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The prefixes of a binary representation, one bit at a time

The prefixes `⌊z/2^ℓ⌋` of a number `0 ≤ z < 2^L` are computed without division, from the level
`ℓ = L` down to `ℓ = 0`.  Next to the prefix `q = ⌊z/2^ℓ⌋` (`prefQ`) one keeps the rest of the
number, moved to the top: `r = (z mod 2^ℓ) 2^(L-ℓ) < 2^L` (`prefR`).  One step doubles `r`; if the
result reaches `2^L`, then the next bit of `z` is 1 (`pref_step`).  The bit is the binary digit
number `ℓ` of `z` (`testBit_iff_shift`).  One step on lists of numbers is `zipWith_shiftQ` and
`map_shiftR`.


 ## Prefixes, one bit at a time 

### `prefQ`

 The prefix `⌊z/2^ℓ⌋`. 

### `prefR`

 The rest `z mod 2^ℓ`, moved to the top of `L` bits. 

### `shiftQ`

 The new prefix after one step: the old one with the next bit appended. 

### `shiftR`

 The new rest after one step. 

### `prefQ_start`

 At the top level the prefix is 0. 

### `prefR_start`

 At the top level the rest is the number itself. 

### `pref_step`

 **One step**: the prefix and the rest at the level `ℓ` are `shiftQ` and `shiftR` of those at the
level `ℓ + 1`. 

### `prefQ_nonneg`

 The prefixes of a nonnegative number are nonnegative. 

### `prefQ_le`

 The prefixes of a nonnegative number are at most the number. 

### `prefR_nonneg`

 The rests are nonnegative. 

### `prefR_lt`

 The rests have `L` bits. 

### `prefQ_natCast`

 The prefix of a natural number is the quotient of natural numbers. 

### `testBit_iff_shift`

 The bit that a step moves from the rest to the prefix is the binary digit number `ℓ`. 

 ## The lists of the prefixes and of the rests 

### `zipWith_shiftQ`

 One step on the list of the prefixes. 

### `map_shiftR`

 One step on the list of the rests. 

### `map_prefR_start`

 At the top level the rests are the numbers themselves. 
