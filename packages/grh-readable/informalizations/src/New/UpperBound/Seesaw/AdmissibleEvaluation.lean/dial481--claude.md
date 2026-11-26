---
{
  "module": "src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite evaluation of edge pairs takes translates of the vacuum to admissible combinations

This file proves that the finite evaluation of a pair of edges takes translates of the vacuum to
admissible combinations. It first gives a test for membership in the lattice of a graded space whose
string has odd length. For a pair of edges it then builds an integral matrix `latticeLift`, whose
adjoint kills the shift and keeps denominators, and uses it to identify the image `L'` of `L ∩ I^⊥`
in `I^⊥ / I` with the neighbour lattice. Here `L` is the lattice of the vacuum and `I` is the
isotropic subspace of the splitting. It follows that the evaluation of a translate of the vacuum is
`0` or a root of unity times a translate of the zero term of the vacuum, and that this zero term is
a nonzero multiple of the sum of the translates of the vacuum by representatives of `L'`. The two
conditions `LiftsNeighbours` and `MatchesDenominators` are checked for the middle double lift and
for the last double lift.

Notions from other files:
* A `Space` is a hermitian space over `E` with a point, an adelic basis that is orthonormal at the
  finite places; the columns of its finite part `V.xFin` span the lattice of `V`. The space `V⁻` is
  `V` with the form negated, and `flipSum V V''` is `V⁻ ⊕ V''`.
* `Grading V N (X ⊕ Unit) m` presents `V` as the orthonormal vectors `X ⊕ Unit` plus a string of `m`
  basis vectors, in which vector `i` pairs only with vector `m - 1 - i`, to `1`, or to `-N` if it is
  the middle vector; `Grading.SpansLattice` says that the point of `V` spans the lattice of the
  basis `gradedLatticeBasis`, in which, for odd `m`, the last vector of `X ⊕ Unit` is glued to the
  middle vector of the string.
* `DoubleLiftData`, called a pair of edges `Y → Y' → Y''`, is the data of two consecutive lifts
  between graded spaces `V`, `V'`, `V''`. It identifies the part of grade zero of `V⁻ ⊕ V''` with
  `(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)` plus hyperbolic planes.
* `IsNeighbourVector π δ c x` lists the congruences that glue the last entries of a vector `x`
  indexed by `PairIndex X X'' = (X ⊕ Unit) ⊕ (X'' ⊕ Unit)` to the coefficient `c`.
* `selfOrConj β` is the allowed denominator: `β` on the first block of indices, `β̄` on the second.
* `IsScalingAtM N β δ κ` says that each factor of `κ` is `1` or `δ`, that `δ` has norm one and is
  `1` above `N`, that `β` is a unit above `N`, and that the denominators of `κ` are bounded by `β`
  and `β̄`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


 ## Membership in a glued lattice 

### `inv_xFin_mulVec_mem_of_spansLattice`

 Let the grading `Y` present the space `V` as `n₀ ⊕ Unit` plus a string of `m` vectors, and
suppose that the columns of `V.xFin`, the finite point of `V`, span the lattice of
`gradedLatticeBasis` for `a`, `π` and `u`, in which the last vector of `n₀ ⊕ Unit` is glued to the
middle of the string. Let `vec` have the component `x` in `n₀ ⊕ Unit`, the coordinate
`u * (π⁻¹ * x e + c)` at the middle vector of the string, where `e = Sum.inr ()` is the last index,
and `0` at the other vectors of the string. If `c`, `π̄ * x e` and the other entries of `x` are
integral, then `vec` lies in that lattice. 

### `flipScale`

 The finite idele by which negating the form of a space scales its point: the finite part of
the conjugate of `flipIdele` for `η = normNegOne`, a unit of `Ô E` with `η̄ η = -1`. 

### `coe_flipScale`

 The idele `flipScale E` is the conjugate of `η = normNegOne` times `ᾱ α⁻¹`, where `α` is the
finite idele of the Weil data. 

### `inv_xFin_flipSum`

 The inverse of the finite point of `V⁻ ⊕ V''` is block diagonal, with blocks the inverse point
of `V` divided by `flipScale E` and the inverse point of `V''`. 

### `inv_xFin_flipSum_mulVec_mem_iff`

 A vector `y` of finite adeles indexed by `ι ⊕ ι''` lies in the lattice of `V⁻ ⊕ V''`, that is
`(flipSum V V'').xFin⁻¹ *ᵥ y ∈ stdLattice`, exactly if its first block, divided by `flipScale E`,
lies in the lattice of `V` and its second block lies in the lattice of `V''`. 

### `_root_.New.Grading.gradeZeroRows`

 The rows of the finite part of the point of `V'` at the basis vectors of `X' ⊕ Unit`. 

### `_root_.New.Grading.isIntMatrix_gradeZeroRows`

 Let `Y'` present `V'` as `X' ⊕ Unit` plus a string of even length `m'`, and suppose that the
finite point of `V'` spans the lattice of `gradedLatticeBasis` for `a`, `π`, `u`. For even length
this basis is the identity on `X' ⊕ Unit` and scales the string vectors by `u a⁻¹` or `u ā`. Then
the rows of the point at `X' ⊕ Unit` are integral. 

### `_root_.New.Grading.conjTranspose_gradeZeroRows`

 The adjoint of the rows of the point of `V'` at `X' ⊕ Unit` consists of the columns of the
inverse point at these basis vectors, since the form of `V'` is `1` on them. 

### `liftVector`

 The vector of grade zero in `V⁻ ⊕ V''`, in rational coordinates, with the component `κ x` in
`X⁻ ⊕ X''` and the coefficient `u c` at the second basis vector of each plane; this coefficient
and the component in `X⁻` are multiplied by `flipScale E`. 

### `LiftsNeighbours`

 Every neighbour vector `(c, x)`, that is, every solution of the gluing congruences
`IsNeighbourVector π δ c x`, has its lift `liftVector` in the lattice of `V⁻ ⊕ V''`. 

### `MatchesDenominators`

 Where the inclusion of `X⁻ ⊕ X''` joins an index `b` to an index `i` of `V⁻ ⊕ V''`, the
denominator allowed at `i` has the valuations of the denominator allowed at `b` times `κ b`. 

### `neighbourLift`

 The matrix whose columns are the lifts of the columns of `neighbourMatrix`, in the coordinates
of the lattice of `V⁻ ⊕ V''`. 

### `planeCoeff`

 The coefficients of the lifted columns at the second basis vectors of the planes. 

### `isotropicCoeff`

 The coordinates, in the isotropic frame of the splitting of `Hom (V', V⁻ ⊕ V'')`, of the
isotropic part of the columns of `latticeLift` (see `latticeLift_eq_latticeUnitary_add_isotropic`):
zero at the indices of positive grade and `planeCoeff ⊗ 1` at the planes. 

### `latticeLift`

 The matrix `B` of the map `x ↦ A x R` from `Hom (X' ⊕ Unit, X⁻ ⊕ X'')` to
`Hom (V', V⁻ ⊕ V'')`, in the coordinates of the lattices, with `A = neighbourLift` and
`R = gradeZeroRows`. 

### `conjTranspose_latticeLift_mulVec_stackedStringMapFin`

 For a finite set of places `P`, an idele `π`, a unitary adele `u` and scaling factors `κ`, let
`B = latticeLift` be the matrix of `x ↦ A x R`. Here the columns of `A` are the lifts to `V⁻ ⊕ V''`
of the columns of `neighbourMatrix`, and `R` consists of the rows of the point of `V'` at
`X' ⊕ Unit`. Then `Bᴴ` kills `stackedStringMapFin`, the finite coordinates of the map
`V' → V⁻ ⊕ V''` made of the adjoint of `stringMap` for `V → V'` and of `stringMap` for `V' → V''`;
these maps only move vectors of the strings. 

### `latticeLift_eq_latticeUnitary_add_isotropic`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄`
with `π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling
factors with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele
`β` and its conjugate (`hκ`).
Let `D` be the data of two consecutive lifts between the graded hermitian spaces `V`, `V'`,
`V''`, and let `V⁻` be `V` with the form negated.
For a unitary adele `u`, let `B = latticeLift` be the matrix of `x ↦ A x R`, where the columns
of `A` are the lifts to `V⁻ ⊕ V''` (`liftVector` for `u` and `κ`) of the columns of
`neighbourMatrix` and `R` consists of the rows of the point of `V'` at `X' ⊕ Unit`.
Let `g = latticeUnitary` be the unitary `(κ γ) ⊗ 1`, with `γ = neighbourMatrix` and `κ` read as a
diagonal matrix. Then `B x` is the image of `g x` in `Hom (V', V⁻ ⊕ V'')` (by `iFin`) plus a vector
of the isotropic subspace `I` of the splitting of `D`. Its coordinates in the basis
`isotropicBasisFin` of `I` are `isotropicCoeff` applied to `x`: zero in positive grade and
`planeCoeff ⊗ 1` at the hyperbolic planes, which `q` indexes. So `B x` lies in `I^⊥` and has the
class `g x` in `I^⊥ / I`. 

### `isIntMatrix_latticeLift`

 Let `P` contain one place of each conjugate pair above `N`, let `π` be the matching idele and
`κ` scaling factors with values `1` or `δ`. Suppose that the point of `V'` spans the lattice of
its grading `Y'` and that all neighbour vectors lift to the lattice of `V⁻ ⊕ V''`. Then the matrix
`B = latticeLift` of the pair of edges `D : Y → Y' → Y''` is integral:
its columns lie in the lattice `L` of the vacuum of `Hom (V', V⁻ ⊕ V'')`. 

### `zeroTermLattice_splitting_eq`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄`
with `π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling
factors with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele
`β` and its conjugate (`hκ`).
Let `D` be the data of two consecutive lifts between the graded hermitian spaces `V`, `V'`,
`V''`, and let `V⁻` be `V` with the form negated. Suppose that the point of `V'` spans the
lattice of `gradedLatticeBasis` for `a`, `π`, `u'` (`hL`) and that every solution of the
congruences `IsNeighbourVector` lifts to the lattice of `V⁻ ⊕ V''` (`h_lift`). Let `L` be the
standard integral lattice of `Hom (V', V⁻ ⊕ V'')` and `I` the isotropic subspace of the splitting
of `D`. Then the image of `L ∩ I^⊥` in `I^⊥ / I` is `neighbourLattice`, the image of the standard
lattice under `latticeUnitary`. 

### `evalAt_liftVector_eq_zero`

 Let `D` be the data of two consecutive lifts between `V`, `V'`, `V''`, let the place `w` and its
conjugate `star w` lie outside `P`, and let `j` be an index of
`PairIndex X X'' = (X ⊕ Unit) ⊕ (X'' ⊕ Unit)`. Suppose that the entry `(l, j)` of the inclusion of
`(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)` in `V⁻ ⊕ V''` is zero. Then, for all `u` and `κ`, the lift of the
column `j` of `neighbourMatrix`, with its coefficient `neighbourCoeff` at the isotropic vectors, has
entry `l` vanishing at `star w`. 

### `evalAt_neighbourLift_eq_zero`

 Let `P` contain one place of each conjugate pair above `N` (`hP`), and let `κ` be scaling
factors with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele
`β` and its conjugate (`hκ`). Write `d = selfOrConj β`, which is `β` on the first block of indices
and `β̄` on the second. Suppose that `d l` and `d b * κ b` have the same valuation `v` at every
finite place whenever the entry `(l, b)` of the inclusion of `(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)` in
`V⁻ ⊕ V''` is nonzero (`h_match`). If `d i` and `d j * κ j` have different valuations at `w`, then,
for every idele `π` and unitary adele `u`, the entry `(i, j)` of `neighbourLift`, the matrix of the
lifted columns of `neighbourMatrix`, vanishes at the conjugate place `star w`. 

### `conjTranspose_latticeLift_mulVec_mem`

 Let `P` contain one place of each conjugate pair above `N` (`hP`) and let `κ` be scaling factors
with values `1` or `δ`, trivial above `N` (`hκ`). Let `D` be double-lift data for `Y`, `Y'`, `Y''`
whose matrix `B = D.latticeLift P π u κ` is integral (`h_int`) and whose denominators match through
`κ` (`h_match`). Then `Bᴴ` keeps the allowed denominators up to `κ`: if each entry of `y` in a row
`(i, i')`, times `selfOrConj β i`, is integral at the places not dividing `n`, then so is each entry
of `Bᴴ y` in a row `(j, j')`, times `selfOrConj β j * κ j`. 

### `latticeUnitary_mulVec_conjTranspose_latticeLift_mulVec`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄` with
`π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling factors
with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele `β` and
its conjugate (`hκ`). Let `D` be the data of two consecutive lifts between the graded hermitian
spaces `V`, `V'`, `V''`, and let `V⁻` be `V` with the form negated. For a unitary adele `u`, let
`B = latticeLift` be the matrix of `x ↦ A x R`, where the columns of `A` are the lifts to `V⁻ ⊕ V''`
(`liftVector` for `u` and `κ`) of the columns of `neighbourMatrix` and `R` consists of the rows of
the point of `V'` at `X' ⊕ Unit`. Let `g = latticeUnitary` be the unitary `(κ γ) ⊗ 1` with
`γ = neighbourMatrix`, and let `iFin` be the inclusion of
`Hom (X' ⊕ Unit, (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))` in `Hom (V', V⁻ ⊕ V'')` given by the splitting of `D`.
If `y` vanishes above `N`, then `g Bᴴ y` is the orthogonal projection `iFinᴴ y` of `y`. 

### `conjTranspose_iFin_mulVec_mem`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄` with
`π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling factors
with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele `β` and
its conjugate (`hκ`). Suppose that, for a unitary adele `u`, the matrix `latticeLift` built from the
lifted columns of `neighbourMatrix` is integral, that the denominators match through `κ`, and that
`y` vanishes above `N`. If each entry of `y` in a row `i`, times `selfOrConj β i`, is integral at
all places not dividing `n`, then the orthogonal projection `iFinᴴ y` of `y` to
`Hom (X' ⊕ Unit, (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))` has the same property. 

### `exists_finEval_finHeisenbergOp_vacElem`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄`
with `π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling
factors with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele
`β` and its conjugate (`hκ`).
Let `D` be the data of two consecutive lifts between the graded hermitian spaces `V`, `V'`,
`V''`, and let `V⁻` be `V` with the form negated.
Suppose that, for a unitary adele `u`, the matrix `latticeLift` built from the lifted columns of
`neighbourMatrix` is integral, and that `y` vanishes above `N`. Let `φ = vacElem` be the vacuum
(Gaussian times twisted lattice indicator) of `V'.hom (flipSum V V'') = Hom (V', V⁻ ⊕ V'')`. The
map `D.finEval` translates by `stackedStringMapFin`, takes the finite constant term `zeroTermFin`
along the splitting of `D`, and applies a left inverse of `arrowTensor`, the map that joins data on
`Hom (X ⊕ Unit, X' ⊕ Unit)` and on `Hom (X' ⊕ Unit, X'' ⊕ Unit)`. Its value on the Heisenberg
translate of `φ` by `y` is `0` or a root of unity times that left inverse applied to the constant
term of `φ` translated by the orthogonal projection `iFinᴴ y`. 

### `exists_zeroTermFin_splitting_vacElem_eq_sum`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄` with
`π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling factors
with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele `β` and
its conjugate (`hκ`). Let `D` be the data of two consecutive lifts between the graded hermitian
spaces `V`, `V'`, `V''`, and let `V⁻` be `V` with the form negated. Suppose that the point of `V'`
spans the lattice of `gradedLatticeBasis` for `a`, `π`, `u'` (`hL`) and that every solution of the
congruences `IsNeighbourVector` lifts, with `u` and `κ`, to the lattice of `V⁻ ⊕ V''` (`h_lift`).
Then the finite constant term `zeroTermFin`, along the splitting of `D`, of the vacuum of
`Hom (V', V⁻ ⊕ V'')` is a nonzero multiple of the sum of the translates of the vacuum of
`Hom (X' ⊕ Unit, (X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit))` by the vectors `neighbourCosetRep r`. These represent
`neighbourLattice`, the image of the standard lattice under `latticeUnitary`, modulo its integral
points. Here `r` consists of residues at `P`, which give the vector `neighbourTranslation` (rows
`η ȳ / N` and `-ȳ / N` at the two last indices for residues `y`, `η = normNegOne`), and a class
modulo integral points of vectors of `neighbourLattice` that vanish above `N`
(`AwayLatticeQuotient`); the representative is the sum of that vector and a member of the class. 

### `isAdmissibleEval_finEval`

 Let `P` contain one place of each conjugate pair above the prime `N` (`hP`), let `N = π π̄`
with `π` a uniformiser at the places of `P` and a unit elsewhere (`hπ`), and let `κ` be scaling
factors with values `1` or `δ`, trivial above `N`, with denominators bounded by the integral adele
`β` and its conjugate (`hκ`).
Let `D` be the data of two consecutive lifts between the graded hermitian spaces `V`, `V'`, `V''`,
with hyperbolic planes indexed by `q`, and let `V⁻` be `V` with the form negated. Suppose that the
point of `V'` spans the lattice of `gradedLatticeBasis` for `a`, `π`, `u'`, that the solutions of
the congruences `IsNeighbourVector` lift to the lattice of `V⁻ ⊕ V''`, and that the denominators
match through `κ`. The map `D.finEval` translates by `stackedStringMapFin`, takes the finite
constant term along the splitting of `D` and splits the result into a tensor. There is then a
constant `C` such that, for `n` prime to `N` and `y` with denominators `β` on `V⁻` and `β̄` on
`V''` away from `n`, it sends the vacuum translated by `y` to a finite combination of vectors
`C • gluedTranslate N P (t₁, t₂)` (the gluing of the tensor of the vacua translated by `t₁`, `t₂`)
with `β̄ t₁`, `β̄ t₂` integral away from `n`. The coefficients have a denominator away from `n`
that depends only on `β` and the index types, and absolute sum at most `1` under every automorphism
of `ℂ` (`IsAdmissibleEval`). 

### `liftsNeighbours_middleDoubleLift`

 Let `Y`, `Y'`, `Y''` present the hermitian spaces `V`, `V'`, `V''` as orthonormal vectors
`X ⊕ Unit`, `X' ⊕ Unit`, `X'' ⊕ Unit` plus strings of `m`, `m - 1`, `m - 2` further basis vectors,
paired in reverse order, with `m` odd and `Y.genericConst = Y'.genericConst` (`h_string`). Let
`m ≠ 1` and let `dim V + dim V''` be even. The middle vectors `z`, `z''` of the strings of `V`,
`V''` have norm `-N`, so `z + z''` is isotropic in `V⁻ ⊕ V''`. Suppose that the points (adelic bases
`xFin`) of `V` and `V''` span the lattices of `gradedLatticeBasis` for `a`, `π` and `u`, `u''`, and
that `s u = η̄ δ u''`, where `η = normNegOne` has `η̄ η = -1` and `s = flipScale E` scales the point
of `V⁻`. Let `e`, `e''` be the last indices of `X ⊕ Unit`, `X'' ⊕ Unit`, and let `(c, x)` satisfy
`IsNeighbourVector π δ c x`: `δ c = c`, the entries of `x` are integral except that `x e`, `x e''`
have denominator at most `π̄`, and `x e / π ≡ c`, `x e'' / π ≡ η̄ c` modulo integral adeles. Then
the lift of `(c, x)`, with component `s x` in `X ⊕ Unit`, `x` in `X'' ⊕ Unit` and coefficient
`s u c` at `z + z''`, lies in the lattice of `V⁻ ⊕ V''`. 

### `matchesDenominators_middleDoubleLift`

 In a middle pair (strings of lengths `m`, `m - 1`, `m - 2` with `m` odd and not `1`) the
inclusion of `(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)` in `V⁻ ⊕ V''` keeps each index in its block, so the
denominators `β` on the first block and `β̄` on the second match without any scaling. 

### `lastScaling`

 The scaling of the last pair: `δ` at the last basis vector of `X'' ⊕ Unit` and `1`
elsewhere. 

### `liftsNeighbours_lastDoubleLift`

 Let `Y`, `Y'`, `Y''` present the hermitian spaces `V`, `V'`, `V''` as orthonormal vectors
`X ⊕ Unit`, `X' ⊕ Unit`, `X''` plus strings of `1`, `0`, `0` further basis vectors, with
`Y.genericConst = Y'.genericConst` (`h_string`, `hm`). Let `V''` be standard, `dim V + dim V''` even
and `N = p p̄`. The string vector `z` of `V` has norm `-N`, so `z / p` has norm one in `V⁻`, which
is `V` with the form negated; `lastDoubleLift` identifies `V⁻ ⊕ V''` with
`(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)`. Suppose that `π` is the principal idele of `p`, that the point (adelic
basis `xFin`) of `V` spans the lattice of `gradedLatticeBasis` for `a`, `π`, `u`, and that
`s u = η̄ δ`, where `η = normNegOne` has `η̄ η = -1` and `s = flipScale E` scales the point of `V⁻`.
Let `e`, `e''` be the last indices of `X ⊕ Unit`, `X'' ⊕ Unit`, and let `(c, x)` satisfy
`IsNeighbourVector π δ c x`: `δ c = c`, the entries of `x` are integral except that `x e`, `x e''`
have denominator at most `π̄`, and `x e / π ≡ c`, `x e'' / π ≡ η̄ c` modulo integral adeles. Then
the lift of `(c, x)`, with component `s x` in `X ⊕ Unit`, `x` in `X''` and coefficient `δ x e'' / p`
at `z`, lies in the lattice of `V⁻ ⊕ V''`; there is no hyperbolic plane, so `u c` does not enter the
lift. 

### `matchesDenominators_lastDoubleLift`

 Let `Y`, `Y'`, `Y''` present the hermitian spaces `V`, `V'`, `V''` as orthonormal vectors
`X ⊕ Unit`, `X' ⊕ Unit`, `X''` plus strings of `m = 1`, `m' = 0`, `m'' = 0` further basis vectors,
with `Y.genericConst = Y'.genericConst` (`h_string`, `hm`). Let `dim V + dim V''` be even and
`N = p p̄`. In `lastDoubleLift` the last basis vector `e''` of `X'' ⊕ Unit` is `z / p` for the
string vector `z` of `V⁻`. If, for the integral adele `β`, `β̄ δ` and `β` have the same valuation at
every finite place, then the denominators of indices joined by the inclusion of
`(X ⊕ Unit)⁻ ⊕ (X'' ⊕ Unit)` in `V⁻ ⊕ V''` have the same valuations after the scaling `lastScaling`,
which is `δ` at `e''` and `1` elsewhere. 
