---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Coefficients.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Coefficients.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Tables/Coefficients.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The tables of the coefficients of Schönhage's identity

Section 2.2 defines, for each of the ten terms λ of Schönhage's identity, two linear forms φ_λ and
ψ_λ in seven variables each; step (2) of the recursion applies them.  coef(phi) writes the
coefficient φ_λ(s) of the variable number s < 7 in the form of the term number λ < 10 to the cell
phi + 7 λ + s, and ψ_λ(t) to the cell phi + 70 + 7 λ + t.  The body is a straight line of 140
stores, made from the two tables `Spec.phiTable` and `Spec.psiTable`.  `storeSigns_spec` treats
such a line of stores by induction on the list, and `coef_entry`, the specification that the callers
of the procedure assume, applies it to the two tables.


### `signExpr`

 A coefficient as an expression: 1, 0, or 0 - 1. 

### `Coef.Dest`

 The only local variable of coef: its argument phi. 

### `storeSigns`

 Stores the numbers of the list l, each of them 1, 0 or -1, into the cells from phi + i on. 

### `coefBody`

 coef(phi). 

### `signExpr_gives`

 A coefficient's expression stays within the limits and gives the coefficient. 

### `signExpr_cost`

 A coefficient's expression costs at most 3 steps. 

### `storeSigns_spec`

 **storeSigns** writes the list to the cells from base + i on, changes nothing else, and takes
at most 7 steps for each number. 

### `coef_signs`

 All coefficients are 1, 0 or -1. 

### `coef_entry`

 **coef** writes the two tables and changes nothing else, in 7 · 140 steps: the specification
that its callers assume. 
