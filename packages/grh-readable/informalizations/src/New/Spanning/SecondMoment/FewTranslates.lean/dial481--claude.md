---
{
  "module": "src/New/Spanning/SecondMoment/FewTranslates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Few translates fill

Let a finite group act unitarily on `T`, let `pr₀` be the projection onto a stable subspace `T₀`,
and let `B : S → T` be linear. Suppose that `pr₀ B` is almost an isometry from below in mean square
and that the second moment of the operators `B* s B` is nearly as small as Cauchy–Schwarz allows.
Then a few translates `s pr₀ B` span almost all of `T₀`. In this file `‖A‖`, written of a linear map
`A`, is its Hilbert–Schmidt norm.

* `New.hilbertSchmidtNorm`, `New.IsNearIsometry`: the Hilbert–Schmidt norm, and the first
  hypothesis.
* `New.isSpread_of_second_moment`: for any subspace `W` of `T₀`, the preimage of `W` under some
  translate `s pr₀ B` is small, in terms of the share of `W` in `T₀` (`New.IsSpread`).
* `New.IsSpread.exists_few_le_finrank_iSup_range`: a logarithm times `dim T₀ / dim S` translates
  span almost all of `T₀`.

## Relation to the literature

Rank bounds from second moments: Welch 1974. Greedy covering with a logarithmic loss: Wolsey, Greedy
algorithm for the submodular set covering problem, 1982.


### `IsSpread`

 The maps `B s` spread: for every subspace `F` of `W`, with share `α` of the dimension, the
preimage of `F` under one of them has dimension at most `((1 + α) / 2 + η) dim V`. The share is the
quotient of the two values of `finrank`, so it is `0` if `finrank W = 0`. 

### `hilbertSchmidtVector`

 The values of a linear map on an orthonormal basis of the source, as one vector of a Hilbert
space. Its inner product is the Hilbert–Schmidt inner product of maps. 

### `hilbertSchmidtNorm`

 The Hilbert–Schmidt norm of a linear map. 

### `inner_hilbertSchmidtVector`

 The inner product of `hilbertSchmidtVector A` and `hilbertSchmidtVector B`, the vectors of the
values of `A` and `B` on an orthonormal basis, is the trace of `A* B`: the Hilbert–Schmidt inner
product. 

### `hilbertSchmidtNorm_sq_eq_sum`

 The squared Hilbert–Schmidt norm of `A` is the sum of `‖A (b i)‖ ^ 2` over the vectors `b i` of
any orthonormal basis `b` of `S`. 

### `hilbertSchmidtNorm_sq_eq_sum_entries`

 The squared Hilbert–Schmidt norm is the sum of the squared moduli of the matrix entries. 

### `hilbertSchmidtNorm_le_of_norm_le`

 If `‖A x‖ ≤ ‖B x‖` for all `x`, then the Hilbert–Schmidt norm of `A` is at most that of `B`. 

### `orthoProj`

 The orthogonal projection onto a subspace, as the linear map under `starProjection`. 

### `hilbertSchmidtNorm_orthoProj_sq`

 The squared Hilbert–Schmidt norm of the orthogonal projection onto `U` is `dim U`. 

### `hilbertSchmidtNorm_orthoProj_comp_sq`

 The squared Hilbert–Schmidt norm of `pr_W A` is the real part of the inner product of
`pr_W` with `A A*`, where `hilbertSchmidtVector` carries the Hilbert–Schmidt inner product of
maps. 

### `IsNearIsometry`

 `A` is almost an isometry from below in mean square, with the error `ε`: on every subspace `U`
its squared Hilbert–Schmidt norm `‖A pr_U‖²` is at least `dim U - ε dim S`. 

### `isNearIsometry_of_hilbertSchmidtNorm_le`

 If the squared Hilbert–Schmidt norm of `A* A - 1` is at most `ε² dim S`, then
`IsNearIsometry A ε`: on every subspace `U` the squared Hilbert–Schmidt norm of `A` is at least
`dim U - ε dim S`. 

### `IsNearIsometry.mono`

 A near isometry with the error `ε` is one with any larger error. 

### `IsNearIsometry.finrank_range_pos`

 Let `pr₀` be any endomorphism. If `pr₀ B` is almost an isometry from below in mean square, with
an error `ε` below `1`, and the source `S` is not zero, then the range of `pr₀` is not zero. 

### `norm_sq_eq_add_of_isSymmetricProjection`

 An orthogonal projection `pr` splits `y` orthogonally: `‖y‖² = ‖pr y‖² + ‖(1 - pr) y‖²`. 

### `hilbertSchmidtNorm_one_sub_mul_comp_sq_le`

 For an orthogonal projection `p` and any `q`: in squared Hilbert–Schmidt norm, the part
`(1 - p q) A` that `p q` misses is at most the sum of the parts that `p` and `q` miss. 

### `IsNearIsometry.proj_comp`

 Let `IsNearIsometry A ε`: `dim U - ε dim S ≤ ‖A pr_U‖²` in Hilbert–Schmidt norm for all
subspaces `U`. If an orthogonal projection `pr` misses at most `δ dim S` of the squared norm of
`A`, then `IsNearIsometry (pr A) (ε + δ)`. 

### `inner_hilbertSchmidtVector_translate`

 Let `ρ` be a unitary representation of `Γ` on `T`. The vector `hilbertSchmidtVector X` lists the
values of a map `X` on an orthonormal basis, so `⟪hilbertSchmidtVector X, hilbertSchmidtVector Y⟫`
is the Hilbert–Schmidt inner product `tr (X* Y)`. This product of `s B B* s⁻¹` and `t B B* t⁻¹` is
the squared Hilbert–Schmidt norm of `B* s⁻¹ t B`. So `s ↦ ‖B* s B‖²` has positive type in this
norm. 

### `sq_sum_hilbertSchmidtNorm_orthoProj_comp_le`

 Cauchy–Schwarz for the projection onto `W` and the sum of the operators `s B B* s⁻¹`, where
`s` runs through a finite group that acts unitarily: the sum of the squared Hilbert–Schmidt norms
`‖pr_W s B‖²` has square at most `dim W` times the order of the group times the sum of
`‖B* s B‖²`. 

### `isSpread_of_second_moment`

 **One translate.** Let a finite group `Γ` act unitarily on `T` by `ρ`, and let `pr₀` be the
orthogonal projection onto a stable subspace `T₀`, so that `pr₀ s = s pr₀`. Suppose that `pr₀ B` is
almost an isometry in mean square with the error `ε`, and that `dim T₀` times the mean of
`‖B* s B‖²` is at most `(1 + ε) (dim S)²`. Then the maps `pr₀ s B` spread (`IsSpread`): for every
subspace `W` of `T₀`, of dimension `α dim T₀`, the preimage of `W` under some `pr₀ s B` has
dimension at most `(1 + α + 3 ε) / 2 · dim S`. 

### `finrank_sup_range_add_finrank_comap`

 The image of `A` adds `dim V - dim A⁻¹ F` dimensions to `F`. 

### `IsSpread.exists_codim_le`

 One step of the greedy choice. Let `W` be nonzero and suppose that the maps `B s` spread with
the error `3 ε / 2`. If `F` misses more than a share `16 ε` of the dimensions of `W`, then adding
some image `range (B s)` to `F` multiplies the codimension by at most `1 - 2 dim V / (5 dim W)`. 

### `IsSpread.exists_codim_le_max`

 The greedy choice after `l` steps. Let `W` be nonzero and let the maps `B s : V → W` spread with
the error `3 ε / 2`. Then the span of the images of at most `l` of them misses at most a share
`max (16 ε) (exp (-l rate))` of the dimensions of `W`, where `rate = 2 dim V / (5 dim W)`: each step
removes at least that share of what is missing. 

### `IsSpread.exists_few_le_finrank_iSup_range`

 **Few maps span almost everything.** Let `V` and `W` be nonzero finite-dimensional spaces, let
`0 < ε < 1 / 16`, and let the maps `B s : V → W` spread with the error `3 ε / 2`. Then the images of
at most `(5/2) (1 + log (1 / (16 ε))) dim W / dim V` of them span a subspace of dimension at least
`(1 - 16 ε) dim W`. 

### `finrank_biSup_map_le`

 The images of a subspace `C` under `#t` maps span at most `#t dim C` dimensions. 

### `finrank_biSup_range_le`

 Restricting finitely many maps to a subspace `U` lowers the dimension of the span of their
images by at most the codimension of `U` for each map. 
