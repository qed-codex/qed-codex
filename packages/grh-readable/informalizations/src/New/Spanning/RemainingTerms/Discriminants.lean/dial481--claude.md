---
{
  "module": "src/New/Spanning/RemainingTerms/Discriminants.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Discriminants.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Discriminants.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Discriminants of lattices and sums over sublattices

Lattices of rational subspaces of a space with the standard hermitian form, written over `Ô`;
their discriminants; and a bound for the sum of a negative power of the index over all sublattices
of finite index.

The bound for the sum over sublattices is a consequence of Hey's formula for the zeta function of a
lattice. Here it is proved directly, by induction on the rank, over any
commutative ring whose ideals of finite index are principal.

The formula that compares the discriminant of `L ∩ W` with that of the dual lattice in `W^⊥` is
`New.Filling.jacobi_perp_discriminant`, stated for Gram determinants.


### `submoduleZeta`

 The sum of `[N : M] ^ (-s)` over the submodules `M` of finite index in `N`. 

### `cardQuot_comap`

 The index of the preimage of `M` under `f` is the index of `M ⊓ range f` in the range of `f`. 

### `cardQuot_comap_of_surjective`

 Pulling back along a surjective linear map keeps the index. 

### `tsum_relIndex_range_le_submoduleZeta`

 The sum of `[range f : M] ^ (-s)` over the submodules `M` of finite index in the range of a
linear map `f` is at most the same sum over the submodules of finite index in its domain. 

### `submoduleZeta_le_of_surjective`

 If `N` maps onto `N'`, then the sum of `[N' : M] ^ (-s)` over the submodules `M` of finite
index in `N'` is at most the same sum for `N`. 

### `cardQuot_eq_cardQuot_map_fst_mul_comap_inr`

 The index of a submodule of a product is the index of its projection to the first factor times
the index of its intersection with the second factor. 

### `eq_span_sup_of_map_fst_eq_span`

 Let `M` be a submodule of `R × N` whose first coordinates are the multiples of `g`, and let
`(g, n) ∈ M`. Then `M` is spanned by `(g, n)` and its intersection with `N`. 

### `tsum_quotient_cardQuot_inv_pow`

 For a submodule `M` of finite index in `N`, the sum of `[N : M] ^ (-(s + 1))` over the classes
modulo `M` is `[N : M] ^ (-s)`. 

### `submoduleZeta_prod_le`

 Write `ζ_X(s) = submoduleZeta R X s` for the sum of `[X : M] ^ (-s)` over the submodules `M` of
finite index in an `R`-module `X`. If the ideals of finite index of `R` are principal, then
`ζ_{R × N}(s + 1) ≤ ζ_R(s + 1) * ζ_N(s)`. 

### `submoduleZeta_pi_le`

 If the ideals of finite index of `R` are principal, then the sum of `[R ^ r : M] ^ (-(r + μ))`
over the submodules `M` of finite index is at most the `r`th power of the sum of `[R : I] ^ (-μ)`
over the ideals `I` of finite index. 

### `colLattice_mul`

 The lattice of the columns of `B * C` is the image under `B` of that of the columns of `C`. 

### `exists_isIntMatrix_mul_eq`

 If the lattice of the columns of `C` lies in that of the columns of `B`, then `C = B U` for
some matrix `U` with entries in `R`. 

### `colLattice_mul_le`

 If `U` has entries in `R`, then the lattice of the columns of `B * U` lies in that of the
columns of `B`. 

### `exists_range_eq_colLattice`

 Let `R` be a subring of a commutative ring `A`. The `R`-span `colLattice R B` of the columns of
an `m × n` matrix `B` over `A` is the range of an `R`-linear map from `R ^ n` to `A ^ m`. 

### `_root_.New.IsValuationPair.exists_square_colLattice_eq`

 Let `R` be a subring of a commutative ring `A` and suppose that any `a`, `b` in `A` are
`R`-multiples of `(1 - e) a + e b` for some idempotent `e` of `R` (`IsValuationPair R`). Then the
`R`-span `colLattice R Y` of the columns of an `m × n` matrix `Y` over `A` is the span of the
columns of a square `m × m` matrix `D`. 

### `_root_.New.IsValuationPair.isBezout`

 If `R` is a valuation pair, that is, any `a`, `b` in `A` are `R`-multiples of `(1 - e) a + e b`
for some idempotent `e` of `R`, then every finitely generated ideal of `R` is principal. 

### `IsLatticeOfRank`

 Let `𝔸f E` be the finite adeles of the number field `E` and `Ô E` the integral ones. An
`Ô E`-submodule `L` of `(𝔸f E) ^ κ` is a lattice of rank `r` if it is spanned over `Ô E` by the
columns of `x a`, where the `r` columns of `x` are independent vectors in `E ^ κ` and `a` is an
invertible `r × r` matrix over `𝔸f E`. 

### `discriminant`

 The discriminant of a lattice `L` of rank `r`: the square root of `genIndex (det (Bᴴ * B))` for
some chosen basis `B = x a`. Here `ᴴ` is the conjugate transpose and `genIndex u` is the inverse of
the factor by which a unit `u` scales Haar measure on the finite adeles (`0` for a non-unit). The
value is `0` if `L` is not a lattice of rank `r`. 

### `hasLeftInv_finAdeleMatrix_mul`

 If `x` has a left inverse over `E` and `a` is an invertible matrix over the finite adeles
`𝔸f E`, then `finAdeleMatrix x * a` (with `x` read over `𝔸f E`) has a left inverse over `𝔸f E`. 

### `genIndex_det_gram_eq_of_colLattice_eq`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let `B`, `C` be matrices over `𝔸f E` whose columns have the same `Ô E`-span, and
let `B` have a left inverse. Then the Gram determinants `det (Bᴴ * B)` and `det (Cᴴ * C)`, with `ᴴ`
the conjugate transpose, have the same generalised index: `genIndex a` is the inverse of the factor
by which a unit `a` scales Haar measure, and `0` for a non-unit. 

### `discriminant_colLattice`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let `x` be a matrix over `E` with a left inverse, `a` an invertible matrix over
`𝔸f E`, and `B = finAdeleMatrix x * a`, with `x` read over `𝔸f E`. The discriminant of the
`Ô E`-span of the columns of `B`, defined from a chosen basis of this form, can be computed from
`B`: it is `√(genIndex (Bᴴ * B).det)`. 

### `det_gram_ne_zero`

 Let `E` be a CM field, with `ᴴ` the conjugate transpose for its complex conjugation. If the
columns of `x` are independent over `E` (`x` has a left inverse), then their Gram determinant
`det (xᴴ * x)` for the standard hermitian form is not zero. 

### `IsLatticeOfRank.discriminant_pos`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let `L` be a lattice of rank `r` in `(𝔸f E) ^ κ`: the `Ô E`-span of the columns
of `x a`, where `x` has `r` independent columns over `E` and `a` is invertible over `𝔸f E`. Then
the discriminant of `L`, the square root of the generalised index `genIndex` of the Gram
determinant of such a basis, is positive. 

### `exists_colLattice_fromCols_eq`

 Let `E` be a number field, `𝔸f E` its finite adeles and `Ô E` the integral ones. If an
`Ô E`-submodule `M` of `(𝔸f E) ^ n` contains the `Ô E`-span `colLattice (Ô E) C` of the columns of
`C` with finite index (`submoduleIndex` is not `0`), then `M` is spanned by the columns of `C` and
finitely many further vectors, the columns of `reps`. 

### `exists_colLattice_eq_of_submoduleIndex_ne_zero`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. If an `Ô E`-submodule `M` of the module `intVectors (Ô E) n` of vectors in
`(𝔸f E) ^ n` with entries in `Ô E` has finite index, then it has a basis: it is the `Ô E`-span
`colLattice` of the columns of a matrix that is invertible over `𝔸f E`. 

### `sqrt_genIndex_det_gram_mul`

 For an adelic matrix `B` and an invertible adelic matrix `A`, passing from `B` to `B * A`
multiplies the square root of the generalised index `genIndex` of the Gram determinant by the
generalised index of `det A`. 

### `exists_colLattice_mul_eq_of_le`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let `B` be a matrix over `𝔸f E` with a left inverse, and `M` a submodule of
finite index in the `Ô E`-span `colLattice` of the columns of `B`. Then `M` is spanned by the
columns of `B * A` for some `A` invertible over `𝔸f E`, and the index of `M` is `genIndex (det A)`,
the inverse of the factor by which `det A` scales Haar measure. 

### `IsLatticeOfRank.of_submoduleIndex_ne_zero`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. A lattice of rank `r` is the `Ô E`-span in `(𝔸f E) ^ κ` of the columns of `x a`,
with `r` independent columns of `x` over `E` and `a` invertible over `𝔸f E`. An `Ô E`-submodule `M`
of finite index (`submoduleIndex M L` is not `0`) in such a lattice `L` is again one. 

### `IsLatticeOfRank.discriminant_eq_mul_submoduleIndex`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let `L` be a lattice of rank `r` in `(𝔸f E) ^ κ`: the `Ô E`-span of the columns
of `B = x a`, with `r` independent columns of `x` over `E` and `a` invertible over `𝔸f E`. If `M` is
an `Ô E`-submodule of `L` of finite non-zero index `submoduleIndex M L`, then its discriminant is
that of `L` times this index. 

### `IsLatticeOfRank.of_le_and_discriminant_eq_mul_index`

 An `Ô E`-submodule `M` of finite index in a lattice `L` of rank `r` is a lattice of the same
rank, and its discriminant is the discriminant of `L` times the index `submoduleIndex M L` of `M` in
`L`. 

### `colLattice_le_preimageLattice_iff`

 The `Ô`-span `colLattice` of the columns of `B` lies in `preimageLattice (Ô E) H`, the vectors
that `H` maps to integral ones, if and only if `H * B` has all entries in `Ô`. 

### `map_colLattice_finAdeleMatrix_mul`

 The image under a rational matrix `η` of the lattice spanned by the columns of `x a` is the
lattice spanned by the columns of `(η x) a`. 

### `IsLatticeOfRank.map_of_hasLeftInv`

 A matrix `η` over `E` with a left inverse maps a lattice of rank `r` in `(𝔸f E) ^ κ` (the
`Ô E`-span of the adelic basis `x a` of an `r`-dimensional subspace of `E ^ κ`) to a lattice of
rank `r`. 

### `IsLatticeOfRank.discriminant_map_of_unitary`

 An isometry `η` of the standard hermitian form over `E` (`ηᴴ * η = 1`) keeps the discriminant
of a lattice of rank `r`, that is, the square root of the generalised index of the Gram determinant
of a basis of the lattice. 

### `IsLatticeOfRank.map_of_unitary`

 An isometry `η` of the standard hermitian form over `E` (`ηᴴ * η = 1`) maps a lattice of rank
`r` to a lattice of rank `r` with the same discriminant. 

### `saturatedLattice`

 The saturated lattice of a subspace `V` of `E ^ κ` for a matrix `H` with left inverse `H'`: the
`Ô`-span of the chosen basis `sublatticeBasis u V`, where `u` is the identity `H' * H = 1`. Its
columns are adelic points of `V`, and their image under `H` is a primitive integral matrix. 

### `saturatedLattice_le`

 The matrix `H`, which has the left inverse `H'`, maps the saturated lattice of `V` to integral
vectors. 

### `isLatticeOfRank_saturatedLattice`

 The saturated lattice of `V` is a lattice whose rank is the dimension of `V`. 

### `discriminant_saturatedLattice`

 The discriminant of the saturated lattice of `V` is `sublatticeDiscriminant h_left_inv V`, the
square root of the generalised index of the Gram determinant of its chosen basis. 

### `one_le_sublatticeDiscriminant`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones. Let the matrix `H` over `𝔸f E` have the left inverse `H'`, and let `V` be a
subspace of `E ^ κ`. Suppose that, for every adelic matrix `m` with `finrank E V` columns, the Gram
matrix `mᴴ * m` has entries in `Ô E` whenever `H * m` has. Then the discriminant
`sublatticeDiscriminant h_left_inv V` is at least `1`. 

### `IsLatticeOfRank.exists_eq_colLattice_sublatticeBasis_mul`

 Let `E` be a CM field with a primitive 5040th root of unity, `𝔸f E` its finite adeles and `Ô E`
the integral ones, and let the matrix `H` over `𝔸f E` have the left inverse `H'`. Let `L` be a
lattice of rank `r` that `H` maps to integral vectors: the `Ô E`-span in `(𝔸f E) ^ κ` of the columns
of `x a`, with `r` independent columns of `x` over `E` and `a` invertible over `𝔸f E`. Then `L` is
spanned by the columns of `S * A` for some subspace `W` of `E ^ κ` of dimension `r` and some
integral `A` invertible over `𝔸f E`. Here `S = sublatticeBasis h_left_inv W` is the chosen basis of
the saturated lattice of `W`. The discriminant of a lattice is the square root of `genIndex` of the
Gram determinant of a basis, with `genIndex u` the inverse of the factor by which a unit `u` scales
Haar measure; that of `L` is `sublatticeDiscriminant h_left_inv W`, the one of `S`, times
`genIndex (det A)`. 

### `isPrincipal_of_cardQuot_ne_zero`

 Let `E` be a CM field with a primitive 5040th root of unity. Every ideal of finite index in the
ring `Ô E` of integral finite adeles is principal. 

### `tsum_submoduleIndex_colLattice_inv_pow_le`

 For an adelic matrix `B` with `r` columns, the sum of `[L : M] ^ (-(r + μ))` over the submodules
`M` of finite index in the span `L = colLattice (Ô E) B` of its columns is at most `ζ(μ) ^ r`, where
`ζ(μ) = idealZeta (Ô E) μ` is the sum of `[Ô : I] ^ (-μ)` over the ideals `I` of finite index. 

### `IsLatticeOfRank.tsum_submoduleIndex_inv_pow_le`

 For a lattice `L` of rank `r`, the sum of `[L : M] ^ (-(r + μ))` over the sublattices `M` of
finite index is at most `ζ(μ) ^ r`, where `ζ(μ) = idealZeta (Ô E) μ` is the sum of
`[Ô : I] ^ (-μ)` over the ideals `I` of finite index in `Ô`. (Hey's formula would give the sum
exactly, as a product of zeta values; only this bound is used, and it is proved without the
formula.) 
