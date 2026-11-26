---
{
  "module": "proof/consequences/CircuitLowerBound/Tab/Spec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Spec.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Tab/Spec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): what the table of a machine says (definitions only)

A run of one of Mathlib's multi-stack machines is written as a table of rows, one row for each time
t = 0, …, 2^b. A row holds the label, the state, and for every stack k and every position q the
symbol at depth q below the top of the
stack (or «blank»). One step of the machine sees only the top d symbols of each stack and replaces
them by at most 2d symbols; the rest of the stack is shifted. `Spec` lists the conditions on the
rows; each of them is a clause of at most
three literals that is repeated for all times t and all positions q. 

### `ops`

 The largest number of stack operations on a path through a statement. 

### `pref`

 The symbols of a list of cells up to the first blank. 

### `dep`

 The number d of symbols at the top of a stack that one step can see: at least 1. 

### `lamOf`

 By how many bits positions are longer than times. 

### `Win`

 The top d cells of every stack. 

### `Case`

 What one step depends on: label, state, the top d cells of every stack. 

### `nc`

 The number of cases. 

### `ec`

 The cases in some order. 

### `nxt`

 The step of the machine on the tops alone; a halted machine stays as it is. 

### `Atom`

 The kinds of statements about a row: «the label is l», «the state is v», «the new top of stack k
has n symbols», «the cell of stack k at this position holds x», «the case is γ», «the case is among
the first i», «this position is at most P». 

### `Spec`

 The conditions. α a t q is the truth value of the statement a at time t and position q;
statements about a whole row stand at position 0. 

### `Spec.preTop`

 at every time before the last some case holds 

### `Spec.csLab`

 the case that holds is that of the row 

### `Spec.nxLab`

 the case fixes label, state and the new tops of the next row 

### `Spec.copy`

 below the new top the stack is what lay below the old top 

### `Spec.iLab`

 the first row: the machine is started on 1^P 0 y 

### `Spec.fLab`

 the last row: halted, with the output 1 

 ### The statements of this group 

### `lits`

 The three literals of a clause of a table. 

### `GoodCode`

 The kinds are at least 1 and fit into kb bits, and the numbers added to positions are at most
2^lam. 

### `holdsT`

 A literal of a table holds in the shift by (t, q). 

### `SatT`

 Some truth values of the triples (kind, time, position) satisfy all shifts of the clauses. 

### `StPack`

 Triples and numbers of variables: the formula of a table is satisfiable if and only if its
clauses are, read with triples. 

### `StSpec`

 The conditions hold for some truth values if and only if the machine accepts. 

### `StSpecTab`

 The conditions are the shifts of a table. 
