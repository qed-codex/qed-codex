---
{
  "module": "proof/rates/ClauseBound/ParityChecks/EndOL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/EndOL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/EndOL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From the function of the padded input to the Turing machine, for the bound in n of Theorem D (exponent k²·n·log log n/√(log n))

`stEndO : StEndO`, from `StPaddedW` (the padding machine), `StCorrectO`, `StCertO` and `StArithO`.
The two constants of the function are chosen in this order: c from `StArithO`, then n₀ from
`StCorrectO` for this c, then the constant A of `StArithO` for c and n₀. The padding machine runs
for q·(|x| + 2^(e x) + 1)^q steps on the input x. For the code x of an instance of k-SAT on n
variables |x| + 1 ≤ (k·2^k+1)·(n+2)^(k+1). Let r be the function in the hypotheses of `StEndO`, e_l
the exponent `e` of the level l chosen for n, and s the length of the list `slU` at that level. The
exponent e x is at most n,
which is used if n is below a constant, and at most A·n·e_l·(s+1) otherwise, so it is O(n·r(n)) in
both cases. Because r(n) ≥ 1/(c₁·(log₂(n+2))^c₁), also log₂(n+2) = O(n·r(n)). The same argument is
used in proof/rates/ClauseBound/TopN/End.lean. 

### `planAtO_getD_le`

 The exponent of a plan, or else n, is at most n. 

### `stEndO`

 The padding machine, run on the function and the exponent function of a solver with a sequence
of levels, counts within C·2^(C·n·r(n)) steps. 
