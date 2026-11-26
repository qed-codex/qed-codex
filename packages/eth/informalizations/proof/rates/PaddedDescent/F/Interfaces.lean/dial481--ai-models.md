---
{
  "module": "proof/rates/PaddedDescent/F/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Interfaces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The interface lemmas, as PROPOSITIONS

The main lemmas that connect the files of this folder are written here as definitions `St… : Prop`.
Nothing is proved and nothing is assumed: this
file has no theorem. One file proves `theorem … : St…`. A file that needs such a lemma either
imports that file or takes `(h : St…)` as a hypothesis; in
the second case the final assembly (proof/rates/PaddedDescent/Main.lean) feeds the proof in. No file
contains a placeholder proof. 

### `WFQ`

 θ is a well-formed query at v: labels of ℓ bits, the empty word at v itself. 

 ### Table.lean 

 ### RebalF.lean: the rebalancing, from a network on g nodes to an explicit instance on K nodes 

 ### RebalG.lean: the rebalancing at the levels, on a grid of side g = K·L 

### `StRG`

 `StR` for `rebalG`: the label length β is given. 

 ### SideF.lean and Expand.lean: one level 

### `StChild`

 One pattern: the core of `StE`. 

 ### Descend.lean: brute force at the bottom, and all levels 

 ### MarkLayers.lean: the choice of the layers 

### `StLayersE`

 If the evaluation function is exact on the lists that are asked, the cap is at least n + 2 and
there are enough layers, then the last evaluation is the
number of satisfying assignments. 

 ### MarkCode.lean: the code of the labels 

 ### MarkVal.lean, MarkProf.lean, MarkPi.lean, MarkSize.lean: the network of marks 

### `StMarkVal`

 The value of the network of one profile, admissible or not. 

### `StProfSum`

 Every set of clause indices has exactly one profile number whose digits below the diagonal are
0; that number is admissible iff no layer has more than w
members of the set. 

### `StPiSum`

 The signed sum over the sets of violated clauses with at most w members in every layer. 

### `StMarkSum`

 The central identity: the values of the networks of the admissible profiles add up to the
cut-off sum. No hypothesis on the layers beyond their form. 

### `StMarkSized`

 The size of the network of an admissible profile, if every variable occurs in at most Δ clauses
and there are at most b·(n + 1) clauses. 

 ### Eval.lean and Top.lean: one evaluation, one sparse formula, the sparsification tree, the whole function 

### `StValF`

 `valF` computes the value of every network that F presents, if its entries are 0, 1, −1 and the
pad is long enough. 

### `StEval`

 One evaluation is exact: at most R₁ layers, which together hold at most m clauses, every
variable in at most Δ of them. 

### `StCountM`

 `countM k` counts the satisfying assignments of a formula with clauses of 1 to k literals. 

### `StLeaf`

 Every leaf of the sparsification tree at width k has nonempty clauses only, and every variable
occurs in at most leafC τ k of them. 

### `StCorrect`

 The end of the correctness side; this is the last hypothesis, `h`, of `inRateTM_of_algorithm`
(proof/rates/PaddedDescent/Reduce.lean). 

 ### The arithmetic (the files Arith*.lean): the pad is long enough 

### `StA`

 The part of the arithmetic that does not know the width: for sOf n ≥ 1 the pad of length
2^(8·(⌊n/2^(sOf n)⌋ + 1)) suffices for all evaluations, for every width
k ≤ sOf n and every bound Δ ≤ 2^(betaOf (sOf n)) on the number of clauses in which a variable
occurs, and for the computation of the schedule. 

### `StAW`

 The part of the arithmetic that knows the width k: for sOf n ≥ s0K k, the width is at most sOf
n, a variable occurs in at most 2^(betaOf (sOf n)) clauses of a leaf of the
sparsification tree (with 2 to spare), and the pad of length 2^(8·(⌊n/2^(sOf n)⌋ + 1)) suffices for
the rounds of the walk through the tree and for its stack. 

 ### The polynomial-time certificates (the files Cert*.lean) 

### `FKeeps`

 The lengths of a network are given in unary and its two functions are polynomial-time. 

### `StCertRebalG`

 `StCertRebal` for `rebalG`: jointly also in the label length β, in unary. 
