---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Run.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Run.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Run.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the checks as a computation: the run

The run decides the m·r pairs (check, clause) one after the other; each time it takes the option
with the smaller numerator of the truncated potential. This file proves that it ends with good
checks that satisfy the three bounds (`run_ok`).

The invariant: after t decisions the potential is at most 1/2 + t·(2δ), where δ bounds the error of
the truncated potential; by the hypothesis on the parameters this stays below 3/4. One decision:
both
options are states that satisfy the bounds for states that are tried, because the state reached has
a potential below 1 and they have at most one pair more; so the two functions give the right
integers, the numerators over the common denominator are the truncated potentials, and the option
taken has a potential of at most the smaller potential plus 2δ, which is at most the old potential
plus 2δ, because the old potential is a mean of the two. From one check to the next the potential
does not grow. 

### `OrcOK`

 The two functions are right, modulo 2^β, in every state that satisfies the bounds for states
that are tried. 

 ### Lists and sets 

 ### The bounds for states that are tried 

### `Bd`

 The three bounds that a potential below 1 gives. 

 ### The potential of a state of the run 

### `UU`

 The potential of the state (Ls, cur, e). 

### `tUU`

 The truncated potential of the state (Ls, cur, e). 

### `NN`

 The bound on Σ_ξ ω(ξ). 

### `abs_tUU_sub`

 The truncated potential differs from the potential by at most δ = ε·N/2. 

### `bd_of_lt_one`

 A potential below 1 gives the three bounds. 

### `num_congr`

 The numerator uses the B_i with i ≤ i₀ only. 

### `numO_div_den`

 In a state that satisfies the bounds for states that are tried, the numerator that the run
computes, over the denominator, is the truncated potential. 

 ### One decision 

### `Inv`

 What is known of a state that the run has reached, after t decisions. 

### `Inv.lt_one`

 In a state that the run has reached the potential is below 1 (the proof gives below 3/4). 

### `Inv.tent`

 Both options of a decision satisfy the bounds for states that are tried. 

### `Inv.step`

 One decision keeps the invariant. 

 ### One check, all checks 

### `inv_runTo`

 The decisions for one check keep the invariant. 

### `inv_runChecks`

 At the beginning of every check the invariant holds. 

### `run_ok`

 The result of the run: r checks, each a list of clauses without repetition; they are good; and
the three bounds hold. 
