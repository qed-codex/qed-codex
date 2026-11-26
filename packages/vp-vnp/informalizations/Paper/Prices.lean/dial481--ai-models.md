---
{
  "module": "Paper/Prices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Prices.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Prices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Tensors, prices and duality": prices

The subsection "Prices". The definitions are in Nc/Price/Basic.lean.


### `def_price`

 **Paper: Definition def:price.** "A price on a finite set V is a limit of multiples s·d_φ, s ≥ 0, φ a spectral
point on V. A function on the pairs of an arbitrary set Y is a price if all its pull-backs to finite sets are prices." 

### `def_price_pseudometric`

 "Prices are pseudometrics." By Lemma lem:exponents the d_φ are; the conditions are closed and kept by multiples. 

### `def_price_pullback`

 "Pull-backs … of prices are prices; for g : V → W one uses t ↦ φ(gt)." (The latter is Nc.Price.specCone_comp, which
makes the two parts of Definition def:price consistent.) 

### `def_price_multiple`

 "Nonnegative multiples … of prices are prices". 

### `def_price_closed`

 The set of prices is closed under pointwise convergence. 

### `def_price_limit`

 "Pointwise limits of prices are prices". 

### `def_price_compact`

 "The prices below a given function form a compact set, by Tychonoff's theorem." 

 The same facts in the form in which the development cites them. 

### `prop_random_spectral`

 Proof of Proposition prop:random, the finite case for w = d_φ: "Let C be the product of all wires ⟨2⟩_uv with u, v ∈ Y, and
apply Proposition prop:extend. For every pair e of Y ∪ Q we obtain d_φ′(e) ≤ ∑ θ_l d_φ(π_l e). On Y we have d_φ′ ≤ d_φ with
equality for the sum over all pairs, hence equality for each." 

### `prop_random_compact`

 Proof of Proposition prop:random, the reduction to finite sets: "It is enough to find, for all finite Y₀ ⊆ Y and Q₀ ⊆ Q
such that σ maps Q₀ into Y₀, a price on Y₀ ∪ Q₀ with the two properties: these prices form compact sets, so then there is
one that works for all of them at once." Here Z is Y ∪ Q, the two properties are bounds A ≤ |oo′| ≤ B, and the compact
sets are those of def_price_compact. 

### `prop_random_limit`

 Proof of Proposition prop:random, the finite case: "So let Y and Q be finite, and let σ take the values π_l with
probabilities θ_l. By a limit we may assume w = s·d_φ, and then s = 1 by homogeneity." The prices that
prop_random_spectral gives for approximations s·d_φ of w have a limit, since they lie in a compact set (def_price_compact). 

### `prop_random_values`

 Proof of Proposition prop:random: "let σ take the values π_l with probabilities θ_l". On a finite set T of new points a
random map, each σ(o) having finitely many values, takes finitely many values π_l; with their probabilities θ_l, the
expectation of any function of the map is a finite mean. 

### `prop_random`

 **Paper: Proposition prop:random.** "Let w be a price on Y, let Q be a set disjoint from Y, and let σ be a random
map Y ∪ Q → Y that is the identity on Y, each σ(o) having finitely many values. Then a price on Y ∪ Q extends w and
satisfies |oo′| ≤ E |σ(o)σ(o′)| for all o, o′." 

### `prop_random_finite`

 Proposition prop:random for a random map with finitely many values σ_l, taken with probabilities θ_l. 

### `lem_hubs`

 **Paper: Lemma lem:hubs.** "Let I = I₁ ⊔ I₂, let a tensor t on I be a sum of r products of a tensor on I₁ and one
on I₂, and let n_p be its index sizes. For two further parties o₁, o₂ it is a restriction of
∏_{p ∈ I₁} ⟨n_p⟩_{p o₁} · ⟨r⟩_{o₁ o₂} · ∏_{p ∈ I₂} ⟨n_p⟩_{p o₂}, and this remains true when o₁, o₂ are identified with given
parties." In Lean the paper's I is A, its part I₁ is given by the predicate S, and α j, β j are the factors of the j-th
product, functions of the indices in I₁ and in I₂. The map π places the parties of A among those of a set I that also
contains o₁ and o₂, in any way; lem_hubs_further is the case of two further parties. 

### `lem_hubs_further`

 Lemma lem:hubs as printed, "for two further parties o₁, o₂": the parties are I₁ ⊔ I₂ and the two hubs. 
