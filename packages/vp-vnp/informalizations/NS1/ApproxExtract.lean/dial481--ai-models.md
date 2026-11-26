---
{
  "module": "NS1/ApproxExtract.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxExtract.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxExtract.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Back to equality

A program guesses, for every constant, the digits of its power and one term of that power, multiplies by the
coefficient of the term, an element of the ring E, and adds the exponent of ε on a counter. It accepts only if the
counter is 0. So its value is the coefficient of ε^0 of an approximate value: the exact one.


### `chT`

 Guess a word of length `n`; go on with the formula of this word. 

### `RelX`

 A run that gives budgets and the digits of a counter, and multiplies by a coefficient. 

### `termExp`

 The exponent of the term with the number `k`. 

### `termCoef`

 Its coefficient; 0 if there is no such term. 

### `expBits`

 An exponent as `W` digits modulo 2 ^ W. 

### `wrap`

 Exponents modulo 2 ^ W. 

### `mark`

 A coefficient with the exponent on the counter. 

### `coeff_wrap_zero`

 **Paper: proof of Proposition prop:approx-acc, the counter at 0.** The coefficient at 0 modulo 2 ^ W is the one of ε^0. 

### `sum_terms`

 **All terms of a Laurent polynomial.** 

### `coefK`

 The coefficients of the terms of the powers, with names for every choice of digits and term. 

### `xL`

 What the gadget guesses: budgets, a coefficient, the digits of the counter. 

### `combF`

 Pair the budgets and add the counters. 

### `xF`

 The gadget. 

### `bt_xL`

 The budgets of the gadget have few digits. 

### `sum_xL`

 **Paper: proof of Proposition prop:approx-acc, the guessed terms together give all budgets.** Counted modulo 2 ^ W. 

### `xF_ev`

 **The runs of the gadget.** 
