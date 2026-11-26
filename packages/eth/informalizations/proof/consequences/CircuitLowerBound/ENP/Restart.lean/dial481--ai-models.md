---
{
  "module": "proof/consequences/CircuitLowerBound/ENP/Restart.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/ENP/Restart.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/ENP/Restart.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the language L0 is in E^NP, in the restart form

`stENP'_of`: the language `L0` is decided by an ordinary machine that is started again after every
answer of the oracle (`ENP.InENP'`). The machine computes the function `roundF` of
`proof/consequences/CircuitLowerBound/ENP/Round.lean`, after
writing a pad of 2^(2m+4) units by doubling (`CountKSatRate.stPaddedW`,
proof/consequences/CountKSatRate/Pad.lean). On a word x of length m that writes the number i, the
protocol makes i + 1 ≤ 2^m queries. After j answers, the negated answers
are the first j values of the search `greedy (Phi m)`: the answer «satisfiable with 0 for the next
variable» means the value 0. The result is value number i.
The hypotheses are interface statements: the chains and the formulas are computed in polynomial time
(`StCertSched`, `StCertTabF`, `StFlip`). That the variables of the formula of a table have L bits
(`StVars`) is taken from
`proof/consequences/CircuitLowerBound/Small.lean`. 

### `length_greedy`

 The search has set j variables after j steps. 

### `time_le`

 The time of a round on x and a ≤ 2^m answers, m = |x|. 

### `protocol`

 The protocol, from what the rounds return. After j answers the negated answers are the first j
values of the search; d more rounds with a query follow, and the round with the result. 

### `stENP'_of_vars`

 The language L0 is in E^NP, in the form with a machine that is started again after every answer;
with the bound on the variables as a hypothesis. 

### `stENP'_of`

 The language L0 is in E^NP, in the form with a machine that is started again after every answer. 
