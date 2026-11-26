---
{
  "module": "src/Lib/Weil/DualPair/ShortIsotropicVectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ShortIsotropicVectors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/ShortIsotropicVectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Short isotropic vectors and means of theta functionals over isotropic subspaces

This file prepares the rapid decay of theta kernels under a support condition on Ψ, on the data
space of Hom(S, T), which carries the representation `New.pairWeil`. The datum v ⊗ Ψ ⊗ f₀ is
`integrated _ v (schrodingerOp _ P Ψ f₀)`, with v in Fock space, Ψ Schwartz–Bruhat above a set P
of finite places disjoint from its conjugate (`New.IsSchwartzBruhat`), and f₀ in the finite part
`New.Space.finitePart`. The argument is the one for cusp forms. At a point of large height the
lattice has a short isotropic vector, and θ is invariant under the rational maps of rank one
through it. The mean over the adelic maps of this kind vanishes by the support condition on Ψ
(`New.map_schrodingerOp_eq_zero_of_invariant`), and θ is close to this mean because the maps are
short (`New.Space.exists_norm_sub_subspaceMean_le`).

## Main definitions and results

* `New.Space.exists_short_isotropic`: If the height of `g` exceeds `2`, then the lattice of `S` at
  `g` contains a nonzero isotropic vector, written as a matrix with one column, of length at most
  `2 / height g` (`latticeBall`).
* `New.Space.exists_norm_sub_subspaceMean_le`: for vectors `z i` of the lattice at `g` of lengths
  at most `δ` spanning an isotropic subspace `Z`, a bounded functional invariant under the
  Heisenberg operators of `Z` is close, on data with finite part `f₀`, to its mean
  `New.Space.subspaceMean` over the adelic points of `Z` modulo the rational ones.

Notions from other files:
* `New.G`: The adelic unitary group G = G_∞ × G_f for signs s at the infinite places and the
  identity matrix at the finite places.
* `New.Space`: A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
  diag(s) at the infinite places and 1 at the finite places; Γ = x⁻¹U(J)(E)x.

## Relation to the literature

Known; see `Lib.Weil.DualPair.KernelDecay` for sources.


 ### Rational matrices in adelic coordinates, short vectors 

### `Space.coordMatrix`

 The coordinates at an adelic point `g` of a matrix `c` over `E`: the adelic matrix `g⁻¹ x⁻¹ c`,
where `x = S.x` carries the form of `S` to the standard form. 

### `Space.mul_coordMatrix_ne_zero`

 Let `c ≠ 0` be a matrix over `E` with coordinates `c'` at `g`, let `X` be an invertible adelic
matrix, and let `M` be a finite adelic matrix that has a left inverse after a ring map `φ` from the
finite adeles to a nonzero ring. Then the product of the finite part of `Xᴴ`, of `M` and of the
finite part of `c'` is not zero. 

### `Space.coordMatrix_mul_ne_zero`

 Let `c ≠ 0` be a matrix over `E` with coordinates `c'` at `g`, let `X` be an invertible adelic
matrix, and let `M` be a finite adelic matrix that has a right inverse after a ring map `φ` from the
finite adeles to a nonzero ring. Then the product of the finite part of `c'ᴴ`, of `M` and of the
finite part of `X` is not zero. 

### `Space.exists_short_isotropic`

 If the height of `g` exceeds `2`, then the lattice of `S` at `g` contains a nonzero isotropic
vector, written as a matrix with one column, of length at most `2 / height g` (`latticeBall`). 

### `apply_vecAtPoint`

 The function x ↦ θ(ϱ(x)f) has the same value at a rational vector as at 0. 

 ### Supports 

### `Space.map_eq_zero_of_support_not_orthogonal`

 Let `Ψ` be Schwartz–Bruhat above a set `P` of finite places disjoint from its conjugate, `I` a
submodule of the adelic vectors of `V`, and `A` a bounded linear map on `𝒮 V` that is invariant
under the Heisenberg operators `ϱ z` for `z` in `I`. If no `y` with `Ψ y ≠ 0` is orthogonal to the
finite part of `I`, then `A` kills `Ψ ⊗ f` (`schrodingerOp`). 

### `shiftMatrix`

 The matrix of the map `z ↦ X z Yᴴ ε` on matrices written as vectors, where `ε` is the standard
form of signs `s`. 

### `map_schrodingerOp_eq_zero_of_invariant`

 Let `Ψ` be Schwartz–Bruhat above a set `P` of finite places disjoint from its conjugate. Let
`ℓ` be a bounded functional on the data space of Hom(S, T) that is invariant under the Heisenberg
operators `ϱ (X z Yᴴ ε)` for all adelic `z` (`shiftMatrix`; `ε` is the standard form). If the finite
part of `Xᴴ y Y` is not zero for every `y` with `Ψ y ≠ 0`, then `ℓ` kills `Ψ ⊗ f`
(`schrodingerOp`). 

 ### Short isotropic vectors 

### `Space.adelicPoints`

 The adelic points of a subspace `Z` of `V`: the span over the adeles of the adelic vectors of
the elements of `Z`. 

### `Space.ratPoints`

 The rational points among the adelic points of a subspace `Z` of `V`: the adelic vectors of the
elements of `Z`. 

### `Space.mem_adelicPoints_span_range_iff`

 The adelic points of the span of finitely many vectors `z i` are the adelic combinations of the
adelic vectors of the `z i`. 

### `exists_toAdele_add_eq_nsmul`

 There is `R > 0` such that, for every nonzero natural number `M`, every adele is congruent
modulo `E` to `M` times an adele with integral finite part and infinite components of modulus at
most `R`. 

### `Space.adelicCombination`

 The map `c ↦ ∑ c i • z i` from adelic coefficients to the adelic points of the span of the
vectors `z i`. 

### `Space.adelicCombination_surjective`

 Every adelic point of the span of the `z i` is an adelic combination of the `z i`. 

### `Space.ratVectors_le_comap_adelicCombination`

 The map `c ↦ ∑ c i • z i` carries rational coefficients to rational points of the span. 

### `Space.compactSpace_adelicPoints_quotient`

 The adelic points of a subspace `Z` of `V` modulo the rational ones form a compact group. 

### `Space.subspaceMean`

 The mean of a function `F` on adelic vectors over the adelic points of a subspace `Z` of `V`
modulo the rational ones, for the Haar probability measure of this compact group. It is meant for
`F` periodic under the rational points. 

### `Space.subspaceMean_span_range`

 The mean over the adelic points of the span of vectors `z i` may be computed in the coordinates
`c ↦ ∑ c i • z i`, as a mean over adelic `c` modulo rational `c`, if the function is continuous and
periodic under the rational points. 

### `Space.rho_add_of_mem_adelicPoints`

 On the adelic points of an isotropic subspace `Z` of `V`, the Heisenberg operators compose
without a cocycle. 

### `Space.isContPeriodic_ratPoints`

 Let `Z` be an isotropic subspace of `V` and `Λ` a bounded functional that is invariant under the
Heisenberg operators of `Z`. Then `x ↦ Λ (ϱ x f)` is continuous on the adelic points of `Z` and
periodic under the rational ones. 

### `Space.exists_eq_subspaceMean`

 Let `V` be a hermitian space over the CM field `E` with Weil data. Let `Z` be a subspace of
`E^n` that is isotropic for the form `J` of `V`. Let `Λ` be a bounded (continuous linear) functional
on the Schwartz space `𝒮 V` with `Λ (V.ϱ (V.vecAtPoint γ) f) = Λ f` for every rational vector
`γ ∈ Z`, where `V.ϱ x` is the Heisenberg operator of the adelic vector `x`. Then the mean
(`V.subspaceMean Z`) of `x ↦ Λ (V.ϱ x f)` over the adelic points of `Z` modulo the rational ones is,
as a function of `f`, again a bounded functional `Λ₀` on `𝒮 V`. 

### `Space.subspaceMean_rho`

 Let `Z` be an isotropic subspace of `V`, `Λ` a bounded functional that is invariant under the
Heisenberg operators of `Z`, and `Λ₀` the mean of `Λ ∘ ϱ x` over the adelic points `x` of `Z` modulo
the rational ones. Then `Λ₀` is invariant under `ϱ y` for all adelic points `y` of `Z`. 

### `Space.exists_rho_nsmul_eq_self`

 Let `f₀` lie in the finite part of `𝒮 V`. There is a nonzero natural number `M` such that, for
every adelic vector `u` with integral finite part, the Heisenberg operator of the finite part of
`M • u` fixes `f₀`. 

### `Space.exists_rho_eq_realHeisenbergOp`

 Let `f₀` lie in the finite part of `𝒮 V` and let `ι` be a finite index type. There is `C` as
follows. Let the vectors `z i` lie in the lattice at `g` with lengths at most `δ ≥ 0`
(`latticeBall`). Then every adelic point `x` of their span has a rational translate `γ + x` such
that `ϱ (g⁻¹ (γ + x))` acts on the data `v ⊗ f₀` (`integrated`) as a real translation of `v`
(`realHeisenbergOp`) by a vector whose coordinates have modulus at most `C δ`. 

### `Space.rho_omega`

 The Heisenberg operator of `x` passes through the Weil operator `ω g` as that of `g⁻¹ x`. 

### `Space.exists_norm_le_of_differences`

 Differencing along short isotropic vectors. Let `f₀` lie in the finite part of `𝒮 V`, let `l` be
a natural number and `ι` a finite index type. There is `C` as follows. Let the vectors `z i` of the
lattice at `g` have lengths at most `δ ≥ 0` and span an isotropic subspace `Z`. Let `Λ` be a bounded
functional that is invariant under the Heisenberg operators `ϱ` of `Z`. Suppose that, for all `f`,
a bound for the differences `‖Λ (ω g f) - Λ (ϱ x (ω g f))‖` at all adelic points `x` of `Z` bounds
`‖Λ (ω g f)‖`. Then `‖Λ (ω g (v ⊗ f₀))‖ ≤ C ‖Λ ∘ ω g‖ δ ^ l ‖v‖_l` for all `v` whose moment `‖v‖_l`
(`fockMoment`) is finite. Here `v ⊗ f₀` is `V.integrated v f₀`. 

### `Space.exists_norm_sub_subspaceMean_le`

 Let `f₀` lie in the finite part of `𝒮 V`, let `l` be a natural number and `ι` a finite index
type. There is `C` as follows. Let `g` be an adelic point of the unitary group, `δ ≥ 0`, and let the
vectors `z i` of the lattice at `g` have lengths at most `δ` (`latticeBall`) and span an isotropic
subspace `Z` of `V`. Let `Λ` be a bounded functional on `𝒮 V` that is invariant under the Heisenberg
operators `ϱ` of `Z`, and `Λ₀` the mean of `Λ ∘ ϱ x` over the adelic points `x` of `Z` modulo the
rational ones (it exists by `exists_eq_subspaceMean`). Then `‖(Λ - Λ₀) (ω g (v ⊗ f₀))‖ ≤ C ‖Λ ∘ ω g‖
δ ^ l ‖v‖_l` for all `v` in Fock space whose moment `‖v‖_l` (`fockMoment`) is finite. Here `ω` is
the Weil representation and `v ⊗ f₀` is `V.integrated v f₀`. 
