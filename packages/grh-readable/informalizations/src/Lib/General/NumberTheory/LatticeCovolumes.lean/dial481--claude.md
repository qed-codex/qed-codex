---
{
  "module": "src/Lib/General/NumberTheory/LatticeCovolumes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/LatticeCovolumes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/LatticeCovolumes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lattice indices, primitive matrices, Jacobi's identity and covolumes of fundamental domains

The first part is lattice algebra over an adelic pair `R ⊆ A` (`New.IsAdelic`; among its conditions,
`R` is open and compact in `A`), modelled on `New.Ô` inside the finite adeles. The file proves
results on indices and determinants under integral base change. For a CM field `E`, it then gives
tools for computing, coordinate by coordinate, the covolume of an arithmetic subgroup of a unipotent
group.

## Main definitions and results

* `New.genIndex_det_conj_of_isIntMatrix`: the size of a determinant does not change under an
  integral base change with integral inverse.
* `New.exists_isPrimitiveMatrix_mul_fromBlocks`, `New.exists_preimageLattice_eq_colLattice`: a left
  invertible matrix becomes primitive after multiplication by an invertible (block triangular)
  matrix.
* `New.exists_mulVec_eq_of_orthogonal`: for `J` hermitian and invertible, if the left invertible `F`
  and `n` have orthogonal columns, as many in all as `J` has rows, the orthogonal complement of `n`
  lies in the span of `F`.
* `New.genIndex_det_orthogonal_mul_submoduleIndex_sq`: Jacobi's identity between a lattice and its
  orthogonal complement; `New.Filling.jacobi_perp_discriminant` joins it with the previous result.
* `New.exists_fundamental_domain_classLattice`: the covolume of a lattice in `(E ⊗ ℝ)ⁿ` cut out by a
  finite adelic matrix and rescaled at the infinite places.
* `New.Filling.existsUnique_mul_mem_box`: suppose a group `Γ` shifts the coordinates of `G` in a
  triangular way by additive submonoids. Then the box over strict fundamental domains of these
  submonoids meets each coset `xΓ` exactly once.
* `New.Filling.exists_fundamental_domain_im_skew`: the covolume of the group
  `New.Filling.imSkewLattice` of rescaled purely imaginary integers of `E`, if `E` contains a
  primitive 5040th root of unity.

Notions from other files:
* `New.genIndex`: on units the inverse of the factor by which multiplication scales Haar measure,
  and `0` elsewhere; `New.submoduleIndex M M'`: the index of `M ∩ M'` in `M'`, as additive groups
  (`0` if infinite).
* `New.IsPrimitiveMatrix`: a matrix with entries in `R` and a left inverse with entries in `R`.
* `New.colLattice`: the `R`-module spanned by the columns of `M`; `New.preimageLattice`: the
  `R`-module of vectors `v` over `A` such that `M v` has entries in `R`.
* `New.Variety.classLattice g S Q`: the image, under the CM embedding followed by the linear map
  `Q`, of the group of `y` in `Eⁿ` such that the class of `g⁻¹ y` in `(𝔸_f/Ô)ⁿ` lies in `S`.

## Relation to the literature

Known; see `Lib.Adelic.Adeles.Basic` and `New.Spanning.RemainingTerms.SiegelLemma` for sources.


 ## Indices, primitive matrices and Jacobi's identity 

 ### Indices under a linear map and divisibility 

### `Filling.submoduleIndex_dvd_of_le`

 If `P` maps `D` into `K` and `K'` lies in `P M + K`, then the index of `K` in `K'` divides the
index of `D` in `M` (indices in the sense of `New.submoduleIndex`). 

 ### Orthogonal complements over a commutative ring 

### `fromRows_mul_fromCols_eq_one`

 If `P * Q = 1`, `P * n = 0` and `l * n = 1`, then the matrix with row blocks `P` and
`l - l * Q * P` is a left inverse of the matrix with column blocks `Q` and `n`. 

### `exists_mulVec_eq_of_orthogonal`

 Let `J` be hermitian and invertible, and let `F` and `n` be left invertible, with the columns of
`F` orthogonal to those of `n` for `J` and as many columns in all as `J` has rows. Then a vector
orthogonal to the columns of `n` is a combination of the columns of `F`. 

 ### Determinants, saturation and orthogonal complements 

### `genIndex_det_conj`

 Replacing the form `H` by `Jᴴ * H * J` multiplies the generalised index of its determinant by
the square of that of `det J` (`genIndex` is the inverse Haar modulus on units, `0` elsewhere). 

### `genIndex_det_conj_of_isIntMatrix`

 If `n` and `l` are integral and inverse to each other, the Gram matrix `nᴴ * H * n` of `H` in
the basis `n` has a determinant of the same generalised index as `det H`. 

### `exists_isPrimitiveMatrix_mul_fromBlocks`

 A left invertible matrix whose columns fall into two blocks becomes primitive after
multiplication by a block upper triangular matrix with invertible diagonal blocks. 

### `exists_preimageLattice_eq_colLattice`

 For an adelic pair `R ⊆ A` and a left invertible matrix `m` over `A`, there is an invertible
`a` whose columns span `{y | m y integral}` over `R`, with `m * a` primitive over `R`. 

### `hasLeftInv_of_genIndex_det_ne_zero`

 If the Gram matrix of the columns `(F | p)` for the form `J`, with `c` added on the diagonal of
the `p` block, has a determinant of nonzero generalised index (that is, a unit determinant), then
`F` has a left inverse over `A`. 

### `submoduleIndex_intVectors_mul_genIndex_det`

 If `F` is integral and the columns of the invertible `a` span `{y | F y integral}`, the index of
`R^σ` in this lattice is the inverse of the generalised index of `det a`. 

### `one_add_fromRows_mul_fromCols_eq`

 Let `P = (F * a)ᴴ * u` with `u` hermitian and `P * Q = 1`, and let `N` be the Gram matrix of the
columns `(F | p)` for `u` with `c` added on the diagonal of the `p` block. Then the displayed
matrix, one plus a product of a block column and a block row, is `N` between two block triangular
matrices. 

### `genIndex_det_orthogonal_mul_submoduleIndex_sq`

 Jacobi's identity between the discriminants of a lattice and of its orthogonal complement. Let
`J` be unimodular hermitian, `F` integral and left invertible over `A`, and `n` primitive, with the
columns of `F` orthogonal to those of `n` and as many columns in all as `J` has rows. Take the Gram
matrix of the columns `(F | p)` and add the unit `c` on the diagonal of the `p` block. The
generalised index of its determinant is the product of the generalised index of the determinant on
`n` of the form `J + c⁻¹ J p pᴴ J`, of the square of the index of `R^σ` in `{y | F y integral}`,
and of `genIndex c ^ card ρ`. 

### `Filling.jacobi_perp_discriminant`

 Jacobi's identity, over `R ⊂ A` modelled on `Ô ⊂ 𝔸_f` (`IsAdelic R`). Let `J` be unimodular
hermitian, `F` integral and `n` primitive, with `Fᴴ J n = 0` and `card π = card σ + card τ`; let `N`
be `(F | p)ᴴ J (F | p)` plus the unit `c` on the diagonal of the `p` block, and let `F` be left
invertible or `genIndex N.det ≠ 0`, where `genIndex a` is the inverse of the Haar-measure scaling
factor of multiplication by `a` (`0` for a non-unit). Then (a) every `u` with `nᴴ J u = 0` equals
`F v` for some `v` over `A`, and (b) `genIndex N.det` is the product of
`genIndex det (nᴴ (J + c⁻¹ J p pᴴ J) n)`, the square of the index of `R^σ` in `{y | F y integral}`,
and `genIndex c ^ card ρ`. 

 ## The quotient of a unimodular lattice by an isotropic sublattice 

### `orthogonal_symm`

 Orthogonality for a hermitian form `J` is symmetric. 

### `IsQuotientBasis`

 Let `Λ = R ^ π` carry the form `J`, and let the columns of `ι` be a basis of `Λ ∩ I` for an
isotropic space `I`. The columns of `B` represent a basis of the lattice `(Λ ∩ I^⊥)/(Λ ∩ I)`, and
`q` gives the coordinates of the class of a vector of `I^⊥` in this basis. 

### `IsQuotientBasis.isIntMatrix_basis`

 The representatives lie in `Λ`. 

### `IsQuotientBasis.isIntMatrix_coord`

 A vector of `Λ` has integral coordinates. 

### `IsQuotientBasis.coord_mul_isotropic`

 The vectors of `I` have the class zero. 

### `IsQuotientBasis.coord_mul_basis`

 The coordinates of the columns of `B` are the unit vectors. 

### `IsQuotientBasis.basis_orthogonal`

 The representatives lie in `I^⊥`. 

### `IsQuotientBasis.exists_eq_add`

 A vector of `I^⊥` differs from the representative of its class by a vector of `I`, with
  coefficients that depend integrally on the vector. 

### `mul_basis_mul_coord`

 The product of two vectors of `I^⊥` depends only on the class of the second. 

### `gram_coord`

 The form `Bᴴ J B` on the quotient is induced by `J`: on the coordinates of the classes of two
vectors of `I^⊥` it takes the value of `J` on the vectors themselves, for hermitian `J`. 

### `isUnimodular`

 Let `Λ = R^π` carry the form `J`, let the columns of `ι` be a basis of `Λ ∩ I` for an isotropic
space `I`, and let `B` represent a basis of `(Λ ∩ I^⊥)/(Λ ∩ I)` (`IsQuotientBasis`). If `R` is
stable under `star` and `J` is unimodular over `R` (hermitian and in GL(R)), then so is the Gram
matrix `Bᴴ J B`. 

### `exists_isQuotientBasis`

 Let `R` be an adelic ring and `Λ = R ^ π` unimodular for `J`. Let the columns of `ι₀` span an
isotropic space `I`, and let those of `(ι₀ | y)` be a basis of `I^⊥`: they have a left inverse, are
orthogonal to `I` and are as many as the rank of `I^⊥`. Then for some invertible `a` the columns of
`ι₀ a` lie in `Λ`, and the quotient `(Λ ∩ I^⊥)/(Λ ∩ I)` has a basis `B` with coordinates `q`. 


## Covolumes of scaled lattices and boxes of fundamental domains

Fundamental domains are strict: every point has exactly one translate in `F`.


### `existsUnique_mul_toRealVectors_add_mem`

 Let `t` be a unit of `(E ⊗ ℝ)ⁿ` and `F` a strict fundamental domain of the lattice of the
`t * y`, `y ∈ Eⁿ` whose class `frameTorsionClass m⁻¹ y`, the class of `m y` in `(𝔸_f/Ô)ⁿ`
(`AdelicTorsion E n`), is trivial. Then for all `z` and every class `w` exactly one `y ∈ Eⁿ` of
class `w` has `t * y + z ∈ F`. 

### `exists_fundamental_domain_classLattice`

 Let `t ∈ (E ⊗ ℝ)ⁿ` (here `RealVectors E n`) and the finite adelic matrix `m` be invertible. The
vectors `(t j v * Φ v (x j))`, for `x ∈ Eⁿ` with `m x` integral (`Φ` is the CM type), form the group
`classLattice m⁻¹ ⊥ _` (`⊥`: the class of `m x` in `(𝔸_f/Ô)ⁿ` is to be zero; the last argument is
multiplication by `t`). It has a measurable strict fundamental domain `F` of volume
`(∏ w, ‖∏ j, t j w‖ ^ 2) / genIndex (det m) / volÔ E ^ n`, where `genIndex` is the inverse Haar
modulus and `volÔ E = 2 ^ r₂ / √|disc E|`. 

### `Filling.existsUnique_mul_mem_box`

 Let `c` be injective coordinates on a group `G`, with values in additive groups `V i` and
graded by `deg`, and let `F i` be strict fundamental domains of submonoids `L i` of `V i`. Let `Γ`
be a subgroup that acts on the coordinates from the right in a triangular way: every point of `L i`
is coordinate `i` of some `γ ∈ Γ` whose other coordinates of degree `≤ deg i` are those of `1`
(`h_onto`); if the coordinates of `γ ∈ Γ` of degree `< deg i` are those of `1`, then `c γ i ∈ L i`
(`h_mem`) and right multiplication by `γ` adds `c γ i` on the left to coordinate `i` (`h_transl`).
Then for every `x` exactly one `γ ∈ Γ` has `c (x γ)` in the box over the `F i`. 

### `Filling.imSkewLattice`

 The group of the vectors `(t v * Im Φ_v(s))_v`, for integers `s` of the CM field `E` with
`star s = -s`; here `Φ` is the CM type. 

### `Filling.mem_imSkewLattice`

 A vector lies in `imSkewLattice t` iff it is `(t v * Im Φ_v(s))_v` for an integer `s` of `E`
with `star s = -s`. 

### `Filling.mem_imSkewLattice_iff_exists_real`

 If `ι² = -1`, `star ι = -ι` and all `Φ_v(ι)` are imaginary, the group `imSkewLattice t`
consists of the vectors `(t v * Im Φ_v(ι) * Re Φ_v(a))_v`, `a` an integer of the maximal real
subfield. 

### `Filling.exists_fundamental_domain_im_skew`

 Let the CM field `E` contain a primitive 5040th root of unity (`New.HasPrimitiveRoot5040`) and
let all `t v` be nonzero. Then the group `imSkewLattice t` of rescaled imaginary parts of the
integers `s` of `E` with `star s = -s` has a measurable strict fundamental domain, whose volume is
`∏ |t v| * √√|disc E|`. 

 ## Lattices with an integral Gram matrix 

### `volume_fundamentalDomain_pi_basis`

 The fundamental domain of the product basis `Pi.basis b` is the product of the fundamental
domains; if these have volume `1`, so has the product. 

### `volume_fundamentalDomain_basisOneI`

 The unit square in `ℂ` has area `1`. 

### `exists_isAddFundamentalDomain_of_integral`

 Let `L` be a lattice in a real vector space with a basis `e` whose fundamental domain has
measure `1`. If the euclidean product in the coordinates of `e` is integral on `L`, then `L` has a
fundamental domain of finite measure at least `1`. 
