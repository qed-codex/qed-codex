---
{
  "module": "proof/rates/PaddedDescent/F/MarkLayers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkLayers.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/F/MarkLayers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The choice of the layers

The clauses of a formula ψ are divided into R + 1 layers, one clause at a time, so that the layers
are good (`Good`): an assignment that satisfies all later layers violates
at most w clauses of a layer. A clause C is offered to the layers in turn. Layer Λ, with the later
layers `rest`, takes C («drops» it) if the sum `BB`, over the assignments that
satisfy `rest` and violate C, of 2^(number of violated clauses of Λ) is small enough (`dropC`);
otherwise C is passed on, and the last layer takes whatever reaches it.

* `Inv` is the inequality that this rule keeps (`Inv.placeM`), in natural numbers: X·2^(κ+d+2) +
  3^κ·2^w ≤ 2^(w+κ+d+1), where X = `XX` is the sum of
  2^(number of violated clauses of Λ) over the assignments that satisfy `rest`, κ is the number of
  clauses in `rest` and d the number in Λ. It holds at the start if n + 2 ≤ w.
* It gives goodness (`InvS.nvio_lt`, `Inv.good`) and 3κ ≤ 2(κ+d) + 5 (`InvS.size`), so the last of R +
  1 layers has at most (2/3)^R·|ψ| + 5 clauses (`Inv.last_le`).
* The sum `BB` is the difference of two evaluations `trunc`, with and without C in the layer
  (`trunc_sub_trunc`).
* `layersE` (`proof/rates/PaddedDescent/F/MarkMath.lean`) is the same procedure with any function
  `ev` in place of `trunc`. If `ev` agrees with `trunc` on the lists of layers
  described by `Asked`, then the procedure builds the same layers (`layersE_eq_layersM`), and `ev`
  of these layers, with an empty layer in front, is the number of
  assignments that satisfy ψ (`ev_layersE`). This is `StLayersE`, one of the interface statements of
  `proof/rates/PaddedDescent/F/Interfaces.lean`. 

 ### Small facts on lists and powers 

### `nvio_cons`

 One more clause in a layer: one more violated clause if σ violates it. 

### `drop_step`

 The arithmetic of a drop: X grows by B and d by 1. 

### `keep_step`

 The arithmetic of passing on: X falls by B and κ grows by 1. 

### `size_step`

 3^κ ≤ 2^N gives 3κ ≤ 2N + 3, because 8 ≤ 9. 

### `drop_eq_cons`

 The layers from number i on begin with layer number i. 

### `getLastD_drop`

 The layers from number i on have the same last layer. 

### `flatten_drop_sublist`

 The clauses of the layers from number i on are among the clauses of all layers. 

 ### The rule and its invariant 

### `satL`

 σ satisfies all layers. 

### `decSatL`

 Whether σ satisfies all layers can be decided. 

### `XX`

 Σ over the assignments that satisfy rest of 2^(violated clauses of Λ). 

### `BB`

 Σ over the assignments that satisfy rest and violate C of 2^(violated clauses of Λ). 

### `InvS`

 The inequality kept for a layer Λ and the layers after it: κ clauses after it, d in it. 

### `Inv`

 The inequality for every layer but the last. 

### `dropC`

 Is C dropped into Λ? 

### `decDropC`

 The test can be decided. 

### `placeM`

 C goes into the first layer that drops it, else into the last. 

### `placeM_ne_nil`

 The placement does not remove layers. 

### `satL_cons`

 σ satisfies L :: Ls exactly if it violates no clause of L and satisfies Ls. 

### `satL_placeM`

 After the placement of C the layers are satisfied exactly if they were before and C is not
violated. 

### `length_flatten_placeM`

 The placement adds one clause. 

### `length_placeM`

 The placement keeps the number of layers. 

### `XX_cons`

 Dropping C into Λ adds B. 

### `XX_keep`

 Keeping C, that is passing it on to the later layers, subtracts B. 

### `Inv.placeM`

 Placing a clause keeps the invariant. 

### `inv_replicate`

 The start: empty layers. 

### `InvS.nvio_lt`

 From the inequality: an assignment that satisfies the later layers violates fewer than w clauses
of Λ. 

### `Inv.good`

 The invariant and a short last layer make the layers good. 

### `InvS.size`

 From the inequality: the later layers hold at most about two thirds of the clauses. 

### `Inv.last_le`

 The last of R + 1 layers holds at most (2/3)^R of all clauses, and 5 more. 

 ### What the test evaluates 

### `trunc_eq_XX`

 One evaluation on good layers, as a natural number. 

### `Inv.good_trial`

 The layers with C on trial in the first of them are good. 

### `trunc_sub_trunc`

 The quantity of a decision: the difference of two evaluations is the sum BB. 

 ### Suffixes 

### `Inv.drop`

 The invariant passes to the layers from number i on. 

 ### The placement by position 

### `placeM_eq_placeAt`

 The placement by recursion is the placement into the first layer whose test holds, or else the
last. 

 ### All clauses 

### `layersM`

 The layers of ψ: R + 1 of them. 

### `layersM_append`

 One more clause at the end of ψ is placed last. 

### `length_layersM`

 There are R + 1 layers. 

### `layersM_ne_nil`

 There is at least one layer. 

### `inv_layersM`

 The layers of ψ satisfy the invariant. 

### `length_flatten_layersM`

 The layers of ψ have as many clauses as ψ. 

### `satL_layersM`

 The layers of ψ are satisfied exactly if no clause of ψ is violated. 

### `last_layersM_le`

 If 2^R·|ψ| + 5·3^R ≤ 3^R·c, the last layer has at most c clauses. 

### `good_layersM`

 The layers of ψ are good. 

### `trunc_layersM`

 The final evaluation is the number of assignments that satisfy ψ. 

 ### The same with an evaluation function in place of the sums 

### `placeE_eq_placeM`

 With the invariant, a short last layer and exact evaluations, the placement by evaluations is
the placement by sums. 

### `perm_flatten_placeM`

 After the placement of C the clauses of the layers are C and the clauses before, in some order. 

### `perm_flatten_layersM`

 The clauses of the layers of ψ are the clauses of ψ, in some order. 

### `layersE_append`

 One more clause at the end of ψ is placed last. 

### `layersE_eq_layersM`

 If the evaluation is exact on the lists on which it is used, the layers by evaluations are the
layers by sums. 

### `ev_layersE`

 If the evaluation is exact on the lists on which it is used, the last evaluation is the number
of assignments that satisfy ψ. 

### `stLayersE`

 `Mark.ev_layersE`, in the form of the interface statements of
`proof/rates/PaddedDescent/F/Interfaces.lean`. 
