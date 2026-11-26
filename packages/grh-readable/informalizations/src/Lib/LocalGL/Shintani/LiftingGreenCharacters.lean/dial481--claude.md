---
{
  "module": "src/Lib/LocalGL/Shintani/LiftingGreenCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/LiftingGreenCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/LiftingGreenCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shintani lifting of Green's characters along extensions of prime degree

For an extension `k'/k` of finite fields of prime degree, the file shows that Green's characters of
`GL_m` lift from `k` to `k'` by true characters. `New.Hall k` is the ring of complex functions on
similarity classes of square matrices over `k` of all sizes, with parabolic induction as product,
and μ is the inverse of the constant function 1 in it. For a label `c` (monic, squarefree,
`c(0) ≠ 0`), `New.labelChar T c` is the product Ξ_c of Green's functions `New.greenTau T P` over the
irreducible factors `P` of `c`. `thetaChar T q x` is a character of `K` attached to `x` and a field
size `q`; for `x` in `k`, `thetaChar T |k| x` at the norm from `k'` is `thetaChar T |k'| x`.
`New.Lift Z F F'` says that in each rank `m` one `Z`-combination of characters of
`GL_m(k') ⋊ Gal(k'/k)` restricts to `F'` on `GL_m(k')` and is `F` of the norm on the cosets of the
`σ` with fixed field `k` (`New.DescendsTo Φ F` for `F` over `k`; for `F'` over `k'`,
`DescendsTo Φ F'` means `Φ ∘ inl = F'.evalGL`).

## Main definitions and results

* `New.sum_evalGL_prod_eq_zero_iff`: the element `∑ conj (χ g) g` of a parabolically induced
  character `χ` kills a vector `v` if and only if the corresponding sum over the block upper
  triangular matrices kills all translates of `v`.
* `New.exists_isChar_descendsTo_labelChar`: let `P` be irreducible of degree `r = [L : k]`, a label
  (`IsLabel r P`), with a root `x`. Then one character of `GL_r(k') ⋊ Gal(k'/k)` descends both to
  the cuspidal function of `θ_x` times `μ` and to `(-1) ^ r Ξ_P μ` over `k'`. This is used to lift
  `Ξ_P` from `k` to `k'`.
* `New.lift_detChar`: the lift of `χ ∘ det`.
* `New.DescendsTo.card_mul_classInner`: the inner product of two lifts in terms of the inner
  products over `k'` and over `k`.
* `New.shintani_lift_labelChar`: the lift by true characters for any label (`New.IsLabel`: monic,
  squarefree, non-zero constant term).

Notions from other files:
* `New.Hall.evalGL`: for `F : Hall k` and `g : GL n k`, the value of `F` at the similarity class of
  the endomorphism of `n → k` given by `g`.
* `New.blockHom b a`: the homomorphism sending a block upper triangular invertible matrix (for the
  level function `b`) to its diagonal block of level `a`.
* `New.classInner f h`: the inner product of complex functions on a finite set, the average of
  `conj (f g) * h g`; `New.Hall.rankInner n F H` is the same over `GL_n(k)` for functions on
  classes, `F.mulMoebius` is `F` times `μ`, and `New.finMean f` is the average of `f` over a finite
  type.

## Relation to the literature

Known result: Shintani lifting of characters of GL_n(F_q) to an extension field, with the lift
identified for Green's characters. Here the degree is prime, and only Green's characters with
squarefree labels and characters of the determinant are treated. For these, one character of the
semidirect product with the Galois group is the lifted character on GL_n(k'), and on the cosets of
the σ with fixed field k it is the original character at the norm; no bijection of characters is
given. Source: T. Shintani, J. Math. Soc. Japan 28 (1976) 396-414; A. Silberger and E.-W. Zink, J.
Algebra 319 (2008) 4147-4176, Thm 5.1; for tensor induction, Gluck-Isaacs, Illinois J. Math. 27
(1983).

See also `Lib.LocalGL.Green.TauFunctions`.



## Frobenius reciprocity for parabolically induced characters

A criterion for the element `∑ conj (χ g) g` of a parabolically induced character `χ` to kill a
vector, in terms of the sum over the block upper triangular matrices.


### `sum_evalGL_prod_eq_zero_iff`

 Let each `F a` be a character in every size (`hF`: the lift from `k` to itself makes each
`(F a).evalGL` an `ℕ`-combination of characters), and let the operators `A g` act on `v` like a
representation of `GL n k` (`hA_mul`). Let `χ` be the induction product of the `F a`, each cut down
to the size of the block of level `a`. Then `∑ g, conj (χ g) • A g v = 0` if and only if, for all
`y`, the sum of `conj (∏ a, F a (p_a)) • A (p * y) v` over the block upper triangular `p` with
diagonal blocks `p_a` vanishes. 

 ## A Galois-twisted character descending to Green's functions 

### `natDegree_dvd_iff_of_common_root`

 Let irreducible polynomials `S` over `k'` and `P` over `k` have a common root `z`. Then
`deg S ∣ n ↔ deg P ∣ [k' : k] * n`, as both sides say that `z ^ |k'| ^ n = z`. 

### `exists_rankInner_labelChar_eq_finMean`

 Let `P` be irreducible over `k` with root `x`, and let the label `c` (monic, squarefree, nonzero
constant term) of degree `n` over `k'` divide `P`. For some `a j` (`j < b`): (a) each root of `c` is
`k'`-conjugate to some `x ^ |k| ^ a j` with `a j < deg P`; (b) `b * [k'(x) : k'] = n`; (c) for each
class function `B` over `k'`, `(-1) ^ n` times the `GL_n(k')`-mean of
`conj (labelChar T c) * mulMoebius B` equals the mean over units `u` of `k'(x) ^ b` of `B` at
multiplication by `u` times `∏ j, conj` of the `thetaChar` of `x ^ |k| ^ a j` at `u j`. Here
`labelChar` is the product of Green's `τ_Q` over the factors `Q` of `c`, and
`mulMoebius B = B · μ`. 

### `bijective_frobeniusAlgEquivOfAlgebraic_pow_of_roots`

 Let `x` be a root of the irreducible `P` over `k`, and let `a j < deg P` (`j < g`) be exponents
such that every root of `P` over `k'` is conjugate over `k'` to some `x ^ |k| ^ a j`. If
`g * [k'(x) : k'] = deg P` and `[k' : k] * [k'(x) : k'] = deg P * s`, then the map
`(j, i) ↦ F ^ (a j + deg P * i)`, for `F` the Frobenius of `k'` over `k`, is a bijection from
`Fin g × Fin s` onto `Gal(k'/k)`. 

### `conj_thetaChar_prod_eq_prod_conj_thetaChar`

 Let `χ m : k' ⊗ L → k'(x)` be `k'`-algebra maps such that `χ 0` after the power
`F ^ (a j + deg P * i)` of the Frobenius `F` of `k'` over `k` is `χ (a j)` followed by the same
power of the Frobenius of `k'(x)` (`χ_frob`), and let these powers run once through `Gal(k'/k)`
(`frob_bij`). Then for a unit `t` of `k' ⊗ L`, `conj θ_x` at `χ 0` of the norm `∏ τ, τ t` is the
product over `j` of `conj θ_(x ^ |k| ^ a j)` at `χ (a j) t`. 

### `exists_isChar_descendsTo_labelChar`

 Let `P` over `k` be irreducible and a label of degree `r` (`IsLabel r P`: monic, squarefree,
nonzero constant term), with a root `x` in `K`, and let `[L : k] = r`. There is a character `Φ` of
the semidirect product `GL_r(k') ⋊ Gal(k'/k)` that descends (`DescendsTo`) to `μ` times the
cuspidal function `greenCuspidal k θ_x`, where `θ_x = thetaChar T (|k| ^ r) x`. The same `Φ`
descends to `(-1) ^ r Ξ_P μ`, with `Ξ_P = labelChar T P` formed over `k'`. 

### `lift_brauerLift_pow_of_forall_eq_one`

 Let `k'` be an algebra over itself (through some automorphism) whose Galois group is trivial
(`h_gal`), and let the structure map raise the roots of every polynomial to the power `a`
(`h_roots`). Then for every `η : K → ℂ` the Brauer lift of `y ↦ η (y ^ a)` lifts to the Brauer
lift of `η`: over `ℂ` every class function is a combination of characters. 

### `lift_labelChar_map_of_forall_eq_one`

 In the situation of `lift_brauerLift_pow_of_forall_eq_one`, let the structure map of `k'` over
itself also keep irreducible polynomials irreducible (`h_irr`). Then for every label `c` over `k'`
the function `labelChar T` of the image of `c` lifts to `labelChar T c`, by induction on the
irreducible factors of `c`. 

### `evalGL_map_eq_of_lift`

 Let `k'` be an algebra over itself with surjective structure map `s` (`h_surj`), and let `F`
lift to `F'` over it. Then `F'` at `s(g)` is `F` at `g`: a common lift `Φ` is `F'` on `GL n k'`
and descends to `F` on the coset of `1`, whose fixed field is `k'`. 

### `evalGL_labelChar_map`

 Galois equivariance of Green's functions. Let `T` be a faithful character (`K` algebraically
closed, `T : K → ℂ` injective), and let `Ξ_c = labelChar T c`, the parabolic-induction product of
the `τ_P` over the irreducible factors `P` of `c`. Then for `σ ∈ Gal(k'/k)`, every label `c` of
degree `r` over `k'` (monic, squarefree, of degree `r`, with nonzero constant term) and every
`g ∈ GL_n(k')`, we have Ξ_c(σ(g)) = Ξ_{σ(c)}(g). 

### `lift_detChar`

 Let `T` be an injective character of the algebraically closed field `K`, and let `χ`, `χ'` be
multiplicative characters of `k` and `k'` whose names correspond, that is, the name of `χ'` is the
image of the name of `χ`. Here `charName T χ` is the unit `x_χ ∈ kˣ` with `χ = θ_{x_χ}` on `k`, and
`θ` is built from `T` with `Q = |k|`. Then `χ ∘ det` lifts to `χ' ∘ det` by characters: for every
`m`, some character `Φ` of `GL_m(k') ⋊ Gal(k'/k)` descends (`DescendsTo`) both to `χ ∘ det` over `k`
and to `χ' ∘ det` over `k'`. 

### `rankInner_greenCuspidal_mulMoebius_brauerLift`

 Let `P` be a label of degree `m` over `k` with `P(1) ≠ 0`, and suppose that `Ξ_P` is `(-1) ^ m`
times the rank-`m` part of `greenCuspidal k θ`. Then the inner product in rank `m` of
`greenCuspidal k θ` times `μ` with the Brauer lift of `θ` is `1`. 

### `rankInner_neg_one_pow_smul_mulMoebius_labelChar`

 Let `c` be a label of degree `m` over `k'` with `c(1) ≠ 0`, and `B` a class function. The inner
product in rank `m` of `(-1) ^ m` times `Ξ_c μ` with `B` is the inner product of `Ξ_c` with
`(-1) ^ m` times the rank-`m` part of `B μ` times the constant function `1`. 

### `labelChar_map_evalGL_galActionGL`

 For a label `P` over `k`, the function `Ξ` of `P` formed over `k'` is Galois stable: its value
at `σ(g)` is its value at `g`, as `σ` fixes the coefficients of `P`. 

### `hasFixedField_iff_ne_one`

 In an extension `k'/k` of prime degree, the fixed field of `σ` is `k` exactly when `σ ≠ 1`. 

### `DescendsTo.card_mul_classInner`

 Let `k'/k` have prime degree, and let the class functions `Φ` and `Ψ` on
`GL n k' ⋊ Gal(k'/k)` descend to `F` and `G`. Then `#Gal(k'/k)` times the inner product of `Φ` and
`Ψ` is the inner product of their restrictions to `GL n k'`, plus `#Gal(k'/k) - 1` times the inner
product of `F` and `G` in rank `#n`. 

### `lift_labelChar_of_not_isRoot_one`

 The irreducible case of `shintani_lift_labelChar` when `1` is not a root. Let `P` be a label of
degree `m` over `k` with `P(1) ≠ 0` and `Ξ_P = (-1) ^ m` times the rank-`m` part of
`greenCuspidal k θ`, and let the character `J` descend to `greenCuspidal k θ` times `μ` over `k` and
to `(-1) ^ m` times `Ξ_P μ` formed over `k'`. Then `Ξ_P` lifts by characters to `Ξ_P` over `k'`. 

### `shintani_lift_labelChar`

 Shintani lifting: let `k'/k` be an extension of finite fields of prime degree (`hp`), `T`
injective (`IsFaithfulMulChar`) and `c` a label over `k` (`IsLabel`: monic, squarefree,
`c(0) ≠ 0`). Then `Ξ_c = labelChar T c` lifts by characters (`New.Lift ℕ`) to `Ξ_c` formed over
`k'`. 
