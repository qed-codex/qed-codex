---
{
  "module": "src/New/Spanning/Frames/Lengths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Lengths.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Lengths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sizes, lengths and balanced frames

A filtration `ofSize i` of the ring `A` measures numbers, vectors and matrices on one scale L. It
gives the length of a vector at a point `g` of the unitary group, the induced length on the quotient
Y^(l) along the frame, and balanced frame vectors.

Letters used in this folder: G^(l) = `floorGroup l`, R^(l) = `partialUnitriangularGroup l`,
U_(<l) = `unipotentBelow l`; Y^(l) is the quotient of the vectors orthogonal to the e_b, b < l, by
their span; for a place datum `F` (`New.Floors.PlaceData`), K = `F.boxSet` is its compact set and
M = `F.levelUnit` its modulus; for a gauge `Γ` (`New.Floors.Gauge`), Λ = `Γ.loss` is its constant.

## Guide to this folder

The files of this folder bound the local densities of pairs of frames, at a real place and over the
ring of all finite places of a finite set. Steps 3 to 6 rest on the gains of step 13, which steps 7
to 12 prepare.

1. Gauges, lengths of vectors and balanced frames. `New.Floors.Gauge`, `New.Floors.Size.LengthLeAt`,
   `New.Floors.Size.IsBalanced`.
2. A density is an integral over a position and two frames. `New.Floors.PlaceData.floorForm`,
   `New.Floors.Gauge.integral_psi_mul_floorForm_succ`,
   `New.Floors.Gauge.inner_besselOrbitalIntegral`.
3. The positions are cut into shells by their height; a few factors of the gain pay for the sum over
   the shells. `New.Floors.Gauge.IsShell`, `New.Floors.Gauge.lintegral_le_of_shells`.
4. The finite places, taken together: the decay in the frequency and the mass on the congruence
   subgroup. `New.Floors.IntegralPlace.IsLargeLatticeData.enorm_floorForm_le`,
   `New.Floors.IntegralPlace.IsLargeLatticeData.massIntegral_le_main_add_error`.
5. The gain in the mass from the fixed vectors, and the resulting system.
   `New.Filling.IsFillingData.exists_intermediateGroup_places`,
   `New.Filling.IsFillingData.exists_intermediateGroup_sieveSystem`.
6. The mass at a real place, against the uncut Bessel function.
   `New.Floors.IsCutBessel.norm_floorForm_zero_le`.
7. Plancherel's formula on a quadric, for the pivots and for the vectors after them.
   `New.Floors.Gauge.fourierSqNormLe_floorQuadricMeasure`, `New.Floors.Gauge.lintegral_section_le`,
   `New.Floors.Gauge.parseval_heisenbergMeasure_le`.
8. Depth, and a subspace of large rank that looks the same from both points.
   `New.Floors.PlaceData.depth`, `New.Floors.PlaceData.depthWeight`,
   `New.Floors.PlaceData.commonVectors`.
9. Deep vectors are rare, and long coordinates force depth.
   `New.Floors.Gauge.floorMassLe_depth_pow`,
   `New.Floors.Gauge.lintegral_heisenbergMeasure_inv_depth_le`.
10. A position of large height has a deep vector after the head.
    `New.Floors.Gauge.hasMatrixSize_sub_one_of_stableProducts`,
    `New.Floors.Gauge.exists_unit_mem_stableProducts_of_isHead`.
11. One frame, along the Heisenberg groups. `New.Floors.Gauge.lintegral_weightedSquareIntegral_le`.
12. A weight made of depths separates the two frames.
    `New.Floors.Gauge.sq_lintegral_le_mul_lintegral`,
    `New.Floors.Gauge.sq_lintegral_mul_comp_weylElem_inv_le_of_section`.
13. The gains at one position: a frequency, two heads, a deep vector.
    `New.Floors.Gauge.formIntegrandL1Norm_sq_le_of_char`,
    `New.Floors.Gauge.formIntegrandL1Norm_sq_le_of_heads`,
    `New.Floors.Gauge.formMajorant_sq_le_of_hasDeepVector`.

The equation of a quadric is solved in a block of orthonormal coordinates, in the same way at both
kinds of place (`New.Floors.Place.IsSolvedIn`, `New.Floors.Gauge.exists_blockKernel`). Both pivots
are first moved into one space; their equations are solved in two disjoint blocks, and Plancherel's
formula acts on the orthonormal coordinates off both blocks.

## Main definitions and results

* `New.Floors.Size`, `New.Floors.Size.vecsOfSize`, `New.Floors.Size.HasMatrixSize`: sizes of
  numbers, vectors and matrices.
* `New.Floors.weylRatio`, `New.Floors.coe_weylRatio`: the quotient of two Weyl elements is diagonal.
* `New.Floors.IsOrthogonalBelow`, `New.Floors.CongrBelow`: the vectors of Y^(l) and their lifts.
* `New.Floors.Size.LengthLeAt`, `New.Floors.Size.InducedLengthLe`, `New.Floors.Size.IsBalanced`:
  lengths at a point, induced lengths, balanced vectors.
* `New.Floors.Size.GaugesDifferLe`, `New.Floors.Size.HasShortDual`, `New.Floors.Size.IsHead`: the
  notions compared in `New.Spanning.Frames.TwoGauges`.

Notions from other files:
* `New.Shape.BesselIndex`: the index set of the basis e_a, x_i, z, e*_a (a < ϱ) of V; the x_i and z
  form the middle block.
* `New.Shape.Form.splitGram`: the Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix `T`; `New.Floors.IsHermitianUnit` says that it is hermitian and invertible, and `T.G` is
  its unitary group.
* `New.BesselIndex.level`, `New.Floors.FloorGroups.floorOf`: e_a has level `a`, the middle block
  level `ϱ`, e*_a level `2ϱ - a`; both e_a and e*_a have floor `a`, z has floor `ϱ` and the x_i have
  floor `ϱ + 1`.
* `New.Shape.Form.partialUnitriangularGroup`: the group R^(l), for l ≤ ϱ + 1 unitriangular on the
  first l vectors of the frame (e_0, …, e_(ϱ-1), e_ϱ = z).
* `New.Shape.Form.unipotentBelow`: the group U_(<l) of the isometries that are unitriangular when
  the basis vectors of floor at least l are all given the middle level `ϱ`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.



## Sizes, lifts and lengths

The basis is indexed by `𝔰.BesselIndex`: `inl a` is e_a and `eStar a = inr (inr a)` is e*_a
(`a < ϱ`), in hyperbolic pairs.


### `Size`

 Sizes for a fixed scale. There are two cases in view. At a real place, a number x has size i if
|x| ≤ L^i, for a fixed number L. At the finite places, x has size i if α^i x is integral, for a
fixed integral unit α. The fields are the rules that the proofs use. 

### `Size.ofSize`

 The set A_(i) of numbers of size i. 

### `Size.mul_mem_ofSize`

 Sizes add under multiplication: A_(i) A_(j) ⊆ A_(i+j). 

### `Size.sum_mem_ofSize`

 A sum of at most r + 1 terms of size i has size i + 1, where r is the rank of the space. 

### `Size.neg_mem_iff_and_star_mem_iff`

 Each of -x and star x has size i exactly when x has. 

### `Size.zero_one_mem_ofSize`

 The elements 0 and 1 have every size. 

### `Size.splitGram_and_inv_mem`

 The entries of the Gram matrix `T.splitGram` and of its inverse have size 1. 

### `weylRatio`

 The quotient w_q⁻¹ w_p of two Weyl elements of the first j hyperbolic pairs. Here
w_p = `weylElem j p` sends e_a to p_a e*_a and e*_a to (star p_a)⁻¹ e_a for a < j. 

### `coe_weylRatio`

 The matrix of `weylRatio j p q` = w_q⁻¹ w_p is diagonal. For a < min j ϱ, its entry at e_a is
p_a / q_a and its entry at e*_a is `star` of q_a / p_a. Every other diagonal entry is 1. (Both e_a
and e*_a have floor a, and only e_a has level below ϱ.) 

### `weylRatio_inv`

 The inverse of w_q⁻¹ w_p is w_p⁻¹ w_q. 

### `card_subtype_succ_le_floorOf_eq`

 For a < ϱ, the number of basis indices of floor at least a + 1 is k + 1 + 2(ϱ − (a + 1)), the
rank of the orthogonal complement of the first a + 1 hyperbolic planes. Here k + 1 is the rank of
the middle block. 

 ### Quotients along the frame

For `l ≤ ϱ` the space Y^(l) is the quotient of the vectors orthogonal to e_0, …, e_(l-1) by the span
of these vectors, so e_a lies in Y^(a). Its elements are handled through their lifts. 

### `IsOrthogonalBelow`

 The vector ω is orthogonal to the e_b, b < l. The product ⟨e_b, ω⟩ is the coordinate of ω at
e*_b. 

### `CongrBelow`

 The vectors ω and ω' differ by an element of the span of the e_b, b < l, for l ≤ ϱ: they are two
lifts of one class. The indices of level at least l are those other than the e_b, b < l. 

### `le_level_eStar`

 The index e*_b has level 2ϱ - b, which is at least ϱ. 

### `exists_eq_inl_of_level_lt`

 For l ≤ ϱ, a basis index of level below l is the index of some e_b, b < l. 

### `CongrBelow.refl`

 Congruence modulo the e_b, b < l, is reflexive. 

### `CongrBelow.symm`

 Congruence modulo the e_b, b < l, is symmetric. 

### `CongrBelow.trans`

 Congruence modulo the e_b, b < l, is transitive. 

### `CongrBelow.apply_eStar`

 For l ≤ ϱ, two vectors that are congruent modulo the e_b, b < l, have the same coordinate at
every e*_b. 

### `IsOrthogonalBelow.of_congrBelow`

 For l ≤ ϱ, a vector congruent modulo the e_b, b < l, to a vector orthogonal to these e_b is
orthogonal to them as well. 

### `IsOrthogonalBelow.smul`

 A multiple of a vector orthogonal to the e_b, b < l, is orthogonal to them. 

### `CongrBelow.smul`

 Congruence modulo the e_b, b < l, is kept under multiplication by a scalar. 

### `IsOrthogonalBelow.mulVec`

 Let l ≤ j. An element of R^(j) = `partialUnitriangularGroup j`, which changes each e_b, b < j,
by a combination of the earlier ones, keeps vectors orthogonal to the e_b, b < l, orthogonal to
them. 

### `CongrBelow.mulVec`

 Let l ≤ j and l ≤ ϱ = `𝔰.ϱ`, the number of hyperbolic planes. An element `s` of
R^(j) = `partialUnitriangularGroup j` changes each e_b, b < j, by a combination of the earlier ones.
It respects congruence modulo the e_b, b < l: if ω and ω' are congruent, so are `s *ᵥ ω` and
`s *ᵥ ω'`. 

### `IsOrthogonalBelow.congrBelow_mulVec`

 The unipotent group U_(<l) = `unipotentBelow l` keeps the coordinates of level at least l of a
vector orthogonal to the e_b, b < l. For l ≤ ϱ this says that it acts as 1 on Y^(l). 

### `CongrBelow.form_eq_left`

 Let l ≤ ϱ, and let o be orthogonal to the e_b, b < l. The product ⟨ω, o⟩ for the Gram matrix
`T.splitGram` depends only on the class of its left argument ω modulo these e_b. 

### `CongrBelow.form_eq_right`

 Let l ≤ ϱ = `𝔰.ϱ`, the number of hyperbolic planes, and let o be orthogonal to the e_b, b < l.
The product ⟨o, ω⟩ for the Gram matrix `T.splitGram` depends only on the class of its right argument
ω modulo these e_b. So it is unchanged when ω is replaced by a vector ω' congruent to it. 

### `CongrBelow.sub_smul`

 From congruence modulo e_0, …, e_a to congruence modulo e_0, …, e_(a-1), where `inl b` is the
index of e_b. Let ω' be congruent to ω modulo the e_b, b ≤ a, and let f be congruent to e_a modulo
the e_b, b < a. Then ω' - c f is congruent to ω modulo the e_b, b < a, where c is the coordinate of
ω' - ω at e_a. 

### `CongrBelow.form_sub_form`

 Write ⟨v, w⟩ for the form with Gram matrix `T.splitGram`, so that ⟨e_a, ζ⟩ is the coordinate of
ζ at e*_a (index `eStar a`). Let ζ be a dual of e_a, that is, orthogonal to the e_b, b < a, with
⟨e_a, ζ⟩ = 1, and let ζ' be congruent to ζ modulo these e_b. Let ω be orthogonal to the e_b, b ≤ a,
and let ω' be congruent to ω modulo these vectors. Then ⟨ζ', ω'⟩ - ⟨ζ, ω⟩ is the coordinate of ω' -
ω at e_a. 

### `vecsOfSize`

 The vectors of size i for the sizes `S`: all entries have size i. 

### `HasMatrixSize`

 A matrix has size i for the sizes `S` if all its entries have size i. 

### `LengthLeAt`

 The vector y has length at most L^i at the point g: the vector g⁻¹ y has size i. Here and below
L is the scale of the sizes `S`. 

### `InducedLengthLe`

 Some vector congruent to y modulo the e_b, b < l, has length at most L^i at g. For l ≤ ϱ and y
orthogonal to these e_b, this bounds the induced length of the class of y in Y^(l). 

### `IsBalanced`

 The vector e_a is balanced in Y^(a) at g, with bound L^i: its class has induced length at most
L^i, and it has a dual of length at most L^i, a vector ζ orthogonal to the e_b, b < a, with
⟨e_a, ζ⟩ = 1. The short dual stands for a lower bound on the length at a real place and for
primitivity at the finite places. 

### `IsBalanced.inducedLengthLe`

 The class of e_a in Y^(a) has induced length at most L^i. 

### `IsBalanced.exists_dual`

 Some ζ orthogonal to the e_b, b < a, with ⟨e_a, ζ⟩ = 1 has length at most L^i. 

### `AgreesModulo`

 The vector ω read at g agrees modulo r with a vector ω' read at g', where ω' is congruent to ω
modulo the e_b, b < l: the vector (g⁻¹ ω - g'⁻¹ ω') / r has size i. 

### `GaugesDifferLe`

 The lengths at g and g' on Y^(l) differ by at most L^t, modulo r: a vector orthogonal to the
e_b, b < l, of length at most L^i at g agrees modulo r, up to size i + t, with a lift of its class
read at g'. For r = 1 the class then has length at most L^(i+t+1) at g'. The comparison goes from g
to g' only, and for general r it asks for a congruence, not only for a bound on lengths. 

### `HasShortDual`

 The vector e_a has a short dual ζ for the points g and g': ζ is orthogonal to the e_b, b < a,
⟨e_a, ζ⟩ = 1, the length of ζ at g is at most L^i, and ζ read at g agrees modulo r, up to size i,
with a lift of its class in Y^(a) read at g'. 

### `IsHead`

 The head p of length j, a sequence of units p₀, …, p_(j-1), is adapted to the scale: the
inverses of the products p₀ ⋯ p_(l-1), l ≤ j, have size 1. 

### `IsHead.star_head`

 If the head `p` of length `j` is adapted to the sizes `S` (the inverses of the products p₀ ⋯
p_(l-1), l ≤ j, have size 1), so is the head `star p` of its conjugates. 

### `mem_ofSize_mono`

 A number of size i has every larger size. 

### `neg_mem_ofSize`

 The negative of a number of size i has size i. 

### `star_mem_ofSize`

 The conjugate of a number of size i has size i. 

### `neg_one_pow_mul_mem_ofSize`

 A sign does not change the size. 

### `sum_fin_mem_ofSize`

 A sum of at most ϱ + 1 terms of size i has size i + 1. 

### `sub_mem_ofSize`

 The difference of two numbers of size i has size i + 1. 

### `HasMatrixSize.mono`

 A matrix of size i has every larger size. 

### `HasMatrixSize.one`

 The identity matrix has every size. 

### `HasMatrixSize.sub`

 The difference of two matrices of size i has size i + 1. 

### `hasMatrixSize_splitGram`

 The Gram matrix `T.splitGram` has size 1. 

### `dotProduct_mem_ofSize`

 If v has size j and the entries of w on the support of v have size i, then the dot product of
w and v has size i + j + 1. 

### `HasMatrixSize.mulVec`

 A matrix of size i maps vectors of size j to vectors of size i + j + 1. 

### `HasMatrixSize.mul`

 The product of matrices of sizes i and j has size i + j + 1. 

### `mem_vecsOfSize_mono`

 A vector of size i has every larger size. 

### `smul_mem_vecsOfSize`

 A number of size i times a vector of size j is a vector of size i + j. 

### `sub_mem_vecsOfSize`

 The difference of two vectors of size i has size i + 1. 

### `single_mem_vecsOfSize`

 The basis vectors have every size. 

### `lengthLeAt_one_iff`

 At the point 1, having length at most L^i means having size i. 

### `lengthLeAt_mulVec_iff`

 The vector g v has length at most L^i at g if and only if v has size i. 

### `form_mem_ofSize`

 If v has size i and w has size j, then the product ⟨v, w⟩ for the form `T.splitGram` has size
i + j + 3. 

### `form_sub_form_mem_ofSize`

 The form respects closeness modulo r. Write ⟨v, w⟩ for the form with Gram matrix `T.splitGram`.
Let r be a self-adjoint unit of size 1. If v and (v - v') / r have size i, and w and (w - w') / r
have size j, then (⟨v', w'⟩ - ⟨v, w⟩) / r has size i + j + 6. 

### `det_mem_ofSize`

 For the sizes `S` (a matrix has size i if all its entries do): if `Z` is a square matrix of
order `j ≤ 𝔰.ϱ`, with ϱ the number of hyperbolic planes, and `Z` has size 7, then `Z.det` has size
`8 * j`. 

### `det_mem_ofSize_of_last_row`

 For the sizes `S`: let `Z` be a square matrix of order `j + 1`, where `j ≤ 𝔰.ϱ` and ϱ is the
number of hyperbolic planes. If the last row `Z (last j)` has size 9 and the other rows have size 7,
then `Z.det` has size `9 * (j + 1)`. 

### `adjoint_apply_mem_ofSize`

 Let the Gram matrix J = `T.splitGram` be hermitian and invertible (`IsHermitianUnit`), and let X
be the adjoint of Y for J, that is, J X = Yᴴ J. Sizes are those of `S`, and a vector has size i if
all its entries do. If the rows n of Y with J n b ≠ 0 have size i, then the entries of the column b
of X have size i + 4. 

### `HasMatrixSize.inv`

 If the matrix of x, an element of the unitary group of J = `T.splitGram`, has size i, then the
matrix of x⁻¹ has size i + 4, since J x⁻¹ = xᴴ J. 
