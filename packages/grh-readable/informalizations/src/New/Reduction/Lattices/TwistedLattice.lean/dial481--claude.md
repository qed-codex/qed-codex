---
{
  "module": "src/New/Reduction/Lattices/TwistedLattice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Twisted lattices

A twisted lattice on a complex vector space `V` is a family of linear maps `Θ_ξ` from `V` to inner
product spaces, one for each twist `ξ`, with a module of integral vectors at every `ι ∣ l` in each
of these spaces, and coordinates on the space for the trivial twist in which the inner product
has a rational matrix. A twist is a member of an index type `T`, the trivial twist is `1`, and for
each prime `l` some twists are called allowed at `l` (`IsAllowed`). A vector of `V` is integral at
`ι ∣ l` if its images for all twists allowed at `l` are (`integralVectors`), while the covolume
refers to the trivial twist alone. An inner product on `V` and its finite dimension are assumed only
from the definition of the number `Z(ξ)` on.

* `New.TwistedLattice.IndexLe`, `New.TwistedLattice.CovolumeLe`, `New.TwistedLattice.volume`: index
  and covolume of a family in `V`, and the number `Z(ξ) = det (Θ_ξ* Θ_ξ)`.
* `New.TwistedLattice.CovolumeLe.norm_map_det_gram_le`, `New.TwistedLattice.CovolumeLe.sumElim`,
  `New.TwistedLattice.norm_det_mul_det_gram_le_one`: conjugates of Gram determinants, adjoining
  vectors, and valuations of Gram determinants.
* `New.TwistedLattice.covolume_add_index_nonneg`: given an allowed twist `ξ_ι` for each `ι`, a
  lower bound for the covolume of a family in terms of its index, the height of `Z(1) / Z(ξ_ι)`,
  and the sizes and denominators of vectors that complete the family to a basis.

Notions from other files:
* `New.PrimePadicIso`: pairs `ι` of a prime `l = ι.prime` and an isomorphism `ι.iso : ℂ ≃ ℚ̄_l`,
  written `ι ∣ l`. A number `x` is integral at `ι` if `‖ι.iso x‖ ≤ 1`.
* `New.HeightLe c y`: the family `y`, with one complex number for each `ι`, has height at most `c`:
  for some `H ≠ 0`, bounds for all `log |σ H|` and for `log ‖ι (H y_ι)‖` at each prime add up to at
  most `c`.
* `New.formGram G v`: the matrix of the products `v_i* G v_k`.

## Relation to the literature

Size-versus-divisibility bounds for a determinant are known in the literature. Related work: Bost,
Algebraic leaves of algebraic foliations over number fields, 2001; Laurent, Linear forms in two
logarithms and interpolation determinants, 1994.


### `conj`

 The isomorphism `ῑ`, with `ῑ z = ι z̄`. 

### `place`

 The embedding `ℂ → ℂ_l` given by `ι ∣ l`. 

### `integers`

 The valuation ring `𝒪_ι` of the valuation that `ι` induces on `ℂ`. 

### `norm_place`

 The embedding `ℂ → ℂ_l` given by `ι ∣ l` induces the same absolute value on `ℂ` as `ι`. 

### `inv_pow_le_norm_of_dvd`

 Let `ι` consist of the prime `l = ι.prime` and the isomorphism `ι.iso : ℂ ≃ ℚ̄_l`. If `x`
divides `l ^ j` in the valuation ring `𝒪_ι`, then `‖ι x‖ ≥ l ^ (-j)`. 

### `Carries`

 The square matrix `u` over `𝒪_ι` carries the family `y` into `M` with loss `a`: the combinations
`∑ u_ik y_k` lie in `M`, and the valuation of `det u` at `ι` is at most `a`. 

### `Carries.le_norm_det`

 `‖ι (det u)‖ ≥ l ^ (-a)`: the valuation of `det u` at `ι ∣ l` is at most `a`. 

### `Carries.sum_smul_mem`

 The combinations `∑ u_ik y_k` lie in `M`. 

### `Carries.fromBlocks`

 Let `ι` consist of a prime `l` and an isomorphism `ℂ ≃ ℚ̄_l`, and let `𝒪_ι = ι.integers` be the
ring of complex numbers `x` with `‖ι x‖ ≤ 1`. If `u` carries `y` into `M` with loss `a` and `u'`
carries `y'` into `M` with loss `a'`, then the block diagonal matrix with blocks `u` and `u'`
carries the union of the two families into `M` with loss `a + a'`. 

### `conjAut`

 The automorphism `σ'` of `ℂ`, with `σ' z = conj (σ (conj z))`. 

### `TwistedLattice`

 A twisted lattice on `V`, with twists `ξ : T` and trivial twist `1`: linear maps `Θ_ξ` to inner
product spaces, in each of them a module of vectors integral at `ι`, such that, if `ξ` is allowed at
the prime of `ι`, products of vectors integral at `ῑ` with vectors integral at `ι` are integral at
`ι`, and coordinates for the trivial twist in which the inner product has a rational matrix. 

### `TwistedLattice.Space`

 The inner product space for the twist `ξ`. 

### `TwistedLattice.lift`

 The map `Θ_ξ`. 

### `TwistedLattice.IsAllowed`

 The twist `ξ` is allowed at the prime `l`. 

### `TwistedLattice.lattice`

 The vectors for the twist `ξ` that are integral at `ι`. 

### `TwistedLattice.norm_inner_le_one`

 For `ξ` allowed at the prime of `ι`, the product of a vector integral at `ῑ` and a vector
  integral at `ι` is integral at `ι`. 

### `TwistedLattice.Coord`

 The set of coordinates on the space for the trivial twist. 

### `TwistedLattice.coord`

 The coordinates of a vector. 

### `TwistedLattice.gramMatrix`

 The rational matrix of the inner product in these coordinates. 

### `TwistedLattice.posDef_gramMatrix`

 The matrix defines an inner product on all coordinate vectors. 

### `TwistedLattice.inner_eq`

 The inner product is the one induced from coordinate vectors. 

### `integralVectors`

 The vectors of `V` that are integral at `ι ∣ l`: those `y` for which `Θ_ξ y` is integral at `ι`
for every twist `ξ` allowed at `l`. 

### `IndexLe`

 The family `y` has index at most `δ`: there are numbers `δ_l = e l ≥ 0` with `∑ δ_l log l ≤ δ`,
the sum taken over primes, such that for every `ι ∣ l` some matrix over `𝒪_ι` carries the family
into the vectors integral at `ι` with loss `δ_l`. The matrix does not depend on the twist. 

### `IndexLe.of_comp_equiv`

 Let `L` be a twisted lattice on `V`. The index does not depend on the numbering of the family:
if `y ∘ f` has index at most `δ` for a bijection `f`, then so has `y`. 

### `indexLe_of_colengthDvd`

 Let `L` be a twisted lattice on `V`, and let `e l ≥ 0` with `∑ e l log l ≤ δ` over every finite
set of primes. Suppose that for every prime `l` and every `ι ∣ l` (so `l = ι.prime`) the family `y`
lies in an `𝒪_ι`-module `M` all of whose finite families are taken into the vectors integral at `ι`
by matrices with determinant dividing `l ^ j` (`New.ColengthDvd`), where `j ≤ e l`. Then `y` has
index at most `δ` (`IndexLe`): for some `δ_l ≥ 0` with `∑ δ_l log l ≤ δ` and each `ι ∣ l`, a matrix
`u` over `𝒪_ι` with `‖ι (det u)‖ ≥ l ^ (-δ_l)` takes `y` into the vectors integral at `ι`. 

### `IndexLe.sumElim`

 Let `L` be a twisted lattice on `V`. If two families have index at most `δ` and `δ'`, then their
union `Sum.elim y y'` has index at most `δ + δ'`. 

### `indexLe_card_mul`

 Let `t` be a finite set of indices, and suppose that for each `s ∈ t` every finite family in the
set `A s ⊆ V` has index at most `δ`. Then a finite family `y` with all its members in the union of
these sets has index at most `#t δ`. 

### `toBlocks₁₁_formGram_sumElim`

 The upper left block of the Gram matrix of the union of `v` and `w` is the Gram matrix
of `v`. 

### `toBlocks₂₂_formGram_sumElim`

 The lower right block of the Gram matrix of the union of `v` and `w` is the Gram matrix
of `w`. 

### `conjCoord`

 The coordinates of `σ Θ₁ y`: those of `Θ₁ y`, with `σ` applied to each of them. 

### `normSqAt`

 The number `‖Θ₁ y‖_σ² = ⟨σ Θ₁ y, σ Θ₁ y⟩`, with the product given by the rational matrix
`L.gramMatrix` on coordinate vectors. 

### `CovolumeLe`

 The family `y` has covolume at most `c`: for every automorphism `σ` of `ℂ` the determinant of
the products `⟨σ Θ₁ y_i, σ Θ₁ y_k⟩`, taken by the rational Gram matrix on the coordinate vectors
`L.conjCoord σ (y i)`, has absolute value at most `exp c`. 

### `map_inner_lift_one`

 Since the Gram matrix `L.gramMatrix` is rational, `σ ⟪Θ₁ v, Θ₁ w⟫ = ⟨σ' Θ₁ v, σ Θ₁ w⟩`, where
`Θ₁ = L.lift 1` and `σ' = conjAut σ`, with `σ' z = conj (σ (conj z))`; the right side pairs the
coordinate vectors `L.conjCoord` by the Gram matrix. 

### `CovolumeLe.norm_map_det_gram_le`

 **Gram determinants, conjugates.** Let `L` be a twisted lattice on `V`, with map `Θ₁ = L.lift 1`
for the trivial twist. For an automorphism `τ` of `ℂ`, write `τ Θ₁ v` for the coordinate vector of
`Θ₁ v` with `τ` applied to each coordinate (`conjCoord`); such vectors are paired by the rational
matrix `L.gramMatrix` of the inner product. If `y` has covolume at most `c`, that is,
`|det ⟨τ Θ₁ y_i, τ Θ₁ y_k⟩| ≤ exp c` for all `τ`, then `|σ Gram(1)| ≤ exp c` for every automorphism
`σ`, where `Gram(1) = det ⟨Θ₁ y_i, Θ₁ y_k⟩`. 

### `covolumeLe_of_normSqAt_le`

 Let `L` be a twisted lattice on `V`, with map `Θ₁ = L.lift 1` for the trivial twist. For an
automorphism `σ` of `ℂ`, apply `σ` to the coordinates of `Θ₁ v` and pair the results by the rational
Gram matrix: `L.normSqAt v σ = ‖Θ₁ v‖_σ²` is the product of such a vector with itself, and a family
has covolume at most `c` (`CovolumeLe`) if for every `σ` the determinant of these products of its
members has absolute value at most `exp c`. If `‖Θ₁ z_i‖_σ² ≤ exp h` for all `i` and `σ`, then
`z_1, …, z_n` has covolume at most `n h`. This is Hadamard's inequality. 

### `CovolumeLe.sumElim`

 **Gram determinants, adjoining vectors.** Let `L` be a twisted lattice on `V`, with map
`Θ₁ = L.lift 1` for the trivial twist. For an automorphism `σ` of `ℂ`, write `σ Θ₁ v` for the
coordinate vector of `Θ₁ v` with `σ` applied to each coordinate (`conjCoord`); such vectors are
paired by the rational matrix `L.gramMatrix` of the inner product. If `y` has covolume at most `c`,
that is, `|det ⟨σ Θ₁ y_i, σ Θ₁ y_k⟩| ≤ exp c` for all `σ`, and
`L.normSqAt (z i) σ = ⟨σ Θ₁ z_i, σ Θ₁ z_i⟩ ≤ exp h` for all `i` and `σ`, then the family `y`
together with `z_1, …, z_n` has covolume at most `c + n h`. This is Fischer's inequality together
with Hadamard's. 

### `volume`

 The number `Z(ξ) = det (Θ_ξ* Θ_ξ)`, the Gram determinant of the images of an orthonormal basis
of `V`. 

### `volume_eq_det_adjoint_comp`

 If the space `L.Space ξ` for `ξ` has finite dimension, the volume `Z(ξ) = L.volume ξ` is the
determinant of `Θ_ξ* Θ_ξ` on `V`, where `Θ_ξ = L.lift ξ`. 

### `norm_det_mul_det_gram_le_one`

 **Gram determinants, valuations.** Let `L` be a twisted lattice on `V` with maps
`Θ_ξ = L.lift ξ`. Let `ι` consist of a prime `l` and an isomorphism `ι.iso : ℂ ≃ ℚ̄_l`, and let
`ῑ z = ι z̄`. Let `ξ` be allowed at `l`. If `u` takes the vectors `Θ_ξ w_i` to vectors integral at
`ι` and `u'` takes them to vectors integral at `ῑ`, then
`‖ι (conj (det u') · Gram(ξ) · det u)‖ ≤ 1`, where `Gram(ξ) = det ⟨Θ_ξ w_i, Θ_ξ w_k⟩`. 

### `exists_matrix_elim_mem_lattice`

 Let `L` be a twisted lattice with maps `Θ_ξ = L.lift ξ`, let `ι ∣ l`, and let the twist `ξ` be
allowed at `l`. Let `u` take `y` into `L.integralVectors ι`, and let the vectors `γ Θ_ξ z_i` be
integral at `ι`. Then a matrix `v` with `det v = det u · γ ^ n'` takes
`Θ_ξ y_1, …, Θ_ξ y_n, Θ_ξ z_1, …, Θ_ξ z_n'` to vectors integral at `ι`. 

### `norm_pow_mul_det_gram_le`

 Let `L` be a twisted lattice with maps `Θ_ξ = L.lift ξ`. Let `l = ι.prime`, so that
`‖ι x‖ = ‖ι.iso x‖` is the `l`-adic absolute value of `x` under `ι.iso : ℂ ≃ ℚ̄_l`, and let
`ῑ z = ι z̄`. Let `ξ` be allowed at `l`, let `u` carry `y` into the vectors integral at `ι` and `u'`
carry `y` into those integral at `ῑ`, both with loss `a`, and let the vectors `γ Θ_ξ z_i` be
integral both at `ι` and at `ῑ`. Then `‖ι (|γ| ^ (2 n') Gram(ξ))‖ ≤ l ^ (2 a)`, where `Gram(ξ)` is
the Gram determinant of the images of `y_1, …, y_n, z_1, …, z_n'` under `Θ_ξ`. 

### `heightLe_pow_mul_det_gram`

 Let `L` be a twisted lattice with maps `Θ_ξ = L.lift ξ`. Let `y` have index at most `δ`, let
`ξ_ι = θ ι` be allowed at the prime of `ι`, and let the vectors `γ_ι Θ_{ξ_ι} z_i` be integral both
at `ι` and at `ῑ`, where `ῑ z = ι z̄`. Let `Gram(ξ)` be the Gram determinant of the images of
`y_1, …, y_n, z_1, …, z_n'` under `Θ_ξ`. Then the family `x_ι = |γ_ι| ^ (2 n') Gram(ξ_ι)` has height
at most `2 δ` (`New.HeightLe`): for some common `H ≠ 0`, the bounds for `log |σ H|` over
automorphisms `σ` of `ℂ` and for `log ‖ι (H x_ι)‖` at the primes add up to at most `2 δ`. 

### `covolume_add_index_nonneg`

 **A twist for each prime.** Let `L` be a twisted lattice on `V` with maps `Θ_ξ = L.lift ξ`, all
injective. Let `y_1, …, y_n, z_1, …, z_n'` be a basis of `V`, and let `ξ_ι = θ ι` be allowed at the
prime of `ι`. Suppose that
* `y` has covolume at most `c` and index at most `δ`;
* `γ(ξ) ≠ 0`, and `γ(ξ) Θ_ξ z_i` is integral at all `ι ∣ l` for `ξ` allowed at `l`;
* `⟨σ Θ₁ z_i, σ Θ₁ z_i⟩ ≤ exp b_short` for all automorphisms `σ` of `ℂ`;
* the families `|γ(ξ_ι)| ^ (-2)` and `Z(1) / Z(ξ_ι)` have height at most `b_denom` and `b_volume`
  respectively.

Then `c + 2 δ + n' (b_short + b_denom) + b_volume ≥ 0`. 
