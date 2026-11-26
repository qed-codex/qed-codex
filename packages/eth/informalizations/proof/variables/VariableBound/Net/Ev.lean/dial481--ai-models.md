---
{
  "module": "proof/variables/VariableBound/Net/Ev.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Ev.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Ev.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3 of Appendix D: the programs for X(𝓛) and F(𝓛) are right

Proves `VariableBound.Net.StEvD` and `VariableBound.Net.StEvXF` from statements on the parts.

* One evaluation `evD` adds, over the admissible profiles, the numbers that the clique solver
  returns for their networks. The solver returns the value of the network
  (`ClauseBound.Alg.StValS`), because the functions `netD` present it
  (`StPresents`), its parameters and its total are within the bounds `PbD`, `BbD`, `UbD` (`StSize`)
  and the pad, the string of ones by which, as Appendix E says, the Lean proofs render a number of
  operations as time, is long enough. The sum of the values is the right side of display (65)
  (`StTotal`).
* By display (65) the right sides are congruent to X(𝓛) modulo 2^β and to F(𝓛) modulo 2^(n+1), and
  «the residues determine the numbers»: 0 ≤ X(𝓛) ≤ 2^n·C(m, n̄+1) ≤ 2^(β−1), and 0 ≤ F(𝓛) ≤ 2^n if
  X(𝓛) = 0. 

### `presents`

 The functions `netD` present the network of the profile y on g nodes, given `StPresents`. 

### `stEvD`

 Step 3 and Step 4: one evaluation is the right side of display (65). Hypotheses of the statement
(`StEvD`): the solver is right at the indices with `ok`, ok i, K ≥ 2, the list is fit for an
evaluation (`Fit`), and the pad is at least as long as the number `nPr` of numbers tried as profiles
and as 2^`needNet` for the bounds `UbD`, `PbD`, `BbD`. Derived from: the solver returns the value of
a network that is presented and within the bounds (`ClauseBound.Alg.StValS`), and the statements
`StPresents`, `StTotal` and `StSize` on the networks of the profiles. 

### `emod_eq_of_modEq`

 A number in [0, N) is the remainder modulo N of every number congruent to it. 

### `stEvXF`

 Step 1, display (65) and «the residues determine the numbers», for the programs: they compute
X(𝓛), and F(𝓛) if X(𝓛) = 0. Hypotheses of the statement (`StEvXF`): those of `StEvD` (solver right,
ok i, K ≥ 2, `Fit`, the two conditions on the pad), M ≥ β − 1 + r and M ≥ n + r, with β = n + ⌈log
C(m, n̄ + 1)⌉ + 1. Derived from: one evaluation is the right side of display (65) (`StEvD`), display (65)
(`AppVariables.XFStmt`), the bounds on X and F (`AppVariables.ResiduesStmt`), and that the list of
sets has as many checks as the list of lists (`StChks`). 
