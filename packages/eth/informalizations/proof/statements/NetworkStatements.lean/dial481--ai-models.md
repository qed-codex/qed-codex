---
{
  "module": "proof/statements/NetworkStatements.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/NetworkStatements.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/NetworkStatements.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Definitions for a recursion with single-bit pieces, which the paper does not use

This file holds definitions only, for a variant of the recursion that the paper does not state: the
crossing is uncrossed bit by bit,
[x=v][y=u] = [x=u][y=v] − s(x,y)·s(u,v), as in Appendix H, and the pieces A_i group the terms by the
number of uncrossed bits; the constant ρ = ¼ log₂ 12
(the count by ranks for single bits in Appendix H) takes the place of the paper's ρ = 11/12. It also
defines the value Z of a clique of tensors, arithmetic formulas, the bound `Within`, and labels by
strings of Bell states.
It imports Mathlib and `ThreeSatStatement` only. `n` stands for λ throughout.

Time. The paper measures the time of an algorithm. In `Within` time is replaced by a measure that
needs no
machine: the size of an arithmetic formula (+, ×, integer constants) that computes Z from the
entries of the tensors.
This is a non-uniform measure, so `Within` is a statement on tensor networks, not on 3-SAT: a
constant of any size counts as one leaf, the bit lengths of the entries play no role, and a formula
gets for free what an
algorithm has to search for or decode. On the other hand a formula is a
tree: nothing computed once can be used twice. 

 ## The problem 

### `Bits`

 A λ-bit index. 

### `Tensors`

 An arbitrary tensor for every node of the complete graph on `J`: `W v h` is the entry of the
tensor of `v` at the
indices `h w` of the edges {v,w}. The argument `h v` is a dummy: `Z` reads only entries where it is
0…0. 

### `edgeIndices`

 The ways to give every edge an index: `x a b = x b a` is the index of the edge {a,b}, and
`x a a` is 0…0. 

### `Z`

 Z = Σ ∏_v W_v, summed over all index bits. 

### `N`

 N = C(K,2)·λ, the number of index bits. 

### `Formula`

 Arithmetic formulas over the variables `V`. 

### `Formula.eval`

 The value of a formula. 

### `Formula.size`

 The size of a formula: its number of leaves. 

### `Entry`

 The variables of the problem: one for every entry of every tensor. 

### `Formula.ComputesZ`

 The formula `φ` computes Z, for all tensors. 

### `Within`

 Formulas of size 2^{eN}·poly(λ) compute Z, for fixed K and all λ: formula size in place of time.
The constant `C` may
depend on `K` and `e`, not on λ. 

### `ρ`

 ρ = ¼ log₂ 12. 

 ## Uncrossing 

### `s`

 s(p,q) = (−1)^p [p ≠ q]. 

### `X₁`

 One bit of the crossing: [x = v][y = u] (the two diagonals of the rectangle with x, y on top and
u, v below). 

### `I₁`

 One bit of the uncrossed term: [x = u][y = v] (the two vertical sides). 

### `cross`

 The crossing of two λ-bit diagonals: [x = v][y = u]. 

 ## Grouping 

### `A`

 A_i: the sum, over the sets S of i bit positions, of the product of −s(x_k,y_k)·s(u_k,v_k) for k
∈ S and [x_k = u_k][y_k = v_k] for the other k. 

### `Bell`

 The names of the four Bell states: (false,false) is Φ⁺, (false,true) is Φ⁻, (true,false) is Ψ⁺,
(true,true) is the singlet. 

### `singlets`

 The number of singlets in a string. 

### `others`

 The number of states other than Φ⁺ in a string. 

### `rowLabels`

 The strings with at least i singlets. 

### `colLabels`

 The strings with at most i states other than Φ⁺. 
