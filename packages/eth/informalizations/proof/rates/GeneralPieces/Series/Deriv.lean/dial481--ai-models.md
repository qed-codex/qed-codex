---
{
  "module": "proof/rates/GeneralPieces/Series/Deriv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Deriv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Series/Deriv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on the operators Q_s, paragraph "Series": termwise differentiation, and display (49)

This follows the paragraph "Series" of the proof of the lemma on the operators Q_s (Appendix B),
from "and are closed under termwise differentiation" to display (49), and the two sentences of the
paragraph "Generating functions" that evaluate the sums over k in κ and κ'. As in `Rings.lean`,
everything is proved once in the ring `S` with an inner variable u and an outer variable v, and then
read twice: in 𝓛₊, ∂_{ω₁} = ∂/∂u and ∂_{ω₂} = ∂/∂v; in 𝓛₋ it is the other way round.
The differentiations are derivations of the ℚ-algebra `S` in Mathlib's sense (`du`, `dv`); `cf_du`,
`cf_dv` say that they act term by term. The product rule is proved first for u·∂/∂u and
v·∂/∂v, which multiply the coefficient of u^x·v^y by x and by y (`twist_mul`), and ∂/∂u is u⁻¹ times
u·∂/∂u.
Display (49) is proved in any ring with two derivations and an element ε with D₁ε = −ε² and D₂ε = ε²
(`displayGamma`), which is why Γ_{j,n} is the same for both signs; it is the number
`ClauseBound.Boson.Gam j n` = n·C(−n−1, j−1). The paper does not write out the sum over k in κ';
`kappa'_sum` does. 

 ### An operator that acts on every coefficient of a series 

### `twist`

 The series whose coefficient of v^y is D_y applied to the coefficient of v^y in f. 

### `twist_mul`

 If D_{i+j}(ab) = D_i(a)·b + a·D_j(b), the operator satisfies the product rule. 

 ### u·∂/∂u and v·∂/∂v 

### `thI`

 u·d/du on the Laurent polynomials in u: the coefficient of u^x is multiplied by x. 

### `thI_mul`

 The product rule for u·d/du on the Laurent polynomials. 

### `thU`

 u·∂/∂u on the series. 

### `thV`

 v·∂/∂v on the series. 

 ### Termwise differentiation 

### `du`

 ∂/∂u, termwise: u⁻¹ times u·∂/∂u. It is linear and satisfies the product rule. 

### `dv`

 ∂/∂v, termwise: v⁻¹ times v·∂/∂v. It is linear and satisfies the product rule. 

### `cf_du`

 ∂/∂u is termwise: the term c·u^{x+1}·v^y becomes (x+1)·c·u^x·v^y. 

### `cf_dv`

 ∂/∂v is termwise: the term c·u^x·v^{y+1} becomes (y+1)·c·u^x·v^y. 

### `du_eps`

 Differentiating (u − v)·ε = 1 with respect to u. 

### `dv_eps`

 Differentiating (u − v)·ε = 1 with respect to v. 

 ### The two readings 

### `d1P`

 ∂_{ω₁} on 𝓛₊. 

### `d2P`

 ∂_{ω₂} on 𝓛₊. 

### `d1M`

 ∂_{ω₁} on 𝓛₋. 

### `d2M`

 ∂_{ω₂} on 𝓛₋. 

### `d1P_epsP`

 "Differentiating (ω₁ − ω₂)·ε₊ = 1 gives ∂_{ω₁}ε₊ = −ε₊²". 

### `d2P_epsP`

 "… and ∂_{ω₂}ε₊ = ε₊²". 

### `d1M_epsM`

 "Differentiating (ω₁ − ω₂)·ε₋ = 1 gives ∂_{ω₁}ε₋ = −ε₋²". 

### `d2M_epsM`

 "… and ∂_{ω₂}ε₋ = ε₋²". 

 ### Display (49), in any ring with two derivations and an element ε with D₁ε = −ε² and D₂ε = ε² 

### `deriv_pow`

 If Dε = s·ε², then D(ε^m) = s·m·ε^{m+1}. 

### `iter_pos`

 m!·D₂^b(ε^{m+1}) = (m+b)!·ε^{m+1+b}. 

### `iter_neg`

 D₁^a(ε^m) = a!·C(−m, a)·ε^{m+a}. 

### `displayGamma`

 Display (49) with Γ_{j,n} = n·C(−n−1, j−1). 

### `displayGamma_P`

 Display (49) for ε₊: (1/((j−1)!(n−1)!))·∂_{ω₁}^{j−1}∂_{ω₂}^{n−1}ε₊² = Γ_{j,n}·ε₊^{j+n}. 

### `displayGamma_M`

 Display (49) for ε₋, with the same number Γ_{j,n}. 

 ### The series Σ_{k ≥ 1} c_k·u^{−k−p}·v^{k−q}, differentiated term by term 

### `ser`

 Σ_{k ≥ 1} c_k·u^{−k−p}·v^{k−q}. 

### `du_ser`

 ∂/∂u of the term u^{−k−p}·v^{k−q} is (−k−p)·u^{−k−p−1}·v^{k−q}. 

### `dv_ser`

 ∂/∂v of the term u^{−k−p}·v^{k−q} is (k−q)·u^{−k−p}·v^{k−q−1}. 

### `du_iter_ser`

 ∂^a/∂u^a of the term u^{−k−p}·v^{k−q} is a!·C(−k−p, a)·u^{−k−p−a}·v^{k−q}. 

### `dv_iter_ser`

 ∂^b/∂v^b of the term u^{−k−p}·v^{k−q} is b!·C(k−q, b)·u^{−k−p}·v^{k−q−b}. 

### `dv_eps_eq`

 ∂ε/∂v = Σ_{k ≥ 1} k·u^{−k−1}·v^{k−1}. 

### `sumP`

 Σ_{k ≥ 1} c_k·ω₁^{−k−j}·ω₂^{k−n} in 𝓛₊. 

### `sumM`

 Σ_{k ≥ 1} c_k·ω₁^{k−j}·ω₂^{−k−n} in 𝓛₋. 

### `cfP_sumP`

 In Σ_{k ≥ 1} c_k·ω₁^{−k−j}·ω₂^{k−n} the coefficient of ω₁^{−k−j}·ω₂^{k−n}, k ≥ 1, is c_k; all
other coefficients vanish. 

### `epsP_sq`

 "ε₊² = ∂_{ω₂}ε₊ = Σ_k k·ω₁^{−k−1}·ω₂^{k−1}". 

### `epsM_sq`

 "ε₋² = −∂_{ω₁}ε₋ = Σ_k k·ω₂^{−k−1}·ω₁^{k−1}". 

### `leftGamma_P`

 "The sum over k is the left side of (49)", in 𝓛₊: differentiating Σ_k k·ω₁^{−k−1}·ω₂^{k−1} term
by term. 

### `leftGamma_M`

 The same in 𝓛₋: differentiating Σ_k k·ω₂^{−k−1}·ω₁^{k−1} term by term. 

### `kappa_sum`

 The sum in the display for κ: Σ_{k ≥ 1} k·C(−k−1, j−1)·C(k−1, n−1)·ω₁^{−k−j}·ω₂^{k−n} =
Γ_{j,n}·ε₊^{j+n}, "because the sum over k is the left side of (49)". 

### `kappa'_sum`

 The sum for κ', "in the same way": Σ_{k ≥ 1} k·C(k−1, j−1)·C(−k−1, n−1)·ω₁^{k−j}·ω₂^{−k−n} =
Γ_{j,n}·ε₋^{j+n}. 
