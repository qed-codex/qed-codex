---
{
  "module": "src/Lib/LocalGL/Iwahori/HeckeDegrees.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/HeckeDegrees.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Iwahori/HeckeDegrees.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iwahori degrees, partial Hecke sums and Satake's formula

Let `F` be the completion at `w`, with ring of integers `𝒪`, uniformiser `ϖ` and residue field of
order `q`, and let `K0 = New.proIwahori` be the pro-`p` Iwahori subgroup of `GL_N(𝒪)`. An exponent
is a linear form that is an eigenform for the torus character
`New.torusChar θ = ∏ θ_i(t_i) |t_i| ^ (N - 1 - i)`. This file computes the Hecke operator of a
dominant double coset `K0 t K0` on `K0`-fixed vectors by counting its cosets. It defines partial
Hecke operators as sums over the `g` in `New.basicDoubleCoset` (`ϖ 𝒪^N ⊆ g 𝒪^N ⊆ 𝒪^N`,
colength `j`) whose lattice contains the first `r` basis vectors. A count of hyperplanes over the
residue field relates `r` and `r + 1` and gives Satake's formula for the eigenvalue on an exponent.
It also proves a duality of lattices for these operators.

## Main definitions and results

* `New.heckeFun_iwahoriDoubleCoset_eq_iwahoriDegree_smul`: the operator of a dominant double coset
  `K t K` (`K = proIwahori`) on `K`-fixed vectors, through the number `New.iwahoriDegree t` of its
  cosets.
* `New.partialCosets`, `New.partialHecke`: the lattices that contain the first `r` basis vectors,
  and the sum over them. It is the `j`-th Hecke operator for `r = 0`, and `0` for `r = N`, `0 < j`.
* `New.echelonRows`, `New.card_echelonRows_mem_residueKer`: the rows `(0, …, 0, 1, *, …, *)` over
  the residue field, and how many of them kill a lattice.
* `New.partialHecke_hyperplane_count`: a count of hyperplanes that relates `r` and `r + 1`.
* `New.IsExponent.apply_partialHecke`: Satake's formula for the eigenvalue on an exponent, by
  descent in `r`.

Notions from other files:
* `New.dominantTorus`: The diagonal t with `v (t i) ≤ v (t j)` for i ≤ j.
* `New.blockParahoric`: For a level function b on the indices, the g in GL_N(𝒪) with g_ij in the
  maximal ideal whenever b(j) < b(i).
* `New.IsExponent`: For a character ξ of the torus, the linear form l satisfies l(ρ(t) · mean of x
  over K0) = ξ(t) l(x) for all x and all dominant t.
* `New.heckeCoset`: The Hecke operator of the double coset KgK: the sum of ρ(h) over chosen
  representatives h of the cosets hK in KgK.
* `New.compactMean`: The mean of ρ(h)x over h in a compact subgroup H, for a smooth ρ.

## Relation to the literature

Known; see `Lib.LocalGL.Iwahori.SphericalExponents` for sources.


 ### Double cosets of the pro-`p` Iwahori subgroup 

### `iwahoriDegree`

 The product of `‖t j / t i‖` over the pairs `i < j`. For dominant `t` it is the number of
cosets in `K0 t K0 / K0`, the factor in `New.heckeFun_iwahoriDoubleCoset_eq_iwahoriDegree_smul`. 

### `mul_apply_sub_mul_apply_of_unitriangular`

 Multiplying on the left by an upper unitriangular `u` keeps the difference of the entries
`(i, l)` of two matrices whose columns `l` agree below row `i`. 

### `heckeFun_iwahoriDoubleCoset_eq_card_smul`

 Let `t` be a torus element and `x` be fixed by `K = proIwahori`. If the `r c * t`, for `c` in a
finite type `C` and `r c ∈ K`, represent each coset of `K t K / K` exactly once, then the operator
of the double coset `K t K` sends `x` to `#C` times the mean over `K` of `ρ t x`. 

### `coe_div_mem_integer_of_mem_dominantTorus`

 For dominant `t` and `i ≤ j`, the quotient `t i / t j` is integral. 

### `UnitriangularClasses`

 For dominant `t`, the families `c` of classes `c (i, j)` in `𝒪 / (t i / t j)`, over the pairs
`i < j`. 

### `unitriangularOfClasses`

 The upper unitriangular integral matrix whose entries above the diagonal are representatives of
the classes `c`. 

### `existsUnique_inv_mul_mem_proIwahori`

 Let `t` be dominant, and let `r c ∈ K = proIwahori` have the matrix `unitriangularOfClasses c`
for each family `c` of classes. Then for each `k ∈ K` exactly one `c` has `(k t)⁻¹ (r c t) ∈ K`: the
cosets `r c * t * K` are those of the double coset `K t K`, each once. 

### `heckeFun_iwahoriDoubleCoset_eq_iwahoriDegree_smul`

 Let `K = proIwahori` be the pro-`p` Iwahori subgroup (upper unitriangular modulo the maximal
ideal), `ρ` smooth, and `t` dominant (`v (t i) ≤ v (t j)` for `i ≤ j`). Then for `x` fixed by `K`,
the Hecke operator of the indicator of the double coset `K diag(t) K` sends `x` to `iwahoriDegree t`
times the mean over `K` of `ρ (diag t) x`. Here `iwahoriDegree t` is the product of `‖t j / t i‖`
over `i < j`, the number of cosets in `K t K / K`. 

### `heckeCoset_mulSingle_zero_eq`

 For `N ≥ 1` and a uniformiser `ϖ` (`hϖ`), write `t = (ϖ, 1, …, 1)` and `K0 = proIwahori`.
Then (a) `t` is dominant; (b) on `K0`-fixed vectors the Hecke operator of `K0 t K0` is
`q ^ (N - 1)` times the mean over `K0` of `ρ t`, where `q` is the order of the residue field. 

 ### Lattices that contain the first basis vectors 

### `partialCosets`

 The `g` in `New.basicDoubleCoset` (colength `j`) whose lattice `g 𝒪^N` contains the first `r`
basis vectors, that is, the first `r` columns of `g⁻¹` are integral. 

### `partialHecke`

 The sum of `ρ g` over the cosets `g localIntGL` in `New.partialCosets r j`, one for each such
lattice. 

### `mul_mem_partialCosets_iff`

 `partialCosets m j` is the set of `g` in the basic double coset of colength `j` whose lattice
`g 𝒪^N` contains the first `m` standard basis vectors. This set is (a) invariant under left
multiplication by the parahoric subgroup `blockParahoric (fun i ↦ i + 1 - m)`, whose first block has
size `m` and all others size `1`, and (b) invariant under right multiplication by `GL N (𝒪)`
(`localIntGL`). 

### `partialHecke_zero_eq_heckeGL`

 For `r = 0` the condition on basis vectors is empty, and `New.partialHecke ρ 0 j` is the `j`-th
Hecke operator `New.heckeGL ρ j`. 

### `partialHecke_top_eq_zero`

 No lattice of positive colength contains all `N` basis vectors, so
`New.partialHecke ρ N (j + 1)` is `0`. 

### `inv_mul_mem_partialCosets_iff`

 Dividing row `r` by the uniformiser `ϖ` (`hϖ`): the product lies in `partialCosets (r + 1) j`
iff `g` lies in `partialCosets r (j + 1)` and row `r` of `g` vanishes modulo `ϖ`. 

### `mem_partialCosets_iff_residueKer`

 Let `g` lie in `basicDoubleCoset (Fin N) w j`. The lattice of `g` contains the first `m` basis
vectors iff the rows that kill `g` modulo the maximal ideal vanish at the indices below `m`. 

### `echelonRows`

 The rows `(0, …, 0, 1, *, …, *)` over the residue field, with the entry `1` at the index `r`. 

### `mem_echelonRows`

 The rows of `echelonRows r` are those with entry `1` at `r` and `0` before it. 

### `card_echelonRows`

 There are `q ^ (N - 1 - r)` rows `(0, …, 0, 1, *, …, *)` with the entry `1` at `r`, where `q` is
the order of the residue field. 

### `card_echelonRows_mem_residueKer`

 Let `g` lie in `partialCosets r (j + 1)`: it is in the basic double coset of colength `j + 1`
and its lattice `g 𝒪^N` contains the first `r` standard basis vectors. Consider the rows `u` in
`echelonRows r` over the residue field, which are `(0, …, 0, 1, *, …, *)` with the `1` at index `r`.
The number of such `u` in the kernel of the transpose of `g` reduced modulo the maximal ideal is `0`
if `g` also lies in `partialCosets (r + 1) (j + 1)`, and `q ^ j` otherwise, where `q` is the order
of the residue field. 

### `partialHecke_mem_levelSpace`

 If `x` is fixed by `GL_N(𝒪)` (`hx`), then `partialHecke ρ m j x` is fixed by the parahoric
subgroup whose blocks are given by the level function `i ↦ i + 1 - m` (truncated subtraction). 

### `partialHecke_zero_right`

 Every lattice of colength `0` is `𝒪^N` and contains all basis vectors, so
`partialHecke ρ m 0` fixes a vector `x` fixed by `GL_N(𝒪)`. 

### `sum_echelonRows_indicator_partialCosets_eq`

 Let `b` be diagonal with `ϖ` at `r` and `1` elsewhere, and for each row
`u = (0, …, 0, 1, *, …, *)` let `n u ∈ proIwahori` have row `r` equal to `u` modulo the maximal
ideal. Then the sum over these `u` of the indicator of `partialCosets (r + 1) j` at
`((n u)⁻¹ * b)⁻¹ * g` is `q ^ j` times the indicator of `partialCosets r (j + 1)` minus that of
`partialCosets (r + 1) (j + 1)`, at `g`. 

### `partialHecke_hyperplane_count_of_invariant`

 The count of hyperplanes. Let `ϖ` be a uniformiser (`v ϖ = exp (-1)`), `q = w.q`, `x` a vector
fixed by `GL_N(𝒪_w)` (`localIntGL`), and `T r j = partialHecke ρ r j`, the sum of `ρ g` over the
cosets in `partialCosets r j`. Let `b` be diagonal with `ϖ` at the index `r` (counted from `0`) and
`1` elsewhere, and let the linear map `ψ` be invariant under `ρ k` for every `k` in the pro-`p`
Iwahori subgroup `proIwahori` whose off-diagonal entries vanish outside row `r`. Then
`q ^ (N - 1 - r) ψ (ρ b (T (r + 1) j x)) = ψ (q ^ j (T r (j + 1) x - T (r + 1) (j + 1) x))`. 

 ### The hyperplane count, Satake's formula and the duality of lattices 

### `partialHecke_hyperplane_count`

 The count of hyperplanes of `partialHecke_hyperplane_count_of_invariant`, for `ψ` invariant
under `ρ k⁻¹` whenever `k⁻¹ ∈ proIwahori` and `k` has no off-diagonal entry outside row `r`. Write
`T r j` for `partialHecke ρ r j` and `b` for the diagonal matrix with `ϖ` at `r` and `1` elsewhere:
`q ^ (N - 1 - r) ψ (ρ b (T (r + 1) j x)) = ψ (q ^ j (T r (j + 1) x - T (r + 1) (j + 1) x))`. 

### `IsExponent.apply_partialHecke`

 Satake's formula, in stages. Let `ρ` be a smooth representation of `GL_N` over the completion at
`w`, `ϖ` a uniformiser (`v ϖ = exp (-1)`), `q = w.q`, `x` fixed by `GL_N(𝒪_w)` (`localIntGL`),
`r ≤ N`, and `l` an exponent (`New.IsExponent`) for the torus character `New.torusChar θ`; put
`y i = θ i ϖ`. Then `l (partialHecke ρ r j x)` (the sum of `ρ g` over the cosets in
`partialCosets r j`) is `e_j (y r, …, y (N - 1)) / q ^ (j (j - 1) / 2)` times `l x`, with `e_j` the
elementary symmetric function. The case `r = 0` is Satake's formula for the `j`-th Hecke operator of
`GL_N`. 

### `partialHecke_dual`

 Duality of lattices. Let `ϖ` be a uniformiser, `x` a vector fixed by `GL N (𝒪)`, and
`m + i + j = N`. The operator `partialHecke _ m j` of the representation `g ↦ ρ (gᵀ)⁻¹` sends `x`
to `partialHecke ρ m i x` followed by the diagonal matrix with `m` entries `1` and then `ϖ⁻¹`. 
