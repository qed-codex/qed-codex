---
{
  "module": "src/Lib/Adelic/AutomorphicForms/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/Basic.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Automorphic forms on adelic unitary groups, the Petersson product and rapid decay

This file studies functions on the adelic unitary group G = G_∞ × G_f of a hermitian space V over E
with signs s. Here Γ = `V.Γ` is its group of rational points, and `V.quotMeasure` is the measure for
integrals over Γ\G. The forms of type e (see `New.Space.IsForm` below) make up an inner product
space under the Petersson product and carry an action of G_f. The height `New.Space.height` is the
inverse of the first minimum `New.Space.firstMinimum`, cut off at `1`. Moderate growth and rapid
decay are measured against the height, and the rapidly decaying automorphic functions form a
subrepresentation. When Γ is cocompact, in particular when all signs of V are equal, every
automorphic function has rapid decay.

## Main definitions and results

* `New.Space.IsAutomorphic`: continuous, left Γ-invariant functions with a level.
* `New.Space.IsForm`: bounded automorphic functions that are fixed by convolution with a kernel e if
  e is integrable (for e not integrable this condition is empty). A form is bounded and measurable
  (`IsBoundedMeasurable`, which follows from bounded and continuous), hence lies in L²(Γ\G).
* `New.Space.Form`: the space of these forms, an inner product space under the Petersson product
  `New.Space.petersson`, with the action `New.Space.formRep` of G_f.
* `New.Space.rapidFunctions`: the automorphic functions of rapid decay form a subrepresentation.
* `New.Space.isRapid_of_isCocompact`: continuous Γ-invariant functions are rapid when Γ is
  cocompact.
* `New.Space.IsAutomorphic.mem_rapidFunctions`: automorphic functions are rapid when all signs are
  equal.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.Space.Γ`: for a space (J, x), the subgroup x^{-1} U(J)(E) x of G, the image of the rational
  unitary group.
* `New.GInf`: the archimedean unitary group G_∞ for signs s: one copy of the complex unitary group
  U(diag s) for each infinite place of E.
* `New.Space.IsModerate`, `New.Space.IsRapid`: |F| ≤ C·ht^B for some C and B; |F|·ht^B is bounded
  for every B.

## Relation to the literature

Known result: automorphic forms on unitary groups and their rapid decay. Cusp forms are treated in
`Lib.Adelic.AutomorphicForms.Cuspidality`.



## Automorphic functions, automorphic forms and the Petersson product

* `New.typeKernel`, `New.realConv`: the product kernel on G_∞ of given parameters, and right
  convolution over G_∞.
* `New.ThetaKernel`: the data of a kernel on the product of two groups that is invariant under the
  rational points; it is used for theta lifts of forms.


### `typeKernel`

 The function e_λ(x) = ∏_w e_{λ_w}(x_w) on G_∞, for a family of doubled parameters l_w = 2λ_w. It
is the product over the infinite places of the functions `dsKernel` on U(diag s), each the formal
degree times the conjugate of the discrete series coefficient. 

### `realConv`

 Right convolution over the real points: R(k)F(g) = ∫_{G_∞} k(x) F(gx) dx, for k on G_∞ and F
on G. 

### `finRightRep`

 The representation of G_f on complex functions on G by right translation. 

### `ThetaKernel`

 A theta kernel (g, h, φ) ↦ θ(ω(g, h) φ) for the spaces S and T: an action ω of the product of
their groups on a normed space X and a functional θ on X, such that ω is jointly continuous and the
kernel is left invariant under Γ_S × Γ_T. 

### `ThetaKernel.ω`

 The action of the product of the groups of S and T on X by continuous linear maps. 

### `ThetaKernel.θ`

 The linear functional θ on X. 

### `ThetaKernel.continuous`

 The action `(p, φ) ↦ ω p φ` is jointly continuous. 

### `ThetaKernel.rat_mul`

 The kernel is invariant under left multiplication by rational points of both groups. 

### `IsAutomorphic`

 F on G is automorphic: continuous, left Γ-invariant, and right invariant under some open
subgroup of G_f. 

### `IsAutomorphic.continuous`

 `F` is continuous. 

### `IsAutomorphic.rat_mul`

 `F` is invariant under left multiplication by rational points. 

### `IsAutomorphic.exists_level`

 `F` has a level: it is right invariant under an open subgroup of the finite points. 

### `petersson`

 The Petersson product ⟨F, F'⟩ = ∫_{Γ\G} conj(F) F', taken with the measure
`New.Space.quotMeasure`. 

### `IsForm`

 F is a form of type e, for a function e on G_∞: F is automorphic, bounded, and fixed by right
convolution with e if e is integrable. For e not integrable the last condition is empty, so that
every bounded automorphic function is then a form of type e. The forms of parameter λ are those of
type e_λ = `New.typeKernel l s`, with l = 2λ. 

### `IsForm.bounded`

 `F` is bounded. 

### `IsForm.realConv_eq`

 If `e` is integrable, right convolution with `e` over the real points fixes `F`. 

### `IsAutomorphic.map₂`

 For automorphic functions F, F' and a function f of two complex variables that is jointly
continuous, the function g ↦ f(F(g), F'(g)) is automorphic. The continuity may be omitted when
`fun_prop` proves it. 

### `IsAutomorphic.comp_mul_right`

 A right translate g ↦ F(ga) of an automorphic function F by a point a of G is automorphic. 

### `IsAutomorphic.eq_zero_of_petersson_self`

 The Petersson product is definite: an automorphic function F that is square integrable on
Γ\G and has ⟨F, F⟩ = 0 vanishes everywhere. 

### `IsForm.comp_mul_right`

 The right translate g ↦ F(g·(1, a)) of a form F of type e by a finite point a is again a form
of type e. 

### `IsForm.smul_add_smul`

 A linear combination aF + bF' of two forms F, F' of type e (bounded automorphic functions on G
fixed by convolution with e if e is integrable) is a form of type e. 

### `formSubmodule`

 The forms of type e for V, as a submodule of the complex functions on G. 

### `Form`

 The complex vector space of forms of type e for V, namely the type of elements of
`New.Space.formSubmodule`. 

### `Form.toL2`

 The linear map that sends a form of type e to its class in L²(Γ\G), taken for the measure
`New.Space.quotMeasure`. 

### `Form.petersson_eq_inner_toL2`

 The Petersson product of two forms of type e is the inner product of their classes in
L²(Γ\G). 

### `peterssonCore`

 The positive definite inner product on forms of type e given by the Petersson product, the
integral of conj(F)·F' over Γ\G. Symmetry, positivity and sesquilinearity are those of the inner
product of L²(Γ\G); definiteness holds because forms are continuous. 

### `formRep`

 The representation of G_f on forms of type e by right translation. 


## Heights and rapidly decaying functions

* `New.Space.exists_height_le_mul`: the height changes by a bounded factor under rational points on
  the left and a compact set on the right.


 ### The height 

### `one_le_height`

 The height is at least 1, as the first minimum is cut off at 1. 

### `exists_height_le_mul`

 For compact K ⊆ G there is C ≥ 1 such that ht(k) ≤ C·ht(g) whenever g⁻¹γk ∈ K. Here γ runs over
the rational unitary group U(J)(E) of V, mapped into G by `New.Space.ratEmbed`, and ht is the
height of V, the inverse of the first minimum cut off at 1. 

### `exists_mul_height_pow_le`

 For a compact set K ⊆ G, a real C and a natural number B, the function g ↦ C·ht(g)^B is bounded
above on the set of g that a point of Γ moves into K. Here ht is the height of V, the inverse of
the first minimum cut off at 1. 

 ### Rapidly decaying functions 

### `IsRapid.mul`

 The product of a function M of moderate growth (|M| ≤ C·ht^b for some C and b) and a function F
of rapid decay (|F|·ht^B bounded for every B) has rapid decay. Here ht is the height of V. 

### `IsRapid.comp_mul_right`

 If F has rapid decay (|F|·ht^B is bounded for every B), then so has its right translate
g ↦ F(gx) by any point x of G. 

### `IsRapid.integrable`

 A continuous function of rapid decay is integrable for the measure `New.Space.quotMeasure` of
Γ\G. 

### `IsRapid.smul_add_smul`

 A linear combination aF + bF' of two functions of rapid decay (|F|·ht^B bounded for every B,
with ht the height of V) has rapid decay. 

### `rapidFunctions`

 The automorphic functions of rapid decay for `V`, as a subrepresentation of the functions on G
under right translation by G_f. 

### `star_mem_rapidFunctions`

 The complex conjugate of a rapidly decaying automorphic function is one as well. 

 ## Rapid decay on definite spaces 

### `isRapid_of_isCocompact`

 If the group Γ of rational points is cocompact, a continuous left Γ-invariant function F has
rapid decay: |F|·ht^B is bounded for every B, with ht the height of V. 

### `IsAutomorphic.mem_rapidFunctions`

 On a definite space (all signs `s i` are equal) every automorphic function F (continuous, left
Γ-invariant, with a level) has rapid decay (|F|·ht^B is bounded for every B), so it lies in
`rapidFunctions`. 
