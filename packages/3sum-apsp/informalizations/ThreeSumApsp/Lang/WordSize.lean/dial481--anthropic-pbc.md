---
{
  "module": "ThreeSumApsp/Lang/WordSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/WordSize.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/WordSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A polynomial bound in the parameters fits in a word

The running-time claims hold at every word size W ≥ b (log₂ p₁ + ⋯ + log₂ p_r + 1), where p₁, …, p_r
are the parameters of the instance and the slope b is chosen with the program (`Admissible`).  A
light program states its limits as a polynomial in the parameters,
`polyBound s k params` = 2^s ((p₁ + 1) ⋯ (p_r + 1))^k.

The main fact is `polyBound_le`: this bound is at most 2^W as soon as b ≥ s + k r + k.  Each factor
p + 1 is at most 2^(log₂ p + 1) (`prod_succ_le`), so with S the sum of the logarithms the bound is
at most 2^(s + k (S + r)), and s + k (S + r) ≤ (s + k r + k) (S + 1) ≤ W.


### `polyBound`

 The bound 2^s · ((p₁ + 1) (p₂ + 1) ⋯)^k in the parameters of an instance. 

### `polyBound_le`

 At an admissible word size, words have room for a polynomial bound in the parameters, if the
slope is large enough. 

### `one_le_polyBound`

 The bound is positive. 

### `polyBound_cons_le`

 The bound grows with its first parameter. 

### `polyBound_mono`

 The bound grows with its two exponents. 

### `le_polyBound_of_le_pow`

 A number that is at most A (n + 1)^e with e ≤ k has a bound of this form in n. 

### `polyBound_pair_le`

 A bound in two parameters is a bound in n, of twice the degree, if both are at most n. 

### `polyBound_mul`

 A power of two times the bound is a bound of the same form. 

### `add_le_polyBound`

 The sum of two numbers with such bounds has such a bound. 
