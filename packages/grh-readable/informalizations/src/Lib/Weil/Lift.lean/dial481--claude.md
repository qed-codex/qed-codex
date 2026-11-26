---
{
  "module": "src/Lib/Weil/Lift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Lift.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Lift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta lifts of forms: products of minors, edges, arrows between spaces of forms

This file studies theta lifts between spaces of automorphic forms on unitary groups. Over the reals,
`Ω` assigns operators on a Fock space to the points of a pair of real unitary groups, and `e`, `e'`
are kernels on the two groups; the forms of parameter `l` are those of type `New.typeKernel l s`. A
half edge relates `e` to `e'` through a Fock vector `Φ` and its lifts; an edge does so in both
directions. Edges together with finite data give arrows, data for which the global lift sends forms
to forms. The lift is equivariant under the finite points. The transposed lift is the lift for the
swapped kernel, and the descent `y' ↦ conj (transposed lift of conj y')` is the adjoint of the lift.

## Main definitions and results

* `New.isJointHighest_prod_det_pow_staircaseWeight`: a product of powers of nested minors, one nest
  for each sign, is nonzero, harmonic for both groups, and a highest weight vector for the rows and
  for the columns.
* `New.ParamsCorrespond`, `New.jointHarmonic`: parameters `l`, `l'` that correspond at every
  infinite place, and a chosen product of joint harmonics (`New.IsJointHarmonic`) for them.
* `New.IsHalfEdge`, `New.IsEdge`: `e` is a cusp kernel, and the integral of `⟨Φ, Ω (x, 1) Φ⟩`
  against `conj e` is not zero. The lift with `Φ` of a form of type `e` is a form of type `e'` once
  it has a level. The lift with each polynomial Fock vector is a real convolution of it. An edge has
  this both ways.
* `New.ParamsCorrespond.isEdge_jointHarmonic`: for corresponding parameters the chosen product is
  an edge for the real Weil representation.
* `New.formLift`, `New.IsArrow`: the lift on forms, and the data φ for which it sends forms of type
  e to forms of type e'.
* `New.IsEdge.isArrow`, `New.IsEdge.isForm_star_lift_swap`: an edge tensored with any finite datum
  gives arrows in both directions, and the descent sends forms of type e' to forms of type e.

Notions from other files:
* `New.Space`, `New.Space.lift`: a hermitian space with a point, given by a matrix J over E and x in
  GL_n(𝔸) with xᴴJx equal to diag(s) at the infinite places and 1 at the finite places; the theta
  lift h ↦ ∫_{[S]} θ(ω(g, h)φ) y(g) dg of y with datum φ.
* `New.Space.IsForm`, `New.typeKernel`: a form of type e is a bounded automorphic function that
  right convolution (`New.realConv`) with e fixes; `typeKernel l s` is the product over the infinite
  places of the kernels `dsKernel` with parameters l.
* `New.Fock.fockSpace`, `New.Fock.polyVector`, `New.Fock.piTensor`: the Fock space on ℂ^ι with its
  L¹ norm, the vector (polynomial times Gaussian) of a polynomial, and the product of Fock vectors
  in separate variables.
* `New.integratedRep`: for a representation π of U(diag ε) by bounded operators and a function f,
  the operator π(f) with π(f)x = ∫ f(g)π(g)x dg, when such a bounded operator exists.

## Relation to the literature

Known result: Joint harmonics and global theta lifts between discrete series types. Here the
parameter has large gaps, and the types are given by integrable projector kernels. The lift is shown
to carry forms fixed by one kernel to forms fixed by the other, in both directions, without Howe
duality. Source: J.-S. Li, Theta lifting for unitary representations with nonzero cohomology, Duke
Math. J. 61 (1990); Howe, JAMS 2 (1989); A. Ichino, arXiv 2002.09148, Lemma 7.8.



## Products of minors

Explicit harmonic highest vectors in the polynomial (Fock) model: polynomials in variables
`X (a, c)`, with rows `a : n`, all of sign `1`, and columns `c : r` of signs `s c`.


### `New.staircaseWeight`

 The weight at the column `c` of the staircase with `k η j` minors of size `j` and sign `η`,
where `o c` is the place of `c` among the columns of its sign. The first term is the weight of
the vacuum for the columns; it equals `γ + card n` if `s c = -1` and `γ` if `s c = 1`. The sum
counts the minors of sign `s c` and size `j < card n` that contain the column `c`, those with
`o c < j`. 

### `New.staircaseBlock`

 The matrix of variables on the first `p` rows and columns for the sign `η`. Its entry `(i, j)`
is the sum of the `X (a, c)` over the rows `a` at place `i` in the decreasing order of `η • l'` and
the columns `c` of sign `η` with `o c = j`. There is at most one such pair `(a, c)` if `l'` is
injective and `o` is injective on the columns of sign `η`. 

### `New.sum_sigma_filter_eq_sum_mul_sum_Ioo`

 Counting layers. For each sign `η` and size `p < N` take `k η p` layers, with places
`0, …, p - 1`. The layers of sign `η` that have the place `m η` are those of size `p > m η`. So the
sum of a weight `w η` over all such layers is the sum of `w η` times their number. 

### `New.exists_equiv_fin_eq_card_filter_lt`

 For injective `l`, number the columns `c` of sign `η` by decreasing `η * l c`: the number `o c`
of columns of the same sign that come before `c` is a bijection onto an initial segment of `ℕ`. 

### `New.exists_equiv_decreasingPosition_smul`

 For injective `l` and a sign `η`, the position of a row in the decreasing order of `η • l` is a
bijection onto `Fin (card n)`, and the position for `-η` is the reversed one. 

### `New.sign_eq_of_ne_zero_of_lt`

 Layers of opposite signs share no row. Let `x η` be the place of a row among `N` places in the
order of sign `η`, the order for `-η` being the reverse. Assume that `k 1 i = 0` or `k (-1) j = 0`
whenever `N < i + j`. If `k η p ≠ 0`, `k μ q ≠ 0`, `x η < p` and `x μ < q`, then `η = μ`. 

### `New.isJointHighest_prod_det_pow_staircaseWeight`

 Order the rows by decreasing `η • l'` and the columns of sign `η` by decreasing `η • l` (`l`,
`l'` injective); `decreasingPosition (η • l') a` is the place of the row `a` and `o c` the place of
the column `c`. Take the product over `η = ±1` and `p < card n` of the `k η p`-th power of the minor
on the first `p` rows and columns for `η`. Assume that `k η p = 0` if there are fewer than `p`
columns of sign `η` and `p < card n`, and that `k 1 i = 0` or `k (-1) j = 0` whenever
`i + j > card n`. Let `ν a` be the weight of the vacuum at the rows plus the sum over `η` of `η`
times the number of minors of sign `η` that contain the row `a`. `FockDualPair.std 1 s γ γ'` has
rows `n`, columns `r` of signs `s`, and shifts `γ`, `γ' + card n`. `staircaseWeight` at `c` combines
the column vacuum weight (`γ' + card n` if `s c = -1`, else `γ'`) with the count of minors of sign
`s c` containing `c`. Then the product satisfies `New.FockDualPair.IsJointHighest`: it is nonzero,
harmonic for both groups, highest of weight `ν` for the rows, ordered by `l'`, and highest of weight
`New.staircaseWeight` for the columns, ordered by `-l`. 


## Edges: archimedean data for theta lifts

* `New.isHalfEdge_of_oscillatorPair`: a tensor product of joint harmonics for oscillator pairs is a
  half edge.


 ### Corresponding parameters and the chosen joint harmonic 

### `negIf`

 `-l` if `d` is true and `l` otherwise: the parameter of the forms of type `l`, or, if `d` is
true, of their conjugates. 

### `ParamsCorrespond`

 The doubled parameters l for the signs s : n → ℤˣ and l' for the signs t : n' → ℤˣ correspond:
at each infinite place w they satisfy the block rule (`New.IsBlockRule`) for the weights γ w and γ'
w. 

### `jointHarmonicAt`

 A chosen joint harmonic polynomial at the place `w` for the signs `t`, `s`, the weights `γ w`,
`-γ' w` and the parameters `l' w`, `-l w`; an arbitrary polynomial if none exists. See
`isJointHarmonic_jointHarmonicAt`. 

### `jointHarmonic`

 The product over the infinite places `w` of the chosen polynomials `jointHarmonicAt`, each in
the variables of `w`. 

### `ParamsCorrespond.isMatch`

 If the parameters `l` (signs `s`) and `l'` (signs `t`) correspond for the weights `γ`, `γ'`,
then `l' w` and `-l w` match (`New.IsMatch`) for the standard dual pair data at each place `w`. 

### `ParamsCorrespond.symm`

 The correspondence of parameters is symmetric: if `l`, `l'` correspond for the signs `s`, `t`
and the weights `γ`, `γ'`, then `l'`, `l` correspond for `t`, `s` and `γ'`, `γ`. 

### `ParamsCorrespond.neg`

 If `l`, `l'` correspond for the signs `s`, `t` and the weights `γ`, `γ'`, then `-l`, `-l'`
correspond for the signs `-s`, `t` and the weights `card n - γ`, `card n' - γ'`. 

### `isJointHarmonic_jointHarmonicAt`

 Let `w` be an infinite place of `E`. Suppose the doubled parameters `l' w` and `-l w` match
(`New.IsMatch`) for the standard dual pair datum `.std t s (γ w) (-γ' w)`, which has rows with signs
`t`, columns with signs `s`, and weights `γ w` and `-γ' w`. Then the chosen polynomial
`jointHarmonicAt γ γ' l l' s t w` is a joint harmonic for this datum (`New.IsJointHarmonic`): it is
nonzero, highest for the row and column actions with the weights of the two lowest `K`-types, and
termwise harmonic for the datum and for its swap. 

### `ParamsCorrespond.prod_eq_smul_jointHarmonic`

 Let the doubled parameters `l` (for the signs `s`) and `l'` (for the signs `t`) correspond for
the weights `γ`, `γ'`. For each infinite place w, let `P w` be a joint harmonic for the standard
dual pair `.std t s (γ w) (-γ' w)` with parameters `l' w` and `-l w`. Then the product over w of the
`P w`, with the variables of `P w` renamed to those of the place w, is a scalar multiple of
`jointHarmonic γ γ' l l' s t`. 

### `ThetaKernel.HasRealPart`

 The real points of the two groups act through `Ω` on the real vector `v` of a datum
`V.integrated v f` and leave its finite part `f` alone. 

### `IsHalfEdge`

 Half an edge from `e` to `e'`: `e` is a cusp kernel of order `0`, and the integral of
`⟨Φ, Ω (x, 1) Φ⟩` against `conj e / e 1` is not zero. For a theta kernel whose real points act
through `Ω` (`ThetaKernel.HasRealPart`) and a form of type `e`, the lift with `Φ`
is a form of type `e'` as soon as it has a level. For each polynomial Fock vector `v` there is one
continuous `α` of compact support such that, for all these kernels and forms, the lift with `v` is
the real convolution with `α` of the lift with `Φ`. 

### `IsHalfEdge.isCuspKernel_source`

 `e` is a cusp kernel of order `0`. 

### `IsHalfEdge.zetaIntegral_ne_zero`

 The zeta integral of `Φ` against `conj e`, normalised by `e 1`, is not zero. 

### `IsHalfEdge.isForm_lift`

 The lift with `Φ` of a form `y` of type `e` is a form of type `e'` if it has a level. 

### `IsHalfEdge.exists_lift_eq_realConv`

 Every Fock polynomial `v` has a continuous function `α` of compact support such that the lift
  with `v` of any form `y` of type `e` is the convolution with `α` of the lift with `Φ`. 

### `IsHalfEdge.lift_isForm_and_eq_realConv`

 Let `Φ` be a half edge for `Ω` from `e` to `e'`, and let `v` be a polynomial Fock vector. There
is one compactly supported `α` on `GInf E t` with the following property. Take any spaces `V`, `S`,
`T`, any theta kernel `Θ` with `Θ.ω ((x, 1), (x', 1))` acting on `V.integrated u f'` as `Ω (x, x')`
acts on `u`, any `f`, and any form `y` of type `e` (bounded automorphic, fixed by convolution with
`e` if `e` is integrable). Then the lift `F` of `y` with `V.integrated Φ f` is a form of type `e'`
if it has a level, and the lift with `V.integrated v f` is `realConv α F`. 

### `IsEdge`

 Φ is a half edge for Ω with kernels e, e', and also for Ω with its two groups exchanged with
kernels conj(e'), conj(e). 

### `IsEdge.swapped`

 With the two groups exchanged, `Φ` is a half edge from `conj e'` to `conj e`. 

 ### Products of joint harmonics are edges 

### `integral_piTensor_eq_integratedRep`

 Let `π w` be unitary representations of growth `A` of the unitary group of signs `s : n → ℤˣ` on
the Fock space of signs `η : ι → ℤˣ`, let `k w` be continuous functions with integrable moment of
order `A`, and let `T` be a continuous linear map from `fockSpace (realSigns E η)` to a Banach space
`X`, and let `v w` be vectors of `fockSpace η`. The integral over the real points `x : GInf E s` of
the image under `T` of the pure tensor (`piTensor`) of the vectors `k w (x w) • π w (x w) (v w)`
converges, and equals the image under `T` of the pure tensor of the local integrals
`integratedRep (π w) (k w) (v w)`. 

### `integral_typeKernel_smul_piTensor`

 Let `Ω (x, 1)` act on pure tensors place by place through the oscillator pairs `π w`, `π' w` for
the dual pair data `T w`, and let joint harmonics `Φ w` for the parameters `l w`, `l' w` exist. Here
`typeKernel l s` is the product over the places of the kernels `dsKernel (l w)`, each the formal
degree times the conjugate discrete series coefficient. For a continuous linear `L`,
`x ↦ typeKernel l s x • L (Ω (x, 1) v)` is integrable at a pure tensor `v`, and its integral is `L`
of the tensor of the vectors `π w (dsKernel (l w)) (v w)`, where `π w (f)` is the operator
`∫ f(g) π w g dg`. 

### `isCuspKernel_typeKernel_neg_of_isJointHarmonic`

 If the parameters `l w`, `l' w` have joint harmonics, the kernel of type `-l` is a cusp
kernel. 

### `lift_piTensor_integratedRep`

 The lift of a form of type `-l` sees only the part of type `l` of the real vector. Here
`Ω (x, 1)` acts on pure tensors through the oscillator pairs `π w`, `π' w`, joint harmonics for
`l w`, `l' w` exist, and the real points act through `Ω` on the theta kernel: the lift with a pure
tensor is unchanged when each factor is replaced by its projection `π w (dsKernel (l w))`. 

### `integral_mul_lift_eq_lift_piTensor`

 Let `Ω` act on pure tensors through the oscillator pairs `π w`, `π' w` and on the theta kernel
through its real points, let `y` be a form of type `-l`, and write `p w = π w (dsKernel (l w))`. Let
`k w` be continuous, with integrable moment of order `card ι`, and
`π' w (k w) (p w (Φ w)) = p w (v w)`. Fix a finite datum `f`. If `F` is the lift of `y` with
`V.integrated Φ₀ f`, where `Φ₀` is the tensor of the Fock vectors of the joint harmonics `Φ w`, then
`x ↦ (∏ w, k w (x w)) * F (g * (x, 1))` is integrable, and its integral is the lift of `y` with the
tensor of the `v w`, at `g`. 

### `integral_fockInner_mul_typeKernel_ne_zero`

 Let `s`, `t` be the signs of two real unitary groups over the infinite places of `E`. At each
place `w`, let `π w`, `π' w` be commuting oscillator representations of `U(diag s)`, `U(diag t)` on
the rows and columns of the dual pair data `T w`, and let `Φ w` be a joint harmonic for `T w` of
parameters `l w`, `l' w`. If `Ω (x, 1)` maps each pure tensor `⊗ v w` to `⊗ π w (x w) (v w)`, then
for `Φ₀ = ⊗ polyVector η (Φ w)` the integral over `GInf E s` of `⟨Φ₀, Ω (x, 1) Φ₀⟩ * conj
(typeKernel (-l) s x) / typeKernel (-l) s 1` is not zero. 

### `isHalfEdge_of_oscillatorPair`

 If `Ω` acts on pure tensors place by place through oscillator pairs (commuting oscillator
representations of the two groups), the tensor product of the Fock vectors of joint harmonics `Φ w`
for the parameters `l w`, `l' w` (nonzero polynomials, harmonic and highest for both groups) is a
half edge from the kernel of type `-l` to the kernel of type `l'`. 

### `isEdge_of_isJointHarmonic`

 Let `s : n → ℤˣ`, `t : n' → ℤˣ` be the signs of two real unitary groups. At each infinite place
`w`, let `Φ w` be a joint harmonic for `FockDualPair.std t s (γ w) (-γ' w)` with parameters `l' w`,
`-l w`: a nonzero polynomial in variables indexed by `n' × n`, harmonic for both groups and, for
each group, highest of the weight of its lowest `K`-type. Then the Fock vector of the product of the
`Φ w`, each in the variables of `w`, is an edge for `realPairWeil γ γ'` from `typeKernel l s` to
`typeKernel l' t`. This means it is a half edge (`New.IsHalfEdge`, requiring in particular that the
integral of `⟨Φ, Ω (x, 1) Φ⟩` against `conj e / e 1` be nonzero) for these kernels, and also, with
the two groups exchanged, for their conjugates. 

### `ParamsCorrespond.isEdge_jointHarmonic`

 If `l`, `l'` correspond (the block rule holds at every infinite place), the Fock vector
`jointHarmonic` is an edge for the real Weil representation `realPairWeil γ γ'` from
`typeKernel l s` to `typeKernel l' t`. Here `jointHarmonic` is the product over places `w` of the
chosen polynomials `jointHarmonicAt`. Being an edge means a half edge for these kernels, and also
for the representation with its groups exchanged and the conjugate kernels in reverse order.
`typeKernel l s` is ∏_w (formal degree)·conj(discrete series coefficient) on U(diag s). 


## Arrows: the theta lift on forms, equivariance and adjoints

The theta lift as a linear map between spaces of forms. A theta kernel K for spaces S and T
(`New.ThetaKernel`) consists of a representation ω of the pair of their adelic unitary groups and a
functional θ, and `New.Space.lift` integrates a function on the first group against the kernel
θ(ω(g, h)φ). `New.Space.Form S e` is the space of forms of type e on S (`New.Space.IsForm`), and
`New.ThetaKernel.swap` exchanges the two groups, so that its lifts are the transposed lifts.


### `formLift`

 A chosen bilinear map (φ, y) ↦ L_φ y from data and forms of type e on S to forms of type e' on T
that agrees with the theta lift `New.Space.lift` whenever y is of rapid decay and its lift is such a
form. It is built from left inverses of the inclusions of these spaces of functions. 

### `IsArrow`

 The datum φ is an arrow e → e' for the theta kernel K: forms of type e on S are rapid, and their
lifts by φ are forms of type e' on T. 

### `conjForm`

 Complex conjugation F ↦ conj(F), as a conjugate-linear map from forms of type e to forms of
type e', when e' is the conjugate of e. 

### `coe_conjForm`

 `conjForm h y` is the pointwise complex conjugate of `y`. 

### `IsEdge.isArrow`

 Let Φ be an edge e → e' for the real Weil representation `realPairWeil γ γ'`. This means Φ is a
half edge from e to e', and also, with the two groups exchanged, from ē' to ē. A half edge requires
that e is a cusp kernel of order 0, that ∫⟨Φ, Ω(x,1)Φ⟩·conj e(x)/e(1) dx ≠ 0, and that lifts with Φ
of forms of type e are of type e' once they have a level. Let a, b be automorphic characters of
weights γ, γ' with tame parts ψ, ψ', and let f lie in the finite part of the data space of
`S.hom T`. Then for the theta kernel `pairThetaKer S T a b`, the datum
Φ ⊗ f = `integrated (S.hom T) Φ f` is an arrow e → e' (forms of type e are rapid and lift to forms
of type e'), and for the swapped kernel it is an arrow ē' → ē. 

### `IsEdge.isForm_star_lift_swap`

 Let Φ be an edge e → e' for `realPairWeil γ γ'`. This means Φ is a half edge from e to e', and
also, with the two groups exchanged, from ē' to ē. A half edge requires that e is a cusp kernel of
order 0, that ∫⟨Φ, Ω(x,1)Φ⟩·conj e(x)/e(1) dx ≠ 0, and that lifts with Φ of forms of type e are of
type e' once they have a level. Let a, b be automorphic characters of weights γ, γ' with tame parts
ψ, ψ', and let f lie in the finite part of `S.hom T`. Then for every form y' of type e' on T, the
descent by Φ ⊗ f is a form of type e on S. Here the descent is the conjugate of the lift of ȳ' by
Φ ⊗ f for the swapped kernel of `pairThetaKer S T a b`. 

### `IsEdge.exists_petersson_lift_eq_mul`

 Let Φ be an edge e → e' for the real Weil representation of weights γ, γ'; that is, Φ is a half
edge e → e', and also conj e' → conj e with the groups exchanged. There is a linear form κ on
polynomials with the following property for all spaces S, T of signs s, t, all characters a, b of
these weights, all f in the finite part of `S.hom T` (spanned by the finite Heisenberg translates of
the vacuum), all polynomials P and all forms y, y' of types e, e'. With the theta kernel
`pairThetaKer S T a b`, the Petersson product of y' with the lift of y by v_P ⊗ f is κ(P) times that
with the lift by Φ ⊗ f, and likewise for the product of ȳ with the transposed lift of ȳ'. Here v_P
is the Fock vector of P, v ⊗ f is `integrated (S.hom T) v f`, the transposed lift is the lift for
`K.swap`, and ȳ is the complex conjugate of y. 

### `eq_formLift_of_coe_eq`

 If some datum φ is an arrow e → e', then for any datum φ' a form z of type e' whose underlying
function is the lift of y by φ' is the value of `New.formLift` at φ' and y. 

### `coe_formLift`

 If the datum φ is an arrow from type e to type e' (forms of type e are rapid and lift to forms
of type e'), then the function underlying `formLift K e e' φ y` is the theta lift of y by φ. 

### `formRep_formLift`

 If φ is an arrow e → e', then for k, k' in the finite groups of S, T and a form y of type e,
the right translate by k' of the lift of y by φ is the lift by ω(k, k')φ of the right translate of
y by k. 

### `formRep_formLift_of_eq_smul`

 Let φ be an arrow and k, k' finite points with ω(k, k')φ = cφ'. Then the translate by k' of
the lift of a form y by φ is c times the lift by φ' of the translate of y by k. 

### `integral_mul_formLift_swap`

 If φ is an arrow e → e' and, for the swapped kernel, an arrow ε' → ε, then
∫_{[T]} z·L_φ y = ∫_{[S]} y·Lᵗ_φ z for forms y of type e and z of type ε', where L_φ is the lift and
Lᵗ_φ the transposed lift by φ. 

### `inner_formLift_adjoint`

 If φ is an arrow e → e' and, for the swapped kernel, an arrow between the conjugate types, then
⟨L_φ y, x⟩ = ⟨y, conj(Lᵗ_φ conj(x))⟩, where L_φ is the lift and Lᵗ_φ the transposed lift by φ. So
the adjoint of the lift is the descent x ↦ conj(Lᵗ_φ conj(x)). 
