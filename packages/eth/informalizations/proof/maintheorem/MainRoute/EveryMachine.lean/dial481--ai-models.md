---
{
  "module": "proof/maintheorem/MainRoute/EveryMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/EveryMachine.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/MainRoute/EveryMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The bound in m of the Main Theorem, for every machine that computes the named function

`boundInMForEveryMachine`: an ARBITRARY machine that computes the function `AM` with the exponent
`eM` (`PairsToBound.Computes`) on the recursion of Appendix A meets the bound in m. The proof uses
nothing of the machine but what it puts out and the bound q·(|x| + 2^(exponent) + 1)^q on its steps,
and of the function three facts from `GeneralPieces.Tied.TopM` (part (c) of Theorem A for the named
programs): it is
right, its exponent is O(k·m/√(log m)), and a machine that computes it exists. (Theorem D (a) in the
same form is `RecursionToBound.thmVariablesAForEveryMachine`.) 

 ### The bound in m 

### `steps_le_of_exponent_le`

 The numbers: if E ≤ G·X with X ≥ 1, then q·(L + 2^E + 1)^q ≤ ⌊2^(C·X)⌋ + C·L^C for L ≥ 1, with C =
2q + 2q(G + 1) + q·4^q. 

### `boundInMForEveryMachine`

 The first sentence of Theorem A (c) at ρ = 1/√2 for every machine that computes the named
function, and there is one. 
