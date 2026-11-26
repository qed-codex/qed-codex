---
{
  "module": "proof/rates/ClauseBound/TopN/EvalW.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/EvalW.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/TopN/EvalW.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The sum over the profiles with a weight that depends on the numbers of marks per layer

In the network of ONE profile y the number of marks in layer i is fixed: it is `tl g Ls y i`, the
sum over the nodes of the numbers of marks that the profile lets them own. So a weight
and a condition that depend only on these numbers can stay outside the network.
`evalV_weight`: let G be a function of the numbers of marks of the layers. One evaluation in which
the value of the network of the profile y is multiplied by G (tl g Ls y) is the sum, over the
assignments σ and the sets P of clauses that σ violates, with at most w members in every layer, of G
(numbers of members of P in the layers) times the sign of P. The proof is that of
`Mark.Sum.stMarkSum`: exchange the sums, use the value of one network for each y and the sum over
the profiles for each P. The extra step is `tl_eq_card`: if P has the profile y then
tl g Ls y i is the number of members of P in layer i, because every clause has exactly one owner.
`evalV_truncW`: for the weight `GW`, which is ∏_i (ws_i·s_i)^(t_i) if lo_i ≤ t_i ≤ hi_i for all i
and 0 otherwise, with s_0 = 1 and s_i = −1 for i ≥ 1, and for hi_i ≤ w, that sum is
`truncW`: Σ_σ ∏_i Σ_{lo_i ≤ j ≤ hi_i} ws_i^j·C(number of violated clauses of layer i, j). The signs
s_i cancel the sign of P, and P is chosen layer by layer.
`evalV_truncW_ctx` is the same for an evaluator that reads the number of nodes and the number of
layers from the context of the network, so that one evaluator serves all lists of layers. 

 ### Definitions 

### `tl`

 The number of marks in layer i that the profile y prescribes. 

### `GW`

 The weight ∏_{i < R} (ws_i·s_i)^(t_i), s_0 = 1, s_i = −1 for i ≥ 1, if lo_i ≤ t_i ≤ hi_i for all
i < R; 0 otherwise. 

### `truncW`

 Σ_σ ∏_i Σ_{lo_i ≤ j ≤ hi_i} ws_i^j·C(number of violated clauses of layer i, j). 

 ### The sum over the profiles 

### `tl_eq_card`

 If P has the profile y, the profile prescribes for layer i the number of members of P in layer
i. 

### `evalV_weight_aux`

 `evalV_weight` with the four parameters n, w, β, b named. 

### `evalV_weight`

 One evaluation with the weight G of the numbers of marks per layer is the sum over the
assignments σ and the sets P of violated clauses with at most w members in every layer of
G (numbers of members of P in the layers) times the sign of P. 

 ### The product form 

### `prod_map_range`

 A product over `List.range` is the product over `Finset.range`. 

### `sum_powerset_Icc`

 The sum of s^|P| over the subsets P of S with lo ≤ |P| ≤ hi is Σ_{lo ≤ j ≤ hi} s^j·C(|S|, j). 

### `GW_congr`

 The weight depends only on the numbers of the layers below R. 

### `GW_mul_sgnP`

 The weight times the sign of P is the product over the layers of ws_i^(members of P in layer i),
or 0 if some layer has too few or too many members. 

### `sum_vset_GW`

 For one assignment: the sum over the sets of violated clauses, with the weight `GW`, is the
product over the layers. 

### `evalV_truncW`

 One evaluation with the weight `GW` is `truncW`, if no upper limit exceeds w. 

### `evalV_truncW_ctx`

 The same with an evaluator that does not mention the list of layers: the number of layers is
read from the context of the network. 
