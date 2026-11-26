---
{
  "module": "src/Lib/Weil/DualPair/KernelDecay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/KernelDecay.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/KernelDecay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rapid decay of theta kernels of unitary dual pairs under support conditions

This file proves that the theta kernel `New.pairTheta` of the dual pair U(S) × U(T), acting on
data on Hom(S, T) through `New.pairWeil`, decays rapidly under support conditions on the finite
datum `Ψ`. The kernel is `(g, h) ↦ θ (ω (g, h) φ)`, with `g` in the adelic group of `S` and `h` in
that of `T`. At a point of large height the proof uses short pairs of rational matrices
(`New.IsShortPair`) and the rational maps of rank one `dᵢ ⟨cⱼ, ·⟩` that they span.
`New.modDatum S T 𝔪 Ψ v` is the datum `v ⊗ Ψ ⊗ vac` on `Hom(S, T)`, where `Ψ` is a function on
matrices modulo an ideal `𝔪` prime to its conjugate (`New.Modulus`), and `New.pairTheta` is its
theta kernel on `U(S) × U(T)`.

## Main definitions and results

* `New.pairTheta_decay_of_onto`: rapid decay of the theta kernel on U(T) when Ψ is supported on
  surjective maps.
* `New.pairTheta_decay_of_injective`: rapid decay of the theta kernel on U(S) when Ψ is supported on
  injective maps.
* `New.pairTheta_modDatum_decay`: suppose some place divides `𝔪` and `Ψ` is supported on left
  invertible matrices. Then the kernel decays rapidly in the height of `g`, with polynomial growth
  in the height of `h`.

Notions from other files:
* `New.Space`: A hermitian space with a point: a matrix J over E and x in GL_n(𝔸) with xᴴJx equal to
  diag(s) at the infinite places and 1 at the finite places; Γ = x⁻¹U(J)(E)x.
* `New.Space.IsAutomorphic`, `New.Space.IsRapid`: a function F is automorphic if it is continuous,
  left Γ-invariant and right invariant under an open subgroup of G_f; it is rapid if |F(g)|·ht(g)^B
  is bounded for every B, and moderate (`New.Space.IsModerate`) if |F(g)| ≤ C·ht(g)^A for some C and
  A.
* `New.Modulus.liftFn`: A function Ψ of vectors modulo 𝔪 read on finite adelic vectors x: Ψ of the
  reduction of the components of x at the places dividing 𝔪 if these are integral, else 0.
* `New.Space.coordMatrix` (in `Lib.Weil.DualPair.ShortIsotropicVectors`): the coordinates
  `g⁻¹ x⁻¹ c` at an adelic point `g` of a matrix `c` over `E`.
* `New.Space.adelicPoints` (in `Lib.Weil.DualPair.ShortIsotropicVectors`): the span over the
  adeles of the adelic vectors of the elements of a subspace `Z` of `V`.

## Relation to the literature

Theta kernels of unitary dual pairs, with functoriality, seesaw, growth and rapid decay, are known.
Here both spaces are hermitian and act on the maps between them. Decay is proved for data
supported on maps of full rank at split places, using small shifts along a short isotropic vector
instead of Siegel sets. Source: S. Kudla, Seesaw dual reductive pairs, Progr. Math. 46 (1984);
Harris, Kudla, Sweet, Theta dichotomy for unitary groups, J. Amer. Math. Soc. 9 (1996), section 1;
for decay, Kudla, Rallis, A regularized Siegel-Weil formula: the first term identity, Ann. Math. 140
(1994).


 ### Short pairs 

### `Space.rankOneMaps`

 The matrix of the map `z ↦ d z cᴴ S.J` on matrices written as vectors. Its columns are the
rational maps `dᵢ ⟨cⱼ, ·⟩`, where `dᵢ` and `cⱼ` are the columns of `d` and `c` and `⟨·, ·⟩` is the
form of `S`. 

### `IsShortPair`

 The conditions of the decay estimate at a point `(g, h)`, with `g` in the group of
`S : Space E n s` and `h` in that of `T : Space E n' s'`, on rational matrices `d` for `T` and `c`
for `S`, for a functional `ℓ` and a function `Ψ` on finite adelic maps. Below `d'` and `c'` are the
coordinates `Space.coordMatrix` of `d` at `h` and of `c` at `g`. 

### `IsShortPair.short_target`

 The columns of `d` are vectors of length at most `x` in the lattice at `h`. 

### `IsShortPair.short_source`

 The columns of `c` are vectors of length at most `y` in the lattice at `g`. 

### `IsShortPair.mul_le`

 The product of the two length bounds is at most `t`. 

### `IsShortPair.isotropic`

 The columns of `d`, or those of `c`, span an isotropic subspace. 

### `IsShortPair.invariant`

 `ℓ` is invariant under the Heisenberg operators of the rational maps `z cᴴ S.J`. 

### `IsShortPair.ne_zero_or_mean_eq_zero`

 Either the finite part of `d'ᴴ u c'` is not zero whenever `Ψ u ≠ 0`, or the mean of `ℓ ∘ ϱ u`
  over the adelic points `u` of the span of the maps `dᵢ ⟨cⱼ, ·⟩` is zero. 

### `Space.move_vecAtPoint_col`

 The coordinates at `g` of a column of `c` form the column of `Space.coordMatrix`. 

### `Space.mem_adelicPoints_span_col_iff`

 The adelic points of the span of the columns of `c` are the vectors `g c' w`, where `c'` is the
matrix of coordinates of `c` at `g` (`Space.coordMatrix`) and `w` is an adelic vector. 

### `coordMatrix_rankOneMaps`

 At the point `(g, h)` the maps `dᵢ ⟨cⱼ, ·⟩` have the coordinates `d'ᵢ c'ⱼᴴ ε`, where `d'` and
`c'` are the coordinates of `d` at `h` and of `c` at `g`, and `ε` is the standard form. 

### `col_rankOneMaps_mem_latticeBall`

 If the columns `dᵢ` and `cⱼ` are vectors of lengths at most `x` and `y` in the lattices at `h`
and `g`, then the map `dᵢ ⟨cⱼ, ·⟩` has length at most `x y` and lies in the lattice of Hom(S, T) at
`(g, h)`. 

### `isotropic_span_rankOneMaps`

 If the columns of `d`, or those of `c`, span an isotropic subspace, then the maps `dᵢ ⟨cⱼ, ·⟩`
span an isotropic subspace of Hom(S, T). 

### `mem_span_rankOneMaps_iff`

 If `d` is invertible, the maps `dᵢ ⟨cⱼ, ·⟩` span the space of all maps `z cᴴ S.J`. 

### `IsShortPair.invariant_span`

 For a short pair `d`, `c`, the functional `ℓ` is invariant under the Heisenberg operators of the
span of the maps `dᵢ ⟨cⱼ, ·⟩`. 

### `exists_norm_schrodingerOp_le_of_isShortPair`

 Let `E` be a CM field with Weil data, `a`, `b` automorphic characters, `Ψ` Schwartz–Bruhat above
a set `P` of finite places disjoint from its conjugate, `f₀` in the finite part of the data space of
Hom(S, T), and `l` a natural number. There is `C ≥ 0`, independent of `g`, `h`, `ℓ`, `d`, `c`, `x`,
`y`, `t`, with the following property. Whenever `IsShortPair g h ℓ Ψ d c x y t` holds (the
conditions of the decay estimate at `(g, h)` on rational matrices `d` for `T` and `c` for `S`, the
functional `ℓ`, `Ψ` and reals `x`, `y`, `t`), every Fock-space vector `v` with finite moment
`fockMoment l v` satisfies `‖ℓ (ω (g, h) (v ⊗ Ψ⊗ f₀))‖ ≤ C ‖ℓ ∘ ω (g, h)‖ |t| ^ l ‖v‖_l`, where
`ω = pairWeil S T a b`, `Ψ⊗` is `schrodingerOp` and `v ⊗ ·` is `integrated`. 

### `exists_norm_pairWeil_schrodingerOp_mul_pow_le`

 Decay estimate. Let `Ψ` be Schwartz–Bruhat above a set `P` of finite places disjoint from its
conjugate, and let `f₀` lie in the finite part of 𝒮(Hom(S,T)), the span of the finite Heisenberg
translates of the vacuum. Then there is C, independent of `v`, `g`, `h`, `ℓ`, `ρ`, `H`, with the
following property: if ρ ≥ 1, H > 0, the moment
‖v‖_{N+A} = `fockMoment (N + A) v` = ∫(1+‖y‖)^{N+A}|v(y)| dy is finite, L = ℓ ∘ ω(g, h)
(ω = `pairWeil S T a b`) satisfies ‖L f‖ ≤ Y ‖f‖ (ρH)^A for all f, and for H > 2 there are rational
matrices d (n' × p), c (n × q) and reals x, y with `IsShortPair g h ℓ Ψ d c x y (Z ρ (2 / H))`, then
‖L(v ⊗ Ψ ⊗ f₀)‖ H^N ≤ C ‖v‖_{N+A} ρ^{N+2A}, where v ⊗ Ψ ⊗ f₀ = ∫ v(y) ϱ(y)(Ψ⊗ f₀) dy. 

### `pairTheta_decay_of_onto`

 Data on surjective maps decay rapidly on the target group. Let `Ψ` be Schwartz–Bruhat above a
set `P` of finite places disjoint from its conjugate. Suppose that every map `y` with `Ψ y ≠ 0` has
a right inverse after the ring map `φ` to a nonzero ring (for evaluation at a place `w`: `y` is
surjective at `w`). Then the theta kernel of `v ⊗ Ψ ⊗ vac` at `(g, k)`, times the `N`-th power of
the height of `k`, is at most a constant times a moment of `v` (`fockMoment`) times a power of the
height of `g`. 

### `pairTheta_decay_of_injective`

 Data on injective maps decay rapidly on the source group. Let `Ψ` be Schwartz–Bruhat above a
set `P` of finite places disjoint from its conjugate. Suppose that every map `y` with `Ψ y ≠ 0` has
a left inverse after the ring map `φ` to a nonzero ring (for evaluation at a place `w`: `y` is
injective at `w`). Then the theta kernel of `v ⊗ Ψ ⊗ vac` at `(g, k)`, times the `N`-th power of
the height of `g`, is at most a constant times a moment of `v` (`fockMoment`) times a power of the
height of `k`. 

### `Rows.modulusResidue`

 For a place w dividing 𝔪, the reduction map from O_E/𝔪 to the residue field at w. 

### `Rows.isPrimitiveMatrix_of_liftFn_ne_zero`

 Suppose Ψ(y) ≠ 0 forces the matrix of entries of y arranged by e to have a left inverse
modulo 𝔪. Then wherever the adelic lift of Ψ is nonzero, the matrix so arranged is primitive
over O_w at each w dividing 𝔪. 

### `Space.height_sum_le`

 The height on the orthogonal sum of `S` and `T` is at most the product of the heights. 

### `modDatum_eq_sum`

 The datum is linear in `Ψ`: it is the combination of the data of the indicator functions of
single matrices. 

### `pairTheta_modDatum_decay`

 Let `E` be a CM field with Weil data, `a`, `b` automorphic characters in `AutChar E`, and `Ψ` a
function on `n' × n` matrices modulo `𝔪` supported on left invertible matrices, with some place
dividing `𝔪`. Let `K` be the theta kernel `pairTheta S T a b` of `modDatum S T 𝔪 Ψ v`, the datum
`v ⊗ Ψ ⊗ vac` that is the Fock vector `v` at the infinite places, `Ψ` at the places dividing `𝔪`,
and the vacuum at the other finite places. For each exponent `M` there are `B`, `N`, `C`,
independent of `v`, `g`, `h`, such that for every `v` with finite moment
`fockMoment N v` = ∫ (1 + ‖y‖)^N |v(y)| dy, we have
`‖K (g, h)‖ S.height g ^ M ≤ C (fockMoment N v) T.height h ^ B`. 

### `pairTheta_modDatum_decay_of_rightInv`

 Let `E` be a CM field with Weil data, `a`, `b` automorphic characters in `AutChar E`, and `Ψ` a
function on `n' × n` matrices modulo `𝔪` supported on right invertible matrices (the transpose has a
left inverse), with some place dividing `𝔪`. Let `K` be the theta kernel `pairTheta S T a b` of
`modDatum S T 𝔪 Ψ v`, the datum `v ⊗ Ψ ⊗ vac` that is the Fock vector `v` at the infinite places,
`Ψ` at the places dividing `𝔪`, and the vacuum at the other finite places. For each exponent `M`
there are `B`, `N`, `C`, independent of `v`, `g`, `h`, such that for every `v` with finite moment
`fockMoment N v` = ∫ (1 + ‖y‖)^N |v(y)| dy, we have
`‖K (g, h)‖ T.height h ^ M ≤ C (fockMoment N v) S.height g ^ B`. 
