---
{
  "module": "proof/rates/PaddedDescent/F/MarkMath.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkMath.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkMath.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Marks and layers, part 1: the sums

The clauses of a formula are divided into layers. For an assignment σ and a layer L let v be the
number of clauses of L that σ violates. The alternating sum
Σ_j (−1)^j·C(v, j) is 1 if v = 0 and 0 otherwise; cut off at j ≤ w it is still that if v ≤ w. If
every assignment that satisfies the later layers
violates at most w clauses of a layer (`Good`), the product of the cut-off sums over the layers is 1
at the satisfying assignments and 0 elsewhere.
This file has definitions only. 

### `Cl`

 A clause: a list of literals (variable, the value that makes the literal true). 

### `vio`

 σ makes every literal of C false. 

### `nvio`

 The number of clauses of L that σ violates. 

### `Tpl`

 Σ_{j ≤ w} C(v, j). 

### `Tsg`

 Σ_{j ≤ w} (−1)^j·C(v, j). 

### `ext`

 An assignment of the variables below n, continued by false. 

### `trunc`

 The sum that one evaluation computes: the first layer without signs, the others with signs, all
cut off at w. 

### `Good`

 Every assignment that satisfies the later layers violates at most w clauses of a layer. 

### `nSat`

 The number of assignments of the variables below n that satisfy ψ. 

### `occ`

 The clauses of x in which the variable v occurs. 

 ### The choice of the layers, for any evaluation function ev in place of `trunc n w` 

### `dropE`

 Is the clause C put into layer i? When ev is `trunc n w` and both lists are good, the difference
of the two evaluations is the sum, over the assignments
that satisfy the later layers and violate C, of 2^(number of violated clauses of layer i). 

### `placeAt`

 Ls with the clause C added to layer i. 

### `placeE`

 C goes into the first layer whose test holds, else into the last. 

### `layersE`

 The clauses of ψ, placed one after the other into R + 1 layers. 

### `Asked`

 The lists of layers on which the choice of the layers of ψ uses the evaluation: good, at most R +
2 layers, and their clauses are clauses of ψ, counted
with repetition. 
