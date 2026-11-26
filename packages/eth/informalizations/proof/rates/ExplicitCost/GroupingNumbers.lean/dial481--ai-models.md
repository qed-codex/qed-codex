---
{
  "module": "proof/rates/ExplicitCost/GroupingNumbers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingNumbers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingNumbers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The numbers K, g, P, B, U, L and B' of the input

The procedure reads K, g, P, B and the numbers c_{a,b} off its input and computes U, L and B' from
them. On the input that belongs to ζ = a/b, K and a network N with parameters P, B these are the
numbers of Lemma 8 (Appendix A) of the paper:

* `inK_groupingInput`, `inG_groupingInput`, `inP_groupingInput`, `inB_groupingInput`,
  `inU_groupingInput`: K, g, P, B and the total U of N;
* `lbLen_groupingInput`: the number of bits between two groups that the test forms is Y_{γ,γ'};
* `ceil_div_nat`: ⌈n/d⌉ as a quotient of natural numbers;
* `labelLengthIsL`: the number computed is L = ⌈(U + 2ζgP)/K²⌉, and `Printed.bitsOut` is B'. 

### `inK_groupingInput`

 The K of the input. 

### `inG_groupingInput`

 The g of the input. 

### `inP_groupingInput`

 The P of the input. 

### `inB_groupingInput`

 The B of the input. 

### `inU_groupingInput`

 The sum of the numbers c_{a,b} of the input is the total U. 

### `lbLen_groupingInput`

 The number of bits between two groups that the test forms from the input is Y_{γ,γ'}. 

### `ceil_div_nat`

 ⌈n/d⌉ = ⌊(n + d − 1)/d⌋ for natural numbers n and d ≥ 1. 

### `labelLength_groupingInput`

 The number that the procedure computes, written out. 

### `labelLengthIsL`

 The number computed is the L of Lemma 8, and `Printed.bitsOut` is its B'. 
