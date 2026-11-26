---
{
  "module": "proof/consequences/CircuitLowerBound/Inf.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Inf.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Inf.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7) at infinitely many lengths

`ENP.allDecided`: every set of words of length n is decided by some circuit. The proof extends a
given circuit: a function of the input is AVAILABLE in a circuit if some wire carries it; every
circuit can be extended so that a given function
becomes available (`Ext`), first for the input bits and the constants, then for any function of two
functions that have this property, then, by induction on k, for every function that depends on the
first k input bits only.
`ENP.infinitely_often`: if for some c all lengths n ≥ N had circuits with at most c·(n+1) gates, the
finitely many lengths below N could be paid for by a larger c; so a language without circuits of
linear size fails at infinitely many lengths, for every c. 

### `Avail`

 Some wire of the circuit carries g x on every input x of n bits. 

### `Avail.gate`

 One more gate. 

### `Ext`

 Every circuit can be extended so that g becomes available. 

### `ext_of_dep`

 Every function that depends on the first k input bits only can be made available. 

### `ENP.allDecided`

 Every set of words of length n is decided by some circuit. 

### `ENP.infinitely_often`

 A language that is not decided by circuits of linear size fails at infinitely many lengths, for
every c. 
