---
{
  "module": "proof/rates/CountedRecursion/CallLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallLemma.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/CallLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 8 at the network of a pattern

The row network and the column network of a pattern are networks on `nParts g g tr` nodes, a number
that equals g but is not g by definition, while the machines write g. Here the statements of Lemma 8
are put into the form «a network on n nodes, n = g», for ζ = 1/b:
* `firstGrouping_cast`: from `GroupingWithCall` and `LabelLengthIsL`: the first grouping that the
  test accepts has at most 2g/K nodes in every group and Y_{γ,γ'} ≤ L, and the number that the
  procedure computes is L;
* `entryCost_cast`: `EntryCostExplicit`;
* `groupClique_value`: `ValueIsKept`, for the procedures `asked`, run with the oracle `netOracle N`
  of the network;
* `netTotal_le`, `Lof_bounds`: U ≤ gP and 1 ≤ L ≤ gP. 

### `firstGrouping_cast`

 **The first grouping that the test accepts**, for ζ = 1/b and a network on n = g nodes in case (i)
or (ii). 

### `entryCost_cast`

 **The cost of an entry, with one constant**, for a network on n = g nodes. 

### `groupClique_value`

 «… the (K, L)-clique with the tables W̃_γ, whose value is that of the network», for the clique
of the groups as the statements of Lemma 8 name it. 

### `netTotal_le`

 U ≤ gP, by (i) of Definition 2. 

### `Lof_bounds`

 1 ≤ L ≤ gP, for ζ = 1/b, K ≥ 2 and U ≤ gP. 
