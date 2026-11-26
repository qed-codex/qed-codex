---
{
  "module": "proof/sparsification/UniformInK/Top/ArithDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/ArithDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The arithmetic of the exponent: constants and interface statements

Notation: K the number of nodes at the level picked for n, so that K^17 ≤ n < K^(17·C₀); Y the
number of binary digits of K; β a natural number, later `betaU k s`; b = β + 3, D = 2^β,
W = b²·D·Y (`WofU`). The plan is that of proof/rates/ClauseBound/ParityChecks/ArithOL.lean. What
differs: the inequality W ≤ A₁·K·e has a constant A₁ that depends on C₀ only, under the hypothesis
D⁶ ≤ K;
and D⁶ ≤ K follows from 2·(102·C₀·c)² ≤ ⌊log₂ n⌋ when D ≤ (⌊log₂ n⌋ + 1)^c (`StSixU`).
This file has definitions only. The statements `St…` are propositions. 

 ### Constants 

### `WofU`

 W = b²·D·Y for b = β + 3, D = 2^β and Y the number of binary digits of K. 

### `GU`

 The constant in g·P ≤ G·W·n. 

### `ccU`

 The sum of the constants of the parts of lower order. 

### `aU`

 The parameter a of the plan: 2^(betaU k s) ≤ (⌊log₂ n⌋ + 1)^(a·k). 

### `A1U`

 The constant of the inequality W ≤ A₁·K·e. 

 ### The exponent 

### `StNeedU`

 The exponent `needU` is at most (354·k·35·k + cc·A₁ + 1)·n·e·(s+1), if W ≤ A₁·K·e. 

 ### The inequality W ≤ A₁·K·e with a constant that does not depend on k, and bounds on 2^β 

### `StMasterU`

 W ≤ A₁·K·e if D⁶ ≤ K. 

### `StDLogU`

 2^(betaU k s) ≤ (⌊log₂ n⌋ + 1)^(a·k) for a = `aU C C₀`, if 2 ≤ K ≤ n, 1/(log₂ K)^C₀ ≤ e and 2^s
≤ (2/e)^C. 

### `StSixU`

 A number D ≤ (⌊log₂ n⌋ + 1)^c has D⁶ ≤ K, if 2·(102·C₀·c)² ≤ ⌊log₂ n⌋ and n < K^(17·C₀). 

### `StBetaU`

 What is used of β = `betaU k s`. 
