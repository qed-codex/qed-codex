---
{
  "module": "Paper/Toolkit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Toolkit.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Toolkit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Prices are nonpositively curved": CAT(0) spaces

The definition of CAT(0) spaces and Lemma lem:toolkit, part by part. All of it rests on the inequality (CN) alone, which is
the class Cat.CN. Two predicates of the library are used in the proofs: Cat.IsPt x v t b says that b satisfies the inequality
of part (a), and Cat.IsBary w x b that b satisfies the inequality of part (c), for weights w.


### `cat0_iff`

 The paper's definition: "A complete metric space is CAT(0) if any two points x, v have a midpoint and (CN) holds
for it." 

### `lem_toolkit_minimization`

 The minimization behind parts (a), (c) and (d): "Strict convexity of the functions to be minimized, from (CN), makes
minimizing sequences converge; comparing the minimum with points close to it on [b,y], respectively [Py,q], gives the
inequalities." Let C be nonempty, closed and convex, and let Θ ≥ 0 be continuous with
Θ(m) ≤ ½Θ(x) + ½Θ(v) − (c/4)|xv|² for the midpoint m of x, v ∈ C, where c > 0. Then some b ∈ C has Θ(y) ≥ Θ(b) + c|yb|² for all
y ∈ C. 

### `lem_toolkit_c_exists`

 The first half of part (c) with weights: points x_i with weights w_i ≥ 0 have a barycenter b, with
∑ w_i|yx_i|² ≥ (∑ w_i)|yb|² + ∑ w_i|bx_i|² for all y. It is the minimizer of y ↦ ∑ w_i|yx_i|² given by lem_toolkit_minimization. 

### `lem_toolkit_a`

 **Paper: Lemma lem:toolkit (a).** "For x, v and t ∈ [0,1] exactly one point γ(t) has distances t|xv|, (1−t)|xv| from
them, and |zγ(t)|² ≤ (1−t)|zx|² + t|zv|² − t(1−t)|xv|²." The point is the barycenter of x and v with the weights 1−t and t. 

### `lem_toolkit_a_isPt`

 Part (a) in the words of the library. 

### `lem_toolkit_a_of_dist`

 A point with the distances of part (a) satisfies its inequality. 

### `lem_toolkit_b_box`

 The first step of the proof of part (b): for the point q at s on [p,p′], insert (a) twice into
t(1−t)|xv|² ≤ (1−t)|xq|² + t|qv|². 

### `lem_toolkit_b_first`

 The second step of the proof of part (b), the choice of the parameter: it gives the first inequality of (b), here as
|x₁x₃|² + |x₂x₄|² ≤ |x₁x₂|² + |x₃x₄|² + 2|x₂x₃||x₁x₄|. 

### `lem_toolkit_b`

 **Paper: Lemma lem:toolkit (b).** "|xv|² + |yu|² ≤ |xu|² + |yv|² + 2|xy||uv|; in particular the squared diagonals of a
quadrangle add up to at most its squared sides, and if there is equality, opposite sides are equal." 

### `lem_toolkit_c_contract`

 The second half of part (c) with weights: (∑ w_i)|bb′| ≤ ∑ w_i|x_ix′_i|. "Adding the inequality of (c) for (b,x) at b′
and for (b′,x′) at b, and applying (b) to every b, b′, x_i, x′_i". 

### `lem_toolkit_c`

 **Paper: Lemma lem:toolkit (c).** "Points x₁, …, x_n, n ≥ 1, have a barycenter b, the minimizer of y ↦ ∑|yx_i|², with
∑|yx_i|² ≥ n|yb|² + ∑|bx_i|² for all y; if b′ is that of x′₁, …, x′_n, then n|bb′| ≤ ∑|x_ix′_i|." Here a barycenter is a
point with the displayed inequality; by lem_toolkit_c_minimizer this is the same as being the minimizer, and there is exactly
one. 

### `lem_toolkit_c_minimizer`

 Part (c): the barycenter is "the minimizer of y ↦ ∑|yx_i|²". For n ≥ 1 there is exactly one minimizer, and a point is the
minimizer if and only if it satisfies the inequality of (c), by which lem_toolkit_c describes the barycenter. 

### `lem_toolkit_d`

 **Paper: Lemma lem:toolkit (d).** "A nonempty closed convex F has nearest points Py, with |yq|² ≥ |yPy|² + |Py,q|² for
q ∈ F." A set is convex if it contains the midpoints of its points. 

### `lem_toolkit_e_general`

 Part (e) for factors that may differ. 

### `lem_toolkit_e`

 **Paper: Lemma lem:toolkit (e).** "Finite L² products of copies of Y are CAT(0)." 

 Part (f). The letters are those of the paper: |xy| = |uv| = δ, |xu| = |yv| = h, a is the point at s on [x,u] and b the
point at t on [y,v]. The steps before the last one ask only that the squared diagonals add up to at least 2h² + 2δ² (a flat
parallelogram). The form Φ(p,p′;r,r′) = |pr′|² + |p′r|² − |pr|² − |p′r′|² is at most 2|pp′||rr′| by (b), and it is additive when
[p,p′] and [r,r′] are cut; so equality for the whole is inherited by the parts. 

### `lem_toolkit_f_form`

 Φ(p,p′;r,r′) ≤ 2|pp′||rr′|, by part (b). 

### `lem_toolkit_f_parts`

 The form is additive, Φ(x,u;y,v) = Φ(x,a;y,b) + Φ(x,a;b,v) + Φ(a,u;y,b) + Φ(a,u;b,v), and the four bounds of
lem_toolkit_f_form add up to 2h², which is at most Φ(x,u;y,v) by hypothesis. So all four are equalities; the first one says
|xb|² + |ay|² − δ² − |ab|² = 2sth². 

### `lem_toolkit_f_same`

 The case s = t: then |ab| = δ, and |xb|² and |ay|² have the values that the inequality of (a) allows at most. 

### `lem_toolkit_f_parallelogram`

 The values of |xb|² and |ay|² from lem_toolkit_f_same, inserted into lem_toolkit_f_parts: the formula for |ab|², still in
terms of the two diagonals. 

### `lem_toolkit_f_isPt`

 Part (f), with a ∈ [x,u] and b ∈ [y,v] given by the inequality of (a) (Cat.IsPt), and with lower bounds for the diagonals. 

### `lem_toolkit_f`

 **Paper: Lemma lem:toolkit (f).** "Flat rectangles: if |xy| = |uv| = δ, |xu| = |yv| = h and both diagonals have squared
length δ² + h², and a ∈ [x,u], b ∈ [y,v] have |xa| = sh, |yb| = th, then |ab|² = δ² + h²(s−t)²." 

### `lem_toolkit`

 **Paper: Lemma lem:toolkit.** "Let Y be CAT(0). (a) For x, v and t ∈ [0,1] exactly one point γ(t) has distances t|xv|,
(1−t)|xv| from them, and |zγ(t)|² ≤ (1−t)|zx|² + t|zv|² − t(1−t)|xv|². (b) |xv|² + |yu|² ≤ |xu|² + |yv|² + 2|xy||uv|; in
particular the squared diagonals of a quadrangle add up to at most its squared sides, and if there is equality, opposite sides
are equal. (c) Points x₁, …, x_n, n ≥ 1, have a barycenter b, the minimizer of y ↦ ∑|yx_i|², with
∑|yx_i|² ≥ n|yb|² + ∑|bx_i|² for all y; if b′ is that of x′₁, …, x′_n, then n|bb′| ≤ ∑|x_ix′_i|. (d) A nonempty closed
convex F has nearest points Py, with |yq|² ≥ |yPy|² + |Py,q|² for q ∈ F. (e) Finite L² products of copies of Y are CAT(0).
(f) Flat rectangles: if |xy| = |uv| = δ, |xu| = |yv| = h and both diagonals have squared length δ² + h², and a ∈ [x,u],
b ∈ [y,v] have |xa| = sh, |yb| = th, then |ab|² = δ² + h²(s−t)²." In (c) a barycenter is a point with the displayed
inequality; by lem_toolkit_c_minimizer this is the same as being the minimizer, and there is exactly one. 
