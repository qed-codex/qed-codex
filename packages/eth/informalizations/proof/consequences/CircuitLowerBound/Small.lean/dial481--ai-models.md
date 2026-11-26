---
{
  "module": "proof/consequences/CircuitLowerBound/Small.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Small.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Small.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): small facts

The chains (`stChain`), the size of the variables of the formula of a table (`stVars`), the search
for a satisfying assignment (`stGreedy`), and the numbers of tables (`stCode`). 

 ### The chains 

 ### The search 

### `sat_greedy`

 The values found so far can always be continued to a satisfying assignment. 

 ### Numbers of tables 

### `bits_foldr`

 A word that ends with 1 is the list of binary digits of a number. 

### `fld_flatten`

 The i-th number of W bits in a word that begins with numbers of W bits. 

### `n5`

 The five numbers of a literal. 

### `n15`

 The fifteen numbers of a clause. 

### `getD_flat15`

 Entry 15·r + i of the numbers of a list of clauses. 

### `stChain`

 The chains. 

### `stVars`

 The variables of the formula of a table have L bits. 

### `stGreedy`

 The search finds a satisfying assignment if there is one. 

### `stCode`

 Every table has arbitrarily large numbers. 
