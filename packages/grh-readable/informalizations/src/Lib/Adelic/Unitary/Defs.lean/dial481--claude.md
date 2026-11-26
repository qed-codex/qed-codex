---
{
  "module": "src/Lib/Adelic/Unitary/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adelic unitary groups over a CM field: levels, hermitian spaces, lattices and mass

This file defines unitary groups over the adeles of a CM field `E`, with signs `s` at the infinite
places. `New.Gf` is the finite adelic unitary group of the identity form, `New.stdLevel` is its
integral subgroup K_0, and `New.G` is the product G_∞ × G_f. A level is an open subgroup of K_0.
Given a CM type of `E` (`CMType E`, which fixes a complex embedding at each infinite place), a
hermitian space with a point is a form J over E together with an adelic matrix x such that xᴴJx is
diag(s) at the infinite places and 1 at the finite ones; it yields a rational subgroup and a
lattice. The mass is defined for the standard space, where J = 1 and x = 1.

Notions from earlier files:
* `𝔸 E`, `𝔸f E`: the adeles of `E` and its finite adeles; `Ô E`: the integral finite adeles;
  `toAdele : E →+* 𝔸 E` is the embedding of E in its adeles.
* `LocField w`, `LocInt w`: the completion E_w at a finite place w and its ring of integers;
  `evalAt w` takes a finite adele to its component at w.
* `U J`: the group of invertible matrices g with gᴴJg = J.
* `intGL n O`: the matrices in GL_n(R) that, with their inverses, have entries in the subring O;
  `congruenceGL M e`: those of them whose rows e(i) are congruent to rows of 1 modulo M.
* `star w`: the complex conjugate of a finite place w; w is split (`IsSplit`) if `star w ≠ w`.
  `star` on finite adeles is complex conjugation, and `conjLoc h : E_u →+* E_w` is the map it
  induces when `star u = w`.

## Main definitions and results

* `New.Gf`: the finite adelic unitary group G_f.
* `New.G`: the adelic unitary group G = G_∞ × G_f.
* `New.mass`: the mass of the genus of O_E^l.

## Relation to the literature

Known; see `Lib.Adelic.Unitary.WeakApproximation` and `Lib.Adelic.Witt.IwasawaDecomposition` for
sources.


 ### Adelic matrices and their local components 

### `matrix_ext_evalAt`

 Two matrices over the finite adeles are equal if they have the same component at every finite
place. 

### `evalInf`

 The ring homomorphism 𝔸 → ℂ taking an adele of E to its component at the infinite place v;
in `𝔸 E` every infinite component is a complex number. 

### `matrix_ext_𝔸`

 Two matrices over the adeles are equal if they have the same component at every infinite place
and the same finite part. 

### `singleGL`

 The homomorphism sending g in GL_n(E_w) to the element of GL_n(𝔸_f) with component g at w
and 1 at the other places. 

### `evalAt_singleGL`

 The component of `singleGL w g` at `w` itself is `g`. 

### `evalAt_singleGL_of_ne`

 The component of `singleGL w g`, the adelic matrix placing `g` at `w`, at a place `u` other than
`w` is `1`. 

 ### Topology of integral and congruence subgroups 

### `units_matrix_eq_intGL`

 The units of the ring of matrices with entries in a subring O form the group `intGL n O` of
invertible matrices that, with their inverses, have entries in O. 

### `isOpen_intGL`

 If a subring O of R, a commutative ring with a topology, is open, then GL_n(O) = `intGL n O` is
open in GL_n(R). 

### `isCompact_intGL`

 If a subring O of a Hausdorff topological ring R is compact, then GL_n(O) = `intGL n O` is
compact. 

### `isOpen_congruenceGL`

 If the subring O of R and the O-submodule M are open, then the congruence subgroup of GL_n(O)
of matrices whose rows e(i) are congruent to those of 1 modulo M is open in GL_n(R). 

### `eventually_congruenceGL_subset`

 If the O-submodules M_i of R shrink to 0 along a filter, then the principal congruence
subgroups of level M_i eventually lie in any given neighbourhood of 1 in GL_n(R). 

 ### The local and adelic groups 

### `localIntGL`

 For a finite place w of E, the subgroup GL_n(O_w) of GL_n(E_w) of matrices that, with their
inverses, have entries in the local integers. 

### `basicDoubleCoset`

 The set of g in GL_n(E_w) with g and ϖg⁻¹ integral and det g of valuation j, where ϖ is a
uniformiser. For j at most the cardinality of n it is the GL_n(O_w)-double coset of
diag(ϖ1_j, 1). 

### `Gf`

 The finite adelic unitary group G_f: matrices g in GL_n(𝔸_f) with gᴴg = 1. 

### `Gf.coe_mul_U`

 The matrix of the product of an element of G_f and an element of `U 1`, which is the same
group, is the product of the matrices. 

### `Gf.codRestrict_eq_mk`

 A homomorphism f into GL_n(𝔸_f) with values in `U 1`, seen as a homomorphism into G_f, sends x
to f x with the proof that it is unitary. The type `M →* Gf E n` is given explicitly because
`simp` does not unfold `Gf`, so the lemma for `M →* U 1` does not apply to such terms. 

### `stdLevel`

 The subgroup K_0 = G_f ∩ GL_n(Ô) of the finite adelic unitary group, the stabiliser of the
standard lattice Ô^n. 

### `GInf`

 The archimedean unitary group G_∞ for signs s: one copy of the complex unitary group U(diag
s) = `USign s`, the g in GL_n(ℂ) with gᴴ diag(s) g = diag(s), for each infinite place of E. 

### `G`

 The adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the identity
matrix at the finite places. 

### `instance : Coe (Gf E n) (G E s)`

 Elements of `New.Gf` are viewed in `New.G` with component 1 at the infinite places. 

### `stdForm`

 The diagonal adelic matrix that is diag(s) at every infinite place and the identity at the
finite places. 

### `HasLevel`

 The function F on G = G_∞ × G_f is right invariant under K, a subset or subgroup of G_f:
F(g·(1, k)) = F(g) for all k ∈ K and all g ∈ G. 

### `heckeGL`

 The j-th Hecke operator on a representation π of GL_n(E_w): the action (`New.heckeFun`) of
the indicator function of `New.basicDoubleCoset` j, for K = GL_n(O_w). 

 ### Conjugate places and split places 

### `evalAt_star_eq_conjLoc`

 For complex conjugate finite places, `star u = w`, the component at `w` of the conjugate of a
finite adele `x` is the image of its component at `u` under `conjLoc h : E_u →+* E_w`. 

### `evalAt_star_GL`

 Let `u` and `w` be complex conjugate finite places, `star u = w`, and `g` an invertible matrix
over the finite adeles. The component at `w` of the conjugate transpose of `g` is the transpose of
the component of `g` at `u`, carried to `E_w` by the conjugation `conjLoc h : E_u →+* E_w`. 

### `evalAt_star_singleGL`

 For finite places with `star u ≠ w`, where `star u` is the complex conjugate place, the
component at `u` of the conjugate transpose of `singleGL w g` (the adelic matrix with component `g`
at `w` and `1` elsewhere) is `1`. 

### `Gf.atPlace`

 The homomorphism G_f → GL_n(E_w) sending an element to its component at w. 

### `singleGL_mul_star_singleGL_inv_mem_U`

 At a split place `w` (one moved by complex conjugation), the finite adelic matrix with
component `g` at `w`, the inverse of the conjugate transpose of `g` at `star w` and `1` elsewhere
is unitary. 

### `ofSplitPlace`

 For a split place w, the homomorphism GL_n(E_w) → G_f sending g to the unitary element with
component g at w, the inverse conjugate transpose of g at w̄, and 1 at all other places. 

### `atPlace_ofSplitPlace`

 For a finite place `w` of `E` that is split over the maximal real subfield and for `g` in
`GL_n(E_w)`, the component at `w` of the element `ofSplitPlace hw g` of `G_f` is `g`. 

 ### Supports, levels and reductions 

### `stdLevel.map`

 For a ring homomorphism f from the integral finite adeles to S, the homomorphism K_0 →
GL_n(S) applying f to each entry. 

### `Gf.supportedOn`

 The subgroup of G_f of elements supported on S ∪ S̄, that is, with component 1 at every
place outside S ∪ S̄. 

### `localLevel`

 The elements of `New.Gf` whose component at each `w ∈ S` lies in the subgroup `K w`, with no
condition outside `S`; by default `K w` is `New.localIntGL`, the integral matrices with integral
inverse. 

### `Gf.trivialOn`

 The subgroup of G_f of elements with component 1 at every place in S (hence, being unitary,
also at the conjugate places). 

### `stdLevel.reduceAt`

 Reduction modulo w: the homomorphism from K_0 = G_f ∩ GL_n(Ô) to GL_n of the residue field
at w. 

### `mem_localLevel`

 An element of the finite adelic unitary group G_f lies in `localLevel n S K` iff its component
at each place `w ∈ S` lies in the subgroup `K w` of GL_n(E_w). 

### `mem_stdLevel`

 An element of the finite adelic unitary group G_f lies in its integral subgroup K_0 =
`New.stdLevel` iff its entries lie in the integral finite adeles `Ô E`. 

### `IsLevel`

 The subgroup K of the finite adelic unitary group G_f is a level: it is open and contained
in K_0 = G_f ∩ GL_n(Ô). 

### `IsLevel.le`

 K lies in K_0 = `New.stdLevel`. 

### `IsLevel.isOpen`

 K is open. 

### `stdLevelIndex`

 For a subgroup K of G_f, the index [K₀ : K ∩ K₀], where K₀ = `New.stdLevel`; it is 0 if the
index is infinite. 

 ### The adelic group as a group of adelic matrices; compactness and Haar measure 

### `mkAdelicGL`

 The homomorphism sending a family (a_w) in GL_n(ℂ), indexed by the infinite places, and b in
GL_n(𝔸_f) to the element of GL_n(𝔸) with components a_w and finite part b. 

### `G.toUnitary`

 The isomorphism from G = G_∞ × G_f to the unitary group over the adeles of the form that is
diag(s) at the infinite places and 1 at the finite ones, `New.stdForm`. 

### `G.adeleMatrix`

 The matrix over the adeles of an element g of the adelic unitary group G. 

### `G.adeleMatrix_fst`

 At an infinite place, the entries of the adelic matrix `g.adeleMatrix` of an element `g` of
G = G_∞ × G_f are those of the component of `g` there. 

### `G.adeleMatrix_snd`

 The finite parts of the entries of the adelic matrix `g.adeleMatrix` of an element `g` of
G = G_∞ × G_f are the entries of the finite component of `g`. 

### `IsLevel.isCompact`

 A level is compact: it is an open, hence closed, subgroup contained in the compact group K_0. 

### `instance : MeasureSpace (Gf E n)`

 The Haar measure on `New.Gf` that gives `New.stdLevel` mass one. 

### `volume_stdLevel`

 For a CM field `E`, the standard level `stdLevel E n` has measure 1 under `volume` on the finite
adelic unitary group `Gf E n` (matrices g over the finite adeles with gᴴg = 1). Here `stdLevel E n`
is the compact open subgroup G_f ∩ GL_n(Ô), the stabiliser of the standard lattice Ô^n. 

 ### Hermitian spaces with a point 

### `Space`

 A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
diag(s) at the infinite places and 1 at the finite places. 

### `Space.J`

 The matrix over `E` of the hermitian form. 

### `Space.x`

 The point, an invertible adelic matrix. 

### `Space.gram_point`

 In the basis `x` the form is `diag s` at the infinite places and `1` at the finite places. 

### `toRatCoords`

 For a space (J, x), the isomorphism g ↦ x g x⁻¹ from G to the adelic unitary group U(J)(𝔸). 

### `ratEmbed`

 For a space (J, x), the homomorphism γ ↦ x⁻¹ γ x from the rational unitary group U(J)(E) to
G. 

### `embFin`

 For a space (J, x), the homomorphism U(J)(E) → G_f sending γ to the finite part of x⁻¹ γ x. 

### `Γ`

 For a space (J, x), the subgroup x⁻¹ U(J)(E) x of G, the image of the rational unitary
group. 

### `Γf`

 For a space (J, x), the subgroup of G_f formed by the finite parts of the elements x⁻¹ γ x,
γ in U(J)(E). 

### `vecAtPoint`

 For a space (J, x), the adelic vector x⁻¹y attached to a rational vector y in E^n. 

### `baseLattice`

 For a space (J, x), the lattice E^n ∩ x_f Ô^n, as an additive subgroup of E^n. It consists of
the y whose vector x⁻¹y has integral finite part. 

### `stdSpace`

 The definite space I_n with J = 1 and x = 1, the hermitian form given by the sum of the norms
of the coordinates. 

### `mass`

 The mass of the genus of O_E^l: the sum of 1/#(Γ ∩ gK_0g⁻¹) over the classes ΓgK_0 in G_f,
where Γ is the image of U_l(E), the rational unitary group of the standard space `stdSpace`. 

### `stdEmbFin`

 The homomorphism U_n(E) → G_f sending a matrix γ over E with γᴴγ = 1 to its image over the
finite adeles. 

### `stdRatPoints`

 The image of U_n(E), the matrices γ over E with γᴴγ = 1, in the finite adelic unitary group
G_f. 

 ## An element z of a CM field with z − star z invertible 

### `exists_isUnit_sub_star`

 A CM field `E` has an element `z` with `z - star z` invertible, as complex conjugation is not
the identity. 
