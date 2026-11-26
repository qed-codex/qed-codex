---
{
  "module": "proof/threesat/Exits/Grouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Grouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Exits/Grouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 for the algorithm of its proof, with the search that halts at the first good grouping

Proof of Lemma 1, «The algorithm»: «Go through all K^g groupings (a constant) and fix the first good
one.» Line 10 of Algorithm 1: «try all groupings into K_ℓ groups until one is good».
This file proves three implications of proof/threesat/Exits/AlgDefs.lean, each from its hypotheses.
* `stSearchStopsOf`: from «try all … until one is good» for any loop (`StFirstUntil`), the search
  halts at the first good grouping number x, within 2·(x + 1) steps: one step for a test and one to
  go on.
* `stGroupingLemmaOf`: Lemma 1 for `Exits.netAlg`, from the run of the search and the three steps of
  the proof: a good grouping exists and the first good one is fixed (`ViaGrouping.StSearch`), the
  cost of one entry (`ViaGrouping.StTable`), the value equals Z (`ViaGrouping.StValue`). The proof
  is that of `Eight.ViaGrouping.netAlg_correct` (proof/networks/Eight/ViaGrouping/Main.lean) with
  this search in the place of the one used there; the steps of «Cost» are called as they stand there
  (`Cost.run_clique`, `Cost.bound_follows`, `Groundwork.RebalanceArith.size_le`), since they do not
  speak of the search. The search takes 2·(x + 1) ≤ 2·K^g steps: «(a constant)».
* `stKeepsOf`: the algorithm has polynomial-time steps if the loop `foldUntil` has
  (`StFoldUntilPoly`); the certificates of L, of the test of a grouping and of the tables are those
  of proof/networks/Eight/ViaGrouping/Keeps.lean.
`correct_of_searchStops` and `search_isPolyT` are steps inside the proofs of the last two, not
statements of AlgDefs.lean. 

### `stSearchStopsOf`

 **Line 10 of Algorithm 1**: «try all groupings into K_ℓ groups until one is good». If x is the
first number below K^g to which the test says yes, the search halts within 2·(x + 1) steps and
returns x. From the same sentence for any loop. 

### `correct_of_searchStops`

 The bound of Lemma 1 for the algorithm of its proof with the search of line 10, on networks on
[g], for every g ≥ K for which a good grouping is found (hypothesis `hS`). The proof runs through
the paragraphs «The algorithm» and «Cost»: «Go through all K^g groupings (a constant) and fix the
first good one» (`hR`: the search halts there), «Run the algorithm for (K, e) with L, B' in the
roles of λ, B» (`Cost.run_clique`), «the bound follows» (`Cost.bound_follows`), and the same for the
sizes of the states. 

### `stGroupingLemmaOf`

 **Lemma 1 for the algorithm of its proof**, with the search of line 10. «Let (K, e) be
achievable and g = 3K⁸. There is a constant C₁ = C₁(K, e) such that the value of every network on
[g] with parameters P, B, τ and total U is computed within C₁·2^{e(U + gP/K) + 2gP/K}·(P + B)^{C₁}·τ
operations.» From the run of the search and the three steps «a good grouping exists … fix the first
good one», «one entry costs …» and «so the value equals Z». 

### `search_isPolyT`

 The search of line 10, «try all groupings into K_ℓ groups until one is good», has
polynomial-time steps, if the loop that can be left early has. 

### `stKeepsOf`

 **The algorithm of the proof of Lemma 1, with the search of line 10, has polynomial-time steps**
if the algorithm E for cliques has. A bound on the number of steps («… is computed within C₁·2^{e(U +
gP/K) + 2gP/K}·(P + B)^{C₁}·τ operations») bounds the time only if each step takes polynomial time;
this is that half. From the polynomial-time steps of the loop. 
