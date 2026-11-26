---
{
  "module": "proof/networks/Eight/ViaGrouping/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 along the printed proof: «Cost», and the lemma for the algorithm of its proof

The file puts the steps of the proof of Lemma 1 together for the algorithm `netAlg K g E` of
proof/networks/Eight/ViaGrouping/Defs.lean. It takes three steps as hypotheses: the search finds a
good grouping (`StSearch`), the procedure `tableM` answers the queries to the tables W̃
(`StTable`), and the clique of the groups has the value of the network (`StValue`). It proves the
other sentences of the paragraph «Cost», one lemma or a few for each (namespace
`Eight.ViaGrouping.Cost`); «each a product of at most g² values» and «one entry costs
2^{2gP/K}·poly(P + B)·τ operations» are part of `StTable`, and the count of the search («Go through
all K^g groupings (a constant)», 2·K^g steps) is `searchP_runs` of
proof/networks/Eight/ViaGrouping/Search.lean.
* «The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K} terms»: `terms_le`;
* «So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B»: `Bp`, `le_Bp`, `serves_Bp`;
* «Run the algorithm for (K, e) with L, B' in the roles of λ, B; this is legitimate because
  Definition 4 covers all integer tables. Answer each of its at most C·2^{eK²L}(B' + L)^C queries by
  computing the entry»: `run_clique`;
* «Since K²L ≤ K² + U + gP/K and L ≤ 2gP, the bound follows»: `K2L_le_real`, `exponent_le`,
  `base_le`, `bound_follows`.
Then `netAlg_correct` (any g ≥ K for which the search succeeds; K need not divide 2g) and
`stLemGrouping_of` (g = 3K⁸).

Different from the paper: steps of step machines are counted, and the sizes of their states are
bounded too (`Groundwork.RebalanceArith.size_le`); a group has at most ⌊2g/K⌋ nodes, so the sum has
at most 2^{P·⌊2g/K⌋} terms; «at most 2^{B'}» stands for «below 2^{B'}», as in the
form of Definition 4 that this development uses; there a query costs t steps and the bound carries
the factor t, which is how «answer each query by computing the entry» is counted. 

 ## The sentences of «Cost» that are arithmetic 

### `floor_le`

 P·⌊2g/K⌋ ≤ 2gP/K. 

### `terms_le`

 «The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K} terms»: the number 2^{P·⌊2g/K⌋}
of strings that `tableM` runs through is at most 2^{2gP/K}. K need not divide 2g. 

### `Bp`

 «B' = ⌈2gP/K⌉ + g²B». 

### `le_Bp`

 The exponent P·⌊2g/K⌋ + g²B that the count of the terms and of the g² values in a term gives is
at most B'. 

### `Bp_le`

 B' ≤ (2g + g²)(P + B): B' is polynomial in P + B. 

### `K2L_le_real`

 «K²L ≤ K² + U + gP/K», for L = max{1, ⌊(U + gP/K)/K²⌋}. 

### `exponent_le`

 The exponents: e·K²L + 2gP/K ≤ e·K² + (e·U + (e + 2)·gP/K), from «K²L ≤ K² + U + gP/K». The term
e·K² is a constant. 

### `base_le`

 B' + L ≤ (4g + g²)(P + B), from «L ≤ 2gP»: the factor (B' + L)^C is polynomial in P + B. 

### `bound_follows`

 «Since K²L ≤ K² + U + gP/K and L ≤ 2gP, the bound follows.» T_E is the number of steps of the
algorithm for cliques, at most A·2^{eK²L}·(B' + L)^A times the cost c₁·2^{P·⌊2g/K⌋}·τ of an entry; s
is the constant number of steps of the search and of the passage
from the search to the call. Then the total T ≤ s + T_E is at most A'·2^{eU + (e+2)gP/K}·(P +
B)^{A'}·τ, and A' depends only on K, g, e, A, c₁, s. 

 ## The sentences of «Cost» that speak of the model 

### `serves_Bp`

 «So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B»: query access with the bound 2^{P·⌊2g/K⌋ + g²B} on
the entries is query access with the bound 2^{B'}. Different from the paper: «at most» for «below». 

### `run_clique`

 «Run the algorithm for (K, e) with L, B' in the roles of λ, B; this is legitimate because
Definition 4 covers all integer tables. Answer each of its at most C·2^{eK²L}(B' + L)^C queries by
computing the entry.» For a good grouping number x, the algorithm E for
cliques, run with L and with `tableM` as the procedure that answers its queries, returns the value
of the network within A·2^{eK²L}·(B' + L)^A·t' steps, where t' = c₁·2^{P·⌊2g/K⌋}·τ is the cost of
one entry. A is the constant of E (the paper's C), c₁ that of `StTable`.
In the form of Definition 4 that this development uses, a query costs t' steps and the bound carries
the factor t'. 

 ## Lemma 1 

### `netAlg_correct`

 The bound of Lemma 1 for the algorithm of its proof, on networks on [g], for every g ≥ K for
which the search finds a good grouping (hypothesis `hS`; for g = 3K⁸ this is `StSearch`). K need not
divide 2g. The proof runs through the paragraphs «The algorithm» and «Cost»:
the search (`searchP_runs`), the call of the algorithm for cliques (`Cost.run_clique`), «the bound
follows» (`Cost.bound_follows`), and the same for the sizes of the states
(`Groundwork.RebalanceArith.size_le`). 

### `stLemGrouping_of`

 **Lemma 1 for the algorithm of its proof** (`StLemGrouping`), from the three steps «a good
grouping exists … fix the first good one», «one entry costs …» and «so the value equals Z». 

### `exponent_eq`

 The exponent of `Correct` with ε = e and b = e + 2 is the exponent of Lemma 1: e·U + (e + 2)·gP/K =
e(U + gP/K) + 2gP/K. 
