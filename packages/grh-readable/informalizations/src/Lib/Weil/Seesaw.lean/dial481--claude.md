---
{
  "module": "src/Lib/Weil/Seesaw.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Seesaw.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Seesaw.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta lifts for families of characters over a real edge and the seesaw of periods

This file constructs theta lifts between two unitary groups for a whole family of characters at
once. For hermitian spaces `S`, `T` and characters `a`, `b` of the norm-one adeles,
`New.pairWeil S T a b` is the Weil representation of the pair. `New.modDatum` is a datum given by a
Fock vector at infinity and a function modulo `𝔪`, and a "type" is a kernel on the real points that
cuts out a space of forms.

## Main definitions and results

* `New.Exchange.modLift`, `New.Exchange.modTransposedLift`: the lift of forms from `S` to `T` and
  the transposed lift back.
* `New.Exchange.IsConjKernelPair`, `New.Exchange.IsEdgeFamily`: a pair of conjugate cuspidal types;
  a family of characters with common weights for which two such pairs and a polynomial form a real
  edge (`New.IsEdge`). `New.Exchange.isEdgeFamily_of_paramsCorrespond` produces edges from
  corresponding parameters.
* `New.Exchange.pairLift`, `New.Exchange.pairTransposedLift`, `New.Exchange.IsPairEdge`: lift,
  transposed lift and edge when the two characters of the pair are given separately. `IsPairEdge`
  has one type on each group and lets the two characters have different tame parts.
* `New.Exchange.IsEdgeFamily.exists_lift_eq_realConv`,
  `New.Exchange.IsEdgeFamily.petersson_lift_eq_mul_inner_modTransposedLift`: replacing the
  polynomial of the edge by another one changes the lift by right convolution with a continuous
  compactly supported function on the real points; the Petersson product of a form with this lift is
  a constant times that of its transposed lift. The function and the constant do not depend on the
  finite data.
* `New.Space.periodPairing`: the bilinear period `∫ M z * f z * y (j z * r)` of a form `f` on `S`
  and a form `y` on `T`, for a moderate weight with function `M` and map `j` and a real point `r`.
* `New.Exchange.seesaw_periods`: suppose the theta kernels of two pairs agree up to moderate weights
  on a spanning set of polynomials (`New.Exchange.IsSeesawMatched`). Then proportionality to a fixed
  vector passes from the periods of lifts (`New.Exchange.modLift`) to the periods of transposed
  lifts (`New.Exchange.modTransposedLift`).

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places (s the signs) and 1 at the finite places.
* `New.IsEdge`: a relation between kernels e, e' on the two real groups and a Fock vector Φ. The
  kernel e is a cusp kernel and the doubling zeta integral of Φ against ē is not zero. For a form of
  type e, the lift with Φ is a form of type e' if it has a level, and for a polynomial v the lift
  with v is the convolution of the lift with Φ by some α ∈ C_c. The same holds with the groups
  exchanged and the kernels ē', ē.
* `New.IsArrow`: the datum φ is an arrow e → e' for the theta kernel K if forms of type e on S are
  rapid and their lifts by φ are forms of type e' on T.
* `New.Space.Form`: `S.Form e` is the space of bounded automorphic functions on the group of `S`
  that right convolution with `e` fixes (when `e` is integrable).
* `New.modKernel`: the theta kernel of the datum `New.modDatum` made of the Fock vector of a
  polynomial and a function on matrices modulo `𝔪`. Along an edge the lift and the transposed lift
  integrate a form against this kernel, in the first and in the second variable.

## Relation to the literature

Known result: Seesaw identity for periods of theta lifts. Here the statement holds for two unitary
pairs whose kernels agree up to moderate factors for a spanning set of Fock polynomials. Both pairs
carry edge families (`IsEdgeFamily`), and the data are taken modulo an ideal. If finite sums of
periods of the lift are proportional to a fixed family of numbers at all real translates, then so
are those of the transposed lift. Source: S. Kudla, Seesaw dual reductive pairs, in Automorphic
forms of several variables (Katata 1983), Progr. Math. 46, Birkhäuser 1984, 244–268.

See also `Lib.Weil.Lift`.


### `kernelPair`

 The pair of kernels `New.typeKernel` (products of discrete series kernels over the infinite
places): the one of the parameter `l` at `false` and the one of `-l` at `true`
(see `New.negIf`). 

### `modLift`

 The theta lift of forms of type e on S to type e′ on T, for the characters `a n`, `a n'` and the
datum of the polynomial P and Ψ mod 𝔪. It is a chosen linear map (`formLift`) that equals the lift
integral whenever the lifts are forms of type e′. 

### `modTransposedLift`

 The transposed lift of forms of type e′ on T to forms of type e on S, for the same kernel and
datum as `New.Exchange.modLift`. No complex conjugation enters. 

### `pairWeil_modDatum_single`

 Let k, k' be integral finite points of the two unitary groups and x = k'⁻¹yk modulo 𝔪, where
`𝔪.reductionGL` is the reduction modulo 𝔪 (if the proof `hx` of this equation is omitted, it is
sought by `simp; rfl`). Let v be a real Fock vector and vac the vacuum outside 𝔪. For characters a,
b the representation `pairWeil` at (k, k') sends the datum v ⊗ 1_x ⊗ vac to a(det k') b(det k)⁻¹
(the value of `pairChar`) times the datum v ⊗ 1_y ⊗ vac. 

### `IsConjKernelPair`

 The two functions k(false), k(true) on G_∞ are complex conjugates of each other, and each
satisfies `New.IsCuspKernel` of order 0. 

### `IsEdgeFamily`

 A family of characters `a i` over one real edge. (a) `k` and `k'` are pairs of conjugate
cuspidal types (`New.Exchange.IsConjKernelPair`); (b) all `a i n` have one weight `γ` and all
`a i n'` one weight `γ'`, and for each `i` both have the same tame part `ψ i`, which may vary with
`i`; (c) for the real Weil representation of weights `γ`, `γ'`, the types `k d`, `k' d` and the Fock
vector of the polynomial `Φ` form an edge in the sense of `New.IsEdge`. 

### `isConjKernelPair_kernelPair`

 Let `n` be nonempty and `l` an integer parameter at each infinite place. If the Harish-Chandra
parameter `toHCParam s` of `negIf d l` (which is `-l` if `d` is true and `l` otherwise) has a large
gap (`HasLargeGap 0`) at every infinite place, the kernels of `l` and `-l` are cuspidal and
conjugate to each other. 

### `isEdgeFamily_of_paramsCorrespond`

 Suppose the parameters `negIf d l`, `negIf d l'` (that is `±l`, `±l'`, with the sign `-` for
`d = true`) correspond for the weights `γ`, `γ'` (`New.ParamsCorrespond`). Suppose the characters
`a i n` have the weight `γ`, the characters `a i n'` have the weight `γ'`, and both have the tame
part `ψ i`. Then the `a i` form an edge family: the types are the kernels of `±l`, `±l'`, and the
polynomial is the product over the infinite places of chosen joint harmonics. 

 ### Pairs with two separately given characters 

### `pairLift`

 The theta lift of forms of type `e` on `S` to forms of type `e'` on `T`, for characters
`a`, `b` (entering as a(det h) b(det g)⁻¹ for g on `S`, h on `T`) and the datum of the polynomial
`P` and the function `Ψ` modulo `𝔪`.
It is a chosen linear map (`formLift`) that equals the lift integral along an edge
(`New.Exchange.IsPairEdge.isArrow_lift`). 

### `pairTransposedLift`

 The transposed lift of forms of type `e'` on `T` to forms of type `e` on `S`, for the kernel
and the datum of `New.Exchange.pairLift`. No complex conjugation enters. It equals the integral
along an edge between the conjugate types (`New.Exchange.IsPairEdge.isArrow_swap`). 

### `IsPairEdge`

 Characters `a i`, `b i` over one real edge: each `a i` has weight `γ` and each `b i` has weight
`γ'`, with some tame parts that may depend on `i`, and the types `e`, `e'` with the Fock vector of
`P` form an edge (`New.IsEdge`) for the weights `γ`, `γ'`. 

### `isPairEdge_of_isJointHarmonic`

 Let the characters `a i` have weight `γ` and the `b i` weight `γ'`, with some tame parts. If at
each infinite place `w` the polynomial `Φ w` is a joint harmonic for the parameters `l'`, `-l` and
the weights `γ`, `-γ'` (`New.IsJointHarmonic`), then the product of the `Φ w`, each in the variables
of `w`, gives an edge (`New.Exchange.IsPairEdge`) between the types of `l` and `l'`. This is a
corollary of `New.isEdge_of_isJointHarmonic`. 

### `IsEdgeFamily.isPairEdge`

 An edge family (`New.Exchange.IsEdgeFamily`) of characters `c` with polynomial `P` is an edge
(`New.Exchange.IsPairEdge`) between `k d` and `k' d` for the characters that `c` attaches to the
index types `n`, `n'`. 

### `IsEdgeFamily.isPairEdge_star`

 An edge family of characters `c` with polynomial `P` is an edge between `star (k !d)` and
`star (k' !d)`, the conjugates of the opposite types, which equal `k d` and `k' d`. 

### `IsPairEdge.isCuspKernel`

 The source type `e` of an edge is a cusp kernel of order 0. 

### `IsPairEdge.isCuspKernel_star`

 The conjugate of the target type `e'` of an edge is a cusp kernel of order 0. 

### `IsPairEdge.isArrow`

 Along an edge, the datum of `P` and `Ψ` lifts forms of type `e` to forms of type `e'`, and its
transposed lift takes forms of the conjugate type of `e'` to the conjugate type of `e`. 

### `IsPairEdge.isArrow_lift`

 Along an edge, the datum of `P` and `Ψ` lifts forms of type `e` on `S` to forms of type `e'`
on `T`. 

### `IsPairEdge.isArrow_swap_star`

 Along an edge from `e` to `e'`, the transposed lift by the datum of `P` and `Ψ` takes forms of
the conjugate type of `e'` on `T` to forms of the conjugate type of `e` on `S`. 

### `IsPairEdge.isArrow_swap`

 Suppose the characters `a i`, `b i`, the conjugate types `star e`, `star e'` and the polynomial
`P` form an edge (`New.Exchange.IsPairEdge`). Let v_P be the Fock vector of `P`. Then for each `i`,
the datum v_P ⊗ Ψ ⊗ vac on Hom(S, T) (real part v_P, the lift of Ψ : matrices mod 𝔪 → ℂ at the
places dividing 𝔪, vacuum elsewhere) is an arrow e' → e for the swapped theta kernel of `S`, `T`,
`a i`, `b i`. That is, forms of type `e'` on the group of `T` are rapid, and their transposed lifts
are forms of type `e` on the group of `S`. 

### `IsPairEdge.exists_lift_eq_realConv`

 For an edge with polynomial `P` and any polynomial `Q` there is one continuous function `α` of
compact support on the real points of the target such that, for all finite data, the lift formed
with `Q` is the right convolution by `α` of the lift formed with `P`. 

### `exists_integral_realConv_mul_realConv`

 Real averages against `α` and `β` multiply the pairing of forms of conjugate cuspidal types by
one number. 

 ### Lifts along an edge family 

### `IsConjKernelPair.form_mem_rapidFunctions`

 A form of a type from a conjugate cuspidal pair decreases rapidly. 

### `IsEdgeFamily.isArrow_lift`

 Along an edge, the datum with the Fock vector of `P` at infinity and any finite part `Ψ` modulo
`𝔪` lifts forms of type `k d` on `S` to forms of type `k' d` on `T` (see `New.IsArrow`). 

### `IsEdgeFamily.isArrow_swap`

 Along an edge, the transposed lift by the datum of `P` and `Ψ` takes forms of the conjugate type
`k' (!d)` on `T` to forms of type `k (!d)` on `S` (see `New.IsArrow`). 

### `IsEdgeFamily.isArrow_modDatum`

 Along an edge, the datum of `P` and `Ψ` lifts forms of type `k d` on `S` to forms of type `k' d`
on `T`, and its transposed lift takes forms of type `k' (!d)` on `T` to forms of type `k (!d)` on
`S`. 

### `IsEdgeFamily.exists_lift_eq_realConv`

 For an edge with polynomial `P` and any polynomial `Q` there is one continuous compactly
supported function `α` on the real points of the target group such that, for all finite data, the
lift formed with `Q` is the right convolution by `α` of the lift formed with `P`. 

### `IsEdgeFamily.petersson_lift_eq_mul_inner_modTransposedLift`

 Let `a` be an edge family (`IsEdgeFamily a k k' d P`: characters `a i` over one real edge with
cuspidal types `k`, `k'`) and let `Q` be any polynomial. Then there is one `κ` that works for all
`i`, spaces `S`, `T`, modulus `𝔪`, functions `x` on residue matrices, and forms `y : S.Form (k !d)`,
`z : T.Form (k' !d)`. Take the Petersson product on `T` of `z` with the conjugate of the theta lift
of `star y`, whose kernel is `pairThetaKer` for `a i` and whose datum is `modDatum` of `x` and the
Fock vector of `Q`. It equals `κ` times the inner product of `modTransposedLift` of `z` (formed with
`P`, `x`) with `y`. 

 ## Periods of two forms and the seesaw between lift and transposed lift 

### `Space.height_reindex`

 Relabelling the coordinates of a hermitian space along a bijection `e` that carries the signs
`s` to `t` preserves the height of group elements. 

### `Space.integrable_moderate_mul_forms`

 Let the types `k` form a conjugate cuspidal pair. The product of the moderate weight
`w.weightFn`, a form of type `k d` on `S` (which decreases rapidly) and a form on `T`, read along
`w.comparisonMap` and moved by `r`, is integrable. 

### `Space.periodPairing`

 The integral over the quotient of the group of `S` of the weight, a form on `S`, and a form on
`T` that is pulled back along `w.comparisonMap` and translated by the real point `r`. 

### `Exchange.IsEdgeFamily.isConjKernelPair_source`

 The types `k` on the source of an edge family form a pair of conjugate cuspidal types. 

### `Exchange.IsEdgeFamily.isConjKernelPair_target`

 The types `k'` on the target of an edge family form a pair of conjugate cuspidal types. 

### `Exchange.integrable_kernel_mul_forms`

 For moderate weight `N` and forms `y` on `S` and `f` on `S'` whose types belong to conjugate
cuspidal pairs, the product of `N`, `y`, the theta kernel of `T'` and `S'` with datum `φ` and `f` is
integrable on the product of the two quotients. 

### `Exchange.exists_continuousLinearMap_eq_integral_kernel_mul_forms`

 Let `k`, `k'` be pairs of conjugate cuspidal types (`New.Exchange.IsConjKernelPair`), `y` a form
of type `k d` on `S` and `f` a form of type `k' d'` on `S'`. Let `N` be a moderate weight, with a
function on the group of `S` and a map from it to the group of `T'`. For a Fock vector `v` let θ_v
be the theta kernel of the pair `T'`, `S'` for the characters `a`, `b` and the datum
`modDatum T' S' 𝔪 Ψ v`, made of `v` at infinity and `Ψ` modulo `𝔪`. Then the integral of
`N.weightFn g * y g * θ_v (N.comparisonMap g, x) * f x` over `x` and `g` in the quotients of the
groups of `S'` and `S` is a continuous linear function of `v`. 

### `Exchange.integrable_mul_weight_mul_forms`

 For a continuous `α` of compact support on the real points of the group of `T`, a moderate
weight `M` and a form `U` on `T`, the product of `α r`, `M`, `f` and `U` moved by `r` is
integrable in the two variables. 

### `Exchange.integral_kernel_mul_forms_eq_integral_periodPairing`

 The seesaw for one pair of forms. If the lift of `y` by the datum of `Q` is the average against
`α` of the real translates of `U`, and the weight `N` times the kernel of `p` with characters `a'`,
`b'` and finite datum `Ψ'` agrees with `M` times the kernel with `a`, `b`, `Ψ` of the lift, namely
the kernel of `Q`, then the double integral of `N`, `y`, `f` and the kernel of `p` is the average
against `α` of the periods with weight `M` of `f` against the translates of `U`. 

### `Exchange.IsSeesawMatched`

 The polynomials `p` for the pair `T' → S'` that match the pair `S → T` in the seesaw
`New.Exchange.seesaw_periods`. The data are families indexed by `o : J` and `i : X o`: forms `y` on
`S` and `f` on `S'`, moderate weights `N` and finite data `Ψ'`, with `y` of type `e₁`, lifts of type
`e₂` on `T`, and characters `a o` for `S → T` and `a' o` for `T' → S'`; sums run over `W o` with
coefficients `u o`. The polynomial `p` matches if there are a polynomial `Q`, finite data `Ψ` and
moderate weights `M` with two properties. (a) For every real point, the sums of the periods with
weight `M` of `f` against the lifts of `y` by `Φ` and `Ψ`, moved by that point, are a multiple of
the vector `c`. (b) The weight of `N` times the kernel of `p` and `Ψ'` along the map of `N` equals
the weight of `M` times the kernel of `Q` and `Ψ` along the map of `M`. 

### `Exchange.seesaw_periods`

 Seesaw, for families indexed by `o : J` and `i : X o`. Take two edge families
(`New.Exchange.IsEdgeFamily`): characters `a` with polynomial `Φ` for `S → T`, and characters `a'`
with polynomial `Φ'` for `T' → S'`. Take forms `y o i` on `S` and `f o i` on `S'`, moderate weights
`N o i`, and finite data `Ψ' o i` on matrices over residue rings. Suppose the matched polynomials
(`New.Exchange.IsSeesawMatched`) span all polynomials. These are the ones whose kernel agrees, up to
moderate weights, with a kernel of `S → T` for some polynomial and finite data `Ψ`, such that the
`u`-weighted sums over `W o` of the periods of `f` against the real translates of the lifts of `y`
by `Φ` and `Ψ` are multiples of `c`. Then there is a single `β` such that, for every `o`, the sum
over `i ∈ W o` of `u o i` times the period (`New.Space.periodPairing`, with weight `N o i`, moved by
`r`) of `y o i` against the transposed lift `modTransposedLift` of `f o i` equals `β * c o`. 
