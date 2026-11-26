---
{
  "module": "src/New/UpperBound/Seesaw/NeighbourLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The neighbour lattice of a pair of edges

Take definite spaces with bases indexed by `X ⊕ Unit`, `X'` and `X'' ⊕ Unit`, written `X`, `X'`,
`X''` for short, and let `e` and `e''` be the last basis vectors of the first and of the third. An
explicit unitary carries the standard lattice of `Hom (X', X⁻ ⊕ X'')` to `neighbourLattice`. Away
from `N` this lattice is the standard one with scaled rows. Above `N` it is a neighbour of the
standard lattice, and the translations `neighbourTranslation` represent it modulo its integral
points. The sums `neighbourCosetRep` of these and of scaled rows away from `N` represent the whole
lattice modulo its integral points.

Notions from other files:
* `𝔸f E` is the ring of finite adeles of the CM field `E` and `Ô E` its subring of integral adeles;
  `star` is complex conjugation and `idem S` is the adele that is `1` on `S` and `0` off it.
* `IsSplitLevel P N`: the places above the prime `N` are those in `P` and their conjugates, all
  split of degree one and unramified.
* `IsSplitSquarefree P N π`: the idele `π` is a uniformiser on `P` and a unit elsewhere,
  `N = π π̄`, and `P` does not meet its conjugate.
* `stdLattice E ι` consists of the vectors with integral entries, `integralBox ι S` of those whose
  entries are integral at the places of `S`; `S.conjClosure` is `S` with its conjugate places.
* `residueOverN y` is the adele `y / N` at `P`, for residues `y` modulo `N` at the places of `P`.
* `Gf E ι` is the group of unitary matrices over `𝔸f E` with rows and columns indexed by `ι`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `selfOrConj`

 The denominators allowed on `X⁻ ⊕ X''`: the integral adele `β` on the first block of indices
and its conjugate on the second. 

### `mem_weightedTranslations`

 A vector `x` lies in `weightedTranslations q d` if and only if, for each index `i` and each
finite place `w` not dividing `q`, the absolute values `v` at `w` of `d i` and `x i` have product at
most one. 

### `conjTranspose_mulVec_mem_weightedTranslations`

 The group `weightedTranslations q d` consists of the vectors `y` with denominators `d` away from
`q`: for every index `i` and every place `w` not dividing `q` one has `v (d i w) * v (y i w) ≤ 1`.
The adjoint of an integral matrix `M` maps this group to the one for `d'`, provided that `M i j`
vanishes at the conjugate place `star w` whenever `d i` and `d' j` have different valuations at
`w`. 

### `star_mem_weightedTranslations`

 If `x` lies in `weightedTranslations q d`, then `i ↦ c * star (x (f i))` lies in
`weightedTranslations q` for `i ↦ star (d (f i))`. Here `c` is integral (`hc`) and `f` is any change
of indices. 

### `PairIndex`

 The basis indices of the sum `X⁻ ⊕ X''` of two definite spaces: those of the first space are
`X ⊕ Unit` and those of the second `X'' ⊕ Unit`, `Unit` indexing a last basis vector. 

### `PairIndex.lastSource`

 The index of the last basis vector `e` of the first space. 

### `PairIndex.lastTarget`

 The index of the last basis vector `e''` of the second space. 

### `IsNeighbourVector`

 The gluing conditions on a vector `x` of `X⁻ ⊕ X''` and an adele `c`, which in the application
is the coefficient of an isotropic vector: `x` is integral except at `e` and `e''`, where it has
denominator at most `π̄`, and its entries there, divided by `π`, are congruent to `c` and `η̄ c`. 

### `IsNeighbourVector.mul_coeff`

 The coefficient `c` is unchanged by `δ`. 

### `IsNeighbourVector.mem_of_ne`

 The entries other than those at `e` and `e''` are integral. 

### `IsNeighbourVector.star_mul_mem`

 All entries have denominator at most `π̄`. 

### `IsNeighbourVector.sub_source_mem`

 The entry at `e`, divided by `π`, differs from `c` by an integral adele. 

### `IsNeighbourVector.sub_target_mem`

 The entry at `e''`, divided by `π`, differs from `η̄ c` by an integral adele, where `η` is the
  unit `normNegOne` of norm `-1`. 

### `IsScalingAtM`

 The factors `κ` by which the rows of the standard lattice are scaled at the places dividing
`β` and `β̄`: each is `1` or a fixed adele `δ` of norm one, and nothing happens above `N`. In the
application `β β̄` is the auxiliary level `M` and `δ` generates the ideal `(β / β̄)`. 

### `IsScalingAtM.mul_star_self_eq_one`

 `δ` has norm one. 

### `IsScalingAtM.apply_eq_one`

 `δ` is `1` above `N`. 

### `IsScalingAtM.v_eq_one`

 `β` is a unit above `N`. 

### `IsScalingAtM.eq_one_or_eq`

 Each factor is `1` or `δ`. 

### `IsScalingAtM.star_mul_mem`

 Each factor has denominator at most `β̄`. 

### `IsScalingAtM.selfOrConj_mul_mem`

 The factors on `X⁻` have denominator at most `β`, those on `X''` at most `β̄`. 

### `neighbourAxis`

 The vector `ρ = e + η̄ j̄ e''`, where `j` is the idempotent of `P` and `η` the unit of norm
`-1`. It is `e` except at the places conjugate to `P`, where it is `e + η̄ e''`. It has norm one
when `P` is disjoint from its conjugate. 

### `neighbourScale`

 The adele `A` such that, when `P` is disjoint from its conjugate, `1 + A` is `π` at `P`, `π̄⁻¹`
at the conjugate places and `1` elsewhere. 

### `neighbourMatrix`

 The matrix `γ = 1 + A ρ ρ*`. When `P` is disjoint from its conjugate, so that `ρ` has norm one,
it scales `ρ` by `1 + A` and fixes its orthogonal complement; its columns then span a neighbour at
`N` of the standard lattice. 

### `neighbourCoeff`

 The coefficient of the isotropic vector that goes with each column of `neighbourMatrix`; it is
zero except for the columns of `e` and `e''`. 

### `neighbourTranslation`

 The translation `n y` attached to residues `y` at `P`: the matrix with row `η ȳ / N` at `e`,
row `-ȳ / N` at `e''` and zero elsewhere. It is supported at the places conjugate to `P`. 

### `conjTranspose_mul_one_add_smul_vecMulVec`

 The matrix that scales a unit vector `ρ` by a factor `1 + A` of norm one and fixes its
orthogonal complement is unitary. 

### `IsSplitSquarefree.one_sub_idem_mul_inv_mem`

 If `π` is a uniformiser on `P` and a unit elsewhere, then `π⁻¹` is integral off `P`. 

### `IsScalingAtM.apply_mul_star_eq_one`

 Every scaling factor has norm one. 

### `IsScalingAtM.idem_mul`

 If the places above `N` are `P` and its conjugate, the scaling adele `δ`, which is `1` above
`N`, is `1` at `P`. 

### `IsScalingAtM.star_idem_mul`

 If the places above `N` are `P` and its conjugate, the scaling adele `δ`, which is `1` above
`N`, is `1` at the places conjugate to `P`. 

### `star_mul_neighbourScale_mem`

 Let `N = π π̄` with `π` a uniformiser on `P` and a unit elsewhere, and let `P` be disjoint from
its conjugate (`IsSplitSquarefree`). The adele `A = neighbourScale P π`, which is `π - 1` at `P`,
`π̄⁻¹ - 1` at the conjugate places and `0` elsewhere, has denominator at most `π̄`: the product
`π̄ A` is integral. 

### `neighbourScale_apply_of_notMem`

 The adele `neighbourScale P π` vanishes at each place outside `P` and its conjugate. 

### `star_one_add_neighbourScale_mul`

 Let `π` be split squarefree for `N` at the finite set of places `P` (`IsSplitSquarefree`):
`N = π π̄`, the idele `π` is a uniformiser at each place of `P` and a unit at all others, and no
place of `P` has its conjugate in `P`. For `A = neighbourScale P π` the adele `1 + A`, which is `π`
at `P`, `π̄⁻¹` at the conjugate places and `1` elsewhere, has norm one: its product with its own
conjugate is `1`. 

### `neighbourMatrix_apply`

 The entries of `γ = 1 + A ρ ρ*`, where `A = neighbourScale P π` and
`ρ = neighbourAxis X X'' P`. 

### `neighbourMatrix_apply_of_notMem`

 Off `P` and its conjugate, `γ = neighbourMatrix X X'' P π` is the identity. 

### `neighbourCoeff_apply_of_notMem`

 The coefficient `neighbourCoeff X X'' P π m` attached to each column `m` of `neighbourMatrix`
has component `0` at every place `w` outside `P` and its conjugate. 

### `mul_neighbourCoeff`

 Let `P` and its conjugates be the places above the prime `N` (`IsSplitLevel`). Let `δ` be the
scaling adele of `IsScalingAtM`, which is `1` above `N`. Then multiplying by `δ` does not change the
coefficient `neighbourCoeff X X'' P π m` of the isotropic vector that goes with column `m` of
`neighbourMatrix`. 

### `neighbourCoeff_sub_lastSource`

 Let `π` be split squarefree for `N` at `P`: `N = π π̄`, `π` is a uniformiser on `P` and a unit
elsewhere, and `P` does not meet its conjugate. The matrix `γ = neighbourMatrix X X'' P π` is
`1 + A ρ ρ*`, with rows and columns indexed by the bases of two spaces with last vectors `e`
(index `lastSource`) and `e''` (index `lastTarget`); here `A = neighbourScale P π`,
`j = idem P` is `1` at `P` and `0` elsewhere, `η = normNegOne` has norm `-1`, and
`ρ = e + η̄ j̄ e''`. The adele `neighbourCoeff X X'' P π m` is `A π⁻¹ j̄` for the column of `e`,
`A π⁻¹ η j` for that of `e''` and `0` for the others. This lemma computes it minus `π⁻¹` times
the entry `γ lastSource m`: it is `-ϖ` if `m` is the index of `e` and `0` otherwise, where
`ϖ = j + (1 - j) π⁻¹` is `1` at `P` and `π⁻¹` elsewhere. 

### `star_normNegOne_mul_neighbourCoeff_sub_lastTarget`

 Let `π` be split squarefree for `N` at `P`: `N = π π̄`, `π` is a uniformiser on `P` and a unit
elsewhere, and `P` does not meet its conjugate. The matrix `γ = neighbourMatrix X X'' P π` is
`1 + A ρ ρ*`, with rows and columns indexed by the bases of two spaces with last vectors `e`
(index `lastSource`) and `e''` (index `lastTarget`); here `A = neighbourScale P π`,
`j = idem P` is `1` at `P` and `0` elsewhere, `η = normNegOne` has norm `-1`, and
`ρ = e + η̄ j̄ e''`. The adele `neighbourCoeff X X'' P π m` is `A π⁻¹ j̄` for the column of `e`,
`A π⁻¹ η j` for that of `e''` and `0` for the others. This lemma computes `η̄` times it minus
`π⁻¹` times the entry `γ lastTarget m`: it is `-ϖ` if `m` is the index of `e''` and `0`
otherwise, where `ϖ = j + (1 - j) π⁻¹` is `1` at `P` and `π⁻¹` elsewhere. 

### `idem_conjClosure_mul_neighbourCoeff`

 The coefficients of the isotropic vector are supported above `N`. 

### `isNeighbourVector_col_neighbourMatrix`

 Suppose that the places above the prime `N` are `P` and its conjugate, that `N = π π̄` with `π`
a uniformiser on `P` and a unit elsewhere, and that `κ` are factors `1` or `δ` for an adele `δ` of
norm one that is `1` above `N`, with the denominators bounded by `β` and `β̄` (`IsScalingAtM`). Let
`x` be column `m` of `γ = neighbourMatrix X X'' P π = 1 + A ρ ρ*` and `c` its coefficient
`neighbourCoeff`. Then `δ c = c`; `x` is integral except at `e` and `e''`; all of `π̄ x` is
integral; and `c - π⁻¹ x_e` and `η̄ c - π⁻¹ x_e''` are integral, with `η = normNegOne` of norm `-1`.
These are the conditions `IsNeighbourVector`. 

### `star_neighbourAxis_dotProduct`

 The inner product of `ρ = e + η̄ j̄ e''` with a vector `x` is the sum of the entry at `e` and
`η j` times the entry at `e''`, where `j` is the idempotent of `P` and `η` the unit of norm `-1`. 

### `star_neighbourAxis_dotProduct_self`

 The vector `ρ = neighbourAxis X X'' P` satisfies `star ρ ⬝ᵥ ρ = 1` when `π` is a split
squarefree idele for `N` at `P` (`hπ`), so that `P` is disjoint from its conjugate. 

### `neighbourMatrix_mulVec`

 Multiplication by `γ = neighbourMatrix X X'' P π` adds to a vector `x` the multiple `A ⟨ρ, x⟩ ρ`
of `ρ`. Here `A` is `neighbourScale P π`, `ρ` is `neighbourAxis X X'' P`, and `⟨ρ, x⟩ = x
lastSource + normNegOne * idem P * x lastTarget`. 

### `neighbourUnitary`

 The matrix `γ` (`neighbourMatrix`) as a finite point of the unitary group, for a split
squarefree idele `π` for `N` at `P`. 

### `coe_neighbourUnitary`

 The matrix of `neighbourUnitary` is `γ`. 

### `IsScalingAtM.idem_mul_apply`

 If `N` is prime, `P` is a split level for `N` (`IsSplitLevel P N`) and `κ` satisfies
`IsScalingAtM N β δ κ`, then each factor `κ i` is `1` at the places of `P`:
`idem P * κ i = idem P`. 

### `IsScalingAtM.star_idem_mul_apply`

 If `N` is prime, `P` is a split level for `N` (`IsSplitLevel P N`) and `κ` satisfies
`IsScalingAtM N β δ κ`, then each factor `κ i` is `1` at the places conjugate to `P`:
`star (idem P) * κ i = star (idem P)`. 

### `commute_neighbourMatrix_diagonal`

 At a level prime `N` split as `P` and its conjugate, the matrix `γ` commutes with the diagonal
matrix of the scaling factors `κ`: it differs from `1` only above `N`, where all of these factors
are `1`. 

### `scalingUnitary`

 The diagonal matrix of the factors `κ`, each of which has norm one, as a finite point of the
unitary group. 

### `vanishingAbove`

 The vectors that vanish at the places of `P` and at their conjugates. For a split level `N`
these are the places above `N`. 

### `sub_idem_smul_mem_vanishingAbove`

 The part of a vector off `P` and its conjugate vanishes at these places. 

### `kroneckerOne`

 The homomorphism `g ↦ g ⊗ 1`. Its values act on matrices with columns indexed by `X'` by left
multiplication with `g`. 

### `latticeUnitary`

 The unitary `(γ κ) ⊗ 1`. It carries the standard lattice of `Hom (X', X⁻ ⊕ X'')` to the lattice
that is the neighbour above `N` and has its rows scaled by `κ` elsewhere. 

### `neighbourLattice`

 The image of the standard lattice under `latticeUnitary`. For a pair of edges it is the lattice
`zeroTermLattice` of their splitting, by `DoubleLiftData.zeroTermLattice_splitting_eq`. 

### `awayLattice`

 The elements of the lattice that vanish above `N`. 

### `AwayLatticeQuotient`

 The classes of `awayLattice` modulo its integral points. Only the rows scaled by `δ` can fail
to be integral. 

### `coe_kroneckerOne`

 The matrix of `g ⊗ 1` is the Kronecker product of that of `g` with the identity. 

### `kroneckerOne_smul`

 The action of `g ⊗ 1` on a matrix `x` multiplies each column of `x` by `g`. 

### `star_idem_mul_star_residueOverN`

 The conjugate of `residueOverN y` (the adele `y w / N` at `w ∈ P`, `0` elsewhere) is unchanged
by multiplication with the conjugate of `idem P`, so it is supported at the places conjugate to
`P`. 

### `star_idem_mul_neighbour_add_translation`

 Let `π` be split squarefree for `N` at `P`, `j = idem P` the adele `1` at `P` and `0` elsewhere
and `η = normNegOne` of norm `-1`. The matrix `x` has rows indexed by `PairIndex X X''`, with last
indices `e = lastSource` and `e'' = lastTarget`, and columns by `X'`. Let
`γ = neighbourMatrix X X'' P π`, let `ρ = neighbourAxis X X'' P = e + η̄ j̄ e''` and, for residues
`y` modulo `N` at the places of `P`, let `n y = neighbourTranslation X X'' y` be the matrix with row
`η ȳ / N` at `e`, row `-ȳ / N` at `e''` and zero elsewhere. After multiplication by `j̄`, each
column of `γ x + n y` is that of `x` plus `ρ` times `j̄ (π̄⁻¹ x_e + η ȳ / N) - j̄ x_e`. 

### `exists_class_star_idem_mul_mem_iff`

 Let the prime `N` be split as `P` and its conjugate, let `π` be split squarefree for `N` at `P`,
let `η = normNegOne` have norm `-1` and, for residues `y` modulo `N` at the places of `P`, let
`residueOverN y` be the adele `y / N` at `P` and `0` elsewhere. Multiplication by the conjugate of
`idem P` keeps only the places conjugate to `P`. If `t` is integral there, then `π̄⁻¹ t + η ȳ / N`
is integral there for exactly one family of residues `y`, and otherwise for none. 

### `exists_add_neighbourTranslation_mem_iff`

 Let the prime `N` be split as `P` and its conjugate and `π` split squarefree for `N` at `P`.
`kroneckerOne` lets the unitary `γ` act on each column. Let `η = normNegOne` have norm `-1`. For
residues `y` modulo `N` at `P`, `n y = neighbourTranslation X X'' y` has row `η ȳ / N` at `e`, row
`-ȳ / N` at `e''` and zero elsewhere. At the places conjugate to `P`, `γ x + n y` is integral for
exactly one `y` if `x` is integral there, and for none otherwise. 

### `star_idem_smul_neighbourTranslation`

 The translation `n y = neighbourTranslation X X'' y` is supported at the places conjugate to
`P`: multiplication by `star (idem P)`, the idempotent `j̄` of these places, fixes it. 

### `kroneckerOne_scalingUnitary_smul`

 The element `scalingUnitary hκ ⊗ 1`, where `scalingUnitary hκ` is the diagonal matrix of the
factors `κ`, multiplies row `i.1` of a matrix `x` by `κ i.1`. 

### `coe_latticeUnitary`

 At a level prime `N` split as `P` and its conjugate, the matrix of `latticeUnitary` is
`(diagonal κ * γ) ⊗ 1`, where `γ = neighbourMatrix X X'' P π`. 

### `latticeUnitary_smul`

 Acting by `latticeUnitary` means scaling the rows by `κ`, then acting by `γ ⊗ 1`. 

### `latticeUnitary_smul_of_mem_vanishingAbove`

 Let `π` be split squarefree for `N` at `P`, and let `κ` be row factors that are `1` or a fixed
adele `δ` of norm one (`IsScalingAtM`). The unitary `latticeUnitary` is `(γ κ) ⊗ 1` for
`γ = neighbourMatrix X X'' P π`. On a matrix `x` that vanishes at `P` and its conjugate, where `γ`
acts trivially, it multiplies row `b` by `κ b`. 

### `mem_neighbourLattice_iff_of_mem_vanishingAbove`

 Let `π` be split squarefree for `N` at `P`. Let `κ` be row factors that are `1` or a fixed adele
`δ` of norm one, with denominators bounded by `β` and `β̄` (`IsScalingAtM`). Off `P` and its
conjugate, `neighbourLattice` is the standard lattice with its rows scaled by `κ`: a matrix `x` that
vanishes at `P` and its conjugate lies in it if and only if `κ⁻¹ x = κ̄ x` has integral entries. 

### `awayLattice_le_weightedTranslations`

 Let `π` be split squarefree for `N` at `P`, and let `κ` be row factors of norm one with
denominator at most `β` in the first block and `β̄` in the second (`IsScalingAtM`). An element of
`awayLattice`, the part of `neighbourLattice` that vanishes at `P` and its conjugate, is `κ` times
an integral matrix. So its rows, times `β` in the first block and `β̄` in the second, are integral
at every place, in particular at those not dividing `n`, as `weightedTranslations n` asks. 

### `card_awayLatticeQuotient_dvd`

 Let `π` be split squarefree for `N` at `P` (`IsSplitSquarefree`): `N = π π̄`, `π` is a
uniformiser on `P` and a unit elsewhere, and `P` does not meet its conjugate. Let `κ` be row factors
that are `1` or a fixed adele `δ`, with denominator at most `β̄` (`IsScalingAtM`). The matrices have
rows indexed by `PairIndex X X''`, the basis indices of a sum of two definite spaces, and columns
indexed by `X'`. The group `awayLattice` consists of the matrices in `neighbourLattice` that vanish
at `P` and its conjugate. `AwayLatticeQuotient` is its quotient by the matrices all of whose entries
lie in the integral adeles `Ô E`. The order of this quotient divides the number of such matrices
with entries in `Ô E ⧸ (β)`. 

### `neighbourTranslation_mem_neighbourLattice`

 Let the prime `N` be split as `P` and its conjugate, let `N = π π̄` with `π` a uniformiser on
`P` and a unit elsewhere, and let `κ` be row factors that are `1` or `δ`, where `δ` is `1` above `N`
(`IsScalingAtM`). Then every translation `n y` attached to residues `y` modulo `N` at `P` lies in
`neighbourLattice`, the image of the standard lattice under `(γ κ) ⊗ 1` for
`γ = neighbourMatrix X X'' P π`. 

### `idem_mul_neighbour_add_translation_mem`

 Let `N = π π̄` with `π` a uniformiser on `P` and a unit elsewhere, and let `P` be disjoint from
its conjugate (`IsSplitSquarefree`). An adele is integral at `P` if its product with `idem P`,
which is `1` at `P` and `0` elsewhere, is integral. The matrices have rows indexed by
`PairIndex X X''`, with last indices `e` and `e''`, and columns by `X'`; `kroneckerOne` lets the
unitary `γ` (`neighbourUnitary`, with matrix `neighbourMatrix X X'' P π`) act on each column, and
`n y = neighbourTranslation X X'' y` has row `η ȳ / N` at `e` and `-ȳ / N` at `e''`, both
supported at the places conjugate to `P`. If `z` is integral at `P`, then so is `γ z + n y`: at
`P`, `γ` is integral and `n y` is `0`. 

### `existsUnique_add_neighbourTranslation_mem`

 Let the prime `N` be split as `P` and its conjugate, let `N = π π̄` with `π` a uniformiser on
`P` and a unit elsewhere, and let `κ` be row factors that are `1` above `N` (`IsScalingAtM`). Above
`N` the translations `n y` represent `neighbourLattice` modulo its integral points: for each element
`x` there is exactly one family `y` of residues modulo `N` at `P` such that `x + n y` is integral at
`P` and its conjugate, the places above `N`. 

### `idem_conjClosure_smul_neighbourTranslation`

 Under `hπ`, the translations `n y = neighbourTranslation X X'' y` are supported above `N`:
multiplication by the idempotent `idem` of `P` and its conjugate places fixes them. 

### `neighbourCosetRep`

 The representative `n y + t`, where `n y = neighbourTranslation X X'' y` is attached to residues
`y` at `P` and `t` is the chosen representative of a class in `AwayLatticeQuotient`. 

### `neighbourCosetRep_mem_neighbourLattice`

 Let `N` be prime, `IsSplitLevel P N`, `IsSplitSquarefree P (N : E) π` and
`IsScalingAtM N β δ κ`. Then `neighbourCosetRep a` lies in `neighbourLattice X' hπ hκ`, the image of
the standard lattice under `latticeUnitary`. 

### `existsUnique_sub_neighbourCosetRep_mem`

 Let the prime `N` be split as `P` and its conjugate, let `N = π π̄` with `π` a uniformiser on
`P` and a unit elsewhere, and let `κ` be row factors that are `1` above `N` (`IsScalingAtM`). Then
each `z` in `neighbourLattice` differs by a matrix with integral entries (`stdLattice`) from
`neighbourCosetRep (y, q)` for exactly one pair `(y, q)`. Here `y` is a family of residues modulo
`N` at `P`, `q` is a class of lattice elements vanishing above `N` modulo integral ones, and
`neighbourCosetRep (y, q)` is `neighbourTranslation X X'' y` plus the chosen representative of
`q`. 
