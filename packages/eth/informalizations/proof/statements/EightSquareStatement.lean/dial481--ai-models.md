---
{
  "module": "proof/statements/EightSquareStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/EightSquareStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/EightSquareStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity: definitions and statements only

Section 4 of the paper, «Two crossing equalities as a sum of ⌈λ/3⌉ + 1 cheaper functions», which
starts from the eight-square identity of Degen and Graves. This file has no proofs. It imports parts
of Mathlib and
`PiecesStatement.lean` (which imports only Mathlib), from which it takes: `Pieces.Bits n` (strings
of n bits), `Pieces.Four n` (integer functions of four strings x, y, u, v), `Pieces.cross` ([x =
v][y = u]), `Pieces.rowwise`
(a function of (x,y) and (u,v)) and `Pieces.colwise` (a function of (x,u) and (y,v)).

The statements are `Eight.Signs` (the eight-square identity in the form used in Section 4) and
`Eight.LemPieces` (Lemma 2 without «computable in time poly(λ)», which needs a model of computation
that this file does not import). 

 ## The eight-square identity 

### `Block`

 A block of three bits, p = (p₁, p₂, p₃). 

### `bxor`

 p ⊕ q, bit by bit. 

### `phi`

 φ(p,q) = Σ_{1 ≤ i ≤ j ≤ 3} p_i q_j + q₁p₂p₃ + p₁q₂p₃ + p₁p₂q₃, as a natural number. 

### `sigma`

 The sign σ(p,q) = (−1)^{φ(p,q)}. 

### `Signs`

 The eight-square identity, first form: for all blocks p, q, p', q' with p ⊕ q = p' ⊕ q' and q ≠
q', σ(p,q)σ(p',q') + σ(p,q')σ(p',q) = 0. 

 ## The functions R and C of four blocks 

### `psi`

 ψ_k(p,q) = [p ⊕ q = k]·σ(p,q). 

### `Rb`

 R(x,y,u,v) = Σ_k ψ_k(x,y)·ψ_k(v,u). 

### `Cb`

 C(x,y,u,v) = Σ_k ψ_k(x,u)·ψ_k(v,y). 

### `FactorsLe`

 Definition 1 of the paper with a bound: F(z,z') = Σ_θ f(z,θ)·f'(z',θ) over θ ∈ {0,1}^c, and all
values of f and f' are at most b in absolute value. (`Pieces.FactorsThrough` has the strict bound
«below b».) 

 ## The pieces A_0, …, A_t 

### `tOf`

 t = ⌈λ/3⌉. 

### `bitAt`

 The bit number j (from 0) of a string after zeros have been appended. 

### `blockAt`

 The block number s (from 0) of a string after zeros have been appended. 

### `prodRC`

 ∏_s (R(x_s,y_s,u_s,v_s) + T·C(x_s,y_s,u_s,v_s)), a polynomial in T; the blocks are numbered s =
0, …, t − 1. 

### `A`

 A_i: the coefficient of T^i. 

### `crow`

 c_i^row = min{2λ, 4t + 3i}. 

### `ccol`

 c_i^col = min{2λ, 7t − 3i}. (For i ≤ t the subtraction of natural numbers is the ordinary one.) 

### `rho`

 ρ = 11/12. 

### `LemPieces`

 **Lemma 2**, without «computable in time poly(λ)». For every λ ≥ 1 and i ∈ {0, …, t}: (a) A_0 +
… + A_t = 2^t·[x = v][y = u], and |A_i| ≤ 2^t; (b) as a function of (x,y) and (u,v), A_i factors
through c_i^row bits, as a
function of (x,u) and (y,v) through c_i^col bits, and the functions of both factorizations have
values at most 2^t in absolute value; (c) c_i^row ≤ 2λ, c_i^col ≤ 2λ and c_i^row + c_i^col ≤ 4ρλ +
8, where ρ = 11/12. 

### `LemPieces.c_sum_t`

 from the proof of (c): c_i^row + c_i^col ≤ 11t 
