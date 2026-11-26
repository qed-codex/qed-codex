---
{
  "module": "proof/networks/Value/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # «… so the value equals Z», along the sentences of the paper (definitions and statements only)

Proof of Lemma 1, after the display of W̃_γ: the value of this clique is a sum over the settings of
its nodes γ; the two copies of the string on an edge {γ, γ'} must agree, and both W̃_γ and W̃_γ'
read θ_{a,b} from the same block of this string,
so θ_{a,b} = θ_{b,a}; the appended bits must be 0. Together with the sums inside the tables, this is
a sum over all z ∈ ∏_{a ∈ [g]} S_a and over one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of
nodes in different groups. Each θ_{a,b} occurs only in f_{a,b} and f_{b,a}, and
Σ_{θ_{a,b}∈{0,1}^{c_{a,b}}} f_{a,b}(z_a, θ_{a,b}) f_{b,a}(z_b, θ_{a,b}) = Ψ_{a,b}(z_a, z_b), so the
value equals Z.
And after Definition 3: only the terms in which the two copies on every edge agree contribute, and
the value is the sum, over all choices of one string in {0,1}^λ per edge, of ∏_{w∈[K]} W_w evaluated
at the strings on the edges at w.

`Eight.ViaGrouping.stValue` (proof/networks/Eight/ViaGrouping/Table.lean) proves «the value equals
Z» by another route: each group is merged into one node (`Groundwork.Network.value_merge`), and the
merged network is compared with its tables (`Groundwork.Prog.NetE.ZW_merged`,
`Groundwork.Network.ZW_toInst`, `Paper.grouped_value`);
Here each sentence of the paper is a statement, and the end statements are proved from these and
from nothing else of that route. Most implications below are between closed propositions, so their
types do not force the route; no proof of this folder uses the theorems just named.
The objects are those of this development: the clique as a network (`Eight.SecNetworks.clique`), the
display of W̃_γ (`Eight.ViaGrouping.display`), the appended bits and θ_{a,b}
(`Eight.SecNetworks.appendedBits`, `thetaAt`), the grouping number x (`Paper.grouping`).
This file has no proofs. 

 ## The clique: two copies on every edge, and one string per edge (Definition 3 and the sentences after it) 

 Tables whose argument gives, for every other node w', the string on the edge {w, w'}
(`Paper.Tables`) are read as the tables of Definition 3, whose argument is the setting z_w (one
string of (K − 1)λ bits, the concatenation of the K − 1 copies z_w(w')), by
`Eight.SecNetworks.tablesOn` (proof/networks/Eight/SecNetworks_Clique.lean). Every table on settings
is of this form. 

### `edgeStrings`

 The choices of one string of λ bits per edge {w, w'}, w < w'. (A function on all pairs; the
empty string off the edges.) 

### `CopiesAgree`

 In the choice z = (z_w) of one setting per node, the two copies of the string on every edge
agree. 

### `cliqueTerm`

 The term of the choice z = (z_w) in the value of the (K, λ)-clique: ∏_w W_w(z_w) ∏_{{w,w'}}
[z_w(w') = z_{w'}(w)]. 

### `StSumOverSettings`

 «The value of this clique is by definition a sum over the settings of its nodes». 

### `StCopiesMustAgree`

 «The two copies of the string on an edge must agree» / «only the terms in which the two copies
on every edge agree contribute»: every other term is 0, and in such a term the factors of the edges
are 1. 

### `StOneStringPerEdge`

 The choices of settings in which all copies agree are the choices of one string per edge: each Λ
belongs to exactly one choice z of settings, the one with z_w(w') = Λ{w, w'} for all w ≠ w'; and
every z in which all copies agree belongs to some Λ. 

### `StCliqueValue`

 «and the value is the sum, over all choices of one string in {0,1}^λ per edge, of ∏_{w∈[K]} W_w
evaluated at the strings on the edges at w» (after Definition 3). The right-hand side is
`Paper.cliqueValue lam W` written out. It holds for all K and λ (Definition 3 has K ≥ 2, λ ≥ 1). 

### `StCliqueValueOf`

 The sentence after Definition 3, with what it rests on in its hypotheses. 

 ## The clique of the groups 

### `groupClique`

 «We define a (K, L)-clique whose nodes are the groups. By Definition 3 only its tables W̃_γ need
to be defined»: the network of Definition 3 with the display of W̃_γ as tables, for the grouping
number x. 

### `Across`

 The pairs {a, b}, a < b, of nodes in different groups. 

### `blockStrings`

 The choices of «one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different
groups». (A function on all pairs; the empty string elsewhere.) 

### `readBlocks`

 What the tables read from a choice Λ of one string per edge of the clique of the groups: for
each pair {a, b}, a < b, of nodes in different groups, the string θ_{a,b} that the table of a's
group cuts out of the string on the edge between the two groups. (The empty string at all other
pairs.) 

### `AppendedZero`

 On every edge of the clique of the groups all appended bits of the string are 0. 

### `jointTerm`

 The term of (z, θ) in the joint sum: ∏_a W_a(z_a), times Ψ_{a,b}(z_a, z_b) for the pairs inside
a group, times f_{a,b}(z_a, θ_{a,b})·f_{b,a}(z_b, θ_{a,b}) for the pairs of nodes in different
groups. 

### `StLayout`

 «For each pair of groups {γ, γ'} choose an order of the pairs {a, b} … In this order, the pair
{a, b} is assigned a block of c_{a,b} consecutive positions of {1, …, L}; the L − Y_{γ,γ'} positions
after the last block hold the appended bits»: the layout that `thetaAt` and `appendedBits` use. The
order is that of the list
`NetE.prs`: the pairs (a', b') with a' in the group with the smaller number, in increasing order of
a', then of b' (the paper: any order will do). The block of the pair number i begins after the
blocks of the pairs before it. The numbers c are those that the procedures give (`cap`). 

### `StSameBlock`

 «both W̃_γ and W̃_γ' read θ_{a,b} from the same block of this string, so θ_{a,b} = θ_{b,a}». (In
Lean the two copies on an edge have been made one string before, by `StCliqueValue`; the paper says
both in one sentence.) For one string per edge of the clique of the groups, and a, b in different
groups, θ_{a,b} as the table of a's group reads it is θ_{b,a} as the table of b's group reads it. 

### `StAppendedZero`

 «the appended bits must be 0»: if on some edge an appended bit of the string is 1, the product
of the tables is 0. 

### `StBlocks`

 The choices of one string of L bits per edge {γ, γ'} with all appended bits 0 are the choices of
one block of c_{a,b} bits per pair {a, b} of nodes in different groups: what the tables read from
such a Λ is a choice of blocks, and every choice θ of blocks is read from exactly one such Λ. 

### `StSumsInside`

 «Together with the sums inside the tables»: a product over the groups of sums over the settings
of the nodes of the group is one sum over the settings of all nodes, because every node lies in
exactly one group. For an arbitrary grouping χ, arbitrary sets S_a and arbitrary functions F_γ. 

### `StJointSum`

 «Together with the sums inside the tables, this is a sum over all z ∈ ∏_{a ∈ [g]} S_a and over
one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups.» 

### `StSumOut`

 «Each θ_{a,b} occurs only in f_{a,b} and f_{b,a}, and Σ_{θ_{a,b}∈{0,1}^{c_{a,b}}} f_{a,b}(z_a,
θ_{a,b}) f_{b,a}(z_b, θ_{a,b}) = Ψ_{a,b}(z_a, z_b)»: for every grouping χ and every z ∈ ∏ S_a, the
sum of the joint terms over θ is the term of z in the value Z of the network. 

### `StValueEqualsZ`

 **«… so the value equals Z»**, for the clique of the groups as the network of Definition 3 (two
copies of the string on every edge): its value is the value of the network N. 

### `StJointSumOf`

 The joint sum, with what it rests on in its hypotheses. 

### `StValueEqualsZOf`

 «so the value equals Z», with the sentences before it in its hypotheses. 

### `StValueOf`

 The form in which the proof of Lemma 1 in proof/networks/Eight/ViaGrouping takes the step
(`Eight.ViaGrouping.StValue`: the value of the clique written with one string per edge, the tables
as `Paper.groupedTables`), from «so the value equals Z» for the clique as a network: back by the
sentence after Definition 3 (`StCliqueValue`), and by
`Eight.ViaGrouping.groupedTables_eq_display`, which says that the tables are given by the display of
W̃_γ (a fact on how the tables are defined, not on the value). So the proof of Lemma 1 runs through
the clique with two copies on every edge. 
