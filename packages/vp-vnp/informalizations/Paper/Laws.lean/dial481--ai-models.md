---
{
  "module": "Paper/Laws.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Laws.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Laws.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Exchange identities"


### `def_law`

 **Paper: Definition def:law.** "A law on U_h over a commutative ring A consists of a finite family of pairs of
distinct elements (its slots), counted by a load σ, a finite nonempty index set with an injective code by λ ≥ 1 bits, a
load len_i on near pairs for every i, and for every i and every element g a table with values in A that depends on the
bits at g, such that ∏_e [the σ_e bits agree at both ends of e] = ∑_i ∑_y ∏_g (table of (i,g))." In the project a law
is an Nc.G.Law; this theorem lists what it carries. The two side conditions (nonempty, λ ≥ 1) are supplied by thm_laws. 

### `indices_agree`

 "Since the near pairs connect U_h, indices that agree along channels agree everywhere." 

### `laws_over_algebras`

 "The laws are finitely many polynomial identities with coefficients in A, so they hold over every commutative
A-algebra." 

### `thm_laws_poincare`

 The opening of the section: "Replacing C₀ by an integer that is at least 2C₀+1, Theorem thm:poincare reads: the mean
of |e|² over all pairs is at most C₀ times 2/b times the sum of |e|² over near pairs, for every price", where h is a
multiple of u with h ≥ 2u and b = |U_h|. C is the constant of the theorem and C₀ the integer. 

### `thm_laws_loads`

 The proof of Theorem thm:laws: "For every price the Cauchy–Schwarz inequality, twice, and the Poincaré inequality
give ∑_e σ_e|e| ≤ max_β ∑_{near e} β_e|e|", over rounded loads β = ⌈y⌉ with ‖y‖_* ≤ √C₀·‖σ‖. Here the two norms are
those of the weights α and β, and the quadratic inequality between them is the hypothesis. 

### `thm_laws_cover`

 The proof of Theorem thm:laws: "φ(W^σ) = 2^(∑ σ_e d_φ(e)), and d_φ is a price; so φ(W^σ) ≤ max φ(W^β). So duality
(Theorem thm:duality) covers W^(qσ) by at most 2^(εq) tensors W^β, with sums β of q elements of the given loads, for
every large q." The cover is given as an identity between functions of bits. 

### `thm_laws_ring`

 The proof of Theorem thm:laws: "The tables are the entries of the finitely many linear maps; let A be generated
by them and −1." 

### `thm_laws_over_field`

 The proof of Theorem thm:laws up to the choice of the ring: for one h and a Poincaré inequality with the integer
C₀, finitely many laws over K with the clauses (a) and (b). "Let a be a large integer", the loads σ_x = ⌈ax⌉, then
duality with one q, codes of λ ≤ εq+2 bits, and a₁ = aq. 

### `thm_laws`

 **Paper: Theorem thm:laws.** "There are a finitely generated subring A of k, a positive integer a₁, and finitely
many laws over A such that (a) for every load n and t ∈ ℕ with ‖n‖ ≤ a₁t some law has n ≤ tσ; (b) for every law and
index, ‖λ + len_i‖_* ≤ √C₁·a₁." Here, as fixed before it, u is that of Theorem thm:poincare, with its constant C; C₀
is an integer that is at least 2C+1; h is a multiple of u with h ≥ 2u, h ≥ 3 and 1 + 8C₁ ≤ h/4, where C₁ = 4C₀. Such
an h exists, and the theorem holds for every one. 

### `exists_laws`

 What the sections on towers and cuts take from Theorem thm:laws. 
