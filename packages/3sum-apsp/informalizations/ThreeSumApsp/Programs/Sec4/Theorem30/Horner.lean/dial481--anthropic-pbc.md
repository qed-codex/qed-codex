---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Horner.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Horner.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Horner.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Horner's rule: the code of a string of decimal digits

horner(a, L) returns the number whose L decimal digits, most significant first, are in the cells
from a.  It is used to index an encoding by a leaf (Section 4.3: "The encodings are indexed by the
leaves (Section 2.4.1) […].  Thus reading the product at a leaf […] takes O(L) operations").

After i rounds the routine holds the number formed by the first i digits (`Horner.Inv`).  One more
digit multiplies it by ten and adds the digit (`ofDigitList_take_succ`), and it stays below 10^L
(`ofDigitList_lt`), which fits in a word.  `horner_spec` is the specification.


### `Str`

 The local variables of horner: the arguments (the address of the string and its length), the
level, and the number formed so far.  Local 0 also takes the result. 

### `Inv`

 Before round i the number formed by the first i digits has been computed.  The memory is not
changed. 

### `hornerBody`

 horner(str, len): multiply by ten and add the next digit, from the most significant digit on. 

### `horner_spec`

 **horner** returns the number with the given decimal digits, and leaves the memory as it
was. 
