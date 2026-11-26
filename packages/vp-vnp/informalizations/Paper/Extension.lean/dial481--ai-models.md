---
{
  "module": "Paper/Extension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Extension.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Extension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Tensors, prices and duality": extension

The subsection "Extension": Proposition prop:extend, with the steps of its proof.


### `extendProduct`

 The product on the right in Proposition prop:extend: "Call the product on the right f(t)". 

### `prop_extend_product`

 Proof of Proposition prop:extend: "Call the product on the right f(t); it is multiplicative and monotone." Also f ≥ 0 and
f(1) = 1. 

### `prop_extend_cover`

 Proof of Proposition prop:extend: "Suppose that ιA = ∑ s_j, each s_j a restriction of b_j. As ιA has trivial index sets
outside ι(I), so has every s_j; so s_j = ιa_j with ∑ a_j = A. Push-forwards preserve restrictions, so a_j = π_l s_j is a
restriction of π_l b_j for every l." 

### `prop_extend_lower`

 Proof of Proposition prop:extend: "So φ(A) ≤ ∑ φ(a_j) ≤ ∑ f(b_j)", for every cover (b_j) of ιA. 

### `prop_extend_upper`

 Proof of Proposition prop:extend: "f(ιA) = φ(A), as π_l ι = id." 

### `prop_extend_gauge`

 Proof of Proposition prop:extend: there is "a gauge with p ≤ f and p(ιA) = φ(A) for all A". In the proof it is the printed
one: "Let p(t) be the infimum of ∑ f(b_j) over the covers (b_j) of t. … With A = 1 this shows p(1) = 1". 

### `prop_extend_localize`

 Proof of Proposition prop:extend: "let c = φ(C) and q(t) = inf p(t ιCⁿ)/cⁿ. As p(ιCⁿ) = cⁿ, this is a gauge below p that
keeps (1, ιC, 1/c)." Stated for any gauge p and any tensor f with p(f) > 0 and p(fⁿ) = p(f)ⁿ: some gauge q below p keeps
(1, f, 1/p(f)). It is the one of prop_gauge_localize, for the classes of tensors. 

### `prop_extend`

 **Paper: Proposition prop:extend.** "Let ι : I → I′ and π_l : I′ → I, l ≤ L, be maps with π_l ι = id, let θ_l ≥ 0
add up to 1, let φ be a spectral point on I, and let C be a tensor on I. There is a spectral point φ′ on I′ with
φ′(t) ≤ ∏ φ(π_l t)^θ_l for all t, and φ′(ιC) = φ(C)." The maps are indexed by any finite type L. 
