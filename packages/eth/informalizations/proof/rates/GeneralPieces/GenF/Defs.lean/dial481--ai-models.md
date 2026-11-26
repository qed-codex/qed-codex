---
{
  "module": "proof/rates/GeneralPieces/GenF/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/GenF/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 9 (Appendix B), paragraph "Generating functions" of its proof: the rings and the series J, A, B, κ

As for the rings 𝓛₊ and 𝓛₋, everything is set up once, for an inner variable u and an outer variable
v, and read twice. In the first reading (`rd = false`) u = ω₁, v = ω₂, the inner family
is A (variables x_n) and the outer family is B (variables x'_n); in the second (`rd = true`) u = ω₂,
v = ω₁, the inner family is B and the outer family is A.
The paper says what an equation between products of exponentials means: apply both sides to a
polynomial and take the coefficient of a monomial in the t_k and of a monomial in the x_n, x'_n.
Here this is the typing: an element of `W` has, for every monomial in the x_n, x'_n and every power
of v, a polynomial in the t_k over ℚ[u, u⁻¹] as its coefficient.
The parts, the indices k of t_k and the indices n of x_n are natural numbers; x₀ and x'₀ are there
but occur nowhere, and t₀ does not occur in the statements that are used (they ask 0 ∉ σ, 0 ∉ σ').
The series J_n are the paper's for n ≥ 1; at n = 0 their values are not used. Definitions, and the
bound on the support that `JpV` needs. 

### `Lu`

 ℚ[u, u⁻¹]. 

### `Vu`

 The polynomials in the t_k over ℚ[u, u⁻¹]. 

### `Tv`

 The series Σ_{j ≥ j₀} p_j·v^j whose coefficients p_j are polynomials in the t_k over ℚ[u, u⁻¹]. 

### `X`

 The names of the further variables: x_n is `Sum.inl n` and x'_n is `Sum.inr n`. 

### `W`

 The formal power series in the x_n, x'_n over `Tv`. 

### `PS`

 The formal power series in the x_n, x'_n over the ring `S` of series in u and v: here the matrix
entries live. 

### `emb`

 `S` is contained in `Tv`: the constant polynomials. 

### `embW`

 `PS` is contained in `W`. 

### `tT`

 t_k as an element of `Tv`. 

### `bra`

 The coefficient of the monomial t^σ, taken in the coefficient of every power of v. 

### `braW`

 The same, taken in the coefficient of every monomial in the x_n, x'_n. This is ⟨·⟩ before the
operator is applied to t^σ'. 

### `xi`

 The variable of the inner family with index n. 

### `xo`

 The variable of the outer family with index n. 

### `z0`

 f, made 0 at the index 0. 

### `sel`

 The function on the variables that is f on the inner and g on the outer family, and 0 on x₀ and
x'₀: these two variables occur nowhere. 

### `bil`

 The bilinear form Σ_{i,i'} q_{i,i'}·x_i·x_{i'}; used only when q_{i,i'} = 0 unless x_i is of the
inner and x_{i'} of the outer family. 

### `JpV`

 J_n^+(v) = Σ_{l ≥ 1} C(l−1, n−1)·t_l·v^{l−n}, an element of `Tv`; the operator is the
multiplication by it. For n ≥ 1 the terms with l < n vanish. 

### `JpU`

 The part of J_n^+(u) with l ≤ E: Σ_{1 ≤ l ≤ E} C(l−1, n−1)·t_l·u^{l−n}. The other terms do not
contribute to the coefficient of a monomial of weight at most E. 

### `JmU`

 J_n^-(u) = Σ_{k ≥ 1} C(−k−1, n−1)·u^{−k−n}·∇_k, with ∇_k = k·∂/∂t_k: the derivation of the
polynomials in the t_k with t_k ↦ k·C(−k−1, n−1)·u^{−k−n}. 

### `sfB'`

 Σ_n x'_n·C(−k−1, n−1)·v^{−k−n}, the coefficient of ∇_k in B⁻ (outer family). 

### `Bp`

 B⁺ = Σ_n x'_n·J_n^+(v). 

### `Ap`

 The part of A⁺ = Σ_n x_n·J_n^+(u) with l ≤ E. 

### `ket`

 e^{B⁻}·t^σ', defined as the product of the t_k + k·(the coefficient of ∇_k in B⁻) over the parts
k of σ'. By Taylor's formula this is the series Σ_m (B⁻)^m/m! applied to t^σ'.
e^{B⁻} is always applied first, to a monomial. 

### `kapS`

 The sum over k in the display for κ, for the index p of the inner and q of the outer family:
Σ_{k ≥ 1} k·C(−k−1, p−1)·C(k−1, q−1)·u^{−k−p}·v^{k−q}. 

### `kap`

 κ = Σ_{p,q} x_p·x'_q·(the sum over k). By the display for κ in the paper, this is Σ_k k·𝖠_k·𝖡_k,
with the 𝖠_k and 𝖡_k of the paper. 
