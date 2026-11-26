---
{
  "module": "proof/networks/Eight/ViaGrouping/Display.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Display.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Display.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Lemma 1, «The algorithm»: the tables that the algorithm computes are the display of W̃_γ

«Put W̃_γ(Θ) = [all appended bits are 0] Σ_{(z_a), a ∈ G_γ} ∏_{a ∈ G_γ} W_a(z_a) ∏_{{a,b} ⊆ G_γ}
Ψ_{a,b}(z_a, z_b) ∏_{a ∈ G_γ, b ∉ G_γ} f_{a,b}(z_a, θ_{a,b}). Here each z_a ranges over S_a.»
The statements `StTable` and `StValue` speak of the tables
`Paper.groupedTables Np.toPaperNetwork c N.toPaperNetwork`, which are defined in two steps.
`SecNetworks.tables_eq` (proof/networks/Eight/SecNetworks_Tables.lean) shows that they are given by
the formula of the paper. Here that formula gets a name
(`display`), and the statement `StTable` is said again with it:
* `groupedTables_eq_display`: the tables are the display, at every Θ : [K] ∖ {γ} → {0,1}^L;
* `tableM_display`: the procedure `tableM` of the algorithm returns the display, within the steps
  and sizes of `StTable`, and the display obeys the bound on the entries. 

### `display`

 **The display of W̃_γ(Θ)** of the proof of Lemma 1, for the grouping number x of a network N
(Definition 2). (z_a) is a function on all nodes, with the empty string outside G_γ; each z_a ranges
over S_a;
the pairs {a, b} ⊆ G_γ are the pairs a < b. The appended bits (`SecNetworks.appendedBits`) and
θ_{a,b} (`SecNetworks.thetaAt`) are cut out of Θ at the positions that the numbers c_{a,b} given by
the procedures fix. 

### `groupedTables_eq_display`

 The tables of `StTable` and `StValue` are the display, for Θ : [K] ∖ {γ} → {0,1}^L and Y_{γ,γ'}
≤ L. This is `SecNetworks.tables_eq`, for procedures that need not give B. 

### `tableM_display`

 **The procedure `tableM` computes the display.** For a grouping with (G1) and Y_{γ,γ'} ≤ L ≤
2gP, and every query (γ, Θ) with L bits for every other group and the empty string at γ: `tableM`
returns the display of W̃_γ(Θ) within c₁·2^{P·⌊2g/K⌋}·τ steps, on states of size at most
S + c₁·(size c + P + B)^{c₁}, and the display is at most 2^{P·⌊2g/K⌋ + g²B} in absolute value. The
constant depends on K and g only. 
