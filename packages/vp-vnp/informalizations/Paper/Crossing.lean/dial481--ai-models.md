---
{
  "module": "Paper/Crossing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Crossing.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Crossing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Two crossing wires": the inequality

The states are in Paper/States.lean (Lemma lem:count) and the identity is in Paper/Identity.lean (Proposition prop:identity).


### `prop_crossing_cut`

 Lemma lem:hubs, read for a spectral point φ: a tensor that is a sum of r products of a tensor on the legs in S and one on the
other legs has φ at most the product of the values of the wires to the hubs o₁, o₂ and of the wire ⟨r⟩ between them. 

### `prop_crossing_hubs_c`

 Proof of Proposition prop:crossing: "Lemma lem:hubs, with the hubs o, o′ for (c) …, bounds φ(Ψ_N)." The four legs are at
x, y, v, u, and f is a sum of R products of a function of the indices at x, y and one of those at v, u. 

### `prop_crossing_hubs_b`

 Proof of Proposition prop:crossing: "Lemma lem:hubs, with the hubs … w, w′ for (b), bounds φ(Ψ_N)." Here f is a sum of L
products of a function of the indices at x, u and one of those at y, v. 

### `prop_crossing_cover`

 Proof of Proposition prop:crossing: "The product of the two wires is covered by the Θ+1 tensors Ψ_N of Proposition
prop:identity (a), φ is subadditive". The left side is the value of φ at the two wires, of dimensions |α| and |β|. 

### `prop_crossing_some`

 Proof of Proposition prop:crossing: "so some N has ln φ(Ψ_N) ≥ (p|xv| + q|yu| − o(1))κ√n₀". Before logarithms: some φ(Ψ_N) is
at least the value of the two wires divided by the number Θ+1 of the tensors. 

### `prop_crossing_term`

 Proof of Proposition prop:crossing: "Lemma lem:hubs, with the hubs o, o′ for (c) and w, w′ for (b), bounds φ(Ψ_N) in both ways."
So for the N of the step before, in logarithms: ln|α|·|xv| + ln|β|·|yu| is at most ln(Θ+1) plus each of the two bounds through the
hubs, where Ψ_N is a sum of R_N products as in (c) and of L_N products as in (b). 

### `prop_crossing_classes`

 Proof of Proposition prop:crossing: "By pigeonhole some classes Σ_i of energy e_i ≤ E_i contain at least a fraction (E_i+1)⁻²,
and of course at most all, of the states of energy at most E_i." 

### `prop_crossing_class_size`

 Proof of Proposition prop:crossing: "so, in units of κ√n₀, their logarithms are p + o(1) and q + o(1) by Lemma lem:count."
Here κ is a constant with the two properties of Lemma lem:count, n is the paper's n₀, and the class Σ of size μ and energy
e ≤ E = ⌊p²n⌋ is the one found by pigeonhole. 

### `prop_crossing_products`

 Proof of Proposition prop:crossing: "In the same units the logarithm of the number of products in (b) is at most l + o(1) and
that in (c) at most r + o(1), with l² = N/n₀, r² = (Θ−N)/n₀". Here M stands for N and for Θ − N, which are at most Θ ≤ An, and
(M+1)P(M) is the number of products. 

### `prop_crossing_tensors`

 Proof of Proposition prop:crossing, the tensors: for every δ > 0 there are s > 0 and finite sets α, β (in the proof: the
paper's κ√n₀ and the classes of states, by pigeonhole and Lemma lem:count) with ln|α| = (p ± δ)s and ln|β| = (q ± δ)s, and
at most e^(δs) tensors Ψ_N with sum the two wires (Proposition prop:identity (a)), where Ψ_N is a sum of at most e^((r+δ)s) products as in (c) and of at most e^((l+δ)s)
products as in (b), with r² + l² ≤ 2(p² + q²). 

### `prop_crossing_spectral`

 Proof of Proposition prop:crossing: "So it suffices to treat d_φ for a spectral point φ"; this is the statement for d_φ. "A limit
of (r, l) along a subsequence proves the first statement." 

### `prop_crossing_first`

 Proposition prop:crossing, the first statement. "Pull the price back to eight distinct points; this covers coincidences. Both
inequalities are homogeneous in the distances, and the pairs (r, l) lie in a compact set, so they pass to limits." 

### `prop_crossing`

 **Paper: Proposition prop:crossing.** "Let x, v, y, u, o, o′, w, w′ be points of a price and p, q ≥ 0. There are r, l ≥ 0 with
r² + l² ≤ 2(p² + q²) such that p|xv| + q|yu| is at most each of p|xo| + q|yo| + p|vo′| + q|uo′| + r|oo′|, p|xw| + q|uw| + q|yw′| + p|vw′| + l|ww′|.
In particular, for every τ > 0," the inequality (eq:Q) holds. The first statement is prop_crossing_first; for the second,
"add the two bounds and use rλ ≤ (τ/2)r² + λ²/(2τ)". 

### `eq_Q`

 **Paper: display eq:Q.** "In particular, for every τ > 0, 2(p|xv| + q|yu|) ≤ p(|xo| + |vo′| + |xw| + |vw′|) +
q(|yo| + |uo′| + |uw| + |yw′|) + τ(p² + q²) + (|oo′|² + |ww′|²)/(2τ)." This is the second statement of Proposition prop:crossing. 
