---
{
  "module": "proof/rates/ExplicitCost/EntryDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/EntryDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/EntryDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One entry of W̃_γ, with K and g as data

Definitions and statements only; nothing is proved here.

**Why.** Lemma 8 (grouping with explicit cost) says that the value of a network is computed «within
(K^g + 𝒯·2^{2gP/K}τ)(g(P+B))^{C₁} operations, by one procedure, the same for all K, g, ζ and all
networks», and Appendix A says: «all costs are
counted again, because poly(·) there hides constants that depend on K and e»; C₁ is an absolute
constant. Its proof: «an entry is a sum of at most 2^{2gP/K} terms, each a product of at most g²
values. Testing a grouping, finding the blocks in an argument Θ … and
the arithmetic for one term … take time polynomial in g(P+B)». For Lemma 1 of the main text the
machine `Printed.tableQ K g` computes an entry; there K and g are parameters of the Lean definition,
so there is one machine, one constant and one certificate for each
K and g (`Printed.StEntryCost`: «The constant depends on K and g only»). Here the same machine reads
K and g from its input, in unary.

**What is here.** `entryData`: built like `Printed.tableQ`, from the same plain functions
(proof/machines/StepMachines/Prog/NetProg.lean, proof/networks/Eight/ViaGrouping/Defs.lean), each
called with the K and g of the input. `EntryCostExplicit`: the cost of an entry with ONE constant
for all K, g
and all networks. `EntryPoly`: ONE certificate of polynomial-time steps. `EntrySameRuns`: for each K
and g the machine runs as `Printed.tableQ K g` does. 

### `DataInput`

 The input: (K, g) in unary, and the input of Definition 2(iii) (P, B and the numbers P_a,
c_{a,b}, in unary). 

### `askedData`

 Definition 2(iii) read by the machine: the numbers are read off the input, and each of the four
procedures is one query. As `Printed.asked`, with K and g beside the input. 

### `kOf`

 The K of the input. 

### `gOf`

 The g of the input. 

### `wData`

 [z_a ∈ S_a]·W_a(z_a). 

### `psiData`

 [z_a ∈ S_a][z_b ∈ S_b]·Ψ_{a,b}(z_a, z_b). 

### `fData`

 [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}). 

### `termData`

 The factor number i = a·g + b of a term of W̃_γ(Θ), as `Printed.termQ`. 

### `entryData`

 **One entry W̃_γ(Θ)**, K and g read from the input: 0 unless all appended bits are 0; else the
sum, over all strings of Σ_{a ∈ G_γ} P_a bits, of the product of the g² factors. 

### `dataInput`

 The input for K, g and the network N with the parameters P, B. 

### `EntryCostExplicit`

 **The cost of an entry, with one constant.** There is ONE number c₁ such that for all 1 ≤ K ≤ g,
every network N on [g] with parameters P, B, every price τ ≥ 1 of a query of Definition 2(iii),
every grouping number x < K^g with at most 2g/K nodes in every
group and Y_{γ,γ'} ≤ L ≤ 2gP: the machine `entryData`, asked for the entry (γ, Θ) of the tables W̃
of the (K, L)-clique of the groups, returns it within 2^{P·⌊2g/K⌋}·τ·(g(P+B))^{c₁} operations, on
states of size at most (g(P+B))^{c₁}; and the entry is below 2^{B'} in absolute value, B' = ⌈2gP/K⌉ +
g²B («As shown there, |W̃_γ| < 2^{B'}»). The proof of Lemma 8 has L ≤ gP + 1;
L ≤ 2gP is weaker (P ≥ 1) and is what `Printed.StEntryCost` asks. 

### `EntryPoly`

 **One certificate**: the machine has polynomial-time steps. (The plain functions inside are
polynomial-time jointly in K and g: proof/rates/PaddedDescent/F/CertNet.lean.) 

### `EntrySameRuns`

 For each K and g the machine runs as `Printed.tableQ K g` does: the same result, own steps and
queries. A state holds the input in up to four places (the two loops, the test before a factor, the
pending query), so the states are larger by at most four copies of K and g in unary. 
