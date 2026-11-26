---
{
  "module": "proof/rates/GeneralPieces/Top/EndM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Top/EndM.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Top/EndM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the top level in m to the machine, for the named function and exponent

`topM_of_arith` states the top level in m with a conclusion that names what the machine computes
(`GeneralPieces.Tied.TopM`): the padding machine, made from the exponent `eM S pick` and the
function `AM S pick`, computes that function on
every input; on the code of a k-CNF the function is the number of satisfying assignments; the
exponent is O(k·m·r(m)). `countInRate_of_topM` derives from it the form with "there is a machine". 

### `topM_of_arith`

 The padding machine, run on the function and the exponent function of a solver with a sequence
of indices, computes that function and counts within C·2^(C·k·m·r(m)) steps. The inequality from the
proof of Theorem A(c), that the exponent at the level picked for m is
O(k·m·e_ℓ), is the hypothesis `hA`, for this sequence. 

### `countInRate_of_topM`

 The form with "there is a machine" follows; it does not name what the machine computes. 
