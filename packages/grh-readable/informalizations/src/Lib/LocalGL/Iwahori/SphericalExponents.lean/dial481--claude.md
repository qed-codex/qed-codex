---
{
  "module": "src/Lib/LocalGL/Iwahori/SphericalExponents.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/SphericalExponents.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/SphericalExponents.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponents that survive on spherical vectors, and a Hecke operator on parahoric eigenvectors

Let `F` be a field with a valuation in `ℤᵐ⁰` and compact ring of integers `𝒪`, with maximal ideal
`𝔭`, uniformiser `ϖ` and residue field of order `q`, and let `K0 = New.proIwahori` be the pro-`p`
Iwahori subgroup of `GL_N(𝒪)`. An exponent is a linear form that is an eigenform for the torus
character `New.torusChar θ = ∏ θ_i(t_i) |t_i| ^ (N - 1 - i)`. This file proves that a non-zero
exponent for `New.torusChar θ` with unramified `θ_i` and non-increasing `|θ_i(ϖ)|` is non-zero on
the vectors fixed by `GL_N(𝒪)`. The proof uses orbit sums for the parahoric subgroups
`P = New.blockParahoric (min m)`, whose columns before `m` lie in `𝔭` below the diagonal, and the
permutation matrices `New.permGL`. For `F` the completion of a number field at a finite place, it
also shows that the Hecke operator of `diag (ϖ, 1, …, 1)` keeps the `New.proIwahori`-fixed
eigenvectors, with eigenvalue depending only on the top left entry, of the stabiliser of a line,
`New.blockParahoric (min 1)`, the matrices in `GL_N(𝒪)` whose first column is in `𝔭` below the
corner.

## Main definitions and results

* `New.Patching.parahoricEigenspace`: for a level function `f` and a function `c` on the group, the
  vectors fixed by `New.proIwahori` on which each `k` in the parahoric subgroup of `f` acts by the
  scalar `c k`.
* `New.Patching.parahoricEigenspace_mem_invtSubmodule`: the Hecke operator of `diag (ϖ, 1, …, 1)`
  keeps this space when `f = min 1` and `c` is a function of the top left entry.
* `New.IsExponent.eq_zero_of_eq_zero_on_spherical`: if `l ≠ 0`, the `θ_i` are unramified and
  `|θ_i(ϖ)|` is non-increasing in `i`, then `l` is non-zero on the vectors fixed by `GL_N(𝒪)`.

Notions from other files:
* `New.blockParahoric`: For a level function b on the indices, the g in GL_N(𝒪) with g_ij in the
  maximal ideal whenever b(j) < b(i).
* `New.IsExponent`: For a character ξ of the torus, the linear form l satisfies l(ρ(t) · mean of x
  over K0) = ξ(t) l(x) for all x and all dominant t.
* `New.heckeCoset`: The Hecke operator of the double coset KgK: the sum of ρ(h) over chosen
  representatives h of the cosets hK in KgK.
* `New.compactMean`: The mean of ρ(h)x over h in a compact subgroup H, for a smooth ρ.

## Relation to the literature

Known result: exponents, U-operators and spherical vectors at pro-p Iwahori level. Here the group is
GL_n at pro-p Iwahori level with tame characters, and eigenforms of the operators U_t on fixed
vectors replace Jacquet modules. No regularity is assumed and ties between roots are allowed.
Source: Casselman, The unramified principal series of p-adic groups I, Compositio 40 (1980), Prop.
2.4, 2.5, 3.6; Haines–Kottwitz–Prasad, Iwahori–Hecke algebras (arXiv math/0309168) §1.



## Orbit sums for a parahoric subgroup

* `New.exists_v_entry_eq_one_of_mem_intGL`: a matrix of `GL_N(𝒪)` and its inverse have unit entries
  in matching positions of a column and a row.
* `New.sum_by_last_nonzero_coord`: the count of residue vectors by their last non-zero coordinate.
* `New.exists_compactMean_and_swap_eq_sum`: vectors whose values under an Iwahori-invariant form are
  explicit sums over the translates of `x` by the swaps `(m j)`.


### `exists_v_entry_eq_one_of_mem_intGL`

 For `k` in `GL_N(𝒪)` there is an index `r` such that the entries `k r m` and `k⁻¹ m r` are both
units. 

### `sum_by_last_nonzero_coord`

 Let `q` be the order of `𝓀[F]`, let indices run over `0, …, N−1`, and let `j(c)` be the last
non-zero coordinate of `c`. The sum of `a (j(c))` over the `c ∈ 𝓀[F]^N` that are non-zero on `I`
with `j(c) ≥ m` equals `∑ q^{j+1} (1 − 1/q)^{|I ∪ {j}|} a j` over the `j ≥ m` that bound `I` from
above. 

### `permGL_swap_mem_blockParahoric_min`

 For `m ≤ j` the permutation matrix of the swap `(m j)` lies in `blockParahoric (min m)`: it
only moves indices from `m` on, which all have the level `m`. 

### `mem_blockParahoric_min_of_mem_update`

 The group of level `update (min m) m N` lies in `blockParahoric (min m)`. 

### `v_apply_lt_one_of_mem_blockParahoric_update`

 An element of the group of level `update (min m) m N` has row `m` in `𝔭` off the diagonal. 

### `reduceParahoric`

 Reduction modulo `𝔭` on `blockParahoric (min m)`, a homomorphism to `GL_N(𝓀[F])`. 

### `residueCol`

 Column `m` of the reduction modulo `𝔭` of an element of `blockParahoric (min m)`. 

### `reduceParahoric_mulVec_residueCol`

 Column `m` of a product: the reduction of `k` times column `m` of the reduction of `p` is column
`m` of the reduction of `k * p`. 

### `apply_eq_of_residueCol_eq`

 Let `x` be fixed by the `p ∈ blockParahoric (min m)` with column `m` in `𝔭` off the diagonal.
Then `ρ u x` depends only on column `m` of `u` modulo `𝔭`. 

### `colVector`

 The vector `ρ p x` at `c = residueCol m p`, and `0` at the `c` that are not of this form. 

### `colVector_residueCol`

 At column `m` of the reduction of `p`, `colVector m x` is `ρ p x`. 

### `exists_mem_blockParahoric_updateCol`

 Let `c` be a column of integers whose entry `c j` is a unit and whose entries below `j` lie in
`𝔭`. The identity matrix with column `j` replaced by `c` lies in the Iwahori subgroup
`blockParahoric (min N)`. 

### `map_colVector_eq_sum`

 Suppose `x` is fixed by every `p` in `blockParahoric (min m)` (entries `p i j` with
`j < min i m` in the maximal ideal) whose column `m` off the diagonal lies in the maximal ideal
(`hx`), and `φ` is invariant under the Iwahori subgroup `blockParahoric (min N)` (`hφ`). For a
residue-field column `c`, `colVector m x c` is `ρ p x` when `c = residueCol m p`, and `0` when `c`
has no such form. Then `φ (colVector m x c)` depends only on the last non-zero coordinate `j` of
`c`: it is `φ (ρ (permGL (swap m j)) x)` if `j ≥ m`, and `0` if `c` vanishes from `m` on. 

### `apply_colVector`

 `blockParahoric (min m)` permutes the vectors `colVector m x c` through its action on the
columns `c`. 

### `apply_sum_colVector`

 Let row `i` of the reduction of `k` be supported in column `a`, for every `a ∈ I`. Then `ρ k`
carries the sum of the `colVector m x c` (`ρ p x` if `c` is column `m` mod `𝔭` of
`p ∈ blockParahoric (min m)`, else `0`) over the `c` that are non-zero on `I` to the sum over the
`c` that are non-zero at `i` (over all `c` if `I` is empty). 

### `exists_compactMean_and_swap_eq_sum`

 Let `F` be a field valued in `ℤᵐ⁰` with compact `𝒪[F]`, `ρ` a smooth representation of
`GL_N(F)`, `φ : ρ →ₗ[ℂ] ℂ`, `m : Fin N`, `P = blockParahoric (min m)` (the `p` in `GL_N(𝒪)` with
`p i j ∈ 𝔭` whenever `j < i` and `j < m`), and `x : ρ` fixed by the `p ∈ P` with column `m` in `𝔭`
off the diagonal, and `φ` invariant under the Iwahori group `blockParahoric (min N)`. For `q` the
order of `𝓀[F]` and `a j = (q - 1) q ^ j φ (ρ (permGL (swap m j)) x)` there are `y` and `z`, `z`
fixed by the `p ∈ P` with row `m` in `𝔭` off the diagonal, with (a) `φ` of the mean of `y` over `P`
equal to `∑_{j ≥ m} a j`; (b) `φ (ρ (permGL (swap m i)) z) = a i + (1 - 1 / q) ∑_{j > i} a j` for
`i ≥ m`. 


## A Hecke operator on eigenvectors of the stabiliser of a line

* `New.Patching.exists_clear_first_row`: one element of `New.proIwahori` clears the first row of a
  matrix in this stabiliser.
* `New.Patching.conj_diagGL_mulSingle_zero_mem_blockParahoric`: if the first row of a matrix of this
  stabiliser is cleared, its conjugate by `diag (ϖ, 1, …, 1)` lies in the stabiliser.
* `New.Patching.parahoricEigenspace_mem_invtSubmodule`: the Hecke operator of `diag (ϖ, 1, …, 1)`
  keeps the `proIwahori`-fixed vectors on which the stabiliser acts through a function of the top
  left entry.


### `exists_clear_first_row`

 One row operation clears the first row: if `g` lies in `blockParahoric (min 1)`, some `u` in
`proIwahori` makes the first row of `u * g` vanish off the corner. 

### `parahoricEigenspace`

 The vectors fixed by the pro-p Iwahori group on which each `k` in the parahoric subgroup of the
level function `f` acts by the scalar `c k`. 

### `conj_diagGL_mulSingle_zero_mem_blockParahoric`

 For a uniformiser `ϖ` and `t = diag (ϖ, 1, …, 1)`: if `m` lies in `blockParahoric (min 1)` and
its first row vanishes off the corner, then `t⁻¹ * m * t` lies in `blockParahoric (min 1)`. 

### `parahoricEigenspace_mem_invtSubmodule`

 For a uniformiser `ϖ` (`v ϖ = exp (-1)`) and `t = diag (ϖ, 1, …, 1)`, the Hecke operator of the
double coset of `t` under `proIwahori` keeps `parahoricEigenspace ρ (min 1) (χ ∘ (· 0 0))`. This
space consists of the `proIwahori`-fixed vectors on which each `k` in the parahoric subgroup of the
level function `min 1` acts by the scalar `χ (k 0 0)`. That parahoric is the `k` in `GL_N(𝒪)` with
`k i 0` in the maximal ideal for `i ≠ 0`. 


## Unramified sorted exponents on spherical vectors

The proof descends from `GL_N(𝒪)` to the Iwahori group through the parahoric groups
`New.blockParahoric (min m)`, using the vectors built in `New.exists_compactMean_and_swap_eq_sum`.


### `New.conj_diagGL_mulSingle_mem_blockParahoric`

 Let `p` lie in the parahoric subgroup `blockParahoric (min m)`, with column `m` in `𝔭` off the
diagonal, and let `b = diag (1, …, ϖ⁻¹, …, 1)` with `ϖ⁻¹` at `m`, for a uniformiser `ϖ`. Then
`b⁻¹ p b` lies in the parahoric subgroup `blockParahoric (update (min m) m N)`, whose row `m` lies
in `𝔭` off the diagonal. 

### `New.IsExponent.apply_swap_diagGL_mulSingle`

 For an exponent `l` of character `torusChar θ`, a vector `z` fixed by the parahoric subgroup
`blockParahoric (update (min m) m N)` and `b = diag (1, …, ϖ⁻¹, …, 1)` with `ϖ⁻¹` at `m`, one has
`l ((m i) b z) = θ_i(ϖ)⁻¹ q ^ (N - 1 - i) l ((m i) z)`. Here `(m i)` is the permutation matrix
`permGL (Equiv.swap m i)` and `q` is the order of the residue field. 

### `New.IsExponent.eq_zero_of_apply_permGL_swap_eq_zero`

 The descent step, for an exponent `(torusChar θ, l)` with `‖θ_i(ϖ)‖` non-increasing in `i`. Let
`l` be Iwahori-invariant and vanish on the averages over the parahoric `P = blockParahoric (min m)`,
and let `x` be fixed by the `p ∈ P` whose column `m` lies in `𝔭` off the diagonal. Write `(m i)` for
the permutation matrix `permGL (Equiv.swap m i)`. If `l ((m i) x) = 0` for all `i ≥ j` (where
`j : Fin (N + 1)`, so that `j = N` asks nothing), then `l x = 0`. 

### `New.IsExponent.eq_zero_of_eq_zero_on_spherical`

 Let `l` be an exponent of the smooth representation `ρ` with character `torusChar θ`. That is,
`l` is `proIwahori`-invariant and `l (ρ t x) = ∏ i, θ i (t i) |t i| ^ (N - 1 - i) · l x` for
`proIwahori`-fixed `x` and dominant diagonal `t`. Assume all `θ i` are trivial on the units of `𝒪`
and `‖θ i ϖ‖` is non-increasing in `i` for the uniformiser `ϖ`. If `l` vanishes on the vectors fixed
by `GL_N(𝒪)`, then `l` is zero: a converse to the fact that spherical representations have a sorted
exponent of unramified characters.

This is a form, in terms of exponents, of one direction of the description of spherical
representations of `GL_N` in the Langlands–Zelevinsky classification: a nonzero sorted unramified
exponent forces a spherical vector. 
