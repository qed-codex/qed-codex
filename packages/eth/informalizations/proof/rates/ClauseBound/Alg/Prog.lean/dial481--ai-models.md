---
{
  "module": "proof/rates/ClauseBound/Alg/Prog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Prog.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Prog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The definitions, part 2: evaluation by enumeration, one level, all levels, and what they need of the pad 

 ### A network evaluated by enumeration of all labels 

### `enumLen`

 The length of the chunk number j = a·g + b of the word that holds one label for every pair a <
b. 

### `enumBits`

 The number of bits of that word: U/2. 

### `enumF`

 Z = Σ_θ ∏_a Σ_{z_a} W_a(z_a) ∏_{b ≠ a} f_ab(z_a, θ_ab). 

 ### One level 

### `gctx`

 The context of the network of the pattern y of the instance I. 

### `nPat`

 The number of patterns. 

### `sumDig`

 Σ_q ι(q). 

### `colSide`

 Is the column network taken for the pattern y? 

### `capSum`

 The largest sum of the two numbers of bits of a piece. 

### `Nof`

 N = (pd)²λ. 

### `ubarG`

 An upper bound for U of every network that is rebalanced at this step. 

### `ebarG`

 An upper bound for U/2 of every column network that is evaluated by enumeration at this step:
e·X is written 8·√(b·X²/a). 

### `lamNextG`

 The label length one level down. 

### `childG`

 The instance on K nodes that the pattern y leads to. 

### `expandG`

 One level: the sum of the terms that are evaluated at once, and the instances on K nodes of the
other terms. 

 ### All levels 

### `DState`

 ((sum so far, common factor so far), label length in unary, work list): factor · Z = sum + Σ of
the values of the work list. 

### `solveG`

 The value of the instance I on the nodes of the first step of sched; K₀ is the number of nodes
after the last step. 

 ### What a step needs 

### `PnG`

 P of the networks that are rebalanced. 

### `bNextG`

 An upper bound for the bit length of the entries one level down. 

### `BudG`

 What one step needs of the length F of the pad. 
