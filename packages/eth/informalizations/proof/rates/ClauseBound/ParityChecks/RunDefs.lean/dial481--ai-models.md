---
{
  "module": "proof/rates/ClauseBound/ParityChecks/RunDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/RunDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/RunDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the checks as a computation: definitions

The clauses are 0, …, m − 1. A check is the list of its clauses. A state of the choice is (Ls, cur,
e): the complete checks, the part of the current check chosen so far, and the number e of
clauses already decided for it. The sums over marked sets are not computed here: they come from two
functions (`orcA`, `orcB`), which are parameters. The four terms of the truncated
potential are written over one common denominator, which does not depend on the decision, so that a
decision compares two integers. Lists, natural numbers and integers only, except for the
translation to the sets of `ParityChecksStatement.lean`. 

### `Chk`

 A check: the list of its clauses. 

### `lam`

 The checks as sets. 

### `Dset`

 The clauses not yet decided: e, …, m − 1. 

 ### The integers that are compared 

### `bal`

 The representative of a modulo 2^β in [−2^{β−1}, 2^{β−1}). 

### `Par`

 The parameters of the choice: (m, nb, r, i₀, β). 

### `k`

 The number of later checks. 

### `den`

 The common denominator of the four terms in a state with j complete checks. 

### `numP`

 A·nb^{i₀} + Σ_{i ≤ i₀} (−2)^i·nb^{i₀−i}·B_i. 

### `colOf`

 The number of checks among Ls and cur that contain the clause x. 

### `numI`

 I·nb + (number of undecided pairs). 

### `numR`

 Σ_{j'} 2^{|Λ_j'|}·nb^{c}·(nb+1)^{m−c}, c the number of clauses decided for check j'. 

### `numC`

 Σ_x 2^{col(x)}·nb^{c}·(nb+1)^{r−c}, c the number of checks for which x is decided. 

### `num`

 The numerator of the truncated potential over `den`. 

 ### The run 

### `numO`

 The numerator in the state (Ls, cur, e), with A and the B_i taken from the two functions and
reduced modulo 2^β. 

### `decide1`

 One decision: the clause e goes into the current check if that does not give the larger
numerator. 

### `runTo`

 The first e decisions for one check. 

### `runChecks`

 The first j checks. 

### `run`

 All checks. 

### `Tent`

 The bounds that hold in every state that is reached, and with one more pair in every state that
is tried. 

### `Hyp`

 What the run needs of the parameters, for a set X of assignments. 
