---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/FlagDensities.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/FlagDensities.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/FlagDensities.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrals of densities over unitary groups and over the flag variety of `K_ℂ`

We study integrals over unitary groups `G = U(diag ε)` (`New.USign ε`) of functions that are
continuous on invertible matrices and transform under triangular matrices by the modulus character.
Here `New.IsBorelMatrix o b` says that `b` is invertible and upper triangular for the order `o`, `B`
denotes these triangular matrices, `New.diagChar (New.twoRho o _) b = ∏ i, b i i ^ (2ρ) i`, and `o`
is assumed injective. Integrals of such functions over `G` become integrals over an open part of
`U(n)`, and their integral over `U(n)` is invariant under left translation by invertible matrices.
As a consequence, a continuous function on the invertible block diagonal matrices `K_ℂ` that obeys
the same rule block by block has an integral over `K` that is invariant under `K_ℂ`.

## Main definitions and results

* `New.openOrbit`: the set `G B` of products of an element of `G` and a triangular matrix.
* `New.IsFlagDensity`: the transformation rule under triangular matrices.
* `New.integral_mul_left_eq_setIntegral_openOrbit`: the integral over `G` of a translate
  `F (x * g)` equals the integral over the part of `U(n)` in `x G B`.
* `New.integral_unitary_mul_left_of_density`: the integral over `U(n)` of such a function is
  invariant under left translation by an invertible matrix.
* `New.integral_haarK_mul_left_of_density`: the same for densities on `K_ℂ`, integrated over `K`.

Notions from other files:
* `New.USign ε`: the unitary group `U(J)` of the diagonal matrix of signs `J = New.signMatrix ε`.
* `New.twoRho l r`: the sum of the roots selected by `r` that are positive for `l`; its `i`-th entry
  is `#{j | r i j ∧ l j < l i} - #{j | r i j ∧ l i < l j}`.
* `New.lowerLiePart ε 1 o 2⁻¹`: the projection `X ↦ N - J Nᴴ J` to the Lie algebra of `U(J)`, where
  `N` is the part of `X` below the diagonal plus half its diagonal. `New.skewOfReal y` is the
  skew-Hermitian matrix with real coordinates `y`; `New.skewCoords` reads them back (real plus
  imaginary part over `√2` off the diagonal).
* `New.maxCompactU ε`, `New.haarK ε`: the group `K` of the elements of `U(J)` that commute with `J`,
  and its Haar measure of mass one.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Character.FormalDegree` and
`Lib.DiscreteSeries.FlenstedJensen.PsiKTypes` for sources.



## The open orbit of U(p,q) on flags and change of variables

* `New.lintegral_openOrbit_le`: an inequality between integrals over two unitary groups, each
  restricted to a translate of an open orbit.

The inequality holds for any two signatures, so using it both ways gives an equality.


### `openOrbit`

 The set `G B` of matrices `g * b` with `g` in `U(diag ε)` and `b` invertible and upper
triangular for the order `o`: the preimage of an open orbit of `G` on flags. 

### `IsFlagDensity`

 The function `F` on matrices is a density on the flags of the order `o`:
`F (y * b) = |∏ i, b i i ^ (2ρ) i| ^ 2 • F y` for `y` invertible and `b` invertible and upper
triangular for `o`, where `2ρ = twoRho o ⊤`. The matrices `b` are upper triangular in the order of
increasing `o`, so this `2ρ` is minus the sum of the roots of the triangular group. 

### `IsBorelMatrix.unitary_eq_of_mul_eq`

 Uniqueness of the factorisation. Let `o` be injective. If `g * b = g' * c` with `g`, `g'` in
`U(diag ε)`, `b`, `c` triangular and all ratios `c i i / b i i` positive reals, then `g = g'`. 

### `IsBorelMatrix.mul_mul_inv_apply`

 Let `o` be injective and `b` triangular. If `y` vanishes at all entries further below the
diagonal than `(i, j)`, then conjugation by `b` multiplies the entry `(i, j)` of `y` by
`b i i * b⁻¹ j j`. 

### `skewCoords_signMatrix_mul_lowerLiePart_apply`

 Let `o` be injective and `J = diag ε`. The real coordinates (`skewCoords`: real plus imaginary
part, divided by `√2` off the diagonal) of `J * (N - J Nᴴ J)`, where `N` is the part of `Z` below
the diagonal plus half its diagonal, in terms of the entries of `Z` on and below the diagonal. 

### `re_add_im_skewOfReal_div`

 Off the diagonal, the coordinate `y i j` is read off from the entry `(i, j)` of
`skewOfReal y`. 

### `im_sub_re_skewOfReal_swap_div`

 Off the diagonal, the coordinate `y i j` is read off from the entry `(j, i)` of
`skewOfReal y`. 

### `prod_prod_ite_div_eq_prod_zpow_twoRho_sq`

 Let `o` be injective and `d` a vector with nonzero entries. The product over all pairs
`(i, j)` of the ratio of `d` at the later index to `d` at the earlier index is
`(∏ i, d i ^ (2ρ) i) ^ 2`, where `2ρ = twoRho o ⊤`. 

### `abs_det_lowerLiePart`

 The Jacobian. Let `o` be injective, `b` triangular with positive diagonal, `J = diag ε`,
`J' = diag ε'`. Take a skew-Hermitian `Y` (real coordinates `New.skewOfReal`), conjugate `J' * Y` by
`b`, and project to the Lie algebra of `U(J)` by `New.lowerLiePart ε 1 o 2⁻¹`, the map
`X ↦ N - J Nᴴ J` with `N = lowerMask 1 o X` plus half the diagonal of `X`. Then multiply by `J` and
read off coordinates by `New.skewCoords`. The determinant of this real linear map has absolute value
`|∏ i, b i i ^ (2ρ) i| ^ 2`, where `(2ρ) i = #{j | o j < o i} - #{j | o i < o j}`. 

### `exists_mul_isBorelMatrix_of_mem_openOrbit`

 For injective `o`, a point of the open orbit is `g * b` with `g` in `U(diag ε)` and `b`
triangular with positive diagonal. 

### `exists_chart_exp_lowerLiePart_mul_borel`

 A chart at `1` for the factorisation. There is `ψ` with `ψ 1 = 0` and derivative the identity
at `1` such that each matrix `x` near `1` is `exp (L (ψ x)) * b`, where
`L = lowerLiePart ε 1 o 2⁻¹` takes values in the Lie algebra of `U(diag ε)` and `b` is triangular
with positive diagonal. 

### `openOrbit_mem_nhds`

 The set `openOrbit ε o = G B` is a neighbourhood of each of its points. 

### `hasFDerivAt_unitary_factor_of_mem_openOrbit`

 Let `o` be injective and `y = Φ y * B y` for `y` in the open orbit, with `Φ y` in `U(diag ε)`
and `B y` triangular with positive diagonal. Then at each point `y` of the orbit `Φ` has the
derivative `Z ↦ Φ y * L ((Φ y)⁻¹ * Z * (B y)⁻¹)`, where `L = lowerLiePart ε 1 o 2⁻¹`. 

### `abs_det_logDerivU_unitary_factor`

 Let `o` be injective and `y = Φ y * B y` for `y` in the open orbit, with `Φ y` in `U(diag ε)`
and `B y` triangular with positive diagonal. Let `c` map real matrices to `U(diag ε')`, be
differentiable at `y`, and let `x * c y` lie in the orbit. Then the Jacobian of `z ↦ Φ (x * c z)` at
`y` (the absolute value of the determinant of the logarithmic derivative
`logDerivU f y v = (f y)ᴴ * J * f' v` (`J` the sign matrix of the group of `f`, `f'` the derivative
of `f` at `y`) in the real coordinates `skewCoords`) is `|∏ i, b i i ^ (2ρ) i| ^ 2` times that of
`c`, where `b = B (x * c y)` and `2ρ = twoRho o ⊤`. 

### `lintegral_openOrbit_le`

 Change of variables on flags. Let `o` be injective, `B` its triangular group, `x` invertible and
`f` a real density on flags (it scales under `B` by the modulus character). Then the integral of the
positive part of `f` over `x U(ε') ∩ U(ε) B`, for the Haar measure `volume` of `U(ε')` (in Cayley's
chart `cayleyChart`, the density `cayleyDensity / volU (card n)`, as for every signature) moved by
`x`, is at most that over `U(ε) ∩ x U(ε') B`. 

### `mem_openOrbit_one`

 By Gram-Schmidt every invertible matrix is a unitary times a triangular matrix. 


## Integrals of densities over unitary groups

Both directions of the inequality `New.lintegral_openOrbit_le` give an integral formula for complex
valued densities on the flags of `GL n ℂ`.


### `lintegral_mul_left_eq_setLIntegral_openOrbit`

 Let `o` be injective, `B` its triangular group, `f` a real density on flags and `x`
invertible. Then the integral of the positive part of `g ↦ f (x * g)` over `U(ε)` is that of the
positive part of `f` over `U(n) ∩ x U(ε) B`. 

### `integrable_mul_left_of_isFlagDensity`

 Let `o` be injective, `F` a density on flags that is continuous on `GL n ℂ`, and `x`
invertible. Then `g ↦ F (x * g)` is integrable on `U(ε)`. 

### `integral_mul_left_eq_setIntegral_openOrbit`

 Let `o` be injective, `B` its triangular group, `F` a density on flags that is continuous on
`GL n ℂ`, and `x` invertible. Then the integral of `g ↦ F (x * g)` over `U(ε)` is that of `F` over
`U(n) ∩ x U(ε) B`. 

### `integrable_haar_of_isFlagDensity`

 Let `o` be injective and `F` a density on flags that is continuous on `GL n ℂ`. Then `F` is
integrable on `U(diag ε)`. 

### `integral_haar_eq_setIntegral_openOrbit`

 Let `G = U(diag ε)`, let `o` be injective, `B` its triangular group and `F` a density on flags
that is continuous on `GL n ℂ`. Then the integral of `F` over `G` is its integral over the part of
`U(n)` in `openOrbit ε o = G B`. Both groups carry their Haar measure `volume`, which in Cayley's
chart has density `cayleyDensity (signMatrix ε) / volU (card n)`, the same rule for every `ε`. 

### `integral_eq_sub_setIntegral_compl_openOrbit`

 Let `o` be injective and `F` a density on flags that is continuous on `GL n ℂ`. Then `F` is
integrable on `U(diag ε)`, and its integral is the integral over `U(n)` less the integral over the
part of `U(n)` outside `openOrbit ε o`. 

### `integral_unitary_mul_left_of_density`

 Let `o` be injective and `F` a density on flags that is continuous on `GL n ℂ`. Then its
integral over `U(n)` is invariant under left translation by any invertible matrix. 


## Densities on the flag variety of `K_ℂ`

The group `K = maxCompactU ε` is a product of two unitary groups, one for each sign, and the
invariance follows from the case of one unitary group by Fubini's theorem.


### `PosIndex`

 The indices `i` of sign `ε i = 1`. 

### `NegIndex`

 The indices `i` of sign `ε i ≠ 1`, that is `ε i = -1`. 

### `signBlocks`

 The block diagonal matrix with the block `a` on the indices of sign `1` and the block `b` on
the others. 

### `signBlocks_apply`

 The entries of `signBlocks ε a b`: those of `a` or `b` at indices of equal sign, else zero. 

### `signBlocks_mem_blockDiagAlg`

 The matrix `signBlocks ε a b` lies in `blockDiagAlg ε`: its entries vanish at indices of
different sign. 

### `signBlocks_preserves_form`

 A block diagonal matrix with unitary blocks preserves the form `signMatrix ε = diag ε`. 

### `isBorelMatrix_signBlocks`

 A block diagonal matrix is invertible and triangular for the order `o` if both blocks are. 

### `diagChar_signBlocks`

 The product `diagChar w m = ∏ i, m i i ^ w i` of a block diagonal matrix splits over the two
blocks. 

### `exists_eq_signBlocks`

 Every matrix in `blockDiagAlg ε` (entries vanish at indices of different sign) has the form
`signBlocks ε a b`. 

### `continuous_signBlocks`

 A block diagonal matrix depends continuously on its two blocks. 

### `signBlocksHom`

 The homomorphism `U(p) × U(q) → K = maxCompactU ε` that puts two unitary matrices on the
diagonal; `p` and `q` count the indices of sign `1` and `-1`. 

### `signBlocksHom_surjective`

 Every element of `K = maxCompactU ε` is block diagonal with unitary blocks. 

### `measurePreserving_signBlocksHom`

 The map `U(p) × U(q) → K = maxCompactU ε`, `(a, b) ↦ signBlocks ε a b`, carries the product of
the Haar measures of mass one to the Haar measure `haarK ε` of mass one. 

### `integral_haarK_eq_integral_signBlocksHom`

 Fubini's theorem on `K = maxCompactU ε ≃ U(p) × U(q)`: the integral of a continuous function
over `K` is the double integral over the unitary blocks. 

### `twoRho_subtype`

 Let `p` select the indices of one sign. On these indices `-2 ρ_c`, minus the sum of the compact
roots (those `e i - e j` with `ε i = ε j`) positive for `l`, is the sum `2 ρ` of all roots of the
block positive for `-l`. 

### `integral_haarK_mul_left_of_density`

 Let `K_ℂ` be the group of invertible matrices in `blockDiagAlg ε` (entries vanish at indices of
different sign), let `K = maxCompactU ε` be its unitary subgroup with Haar measure `haarK ε`, and
let `l` have distinct entries. Let `B_K` be the subgroup of `K_ℂ` of matrices upper triangular in
the order of decreasing `l`, and let `2 ρ_c` be the sum of the compact roots (those `e i - e j` with
`ε i = ε j`) positive for `l`. If `F` is continuous on `K_ℂ` and
`F (y * b) = |∏ i, b i i ^ (-2 ρ_c) i| ^ 2 * F y` for `y` in `K_ℂ` and `b` in `B_K`, then the
integral of `F (x * k)` over `K` equals that of `F k`, for all `x` in `K_ℂ`.

Classically this invariance follows from the Iwasawa decomposition `K_ℂ = K B_K` and the form
`dk d_r b` of the Haar measure of `K_ℂ`; here the invariance is proved block by block, by Fubini's
theorem and `integral_unitary_mul_left_of_density`, without using the Haar measure of `K_ℂ`. 
