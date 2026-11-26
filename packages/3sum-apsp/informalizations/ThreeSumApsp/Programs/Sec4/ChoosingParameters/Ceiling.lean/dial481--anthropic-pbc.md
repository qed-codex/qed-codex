---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/Ceiling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Ceiling.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/Ceiling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollaries 26 and 31 in the light language: ⌈a m / b⌉ by counting

Proof of Corollary 26: "Let L := 21m and t := ⌈m/9⌉"; proof of Corollary 31: "with L := ⌈cm⌉ and t
:= ⌈θm⌉". For rational c = a/b the number ⌈a m / b⌉ is found without division: count in steps of b
up to a m. The numbers a and b are constants of the program text.


### `Arg`

 The locals of ceilMul: the argument m, which the result replaces; the product a m; a counter
that goes up in steps of b; and the number of its steps. 

### `ceilMulBody`

 ceilMul(m) counts up to a m in steps of b. For m = 0 the result is 0, and the constant a is not
touched (it need not fit in a word then). 
