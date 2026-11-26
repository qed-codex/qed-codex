---
{
  "module": "proof/networks/Eight/SecNetworks_Tables.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Tables.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Tables.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 1, «The algorithm»: the display of W̃_γ

«Put W̃_γ(Θ) = [all appended bits are 0] Σ_{(z_a), a ∈ G_γ} ∏_{a ∈ G_γ} W_a(z_a) ∏_{{a,b} ⊆ G_γ}
Ψ_{a,b}(z_a, z_b) ∏_{a ∈ G_γ, b ∉ G_γ} f_{a,b}(z_a, θ_{a,b}). Here each z_a ranges over S_a.»
The tables on which the algorithm of Lemma 1 runs are `Paper.groupedTables`, defined in two steps
(`Network.merge`, then `Network.toInst`). This file unfolds the two steps and states the result as
the one formula of the paper
(`groupedTables_eq`; for a network as Definition 2 prints it: `tables_eq`), with names for the
appended bits (`appendedBits`) and for θ_{a,b} (`thetaAt`, of c_{a,b} bits by `length_thetaAt`), and
proves the sentence «both W̃_γ and W̃_γ' read θ_{a,b} from the same block of this string, so θ_{a,b} =
θ_{b,a}» (`thetaAt_comm`).
Nothing here depends on Lemma 2 or on its pieces. 

### `appendedBits`

 «the L − Y_{γ,γ'} positions after the last block hold the appended bits»: the bits of the string
θ on the edge {γ, γ'} after the first Y_{γ,γ'} positions. Here Y_{γ,γ'} is `lbLen`, the sum of the
numbers c_{a,b} that the procedures give,
over a in the group with the smaller number and b in the other. 

### `thetaAt`

 «For a ∈ G_γ and b ∉ G_γ let θ_{a,b} ∈ {0,1}^{c_{a,b}} consist of the bits of Θ(χ(b)) in the
block of {a, b}.» The order of the pairs between two groups is that of the list `prs`: (a', b') with
a' in the group with the smaller
number, in increasing order of a', then of b'; the paper allows any order. 

### `groupedTables_eq`

 **Proof of Lemma 1, «The algorithm»: the display of W̃_γ.** For Θ : [K] ∖ {γ} → {0,1}^L,
W̃_γ(Θ) = [all appended bits are 0] Σ_{(z_a), a ∈ G_γ} ∏_{a ∈ G_γ} W_a(z_a) ∏_{{a,b} ⊆ G_γ}
Ψ_{a,b}(z_a, z_b) ∏_{a ∈ G_γ, b ∉ G_γ} f_{a,b}(z_a, θ_{a,b}), each z_a ranging over S_a. Same as in
the paper. In Lean's terms: Θ is a function on all
of [K], whose value at γ is not read; (z_a) is a function on all nodes, with the empty string
outside G_γ; the pairs {a, b} ⊆ G_γ are the pairs a < b. 

### `thetaAt_comm`

 «The two copies of the string on an edge {γ, γ'} must agree, and both W̃_γ and W̃_γ' read
θ_{a,b} from the same block of this string, so θ_{a,b} = θ_{b,a}»: if a and b lie in different
groups and the argument Θ of the table of a's group
and the argument Θ' of the table of b's group have the same string on the edge between the two
groups, then θ_{a,b}, read from Θ, is θ_{b,a}, read from Θ'. 

### `length_thetaAt`

 «θ_{a,b} ∈ {0,1}^{c_{a,b}}»: if a and b lie in different groups, the string Θ(χ(b)) has L bits
and Y_{γ,γ'} ≤ L for all pairs of groups, then θ_{a,b} has c_{a,b} bits. 

### `tables_eq`

 **The display of W̃_γ for a network as Definition 2 prints it** (with sets S_a of settings and
functions Ψ_{a,b} of its own): the tables on which the algorithm of Lemma 1 runs are given by the
formula of the paper in terms of
W_a, Ψ_{a,b}, f_{a,b} and S_a of N, for Θ : [K] ∖ {γ} → {0,1}^L and Y_{γ,γ'} ≤ L. Same as in the
paper; the remarks at `groupedTables_eq` apply. 
