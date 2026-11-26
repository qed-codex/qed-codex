---
{
  "module": "Zeta23/MV/Spacing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Spacing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/MV/Spacing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# MV step 0 — spacing lemmas for admissible weights

For an injective `freq : ι → ℝ` on a finite index type with ADMISSIBLE weights `δ`
(`0 < δ r` and `δ r ≤ |freq r − freq s|` for all `s ≠ r` — the shape of Zeta23.MVHilbert),
the open intervals `I_t = (freq t − δ t/2, freq t + δ t/2)` are pairwise disjoint, giving
by comparison with `∫ |u − freq s|^{−σ} du`:

* `spacing_sq`   (σ = 2):  Σ_{t≠s} δ t/(freq s − freq t)²  ≤  9/δ s
* `spacing_four` (σ = 4):  Σ_{t≠s} δ t/(freq s − freq t)⁴  ≤  27/(δ s)³
* `two_point`:  Σ_{k≠ℓ,m} δ k/((freq k − freq ℓ)²(freq k − freq m)²)
                  ≤ 36(δ ℓ + δ m)/(δ ℓ · δ m · (freq ℓ − freq m)²)

These replace [Preissmann 1984, Lemmes 1 & 6] (cited without proof in arXiv:2203.14950)
with elementary arguments at worse constants — sufficient for the ∃C form.


### `Adm`

 Admissibility of weights (matches Zeta23.MVHilbert's hypotheses). 

### `itv`

 The interval `I_t`. 

### `centers_far`

 Centers are far apart: `(δ t + δ t')/2 ≤ |freq t − freq t'|` for `t ≠ t'`. 

### `itv_disjoint`

 The intervals are pairwise disjoint. 

### `abs_le_of_mem_itv`

 For `u ∈ I_t`, `t ≠ s`: `|freq s − u| ≤ (3/2)|freq s − freq t|` and `δ s/2 ≤ |u − freq s|`. 

### `integral_inv_sq_Icc`

 Closed-form tail integrals: `∫_{Icc a b} (u−c)⁻² du = (a−c)⁻¹ − (b−c)⁻¹` for `c ∉ [a,b]`. 

### `integral_inv_four_Icc`

 `∫_{Icc a b} (u−c)⁻⁴ du = ((a−c)⁻³ − (b−c)⁻³)/3` for `c ∉ [a,b]`. 

### `abs_bounds_closed`

 Closed-interval version of the membership bounds (for use on closures `J t`). 

### `window`

 The two-sided tail window around `freq s`, radius `R`. 

### `spacing_sq`

 **Spacing lemma, σ = 2**: `Σ_{t≠s} δ t/(freq s − freq t)² ≤ 9/δ s`. 

### `spacing_four`

 **Spacing lemma, σ = 4**: `Σ_{t≠s} δ t/(freq s − freq t)⁴ ≤ 27/(δ s)³`. 

### `two_point`

 **Two-point lemma** (replaces Preissmann Lemme 6 at constant 36). 
