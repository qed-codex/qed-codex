---
{
  "module": "proof/rates/PaddedDescent/Pad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Pad.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Pad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Padding. Let A be a polynomial-time function of a bit string x and a list of units («the pad»),
and let e be a polynomial-time
function from bit strings to numbers. Then ONE Turing machine of Mathlib computes x ↦ A (x, pad of
length 2^(e x)) within
q·(|x| + 2^(e x) + 1)^q steps, for ONE constant q (`exists_tm_padded`). In words: polynomial time
(`PolyT`) in the padded input gives a
Turing machine with time polynomial in |x| + 2^(e x). `decidesTM_of_padded` is the same for 3-SAT.
The stepped machine `padM` starts with a pad of length 1, doubles it e x times, one doubling per
step, and then applies A in a single step. 

### `pad`

 The pad of length 2^k. 

### `padM`

 The stepped machine: the state is the input with the present pad, or the result. One step
doubles the pad, or, once the
pad has length at least 2^(e x), applies A. 

### `padM_isPolyT`

 Every part of the padding machine is polynomial-time if e and A are. 

### `padM_reaches`

 From the pad of length 2^k, k ≤ e x: the remaining doublings and the last step. 

### `padM_runs`

 The padding machine ends after e x + 1 steps with A (x, pad of length 2^(e x)); its states have
size at most
2|x| + 2·2^(e x) + 3. 

### `pad_bound`

 Arithmetic: the bound of the host for the padding machine is a polynomial in |x| + 2^e + 1. 

### `exists_tm_padded`

 Let `e` (from bit strings to numbers) and `A` (from a bit string and a list of units to a bit)
be polynomial-time. There are a
Turing machine `N` with finite alphabets and a number `q` such that on every bit string `x` the
machine halts with the output
A (x, the list of 2^(e x) units) within q · (|x| + 2^(e x) + 1)^q steps. 

### `decidesTM_of_padded`

 The same for 3-SAT. Let `e` and `A` be polynomial-time. There are a Turing machine `N` with
finite alphabets and a number `q`,
depending on `e` and `A` only, such that for every function `E` of the number n of variables: if on
the code x of every instance of
3-SAT e x ≤ E n, and A (x, the list of 2^(e x) units) is the bit «satisfiable», then `N` decides
3-SAT within
q · (25 (n + 2)^4 + 2^(E n))^q steps. 
