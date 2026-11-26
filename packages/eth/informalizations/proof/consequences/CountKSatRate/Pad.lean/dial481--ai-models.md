---
{
  "module": "proof/consequences/CountKSatRate/Pad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Pad.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CountKSatRate/Pad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Padding, for a function whose value is a word

Let B be a polynomial-time function of a bit string x and a list of units («the pad») whose value is
a bit string, and let e be a polynomial-time function from
bit strings to numbers. Then one Turing machine of Mathlib computes x ↦ B (x, pad of length 2^(e x))
within q·(|x| + 2^(e x) + 1)^q steps, for one constant q
(`stPaddedW`, which proves the interface statement `StPaddedW`). The stepped machine `padMW` starts
with a pad of length 1, doubles it e x times, one doubling per step,
and then applies B in a single step. The file follows proof/rates/PaddedDescent/Pad.lean, where the
value is one bit. The difference: the last state holds the value, so its size has
to be bounded, and the bound comes from the certificate of B. The host machine is that of
proof/consequences/CountKSat/Host.lean. 

### `padMW_isPolyT`

 Every part of the padding machine is polynomial-time if e and B are. 

### `size_bools`

 The size of a bit string. 

### `size_pad`

 The size of the pad of length 2^k. 

### `pad_append`

 Doubling the pad. 

### `length_pad`

 The length of the pad. 

### `padMW_reaches`

 From the pad of length 2^k, k ≤ e x: the remaining doublings and the last step. 

### `padMW_runs`

 The padding machine ends after e x + 1 steps with w = B (x, pad of length 2^(e x)); its states
have size at most 2|x| + 2·2^(e x) + 2|w| + 5. 

### `len_padded`

 The word of (x, pad of length 2^k) has 3|x| + 4·2^k + 6 symbols. 

### `stPaddedW`

 Polynomial time in the padded input gives a Turing machine with time polynomial in |x| + 2^(e
x), for a function whose value is a word. 
