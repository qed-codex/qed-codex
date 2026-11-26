---
{
  "module": "Paper/Lengths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Lengths.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Lengths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, subsection "Lengths": the remark on maps into price spaces, polynomial growth and rank one

The third lemma of the subsection (lem:first) is in Paper/Groups.lean.


### `rankMean`

 The mean of f² over the matrices of rank r. 

### `contracts_iff`

 A length contracts: "for every homomorphism τ from the additive group Mat_μ(F₂) into the group, the mean of |τW|²
over rank μ is at most s² times that over rank 1". It is the project's Contr. 

### `contracts_smul`

 A multiple of a contracting length contracts. 

### `lengths_of_maps`

 The remark after the definition of contracting lengths: "If a map f sends a finite group into a price space, then
|g| = (E_a|f(a)f(ga)|²)^(1/2) contracts: pull the price back along W ↦ f(τ(W)a) and average over a." 

### `lem_growth_digit`

 The proof of Lemma lem:growth: "Compose τ with Z ↦ α(Z ⊗ 1_i)α′ … and average: D(μi) ≤ sD(i) if μi ≤ k." 

### `lem_growth_minkowski`

 The proof of Lemma lem:growth: "By Minkowski's inequality D(i+i′) ≤ D(i) + D(i′)." 

### `lem_growth`

 **Paper: Lemma lem:growth.** "Let 1 ≤ r ≤ k, let τ be a homomorphism from Mat_{k×k}(F₂) into a group with a
contracting length, and let D(r) be the quadratic mean of |τW| over rank r. Then D(r) ≤ μ(j+1)s^j D(1), where
j = ⌊log_μ r⌋." (r = 0 is allowed too.) 

### `lem_words`

 **Paper: Lemma lem:words.** "For 1 ≤ k < n and nonzero ξ, ω the element of U_n with upper right block ξωᵀ and unit
diagonal blocks has, in every length on U_n, length at most 18 ∑_j |x_j|." 
