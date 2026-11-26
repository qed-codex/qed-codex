---
{
  "module": "src/Lib/LocalGL/Green/TauFunctions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/TauFunctions.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/TauFunctions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Green's characters of GL_n over a finite field: θ_x, τ_P, labels and their degrees

This file studies Green's characters of `GL n k` over a finite field `k` that are attached to
squarefree polynomials. These characters live in `New.Hall k`, the complex-valued functions on
similarity classes of square matrices of all sizes, with parabolic induction as product. A faithful
character `T` of the algebraic closure `K` gives characters `θ_x = New.thetaChar T Q x`. For a label
`c`, they also give the product `Ξ_c = New.labelChar T c` of the `τ_P` over the irreducible factors
`P` of `c`. The file proves the symmetries of `θ_x`. It shows that the `τ_P` are cuspidal and
orthonormal and do not depend on the chosen root.

## Main definitions and results

* `New.faithfulChar`, `New.thetaChar`: a faithful character `T` of the algebraic closure, and the
  power `θ_x` of `T` attached to an element `x` of the subfield with `Q` elements.
* `New.greenTau`, `New.labelChar`: the function `τ_P` of an irreducible `P`, and the product `Ξ_c`
  of the `τ_P` over the irreducible factors of `c`.
* `New.IsLabel`: labels of degree `r`, which are monic squarefree polynomials with nonzero constant
  term.
* `New.charName`: for `T` faithful, the isomorphism χ ↦ x_χ from the multiplicative characters of
  the finite field k onto k^×; its inverse sends a unit a to the restriction of θ_a to k.
* `New.rankInner_greenTau`: the `τ_P` are orthonormal.
* `New.labelChar_degree_bounds`: let `q = |k|`. Let `c` be a label of degree `r`
  (`New.IsLabel r c`), with `r = card n`. Let `Ξ = New.labelChar T c` on `GL n k`. Then the real
  part of `Ξ(1)` is non-negative. Also `Ξ(1) conj Ξ(1) / |GL n k|` is at least
  `(1 - r / q) / q ^ r`.

Notions from other files:
* `New.Hall.greenCuspidal`: The class function C_η = (β_η·μ) ∗ 𝟙: the pointwise product of the
  eigenvalue sum β_η with the inverse μ (`moebius`) of 𝟙 (for any F, `F.mulMoebius` is the pointwise
  product F·μ), multiplied in the induction product by the constant function 𝟙.
* `New.Hall.brauerLift`: The class function β_η sending an endomorphism to the sum of η over the
  roots in K of its characteristic polynomial, counted with multiplicity.
* `New.Hall.evalGL`: For a complex function F on similarity classes and an invertible matrix g in
  `GL n k`, indexed by a finite type n, the value of F at the class of the endomorphism of `n → k`
  given by g.
* `New.Hall.rankInner`: For n and complex functions F, H on similarity classes, the average over
  GL_n(k) of the conjugate of F times H.

## Relation to the literature

Known result: Green's characters of GL_n(F_q) and the parabolic-induction ring. Only cuspidal
characters and their products over squarefree polynomials are treated, named through a fixed
character of the algebraic closure, with cuspidality, orthonormality, independence of the chosen
root and a degree bound. Hall polynomials are not covered. Source: J. A. Green, The characters of
the finite general linear groups, Trans. AMS 80 (1955), Thms 2, 9, 12-14; for the ring on all
matrices, Z. Chen, arXiv 2408.06191, Prop. 3.2.



## Green's characters of squarefree polynomials and their idempotents

Choices are made with `Classical.epsilon`.


### `monicsOfDegree`

 The finite set of monic polynomials of degree r over the finite field k. 

### `faithfulChar`

 A chosen injective multiplicative character from the algebraic closure of `k` to `ℂ`
(arbitrary if there is none). For finite `k` one exists (`New.exists_injective_mulChar`), so the
chosen character is injective (the instance `New.faithfulChar_injective`). 

### `IsFaithfulMulChar`

 The field K is algebraically closed and the multiplicative character T : K → ℂ is injective,
so it embeds K^× in ℂ^×. 

### `IsFaithfulMulChar.injective`

 The character T is injective. 

### `thetaExponent`

 A chosen natural number `j` with `T x = exp (2πi / (Q - 1)) ^ j` (arbitrary if there is
none). 

### `apply_eq_exp_pow_thetaExponent`

 Let `T` be a multiplicative character `K → ℂ`. Suppose `2 ≤ Q` and `x` is a `(Q - 1)`-th root of
unity. Then `T x = exp (2πi / (Q - 1)) ^ thetaExponent T Q x`, where `thetaExponent T Q x` is a
chosen natural number `j` with `T x = exp (2πi / (Q - 1)) ^ j` (arbitrary if none exists). So such
an exponent exists. 

### `thetaChar`

 The character `θ_x = T ^ j` of `K`, where `j = thetaExponent T Q x`. 

### `chosenRoot`

 A chosen root of `P` in `K` (arbitrary if there is none). 

### `greenTau`

 Green's class function `τ_P`: `(-1) ^ d` times the rank `d` part of `greenCuspidal k θ_x`,
where `d = deg P`, `x = chosenRoot K P` and `θ_x` is formed with `Q = |k| ^ d`. 

### `labelChar`

 The multiplicative map c ↦ Ξ_c: the product, by parabolic induction, of τ_P over the monic
irreducible factors P of c with multiplicity; Ξ_0 = 0. 

### `IsLabel`

 `c` is a label of degree `r`: a monic squarefree polynomial over `k` of degree `r` with nonzero
constant term. 

### `detChar`

 The class function χ∘det on endomorphisms of every dimension, written through the constant
term of the characteristic polynomial. 

### `hyperplaneSum`

 For a vector `l : n → k`, the element ∑ χ(det h)⁻¹ h of ℂ[GL_n(k)], summed over the invertible
h of the form 1 + u lᵀ with u a column vector. 

### `labelIdem`

 The element e_c = ∑ (Ξ_c(1)/|G|)·conj Ξ_c(g)·g of ℂ[G], G = GL_n(k), Ξ_c formed with
`New.faithfulChar`, if c is a label of degree |n|; zero otherwise. 


## The characters θ_x and the name x_χ of a character of k^×

Fix a multiplicative character `T : K → ℂ`. For x with x^(Q−1) = 1, `thetaChar T Q x` is the
character θ_x = T^e, where T(x) = exp(2πi/(Q−1))^e.

* `New.thetaChar_apply_pow`: the key symmetry, θ_x(z^m) = (T^a)(x) when T(z) = exp(2πi/N)^a and
  N = (Q − 1)m ≠ 0. It gives `New.thetaChar_mul` (θ_{xy} = θ_x θ_y on (Q−1)-th roots of unity) and
  `New.thetaChar_eq_apply_norm_pow` (the change from Q to Q^r is composition with a norm).


### `exists_thetaChar_eq_pow`

 For `2 ≤ Q` and a `(Q - 1)`-th root of unity `x`, the character `thetaChar T Q x` is `T ^ e`
for an exponent `e` with `T x = exp (2πi / (Q - 1)) ^ e`. 

### `thetaChar_apply_pow`

 Let `T` be a multiplicative character of the field `K`, and let `θ_x = thetaChar T Q x` be the
character `T ^ j` of `K`, where `j = thetaExponent T Q x`.
Suppose `Q ≥ 2`, `N ≠ 0`, `N = (Q − 1)m` and `x^{Q−1} = 1`. If `z ∈ K`
satisfies `T(z) = exp(2πi/N)^a`, then `θ_x(z^m) = T(x)^a`. 

### `thetaChar_mul`

 Let Q ≥ 2 and let x, y, z in K satisfy x^(Q−1) = y^(Q−1) = z^(Q−1) = 1. Then
θ_{xy}(z) = θ_x(z)·θ_y(z), where all three characters are formed with Q. 

### `thetaChar_eq_apply_norm_pow`

 Change of Q. Let `T` be a multiplicative character of the field `K`, and let θ_x, formed with
Q, be the character T^j of `K` with j = `thetaExponent T Q x`.
Let Q ≥ 2, Q' = Q^r ≥ 2, x^(Q−1) = 1, y = x^a and z^(Q'−1) = 1. Then θ_y(z), formed with Q', equals
θ_x(z^(1 + Q + … + Q^(r−1)))^a, formed with Q; the power of z is its norm from the field with Q'
elements to the field with Q elements. 

### `eq_one_of_thetaChar_algebraMap_eq_one`

 Let `T` be faithful (`New.IsFaithfulMulChar`) and `a` a unit of the finite field `k`. If θ_a,
formed with Q = |k|, is trivial on the units of `k`, then `a = 1`. 

### `charName`

 For `T` faithful (`New.IsFaithfulMulChar`), the group isomorphism χ ↦ x_χ from the
multiplicative characters of `k` to `kˣ`, inverse to a ↦ θ_a restricted to `k`, with θ_a formed
with Q = |k|. 

### `charName_symm_apply`

 The inverse of `charName T` sends a unit `a` to the restriction of θ_a to `k`. 

### `thetaChar_charName`

 Let `T` be faithful (`K` algebraically closed, `T : K → ℂ` injective), and let θ_a = T^j
(j = `thetaExponent`) be formed with Q = |k|. Let x_χ = `charName T χ` ∈ kˣ be the element attached
to a multiplicative character χ of `k` by inverting the isomorphism a ↦ θ_a restricted to `k`. Then
θ_{x_χ}(y) = χ(y) for all y ∈ k, so every χ is the restriction of θ_{x_χ} to `k`. 


## Green's functions τ_P: cuspidality, orthonormality, independence of the root

Up to the sign `(-1)^d`, `τ_P` is the part of rank `d = deg P` of `New.Hall.greenCuspidal k θ_x`.
Here `x` is a chosen root of `P` in `K` and `Q = |k|^d`. `rankPart d` keeps rank `d`, and
`rankInner d` is the inner product on `GL_d(k)`.


### `labelChar_eq_greenTau`

 Let `T : K → ℂ` be any multiplicative character of a field `K` over the finite field `k`. For
`P` monic and irreducible over `k`, the label character `labelChar T P` (the parabolic-induction
product of Green's class functions over the monic irreducible factors) is the single function
`τ_P = greenTau T P`. 

### `isCuspidal_greenTau`

 Let `T` be any multiplicative character of the field `K` over `k`, and let P be any polynomial
over `k`, of degree d. Green's class function τ_P is (−1)^d times the rank d
part of `greenCuspidal k θ_x`, where x = `chosenRoot K P` and θ_x = T^j (j = `thetaExponent`) is
formed with Q = |k|^d. Then τ_P is cuspidal: its mean over block triangular matrices with given
diagonal blocks vanishes whenever both blocks have nonzero dimension.

This is the cuspidality assertion in the theorem of Green and Deligne–Lusztig on characters of GL_n
over a finite field attached to the Coxeter torus, for τ_P defined by Green's formula.
Irreducibility is not stated here. 

### `aroots_map_frobenius_pow`

 If the endomorphism σ of L is y ↦ y^(q^i) with q = |k|, then the roots of σP in the
algebraically closed field K are the q^i-th powers of the roots of P, with multiplicity. 

### `root_pow_card_pow_pred_eq_one`

 A root `x` of an irreducible `P` with `P(0) ≠ 0` is a `(Q - 1)`-th root of unity, where
`Q = |k| ^ deg P ≥ 2`. 

### `rankPart_greenCuspidal_pow`

 For `a ≠ 0`, in rank `deg P` (`rankPart` keeps the values on classes of dimension `deg P` and is
zero elsewhere), replacing the root `x` by `x ^ a` in `θ_x` has the same effect on
`New.Hall.greenCuspidal` as composing `θ_x` with the `a`-th power map. 

### `greenTau_eq`

 For irreducible `P` with `P.coeff 0 ≠ 0`, any root `x` of `P` may replace the chosen one in the
definition of `greenTau T P`.

This is a case of Green's independence of the cuspidal character from the chosen root, with the
class function defined by Green's formula rather than by Deligne–Lusztig induction. 

### `finMean_conj_mul_eq_ite`

 Orthogonality of the multiplicative characters of a finite field `L`: the mean over `Lˣ` of
`conj χ · ξ` is `1` if `χ = ξ` and `0` otherwise. 

### `aroots_charpoly_mulLeft`

 Let `L` be a finite extension of `k` with an embedding `φ` into `K`, and `q = |k|`. The roots in
`K` of the characteristic polynomial of multiplication by `u` on `L` are the conjugates
`φ(u) ^ q ^ i`, `i < [L : k]`. 

### `count_aroots_eq_ite`

 Let `x` be a root of a monic irreducible `P` and let `S` be monic irreducible. Then `x` is a
root of `S`, and then a simple one, exactly when `P = S`: its multiplicity among the roots of `S`
in `K` is `1` if `P = S` and `0` otherwise. 

### `rankInner_greenTau`

 Let `T` be a faithful multiplicative character of the algebraically closed field `K ⊇ k`
(`IsFaithfulMulChar`), and let `P` be monic irreducible with `P(0) ≠ 0`. Let `τ_P = greenTau T P` be
Green's class function: `(-1)^d` times the rank `d = deg P` part of `greenCuspidal k θ_x`, where `x`
is a chosen root of `P` in `K`. (a) For `S` monic irreducible with `S(0) ≠ 0`, the inner product of
`τ_P` and `τ_S` on `GL_{deg P}(k)` (the mean over the group of conj τ_P · τ_S) is `1` if `P = S` and
`0` otherwise. (b) If `P(1) ≠ 0`, then `New.Hall.skew` of `τ_P` against the constant function `1` in
rank `deg P` vanishes: for every class `a`, the average over `b ∈ GL_{deg P}(k)` of conj `τ_P(b)`
times the block average of `1` at `(a, b)` is zero. Here `1` is `constOne`, and its block average is
its mean over block triangular matrices with diagonal blocks `a`, `b`. 


## Lower bound for the degrees of Green's characters

Idea: pair with the indicator function of the identity maps times `moebius`. Each factor
`New.greenTau T P` multiplies the pairing by `(-1) ^ d / (q ^ d - 1)`, with `d = deg P` and
`q = |k|`, by `mulMoebius_greenCuspidal_one_mul`.


### `IsLabel.induction_irreducible_mul`

 Induction on labels: start from `1` and multiply by monic irreducible polynomials other than
`X`. 

### `IsLabel.map`

 A label stays a label over an extension field, as a finite field is perfect. 

### `_root_.sub_mul_pow_mul_prod_le_mul_prod`

 For a real number q > 1 and m : ℕ, (q - m) q^m ∏_{i<m} q^i ≤ q ∏_{i<m} (q^(i+1) - 1). Divided by
q^(m+1) ∏_{i<m} q^i, this says that ∏_{i<m} (1 - q^(-(i+1))) is at least 1 - m/q. 

### `powerBasisOne`

 The power basis of `k` over itself with generator `1`. 

### `identityIndicator`

 The indicator function of the classes of identity maps, in every dimension: for a class `c`,
`c.out.2` is a chosen endomorphism in it. 

### `mulMoebius_greenCuspidal_one_mul`

 The pointwise product `mulMoebius` with `moebius` of Green's cuspidal function
`greenCuspidal k η` at the identity of `Fin d → k`, times `q ^ d - 1` with `q = |k|`, is `η 1` times
the order of `GL_d(k)`. This is `mulMoebius_greenCuspidal_lsmul` at the generator `1`. 

### `rankInner_greenTau_mul_mulMoebius`

 Let `δ` be the indicator function of the identity classes and `q = |k|`. Pairing with
`δ.mulMoebius`, a factor `τ_P` of degree `d = deg P` in front of `F` multiplies the pairing by
`(-1) ^ d / (q ^ d - 1)`. 

### `exists_le_rankInner_labelChar_mul_eq`

 Let `c` be a label of degree `r`, `q = |k|` and `δ` the indicator function of the identity
classes. There is a natural number `B ≤ q ^ r` such that the pairing of `labelChar T c` with
`δ.mulMoebius` in rank `r`, times `B`, is `(-1) ^ r`. 

### `labelChar_degree_bounds`

 Let `T` be a faithful multiplicative character of the algebraically closed field `K ⊇ k`
(`IsFaithfulMulChar`), and let `c` be a label of degree `r = card n`, i.e. a monic squarefree
polynomial over `k` of degree `r` with nonzero constant term. Let `q = |k|`, and let
`Ξ = labelChar T c` be the class function on `GL n k` obtained by parabolic induction from the
product of Green's functions `τ_P` over the monic irreducible factors `P` of `c`. (a) The real part
of `Ξ(1)` is non-negative. (b) `Ξ(1) conj Ξ(1) / |GL n k|` is at least `(1 - r / q) / q ^ r` in the
order of `ℂ`, so it is a real number. These bounds are consequences of the degree formula of Green
and Deligne–Lusztig for the characters attached to labels; the exact degree is not stated here. 
