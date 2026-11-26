---
{
  "module": "src/Lib/General/LinearAlgebra/IntegralLattices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/IntegralLattices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/IntegralLattices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral matrices over subrings: Smith normal form, Gelfand's condition and lattices

This file studies matrices over a commutative ring `A` that are integral with respect to a subring
`R`. The model is the ring of integral adeles inside the finite adeles. `New.IsIntMatrix R M` says
that all entries of `M` lie in `R`. The property `New.IsValuationPair R` says that of two elements
of `A` one divides the other over `R`, piece by piece along an idempotent of `R`. The file also
defines column lattices and indices of lattices, and studies principal congruence subgroups of
unitary groups.

## Main definitions and results

* `New.IsValuationPair.smith_normal_form`: a square matrix over `A` is diagonalized by row and
  column operations over a subring `R` that satisfies `New.IsValuationPair`.
* `New.exists_invTransposeGL_inv_eq`: for such a subring `O` of `R`, `gᵀ` lies in the double coset
  `GL n O * g * GL n O`.
* `New.IsHeckeFunction.heckeFun_adjoint`, `New.IsHeckeFunction.heckeFun_comm`: adjoints and
  commutativity of Hecke operators for `K = GL n O`, with `O` a valuation subring of a field.
* `New.submoduleIndex`, `New.denomIndex`: the relative index of two `R`-modules, and the index of
  the denominator of `a`. An infinite index is read as `0`.
* `New.colLattice`, `New.preimageLattice`: the span of the columns of `M`, and the vectors `M` makes
  integral.
* `New.unitaryLevel`: the principal congruence subgroup of the unitary group `New.U J`.

Notions from other files:
* `New.intGL n O`: for a subring `O` of `R`, the subgroup of `GL n R` of matrices that have,
  together with their inverse, all entries in `O`.
* `New.U J`: the unitary group of `J`, the `g` in `GL n R` with `gᴴ * J * g = J`.
* `New.heckeFun π K f`: the operator `∑ f g • π g`, summed over chosen representatives `g` of
  `G ⧸ K` (zero if infinitely many terms are nonzero).
* `New.IsHeckeFunction K f`: `f` is left and right `K`-invariant and supported on finitely many
  cosets `g K`.
* `New.levelSpace π K`: the vectors of the representation `π` that are fixed by `K`.

## Relation to the literature

Known result: Commutativity of the spherical Hecke algebra of GL_n. This file proves the case that
is used, by Gelfand's trick: over a valuation subring of a field the Hecke operators commute on
fixed vectors of a representation. Source: J. Tits, Reductive groups over local fields, Corvallis
1979, 3.3.3; T. Tamagawa, On the zeta functions of a division algebra, Ann. Math. 77 (1963).

Part of a known result: the valuation pairs and integral matrices of this file are groundwork for
Witt's extension theorem for unimodular hermitian lattices and for the Iwasawa decomposition (see
`Lib.Adelic.Witt.IwasawaDecomposition`).



## Generalised inverses and matrix factorisations over a field

* `New.exists_mul_add_mul_eq_one`: if the kernel of `x` lies in the column space of `y`, then
  `y * e + b * x = 1` for some matrices `e` and `b`.

`x.mulVecLin.range` is the column space of `x`.


### `New.exists_generalized_inverse`

 Let `f` be a linear map between vector spaces over a field. Then `f` has a generalised inverse:
a linear map `s` with f(s(f x)) = f x for all x. 

### `New.Filling.exists_mul_eq_of_col_mem_range`

 Let `x` and `y` be matrices over a field. If every column of `y` lies in the column space of
`x`, then y = x * s for some matrix s. 

### `New.exists_mul_add_mul_eq_one`

 Let `x` and `y` be matrices over a field. If the kernel of `x` lies in the column space of `y`,
then `y * e + b * x = 1` for some matrices `e` and `b`. 


## Valuation pairs and cutting along idempotents

Cutting along an idempotent `e` of `A` replaces a matrix `g` by `e g + (1 - e)`.


### `IsValuationPair`

 For all `a b : A` there is an idempotent `e` of `R` such that `a` and `b` are `R`-multiples of
`(1 - e) a + e b`. For a valuation ring take `e = 0` or `e = 1`. 

### `isValuationPair_valuationSubring`

 A valuation subring `O` of a field `F` satisfies `New.IsValuationPair`: of two elements of `F`
one is an `O`-multiple of the other. 

### `IsValuationPair.top`

 If `R ⊆ A` satisfies `New.IsValuationPair`, so does `R` as a subring of itself. 

### `cutGL`

 For an idempotent e of the commutative ring A, the endomorphism g ↦ e·g + (1−e)·1 of GL_n(A). 

### `val_mul_cutGL_inv_mul`

 Cutting patches two invertible matrices `c` and `d` to the invertible matrix
`e • d + (1 - e) • c`. 

### `U.cutAt`

 For a self-adjoint idempotent e of A, the endomorphism g ↦ e·g + (1−e)·1 of the unitary group of
the identity form, the g in GL_n(A) with gᴴg = 1. 

 ## Smith normal form over valuation pairs 

### `New.IsValuationPair.directed_span_pivot`

 Let `R ⊆ A` satisfy `New.IsValuationPair`. As `a`, `b` run through the invertible matrices over
`R`, the `R`-modules generated by the `(p, p)` entry of `a * y * b` form a directed family. 

### `New.IsValuationPair.exists_pivot_dvd`

 Existence of a pivot: if `R ⊆ A` satisfies `New.IsValuationPair`, then for suitable invertible
matrices `a`, `b` over `R` every entry of `a * y * b` is an `R`-multiple of its `(p, p)` entry. 

### `New.exists_eq_mul_diagonal_mul_of_pivot_dvd`

 One elimination step. Let every entry `M i j` be the multiple `w i j * M p p` of the pivot, with
`w i j` in the subring `R`. Subtract `w i p` times row `p` from each row `i`. If the block of the
result away from `p` is diagonalized by invertible matrices over `R`, then so is `M`. 

### `New.IsValuationPair.smith_normal_form`

 Smith normal form: if the subring `R` of `A` satisfies `New.IsValuationPair`, every square
matrix `y` over `A` is `k * diagonal d * k'`, where `d : n → A` and `k`, `k'` and their inverses
have entries in `R`. No divisibility among the entries of `d` is stated. 


## The inverse transpose and Gelfand's condition for GL_n at a place

The automorphism `g ↦ (gᵀ)⁻¹` of `GL n R`, written `transposeGL g⁻¹` (here `transposeGL g` is the
transpose `gᵀ` as an element of `GL n R`), preserves `GL n O`. When `O` satisfies
`New.IsValuationPair`, it sends `g⁻¹` into the double coset `GL n O * g * GL n O`. This is Gelfand's
condition for `K = GL n O`, where `O` is a valuation subring of a field.


### `invTransposeGL`

 The automorphism g ↦ (gᵀ)⁻¹ of the group GL_n(R). 

### `exists_invTransposeGL_inv_eq`

 If `O ⊆ R` satisfies `New.IsValuationPair`, the transpose `invTransposeGL g⁻¹` of any
`g ∈ GL n R` is `(kᵀ)⁻¹ * g * k` for some `k` in the subgroup `intGL n O` of integral points. 

 ### Gelfand's trick 

### `IsHeckeFunction.heckeFun_adjoint`

 The adjoint of `f` is `g ↦ σ (f g⁻¹)`. Let `O` be a valuation subring of a field `F` and
`K = GL n O` in `GL n F`. Let `π`, `π'` be representations of `GL n F` over a commutative semiring
`A` on `W`, `W'`. For `f : GL n F → A`, `heckeFun π K f` is the operator `∑ f g • π g` over
representatives `g` of the cosets `g K`. Let `f` be left and right `K`-invariant and supported on
finitely many cosets `g K`. Let `B` be a `GL n F`-invariant pairing of `W` with `W'` that is
`σ`-semilinear in the first argument and linear in the second, and let `v`, `v'` be vectors fixed by
`K`. Then (a) `g ↦ σ (f g⁻¹)` is again left and right `K`-invariant and supported on finitely many
cosets, and (b) `B (heckeFun π K f v) v' = B v (heckeFun π' K (g ↦ σ (f g⁻¹)) v')`. 

### `IsHeckeFunction.apply_invTransposeGL_inv`

 Let `O` be a valuation subring of a field `F`. A function `f` on `GL n F` that is left and right
invariant under `K = GL n O` and supported on finitely many cosets `g K` takes the same value at `g`
and at its transpose `invTransposeGL g⁻¹`. 

### `IsHeckeFunction.heckeFun_heckeFun_eq_finsum`

 Let `K` be a subgroup of `GL n F`, let `f`, `f'` be left and right `K`-invariant and supported
on finitely many cosets `g K`, and let `v` be fixed by `K` in the representation `π`. The operator
of `f'` applied after the operator of `f` acts on `v` as the operator of the convolution
`x ↦ ∑ f' q * f (q⁻¹ * x)`, here written as a sum over representatives `q` of all cosets. 

### `IsHeckeFunction.heckeFun_comm`

 Gelfand's trick. Let `O` be a valuation subring of a field `F`, `K = GL n O` in `GL n F`, and
`π` a representation of `GL n F` over a commutative semiring `A` on `W`. For `f : GL n F → A`,
`heckeFun π K f` is the operator `∑ f g • π g` over representatives `g` of the cosets `g K`. If `f`
and `f'` are left and right `K`-invariant and each is supported on finitely many cosets `g K`, then
their operators commute on every vector `v` fixed by `K`.

This is the commutativity of the spherical Hecke algebra (Gelfand, Satake) for `GL n` and
`K = GL n O`, stated for its action on `K`-fixed vectors. 


## Lattices over adelic pairs: indices, column lattices, unitary levels

* `New.IsAdelic`: the properties of `Ô ⊂ 𝔸f` that are used, as a class on `R ⊂ A`.


 ### Integral vectors and matrices 

### `intVectors`

 The R-module R^n of vectors in A^n with all entries in R. 

### `IsIntMatrix`

 All entries of the matrix M lie in R. 

### `submoduleIndex`

 The index of M ∩ M' in M', as additive groups (0 if infinite). 

### `Filling.mem_span_unit_iff`

 Let `R` be a subring of the commutative ring `A` and `g` a unit of `A`. An element `x` of `A` is
an `R`-multiple of `g` if and only if `g⁻¹ * x` lies in `R`. 

### `IsStarStable`

 The subring R is stable under the involution of A. 

### `IsStarStable.star_mem`

 The conjugate of an element of `R` lies in `R`. 

 ### Adelic pairs, indices, lattices and levels 

### `IsAdelic`

 The properties of the pair Ô ⊂ 𝔸_f abstracted to R ⊂ A: R is open, compact and stable under
conjugation, locally a valuation ring, contains a skew element i with −i·i = 1 and an element of
trace 1, and −1 is a norm from R. 

### `IsAdelic.isOpen_isCompact`

 `R` is open and compact in `A`. 

### `IsAdelic.isValuationPair`

 Any two elements `a`, `b` of `A` are `R`-multiples of `(1 - e) * a + e * b` for some
  idempotent `e` of `R`, as in a product of valuation rings. 

### `IsAdelic.exists_skew_unit`

 Some `i ∈ R` has `-i * i = 1` and `star i = -i`, and some `τ ∈ R` has `τ + star τ = 1`. 

### `IsAdelic.exists_norm_neg_one`

 `-1` is the norm `star c * c` of some `c ∈ R`. 

### `denomIndex`

 The denominator of a: the index in R of the additive subgroup of the r ∈ R with ar ∈ R
(0 if infinite). 

### `colLattice`

 The R-module spanned by the columns of M. 

### `preimageLattice`

 The R-module of vectors v over A such that Mv has entries in R. 

### `unitaryLevel`

 The subgroup of the unitary group U(J) over A of elements lying in GL_n(R) and congruent to
1 modulo the unit g of A, that is, with g⁻¹(k − 1) integral. 

### `IsUnimodular`

 The property of a square matrix T over A that it is hermitian and lies in GL_n(R). 

### `Floors.IsHermitianUnit`

 The matrix J is hermitian and invertible. 

### `Floors.IsHermitianUnit.conjTranspose_eq`

 `J` is hermitian. 

### `Floors.IsHermitianUnit.isUnit`

 `J` is invertible. 


## Integral matrices, congruence subgroups of U(J), unimodular forms

`New.unitaryLevel R u J` is the group of integral isometries of `J` congruent to `1` modulo `u`. A
shape `𝔰` gives a number `ϱ` of hyperbolic planes and the index set of a middle space. For a Gram
matrix `T : 𝔰.Form A` of the middle space, `T.splitGram` is the Gram matrix of its orthogonal sum
with the `ϱ` planes.

* `New.IsUnimodular.mem_unitaryLevel`: let `J` be unimodular, let `R` be stable under the
  involution, and let `u` lie in `R`. Then the congruence alone gives membership in the level.


### `mulVec_mem_intVectors_iff`

 For `k` in GL_n(R), the vector `k w` has entries in `R` if and only if `w` has. 

### `IsIntMatrix.conjTranspose`

 If `R` is stable under the involution, the conjugate transpose of a matrix with entries in `R`
has entries in `R`. 

### `mem_unitaryLevel_def`

 An isometry `x` of `J` lies in the principal congruence subgroup of level `u` if and only if
`x` lies in GL_n(R) and `u⁻¹ (x - 1)` has entries in `R`. 

### `conj_mem_unitaryLevel`

 The integral points of U(J), the level `1`, normalise the principal congruence subgroup of U(J)
of level u. 

### `mem_besselU`

 Let `T.G` be the unitary group of `T.splitGram`, the Gram matrix `T` of a middle space with `ϱ`
hyperbolic planes added. Its basis indices (`SplitIndex`) are `ϱ` first, the middle and `ϱ` last
indices, graded by the natural number `level`. An element `x` lies in the Bessel unipotent group
`T.besselU` if and only if its entries `(i, j)` with `level j ≤ level i` are those of the identity
matrix. 

### `splitGram_mul_splitGram_eq_one`

 Adding `ϱ` hyperbolic planes respects inverses: if `T'` is a right inverse of `T`, then
`T'.splitGram` is a right inverse of `T.splitGram`. 

### `IsIntMatrix.isInt_splitGram`

 If the Gram matrix `T` of the middle space has entries in `R`, then so has the Gram matrix
`T.splitGram` with `ϱ` hyperbolic planes added: its entries are `0`, `1` or entries of `T`. 

 ### Congruence subgroups and unimodular forms 

### `unitaryLevel_one`

 The principal congruence subgroup of level `1` is the group of isometries of `J` in GL_n(R). 

### `isUnit_det_and_isIntMatrix_inv`

 A unimodular matrix (hermitian and in GL_n(R)) has a unit as determinant, and its inverse has
entries in `R`. 

### `mem_unitaryLevel`

 Let J be unimodular (hermitian and in GL_n(R)) over a conjugation-stable subring R, and let
u ∈ R be a unit of A. An isometry x of J with u⁻¹(x − 1) integral lies in the principal congruence
subgroup of level u. 

### `splitGram`

 If the Gram matrix T of the middle space is unimodular (hermitian and invertible over the
subring R), then so is the Gram matrix `T.splitGram` of the space obtained by adding ϱ hyperbolic
planes. 


## Functions of integral matrices and column lattices

* `New.liftIntegralFn`: a function of matrices over `B`, pulled back along `π : R → B` to integral
  matrices over `A` and extended by zero.
* `New.liftIntegralFn_mul`: multiplying the argument on both sides by invertible matrices over `R`
  corresponds to multiplying the argument of the function by their images under `π`.


### `liftIntegralFn`

 For π : R → B, the ℂ-linear map sending a function f on matrices over B to the function on
matrices S over A that is f(πS) for S integral, else 0. 

### `liftIntegralFn_map_subtype`

 The lift of `f` along `π` takes the value `f (π M₀)` at a matrix `M₀` over `R`, viewed as a
matrix over `A`. 

### `liftIntegralFn_of_not_isIntMatrix`

 The lift of `f` along `π` vanishes at a matrix with an entry outside `R`. 

### `isOpen_intVectors`

 If `R` is open in `A`, then `Rⁿ` is open in `Aⁿ` for the product topology. 

### `colLattice_le`

 The `R`-span of the columns of `M` lies in every `R`-module that contains the columns. 

### `IsIntMatrix.of_intGL_mul_mul`

 If `b M a` has entries in `R` for some `a` in GL_n(R) and `b` in GL_m(R), then so has
`M = b⁻¹ (b M a) a⁻¹`. 

### `liftIntegralFn_mul`

 For a ring homomorphism π : R → B, a ∈ GL_n(R), b ∈ GL_m(R) and an m × n matrix M over A, the
value of `New.liftIntegralFn` π f (the function that is f(πS) at integral S, else 0) at bMa equals
the value at M of the lift of S ↦ f(π(b)Sπ(a)). 


## A duality step for common vectors of two flags

`New.exists_mulVec_eq_of_annihilator`: a duality statement. If every linear form that kills certain
columns of two matrices `P`, `P'` takes the same value on `P X` and `P' Y`, then `X` and `Y` can be
changed in the coordinates of those columns so that the two vectors become equal. It is used to pass
from a vector common to two flags at one level to a common vector one level higher.


### `New.exists_mulVec_eq_of_annihilator`

 Let `s`, `s'` be sets of column indices. Suppose that every row vector `l` such that `l P`
vanishes on `s` and `l P'` vanishes on `s'` has `l P X = l P' Y`. Then `P x = P' y` for some `x`
equal to `X` outside `s` and some `y` equal to `Y` outside `s'`. 
