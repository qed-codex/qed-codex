---
{
  "module": "proof/rates/GeneralPieces/Group/Lemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/Lemma.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Group/Lemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 8 (the grouping lemma with explicit cost): a good grouping, and the program that uses it

The order of the proof of Lemma 8 in Appendix A. First "some grouping has at most 2g/K nodes in
every group and Y ≤ L for all γ ≠ γ'" (`someGrouping`): case (i) is `GeneralPieces.caseI`, the
argument of the proof of Lemma 1, case (ii) is
`GeneralPieces.stCaseII`. Then the algorithm: the program `rebalG` goes through the K^g groupings,
takes the first that passes its test and writes out the tables of the (K, L)-clique.

What differs. The test of the program asks for fewer than 2g/K nodes in every group, where the paper
has "at most"; both proofs of existence give the strict bound (`exists_grouping_lt`).
The bound |W̃_γ| ≤ 2^{B'} with B' = ⌈2gP/K⌉ + g²B is proved as in the paper, "a sum of at most
2^{2gP/K} terms, each a product of at most g² values" (`abs_toInst_merge_le`); values are bounded by
2^B and 2^{B'} with "at most" throughout this development, where the paper has "below". 

 ### Some grouping is good 

### `exists_grouping_lt`

 "Some grouping has at most 2g/K nodes in every group and Y ≤ L for all γ ≠ γ'", in both cases,
with fewer than 2g/K nodes in every group. Here P = 0 is allowed: then no two nodes share a bit. 

 ### The size of an entry 

### `card_values_le`

 "Each a product of at most g² values": the nodes of a group, the pairs of nodes inside it, and
the pairs of one node inside and one outside, are at most g² in all. 

### `abs_toInst_merge_le`

 "The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K} terms, each a product of at most
g² values": if every group has at most m nodes, an entry of a table of the clique is at most
2^{Pm + g²B} in absolute value. 

 ### The algorithm 

### `rebalG_spec'`

 "Find the first such grouping among all K^g, define the (K, L)-clique with the tables W̃_γ,
whose value is that of the network": if some grouping passes the test for the label length β and the
pad
is long enough, `rebalG` returns the clique on K nodes with labels of β bits, written out, with the
value of the network and entries of absolute value at most 2^{P·⌊2g/K⌋ + g²B}. This is
`PaddedDescent.F.RebalF.rebalG_spec` with the paper's bound on the entries. 

### `goodG_of_grouping`

 A grouping χ is the number x < K^g whose digits are its values; if χ has fewer than 2g/K nodes
in every group and Y ≤ β for any two groups, x passes the test of the program. 

### `le_B'of`

 P·⌊2g/K⌋ + g²B ≤ B' = ⌈2gP/K⌉ + g²B. 

### `someGrouping`

 The first step of the proof of Lemma 8: "Some grouping has at most 2g/K nodes in every group and
Y ≤ L for all γ ≠ γ'." 

### `wfe_mono`

 An instance whose entries are at most 2^B in absolute value has entries at most 2^{B'} for every
B' ≥ B. 

### `grouping_general`

 Lemma 8 in the form in which the recursion and the top levels call it: in case (i) or (ii), for
every label length β ≥ L (in the recursion "the number L depends on ι";
the programs use one label length for all ι, an upper bound), `rebalG` returns the (K, β)-clique
with the value of the network. Two bounds hold for its entries: the paper's B' = ⌈2gP/K⌉ + g²B, and
P·G + B·(G + G²)·K with G = ⌊2g/K⌋, which is the smaller one once 4g/K + 2 < g and is the one that
the programs compute with. In place of P ≥ 1 only β ≥ 1 is needed. 
