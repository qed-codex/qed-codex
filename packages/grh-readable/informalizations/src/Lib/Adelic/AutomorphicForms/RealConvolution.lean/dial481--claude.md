---
{
  "module": "src/Lib/Adelic/AutomorphicForms/RealConvolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/RealConvolution.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/RealConvolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Convolution over real points, cusp kernels, the Petersson product and Poincaré series

Let G = G_∞ × G_f be the adelic unitary group, and let R(α)F(g) = ∫ α(x) F(gx) dx over G_∞ be right
convolution over the real points (`New.realConv`). For integrable α, R(α) preserves bounded
automorphic functions, and convolving with an idempotent kernel e produces forms of type e. The
product of discrete series kernels over the infinite places is a cusp kernel under a gap condition.
For the Petersson product, right translation is unitary, and a cusp kernel e projects every real
translate of a form of type e to a multiple of it. A bounded Poincaré series, projected term by
term, is a form.

## Main definitions and results

* `New.continuous_realConv`, `New.Space.isAutomorphic_realConv`: for integrable α, R(α)F is
  continuous when F is bounded, measurable and has an open level, and it is automorphic and bounded
  when F is also invariant under the rational points.
* `New.Space.exists_form_eq_realConv`: convolving with an idempotent kernel gives a form of type e.
* `New.IsCuspKernel`: minimal idempotents e on G_∞ with a moment of order B + 1 and decay of order
  B, and with α ∗ e = e for some continuous compactly supported α.
* `New.isCuspKernel_typeKernel`: the product kernel `New.typeKernel` over the infinite places is
  such a kernel when the parameters satisfy a gap condition.
* `New.Space.IsForm.realConv_translate`, `New.Space.IsForm.petersson_real_translate`: `e` projects
  each real translate of a form to a multiple of the form.
* `New.Space.exists_form_eq_tsum_of_fixesLeft`: if an absolutely bounded sum of measurable functions
  is left invariant under `V.Γ` and has level `K`, projecting each term by R(e) gives a form of type
  `e`; `New.Space.exists_form_eq_tsum` is the case of a sum over `V.Γ` of translates of one
  function. `New.levelSpace (V.formRep e) K` is the space of forms of type `e` fixed by the open
  subgroup `K` of the finite points.

Notions from other files:
* `New.Space.IsAutomorphic`: continuous, left invariant under the rational points `V.Γ`, and right
  invariant under some open subgroup of G_f.
* `New.HCParam.dsKernel`: for a parameter l = 2λ, the function e_λ on U(diag s), the formal degree
  times the conjugate of the discrete series coefficient c_λ (`New.HCParam.dsCoeff`).
* `New.IsIdempotentKernel` (part of `New.IsCuspKernel`): e is continuous and integrable, e(g⁻¹) is
  the conjugate of e(g), e(1) ≠ 0, and ∫ e(z)e(x⁻¹z⁻¹y) dz = e(x⁻¹)e(y)/e(1).
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.Space.quotMeasure`: the measure on `G` that computes integrals over `Γ \ G`.

## Relation to the literature

Known result: convolution over real points, cusp kernels, the Petersson product and Poincaré series
projected to forms, from the theory of cusp forms. For sources see
`Lib.Adelic.AutomorphicForms.Cuspidality`.


 ## Convolution over the real points; cusp kernels 

### `bumpProduct`

 For a bump function α_w on U(diag s) at each infinite place w, the product x ↦ ∏_w α_w(x_w⁻¹),
as a continuous compactly supported function on G_∞. 

### `le_prod_opNorm`

 For `n` nonempty and `g` in G_∞, the product over the infinite places of the operator norms
‖g_w‖ is at least 1 and at least each of its factors. 

### `IsCuspKernel`

 A cusp kernel of order B on G_∞: a minimal idempotent e (`New.IsIdempotentKernel`) such that,
with ‖x‖ = ∏_w ‖x_w‖ for the operator norms, (a) ‖x‖^(B+1) e(x) is integrable, (b) α ∗ e = e for
some continuous compactly supported α, and (c) ‖x‖^B e(x) is bounded. 

### `IsCuspKernel.integrable_moment`

 Moment: |e(x)| ‖x‖ ^ (B + 1) is integrable, where ‖x‖ is the product over the infinite places
  of the operator norms. 

### `IsCuspKernel.exists_bump`

 Some continuous compactly supported `α` reproduces `e` by convolution: α ∗ e = e. 

### `IsCuspKernel.decay`

 Decay of order `B`: |e(x)| ‖x‖ ^ B is bounded. 

### `IsCuspKernel.star`

 The complex conjugate of a cusp kernel of order `B` is a cusp kernel of order `B`. 

### `isIdempotentKernel_typeKernel`

 For n nonempty, suppose that at every infinite place w the integer vector l_w = 2λ_w, read by
`toHCParam` as a doubled parameter for the signs s, is a parameter with gap 500|n|³ + B
(`HasLargeGap B`). Then `New.typeKernel` l s, the product over the infinite places of the discrete
series kernels e_(l_w), is an idempotent kernel on G_∞. That is, it is continuous and integrable,
e(g⁻¹) = conj(e(g)), e(1) ≠ 0, and ∫ e(z) e(x⁻¹z⁻¹y) dz = e(x⁻¹) e(y) / e(1). 

### `isCuspKernel_typeKernel`

 Let E be a CM field, n nonempty and s a family of signs. Suppose every l_w = 2λ_w is a
Harish-Chandra parameter whose entries λ_i, λ_j of different signs s are at least 500|n|³ + B apart.
Then `New.typeKernel` l s, the product over the infinite places of the discrete series kernels
e_(l_w), is a cusp kernel of order B: a minimal idempotent e on G_∞ such that, with ‖x‖ = ∏_w ‖x_w‖
the product of operator norms, ‖x‖^(B+1) e(x) is integrable, α ∗ e = e for some continuous compactly
supported α, and ‖x‖^B e(x) is bounded. 

### `Space.mem_levelSpace_formRep_iff`

 A form of type `α` (a bounded automorphic function fixed by `realConv α` when α is integrable)
lies in `levelSpace (V.formRep α) J`, the vectors fixed by the subgroup `J` of G_f, if and only if
it has level `J`, that is, is invariant under right translation by `J`. 

### `hasLevel_realConv`

 If `F` is right invariant under the open subgroup `K` of G_f, then so is its real convolution
R(α)F, since real and finite points commute. 

### `norm_realConv_mul_sub_le`

 The oscillation of an average is bounded by that of the kernel in L¹. Let α be integrable on
G_∞, F bounded and measurable on G, u a real point, real points sitting in G as x ↦ (x, 1), and
R(α)F(g) = ∫_{G_∞} α(x)F(gx) dx (`realConv`). If C ≥ 0 and |F(gx)| ≤ C for all real x with
α(u⁻¹x) ≠ α(x), then |R(α)F(gu) − R(α)F(g)| ≤ ‖α(u⁻¹ ·) − α‖₁ C. 

### `tendsto_integral_norm_translate_sub`

 Translation is continuous on L¹: for α integrable on G_∞, ‖α(u⁻¹ ·) − α‖₁ tends to 0 as the
real point u tends to 1. 

### `eventually_norm_realConv_sub_le`

 Uniform continuity of averages. Let α be integrable on G_∞, K an open subgroup of G_f and ε > 0.
Let z be close enough to 1, with real part z_∞. If (a) F is measurable, bounded and right
K-invariant and (b) |F(gx)| ≤ C for all real x with α(z_∞⁻¹x) ≠ α(x), then
|R(α)F(gz) − R(α)F(g)| ≤ ε|C|. The neighbourhood of 1 does not depend on F, C or g. 

### `integral_mul_realConv`

 Fubini for right convolution: for c, α integrable, j measurable and F bounded measurable on
G, ∫ c(z) R(α)F(j z) dν(z) = ∫_{G_∞} α(x) ∫ c(z) F(j(z)x) dν(z) dx, with ν s-finite. 

### `realConv_realConv`

 Averaging twice is averaging against a convolution: for F measurable and bounded, α and p
integrable and a in G_∞, applying R(p), then right translation by a, then R(α) is R of the function
y ↦ ∫ α(x) p((xa)⁻¹y) dx. Here R = `realConv` is right convolution over G_∞. 

### `IsCuspKernel.exists_realConv_realConv_eq`

 For a cusp kernel e (an integrable idempotent kernel on G_∞ with decay, `IsCuspKernel`) there is
a continuous compactly supported α on G_∞ with α ∗ e = e, and so R(α)R(e)F = R(e)F for every bounded
measurable F on G. Here R(α)F(g) = ∫_{G_∞} α(x) F(gx) dx is `realConv`. 

### `IsIdempotentKernel.realConv_translate_realConv`

 Rank one formula for operators. Let α be an idempotent kernel on G_∞ (continuous, integrable,
α(g⁻¹) = conj(α(g)), α(1) ≠ 0, and ∫ α(z) α(x⁻¹z⁻¹y) dz = α(x⁻¹) α(y) / α(1)), x a real point, and F
on G bounded and measurable. Then applying R(α)F(g) = ∫_{G_∞} α(z) F(gz) dz, then right translation
by (x, 1), then R(α) again gives conj(α(x))/α(1) times R(α)F. For the kernel e_λ of a discrete
series the factor is the coefficient c_λ(x). 

### `Space.petersson_realConv_right`

 For bounded measurable `F`, `F'` and integrable `α`, the convolution in the right argument may
be taken out of the Petersson product `V.petersson`, the integral of `conj F' * F` over `Γ \ G`. 

### `continuous_realConv`

 If F on G is measurable, bounded and right invariant under an open subgroup of G_f, and α is
integrable on G_∞, then R(α)F is continuous. 

### `Space.isAutomorphic_realConv`

 If F on G is measurable, bounded, left Γ-invariant and right invariant under an open
subgroup of G_f, and α is integrable on G_∞, then R(α)F is automorphic (continuous,
Γ-invariant, with a level) and bounded. 

### `Space.exists_form_eq_realConv`

 Let α be an idempotent kernel on G_∞ (`New.IsIdempotentKernel`: continuous, integrable,
α(g⁻¹) = conj(α(g)), α(1) ≠ 0, and ∫ α(z) α(x⁻¹z⁻¹y) dz = α(x⁻¹) α(y) / α(1)). Let K be an open
subgroup of G_f, and F on G bounded, measurable, left invariant under the subgroup `V.Γ` and right
invariant under K. Then R(α)F(g) = ∫_{G_∞} α(x) F(gx) dx is a form of type α (automorphic, bounded
and fixed by R(α)) fixed by right translation by K, that is an element of
`New.levelSpace (V.formRep α) K`. 


## The Petersson product under translation and convolution

The product `New.Space.petersson F F'` is the integral of `conj F * F'` over `Γ \ G`. A form of type
`e` (`New.Space.IsForm`) is a bounded automorphic function fixed by `realConv e` when `e` is
integrable.

In `New.Space.IsForm.realConv_translate`, `New.Space.IsForm.petersson_real_translate` and
`New.Space.IsForm.petersson_realConv_realConv`, `e` is taken to be a cusp kernel
(`New.IsCuspKernel`), though of its properties only those of an idempotent kernel are used.


 ### Translation 

### `integral_comp_mul_right`

 For a continuous left `V.Γ`-invariant function F on G and x in G, the right translate
g ↦ F(gx) has the same integral over `Γ \ G` as F, and it is integrable if and only if F is. 

### `IsAutomorphic.petersson_comp_mul_right`

 For automorphic functions `F`, `F'` and the Petersson product, right translation by `x⁻¹` is
adjoint to right translation by `x`. 

### `inner_formRep`

 The finite points act on forms of type `e` by isometries of the Petersson product. 

 ### Forms of type `e` 

### `petersson_realConv_comm`

 Right convolution with an idempotent kernel `e` is self-adjoint for the Petersson product on
bounded automorphic functions, because `e y⁻¹ = conj (e y)`. 

### `IsForm.petersson_realConv`

 Let `e` be an idempotent kernel, `F` a form of type `e` and `T` a bounded automorphic function.
Replacing `T` by its right convolution `realConv e T` does not change the Petersson product of `F`
and `T`: convolution by `e` is self-adjoint and fixes `F`. 

### `IsForm.conj`

 For a hermitian space `V` over the CM field `E` with signs `s`, let `F` be a function on the
unitary group `G E s` that is a form of type `e`, where `e` is a function on the archimedean group
`GInf E s`. Being a form of type `e` means `F` is automorphic, bounded, and fixed by right
convolution with `e` when `e` is integrable. Then the complex conjugate `star F` is a form of type
`star e`. 

### `IsForm.realConv_translate`

 Rank one formula. Let `e` be a cusp kernel (a minimal idempotent on G_∞ with the decay
conditions of `IsCuspKernel`), `F` a form of type `e` (bounded automorphic on G, fixed by right
convolution with `e`), and `x` a real point. Convolution by `e` sends the translate `F (· * (x, 1))`
to `conj (e x) / e 1` times `F`. The left side is the value at `g` of `realConv e` applied to that
translate. For the kernel e_λ of a discrete series the factor is the coefficient c_λ(x). 

### `IsForm.petersson_real_translate`

 For a cusp kernel `e`, forms `F`, `F'` of type `e` and a real point `x`, the Petersson product
of `F` with the translate `F' (· * (x, 1))` is `conj (e x) / e 1` times the product of `F` and
`F'`. 

### `IsForm.petersson_realConv_realConv`

 For a cusp kernel `e`, forms `F`, `F'` of type `e` and integrable `α`, `β` on the real points,
the product of `realConv α F` and `realConv β F'` is the product of `F` and `F'` times
∫∫ conj(α(x)) β(y) conj(e(x⁻¹y))/e(1) dy dx. 

 ## Poincaré series projected to forms 

### `New.Space.exists_form_eq_tsum_of_fixesLeft`

 Let `W i` be countably many measurable functions on `G` with `∑ i, ‖W i‖` bounded, whose sum is
left invariant under the rational points `V.Γ` and right invariant under the open subgroup `K` of
the finite points. Then the sum of the right convolutions of the `W i` with the idempotent kernel
`e` is an element of `levelSpace (V.formRep e) K`, that is a form of type `e` fixed by `K`. 

### `New.Space.exists_form_eq_tsum`

 **Poincaré series.** Let the sum of countably many measurable `W i`, with `∑ i, ‖W i‖` bounded,
be the sum over `V.Γ` of the left translates of one function `c` that is right invariant under the
open subgroup `K` of the finite points. Then the sum of the right convolutions of the `W i` with
the idempotent kernel `e` is a form of type `e` fixed by `K`. 
