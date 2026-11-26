---
{
  "module": "proof/rates/ClauseBound/TopN/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From an algorithm for cliques to #k-SAT on n variables: definitions and interface statements

The Lean form of part (a) of the theorem of Appendix D. Given: a solver `S` for cliques
(`ClauseBound.Alg.Solver`) with a sequence of levels `Q : S.Seq e C₀`, and a function `slU` that
gives, for the level l, an integer s with 2^(−s) ≤ e_l and 2^s ≤ (2/e_l)^C. For n variables the
function picks the largest level l with K_l ≤ n^(1/17), sets s = s(l),
sparsifies with the threshold τ = 2^(4s+17) (walking the counting tree with `walkS`), and counts
every leaf by the networks of marks of `proof/rates/PaddedDescent/F/MarkNet.lean`,
each of which is rebalanced to K_l nodes and handed to the solver (`valS`). Here the code parameter
β is linear in s, with a slope that depends on the width k, so that a network
has O_k(n·s²) shared bits.
The exponent of the pad is computed from the input under the bound n; if it would be larger than n,
or if s is too small for the width k, or if 2^β > n + 1, the
function counts exhaustively. This file has definitions only. The statements `St…` are propositions. 

 ### One sparse formula, for any way `val` to evaluate a network of marks 

### `evalV`

 One evaluation: the sum of `val` over the admissible profiles. gu is the number of nodes in
unary; p = (n, w, β, b) in unary, as for `PaddedDescent.F.evalF`. 

 ### The parameters for width k and precision s 

### `betaN`

 The code parameter: 2^(betaN k s) is at least the number of clauses per variable of a leaf of
the sparsification tree for width k with the threshold 2^(4s+17). 

### `layersN`

 The number of times that the set of clauses is divided into a layer and a rest. 

### `blockN`

 2^β, cut off at n + 1. The function uses the networks only if 2^β ≤ n + 1, and then this is 2^β.
The cut-off keeps the number small enough to be written in unary. 

### `UbN`

 The bound on the number of shared bits of a network of marks on 3K⁸ nodes. 

### `PbN`

 The bound on the size of a network of marks on 3K⁸ nodes. 

### `root17`

 ⌊n^{1/17}⌋ in unary. 

 ### The exponent of the pad 

### `needNetC`

 `needNet` computed under the bound b; `none` if the exponent of the solver is larger than the
bound. 

### `idxN`

 The index of the level picked for the input x. 

### `precN`

 The precision picked for the input x. 

 ### Budget.lean: what a pad of length 2^(restN …) suffices for 

### `StParN`

 The parameters are large enough for width k: clauses per variable, number of layers. 

 ### Walk.lean: the walk through the counting tree, for any way `val` to count a leaf 

### `StWalkCount`

 If `val` is right on every node that has the properties of a leaf of the counting tree, and the
pad suffices for the rounds and for the stack, the walk returns the number of
satisfying assignments. 
