---
{
  "module": "proof/networks/Eight/ViaGrouping/Keeps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Keeps.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Keeps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The algorithm of the proof of Lemma 1 has polynomial-time steps

A bound on the number of steps of a step machine says something only if each step is cheap. This
file shows that every step of `netAlg K g E` is computable in polynomial time (`IsPolyT`) if the
steps of the four procedures of Definition 2(iii) and of
the algorithm E for cliques are, and the numbers P_a, c_{a,b} and P are given in unary (`KeepsP`):
`stKeeps : StKeeps`.
The parts, in the order of proof/networks/Eight/ViaGrouping/Defs.lean: the plain functions `lamP`
(polynomial-time, and of polynomial size even in unary: E is given L in unary), `goodP` (one test of
a grouping, which the search counts as one step), `qMb`, `qPsi`; then
the machines `wM`, `psiP`, `fM`, `termP`, `tableM`, `searchP`. The certificates of the plain
functions that cut a setting of a group and a string Θ(γ') into their parts are those of
proof/machines/ToTuring/Poly/NetFun.lean. 

 ## The plain functions 

### `lamP_polyT`

 L is computable in polynomial time. 

### `lamP_unary`

 L is computable in polynomial time even if written in unary, since L ≤ 1 + K·U + g·P and the
numbers c_{a,b} and P are given in unary. 

### `g1_polyT`

 The test (G1) is computable in polynomial time. 

### `g2_polyT`

 The test (G2) is computable in polynomial time. 

### `goodP_polyT`

 The test of a grouping, (G1) and (G2), is computable in polynomial time. 

### `qMb_polyT`

 The query (b, z_b) is computable in polynomial time. 

### `qPsi_polyT`

 The query ((a, b), (z_a, z_b)) is computable in polynomial time. 

 ## The machines 

### `wM_isPolyT`

 [z_a ∈ S_a]·W_a(z_a) has polynomial-time steps. 

### `psiP_isPolyT`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b) has polynomial-time steps. 

### `fM_isPolyT`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}) has polynomial-time steps. 

### `termP_isPolyT`

 One factor of a term of W̃_γ(Θ) has polynomial-time steps. 

### `tableM_isPolyT`

 One entry W̃_γ(Θ) has polynomial-time steps. 

### `searchP_isPolyT`

 The search through the K^g groupings has polynomial-time steps. 

### `stKeeps`

 **The algorithm of the proof of Lemma 1 has polynomial-time steps** if the algorithm E for
cliques has: whenever the four procedures have polynomial-time steps and P_a, c_{a,b}, P are given
in unary, so has `netAlg K g E` on them. 
