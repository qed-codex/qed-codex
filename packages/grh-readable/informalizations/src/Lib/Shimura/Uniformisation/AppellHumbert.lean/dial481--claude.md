---
{
  "module": "src/Lib/Shimura/Uniformisation/AppellHumbert.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/AppellHumbert.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/AppellHumbert.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Existence in Appell–Humbert: projective embeddings are given by theta functions

The existence half of the Appell–Humbert theorem, for a projective embedding N of a uniformised
group A(ℂ) = V/L whose class satisfies the parallelogram law.

* `New.Uniformisation.appell_humbert`: the coordinates of N are theta functions for some
  Appell–Humbert data (L, B, χ) with positive Riemann form.
* `New.exists_analyticAt_double_eq`, `New.exists_extension_double`, `New.induction_on_double`: the
  doubling equation near 0, and its continuation to the whole space by halving.

Idea: the parallelogram law gives a frame on A × A, and its values define a function c. After
multiplying c by exp q(z, z) for a suitable quadratic form q, the doubling equation
σ(2z) = σ(z)⁴c(z) is solved near 0 and continued to V by halving. Then σ trivialises the pullback of
N.

`New.Uniformisation` A V is a surjective homomorphism e = `u.expMap` : V → A(ℂ), holomorphic and
immersive, with kernel the lattice L = `u.lattice`. `New.HasThetaCoords` says that θ(z) gives
homogeneous coordinates of e(z), each θ_i a theta function of type (B, χ): entire, with
θ_i(z + l) = χ(l)·exp(B l z + B l l / 2)·θ_i(z) for l in L.

Notions from other files:
* `New.atGeneric`: For a family s of sections of A over Spec O, O a valuation ring of ℂ, the complex
  point of A given by s(z) at the generic point.
* `New.LineBundle.IsHomogeneousCoords`: v is a vector of homogeneous coordinates of the point t for
  L: t lands in U_j exactly when v_j is a unit, and then g_jk(t) = v_k/v_j.
* `New.IsAppellHumbert`: Re B is symmetric, and on L one has |χ| = 1 and χ(l + m) = χ(l)χ(m)·exp(πi
  E(m, l)), E the Riemann form of B.
* `New.IsPosRiemann`: The Riemann form E of B is positive: E(u, iu) > 0 for every u ≠ 0.
* `New.Pic.ParallelogramLaw`: The parallelogram law for a class c in Pic A:
  (x+y)^*c + (x−y)^*c + 2·0^*c = 2(x^*c + y^*c) in Pic T for all T-points x, y of A and all
  S-schemes T.

## Relation to the literature

Known result: Appell–Humbert theorem, a step in the complex uniformisation of PEL abelian varieties.
For a given uniformisation, this file proves the existence half, for a very ample class obeying the
parallelogram law. Source: J. S. Milne, Introduction to Shimura Varieties (2005/2017), Theorem 8.17
and Lemma 5.12; R. Kottwitz, Points on some Shimura varieties over finite fields, J. AMS 5 (1992)
§8; G. Shimura, On analytic families of polarized abelian varieties and automorphic functions, Ann.
Math. 78 (1963); A. Borel, Some finiteness properties of adele groups over number fields, Publ. IHES
16 (1963); D. Mumford, Abelian Varieties §§1–2; L. Breen, Fonctions thêta et théorème du cube, LNM
980 (1983).


### `New.exists_analyticAt_double_eq`

 For `f` analytic at `0`, the equation `g (2z) = 4 g z + f z` has a solution analytic at `0`, up
to a quadratic form. 

### `New.floor_norm_half_div_lt`

 For `r > 0` and `‖z‖ ≥ r`, halving `z` lowers `⌊‖z‖ / r⌋₊`. 

### `New.induction_on_double`

 Induction by doubling: a property that holds on the ball of radius `r > 0` around `0` and
passes from `z` to `z + z` holds on the whole space. 

### `New.exists_extension_double`

 A solution of `σ (2z) = σ z ^ 4 * c z` on a ball around `0` extends to the whole space. 

### `New.exists_analyticAt_mul_double_eq`

 Let `Φ z` have no zero near `z`, with `Φ 0 / Φ z` analytic at `z` and `Φ 0 0 = 1`. Let `c`
have no zero, with `c 0 = 1` and `x ↦ c x * Φ (2a) (2x) / Φ a x ^ 4` analytic at `a`.
Then the doubling equation `σ (2z) = σ z ^ 4 * exp (q z z) * c z` holds for some bilinear form `q`
and some `σ` without zero such that `σ * Φ z` is analytic at `z`. 

### `New.exists_linear_logDeriv_of_periodic`

 Let `W` be entire on `V × V` without zero, and let `y ↦ W (2x, 2y) / W (x, y) ^ 4` be periodic
for the lattice `L`. Then the logarithmic derivative of `W` in the second variable is linear. 

### `New.exists_const_logDeriv`

 Let `W` have no zero and a linear logarithmic derivative `T` in the second variable. A function
`g` without zero, differentiable at `0`, with
`g (x + y) * g (x - y) * W (l + x, y) = g x ^ 2 * W (x, y)` has constant logarithmic derivative. 

### `New.isAppellHumbert_of_double_eq`

 Let `σ` have no zero, satisfy `σ (2l) = σ l ^ 4 * exp (q l l)` on `L` for a bilinear form `q`,
and have the factor of automorphy `exp (B l z) * σ l / σ 0`, with `Re B` symmetric. Then `B` and
`l ↦ σ l / σ 0 / exp (B l l / 2)` are Appell–Humbert data. 

### `New.Uniformisation.isPosRiemann_of_hasThetaCoords`

 If theta functions of type (B, χ) are homogeneous coordinates of a projective embedding of a
uniformised group, then the Riemann form of B is positive. 

### `New.exists_isAppellHumbert_of_analyticAt`

 Let `e : V → G` be additive and zero on the lattice `L`. Let `Φ x x = 1`, with `Φ (e z) ∘ e` not
zero near `z` and `(Φ (e 0) / Φ (e z)) ∘ e` analytic at `z`. Let `C` have no zero, with `C 0 0 = 1`,
and let `C (e x) (e y)`, times `Φ` at `x - y` and `x + y` over `Φ²` at `x` and `y`, be analytic at
each `(a, b)`. Then some `σ` without zero, with `σ * Φ (e z) ∘ e` analytic at `z`, has a factor
of automorphy given by Appell–Humbert data. 

### `New.Uniformisation.appell_humbert`

 The existence half of the Appell–Humbert theorem. Let e : V → A(ℂ) be a uniformisation with
kernel L, and N a linear system that embeds A, whose class satisfies the parallelogram law
`New.Pic.ParallelogramLaw`. Then there are Appell–Humbert data (L, B, χ) with positive Riemann form
and theta functions θ_i of type (B, χ) such that θ(z) is a vector of homogeneous coordinates of e(z)
for N, for all z in V. 
