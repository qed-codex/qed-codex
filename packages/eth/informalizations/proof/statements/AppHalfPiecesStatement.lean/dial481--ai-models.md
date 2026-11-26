---
{
  "module": "proof/statements/AppHalfPiecesStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppHalfPiecesStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/AppHalfPiecesStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Appendix B: the ring V = ℚ[t₁, t₂, …], its operators a[r] and Q_s(a,b), the two lemmas on them, and the pieces with ρ = 1/√2

Definitions and statements only, in the order and in the words of the appendix; imports Mathlib and
the two statement files `PiecesStatement.lean` (pieces with parameters (ρ, c), without the
running time) and `PartitionStatement.lean` (the number p(E) of partitions). Every `def … : Prop` or
`structure … : Prop` below is a statement of the appendix; nothing is proved here.

Sums that the appendix writes as infinite sums with finitely many nonzero terms are `∑ᶠ` (Mathlib's
`finsum`, which is 0 if infinitely many terms are nonzero); each comes with the
statement that only finitely many terms are nonzero. 

 ## The ring and its operators 

### `binom`

 C(k, j) = k(k−1)⋯(k−j+1)/j! for integers k and j ≥ 0, and 0 for j < 0. 

### `BinomRules`

 Pascal's rule and Vandermonde's identity hold for all integers k, k'. (In the sum over j only
the terms with 0 ≤ j ≤ i are nonzero.) 

### `Ptn`

 A partition is a multiset of positive integers, its parts. 

### `wt`

 |μ|, the sum of the parts: μ is a partition of |μ|. 

### `zz`

 z_μ = ∏_k k^{m_k(μ)}·m_k(μ)!, where m_k(μ) = `μ.count k` is the number of parts equal to k. 

### `ptns`

 The partitions of E. 

### `ptnsZ`

 The partitions of an integer E; none if E < 0. 

### `pZ`

 p(E) for an integer E: p(0) = 1 and p(E) = 0 for E < 0. 

### `PtnFacts`

 The partitions of E are the multisets of positive integers with sum E, there are p(E) of them,
and p(E) ≤ p(E+1). 

### `V`

 V = ℚ[t₁, t₂, …]. 

### `tpow`

 The monomial t^μ = ∏_i t_{μ_i}. 

### `coef`

 The coefficient of t^μ in f. 

### `VE`

 V_E, the span of the t^μ with |μ| = E: the polynomials of weight E. V_E = 0 for E < 0. 

### `pn`

 The positive integer |k|, for an integer k ≠ 0. 

### `nabla`

 ∇_{−k} f = t_k·f and ∇_k f = k·∂f/∂t_k for k ≥ 1. (∇₀ is not defined in the appendix; here it is 0.) 

### `Choices`

 The choices in display (47): one nonzero integer k_i for each part μ_i, with Σ_i k_i = −r. 

### `term`

 One term of display (47), applied to f: ∏_i C(−k_i−1, μ_i−1) · ∏_{i: k_i<0} ∇_{k_i} · ∏_{i:
k_i>0} ∇_{k_i}. The differentiations are applied first. 

### `opMon`

 Display (47): a[r] for the monomial a = t^μ whose parts are listed in μ. 

### `op`

 a[r] for all a ∈ V: display (47), extended linearly. 

### `OpFacts`

 What the appendix says with display (47): on every f only finitely many terms are nonzero; the
order in which the parts are listed does not matter; a[r] is linear in f and in a;
and for a monomial it is the sum (47). 

### `IsInt`

 All coefficients are integers. 

### `O1`

 (O1): a[r] maps V_E to V_{E+r}, so a[r]f = 0 if f ∈ V_E and E + r < 0; it maps integer
polynomials to integer polynomials if a is one; and 1[r] = [r = 0]·Id. 

### `pairing`

 The number a[−h]·b, for b ∈ V_h. 

### `O3`

 (O3): if b ∈ V_h, then a[−h]·b ∈ V₀ is a number, and only terms with all k_i positive contribute
to it. 

### `part`

 ā_{h'}, the part of a of weight h'. 

### `WtLe`

 a = Σ_{h'=0}^{h} ā_{h'} with ā_{h'} ∈ V_{h'}. 

### `angle`

 a^⟨i⟩ = Σ_{h'} C(h'+h, i)·ā_{h'}. 

### `Q`

 Display (48): Q_s(a,b) = Σ_{i=0}^{2h} (−1)^i·a^⟨i⟩[s−h+i] b[h−s−i]. 

### `Q'`

 The same with the two factors exchanged in all products. 

### `LemmaQ`

 The lemma on the operators Q_s. Let h ≥ 1, b ∈ V_h and a = Σ_{h' ≤ h} ā_{h'}. On V_E, for every
E ≥ 0: (a) Q_s(a,b) does not change if the two factors are exchanged in all products of (48)
at once; (b) Q_s(a,b) = 0 for |s| > E + h; (c) Σ_{|s| ≤ E+h} Q_s(a,b) = (a[−h]b)·Id. 

### `y`

 y_n = Σ_{j=1}^{n} C(n,j)·t_j. 

### `aFam`

 a^μ = ∏_i (−1)^{μ_i−1}·y_{μ_i}. 

### `bFam`

 b^μ = (h!/z_μ)·t^μ, for a partition μ of h. 

### `LemmaDual`

 The lemma on the dual families: a^μ[−h]·b^ν = h!·[μ = ν] for all partitions μ, ν of h. 

### `ZDvd`

 h!/z_μ is an integer. 

 ## The pieces 

### `hOf`

 The least integer h ≥ 2 with p(h) ≥ 2^λ. 

### `HOfSpec`

 Such an h exists, so `hOf lam` is the least integer h ≥ 2 with p(h) ≥ 2^λ. 

### `desc`

 A partition written as a nonincreasing sequence. 

### `lexNum`

 The number of μ, counting from 0, in the lexicographic list of the partitions of h written as
nonincreasing sequences: the number of partitions of h that come before μ. 

### `val`

 A string read as an integer, first bit lowest. (The appendix does not say which bit is the
lowest.) 

### `IsMu`

 μ(x) is the partition of h with number x in that list. 

### `piece`

 A_s(x,y,u,v) = the coefficient of t^{μ(u)} in Q_s(a^{μ(x)}, b^{μ(v)})·t^{μ(y)}. 

### `Rrow`

 R^row_s = Σ_{i=0}^{2h} p(s+i). 

### `Rcol`

 R^col_s = Σ_{i=0}^{2h} p(2h−s−i). 

### `PieceFacts`

 The steps of the proof of the theorem on the pieces that are statements about the ring, for
partitions μ(x), μ(y), μ(u), μ(v) of h ≥ 1, written ξ, η, υ, ν. 

### `PieceFacts.wtLe`

 a^μ is a combination of monomials of weight at most h, as (48) requires. 

### `PieceFacts.sum`

 Σ_s A_s = h!·[x = v]·[y = u]. 

### `PieceFacts.row`

 Display (54). 

### `PieceFacts.col`

 Display (55). 

### `PieceFacts.int_a`

 All factors are integers. 

### `PieceFacts.terms`

 The numbers of terms are both at least 1. 

### `ThmHalfPiecesPure`

 The theorem on the pieces with ρ = 1/√2, with the construction of its proof and without the
running time: for an absolute constant c and every λ ≥ 1, with h = `hOf λ` and μ(x) the partition of
h with number x in the lexicographic list, the functions A_s, s ∈ {−2h, …, 2h}, with d = h!, c^row_s =
⌈log R^row_s⌉ and c^col_s = ⌈log R^col_s⌉, have the properties (a), (b) and the sizes of
(c) of pieces with parameters (1/√2, c). 
