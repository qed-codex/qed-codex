---
{
  "module": "src/New/UpperBound/Seesaw/EdgePairEvaluation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite zero terms and the evaluation of pairs of edges in the tower of spaces `Y_k`

For a splitting `D` of a hermitian space `V`, the zero term `D.zeroTerm` along its isotropic frame
is split into a real and a finite part, `New.Seesaw.zeroTermFin D`. For spaces presented by
`New.Grading` as a definite part plus a string of basis vectors, the part of grade zero gives
splittings. On `V⁻ ⊕ V''` this leads to a splitting down to `Hom (X', X⁻ ⊕ X'')` and an evaluation
of finite data, and both are equivariant for `New.Seesaw.tripleWeil`. This evaluation is then
applied to the tower `New.Data.spaceY k`, `k ≤ m = 2 ϱ + 2`, two lifts at a time; here `m` and `ϱ`
are the natural numbers `New.Data.m` and `New.Data.ϱ`.

## Main definitions and results

Throughout, a *string* of a grading is the block of basis vectors outside the definite part, and
`DoubleLiftData` records two successive steps `Y → Y' → Y''` where the first step makes the string
one shorter and the second, unless the string is already empty, makes it shorter by one.

* `New.Seesaw.zeroTermFin`: the finite part of the zero term. It obeys the law of the zero term for
  finite points of the parabolic subgroup (`New.Seesaw.zeroTermFin_omega`) and is not zero at the
  vacuum (`New.Seesaw.zeroTermFin_vacElem_ne_zero`).
* `New.Seesaw.GradeZeroPart`, `New.Seesaw.GradeZeroPart.splitting`: the part of grade zero, and the
  splitting it gives.
* `New.Seesaw.DoubleLiftData`: the part of grade zero of `V⁻ ⊕ V''` is `X⁻ ⊕ X''` plus hyperbolic
  planes. `New.Seesaw.middleDoubleLift` (one plane) and `New.Seesaw.lastDoubleLift` (none) are the
  two instances.
* `New.Seesaw.DoubleLiftData.splitting`, `New.Seesaw.DoubleLiftData.finEval`: the splitting down to
  `Hom (X', X⁻ ⊕ X'')` and the evaluation of finite data.
  `New.Seesaw.DoubleLiftData.zeroTerm_splitting_tripleWeil` and
  `New.Seesaw.DoubleLiftData.finEval_arrowProduct_equivariant` show that both are equivariant.
* `New.Data.doubleLiftEvalY`: the evaluation of the pair `Y_{2i} → Y_{2i+1} → Y_{2i+2}`, by
  `New.Seesaw.middleDoubleLift` for `i < ϱ` and `New.Seesaw.lastDoubleLift` for `i = ϱ`.
* `New.Data.translatedPointDatumY`, `New.Data.evaluatedDatum`: the data `New.Data.pointDatumY` moved
  by finite adelic points of the unitary groups, and their evaluation.

Notions from other files:
* `New.Space E n s`: a hermitian space with a point, given by a matrix `J` over `E` and `x` in
  `GL_n(𝔸)` with `xᴴ J x` equal to `diag s` at the infinite places and `1` at the finite places.
  `𝒮 V` is its space of data, with the Weil operators `V.ω g` and the Heisenberg operators `V.ϱ y`.
* `New.Space.Splitting`: dual isotropic frames `l`, `k` with columns indexed by `p` and an isometry
  `i : V₀ → V` onto their orthogonal complement.
* `New.Space.Splitting.zeroTerm`: the bounded map `𝒮 V → 𝒮 V₀` that sends `f` to the function whose
  value at `y` is the mean of `f (i y + k b)` over `b` in `𝔸 ^ p` modulo `E ^ p`.
* `New.Space.finHeisenbergOp`: the Heisenberg operator of a finite adelic vector `x` on `𝒮 V`; it
  translates by `α x`, with `α` the finite idele of `New.WeilData`.
* `New.Data.spaceY`: the hermitian space `Y_k` with its adelic frame, chosen as in
  `New.Data.exists_space_isStd_of_le_and_gram_eq_of_lt`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work. See `Lib.Weil.MixedModel.ZeroTerm` for
sources.



## The finite part of the zero term and the support of its translates

* `New.Seesaw.zeroTermFin_mem_finitePart`, `New.Seesaw.exists_zeroTerm_rho_integrated_eq`:
  `zeroTermFin D` preserves the finite parts and computes `D.zeroTerm` on pure tensors.
* `New.Seesaw.exists_zeroTermFin_finHeisenbergOp_add`: its values on the finite translates of the
  vacuum.
* `New.Seesaw.mem_zeroTermLattice_iff_selfDualAddChar`,
  `New.Seesaw.exists_zeroTermFin_vacElem_eq_sum`: the lattice `New.Seesaw.zeroTermLattice D` is
  unimodular, and the value at the vacuum is a multiple of a sum of translates of the vacuum by
  vectors of this lattice.

`V.integrated v f` is the tensor of a real Fock vector `v` with `f`, `V.finHeisenbergOp x` the
Heisenberg operator of a finite adelic vector `x`, `V.finitePart` the span of the
`V.finHeisenbergOp x`-translates of the vacuum, and `New.stdLattice` the standard lattice `Ô ^ n`.


### `zeroTermFin`

 The finite part of the zero term along the splitting `D` of `V` over `V₀`. It is the map
`f ↦ D.zeroTerm (v ⊗ f)`, where `⊗` is `V.integrated` and `v` is the Fock vacuum moved by the real
part of a chosen point `g` of the unitary group with `D.IsAdapted g 1` (the frame of `D` moved by
`g⁻¹` is orthonormal at the infinite places and integral at the finite places). 

### `zeroTermFin_eq`

 With `g` the adapted point chosen in the definition, `zeroTermFin D` undoes the finite part
`g.2` of `g`, projects on the real vacuum (`V.projReal`), applies the Weil operator `V.ω g` and
takes the zero term. 

### `exists_zeroTermFin_ne_zero`

 Let `D` be a splitting of `V` over `V₀`: dual isotropic frames `k`, `l` with columns indexed by
`p` and an isometry of `V₀` onto their orthogonal complement. The finite part
`zeroTermFin D : 𝒮 V → 𝒮 V₀` of the zero term along `k` does not vanish on `V.finitePart`, the span
of the finite Heisenberg translates of the vacuum. 

### `zeroTermFin_omega`

 The law of the zero term on the parabolic subgroup holds for its finite part and finite points:
if `g k = k a` for the isotropic frame `k` of `D`, with `det a = d`, and `g` acts on `V₀` as `g₀`,
then `zeroTermFin D` carries `ω g` to `(chiAdelic d)⁻¹ • ω g₀`. Here
`chiAdelic d = υ(d) |d| ^ (-1 / 2)`, with `υ` the splitting character of `New.WeilData` and `|d|`
the idele norm. This is a corollary of `New.Space.Splitting.zeroTerm_omega`. 

### `zeroTermFin_mem_finitePart`

 Let `D` be a splitting of `V` over `V₀`, with isotropic frame `k` indexed by `p`. The finite
part `zeroTermFin D : 𝒮 V → 𝒮 V₀` of the zero term along `k` sends `V.finitePart`, the span of the
finite Heisenberg translates of the vacuum, into `V₀.finitePart`. 

### `exists_zeroTerm_rho_integrated_eq`

 Let `D` be a splitting of `V` over `V₀`. The zero term along the isotropic frame of `D` carries
a translated pure tensor to a pure tensor: for an adelic vector `y` and a real Fock vector `v` of
`V` there is a real Fock vector `v₀` of `V₀`, independent of `f`, such that the zero term of
`ϱ(y) (v ⊗ f)` is `v₀ ⊗ zeroTermFin D (ϱ_f(α⁻¹ y_f) f)`, where `ϱ_f` is `V.finHeisenbergOp`, `⊗` is
`integrated` and `α⁻¹ y_f` is `finCoord y`. 

### `zeroTermFin_finHeisenbergOp_finFrameVector`

 Let `D` be a splitting of `V` over `V₀`, with isotropic frame `k`, dual frame `l` and embedding
`i` of `V₀`. In `D.finFrameVector g t a w b` the frame is moved by `g` and `t`; with both equal to
`1` and `a = 0` it is the vector `z = i w + k b`. Then `zeroTermFin D`, the finite part of the zero
term along `k`, carries translation of `V` by `z` to translation of `V₀` by `w`. 

### `exists_sub_orthogonal_of_zeroTermFin_ne_zero`

 Let `D` be a splitting of `V`, `k = D.kAdelic.map snd` the finite part of its isotropic frame
and `k^⊥` the kernel of `kᴴ`. Let `M * M'ᴴ = 1` and let `f` be fixed by the finite Heisenberg
operators of all `M x` with `x` in the standard lattice `Ô ^ n`. If `zeroTermFin D`, the finite part
of the zero term along `k`, does not vanish at the translate of `f` by `y`, then
`y ∈ M' Ô ^ n + k^⊥`. 

### `_root_.New.Space.Splitting.iFin`

 The finite part of the embedding of `V₀` in `V`, in the coordinates of the lattices. 

### `_root_.New.Space.Splitting.isotropicBasisFin`

 The finite part of the isotropic frame, in the coordinates of the lattice. Its columns span the
isotropic subspace `I`. 

### `zeroTermLattice`

 The lattice `L'` of `V₀ = I^⊥ / I`: the image of `L ∩ I^⊥`, where `L` is the standard lattice
of `V` and `I` is spanned by the columns of `k = D.isotropicBasisFin`. A vector of `I^⊥` is written
`i w + k b` with `i = D.iFin`, and `w` is its class. 

### `finFrameVector_zero`

 With `g = 1`, `t = 1` and no component `a` along the dual frame `l`, `D.finFrameVector` is
`D.iFin *ᵥ w + D.isotropicBasisFin *ᵥ b`, the finite vector `i w + k b`. 

### `conjTranspose_isotropicBasisFin_iFin_mulVec_finFrameVector`

 For the vector `D.finFrameVector 1 1 a w b = l a + i w + k b`, the coordinates `a` along the
dual frame `l` and `w` along `V₀` are its products with the columns of `k = D.isotropicBasisFin` and
of `i = D.iFin`. 

### `exists_eq_iFin_add_isotropicBasisFin_of_mulVec_eq_zero`

 A finite adelic vector orthogonal to the columns of the isotropic frame
`k = D.isotropicBasisFin` has the form `i w + k b`, where `i = D.iFin` is the embedding of `V₀`. 

### `exists_eq_add_of_zeroTermFin_ne_zero`

 The finite zero term of the vacuum translated by `y` is `0` unless `y = i w + k b + l` with `l`
in the standard lattice, where `i = D.iFin` embeds `V₀` and `k = D.isotropicBasisFin` is the
isotropic frame. 

### `exists_finHeisenbergOp_add_vacElem`

 The translates of the vacuum under the finite Heisenberg operators of `x` and of `x + l`, with
`l` in the standard lattice `Ô ^ n`, agree up to a root of unity. 

### `exists_zeroTermFin_finHeisenbergOp_add`

 For `y = i w + k b + l` with `l` in the standard lattice, `i = D.iFin` and
`k = D.isotropicBasisFin`, the finite zero term of the vacuum translated by `y` is a root of unity
times the translate by `w` of the finite zero term of the vacuum. 

### `zeroTermFin_vacElem_ne_zero`

 The finite part `zeroTermFin D` of the zero term along a splitting `D` does not vanish at the
vacuum `V.vacElem`. 

### `finHeisenbergOp_zeroTermFin_vacElem`

 For a splitting `D` of `V` over `V₀`, the translations by vectors of the lattice
`zeroTermLattice D` of `V₀` fix the value of the finite zero term `zeroTermFin D` at the vacuum. 

### `exists_omega_vacElem_eq_sum`

 Let `W` be a hermitian space over `E` with a point, `s` the signs of its form at the infinite
places, and let `g` be in `Gf E n`, the finite adelic unitary group. Thus `(1, g)` is the adelic
point with trivial infinite part and `W.ω (1, g)` is its Weil operator. Let `Λ = Ô ^ n` be the
standard lattice and let the `r a` be representatives of `g Λ` modulo `g Λ ∩ Λ`. Then this operator
sends the vacuum to a nonzero multiple of the sum of the finite Heisenberg translates of the vacuum
by the `r a`. 

### `conjTranspose_mulVec_iFin_add_isotropicBasisFin`

 Let `i = D.iFin` be the embedding of `V₀` and `k = D.isotropicBasisFin` the isotropic frame. For
`B = i g + k c` with `g` unitary, the adjoint of `B` sends `i w + k b` to `g⁻¹ w`. 

### `map_stdLattice_le_zeroTermLattice`

 Let `D` be a splitting of `V` over `V₀`, with finite parts `i = D.iFin` of the embedding of `V₀`
and `k = D.isotropicBasisFin` of the isotropic frame. If `g` is unitary and `B = i g + k c` has
entries in `Ô`, then `zeroTermLattice D` contains `g Ô ^ n₀`. 

### `mem_zeroTermLattice_iff`

 Let `D` be a splitting of `V` over `V₀`, with finite parts `i = D.iFin` of the embedding of `V₀`
and `k = D.isotropicBasisFin` of the isotropic frame. The lattice `zeroTermLattice D` consists of
the `w` with `i w + k b ∈ Ô ^ n` for some `b`. If `g` is unitary and `B = i g + k c` has entries in
`Ô`, then this lattice is `g Ô ^ n₀`: a vector `w` lies in it if and only if `g⁻¹ w ∈ Ô ^ n₀`. 

### `exists_isIntMatrix_iFin_mul_add_isotropicBasisFin_mul`

 Let `D` be a splitting of `V` over `V₀`, with finite parts `i = D.iFin` of the embedding of `V₀`
and `k = D.isotropicBasisFin` of the isotropic frame, whose columns are indexed by `p`. There are a
finite point `g` of the unitary group of `V₀` and a matrix `c` such that `i g + k c` has entries in
`Ô`. 

### `exists_zeroTermLattice_eq_map`

 The lattice `L' = zeroTermLattice D` is the image of the standard lattice of `V₀` under a finite
point of the unitary group. 

### `mem_map_stdLattice_iff_selfDualAddChar`

 For a finite point `g` of the unitary group, the image `g Ô ^ n` of the standard lattice is its
own dual: it consists of the `w` with `selfDualAddChar E (x* w) = 1` for all `x` in it. Here
`selfDualAddChar E` is the character of the finite adeles for which `Ô` is self-dual. 

### `mem_zeroTermLattice_iff_selfDualAddChar`

 The lattice `L' = zeroTermLattice D` is unimodular: it consists of the `w` with
`selfDualAddChar E (x* w) = 1` for all `x` in `L'`. 

### `zeroTermLattice_eq_map_of_le`

 If `L' = zeroTermLattice D` contains the image of the standard lattice under a unitary element,
the two lattices are equal, because each is its own dual. 

### `relIndex_map_stdLattice_ne_zero`

 For `g` unitary and `Λ` the standard lattice, `g Λ ∩ Λ` has finite index in `g Λ`. 

### `relIndex_zeroTermLattice_ne_zero`

 For a splitting `D` of `V` over `V₀`, the quotient `L' / (L' ∩ L°)` is finite, where
`L' = zeroTermLattice D` and `L°` is the standard lattice of `V₀`. So finite families of
representatives as in `exists_zeroTermFin_vacElem_eq_sum` exist. This is a corollary of
`exists_zeroTermLattice_eq_map`. 

### `exists_zeroTermFin_vacElem_eq_sum`

 Let `D` be a splitting of `V` over `V₀`, with embedding `i = D.iFin` and isotropic frame
`k = D.isotropicBasisFin`. Let `L' = zeroTermLattice D` be the lattice of the `w` with
`i w + k b ∈ Ô ^ n` for some `b`, and let the `r a` be representatives of `L'` modulo `L' ∩ Ô ^ n₀`.
Then `zeroTermFin D` sends the vacuum of `V` to a nonzero multiple of the sum of the finite
Heisenberg translates of the vacuum of `V₀` by the `r a`. 

### `exists_zeroTermFin_finHeisenbergOp_eq_smul`

 Let `D : V.Splitting V₀ p` be a splitting: `i = D.iFin` embeds `V₀` in `V` and the columns of
`k = D.isotropicBasisFin`, indexed by `p`, are an isotropic frame orthogonal to it. Let
`B = i g + k c` be integral with `g` unitary. Then `zeroTermFin D` sends the vacuum translated by
`y` to `0` or to a root of unity times the translate by `y₀ = g Bᴴ y` of its value at the vacuum. 


## Grade zero parts and equivariant splittings of the seesaw

Three hermitian spaces `V, V', V''` are each presented (`New.Grading`) as a definite part `X`, `X'`,
`X₀` plus a string of basis vectors. They are graded by `New.Grading.gradeOf`, which is zero on the
definite part. The three unitary groups act on data on `Hom (V', V⁻ ⊕ V'')` by
`New.Seesaw.tripleWeil`. For a splitting `D` of a space (`New.Space.Splitting`), `D.zeroTerm` is the
constant term along its isotropic frame, and `New.Seesaw.zeroTermFin D` is its finite part.


### `GradeZeroPart`

 For integer weights (grades) on the basis of `V`, with `V.J` pairing only opposite weights: a
rational isometry from `V''` onto the span of the basis vectors of weight zero. 

### `GradeZeroPart.index`

 An injection that labels the indices of grade zero by the basis indices of `V''`. 

### `GradeZeroPart.mem_range_index`

 The image of the injection is the set of indices of grade zero. 

### `GradeZeroPart.incl`

 The matrix of the inclusion of `V''` in `V`. 

### `GradeZeroPart.incl_eq_zero`

 The inclusion has no component along basis vectors of nonzero grade. 

### `GradeZeroPart.gram_incl`

 The inclusion pulls the Gram matrix of `V` back to that of `V''`. 

### `GradeZeroPart.grade_add_eq_zero`

 The Gram matrix of `V` pairs two basis vectors only if their grades add up to zero. 

### `ratCoordMatrix_sum`

 In rational coordinates, a pair of unitary points acts on `V ⊕ V'` by a block diagonal
matrix. 

### `GradeZeroPart.J_eq_zero_of_add_ne_zero`

 The Gram matrix of `V` vanishes at two indices whose weights are not opposite. 

### `GradeZeroPart.proj_pos_mul_J`

 The Gram matrix pairs weight `a` only with weight `-a`, so it intertwines the projections to the
positive and to the negative weights. 

### `GradeZeroPart.inv_J_apply_eq_zero_of_pos`

 The inverse of the Gram matrix of `V` vanishes at two indices of positive weight. 

### `GradeZeroPart.card_pos_eq_card_neg`

 There are as many basis indices of positive weight as of negative weight. 

### `GradeZeroPart.splitting`

 The splitting of `V` over its weight-zero part `V''` whose isotropic frame `k` consists of the
basis vectors of positive weight; `inclMatrix E u` has the basis vectors `e_{u j}` as columns. 

### `GradeZeroPart.hom`

 If `V''` is the weight-zero part of `V`, all weights are even and `Y'` has a string of even
length, then `Hom(X', V'')` is the weight-zero part of `Hom(V', V)`. 

 ### Pairs of consecutive edges 

### `stackedStringMap`

 The adelic map (T*, T') from V' to V⁻ ⊕ V'', where T* is the adjoint of
`T = Y.stringMap Y' : V → V'` and `T' = Y'.stringMap Y'' : V' → V''`. 

### `stackedStringMapFin`

 The finite part of `New.Seesaw.stackedStringMap`, in the frame coordinates of Hom(V', V⁻ ⊕ V''),
multiplied by α⁻¹. 

### `inclX_mul_stringMap_mul_inclX_inv`

 The map `Y.stringMap Y'` kills `X` and has image in the string, so the groups of `X`, `X'` fix
it. 

### `HasConsecutiveStrings`

 The strings of `Y`, `Y'`, `Y''` have lengths `s`, `s - 1` and `s - 1 - 1` (truncated
subtraction) with `s` odd, and `Y` and `Y'` have the same constant `genericConst`. 

### `HasConsecutiveStrings.odd_length`

 The string of `Y` has odd length. 

### `HasConsecutiveStrings.length_middle`

 The string of `Y'` is one shorter than that of `Y`. 

### `HasConsecutiveStrings.length_last`

 The string of `Y''` is one shorter than that of `Y'`, or both are empty. 

### `HasConsecutiveStrings.c_eq`

 The gradings `Y` and `Y'` have the same constant for the generic character. 

### `DoubleLiftData`

 Data for two consecutive lifts Y → Y' → Y'' with consecutive strings
(`New.Seesaw.HasConsecutiveStrings`) and `card ι + card ι''` even. It identifies the grade-zero part
of V⁻ ⊕ V'' with X⁻ ⊕ X'' plus q hyperbolic planes, compatibly with U(X) × U(X₀) and with
`stackedStringMap`. 

### `DoubleLiftData.zeroPart`

 The part of grade zero of `V⁻ ⊕ V''` is the sum of hyperbolic planes indexed by `q` and of
  `I_X⁻ ⊕ I_{X''}`. 

### `DoubleLiftData.even_card_add`

 The dimensions of `V` and `V''` have even sum. 

### `DoubleLiftData.embX`

 A homomorphism from the adelic unitary group of `I_{X₀}` to that of `I_{X''}`. 

### `DoubleLiftData.det_embX`

 The homomorphism preserves determinants. 

### `DoubleLiftData.intertwines`

 The inclusion of the part of grade zero intertwines `(g, k)`, acting on `V⁻ ⊕ V''` through `X`
  and `X₀`, with the element that is `1` on the planes, `g` on `X` and the image of `k` under the
  homomorphism on `X''`. 

### `DoubleLiftData.gradeOne`

 An injection of `q` into the basis indices of `V'` of grade one. 

### `DoubleLiftData.stackedStringMap_apply`

 In the rows of grade zero, column `gradeOne k` of `stackedStringMap Y Y' Y''` is
  `Y'.genericConst` times the included second basis vector of the `k`-th plane. The columns outside
  the image of `gradeOne` vanish. 

 ### The finite evaluation and its equivariance 

### `even_length_middle`

 The string of the middle grading `Y'` has even length, as `s' = s - 1` with `s` odd. 

### `even_gradeOf`

 All grades on `V⁻ ⊕ V''` are even: the string of `Y` has odd length, and that of `Y''` has odd
length or is empty. 

### `homZeroPart`

 For a pair `D` of consecutive lifts, `Hom(X', Z)` is the part of grade zero of
`Hom(V', V⁻ ⊕ V'')`, where `Z` is the part of grade zero of `V⁻ ⊕ V''`. 

### `splitting`

 The splitting of Hom(V', V⁻ ⊕ V'') that removes first the maps of nonzero degree, then the
maps into the hyperbolic planes, leaving Hom(X', X⁻ ⊕ X''). 

### `finEval`

 The linear map on joined finite data for `Hom(V, V')` and `Hom(V', V'')`. It translates by (T*,
T'), takes the finite constant term along `New.Seesaw.DoubleLiftData.splitting`, and splits the
result by a left inverse of `arrowTensor` into data for `Hom(X, X')` and `Hom(X', X'')`. 

### `arrowTensor_finEval`

 `arrowTensor` applied to `D.finEval (arrowProduct Φ.val Ψ.val)` equals `zeroTermFin D.splitting`
of `arrowProduct Φ.val Ψ.val` after the finite Heisenberg operator of `stackedStringMapFin Y Y' Y''`
on `Hom(V', V⁻ ⊕ V'')` is applied to it. 

### `_root_.New.Seesaw.GradeZeroPart.zeroTerm_hom_omega`

 Let `Z` identify `V''` with the part of weight zero of `V` for even weights `w`: `Z.incl` is the
inclusion, and `ε`, `ε''` are the signs of the two forms at the infinite places. Let `Y'` present
`V'` as the definite space on `X'` plus a string of `s'` further basis vectors, `s'` even, with
`Y'.inclX` the embedding of `U(X')` in `U(V')`. Suppose that, in rational coordinates
(`ratCoordMatrix`), `g` is the identity away from weight zero and acts as `g₀` on `V''`. Then
`Z.hom Y' hs' hw` identifies `Hom (X', V'')` with the part of weight zero of `Hom (V', V)`, and the
zero term along the resulting splitting carries the Weil operator of `(Y'.inclX h, g)` to that of
`(h, g₀)`, times `υ(det g ^ (s' / 2) * (det h)⁻¹ ^ r)⁻¹`. Here `r` is the number of indices of
positive weight and `υ` is the splitting character on the norm-one ideles (`upsilonU1`). 

### `zeroTerm_splitting_tripleWeil`

 Let `Y`, `Y'`, `Y''` present hermitian spaces `V`, `V'`, `V''` as definite spaces on `X`, `X'`,
`X₀` plus strings of `s` (odd), `s' = s - 1` and `s'' = s - 1 - 1` further basis vectors. The data
`D` of this pair of steps identify the part of weight zero of `V⁻ ⊕ V''` with `X⁻ ⊕ X''` plus
hyperbolic planes indexed by `q`, and map `U(X₀)` to `U(X'')` by `D.embX`. For characters `a`, `b`
of `[U(1)]`, the operator `tripleWeil a b (g, g', k)` on `Hom (V', V⁻ ⊕ V'')` is the Weil operator
of `(g', g ⊕ k)` times three scalar characters: that of `(g, g')` made from `a`, that of `(g', k)`
made from `b`, and one made from the splitting character `υ` and the ranks of `V'` and `V`.

The zero term along `D.splitting`, down to `Hom (X', X⁻ ⊕ X'')`, carries this operator at
`(g, g', k)`, embedded by `inclX`, to the same operator of the definite spaces at
`(g, g', D.embX k)`, with no further scalar. 

### `finEval_arrowProduct_equivariant`

 Let `Y`, `Y'`, `Y''` present `V`, `V'`, `V''` as definite spaces on `X`, `X'`, `X₀` plus strings
of lengths `s` (odd), `s - 1` and `s - 1 - 1`, and let the data `D` identify the part of weight zero
of `V⁻ ⊕ V''` with `X⁻ ⊕ X''` plus hyperbolic planes indexed by `q`; `D.embX` maps `U(X₀)` to
`U(X'')`. Finite data are elements of `finitePart`, the span of the finite translates of the vacuum.
`arrowProduct` joins such data `Φ` on `Hom (V, V')` and `Φ'` on `Hom (V', V'')`, and `D.finEval`
sends the result to a tensor of finite data on `Hom (X, X')` and `Hom (X', X'')`.

This evaluation is equivariant: if `Φ`, `Φ'` are moved by finite points `g, g', k` of the unitary
groups of `X, X', X₀`, embedded by `inclXFin`, then the tensor moves by `(g, g')` and `(g', k')`,
where `D.embX (1, k) = (1, k')`. 

 ### The two kinds of pairs 

### `middleDoubleLift`

 The pair data for strings of lengths s (odd, s ≠ 1), s − 1 and s − 2, with
`Y'.genericConst = Y.genericConst` and `card ι + card ι''` even: one hyperbolic plane, spanned by
the middle vectors z of Y and z' of Y'', is removed. 

### `lastDoubleLift`

 The pair data for s = 1 (so Y' and Y'' have no string), N = pp̄,
`Y'.genericConst = Y.genericConst` and `card ι + card ι''` even: no plane is removed, and z/p, z the
string vector of Y, is adjoined to X₀ as last basis vector of X''. 

 ## Gradings of the Y_k and evaluation of consecutive pairs of edges 

### `gradingY`

 The grading of `Y_k` as `X_k` plus a string of length `2 ϱ + 1 - k`, indexed by
`D.indexEquivY k`. As `D.m = 2 ϱ + 2`, the hypothesis says `k < D.m` and the length is
`D.m - 1 - k`. The constant of the generic character, `-(j * (D.M * P.deltaE D.towerExp))⁻¹` with
`j` the purely imaginary element of `New.WeilData`, does not depend on `k`. 

### `lastGrading`

 For `M = D.m`, the grading of `Y_M` (whose Gram matrix is `1`) as `D.InitIndex M`, a set of
`n_M - 1` indices in grade 0, plus a string of length 0. 

### `doubleLiftEvalY`

 The finite evaluation `New.Seesaw.DoubleLiftData.finEval` of the double lift
Y_{2i} → Y_{2i+1} → Y_{2i+2}: for the middle double lift if i < ϱ, the last double lift if i = ϱ,
and 0 beyond. 

### `residueMatrixCount`

 The natural number `M ^ (f n²)`, with `M = p₀ p₁`, `f` the number of infinite places of `E` and
`n = n_m` the rank `D.n D.m`. 

### `translatedPointDatumY`

 For finite adelic points `y k` of the unitary groups, the datum `New.Data.pointDatumY ϑ k` on
Hom(Y_k, Y_{k+1}) moved by `(y k, y (k + 1))` under the finite Weil representation
`New.Seesaw.liftWeilFin` with the character `D.chainChar ϑ (k + 1)` of lift `k + 1`. 

### `evaluatedDatum`

 The finite evaluation `New.Data.doubleLiftEvalY` of pair i on the data of lifts 2i+1 and 2i+2,
moved by (y_{2i}, y_{2i+1}) and (y_{2i+1}, y_{2i+2}) as in `New.Data.translatedPointDatumY`. 
