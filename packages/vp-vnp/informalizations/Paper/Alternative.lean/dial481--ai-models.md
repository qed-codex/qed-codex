---
{
  "module": "Paper/Alternative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Alternative.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Alternative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Flat or contracting"

The definitions, then the steps of the proof of Theorem thm:alt in the order of the paper, then the theorem. The paper's
n_a(W) = |a, a+W|² is `nn w a W`, its B_a(W, W') is `BB w a W W'`, D(r)² is `meanSq w r`, and u xᵀ is `vecMulVec u x`.


 ## Definitions 

### `meanSq`

 The mean of |a, a+W|² over all matrices a and all matrices W of rank r: the square of the paper's D(r). 

### `distAtRank`

 The paper's D(r). 

### `Flat`

 The flat case: "all finite subsets of all Euclidean spaces, with their metrics, are prices". 

### `Contracting`

 The contracting case: "there are an integer μ ≥ 2 and a real s with 1 ≤ s, s² < μ, such that D(μ) ≤ sD(1) for all
prices on Mat_μ(F₂)". 

### `def_cases`

 **Paper: Definition def:cases.** "We are in the flat case if all finite subsets of all Euclidean spaces, with their
metrics, are prices. We are in the contracting case if there are an integer μ ≥ 2 and a real s with 1 ≤ s, s² < μ, such
that D(μ) ≤ sD(1) for all prices on Mat_μ(F₂)." Here D(r)² is "the mean of |a, a+W|² over all matrices a and all matrices
W of rank r". 

### `def_transversal`

 "We call W₁, W₂, … transversal if both their column spaces and their row spaces are independent": this is the
definition `Nc.Flag.Transversal`, unfolded here. 

### `transversal_pair`

 Two matrices are transversal if and only if, after multiplication by invertible matrices p and q, they are diagonal
matrices with entries 0 and 1 and with disjoint supports. 

### `transversal_triple`

 The same for three matrices. 

 ## Matrices of one rank 

### `rank_units`

 Multiplication by invertible matrices keeps the rank. 

### `card_mul_DM`

 The sum of f(p·dg(S)·q)² over all invertible p and q (this is `DM f (dg S)`), divided by the number of these pairs, is the
mean of f(W)² over the matrices W of rank |S|. 

### `frames`

 The number of the triples (p, q, a). 

### `MD_eq_meanSq`

 For uniform invertible p and q the matrix p·dg(S)·q is uniform of rank |S|. 

 ## The proof of Theorem thm:alt: equality 

### `thm_alt_quadrangle`

 "Every price is pulled back from the metric of a CAT(0) space, by Proposition prop:space." So Lemma lem:toolkit (b)
holds in every price: the squared diagonals of a quadrangle add up to at most its squared sides, and if there is
equality, opposite sides are equal. 

### `thm_alt_mean_defect`

 "Let (W, W') be a random transversal pair of ranks i, j, i+j ≤ μ, and let a be uniform and independent of it; then W, W',
W+W' are uniform of ranks i, j, i+j. Both diagonals of a, a+W, a+W+W', a+W' have difference W+W'." The random pair is
(p·dg(S)·q, p·dg(T)·q) for disjoint sets S, T of i and j indices and uniform invertible p, q; that the three matrices are
uniform is `MD_eq_meanSq`. The statement is the consequence: the sum over p, q and a of the squared sides minus the squared
diagonals is the number of the (p, q, a) times 2(D(i)² + D(j)² − D(i+j)²). 

### `thm_alt_subadditive`

 "By Lemma lem:toolkit (b), D(i+j)² ≤ D(i)² + D(j)²", for i + j ≤ μ. 

### `meanSq_le`

 D(r)² ≤ r·D(1)². 

### `thm_alt_bounded`

 "Every distance is at most a constant, depending on μ, times D(1)." 

### `Extremal`

 "A price with D(1) = 1 and D(μ)² = μ." 

### `thm_alt_extremal`

 "As we are not in the contracting case, there are prices with D(μ) > sD(1) for every s < √μ. Every distance is at most
a constant, depending on μ, times D(1), so we may scale to D(1) = 1 and, by compactness, pass to a limit: a price with
D(1) = 1 and D(μ)² = μ." 

### `thm_alt_ranks`

 "For it D(r)² = r for all r, as μ ≤ D(r)² + D(μ−r)²." 

### `thm_alt_equality`

 "So equality holds for all these quadrangles, that is, for every a and every transversal pair": the squared sides of
a, a+W, a+W+W', a+W' add up to the squared diagonals. 

### `thm_alt_opposite`

 "For transversal W, W', opposite sides are equal: n_{a+W'}(W) = n_a(W)." 

### `thm_alt_diagonal`

 "Also all quadrangles have equality, so |a+W, a+W'|² = 2n_a(W) + 2n_a(W') − n_a(W+W')." 

 ## The proof of Theorem thm:alt: rank one 

### `thm_alt_additive`

 "Insert this into the quadrangle at a+W₂ with sides W₁, W₂+W₃, whose other vertices are a+W₁+W₂, a+W₃ and a+W₁+W₃. This
gives, for transversal W₁, W₂, W₃, … B_a(W₁, W₂+W₃) = B_a(W₁, W₂) + B_a(W₁, W₃)." 

### `exists_vec`

 A matrix of rank one is u xᵀ with vectors u, x ≠ 0. 

### `thm_alt_identity`

 "Now u₁x₁ᵀ + u₂x₂ᵀ = u₁(x₁+x₂)ᵀ + (u₁+u₂)x₂ᵀ." 

 The exchange is used twice: for Φ = B_a(W, ·), which is additive by `thm_alt_additive`, and "with W = 0 and n_a in place of
B_a". So it is stated for a matrix W and any function Φ with Φ(V₁ + V₂) = Φ(V₁) + Φ(V₂) for transversal W, V₁, V₂; the paper's
χ(u, x) is Φ(u xᵀ). 

### `thm_alt_exchange`

 "Let W, u₁x₁ᵀ, u₂x₂ᵀ be transversal … For χ(u,x) = B_a(W, uxᵀ) this gives
χ(u₁,x₁) − χ(u₁,x₁+x₂) = χ(u₁+u₂,x₂) − χ(u₂,x₂). The right side does not depend on x₁, and the left side changes sign when x₁
becomes x₁+x₂; both vanish." The matrices u₁x₁ᵀ and u₂x₂ᵀ have rank one, that is, they are not zero. 

### `thm_alt_move`

 "So x may be changed by any vector outside its span with the row space of W, and likewise u." Here u xᵀ ≠ 0 is
transversal to W, that is, u is outside the column space and x outside the row space of W, and rk W + 2 ≤ μ. 

### `thm_alt_connect`

 "As μ ≥ 3, such moves connect all vectors outside the column, respectively row space of a rank-one W": so Φ has one
value on the matrices of rank one that are transversal to W. (What is used of μ ≥ 3 and rk W = 1 is rk W + 2 ≤ μ.) 

### `thm_alt_third`

 "… and any two matrices of rank one are both transversal to a third", as μ ≥ 3. 

### `thm_alt_lambda`

 "As B_a is symmetric, it has one value λ(a) on all transversal pairs of rank one." 

### `thm_alt_reflect`

 "Since n_{a+V}(V) = n_a(V), n_{a+V}(W') = n_a(W') and n_{a+V}(V+W') = |a+V, a+W'|², the display of the first step gives
B_{a+V}(V, W') = −B_a(V, W')", for transversal V, W'. 

### `thm_alt_orthogonal`

 "So λ = 0": B_a vanishes on the transversal pairs of rank one. The proof is the printed one, "By additivity this value is
2λ if V has rank two; so we get λ(a+V) = −λ(a) for V of rank one or two; but two steps of rank one give λ(a+V) = λ(a)", for
the matrices V = dg{i}, dg{j} and dg{i} + dg{j}. 

### `BB_singleton_set`

 By additivity, B_a vanishes on p·dg{i}·q and p·dg(S)·q if i is not in S. 

### `nn_X`

 So n_a(p·dg(S)·q) is the sum of the n_a(p·dg{i}·q) over i in S. 

### `thm_alt_sum`

 "By additivity n_a is additive on transversal sums." 

### `thm_alt_one_value`

 "The same exchange, with W = 0 and n_a in place of B_a, shows that n_a has one value on rank one". 

### `thm_alt_base_point`

 "… as n_{a+W'}(W) = n_a(W), it does not depend on a". 

### `thm_alt_rank_one`

 "… so it is 1": the mean of n_a(W) over all a and all W of rank one is D(1)² = 1. 

### `thm_alt_rank`

 "Hence |a, a'|² = rk(a − a')." 

### `thm_alt_rank_price`

 "Suppose we are not in the contracting case and fix μ ≥ 3. We show that some price is exactly the square root of the
rank of the difference." 

 ## The proof of Theorem thm:alt: a solid cube 

### `cubePts`

 Points of the solid cube [0,1]^μ whose coordinates from `k` on are 0 or 1. 

### `thm_alt_fill`

 "Fill it one coordinate at a time: Lemma lem:toolkit (f), applied to opposite edges in the new direction, shows that
the map stays isometric." A map F that is isometric on the points whose coordinates from k on are 0 or 1 has an extension F'
that is isometric on the points whose coordinates from k + 1 on are 0 or 1. 

### `thm_alt_cube`

 "Fill it one coordinate at a time": if points f(S) of a CAT(0) space have the distances of the vertices of the cube, then the map that sends the
vertex with the coordinates 1 on S and 0 elsewhere to f(S) extends to an isometric map F of the solid cube [0,1]^μ. 

### `thm_alt_vertices`

 "The diagonal 0/1 matrices now form the vertices of a Euclidean cube [0,1]^μ in a price space." 

### `thm_alt_euclidean`

 "Every finite Euclidean configuration of dimension at most μ is, up to translation and scale, a subset of the cube,
hence a price." 

### `thm_alt`

 **Paper: Theorem thm:alt.** "One of the two cases occurs." 
