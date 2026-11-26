---
{
  "module": "src/New/Spanning/RemainingTerms/Cut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Cut.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Cut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The cut: from the lattice of a link to the vectors common to two links

Let `A` be the span of `e₁, …, e_ϱ`, `Λ` the lattice of a class and `M` the level. The vectors of
`Λ` orthogonal to `A` and `γ A` whose part in `A` is divisible by `M` give a lattice `L⁺_γ` in the
link of a term `γ`. We descend from it to its intersection with the link of a second term `γ'`,
and from there to the part orthogonal to `z⁺` and `Υ_γ⁻¹ z⁺`, which lies in
`L_γ = S.termLattice c c' γ`. The last step costs at most a principal minor of their Gram matrix.
So the discriminant of this part, times the torsion index `S.torsionIndex`, the discriminant of
the projection to the complement of the intersection and a gain `x` from the places where the
residue meets, is at most the gauge `S.levelGauge` of the term (`nonempty_linkSplitting` below).

* `New.Filling.HasCellRank.abs_norm_minor_gram_linkVectors_mul_le`,
  `New.Filling.minorNorm_sq_le_linkDiscSq_mul`: the cost of the cut, in the three cases of rank
  `0`, `1` and `2`. The first bounds the principal minors of the Gram matrix of the two vectors;
  the second is the resulting lower bound for the discriminant of a lattice in the link on whose
  span the `z`-forms are injective.
* `New.Filling.LinkSplitting`, `New.Filling.nonempty_linkSplitting`: the splitting of a link along
  its intersection with a second link.
* `New.Filling.HasIntegralLifts.isIntMatrix_linkForm`: for two terms over one block, the form
  `S.linkForm / M` is integral on pairs of lifts.

Notions from other files:

* `New.link γ`: the space of pairs (class of `y`, class of `γ⁻¹ y`) in `(A^⊥ / A)²`, with `y`
  orthogonal to `A` and `γ A`. Here `A^⊥ / A = X₀ ⊥ E z` with `z` of norm `-N`, and the link is
  the graph of an isometry `Υ_γ` of `X₀ ⊥ E z⁺`, with `z⁺` of norm `N`.
* `New.Filling.linkDiscSq`: for a rational basis `v` and an adelic change of basis `e`,
  `S.linkDiscSq v e` is the squared discriminant of the lattice `v e` for `S.linkMetric`, which on
  the link is the form of `X₀ ⊥ E z⁺`.
* `New.Filling.HasIntegralLifts`, `New.Filling.HasLevelLifts`: the columns of a matrix are the
  images in the link of vectors of `Λ` orthogonal to `A` and `γ A`, respectively lie in `L⁺_γ`.
* `New.Filling.termsOver`: `S.termsOver c s c'` is the block of rational `γ` whose matrix in the
  bases of the lattices of `c` and `c'` is integral with reduction `s`.


### `zRowBlockDiagonal_mul_linkMatrix_mul_classCoord`

 Let `n = S.classCoord c * finAdeleMatrix t * w` be the coordinates of the adelic combinations
`t w` of rational vectors in the basis of the lattice of the class `c`. Let
`k = S.translateByClassReps c c' γ` be the matrix of `γ` in the bases of the lattices of `c` and
`c'`. The products with `z` on both halves (`zRowBlockDiagonal`) for `S.latticeMiddle` take the same
values on `linkMatrix k * n` as those for `S.ratMiddle` take on `linkMatrix γ * t * w`. 

### `isotropicFramePair_mul_classCoord_eq_zero`

 Let the columns of the rational matrix `t` be orthogonal to `A` and `γ A`
(`isotropicFramePair γ`). Then the coordinates of the adelic combinations `t w` in the basis of the
lattice of the class `c` are orthogonal to `A` and `k A`, where `k` is the matrix of `γ` in the
bases of the lattices of `c` and `c'`. 

### `toRows_classCoord_mul`

 If the first half of the images `linkMatrix γ * t * w` of adelic combinations `t w` of rational
vectors is a matrix `p` in `X₀`, the middle part of the coordinates of `t w` in the basis of the
lattice of the class `c` is `S.classCoordX₀ c * p`. 

### `HasLevelLifts.exists_orthogonal_split`

 Let the columns of `m` be orthogonal to those of `y` for `S.linkMetric`, and let the columns of
`(m | y) f` lie in the lattice `L⁺_γ` of the link of `γ` for the class `c` (`HasLevelLifts c γ`).
Then there are adelic changes of basis `a`, `v` and a shear `z` such that the columns of `m a` and
of `m z + y v` lie in `L⁺_γ`, and the squared discriminant `S.linkDiscSq` of `(m | y) f` is the
product of those of `m a` and `y v`. 

### `HasIntegralLifts.le_genIndex_det_zRowBlockDiagonal`

 Let `γ` be a term over the classes `c`, `c'` with reduction `s`, where `s` is compatible with
the unipotent character (`S.Agrees s`), and let the columns of `w` have integral lifts. Let `ρ`
choose rows among the two `z`-forms `zRowBlockDiagonal`, such that the minor of their values on `w`
is a unit of the finite adeles. Then the generalised index `genIndex` of the minor is at least `x`,
if `x` is at most the norm `S.meetNorm s` of the product of the places with `S.MeetsAt s`, and if
both forms are chosen unless `x = 1`. 

### `HasCellRank.abs_norm_minor_gram_linkVectors_mul_le`

 Let `γ` have cell rank `j ≤ ϱ + 1` (`S.HasCellRank`): in particular the leading minor of order
`j` of the matrix of products of the standard frame with its image under `γ` is nonzero. Take a
principal minor of order `r`, on the indices chosen by `ρ`, of the Gram matrix of `z⁺` and
`Υ_γ⁻¹ z⁺` (`linkVectors γ`), where `r = 2` is allowed only at the top cell rank `j = ϱ + 1`. Its
absolute norm is at most `(G / μ) ^ 2`. Here `μ = S.minorNorm j γ` is the normalised norm of that
leading minor, and `G` is the maximum of `N ^ f * μ` and of `S.termDiscNorm γ`, the product of the
moduli of the discriminant `S.termDisc γ` of the frames. The prime `N = S.N` of the filling is the
norm of `z⁺`, and `f` is the number of infinite places. 

### `minorNorm_sq_le_linkDiscSq_mul`

 **The part seen by the `z`-forms.** Let `γ` have cell rank `j` and be a term over the classes
`c`, `c'` with reduction `s`, where `s` is compatible with the unipotent character (`S.Agrees s`).
Let the `r` columns of `y` lie in the link, where `r ≤ 2`, and `r ≤ 1` unless `j = ϱ + 1`. Let the
two `z`-forms `zRowBlockDiagonal` be injective on their span, and let them take the same values on
the basis `y v` as on a matrix `w` that has integral lifts. Then the squared discriminant of the
lattice with basis `y v` is at least `(x * μ / G) ^ 2`. Here `μ = S.minorNorm j γ` is the normalised
norm of the leading minor of order `j` of the products of the frames, and `G` is the maximum of
`S.termDiscNorm γ` and `N ^ f * μ`, where the prime `N = S.N` of the filling is the norm of `z⁺` and
`f` is the number of infinite places. The number `x` is at most the norm `S.meetNorm s` of the
product of the places with `S.MeetsAt s`, and `x = 1` unless `r = 2`. 

### `submoduleIndex_termLattice`

 Let `V` be a subspace of `X₀` and let `Λ` be the lattice of the class `c`. Let the frame be
`e₁, …, e_ϱ, z`, with isotropic part `A` spanned by `e₁, …, e_ϱ`, and let
`k = S.translateByClassReps c c' γ`. The index of `Λ ∩ V ∩ L_γ` in the saturated lattice `Λ ∩ V`
(`saturatedLattice`) is read on the products with the image of the frame under `k`. It is the index,
in the module of the products of vectors of `Λ ∩ V` with this image, of those products that are `M`
times the products of a vector of `Λ ∩ A`. 

### `toRows₁_mul_eq_fromRows_zero`

 Let the columns of `m` be pairs of vectors of `X₀ ⊕ E z` on which both `z`-forms, the products
with `z` on the two halves, vanish. Then the first half of any adelic combination `m a` of them
lies in `X₀`: its `z`-coordinate is zero. 

### `gram_linkMetric_eq_gram_toRows₁`

 Let the columns of `m` lie in the link of `γ`, and let both `z`-forms vanish on them. Their Gram
matrix for `S.linkMetric` is the standard Gram matrix of their parts in `X₀`. 

### `HasLevelLifts.discriminant_sq_le`

 **The part in `X₀`.** Let `m` have a left inverse. Let its columns span a subspace of `link γ`
on which both `z`-forms vanish: `zRowBlockDiagonal (S.ratMiddle E) * m = 0`, the rows indexed by `z`
in each copy. Let `p = m.toRows₁.toRows₁` be the parts in `X₀`. Let the lattice with basis `m a` lie
in `L⁺_γ` (`HasLevelLifts`): it has integral lifts whose part in `A` is divisible by the level `M`.
Let `V` be the span of the columns of `p`. Let `L` be the intersection of `saturatedLattice` of `V`
with `L_γ = S.termLattice c c' γ`. Then `r = finrank E V`, and `L` is a lattice of rank `r`. Its
squared discriminant is at most `S.linkDiscSq m a`, the squared discriminant of `m a`, as `L`
contains the columns of `p a`. 

### `LinkSplitting`

 A splitting of the link of `γ` along its intersection with the link of `γ'`, with a complement
of rank `i` and a lattice in it whose vectors have integral lifts modulo the intersection. The
discriminant of this lattice, times `x`, the torsion index of `γ` and the discriminant of
`S.commonPart`, the part of `L_γ` common to the two links, is at most the gauge
`𝗀* = S.levelGauge j c c' γ`. 

### `LinkSplitting.CommonIndex`

 The index set of a family that spans the intersection of the links. 

### `LinkSplitting.commonCols`

 A family that spans the intersection of the links. 

### `LinkSplitting.complCols`

 A basis of a complement of the intersection in the link of `γ`. 

### `LinkSplitting.complLattice`

 The lattice in the complement has the basis `complCols * complLattice`. 

### `LinkSplitting.complShear`

 The coefficients of the vectors of the intersection that are added to the basis vectors. 

### `LinkSplitting.colSpan_common`

 The columns of `commonCols` span the intersection of the links. 

### `LinkSplitting.colSpan_compl_le`

 The complement lies in the link of `γ`. 

### `LinkSplitting.eq_zero_of_mulVec_mem`

 The columns of `complCols` are independent modulo the intersection. 

### `LinkSplitting.colSpan_fromCols`

 The intersection and the complement span the link of `γ`. 

### `LinkSplitting.hasIntegralLifts`

 The basis vectors, moved along the intersection by `complShear`, have integral lifts. 

### `LinkSplitting.isLatticeOfRank_commonPart`

 The part of `L_γ` common to the two links is a full lattice in `commonLink γ γ'`. 

### `LinkSplitting.discriminant_sq_mul_le`

 The bound by the gauge, squared. 

### `HasCellRank.finrank_link_inf_le`

 Let `γ` have cell rank `j ≤ ϱ + 1` (`S.HasCellRank`). The dimension of the intersection of the
links of `γ` and `γ'` exceeds that of `commonLink γ γ'`, the vectors of `X₀` that both links send
to one vector of `X₀`, by at most `2`, and by at most `1` unless `j = ϱ + 1`. 

### `HasCellRank.finrank_link_inf_eq_add_two`

 Let `γ` have the top cell rank `j = ϱ + 1`, and let the links of `γ` and `γ'` be equal, that is,
of corank `S.linkCorank γ γ' = 0`. Then the dimension of their intersection exceeds by `2` that of
`commonLink γ γ'`, the vectors of `X₀` that both links send to one vector of `X₀`. 

### `IsKernelExtension.card_add_eq_finrank`

 Let `y` extend `x` to a basis of `L` by `r` columns in the kernel of `A` (`IsKernelExtension`).
Then the numbers of columns of `x` and `y` add up to the dimension of `L`. 

### `nonempty_linkSplitting`

 **The splitting.** Let `γ` be a term of cell rank `j` over the classes `c`, `c'` with reduction
`s`, where `s` is compatible with the unipotent character (`S.Agrees s`). Let `x` be a natural
number that is at most the norm `S.meetNorm s` of the product of the places with `S.MeetsAt s`, and
that is `1` unless `j = ϱ + 1` and the links of `γ` and `γ'` are equal. Then there is a
`LinkSplitting`, which consists of the following. Its `complCols` are a basis of a complement of the
intersection of the two links in the link of `γ`, of rank `S.linkCorank γ γ'`, the codimension of
the intersection. Its `complLattice` is a lattice in the complement whose basis vectors have
integral lifts modulo the intersection. The part `S.commonPart c c' γ γ'` of the lattice `L_γ` of
the term that is common to the two links is a full lattice in `commonLink γ γ'`. Finally
`(t * d * x) ^ 2 * D ≤ 𝗀* ^ 2`. Here `t` is the torsion index `S.torsionIndex` of the matrix of
`γ` in the bases of the lattices of `c` and `c'`, `d` is the discriminant of the common part, `D` is
the squared discriminant of the lattice in the complement, and the gauge
`𝗀* = S.levelGauge j c c' γ` is a power of the congruence level `M` times `S.minorGauge j c c'
γ / (S.N ^ f * S.minorNorm j γ)` times the larger of `S.termDiscNorm γ` and
`S.N ^ f * S.minorNorm j γ`, with `f` the number of infinite places. 

### `HasIntegralLifts.isIntMatrix_linkForm`

 Let `γ` and `γ'` be terms over the classes `c`, `c'` with the same reduction `s` modulo the
level `M = S.M`. Let `w` and `w'` have integral lifts (`HasIntegralLifts`): their columns are the
images, in the links of `γ` and `γ'`, of vectors of the lattice of `c`. Then the products of the
columns of `w` with those of `w'` for the form `S.linkForm / M` are integral adeles. Here
`S.linkForm = diag(T, -T)` on two copies of `X₀ ⊕ E z`, of Gram matrix `T`. 
