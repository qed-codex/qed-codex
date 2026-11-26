---
{
  "module": "proof/networks/Eight/ViaGrouping/SatPsiDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/SatPsiDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/SatPsiDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6, «Clusters, occurrences, equality tests»: the network of Φ as Definition 2 prints a network (definitions only)

The network of Φ in this development (`Paper.networkOf g Φ`, for clauses of at most k literals
`Groundwork.Prog.Count.wordNet g k Φ`) comes with procedures for W_a and f_{a,b} only
(`Groundwork.Prog.satP g k`). Definition 2(iii) also asks for the number P and
for a procedure that computes Ψ_{a,b}. This file adds them, in the words of the paper:
«Choose an order of these tests, and let z_a|_b ∈ {0,1}^{c_{a,b}} list the bits of z_a at their
occurrences in cluster a; likewise z_b|_a. Put Ψ_{a,b}(z_a, z_b) = [z_a|_b = z_b|_a]» (`restr`,
`satPsi`); «with P = 6m̄» (`satPf`).
The tests between two clusters, in their order, are the list `Groundwork.Prog.Count.links`.
Different from the paper, as in `Groundwork.Prog.Count.wordNet`: a setting has one bit for each
PLACE of a literal (k places per clause, so k·m̄ bits per cluster), not one for each
occurrence; the bit at a place without a literal must be 0. This file has no proofs. 

### `restr`

 z_a|_b: the bits of the setting z of cluster a at its occurrences in the tests between the
clusters a and b, in the order of these tests. A test is a pair (place in the earlier cluster, place
in the later cluster). 

### `satPsi`

 Ψ_{a,b}(z, z') = [z|_b = z'|_a], for the query q = ((a, b), (z, z')): 1 if every test between
the clusters a and b holds, else 0. 

### `satPsiM`

 The procedure for Ψ: one step, which computes `satPsi`. Its context is Φ itself. 

### `satPf`

 P = 2k·m̄, for k = 3 the paper's P = 6m̄; at least 1, because Definition 2 asks for P ≥ 1 and m̄ =
0 if Φ has no clause. 

### `satProcs`

 What an algorithm is given of the network of a formula with at most k literals per clause
(Definition 2(iii)): P, the lengths, and the four procedures. 

### `satNet`

 The network of Φ on g clusters, for clauses of at most k literals, as the data of Definition 2. 
