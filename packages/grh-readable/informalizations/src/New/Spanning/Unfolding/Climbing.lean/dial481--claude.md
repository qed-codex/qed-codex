---
{
  "module": "src/New/Spanning/Unfolding/Climbing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Residue lifts, lattice charts and common flag vectors: which filling terms contribute

This file sorts the terms of the second moment of the filling theorem and shows which of them
contribute. Common vectors of two flags are moved up the flags by elementary linear algebra.

## Main definitions and results

* `New.Filling.mem_congruenceGL_iff_isIntMatrix_scaleAt`: for an integral idele `p` that is a unit
  at one of each pair of conjugate places, a unitary `k` is integral with row `o` congruent to that
  of `1` modulo `p` iff `k - 1` stays integral after dividing row `o` by `p` and column `o` by `p̄`.
* `New.Filling.inclHFin_mem_latticeStabilizer_iff`: `S.inclHFin k` is integral iff `k` is integral
  and its row `k₀` is congruent to that of `1` modulo `S.piN`.
* `New.Filling.MeetsAt`, `New.Filling.fixer`, `New.Filling.IsOpenElement`,
  `New.Filling.InScalarCoset`: the meeting places, and the subsets of the finite group.
* `New.Filling.amplitudeSum_eq_zero_of_not_charsAgree`: a stable set of terms none of which agrees
  contributes `0`.
* `New.Filling.mul_star_eq_and_pairOccursAt_of_le`,
  `New.Filling.exists_pairOccursInColumnsAt_top_of_meetsAt`: when the characters agree, the leading
  coefficients of a common vector of two flags have equal norms and recur at all higher indices over
  `E`; modulo a place above `M` where the flags meet, some pair not both zero occurs at the top
  index.
* `New.Filling.CharsAgree.exists_hasCellRank`: a term with agreeing characters and discriminant `0`
  has a cell rank.

Notions from other files:
* `S : New.Filling E 𝔰`: the filling data over the CM field `E`; `S.chosenPlaces i` is a set of
  places of `E` of norm the prime `S.levelPrime i` (`i = 0, 1`). The places above `M` are these and
  their conjugates, indexed by pairs `(w, false)` and `(w, true)`.
* `S.latticeStabilizer`, `S.reduction`, `S.ResidueGL`: the integral elements of the finite adelic
  unitary group, and their reduction to the product of the general linear groups over the residue
  fields `ResField w` at the chosen places.
* `New.frameImage γ`: the columns of `γ` at the indices of the frame `f = (e₁, …, e_ϱ, z)`; so
  `frameImage 1` is the frame itself.
* `S.CharsAgree γ`, for rational `γ`: the character `S.unipotentChar` takes equal values on rational
  `u`, `u'` in `besselU` with `u γ = γ u'`. `S.Agrees s` is the analogue for `s` in `S.ResidueGL`.
* `besselH`, `besselU`, `besselS`: the unitary group of `X₀`, the unipotent group of the frame, and
  the Bessel subgroup that they generate.
* `Ô E`, `𝔸f E`: the integral finite adeles and the finite adeles of `E`.

## Relation to the literature

Take a rational element under which the unipotent character of the Poincaré series agrees with its
conjugate. For such an element, a vector shared by the standard frame and its image forces a
norm-one pair to occur. Take an integral adelic element k whose reduction modulo M agrees, and two
integral vectors orthogonal, in the standard form, to all vectors of f and kf but the last of each
(f is the frame). If the determinant δ of their products with these two last vectors is a finite
idele, the norm of the product of the primes over M where the span of f meets that of kf is at most
the index of δÔ in Ô (`New.Filling.meetNorm_le_genIndex_det`). This sorts the terms of the unfolded
second moment. Related work: Friedberg, Poincaré series for GL(n), 1987; Y. Liu, Relative trace
formulae toward Bessel and Fourier–Jacobi periods, 2014; Furusawa–Shalika, Central critical values
of degree four L-functions for GSp(4), Mem. AMS 782, 2003.


 ## Residues, meeting places, fixed vectors and open elements 

### `reduction_apply_congr`

 An entry of the reduction of an integral element modulo a chosen place `w` depends only on the
same entry of its matrix. 

### `exists_reduceAt_eq_and_reduceAt_star_eq`

 The chosen places `p` are the places of `E` in `S.chosenPlaces i`, of norm the prime
`S.levelPrime i` (`i = 0, 1`); `New.reduceAt p` is reduction of integral finite adeles modulo `p`.
Given residues `t p` and `t' p` at each chosen place `p`, some integral finite adele `y` reduces to
`t p` at every `p`, while its conjugate `star y` reduces to `t' p` there. 

### `exists_reduceAboveM_eq`

 Residues may be prescribed at all the places above `M`, the product of the two level primes, at
once. Such a place is a pair `x` of a chosen place `w` and a Boolean; `S.reduceAboveM x y` is the
residue at `w` of `y` if the Boolean is false and of its conjugate `star y` if it is true. For any
family `t` of residues there is an integral finite adele `y` with these reductions. 

### `actionAt`

 The action of `s` on the lattice modulo the place `p` of `E` above `M`: by its component at the
chosen place `w`, or by the inverse adjoint if `p` is the conjugate of `w`. 

### `FrameVector`

 A nonzero vector of the span of the frame modulo the chosen place `w` (first component `false`)
or modulo its conjugate (`true`), given by its coordinates in the frame. 

### `vectorFixer`

 For `d = (ε, v)`, the subgroup of the `s` that fix the vector of the span of the frame with
coordinates `v`; the columns of `inclMatrix _ 𝔰.besselFrame` are the frame vectors. If `ε` is false,
`s` acts modulo `w` by its component at `w`; if `ε` is true, it acts modulo the conjugate of `w` by
the inverse adjoint of that component (`S.idOrInvAdjoint ε` makes this choice). See
`mem_vectorFixer`, `mem_vectorFixer_false` and `mem_vectorFixer_true`. 

### `mem_vectorFixer`

 For `d = (ε, v)`, an element `s` lies in `vectorFixer w d` iff its action modulo the place
`(w, ε)` fixes the combination of the frame vectors with coordinates `v`. 

### `mem_vectorFixer_false`

 To fix a vector modulo the chosen place `w` is to fix it by the component at `w`. 

### `mem_vectorFixer_true`

 To fix a vector modulo the conjugate of `w` is to fix, by the inverse transpose of the component
at `w`, the linear form that the vector defines through the Gram matrix of the lattice basis. 

### `mulVec_frameImage_one_mulVec`

 The matrix `g` applied to the combination of the frame vectors with coordinates `x` is the
combination of their images with the same coordinates. 

### `reducedImage_besselH_le_vectorFixer`

 Let `besselH` be the fixer of all basis vectors outside `𝔰.κ`, a copy of the unitary group of
X₀. Its reduction to the residue fields, `S.reducedImage besselH`, fixes every nonzero vector `d` of
the span of the frame f = (e₁,…,e_ϱ,z), taken modulo a chosen place `w` or modulo its conjugate.
That is, `S.reducedImage besselH` lies in `S.vectorFixer w d`. 

### `MeetsAt`

 The element `s` meets at the place `p` of `E` above `M`: modulo `p`, the span of the frame and
its image under `s` share a nonzero vector. 

### `meetNorm`

 The absolute norm of the product of the places at which `s` meets; a place above
`S.levelPrime i` has norm `S.levelPrime i`. 

### `meetsAt_of_mem_vectorFixer`

 An element that fixes a nonzero vector of the span of the frame modulo a place meets there. 

### `prod_le_meetNorm`

 If `s` meets at every place of a set `A` of places above `M`, the product of their norms is at
most `meetNorm s`, the product of the norms of all the places at which `s` meets. 

### `one_le_meetNorm`

 The norm of the product of the places above `M` at which `s` meets is at least `1`. 

### `fixer`

 The subgroup of the elements that fix the given vector modulo `w` or its conjugate, for every
`w` in a set of chosen places above the first level prime. The vectors at other places are
ignored. 

### `mem_fixer`

 An element lies in `fixer places vectors` iff it fixes `vectors w` for every `w` in
`places`. 

### `reducedImage_besselH_le_fixer`

 The group that fixes given vectors of the span of the frame modulo some places contains the
reduction of `besselH`, the unitary group of `X₀`. 

### `mem_fixer_insert`

 For `w` not in `places`, `s` lies in `S.fixer` for `insert w places` and `update vectors w d`
iff `s` lies in `S.fixer places vectors` and in `S.vectorFixer w d`, the subgroup fixing the vector
`d` at `w`. 

### `IsOpenElement`

 The element `s` is open: at some chosen place `w` above the first level prime, the leading
principal minors of order less than `𝔰.n = ϱ + 1` of the matrix `(h(f_j, s f_l))` are all nonzero.
Here `f` is the frame, which has `𝔰.n` vectors, `h` is the form in the lattice basis modulo `w`
(its middle block is `S.latticeMiddle`), and `frameGram` is this matrix of products. 

### `InScalarCoset`

 The element `s` is `ζ` times an element of the reduction of the Bessel subgroup, the integral
adele `ζ` acting through its residues at the chosen places. 


## The group U(X₀) in the lattice basis: integrality, reduction, class sums

The unitary group `New.Gf E 𝔰.κ` of the standard form on `X₀`, with basis indexed by `𝔰.κ`, over
the finite adeles embeds, by `New.Filling.inclHFin`, in the larger unitary group of the filling data
`S` (`New.Filling`). The larger group is written in the basis of a lattice that involves the idele
`S.piN` of norm `S.N` at the index `𝔰.k₀`.

`New.IsIntMatrix` says that a matrix has entries in a subring; `scaleAt p k₀` is the diagonal
matrix with `p` at `k₀` and `1` elsewhere; `congruenceGL M e` is the group of integral invertible
matrices whose rows `e i` are congruent to those of `1` modulo `M`.


### `isIntMatrix_scaleAt_mul_iff`

 The matrix `l` with row `o` multiplied by `a` is integral iff that row times `a` and the other
rows of `l` are integral. 

### `isIntMatrix_middleInclusionMatrix_mul_iff`

 Let `S.piN` be the integral idele of the filling data `S`, and let `l` be a matrix over the
finite adeles with rows indexed by `𝔰.κ`; a matrix is integral (`IsIntMatrix (Ô E)`) if its entries
are integral finite adeles. The columns of `middleInclusionMatrix 𝔰 S.piN` are the orthonormal basis
vectors of `X₀` in the lattice basis of `X₀ ⊕ ⟨z⟩`. Its product with `l` is integral iff `l` is
integral and every entry of row `k₀` of `l` is `S.piN` times an integral adele. 

### `isIntMatrix_middleInclusionMatrix_mul_of_scaleAt`

 If `l` stays integral after dividing its row `k₀` by `S.piN`, then the product of
`middleInclusionMatrix 𝔰 S.piN` with `l` is integral. 

### `inclHFin_sub_one_eq`

 The blocks follow `𝔰.BesselIndex = Fin ϱ ⊕ (𝔰.κ ⊕ Unit) ⊕ Fin ϱ`. The image of `k` in the large
unitary group, in the lattice basis, differs from `1` only in the block with rows `𝔰.κ ⊕ Unit` and
columns `𝔰.κ`. There the difference is `middleInclusionMatrix * ((k - 1) * D)` with `D` the diagonal
matrix `scaleAt (star piN⁻¹) k₀`. 

### `forall_inclHFin_sub_one_iff`

 A property that holds for `0` holds for all entries of `S.inclHFin k - 1` iff it holds for all
entries of `middleInclusionMatrix * ((k - 1) * D)`, with `D` the diagonal matrix
`scaleAt (star piN⁻¹) k₀`. 

### `isIntMatrix_scaleAt_mul_sub_one_mul_scaleAt`

 Let the idele `p` be a unit at `w` or at the conjugate of `w`, for each place `w` (`v` is the
valuation). If the finite adelic unitary matrix `k` is integral with row `o` congruent to that of
`1` modulo `p`, then `k - 1` stays integral after dividing row `o` by `p` and column `o` by
`p̄`. 

### `isIntMatrix_scaleAt`

 The diagonal matrix with `a ∈ O` at `o` and `1` elsewhere has entries in the subring `O`. 

### `mem_congruenceGL_iff_isIntMatrix_scaleAt`

 Let `p` be an integral idele such that at each place `p` or its conjugate is a unit. Let `L` be
the lattice of integral vectors whose coordinate `o` is divisible by `p`; its dual `L^∨` consists of
the vectors that are integral except for a denominator `p̄` in that coordinate. A finite adelic
unitary matrix `k` is integral with row `o` congruent to that of `1` modulo `p` if and only if
`k - 1` maps `L^∨` into `L`. 

### `mem_latticeStabilizer_iff_isIntMatrix_sub_one`

 An element `x` of the large unitary group lies in the stabilizer of the lattice iff `x - 1` is
integral: an isometry of a unimodular form with `x - 1` integral has an integral inverse. 

### `inclHFin_mem_latticeStabilizer_iff`

 Let `k` be a unitary matrix for the identity form on `𝔰.κ` over the finite adeles `𝔸f E`. Its
image `S.inclHFin k` in the finite adelic unitary group of V, written in the lattice basis, lies in
`S.latticeStabilizer` exactly when `k` lies in `congruenceGL`. That means `k` is integral and its
row at `𝔰.k₀` is congruent to that of `1` modulo the integral idele `S.piN`. 

### `reduction_inclHFin_eq_one_iff`

 Let `k` be a unitary matrix for the standard form on `X₀`, with basis indexed by `𝔰.κ`, over the
finite adeles. The embedding `S.inclHFin` sends it to the finite adelic unitary group of the whole
space, written in the lattice basis of `S`; `S.latticeStabilizer` consists of the elements whose
matrix in this basis is invertible over `Ô E`. Let `S.inclHFin k` lie in it, so that `k` is
integral. For `i : Fin 2`, indexing the level primes p₀, p₁ of `S`, and a place `w` in
`S.chosenPlaces i`, of norm p_i, the reduction `S.reduction` of `S.inclHFin k` modulo `w` is `1`
exactly when that of `k` is; `stdLevel.reduceAt w` is the entrywise reduction modulo `w` of integral
unitary matrices. 

### `classSum_sourceLevel_eq_sum`

 The classes `S.Classes` are the double cosets, in the finite adelic points of `U(X₀)`, of the
rational points `stdRatPoints` and the level subgroup `S.sourceLevel` of the filling data. At this
level the stabilisers are trivial, so the class sum of `f` (the sum over the double cosets weighted
by the inverse orders of the stabilisers) is the plain sum over the classes. 

### `card_resField_eq_levelPrime`

 The residue field at a chosen place `w` of index `i` has `S.levelPrime i` elements. 

 ## Terms that do not agree contribute `0` 

### `tsum_indicator_smul_eq_tsum_stabilizer`

 Let `a x • x` be a chosen representative of the orbit of `x` under the group `H`. A sum over
`u : H` that is restricted to those `u` for which `u • x` is the representative is a sum over the
stabilizer of the representative, shifted by `a x`. 

### `integral_besselKernel_eq_zero_of_not_charsAgree`

 Let the characters of the rational element `γ` not agree (`¬S.CharsAgree γ`): the character
`S.unipotentChar` takes different values on some rational `u`, `u'` in the Bessel unipotent group
`besselU` with `u γ = γ u'`. For `c` in `S.Classes`, the double cosets
`U(X₀)(E⁺) \ U(X₀)(𝔸_f) / sourceLevel`, `S.classUnipotent c` is a congruence subgroup of the
rational points of `besselU`. Let `Γ` be the stabilizer in it of the coset
`γ · S.classUnipotent c'`, mapped by `S.ratToInf` to the product over the infinite places of the
complex unitary group `𝔰.G₁`. Let `Γ` be discrete and `β` a cutoff for it. Then the kernel
`S.besselKernel side γ y = W(y) ⊗ W(γ⁻¹ y)^*` has integral `0` against `β`; here `W` is the Bessel
function or its cut, according to `side`. 

### `amplitudeSum_eq_zero_of_not_charsAgree`

 Let `E` contain a primitive root of unity of order `5040`, let the filling data satisfy the
standing hypotheses `S.IsAdmissible`, and let `T` be a set of rational elements that is stable under
multiplication by the unipotent group `besselU` on both sides. Suppose that no `γ` in `T` has
agreeing characters: for each `γ` in `T` the character `S.unipotentChar` takes different values on
some rational `u`, `u'` in `besselU` with `u γ = γ u'`. Then `S.amplitudeSum side T c s c' = 0`.
This is the sum of the amplitudes of the `γ` in `T` such that `h_c⁻¹ γ h_c'` is integral with
reduction `s`, where `h_c`, `h_c'` represent the classes `c`, `c'`. 


## Common vectors of two flags

Two matrices `P`, `P'` with columns indexed by `Fin (n + 1)` give two flags, spanned by the first
columns. A common vector is a relation `P *ᵥ x = P' *ᵥ y`. Indices start at `0`.


### `PairOccursInColumnsAt`

 Some vector lies in the span of the columns of index at most `j` of both `P` and `P'`, and
its coefficients at `j` are `μ` and `μ'`. 

### `IsTopIndex`

 The index `j` is the top index of the vector with coordinates `x` in one frame and `y` in the
other: the least index above which both vanish. 

### `exists_isTopIndex`

 Every pair of coordinate vectors `x`, `y` has a top index. 

### `IsTopIndex.ne_zero_or_ne_zero`

 If `x ≠ 0` and `j` is the least index above which `x` and `y` vanish, then `x j` and `y j` are
not both `0`. 

### `isTopIndex_of_ne_zero`

 An index `j` above which the coordinates `x`, `y` vanish, and at which they are not both `0`, is
the top index. 

### `PairOccursInColumnsAt.of_le`

 Suppose that whenever `μ`, `μ'` are the coefficients at an index of a common vector of the flags
of `P` and `P'`, they are so at the next index. Then coefficients at `j` are coefficients at every
`l ≥ j`. 

### `pairOccursInColumnsAt_of_forall_mul_vecMul_eq`

 If every linear form `m` that kills the columns of index below `j` of `P` and `P'` takes the
same value on `μ` times column `j` of `P` and `μ'` times column `j` of `P'`, then some vector lies
in the span of the columns of index at most `j` of both `P` and `P'`, with coefficients `μ`, `μ'` at
`j`. 

### `dotProduct_cons_zero_init`

 Let `w` vanish up to the index `i` and `x` above it. The vector `cons 0 (init x)` is `x` shifted
up by one index, so only one term remains in the sum of the products `w (b + 1) * x b`. 


## Moving common vectors up the flags over `E`

Here `f = frameImage 1` is the frame `(e₁, …, e_ϱ, z)` and `γ f = frameImage γ` its image under the
rational element `γ`. The predicate `PairOccursAt γ` is `PairOccursInColumnsAt` for these two
matrices.


### `pairOccursAt_succ`

 One step up the flags of the frame `f = (e₁, …, e_ϱ, z)`, the basis vectors at the indices
`𝔰.besselFrame`, and of its image `γ f`. Let the characters of the rational element `γ` agree:
`S.unipotentChar` takes equal values on rational `u`, `u'` in the unipotent group `besselU` with
`u γ = γ u'`. Suppose that `f x = γ f y` for coordinates `x`, `y` that vanish above `j` and equal
`μ`, `μ'` at `j`. Then `f x' = γ f y'` for some `x'`, `y'` that vanish above `j + 1` and equal `μ`,
`μ'` at `j + 1`. 

### `CharsAgree.pairOccursAt_mono`

 Let the characters of `γ` agree. If `μ`, `μ'` are the coefficients at `j` of a common vector of
the flags of the frame `f` and of `γ f`, they are the coefficients of a common vector at every index
`l ≥ j`. 

### `CharsAgree.mul_star_eq_of_pairOccursAt`

 Let the characters of `γ` agree. If `μ`, `μ'` are the coefficients at `j` of a common vector of
the flags of the frame `f` and of `γ f`, then `μ μ̄ = μ' μ̄'`. 

### `mul_star_eq_and_pairOccursAt_of_le`

 Let the characters of `γ` agree. If `μ`, `μ'` are the coefficients at `j` of a common vector of
the flags of the frame `f` and of `γ f`, then `μ μ̄ = μ' μ̄'`, and `μ`, `μ'` are the coefficients of
a common vector at every index `l ≥ j`. 

### `CharsAgree.mul_star_eq_of_isTopIndex`

 Let the characters of `γ` agree, and let a common vector, with coordinates `x` in the frame `f`
and `y` in `γ f`, have the top index `j` (the least index above which `x` and `y` vanish). Then
`x j` and `y j` have the same norm. 

### `CharsAgree.mul_star_ne_zero_of_isTopIndex`

 Let `γ` satisfy `S.CharsAgree γ`. Let `x ≠ 0` and `y` be the coordinates of one vector in the
frames `frameImage 1` and `frameImage γ`, with top index `j`. Then `x j * star (x j) ≠ 0`. 

### `CharsAgree.exists_isTopIndex_apply_eq`

 Suppose `S.CharsAgree γ`: the unipotent character takes equal values at `u` and `γ⁻¹ u γ` for
every rational `u` in `𝖴 ∩ γ 𝖴 γ⁻¹`. Let a nonzero vector have coordinates `x` in the frame
`f = (e₁,…,e_ϱ,z)` (`frameImage 1`) and `y` in `γ f` (`frameImage γ`), with top index `j`. Then for
every `l ≥ j` some such common vector has top index `l` and the coefficients `x j`, `y j` at `l`. 

### `mul_star_eq_and_ne_zero_and_exists_isTopIndex`

 Let `γ` satisfy `S.CharsAgree γ`. Let `x ≠ 0` and `y` be the coordinates of one vector in the
frames `frameImage 1` and `frameImage γ`, with top index `j`. Then
`x j * star (x j) = y j * star (y j) ≠ 0`. For every `l ≥ j`, some such pair `x'`, `y'` has top
index `l` with `x' l = x j` and `y' l = y j`. 


## Common vectors of two frames modulo a place above `M`

For an element of the stabilizer of the lattice whose reduction agrees (`New.Filling.Agrees`), the
coefficients at one index of a common vector of the two flags modulo a place `w` above `M` are also
the coefficients at the next index of some common vector, and so up to the last index. Here `M` is
the product of the two level primes, and a place above `M` is a pair of a chosen place and a Boolean
that is true for its conjugate.


### `actionAt_reduction`

 For `w`, a chosen place of norm `S.levelPrime i` together with a Boolean that says whether to
conjugate first, `S.actionAt (S.reduction k) w` is the integral matrix of `k` reduced entrywise by
`S.reduceAboveM w`. 

### `actionAt_mul`

 The action modulo a place `w` above `M` is multiplicative. 

### `eq_of_forall_actionAt_eq`

 Two elements `s`, `t` of `S.ResidueGL` are equal if `S.actionAt s (q, b) = S.actionAt t (q, b)`
for every chosen place `q`. Here `b` is fixed: either `b = false` (modulo the chosen places) or
`b = true` (modulo their conjugates). 

### `reduceAboveM_star`

 Conjugation exchanges the reductions at a chosen place and at its conjugate. 

### `exists_lift_reduceAboveM_eq`

 Let `w` be a place above `M`, the product of the two level primes: a chosen place, or its
conjugate if the Boolean is true. Residues at `w` lift to integral adeles, `0` to `0`, that vanish
at all other places above `M`. 

### `exists_eichler_mem_latticeStabilizer`

 Let the coordinates `x` in the frame vanish from `a` on, and let the linear form `m` kill the
frame vectors below `a`; both are integral, and so is `r`. Then some `u` in the stabilizer of the
lattice, an Eichler map, lies in the Bessel unipotent group, and the sum of its superdiagonal
entries on the frame is `r` times the value of `m` on `x` shifted up by one index. Modulo a place
`w` above `M` that divides `star x`, it is `1 + r (f x) m`, where `f x = frameImage 1 *ᵥ x` is the
vector with coordinates `x`. 

### `vecMul_frameImage_dotProduct_cons_init_eq_of_agrees`

 Work modulo a place `w` above `M`. Let `k` stabilize the lattice, let its reduction agree, and
write `γ` for `S.actionAt (S.reduction k) w`, the matrix of `k` modulo `w`. Suppose that
`f x = γ f y` for the frame `f`, where the coordinates `x` and `y` vanish from `a` on, and let the
linear form `m` kill `f_c` and `γ f_c` for `c < a`. Then `m` takes the same value on the two vectors
obtained by shifting the coordinates up by one index. 

### `pairOccursInColumnsAt_succ_of_agree`

 One step up modulo a place above `M = p₀ p₁`, the product of the two level primes. Here `w` is a
chosen place, of norm `p₀` or `p₁`, with a Boolean that picks this place or its conjugate. Let `k`
stabilize the lattice, and let its reduction `S.reduction k` agree: integral unipotent `u`, `u'`
with `u k ≡ k u'` modulo `M` have the same unipotent character. Let
`s = S.actionAt (S.reduction k) w` be the matrix of `k` modulo the picked place. Let `A_{≤j}` be the
span of the frame vectors `(e₁,…,e_ϱ,z)` of index at most `j`. If `μ`, `μ'` are the coefficients at
`j` of a vector of `A_{≤j} ∩ s A_{≤j}`, they are also the coefficients at `j + 1` of some vector of
`A_{≤j+1} ∩ s A_{≤j+1}`. 

### `exists_pairOccursInColumnsAt_top_of_meetsAt`

 Let `s` be the reduction `S.reduction k` of an element `k` of the lattice stabilizer, and let
`s` agree: the unipotent character takes equal values on integral unipotent `u`, `u'` with
`u s = s u'` after reduction. Here `w` is a chosen place above `M = p₀ p₁`, the product of the two
level primes, with a Boolean that picks this place or its conjugate. Suppose the span of the frame
`f = (e₁,…,e_ϱ,z)` and that of `s f` share a nonzero vector modulo this place. Then `f x = s f y`
modulo it for some `x`, `y` whose entries `μ`, `μ'` at the last index `𝔰.top` are not both `0`. 

### `meetNorm_le_genIndex_star`

 Let `s : S.ResidueGL` be a tuple of invertible matrices over the residue fields at the places
`S.chosenPlaces i` (of norm p₀ or p₁). Let `δ : Ô E` have conjugate a unit of `𝔸f E`, and let
`S.reduceAboveM w δ = 0` (reduction modulo `w`, after conjugation if the Boolean of `w` is true) at
each chosen `w` where `s` meets: modulo `w`, the span of the frame (e₁,…,e_ϱ,z) and its image under
`s` share a nonzero vector. Then `S.meetNorm s`, the norm of the product of these places, is at most
the generalised index of the conjugate of `δ`: the inverse of the factor by which it scales Haar
measure, here the order of `Ô / δ Ô`. 

### `lastIndices`

 The two indices of the pair of frames `(f | k f)` that belong to the last vector of `f` and to
the last vector of `k f`, listed along the bijection `ρ` of `W` with a set of two elements. 

### `reduceAboveM_det_eq_zero_of_meetsAt`

 Let `w` be a chosen place of `E`, with a Boolean that says whether to conjugate first. Let the
reduction of `k` agree: integral unipotent `u`, `u'` with `u k ≡ k u'` have the same unipotent
character. Let `f = (e₁, …, e_ϱ, z)` be the frame, and let the spans of `f` and `k f` share a
nonzero vector modulo `w`. Let `K` be the matrix of `k` over `Ô`, and let `Q = T (f | K f)` for an
integral matrix `T` whose two rows are indexed by `W`. Suppose all columns of `Q` vanish except the
two at the last index of `f` and of `K f`, which `lastIndices 𝔰 ρ` lists. Then the determinant of
these two columns vanishes modulo `w`. 

### `meetNorm_le_genIndex_det`

 Let `k` stabilize the lattice, and let its reduction agree: integral unipotent `u`, `u'` with
`u k ≡ k u'` modulo `M`, the product of the two level primes, have the same unipotent character. Let
`t` be an integral matrix whose two columns are indexed by `W`. Let `P = (f | k f)ᴴ t`, where
`framePair k` is the matrix `(f | k f)` of the frame `f = (e₁, …, e_ϱ, z)` and its image. Suppose
all rows of `P` vanish except the two at the last index of `f` and of `k f`, which `lastIndices 𝔰 ρ`
lists, and that their determinant is a unit of the finite adeles. Then `meetNorm`, the norm of the
product of the places above `M` modulo which the spans of `f` and `k f` share a nonzero vector, is
at most the generalised index `genIndex` of the determinant: the inverse of the factor by which it
scales Haar measure. 

### `le_genIndex_det_of_le_meetNorm`

 Let `k` stabilize the lattice, and let its reduction agree. Let `t` be an integral matrix with
two columns, and let `P = (f | k f)ᴴ t` for the frame `f`. Suppose all rows of `P` vanish except the
two at the last index of `f` and of `k f`, which `lastIndices 𝔰 ρ` lists, and that their determinant
is a unit of the finite adeles. Let `x` be at most `meetNorm`, the norm of the product of the places
above `M` modulo which the spans of `f` and `k f` share a nonzero vector. Then `x` is at most the
generalised index of the determinant. 

 ## The cell rank of a term whose characters agree 

### `CharsAgree.exists_coords_ne_zero_of_common_vector`

 Let the characters of `γ` agree, and let `j` be the least index from which on one pair `(ζ, 1)`
with `ζ ζ̄ = 1` occurs as the coefficients of a common vector at all indices. Then a nonzero common
vector, with coordinates `x` in the frame `f` and `y` in `γ f`, has nonzero coordinates in both
frames at some index `l ≥ j`. 

### `CharsAgree.leadingMinor_ne_zero`

 Let the characters of `γ` agree: `S.unipotentChar` takes equal values on rational unipotent `u`,
`u'` with `u γ = γ u'`. Let `f = (e₁, …, e_ϱ, z)` be the frame. Let `j` be the least index such that
one pair `(ζ, 1)` with `ζ ζ̄ = 1` occurs as the coefficients of a vector common to the flags of `f`
and of `γ f` at all indices from `j` on. The matrix `S.frameProducts γ` has the entries
`h(f_a, γ f_b)`, where `h` is the hermitian form of the space, with Gram matrix `S.ratGram`. If
`j ≤ 𝔰.ϱ`, the leading minor of order `j` of this matrix is nonzero. 

### `CharsAgree.exists_hasCellRank`

 Let the characters of `γ` agree, and let `S.termDisc γ = 0`, which says that the spans of the
frame `f` and of `γ f` share a nonzero vector. Then `γ` has a cell rank `j`. That is, for one `ζ`
with `ζ ζ̄ = 1` the flags of `f` and of `γ f` share a vector with coefficients `ζ`, `1` at each
index from `j` on; the leading minor of order `j` of the matrix `S.frameProducts γ` of hermitian
products `h(f_a, γ f_b)` is nonzero; and `j ≤ ϱ`. 
