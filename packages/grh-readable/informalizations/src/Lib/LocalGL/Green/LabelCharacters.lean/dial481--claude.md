---
{
  "module": "src/Lib/LocalGL/Green/LabelCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/LabelCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/LabelCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Label characters Ξ_c: orthonormality, central idempotents and twisting by χ∘det

Let k be a finite field, and let T be an injective multiplicative character of an algebraically
closed extension K of k. A label of degree r (`New.IsLabel`) is a monic squarefree polynomial c of
degree r with c(0) ≠ 0. The character Ξ_c = `New.labelChar` T c is the product in `New.Hall`
(parabolic induction) of Green's functions τ_P = `New.greenTau` T P over the irreducible factors P
of c. The file shows that the Ξ_c are orthonormal irreducible characters of GL_r(k). It then studies
the elements e_c = `New.labelIdem` n c of ℂ[GL_n(k)] formed from Ξ_c (0 if c is not a label of
degree |n|), and computes the twist of Ξ_c by χ∘det.

## Main definitions and results

* `New.rankPart_labelChar`, `New.rankInner_labelChar`: Ξ_c lives in dimension r, and the Ξ_c are
  orthonormal.
* `New.IsLabel.isIrreducibleChar_labelChar`: Ξ_c is an irreducible character of GL_r(k).
  `New.lift_labelChar_self` says in the form `New.Lift` that Ξ_c is a genuine character, an
  ℕ-combination of characters. It does not record irreducibility.
* `New.labelIdem_orthogonal`: the e_c are orthogonal idempotents.
* `New.hyperplaneSum_mul_labelIdem`: let l be a nonzero vector. Then e_c kills the sum of χ(det h)⁻¹
  h over the invertible h = 1 + u lᵀ, when the element of kˣ naming χ (`New.charName`) is not a root
  of c.
* `New.tupleIdem`, `New.isCentralProj_tupleIdem`, `New.tupleIdem_orthogonal`: the tensor products
  ⊗_w e_{c_w} over a finite family of fields k_w are orthogonal central idempotents.
* `New.evalGL_labelChar_mul_det`: multiplying the character Ξ_c by `χ ∘ det` scales the roots of `c`
  by the unit x_χ of `k` that corresponds to `χ` under `T`.

Notions from other files:
* `New.charName`: For T injective, the group isomorphism χ ↦ x_χ from the multiplicative characters
  of k to k^×, inverse to a ↦ θ_a restricted to k, with θ_a taken for Q = |k|.
* `New.Hall.rankInner`: For complex functions F, H on similarity classes, the average over GL_n(k)
  of the conjugate of F times H.
* `New.IsIrreducibleChar`: `f` is an irreducible character, stated as three conditions: (a) `f` is a
  character, (b) `New.classInner f f = 1`, and (c) for every class function `h` and every `y`,
  `f 1 * New.classInner f (h (· * y)) = New.classInner f h * f y`.
* `New.IsFaithfulMulChar`: K is algebraically closed and the character T of Kˣ is injective.
* `New.thetaChar`: The character θ_x = T^a of K, where a is a chosen natural number with
  T(x) = exp(2πi/(Q−1))^a.

## Relation to the literature

Known; see `Lib.LocalGL.Green.TauFunctions` for sources.


### `Matrix.vecMulVec_left_injective_of_ne_zero`

 For `v ≠ 0`, the map `u ↦ u vᵀ` from vectors to matrices is injective. 

### `LinearMap.apply_one_eq_neg_charpoly_coeff_zero`

 For a linear map `g` from a field `R` to itself, `g 1` (its determinant) is minus the
constant coefficient of its characteristic polynomial. 


## Orthonormality and irreducibility of Green's characters

Most proofs go by induction on the irreducible factors of c. Orthonormality uses `New.Hall.skew`,
which is adjoint to multiplication by τ_P and is a derivation.


### `labelChar_X_sub_C`

 Let K be an algebraically closed field over the finite field k, with an injective multiplicative
character T : K → ℂ. For a multiplicative character χ of k, let a ∈ kˣ be its name under T, the
inverse of the isomorphism a ↦ θ_a restricted to k, with θ_a formed with Q = |k|. Then Green's class
function Ξ_{X − a} equals χ∘det on similarity classes of dimension 1 and is zero on all other
classes.

A case of Green's identification of his rank-one characters with the multiplicative characters of
`k`. 

### `splits_of_forall_root_pow_card_eq`

 A polynomial over the finite field `k` splits over `k` if each of its roots in the
algebraically closed field `K` is fixed by `x ↦ x ^ q`, where `q` is the order of `k`. 

### `IsLabel.exists_eq_prod_charName_of_splits`

 A label `c` of degree `r` that splits over `k` is the product of the `X - charName T (χ i)`
for some `r` multiplicative characters `χ i` of `k`. 

### `IsLabel.exists_eq_prod_charName_of_root_pow_card_eq`

 `IsLabel.exists_eq_prod_charName_of_splits` with the splitting of `c` tested on its roots in
`K`: each is fixed by `x ↦ x ^ q`, where `q` is the order of `k`. 

### `rankPart_labelChar`

 For a label `c` of degree `r`, the character `New.labelChar T c` lives in dimension `r`: its
part of rank `r` is the whole of it. 

### `skew_greenTau_labelChar_eq_zero`

 Let K be an algebraically closed field over the finite field k, with an injective multiplicative
character T : K → ℂ. A label of degree d is a monic squarefree polynomial of degree d with nonzero
constant term. Let c be a label of degree r, and P an irreducible label of degree d that does not
divide c. Then skewing Ξ_c by τ_P in dimension d gives zero: for every class a, the average over
b ∈ GL_d(k) of conj τ_P(b) times the block average of Ξ_c at (a, b) is 0, where the block average is
the mean, over the corner block x, of Ξ_c at the block triangular matrix with diagonal blocks a, b
and corner x. Here τ_P is Green's class function, (−1)^d times the dimension-d part of Green's
cuspidal function, and Ξ_c is the parabolic-induction product of the τ_Q over the irreducible
factors Q of c. 

### `rankInner_labelChar_mul_constOne`

 Let T be faithful (`New.IsFaithfulMulChar`) and c a label of degree r with c(1) ≠ 0. Then
⟨Ξ_c, A * 1⟩ = ⟨Ξ_c, A⟩ on GL_r(k) for every class function A, where * is parabolic induction and 1
the constant function. 

### `rankInner_labelChar`

 Orthonormality: let T : K → ℂ be an injective multiplicative character of an algebraically
closed field K over the finite field k, and let c, c' be labels of degree r, i.e. monic squarefree
polynomials over k of degree r with nonzero constant term. Ξ_c is the product, by parabolic
induction, of Green's class functions τ_P over the monic irreducible factors P of c. Then the
average over GL_r(k) of conj Ξ_c · Ξ_{c'} (`rankInner r`) is 1 if c = c' and 0 otherwise.

A case of Green's theorem that his characters of general linear groups over a finite field are
irreducible and distinct: the class functions Ξ_c attached to labels of one degree are orthonormal.

This corresponds to the Deligne–Lusztig orthogonality formula, restricted to GL_r and to the class
functions Ξ_c of labels of degree r, which are defined by Green's formula rather than by
Deligne–Lusztig induction. 

### `IsLabel.isIrreducibleChar_labelChar`

 This is a case of Green's theorem: let K be an algebraically closed field over the finite field
k, with an injective multiplicative character T : K → ℂ. Let c be a label of degree |n|, i.e. a
monic squarefree polynomial of degree |n| with nonzero constant term. Then Green's class function
Ξ_c, evaluated on GL_n(k), is an irreducible character in the sense of `IsIrreducibleChar`, which
also requires that class functions act by scalars. Ξ_c is the parabolic-induction product of τ_P
over the monic irreducible factors P of c. 

### `IsLabel.isChar_labelChar`

 Green's function with label `c` is a character of `GL n k` for every `n`. 

### `lift_labelChar_self`

 Green's function with label `c` lifts to itself over `ℕ` along the trivial extension `k/k`. This
is `IsLabel.isChar_labelChar` in terms of `Lift`: for each m, Ξ_c on GL_m(k) is an ℕ-combination of
characters. 

### `skew_detChar_labelChar_eq_zero`

 If x_χ = `New.charName` T χ is not a root of the label c, then the skewing operator of the
character χ of GL_1(k) kills Ξ_c. 


## Label idempotents and hyperplane sums

For a polynomial `c` over `k`, `New.labelIdem n c` is the element
`e_c = ∑ (Ξ_c(1) / |G|) · conj Ξ_c(g) · g` of `ℂ[G]`, `G = GL_n(k)`, where `Ξ_c` is Green's
character with label `c` (`New.labelChar`); it is `0` unless `c` is a label of degree `|n|`.


### `labelIdem_orthogonal`

 Each polynomial c over k gives an element e_c of ℂ[G], where G = GL_n(k). If c is a label of
degree |n| (monic, squarefree, nonzero constant term), e_c = ∑_g (Ξ_c(1)/|G|)·conj Ξ_c(g)·g, with
Green's class function Ξ_c formed with a fixed faithful character. If c is not such a label,
e_c = 0. The family (e_c), indexed by all polynomials c, consists of idempotents, and those of
distinct polynomials have product zero. 

### `isClassFunction_labelIdem_coeff`

 The coefficients of `e_c = New.labelIdem n c` form a class function on `GL_n(k)`: they are
constant on conjugacy classes. 

### `hyperplaneSum_mul_labelIdem`

 Let χ be a multiplicative character of k whose name x_χ ∈ kˣ (`New.charName`) is not a root of
the polynomial c, and let l be a nonzero vector. Here e_c = `labelIdem n c` is ∑ (Ξ_c(1)/|G|)·conj
Ξ_c(g)·g in ℂ[G], G = GL_n(k), with Ξ_c formed with `New.faithfulChar` k, a fixed injective
multiplicative character of an algebraically closed field over k (`New.IsFaithfulMulChar`), when c
is a label of degree
|n|, and is 0 otherwise. Then the sum of χ(det h)⁻¹ h over the invertible h = 1 + u lᵀ (the matrices
that fix the hyperplane l ⬝ᵥ x = 0 pointwise), multiplied on the right by e_c, is zero. 

### `tupleIdem`

 For a tuple (c_w) of polynomials over the fields k_w, the tensor product of the label
idempotents e_{c_w} in the group algebra of ∏ GL_n(k_w). 

### `isCentralProj_tupleIdem`

 Let `c = (c_w)` be a tuple of polynomials over the finite fields `k w`, and let `tupleIdem n c`
be the tensor product of the label idempotents `e_{c_w}`, an element of the complex group algebra of
`∏_w GL_n(k w)`. This element is a central idempotent (`New.IsCentralProj`): it is idempotent and
its coefficients form a class function on `∏_w GL_n(k w)`. 

### `tupleIdem_orthogonal`

 For each tuple (c_w) of polynomials over the finite fields k_w, `tupleIdem` is the tensor
product ⊗_w e_{c_w} of the label idempotents of the group algebras of GL_n(k_w). It lies in the
group algebra of ∏_w GL_n(k_w). These elements are idempotents, and those of distinct tuples have
product zero. 

### `isCentralProj_sum_tupleIdem`

 Let `tupleIdem n c` be the tensor product of the label idempotents `e_{c_w}` for a tuple
`c = (c_w)` of polynomials over the finite fields `k w`, an element of the complex group algebra of
`∏_w GL_n(k w)`. For any finite set `s` of such tuples, the sum of `tupleIdem n c` over `c ∈ s` is a
central idempotent of this algebra (`New.IsCentralProj`): it is idempotent and its coefficients form
a class function. 


## Twisting by χ∘det and distinct conjugates of powers of a generator

* `New.scaleRootsEquiv`, `New.IsLabel.scaleRoots`: scaling the roots of a label by a unit `a` of `k`
  is multiplicative and preserves labels.
* `New.injOn_Iio_pow_card_pow_of_isPrimitiveRoot`: for `9 ∣ |k| - 1`, a power `ξ ^ l ^ a`, with `l`
  prime, of a primitive `(|k| ^ 3 ^ (e + 1) - 1)`-th root of unity has `3 ^ (e + 1)` distinct
  conjugates over `k`.
* `New.evalGL_labelChar_mul_det`: twisting `Ξ_c` by `χ ∘ det` scales the roots of `c` by the name of
  `χ`.


### `scaleRootsEquiv`

 For nonzero a in k, the multiplicative bijection of k[X] to itself scaling the roots of a
polynomial by a, with inverse scaling by a⁻¹. 

### `IsLabel.scaleRoots`

 Scaling the roots of a label `c` of degree `r` (`New.IsLabel`: monic, squarefree, of degree `r`,
with nonzero constant term) by a unit `a` of `k` gives a label of degree `r`. 

### `injOn_Iio_pow_card_pow_of_isPrimitiveRoot`

 Let `q = Nat.card k ≡ 1 mod 9` (`h_nine`), `r = 3 ^ (e + 1)`, `ξ` a primitive `(q ^ r - 1)`-th
root of unity in `K` and `l` a prime. Then `ξ ^ l ^ a` has `r` distinct conjugates: its `q ^ i`-th
powers, `0 ≤ i < r`, are distinct. 

### `evalGL_labelChar_mul_det`

 Let T be faithful, let c be a label of degree r (monic squarefree, with nonzero constant term)
and let χ be a multiplicative character of k. Then Ξ_c(g)·χ(det g) = Ξ_{c'}(g) for g in GL_n(k), for
any n, where c' = `c.scaleRoots x_χ` has roots x_χ times those of c. Here Ξ_c = `labelChar T c` is
the parabolic-induction product of the τ_P over the irreducible factors P of c, and
x_χ = `charName T χ` ∈ kˣ. A case of the compatibility of Green's characters with twisting by
χ∘det. 
