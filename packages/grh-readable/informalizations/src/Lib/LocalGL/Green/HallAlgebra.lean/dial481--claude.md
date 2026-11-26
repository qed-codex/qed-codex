---
{
  "module": "src/Lib/LocalGL/Green/HallAlgebra.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/HallAlgebra.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/HallAlgebra.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hall algebra of class functions: induction product, Mackey formula, Frobenius reciprocity

`New.Hall k` is the space of complex-valued functions on similarity classes of square matrices of
all sizes over a field `k`. For finite `k` it is a commutative ℂ-algebra in which the constant
function `New.Hall.constOne` is invertible. From here on `k` is finite. Let δ denote the block
average `New.Hall.blockAverage` over block triangular matrices. Then δ is multiplicative (Mackey's
formula) and adjoint to the induction product. This yields the adjoint `New.Hall.skew` of
multiplication, a derivation for cuspidal functions, and Frobenius reciprocity along parabolic
subgroups.

## Main definitions and results

* `New.Hall k`: complex-valued functions on `New.SimClass k`. The product is
  `(f * h) g = ∑ W, f (g | W) * h (g | V / W)` over stable `W` (a `finsum`), and `1` is the
  indicator of size `0`. The constant function with value `1` is `New.Hall.constOne`.
* `New.Hall.blockAverage`, `New.Hall.IsCuspidal`: the average over block triangular maps;
  cuspidality.
* `New.Hall.blockAverage_mul`: Mackey's formula, `δ(F * H) = δF * δH`, by a bijection between the
  stable subspaces of the block maps and triples (pair of stable subspaces, map, shear).
* `New.Hall.rankInner_mul_eq_rankInner_skew`: for `f` supported in dimension `d`,
  `New.Hall.skew d f` is adjoint to multiplication by `f`.
* `New.Hall.skew_mul`: for cuspidal `c` and `d ≠ 0`, `New.Hall.skew d c` is a derivation. It follows
  from Mackey's formula `New.Hall.blockAverage_mul` and the degree-zero case
  `New.Hall.rankInner_mul_of_isCuspidal`.
* `New.classInner_evalGL_prod`: the inner product `New.classInner` of a product with a class
  function `Y` is a mean over the group `New.parabolic b` of matrices that are block upper
  triangular for the levels `b : n → ι`; `New.blockHom b a` is the diagonal block of level `a`.

Notions from other files:
* `New.finMean`: the average of a complex function `f` on a finite set `G`: the sum of its values
  divided by the cardinality of `G`.
* `New.classInner f h`: the average over a finite group of `conj (f g) * h g`.

## Relation to the literature

Known; see `Lib.LocalGL.Green.TauFunctions` and `Lib.LocalGL.Green.CuspidalFunctions` for sources.



## Similarity classes of matrices and the induction product

* `New.SimClass k`: similarity classes of square matrices of any size, invertible or not.
  `New.simClassOf g` is the class of an endomorphism `g`, and `New.SimClass.dim` and
  `New.SimClass.charpoly` give its size and characteristic polynomial. The size does not depend on
  the representative (`New.SimClass.dim_mk`).


### `SimClass`

 Similarity classes of square matrices over k of all sizes: pairs (n, endomorphism of kⁿ)
modulo intertwining by linear isomorphisms. 

### `Hall`

 The complex-valued functions on similarity classes of square matrices over k of all sizes; the
product is parabolic induction (sum over stable subspaces). 

 ### The class of an endomorphism; stable subspaces 

### `simClassOf`

 The similarity class of an endomorphism g of a finite-dimensional k-vector space V, obtained
by choosing a basis of V. 

### `StableSubspace`

 The subspaces W of V that are stable under the endomorphism g. 

### `StableSubspace.endOnSub`

 The endomorphism of a g-stable subspace W obtained by restricting g. 

### `StableSubspace.endOnQuot`

 The endomorphism of the quotient of V by a g-stable subspace W induced by g. 

### `SimClass.dim`

 The dimension `n` of the space `k ^ n` on which the chosen representative of the class `c` acts.


### `SimClass.dim_mk`

 The class of an endomorphism of `k ^ n` has dimension `n`, whichever representative is
chosen. 

### `SimClass.charpoly`

 The function sending the similarity class of a k-linear endomorphism of k^n to its
characteristic polynomial in k[X]. 

### `instance : Mul (Hall k)`

 The induction product: `(f * h) c` is the sum, over the subspaces `W` stable under the chosen
representative of `c`, of `f` at its class on `W` times `h` at its class on the quotient by `W`. 

 ### Particular class functions 

### `Hall.constOne`

 The complex-valued function on classes of endomorphisms that takes the value 1 on every class,
in every dimension. 

### `Hall.rankPart`

 The function on similarity classes equal to F on classes of dimension n and zero on the
others. 

### `instance : One (Hall k)`

 The unit of the induction product: the function that is `1` on the classes of dimension `0`
and `0` elsewhere. 

### `Hall.evalGL`

 For a complex function F on similarity classes and an invertible matrix g in `GL n k`, indexed
by a finite type n, the value of F at the class of the endomorphism of `n → k` given by g. 


## The commutative ring of class functions and invertibility of the constant function

* `New.simClassOf_eq_dualMap`: an endomorphism is similar to its transpose; this gives
  commutativity.


 ### Similarity classes and stable subspaces 

### `simClassOf_eq_iff`

 Two endomorphisms `g` and `g'` have the same similarity class if and only if a linear
isomorphism intertwines them. 

### `exists_equiv_simClassOf_out`

 The chosen representative of the class of `g`, an endomorphism of `k^d` with `d` the dimension
of `V`, is conjugate to `g` by a linear isomorphism `e : k^d ≃ V`. 

 ### Values of sums and products 

### `Hall.ext`

 Two class functions are equal once they agree at the class of every endomorphism of every
`k^n`. 

### `Hall.mul_apply`

 The value of the induction product `f * h` at a class `c`, as in its definition. Let g be the
chosen representative of `c`. The value is the finite sum, over the g-stable subspaces W, of `f` at
the class of the restriction of g to W times `h` at the class of the map g induces on the quotient
by W. 

### `Hall.mul_apply_eq_zero_of_dim_lt`

 If `f` vanishes in dimensions below `m` and `h` in dimensions below `n`, then the induction
product `f * h` vanishes in dimensions below `m + n`. 

### `blockTriangularEnd`

 The block triangular endomorphism `(w, v) ↦ (b w, x w + a v)` of `V' × V`. 

### `fintypeStableSubspace`

 For finite `k`, an endomorphism of a finite-dimensional space has finitely many stable
subspaces. 

### `fintypeLinearHom`

 For finite k, there are finitely many linear maps between two finite-dimensional spaces. 

### `simClassOf_endOnQuot`

 If `p` is surjective with kernel `W` and intertwines `g` and `g'`, then `g` on `V / W` has the
class of `g'`. 

### `simClassOf_endOnSub`

 If `p` is injective with image `U` and intertwines `g` and `g'`, then `g'` on `U` has the class
of `g`. 

### `StableSubspace.comap`

 For a `k`-linear map `p` intertwining `g` and `g'`, the preimage `p⁻¹(U)` of a `g'`-stable
subspace `U`, as a `g`-stable subspace. 

### `simClassOf_endOnSub_comap`

 For injective `p` intertwining `g` and `g'` and `U` in the image of `p`, `g` on `p⁻¹(U)` has
the class of `g'` on `U`. 

### `StableSubspace.sum_comap`

 For `p` intertwining `g` and `g'`, the sum of `F` over the `g`-stable subspaces containing
`ker p` equals the sum of `F (p⁻¹ W)` over the `g'`-stable subspaces `W` contained in the image of
`p`. 

### `simClassOf_endOnQuot_comap`

 For surjective `p` intertwining `g` and `g'`, `g` on `V / p⁻¹(U)` has the class of `g'` on
`V' / U`. 

### `Hall.mul_simClassOf`

 The product f * h at the class of an endomorphism g is the sum, over the g-stable subspaces
W, of f at g on W times h at g on V/W. 

### `exists_nondegenerate_mul_form`

 For a finite field `k`, a finite-dimensional quotient `A` of `k[X]` carries a linear form `L`
for which the pairing `(x, y) ↦ L (x * y)` is nondegenerate. 

### `simClassOf_eq_dualMap`

 Every endomorphism of a finite-dimensional space over a finite field is similar to its
transpose. 

### `instance : CommRing (Hall k)`

 For finite `k`, the induction product makes the class functions a commutative ring. 

 ### The constant function 1 is a unit 

### `Hall.one_sub_constOne_pow_apply_eq_zero`

 The m-th power of 1 − 𝟙, where 1 is the unit and 𝟙 the constant function, vanishes in
dimensions below m. 

### `instance : Algebra ℂ (Hall k)`

 The class functions form a `ℂ`-algebra: scalars act pointwise. 

### `Hall.isUnit_constOne`

 Over a finite field `k`, the constant function `𝟙` on similarity classes of square matrices of
all sizes is invertible for the induction product. 


## Block averages, cuspidality and inner products

* `New.Hall.rankInner`, `New.Hall.skew`: the inner product in rank `n`, and the inner product of `F`
  with the block average of `H` in the second class.
* `New.Hall.brauerLift`, `New.Hall.mulMoebius`, `New.Hall.greenCuspidal`: the sum `β_η` of `η` over
  the eigenvalues, and the function `(β_η · μ) * constOne`, where μ = `New.Hall.moebius` is the
  inverse of `New.Hall.constOne`.


### `blockAverage`

 For F on similarity classes, the function of two classes a, b averaging F over block upper
triangular endomorphisms with diagonal blocks a, b and arbitrary off-diagonal block. 

### `moebius`

 The inverse μ of the constant function `New.Hall.constOne` for the induction product. 

### `mulMoebius`

 The pointwise product F·μ, where μ is the inverse, for the parabolic-induction product, of
the constant class function 1. 

### `IsCuspidal`

 F is cuspidal: its average over block triangular endomorphisms with diagonal blocks a, b
vanishes whenever both a and b have nonzero dimension. 

### `rankInner`

 For n and complex functions F, H on similarity classes, the average over GL_n(k) of the
conjugate of F times H. 

### `skew`

 The function sending a class a to the average over b in GL_n(k) of conj F(b) times the block
average `New.Hall.blockAverage` of H at (a, b). 

### `brauerLift`

 The class function β_η sending an endomorphism to the sum of η over the roots in K of its
characteristic polynomial, counted with multiplicity. 

### `greenCuspidal`

 The class function C_η = (β_η·μ) ∗ 𝟙: the pointwise product of the eigenvalue sum β_η with
the inverse μ of 𝟙, multiplied in the induction product by the constant function 𝟙. 

 ## Mackey's formula for block averages 

### `blockAverage_simClassOf`

 The block average of `F` at the classes of `a` and `b` is the average of `F` over the block maps
`New.blockTriangularEnd a b x`, the map `(w, v) ↦ (b w, x w + a v)` of `W × V` for `x : W →ₗ[k] V`,
for these representatives `a`, `b` rather than the chosen ones. 

### `exists_restrict_eq_and_mapQ_eq`

 Any maps `B → A` and `W ⧸ B → V ⧸ A` are induced by one map `W → V` that takes `B` into `A`. 

### `sum_blockAverage_mul_blockAverage_eq`

 The right side of Mackey's formula written out: a sum over the pairs `P = (A, B)` of stable
subspaces of `a` and `b` of the mean, over the maps `B → A` and `W ⧸ B → V ⧸ A`, of `F` at the block
map `blockTriangularEnd` on `B × A` of the restrictions `endOnSub` of `a`, `b`, times `H` at the
block map on the quotients of the induced maps `endOnQuot`. 

### `blockAverage_mul`

 Mackey formula for the block averaging map δ = `New.Hall.blockAverage`, where δF(x, y) averages
`F` over block upper triangular endomorphisms with diagonal blocks x, y and arbitrary off-diagonal
block. The claim is that δ(F * H) at the classes of `a` and `b` equals a sum over the `a`-stable
subspaces `A`, with `A.endOnSub` and `A.endOnQuot` the maps `a` induces on `A` and on `V ⧸ A`. Each
term is the Hall product of the functions δF(class of `A.endOnSub`, ·) and δH(class of
`A.endOnQuot`, ·), taken in the second variable and evaluated at the class of `b`. 

### `blockAverage_of_dim_eq_zero`

 If the class `o` has dimension `0`, the block average of `F` at `(o, a)` and at `(a, o)` is
`F a`. 

### `charpoly_endOnSub_mul_endOnQuot`

 For an `a`-stable subspace `U`, the characteristic polynomial of `a` is the product of those of
its restriction to `U` and of the induced map on `V ⧸ U`. 


## Block averages as adjoint of the induction product

* `New.Hall.rankInner_eq_classInner_simClassOf`, `New.Hall.classInner_evalGL`: inner products over
  the automorphisms of any `V`, or over `GL ι k`, depend only on the dimension.


### `simClassOf_out_eq_one_iff`

 The chosen representative of the class of `a` is the identity if and only if `a` is. 

### `rankInner_eq_classInner_simClassOf`

 The pairing `New.Hall.rankInner` in rank `dim V` is the mean over the automorphisms of `V`. 

### `classInner_evalGL`

 For class functions F, H on matrices over the finite field k, the average over GL_ι(k) of
conj F(g) · H(g) is the inner product `New.Hall.rankInner` of F and H in rank |ι|. 

### `rankInner_mul_eq_sum_skew`

 `Hall k` is the space of complex functions on similarity classes of matrices over the finite
field k, with product given by parabolic induction. In it, `rankInner n (A * B) X`, the
GL_n(k)-average of conj(A * B)·X, equals ∑_{p+q=n} `rankInner p A (skew q B X)`. Here `skew q B X`
sends a class a to the GL_q(k)-average over b of conj B(b) times the block average of X at (a,
b). 


## Adjoint of multiplication by a class function

* `New.Hall.skew_of_isCuspidal`: for cuspidal `c` and `d ≠ 0`, `New.Hall.skew d f c` is the scalar
  `New.Hall.rankInner d f c` times the unit.


### `rankInner_mul_eq_rankInner_skew`

 Here `rankInner m F₁ F₂` is the average over g ∈ GL_m(k) of conj F₁(g)·F₂(g), and `skew d f F`
sends a class a to the average over b ∈ GL_d(k) of conj f(b) times the block average
(`New.Hall.blockAverage`) of `F` at (a, b). Adjunction: if `f` vanishes on the classes of dimension
other than `d`, then `rankInner (d + n) (f * H) F = rankInner n H (skew d f F)`, where `*` is the
parabolic induction product. 

### `eq_simClassOf_zero_of_dim_eq_zero`

 The only class of dimension `0` is that of the zero map of the zero space. 

### `rankInner_mul_of_isCuspidal`

 For cuspidal `c` and `d ≠ 0`, the pairing with `c` in degree `d` satisfies the Leibniz rule, the
other factor being evaluated at the zero space (`New.Hall.rankInner 0`). 

### `skew_of_isCuspidal`

 Take `c` cuspidal in the sense of `New.Hall.IsCuspidal` and `d ≠ 0`. Let `skew d f c` be the
function x ↦ average over y in GL_d(k) of conj f(y) · δc(x, y), with δ the block average
`New.Hall.blockAverage`. Then `skew d f c` equals the unit `1` of the Hall algebra times
`rankInner d f c`, the average over GL_d(k) of conj f · c. 

### `skew_mul`

 `skew d c` is the map sending `F` to the function x ↦ average over y in GL_d(k) of conj
c(y) · δF(x, y), with δ the block average `New.Hall.blockAverage`. For `c` cuspidal in the sense of
`New.Hall.IsCuspidal` and `d ≠ 0`, this map is a derivation of the Hall algebra:
`skew d c (F * H) = skew d c F * H + F * skew d c H`.

This is the derivation property of the adjoint of multiplication by a cuspidal element, from
Zelevinsky's PSH-algebra structure on class functions of finite general linear groups; only the
Leibniz rule is stated. 


## Frobenius reciprocity along parabolic subgroups

The proof removes the largest level and uses the adjunction
`New.Hall.rankInner_mul_eq_rankInner_skew`.


### `simClassOf_submatrix`

 Reindexing the rows and columns of a matrix by one bijection does not change its similarity
class. 

### `exists_eq_evalGL`

 A function on `GL n k` that is invariant under conjugation is the restriction of a function on
similarity classes. 

### `classInner_evalGL_prod`

 **Frobenius reciprocity.** Let `k` be a finite field. Each `F a` is a complex function on
similarity classes of square matrices over `k` of all sizes, in `Hall k`, whose product is parabolic
induction. Let `s` contain all levels `b i` and let `Y` be a class function on `GL n k`. Restrict
each `F a`, `a ∈ s`, to classes of the size of the block of level `a`, and take the product. The
mean over `GL n k` of conj of this product times `Y` equals the mean over block upper triangular `g`
of `conj (∏ a ∈ s, F a (g_a)) * Y g`. Here `g_a` is the diagonal block of level `a`. 
