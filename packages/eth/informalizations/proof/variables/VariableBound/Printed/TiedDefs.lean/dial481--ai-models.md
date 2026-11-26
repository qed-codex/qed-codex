---
{
  "module": "proof/variables/VariableBound/Printed/TiedDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/TiedDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Printed/TiedDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Two statement forms for the bound in n: definitions

Two definitions for statements about the Lean proof of the bound in n (Appendix D):
* `TiedOut A e post rn rm`: ONE machine and ONE constant such that the machine, on EVERY bit string
  x, halts with `post` of `A` at x and a pad of 2^(e x) units, within C·(|x| + 2^(e x) + 1)^C steps,
  and, on the code of (k, φ), halts
  with `post` of the number of satisfying assignments within the three bounds of
  `SatM.CountUniformInRate`, each under its conditions. With `post` the identity the last three
  clauses are `SatM.CountUniformInRate` for that machine.
* `StEndS R`: hypotheses on a solver for cliques with a sequence of levels, a precision `slU` and
  the rates, with a conclusion R that may name the solver, the function `pick` of its sequence of
  levels and the precision `slU`. 

### `TiedOut`

 One machine, finite alphabets, one constant C. On every bit string x the machine halts with
`post (A (x, pad))`, where the pad has 2^(e x) units, within C·(|x| + 2^(e x) + 1)^C steps. On the
code of (k, φ), k ≥ 1, φ a k-CNF on n
variables, it halts with `post` of the number of satisfying assignments in n + 1 bits: within
C·2^{C·k²·n·rn(n)} steps if n ≥ 1; within C·2^{C·k·m·rm(m)} steps if all variables occur and m ≥ 1;
within
C·2^{C·min(k²·n·rn(n), k·m·rm(m))} steps if all variables occur and n ≥ 1. 

### `StEndS`

 Hypotheses on a solver S for cliques with a sequence of levels, a precision `slU` and two rates,
with the conclusion R for S, the function `pick` of its sequence of levels, `slU` and the two rates. 
