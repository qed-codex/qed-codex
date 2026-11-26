---
{
  "module": "Paper/Convex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Convex.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Convex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "The main theorem": sums with few terms and the price of a set


### `lem_few`

 **Paper: Lemma lem:few.** "Let P ⊆ V, let t be a tensor on P and T_1, …, T_J tensors on V, and suppose that
t = ∑_j ⟨f_j|T_j⟩, where each f_j consists of one functional at every party outside P. Then φ(t) ≤ J^g(P) max_j φ(T_j)
for every spectral point on V." (A tensor on P is one on V with legs of size at most one outside P.) 

 The steps of the proof of Lemma lem:convex: the new parties are placed at random by Proposition prop:extend, and
Theorem thm:cn bounds how far they are from the midpoints. 

### `exists_mix_spec_keep`

 Let σ l, with weights θ l ≥ 0 of sum 1, map new parties Q to the
parties P. A spectral point F over P has an extension F' to P ⊕ Q that is, at every tensor, at most the weighted geometric mean of
the values of F at the tensors with the legs moved by σ l. It has the same distances on P and the same value at a given
tensor C over P. 

### `le_mean_of_two_rpow_le`

 Exponents: a power of two below the geometric mean of two powers of two. 

### `exists_mix_hexp`

 Let a, b, m map A to the parties V. A spectral point F over V has an extension
F' with a new party for every element of A, placed half at a and half at b: distances from new parties and the exponent of the
unit tensor on the new parties are at most the means of the two values for F. The distances on V and the exponent of the unit
tensor at m do not change. 

### `sq_dist_midpoint_le`

 Let v be a midpoint of x and y for a price w, and let z have the distance at most
w(x, y)/2 + δ from x and from y. Then w(z, v)² ≤ w(x, y) δ + δ². 

### `hexp_le_mean_add`

 Let F be a spectral point over V, c ≥ 0 a scale, and
a, b, m maps from A to V such that, in the metric c·d_F, every m v is a midpoint of a v and b v up to δ. Then the scaled exponent
of the unit tensor at m is at most the mean of those at a and at b, up to the sum of the numbers √(c d_F(a v, b v) δ + δ²). 

### `hexp_convex`

 Let w be a function on the pairs of a finite set V (the distances of a
placement of V in a metric space), and A a finite set. For every ε > 0 there is a δ > 0 as follows. Let F be a spectral point over
V and c ≥ 0 a scale such that c·d_F differs from w by less than δ. Let a, b, m map A to V, every m v being a midpoint of a v and
b v for w. Then the scaled exponent of the unit tensor at m is at most the mean of those at a and at b, plus ε. 

### `lem_convex`

 **Paper: Lemma lem:convex.** "Let V ⊆ ℝⁿ be finite, and let a, b, m : I → V be such that every
m(i) is the midpoint of a(i) and b(i). For every ε > 0 there is δ > 0 such that for every spectral point φ on V and
c ≥ 0 with |c·d(x,y) − ‖x−y‖| < δ on V, c·g(m) ≤ ½c·g(a) + ½c·g(b) + ε." 

### `cubeAlpha`

 The maps α_χ of the proof of Proposition prop:cube: at level j the centre ±½e_i (i = d, the sign s) goes to itself
if i is among the first j coordinates, and to ±½χ_i(0, …, 0, χ), with j zeros, if not. (Here u stands for the point
½u.) 

### `cubeAlpha_zero`

 "At level 0 the image is contained in a main diagonal." 

### `cubeAlpha_top`

 "At level k it is P." 

### `cubeAlpha_midpoint`

 "For j ≥ 1 the map α_χ is the pointwise midpoint of the two maps α_(±1,χ) of level j − 1; compare the three cases
i < j, i = j, i > j." 

### `prop_cube`

 **Paper: Proposition prop:cube.** "In the flat case let V ⊆ ℝᵏ be finite, P ⊆ V ∩ {±½e₁, …, ±½e_k} nonempty and
ε > 0. There are a spectral point φ on V and c ≥ 0 with |c·d(x,y) − ‖x−y‖| < ε on V and c·g(P) ≤ √k + ε." 
