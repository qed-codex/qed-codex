---
{
  "module": "proof/networks/Value/Joint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Joint.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Value/Joint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The joint sum over z and θ

Proof of Lemma 1, paragraph «The algorithm»: the two copies of the string on an edge {γ, γ'} must
agree, and both W̃_γ and W̃_γ' read θ_{a,b} from the same block of this string, so θ_{a,b} =
θ_{b,a}; the appended bits must be 0. Together with the sums inside the tables, this is a sum over
all z ∈ ∏_{a ∈ [g]} S_a and over one string
θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups.
`stJointSumOf` proves the last sentence from the ones before it, which are its hypotheses, in these
steps:
1. the choices Λ of one string per edge with a nonzero appended bit are dropped (`StAppendedZero`);
2. in the others the factor [all appended bits are 0] is 1, and each table reads the strings θ =
   `readBlocks` Λ, the same from both sides (`StSameBlock`; `display_eq`);
3. the variable Λ is changed for θ (`StBlocks`);
4. the product over the groups of the sums inside the tables is one sum over z (`StSumsInside`);
5. the products are regrouped: nodes by groups, pairs inside groups, and ordered pairs across groups
   into unordered pairs (`prod_groupTerm`). 

### `groupTerm`

 The term of (z_a), a ∈ G_γ, in the display of W̃_γ, with the strings θ_{a,b} taken from a choice
θ of one string per pair {a, b} of nodes in different groups: ∏_{a ∈ G_γ} W_a(z_a) ∏_{{a,b} ⊆ G_γ}
Ψ_{a,b}(z_a, z_b) ∏_{a ∈ G_γ, b ∉ G_γ} f_{a,b}(z_a, θ_{a,b}). 

### `display_eq`

 If all appended bits of Λ are 0, the table of the group γ at the strings of Λ on the edges at γ
is the sum inside the table, with the strings θ_{a,b} that are read from Λ. 

### `prod_groupTerm`

 The product over the groups of the terms of the tables is the term of (z, θ) in the joint sum:
every node lies in one group; a pair of nodes in the same group lies inside one group; a pair {a, b}
of nodes in different groups occurs twice, as (a, b) in the table of a's group and as (b, a) in the
table of b's group, with the same string θ_{a,b}. 

### `stJointSumOf`

 «Together with the sums inside the tables, this is a sum over all z ∈ ∏_{a ∈ [g]} S_a and over
one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups», from the
sentences before it. 

### `stJointSum`

 «Together with the sums inside the tables, this is a sum over all z ∈ ∏_{a ∈ [g]} S_a and over
one string θ_{a,b} ∈ {0,1}^{c_{a,b}} per pair {a,b} of nodes in different groups.» 
