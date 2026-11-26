---
{
  "module": "src/Lib/Weil/Unramified/SplitHecke.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/SplitHecke.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/SplitHecke.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke operators and Hecke polynomials at split places; spherical eigenvectors

Let `w` be a split finite place (`star w ≠ w`) with residue field of order `q`. Through
`New.ofSplitPlace`, the spherical Hecke operators of `GL_n(E_w)` act on representations of the
finite adelic unitary group `New.Gf`. A vector is spherical at `w` when it lies in
`New.sphericalAt`, that is, when it is fixed by the integral elements `New.maxCompactAt` supported
at `w` and `w̄`.

## Main definitions and results

* `New.heckeSplit`: the operator `T_{w,j}` of the double coset `New.basicDoubleCoset` of
  `diag (ϖ 1_j, 1)`.
* `New.heckeSplit_star`: on vectors spherical at `w`, `T_{w̄,j}` is the action at `w` of the inverse
  double coset. Hence `New.heckeSplit_dual` (`ϖ T_{w̄,i} = T_{w,n-i}` on such vectors) and
  `New.heckeSplit_adjoint` (`T_{w̄,j}` is adjoint to `T_{w,j}` on spherical vectors, for a
  `G_f`-invariant pairing).
* `New.heckeSplit_comm`: the operators at two split places commute on vectors spherical at both.
* `New.IsUnitary.le_span_joint_eigenvectors`: in a representation unitary for a form `B`
  (`B y y > 0` for `y ≠ 0`, `B (π g x) (π g y) = B x y`), a finite-dimensional stable space of
  spherical vectors is spanned by joint eigenvectors. `New.IsUnitary.le_span_hecke_eigenvectors` is
  the form for places given by a predicate.
* `New.heckePolyEval`, `New.heckePolyOp`: the Hecke polynomial `∑ (-X)^i q^(i choose 2) T_{w,i}`,
  where `i` runs from `0` to `n`, `q` is the order of the residue field at `w`, and
  `New.heckePolyOp` takes the `T_{w,i}` to be the operators `New.heckeSplit`, while
  `New.heckePolyEval` allows any coefficients `t i`.
* `New.HasHeckePolynomial`: vectors spherical at `w` (`New.sphericalAt`) on which this polynomial
  acts by given scalars.

Notions from other files:
* `New.levelSpace`: For a representation π of G, a subgroup K and a character χ of K, the submodule
  of vectors v with π(k)v = χ(k)v for all k in K.
* `New.heckeFun`: For a function f on G, the operator ∑ f(g)π(g), summed over representatives g of
  G/K.
* `New.stdLevel`: The subgroup K₀ = G_f ∩ GL_n(Ô) of the finite adelic unitary group.
* `New.Gf.supportedOn`: The subgroup of G_f of elements supported on S ∪ S̄, that is, with component
  1 at every place outside S ∪ S̄; `New.Gf.trivialOn`: those with component 1 at every place in S.
* `New.localIntGL`: For a finite place w of E, the subgroup GL_n(O_w) of GL_n(E_w) of matrices that,
  with their inverses, have entries in the local integers.

## Relation to the literature

Known; see `Lib.General.LinearAlgebra.IntegralLattices` for sources.


### `maxCompactAt`

 The subgroup of K₀ of elements whose components away from w and w̄ are 1. 

### `heckeSplit`

 The Hecke operator `T_{w,j}` at a split place `w`: the operator of the double coset of
`diag (ϖ 1_j, 1)` in `GL_n(E_w)`, acting through the embedding `ofSplitPlace hw` of `GL_n(E_w)` in
the finite adelic unitary group. 

### `heckeSplit_eq_heckeFun`

 `T_{w,j}` is the operator `New.heckeFun` of the indicator function of the double coset. 

### `sphericalAt`

 For a representation π of G_f, the vectors spherical at w: those fixed by all elements of K₀
whose components away from w and w̄ are 1. 

### `FinPlace.IsSplit.star`

 The conjugate of a split place is split. 

### `Gf.supportedOn_star`

 The elements supported at `w, w̄` do not depend on which of the two places is named. 

### `levelSpace_le_sphericalAt`

 For a finite set S of places containing neither w nor w̄, every vector of π fixed by the
elements of K₀ with component 1 at all places of S is spherical at w. 

### `mem_sphericalAt_iff`

 At a split place, spherical means fixed by `GL_n(O_w)` acting through `New.ofSplitPlace`. 

### `map_heckeSplit`

 A semilinear map `L` that intertwines, on `v`, the actions of the elements supported at
`w, w̄` intertwines the Hecke operators `T_{w,j}` on `v`. 

### `heckeSplit_comm_of_trivialOn`

 An element with component 1 at `w` (hence at `w̄`) commutes with `T_{w,j}` on every vector. 

 ### The operators on spherical vectors 

### `heckeSplit_star`

 For `w` split and `v` spherical at `w`, the vector `T_{w̄,j} v` is the action on `v`, through
`GL_n(E_w)`, of the indicator function of the inverse of the double coset of `diag (ϖ 1_j, 1)`. 

### `heckeSplit_dual`

 For a uniformiser `ϖ` of `E_w`, `n = i + j` and `v` spherical at the split place `w`: applying
`T_{w̄,i}` and then the scalar matrix `ϖ` embedded at `w` gives `T_{w,j} v`. 

### `heckeSplit_comm_of_atPlace_mem`

 On a spherical vector, `T_{w,j}` commutes with every element that is integral at `w`. 

### `heckeSplit_adjoint`

 The adjoint of `T_{w,j}` is `T_{w̄,j}`. Let `w` be split, let `v` and `v'` be spherical at `w`
for `π` and `π'`, and let `B` be an invariant pairing of `π` with `π'`, `σ`-semilinear in the first
variable. Then `B (T_{w,j} v) v' = B v (T_{w̄,j} v')`. 

### `heckeSplit_mem_levelSpace`

 Let w be split, K a subgroup of K₀ and χ a character of K. If v is spherical at w and of
level (K, χ), then T_{w,j} v is of level (K, χ). 

### `isHeckeFunction_basicDoubleCoset_inv`

 The function `g ↦ 1_D(g⁻¹)`, for `D` the double coset `New.basicDoubleCoset n w j`, is
bi-invariant under `GL_n(O_w)` and lives on finitely many cosets. 

### `heckeSplit_comm`

 Hecke operators at split places `w` and `u` commute on a vector `v` spherical at both:
`T_{w,i} T_{u,j} v = T_{u,j} T_{w,i} v`. A case of the commutativity of the spherical Hecke
algebra. 

 ### Joint eigenvectors in a unitary representation 

### `eigenvector_of_pow_adjoint`

 Let `B` be a sesquilinear form with `B y y ≠ 0` for `y ≠ 0`, and let `T'` be adjoint to `T`
and commute with it. If a power of `T' - c` kills `x`, then `T x = star c • x`. 

### `IsUnitary.le_span_joint_eigenvectors`

 Spectral theorem for spherical Hecke operators. Let `π` be a unitary representation of the
finite adelic unitary group and `S` a set of split places stable under conjugation. Let `U` be a
finite-dimensional subspace, spherical at every `w ∈ S` and stable under every `T_{w,j}` with
`w ∈ S`. Then `U` lies in the span of its vectors `x` that are eigenvectors of all these `T_{w,j}`
at once; `c w j` is the eigenvalue. 

### `IsUnitary.le_span_hecke_eigenvectors`

 For a complex representation `π` of `Gf E n` that is unitary for the form `B`, let `p` be a set
of split finite places closed under conjugation `star`. Let `U` be a finite-dimensional subspace
that is spherical at every place in `p` and stable under every Hecke operator `heckeSplit π _ j` at
those places. Then `U` is spanned by its vectors that are simultaneous eigenvectors of all these
operators, with eigenvalues indexed by pairs of a place satisfying `p` and a degree `j` (a version
of `IsUnitary.le_span_joint_eigenvectors`). 

 ## The Hecke polynomial at a split place 

### `heckePolyEval`

 For a sequence t_i in a complex vector space and X ∈ ℂ, the sum ∑_{i=0}^{n} (−X)^i
q^{binom(i,2)} t_i, with q the order of the residue field at w and n the number of elements of the
index type `n`. 

### `heckePolyOp`

 The Hecke polynomial at `w` as a family of operators on `π`: the function sending `X : ℂ` to
`∑ i ≤ n, (-X)^i q^(i choose 2) T_{w,i}`, with `n` the rank and `q` the order of the residue
field at `w`. Here `hw` is a proof that `star w ≠ w`. 

### `HasHeckePolynomial`

 The vector y is spherical at w (`New.sphericalAt`), that is, fixed by the elements of the
maximal compact subgroup whose components away from w and w̄ are 1. Moreover, the Hecke polynomial
`New.heckePolyOp` at each T ∈ ℂ acts on y by p(T). 


## Spherical eigenvectors and adjoints of the Hecke polynomial

Eigenvectors of the `T_{w,i}` and of the Hecke polynomial, equivariant maps and adjoints.


### `hasHeckePolynomial_of_heckeSplit`

 A spherical vector on which each `T_i` acts by `t i` is an eigenvector of the Hecke polynomial,
with eigenvalue the polynomial made from the `t i`. 

### `HasHeckePolynomial.smul`

 A scalar multiple of a spherical eigenvector of the Hecke polynomial is one with the same
eigenvalue `p`. 

### `map_heckePolyOp`

 A `σ`-semilinear map that is equivariant on `y` for the elements supported above `w` and
`star w` carries the Hecke polynomial at `T` to the Hecke polynomial at `σ T`. 

### `heckePolyOp_adjoint`

 Let w be split and B a G_f-invariant pairing of π and π', σ-semilinear in the first
variable. On vectors spherical at w, the adjoint of the Hecke polynomial H_w(X) is
H_{w̄}(σX): B(H_w(X)y, z) = B(y, H_{w̄}(σX)z). 

### `sum_coeff_invOfUnit_smul_eq`

 If `∑_{i ∈ t} U ^ i • b i = Q(U) • ∑_{i ∈ s} U ^ i • a i` for all complex `U`, with `Q(0) = 1`,
then for each `r ∈ s`, `a r` is the coefficient of `X ^ r` in the power series
`Q⁻¹ * ∑_{i ∈ t} X ^ i • b i`. 

### `heckeSplit_mem_of_heckePolyOp`

 Let `π` be a complex representation of the finite adelic unitary group `Gf E n` on `W`, and let
`w` be a finite place of the CM field `E` that is split, so `star w ≠ w` (witnessed by `hw`). If a
ℂ-linear subspace `N` of the endomorphisms of `W` contains the Hecke polynomial operator
`heckePolyOp π hw X = ∑ i ≤ n, (-X)^i q^(i choose 2) T_{w,i}` for every `X : ℂ`, then `N` contains
the Hecke operator `heckeSplit π hw i` (that is, `T_{w,i}`) for every `i`. 

### `exists_heckeSplit_eq_smul`

 The eigenvalue `p` of the Hecke polynomial determines eigenvalues `t i` of the operators `T_i`,
the same for all spherical eigenvectors. 
