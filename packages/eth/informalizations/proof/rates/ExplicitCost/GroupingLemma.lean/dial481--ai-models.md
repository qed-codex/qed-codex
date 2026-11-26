---
{
  "module": "proof/rates/ExplicitCost/GroupingLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingLemma.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on groupings with explicit cost, for the procedure of its proof

«… define the (K, L)-clique with the tables W̃_γ, whose value is that of the network, run the given
algorithm on it, and answer each query by computing the entry.» The procedure is
`groupingData E arg`, for ANY machine E that outputs the value of every (K, L)-clique with |W_w| <
2^{B'} within 𝒯 operations. With X = g(P+B), n = 2^{P⌊2g/K⌋} and t = n·τ·X^{c₁}, the cost of an
entry:

1. E takes 𝒯 operations, a query counted as one; at t + 2 operations for a query it takes at most
   𝒯·(t + 2) (`QueryMachines.StSlowDown`);
2. each query answered by `entryData` within t operations: the same bound, now at τ operations for a
   query of Definition 2(iii) (`QueryMachines.StSubstWithin`): this is the call carried out,
   `answerCall_within`;
3. the procedure up to the call costs C·K^g + tc when the call costs tc; with tc = 𝒯·(t + 2) + 2 and
   the call carried out as in 2, the whole costs C·K^g + 𝒯·(t + 2) + 2
   (`QueryMachines.StSubstWithin` again);
4. arithmetic: `time_le` (natural numbers; the constants go into a power of X ≥ 2), `real_time_le`
   (P·⌊2g/K⌋ ≤ 2gP/K).

With the constant C of the part of the procedure before the call (`groupingWithCall`) and the
constant c₁ of an entry, C₁ = C + c₁ + 12. 

 ## Arithmetic 

### `time_le`

 C·K^g + 𝒯·(t + 2) + 2 ≤ (K^g + 𝒯·n·τ)·X^{C + c₁ + 12} for t = n·τ·X^{c₁}; Kg stands for K^g. 

### `real_time_le`

 From 2^{P⌊2g/K⌋} to the printed 2^{2gP/K}, and from natural to real numbers. 

 ## The tables of the clique of the groups 

### `groupW`

 The tables W̃ of the clique of the groups, as a machine for cliques takes tables: a function of
the number of the node and of the setting. 

### `clique_groupW`

 The clique with these tables is the clique of the groups. 

 ## The call carried out 

### `answerCall_within`

 **«run the given algorithm on it, and answer each query by computing the entry»**: for a
grouping number x with the two properties, the call of x, carried out by E with its queries answered
by `entryData`, returns the value of the clique of the groups within 𝒯·(t + 2) operations, t the
cost of an entry. 

 ## The lemma 

### `groupingExplicitFrom`

 How the bound on the part of the procedure before the call (`groupingWithCall`), the cost of an
entry and the rules of substitution give the lemma. 

### `groupingExplicit`

 **Lemma 8**, for the procedure of its proof. 
