---
{
  "module": "ThreeSumApsp/Sec2/Recursion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Recursion.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec2/Recursion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strings, vertices and the coefficients of the encoding

Section 2.3.1. The recursion `Full` works on arrays indexed by strings of variables. This file has
the counts that the later cost estimates use: `7^L` left strings and `7^L` right strings of length
`L`, `10^k` vertices at depth `k` of the recursion tree, and coefficients `φ_λ(s)` and `ψ_λ(t)` in
`{0, ±1}`. The first three follow from the sizes of the alphabets; the last is a finite check. So is
the sentence that each form has at most three nonzero coefficients (`card_support_phi_le`,
`card_support_psi_le`), which no later proof uses. The example in the caption of Figure 3 is
`figure_3`.


### `card_leftStr`

 Section 2.3.1: an array on the left strings of length `L` "has 7^L entries in total". 

### `card_rightStr`

 Section 2.3.1: an array on the right strings of length `L` has `7^L` entries. 

### `card_vertex`

 Section 2.3.1: "At depth k there are 10^k vertices"; in particular there are `10^L` leaves. 

### `abs_phi_le_one`

 Section 2.3.1: "φ_λ(s) ∈ {0, ±1}". 

### `abs_psi_le_one`

 Section 2.3.1: `ψ_λ(t) ∈ {0, ±1}`. 

### `card_support_phi_le`

 Section 2.3.1: "for each term λ, at most three of the seven values φ_λ(s) are nonzero". 

### `card_support_psi_le`

 Section 2.3.1: "and similarly for the seven values ψ_λ(t)". 

### `sum_leftVar`

 A sum over the seven left variables, split into the `x` and the `p`. 

### `figure_3`

 Figure 3: "For instance, A_{P₃₁} = a_{x₃} - a_{p₁₁} - a_{p₂₁} and
A_{P₀} = -a_{x₁} - a_{x₂} - a_{x₃}."  (Indices are counted from 0 in Lean.) 
