---
{
  "module": "src/New/OneLift/FalseLifts/BottomOfTower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The bottom of the tower: from the block datum to all data

Let `O` be a descent pair with spaces `W` and `V`, and let `y` be a form on `V` whose descents to
`W` by the data `v_P ⊗ Ψ_bl ⊗ vac` vanish, where `v_P` is the Fock vector of a polynomial `P` and
`Ψ_bl` is the block datum. Suppose that the characters `χ_w` at the places of `Q` are not trivial
and that the hyperplane sums at the chosen places annihilate `y`. This file proves that the descents
vanish for all data that are the vacuum at the finite places other than the chosen places, the
places of `Q` and their conjugates (`DescentPair.descentsVanish_of_hyperplaneSumsAnnihilate`). By
the descents of `y` we mean those of the matrix coefficient of `y` for a fixed linear form `u`.

It suffices to treat the indicator of a small class around each point `x`. If `x` has an integral
block ratio (`HasIntegralBlockRatio`) at every place of `O`, the mean of the translates of this
indicator under the level group is a multiple of a translate of `Ψ_bl` under `U(W)`. Otherwise an
annihilating row at a place where `x` has no integral block ratio gives integral elements `h_v`
(`rowShear`) that fix the components of `x` at the places of `O` and whose sum annihilates `y`.
Classes are taken modulo `i!` (`factorialIdele`) for large `i`, and the mean is taken over the
finitely many translates under the whole level group.

The pair `O` carries two families of split finite places, the chosen places and the places of `Q`,
indexed by `O.ChosenIndex` and `O.TwistIndex`. The family `O.placeAt` lists all these places, and
`O.places` is their set. The pair also carries the space `W = O.W` of rank `r`, an embedding
`O.incl : r ↪ n` and the residue characters `χ_w = O.tamePart w`. The space `V` is `stdSpace E n`,
and `O.FormV` are the forms on `V` of the level of `O`. The level group `O.levelGroup` consists of
the elements of the maximal level whose reductions fix `(1, 0)ᵀ` at the chosen places and are block
lower triangular at the places of `Q`. For an `n × r` matrix `x` we write `x'` for the square block
of the rows `O.incl` and `x''` for the block of the other rows.

The field `E` is CM and carries Weil data (`WeilData E`): a purely imaginary element, a finite idele
and a splitting character, from which the Weil representation is defined.

Notions from other files:
* `New.Space.lift` for the swapped kernel goes from `U(V)` to `U(W)`; the descent of `y` is the
  conjugate of this lift of the conjugate of `y`.
* `New.Space.schrodingerOp`: for a set `S` of split places, `schrodingerOp V S Ψ f` is the vector of
  the Weil representation with the function `Ψ` of finite adelic vectors above `S` and `f`
  elsewhere; `New.Space.integrated` sets the component at infinity, and `New.Space.vacElem` is the
  vacuum.
* `New.cosetIndicator`: `cosetIndicator S t z` is the indicator function of the `x` such that
  `t⁻¹ (x - z)` is integral at every place of `S`.
* `New.DescentPair.blockDatum` is the vector `Ψ_bl ⊗ vac`. The function `Ψ_bl` of a finite adelic
  `n × r` matrix `x` is `∏_{w ∈ Q} χ_w(det x' mod w)` if `x` is integral at all places of `O` and
  `≡ (1, 0)ᵀ` (`New.inclMatrix`) at the chosen places, and `0` otherwise.
* `New.DescentPair.formAction` is the action `s̄ y` on forms of the product of the groups `GL r`
  over the residue fields of the chosen places.


### `submatrix_inclMatrix`

 The rows `ι` of the matrix `inclMatrix R ι = (1, 0)ᵀ` form the identity matrix. 

### `inclMatrix_mulVec_apply_embedding`

 The vector `inclMatrix R ι *ᵥ μ = (μ, 0)` has the entry `μ b` at the index `ι b`. 

### `inclMatrix_mulVec_vecMul`

 The row `inclMatrix R ι *ᵥ μ`, which is `μ` at the indices `ι` and `0` elsewhere, times `x`
equals `μ` times the rows `ι` of `x`, that is, `μ ᵥ* x.submatrix ι id`. 

### `completeColumns`

 The square matrix `(u' 0; u'' 1)`: its columns `ι` are the columns of `u`, and its other columns
are those of the identity matrix. 

### `completeColumns_mul_inclMatrix`

 The columns `ι` of `(u' 0; u'' 1)` are the columns of `u`. 

### `det_completeColumns`

 The determinant of `completeColumns ι u = (u' 0; u'' 1)` is that of `u' = u.submatrix ι id`, the
block of the rows `ι` of `u`. 

### `completeColumns_apply_of_notMem`

 The upper right block of `completeColumns ι u = (u' 0; u'' 1)` is zero: its entry at row `ι a`
and column `b` outside the range of `ι` is `0`. 

### `rowShear`

 The matrix `h_v = (1 + v λ, v λ'; 0, 1)` of a column `v` and a row `l = (λ, λ')`, where `λ` has
the entries of `l` indexed by `ι` and `λ'` has the other entries. 

### `rowShear_mul_inclMatrix`

 The matrix `rowShear ι v l` is block upper triangular with first block `1 + v λ`, where
`λ = l ∘ ι`. 

### `transpose_rowShear_mul_inclMatrix`

 The matrix `rowShear ι v l` is `1 + (v, 0)ᵀ l`, the identity plus the product of the column `v`,
extended by zero along `ι`, with the row `l`. If `l` vanishes outside the range of `ι`, it is block
lower triangular with first block `1 + v λ`, where `λ = l ∘ ι` and `inclMatrix R ι = (1, 0)ᵀ`. 

### `det_rowShear`

 The determinant of `rowShear ι v l` is that of its first block `1 + v λ`, where `λ = l ∘ ι`. 

### `submatrix_eq_of_transpose_mul_inclMatrix`

 If `tᵀ e = e sᵀ` for `e = inclMatrix R ι = (1, 0)ᵀ`, the first block of `t` is `s`. 

### `apply_eq_zero_of_transpose_mul_inclMatrix`

 If `tᵀ e = e sᵀ` for `e = inclMatrix R ι = (1, 0)ᵀ`, the upper right block of `t` is zero. 

### `hyperplaneGroup`

 The group of the invertible matrices `1 + v λ`, for a given row `λ = l` and all columns `v`. 

### `instance [Finite k] (l : r → k) : Fintype (hyperplaneGroup l)`

 Over a finite field the group of the invertible `1 + v λ` is finite. 

### `sum_inv_det_hyperplaneGroup_eq_zero`

 If the row `λ = l` is not zero and `χ ≠ 1`, the sum of `χ(det s)⁻¹` over the invertible matrices
`s = 1 + v λ` is zero. 

### `coeff_hyperplaneSum_eq_ite`

 The hyperplane sum `hyperplaneSum χ l` has the coefficient `χ(det s)⁻¹` at the invertible
matrices `s = 1 + v λ` for the row `λ = l`, and `0` elsewhere. 

### `hyperplaneSum_zero`

 The hyperplane sum `∑ χ(det s)⁻¹ s` over the invertible `s = 1 + v λ` is `1` for the zero row
`λ = 0`. 

### `asAlgebraHom_hyperplaneSum`

 In a representation `σ`, the hyperplane sum of a row `λ = l` acts as `∑ χ(det s)⁻¹ σ(s)` over
the invertible matrices `s = 1 + v λ`. 

### `HasIntegralBlockRatio`

 Let `x'` be the square block of the rows `ι` of `x`, and `x''` the block of the other rows. The
matrix `x` has an integral block ratio if `x'` is invertible and `x'' x'⁻¹` is integral, and also
`≡ 0` modulo `w` if the proposition `chosen` holds. In the applications `chosen` says that `w` is a
chosen place. Here `v` is the valuation at `w`. 

### `HasIntegralBlockRatio.isUnit_det`

 The block `x'` is invertible. 

### `HasIntegralBlockRatio.valuation_le_one`

 The matrix `x'' x'⁻¹` is integral. 

### `HasIntegralBlockRatio.valuation_lt_one`

 At a chosen place `x'' x'⁻¹` is `≡ 0` modulo `w`. 

### `IsAnnihilatingRow`

 An integral row `l = (λ, λ')` with `λ x' + λ' x'' = 0`, with `λ ≢ 0` modulo `w`, and with
`λ' ≡ 0` modulo `w` unless `chosen` holds. Here `λ` and `x'` are the entries of `l` and the rows of
`x` indexed by `ι`, and `λ'` and `x''` are the others. 

### `IsAnnihilatingRow.vecMul_eq_zero`

 The row annihilates `x`. 

### `IsAnnihilatingRow.residue_ne_zero`

 The part `λ` of the row is not zero modulo `w`. 

### `IsAnnihilatingRow.residue_eq_zero`

 At a place that is not chosen the part `λ'` of the row is zero modulo `w`. 

### `exists_isAnnihilatingRow_of_max`

 Let a row `μ` annihilate `x` and have a nonzero entry of largest modulus at an index `ι b`,
strictly larger than the entries outside `ι` unless `chosen` holds; the modulus is the valuation
`v` at `w`. Dividing `μ` by this entry gives an annihilating row: an integral row `l` with
`l x = 0`, nonzero modulo `w` on `ι`, and zero modulo `w` outside `ι` unless `chosen` holds. 

### `exists_isAnnihilatingRow_of_det_eq_zero`

 If the block `x'` of the rows `ι` of `x` is singular, then `x` has an annihilating row: an
integral row `l` with `l x = 0`, nonzero modulo `w` on `ι`, and zero modulo `w` outside `ι` unless
`chosen` holds. 

### `exists_isAnnihilatingRow_of_one_le`

 Let the block `x'` of the rows `ι` of `x` be invertible, and let `x x'⁻¹` have, in a row `a`
outside `ι`, an entry of valuation `v ≥ 1` at `w`, and `v > 1` unless `chosen` holds. Then `x` has
an annihilating row: an integral row `l` with `l x = 0`, nonzero modulo `w` on `ι`, and zero modulo
`w` outside `ι` unless `chosen` holds. 

### `exists_isAnnihilatingRow_of_not_hasIntegralBlockRatio`

 **Points without an integral block ratio.** If `x` has no integral block ratio, there is an
integral row `(λ, λ')` with `λ x' + λ' x'' = 0`, `λ ≢ 0` modulo `w`, and `λ' ≡ 0` modulo `w` unless
`chosen` holds. 

### `mem_of_nested_cosets`

 Let `U 0 ≥ U 1 ≥ …` be subgroups, so that two cosets `x + U i` are nested or disjoint. A
function that is constant on finitely many such cosets `x + U (i x)`, `x ∈ F`, and vanishes off
their union lies in every subspace `P` that contains their indicators. 

### `exists_fixed_forall_linearMap_eq_of_finite`

 Let a vector `f` have finitely many translates under a group `J`. There is a vector `f₁`, the
mean of these translates, that is invariant under `J` and such that `L f₁ = c` for every linear form
`L` with the constant value `c` on the translates. 

### `factorialIdele`

 The finite idele `i!`. The quotient of each of these ideles by the one before is integral, and
they tend to `0` at every finite place, like the powers of a uniformiser at one place. 

### `factorialBox`

 The finite adelic vectors `x` that are `≡ 0` modulo `i!` at the places of `S`, that is, such
that `(i!)⁻¹ x` lies in `integralBox m S`, the vectors integral at these places. 

### `mem_factorialBox`

 A vector `x` is `≡ 0` modulo `i!` at `S` if and only if `(i!)⁻¹ x` lies in `integralBox m S`,
the group of the vectors that are integral at every place of `S`. 

### `mem_factorialBox_iff_exists`

 A vector is `≡ 0` modulo `i!` at `S` if and only if its part at `S` is `i!` times an element of
`stdLattice E m`, the vectors that are integral at every finite place; `idem S` is the adele that is
`1` at the places of `S` and `0` elsewhere. 

### `cosetIndicator_factorialIdele`

 The function `cosetIndicator S (i!) x` is the indicator of the class of `x` modulo `i!` at the
places of `S`. 

### `isLocallyConstant_cosetIndicator_factorialIdele`

 The indicator of the class of `q` modulo `i!` at the places of `S` depends on `q` in a locally
constant way. 

### `antitone_factorialBox`

 For `i ≤ j`, a vector that is `≡ 0` modulo `j!` at the places of `S` is `≡ 0` modulo `i!`. 

### `eventually_const`

 Let `Ψ` be a Schwartz–Bruhat function of the components at `S`. For large `i` it is constant on
the class `x + factorialBox m S i` of `x` modulo `i!` at the places of `S`. 

### `mem_of_eventually_coset`

 Let `P` be a subspace of functions. If for each point `x` the indicator of the class of `x`
modulo the idele `i!` at the places of `S` lies in `P` for large `i`, then `P` contains every
Schwartz–Bruhat function `Ψ` of the components at `S`. 

### `matrixAt`

 The component at `w` of a finite adelic `n × r` matrix. 

### `matrixAt_mul`

 The component of `x A` at `w` is the product of the components of `x` and `A`. 

### `matrixAt_inclMatrix_mul`

 The component of `(1, 0)ᵀ A` at `w` is `(1, 0)ᵀ` times the component of `A`; the rows `ι` carry
the identity block. 

### `leftMul`

 The action `x ↦ h x` of the finite adelic points of `U(V)` on finite adelic `n × r` matrices. 

### `matrixAt_leftMul`

 The component of `h x` at `w` is the product of the components of `h` and `x`. 

### `leftMul_mem_integralBox_iff`

 An element `k` of the maximal level preserves the matrices that are integral at `S`. 

### `cosetIndicator_leftMul_inv`

 For `k` in the maximal level `stdLevel E n`, the indicator `cosetIndicator S t z` of the class
of `z` modulo `t` at the places of `S`, evaluated at `k⁻¹ x`, equals `cosetIndicator S t (k z)`
evaluated at `x`. 

### `cosetIndicator_leftMul_inv_of_fixed`

 An element `k` of the maximal level that fixes the components of `z` at `S` preserves the class
of `z` modulo the idele `t` at the places of `S`. 

### `exists_atPlace_eq`

 Let `O` be a descent pair, with two families of split finite places: the chosen places, indexed
by `O.ChosenIndex`, and the places of a second set `Q`, indexed by `O.TwistIndex`. Invertible
matrices `g j` at these places are the components of a finite adelic point `k` of the unitary group
that is `1` away from them and their conjugates. 

### `exists_stdLevel_atPlace_eq`

 Matrices `τ j` that are invertible over the local integers at the places `O.placeAt j` of `O`
are the components of an element of the maximal level `stdLevel E n`. 

### `mem_levelGroup_of_reduceAt`

 An element `k` of the maximal level `stdLevel E n` lies in `O.levelGroup` if its reductions fix
`inclMatrix O.incl = (1, 0)ᵀ` at the chosen places `O.placeAt (.inl i)`, and at the places
`O.placeAt (.inr i)` of `Q` have zero entries in rows `O.incl` outside the columns `O.incl`. 

### `translatedBlockFn`

 The function `Ψ_bl(· A)`: the block datum of `O` as a function of an adelic `n × r` matrix,
translated on the right by `A`. 

### `isSchwartzBruhat_residueDatum_residueBlockDatum`

 The function `residueDatum O.placeAt O.residueBlockDatum`, the block datum Ψ_bl read on finite
adelic matrices through their reductions at the places `O.placeAt`, is Schwartz–Bruhat above
`O.places`. 

### `residueBlockDatum_mul`

 The function `Ψ = O.residueBlockDatum` of families `X` of residue matrices is
`∏_{w ∈ Q} χ_w(det X_w')` if `X_w = (1, 0)ᵀ` at all chosen places, and `0` otherwise. Let `τ` lie in
`descentResidueLevel`: it fixes `(1, 0)ᵀ` at the chosen places and is block lower triangular at `Q`.
Then `Ψ(τ X) = c Ψ(X)`, where `c` is the conjugate of
`O.residueLevelChar τ = ∏_{w ∈ Q} χ_w(det τ_w')⁻¹`, with `τ_w'` the block of `τ_w` of the rows and
columns `O.incl`. 

### `residueDatum_of_eq_map`

 Suppose the component of the adelic matrix `x` at each `O.placeAt j` is a matrix `Z j` over the
local integers. Let `f` be a function of families of residue matrices. Then
`residueDatum O.placeAt f`, which reads `f` on the reductions of a matrix integral at these places,
takes at `x` the value of `f` at the reductions of the `Z j`. 

### `idem_smul_eq_of_matrixAt_eq`

 Two matrices with the same components at the places of `O` have the same product with the adele
`idem O.places`, which is `1` at these places and `0` elsewhere. 

### `exists_eq_map_of_mem_integralBox`

 The components of a matrix that is integral at the places of `O` are integral matrices. 

### `residueDatum_of_notMem`

 The function `residueDatum O.placeAt f` vanishes at a matrix `x` that is not integral at some
place of `O`. 

### `translatedBlockFn_leftMul`

 Let `Ψ = O.translatedBlockFn A`, that is `Ψ(x) = Ψ_bl(x A)`. For `h` in `O.levelGroup` we have
`Ψ(h x) = c Ψ(x)`, where `leftMul` is the action `x ↦ h x` and `c` is the conjugate of
`O.levelChar h = ∏_{w ∈ Q} χ_w(det h')⁻¹`, with `h'` the block of the rows and columns `O.incl` of
the reduction of `h` at `w`. 

### `exists_leftMul_eq_of_translatedBlockFn_ne_zero`

 If the block datum of `O`, translated on the right by `A` (`translatedBlockFn`), is nonzero at
the finite adelic `n × r` matrix `x`, then at the places of `O` the matrix `x` equals `h ι A⁻¹` for
some `h` in the level group of `O`. Here `ι` is the inclusion matrix of `O.incl`, and
multiplication by `idem O.places` keeps only the components at the places of `O`. 

### `levelTranslate`

 The translation `Ψ ↦ c Ψ(h⁻¹ ·)` by an element `h` of the level group of `O`, where `c` is the
conjugate of the level character `O.levelChar h`: the product over the places `w ∈ Q` of
`χ_w(det h_w')⁻¹`, for the first diagonal block `h_w'` of the reduction of `h` at `w`. 

### `finite_range_levelTranslate`

 The indicator of the class of `z` modulo `i!` at the places of `O` has finitely many translates
under the level group. 

### `eq_smul_translatedBlockFn`

 Let `Ψ₀ = O.translatedBlockFn A = Ψ_bl(· A)` be the block datum of the descent pair `O`,
translated on the right by `A`. Let the function `Ψ` of finite adelic `n × r` matrices depend only
on the components at the places of `O` and vanish wherever `Ψ₀` does. Let it be fixed by the twisted
translations `O.levelTranslate h : Ψ ↦ c Ψ(h⁻¹ ·)` for `h` in the level group, where `c` is the
conjugate of the level character `O.levelChar h`. If `Ψ₀ z = 1`, then `Ψ = Ψ z • Ψ₀`. 

### `translatedBlockFn_eq_one_of_hasIntegralBlockRatio`

 Let `z'` be the block of the rows `O.incl` of `z` and `z''` the block of the other rows. Let `z`
have an integral block ratio at every place of `O`: there `z'` is invertible and `z'' z'⁻¹` is
integral, and `≡ 0` at the chosen places (`j.isLeft`). If `A` has the components `z'⁻¹` at the
places of `O`, then the block datum takes the value `1` at `z A`, whose components there are
`(1, z'' z'⁻¹)ᵀ`. 

### `smul_chosenGLRep_eq_apply_of_triangular`

 Let `π` be a representation of `Gf E n`, the unitary group in `n` variables over the finite
adeles, and `y` a vector on which the group `O.levelGroup` acts by `O.levelChar`. Let `k` be in the
maximal level `stdLevel E n`, and let its reductions `τ_w` at the places of `O` be block triangular
with first block `s_w`: with `e = (1, 0)ᵀ = inclMatrix _ O.incl`, they are upper triangular at the
chosen places, `τ_w e = e s_w`, and lower triangular at `Q`, `τ_wᵀ e = e s_wᵀ`. Then
`π(k) y = χ(s)⁻¹ s̄ y`. Here the product `χ(s) = ∏ χ_w(det s_w)` is over both families, and `s̄` is
the part of `s` at the chosen places, which `O.chosenGLRep π` lets act by `∏ χ_w(det s_w)` times `π`
of a lift of `diag(s_w, 1)`. 

### `isAutomorphic_star_algFormCoeff`

 The complex conjugate of the matrix coefficient `algFormCoeff 1 u y` of a form `y` on `V`, for a
linear functional `u` on the weight space, is automorphic on `U(V)`. 

### `descentPairing`

 The conjugate of the value at `g` of the descent of the matrix coefficient `u` of a form `y` by
the datum `v_P ⊗ Ψ ⊗ vac`, where `v_P` is the Fock vector of the polynomial `P`. It is linear in
`Ψ` and conjugate linear in `y`; below it is written `B(Ψ, y)`. 

### `descentPairing_apply`

 The pairing `B(Ψ, y)` is the value at `g` of the theta lift from `U(V)` to `U(W)`, with datum
`v_P ⊗ Ψ ⊗ vac`, of the conjugate of the matrix coefficient `u` of `y`. 

### `BlockDescentVanishes`

 The descent to `W` of the matrix coefficient `u` of the form `y` by the datum
`v_P ⊗ Ψ_bl ⊗ vac` vanishes, where `Ψ_bl ⊗ vac` is the block datum `O.blockDatum`. 

### `isConjDisjoint_places`

 No place of the descent pair `O` is the conjugate of itself or of another place of `O`. 

### `descentPairing_translate`

 Let `O` be a descent pair with spaces `W` and `V`, and `O.FormV` the forms on `V` of weight
`(O.columnCount, O.detExp)` and of the level of `O`. For a linear functional `u` on the values of
these forms, a polynomial `P` and an adelic point `g` of `U(W)`, let
`B(Ψ, y) = descentPairing u P g Ψ y`. It is the conjugate of the value at `g` of the descent of the
matrix coefficient `u` of `y` by a datum: the Fock vector of `P` at infinity, `Ψ` at the places
`O.places`, and the vacuum elsewhere. Let `k` be in the maximal level `stdLevel E n`, let `Ψ` be
Schwartz–Bruhat at `O.places`, and let `y'` be the right translate of `y` by `k` (the action
`algFormRep`). Then `B(Ψ(k⁻¹ ·), y') = B(Ψ, y)`. 

### `descentPairing_levelTranslate`

 The rule `B(c Ψ(h⁻¹ ·), y) = B(Ψ, y)` for the pairing `B = descentPairing u P g` and `h` in the
level group. Here `c` is the conjugate of the level character at `h`, and `O.levelTranslate h Ψ` is
the function `c Ψ(h⁻¹ ·)`. 

### `blockDatum_val`

 The block datum `O.blockDatum` is the vector `Ψ_bl ⊗ vac` with the function
`Ψ_bl = residueDatum O.placeAt O.residueBlockDatum` at the places of `O` and the vacuum
elsewhere. 

### `exists_pairWeil_blockDatum_eq_smul`

 Let `O` be a descent pair, `W = O.W` its hermitian space of rank `r` and `V = stdSpace E n` the
standard space of rank `n`. The group `U(W) × U(V)` acts by the Weil representation `pairWeil`,
twisted by the character `O.charW` of `U(1)`, on data on `Hom(W, V)`; the argument `((1, A), 1, 1)`
is the finite adelic point `A` of `U(W)`. The block datum `O.blockDatum` is `Ψ_bl ⊗ vac`, that is
`schrodingerOp` of a function `Ψ_bl` of the components at the places of `O` applied to the vacuum
`vacElem`. If `A` is `1` away from these places and their conjugates, it sends `Ψ_bl ⊗ vac` to a
nonzero multiple of `Ψ_bl(· A) ⊗ vac`, with `Ψ_bl(· A) = O.translatedBlockFn A`. 

### `descentPairing_translatedBlockFn_eq_zero`

 Let `O` be a descent pair with spaces `W` (rank `r`) and `V` (rank `n`), `u` a linear functional
on the values of the forms on `V`, `P` a polynomial with Fock vector `v_P`, and `g` an adelic point
of `U(W)`. For a form `y` on `V`, the number `B(Ψ, y) = descentPairing u P g Ψ y` is the value at
`g` of the theta lift to `U(W)`, with datum `v_P ⊗ Ψ ⊗ vac` (`vac` is the vacuum), of the conjugate
of the matrix coefficient `algFormCoeff 1 u y`. The function `Ψ_bl` of `O.blockDatum = Ψ_bl ⊗ vac`
is supported on the matrices that are integral at the places of `O` and, at the chosen places,
`≡ (1, 0)ᵀ` (rows `O.incl` the identity, other rows zero). There it is
`∏_{w ∈ Q} χ_w(det x' mod w)`, for `Q` the other places of `O`, `χ_w = O.tamePart w` and `x'` the
rows `O.incl`. Suppose that the lift for `Ψ = Ψ_bl` is zero at all points, and that the finite
adelic point `A` of `U(W)` is `1` away from the places of `O` and their conjugates. Then
`B(Ψ_bl(· A), y) = 0`. 

### `levelTranslate_idem_smul`

 If `Ψ` is Schwartz–Bruhat at the places of `O`, its translates under the level group read only
the components at these places; `idem O.places • x` is the part of `x` at these places. 

### `eventually_descentPairing_eq_zero_of_hasIntegralBlockRatio`

 **Points with an integral block ratio at every place.** Let `u` be a linear functional on the
values of the forms on `V`, `P` a polynomial with Fock vector `v_P`, and `g` an adelic point of
`U(W)`, for a descent pair `O` with spaces `W` and `V`. For a form `y`, let
`B(Ψ, y) = descentPairing u P g Ψ y` be the value at `g` of the descent of the conjugate of the
matrix coefficient `u` of `y` by the datum `v_P ⊗ Ψ ⊗ vac`. Suppose that this descent vanishes for
the block datum `Ψ_bl ⊗ vac`. Let `z` have an integral block ratio at every place of `O`: the block
`z'` of the rows `O.incl` is invertible, and for the other rows `z''` the matrix `z'' z'⁻¹` is
integral, and `≡ 0` at the chosen places. Then `B(1_C, y) = 0` for large `i`, where `1_C` is the
indicator of the class `C` of `z` modulo `i!` at the places of `O` and `factorialIdele E i` is the
number `i!` as a finite idele. 

### `blockAction`

 The form `χ(s)⁻¹ s̄ y` for blocks `s` at the chosen places and the places of `Q`, where
`χ(s) = ∏ χ_w(det s_w)` over all these places and `s̄` is the part of `s` at the chosen places. 

### `HyperplaneSumsAnnihilate`

 The hyperplane sums annihilate the form `y`: for rows `λ_w` at the chosen places `w`, not all
zero, the product of the sums `∑ χ_w(det s)⁻¹ s` over the invertible `s = 1 + v λ_w` kills `y`. 

### `sum_formAction_mulSingle_eq_zero`

 A descent pair `O` has two families of split places, the chosen places and a set `Q`, residue
characters `χ_w = O.tamePart w`, and a space `O.FormV` of forms on its space `V` of rank `n` with a
fixed weight and level. For a row `λ` over the residue field `k_w` of a chosen place `w`, the
hyperplane sum is `∑ χ_w(det s)⁻¹ s` over the group `hyperplaneGroup λ` of the invertible matrices
`s = 1 + v λ`, with `v` any column. The group `∏_w GL_r(k_w)` acts on these forms by
`O.formAction`: `(s_w)` acts as `∏_w χ_w(det s_w)` times right translation by an element of the
maximal level whose reductions are `diag(s_w, 1)` at the chosen places and `1` at `Q`. Suppose that
the product of the hyperplane sums of rows `λ_w`, not all zero, always kills `y`. Then the
hyperplane sum of `l ≠ 0` at the place of index `i` alone kills `y`. 

### `blockAction_mulSingle`

 For a block `s` at the single place `O.placeAt j` of index `j`, `O.blockAction` sends `y` to
`χ_w(det s)⁻¹` times `O.formAction` of the chosen-place part of `Pi.mulSingle j s` applied to `y`,
where `χ_w = O.tamePart (O.placeAt j)`. 

### `blockAction_mulSingle_inl`

 Let `w = O.placeAt (.inl i)` be the chosen place of index `i`, and `s` in `GL_r` of its residue
field. Then `O.blockAction` of the block `s` at `w` (and `1` elsewhere) on the form `y` is
`χ_w(det s)⁻¹` times `O.formAction` of `s` at `w` on `y`. 

### `blockAction_mulSingle_inr`

 For a block `s` at the place `O.placeAt (.inr i)` of `Q` and the identity at the other places,
`O.blockAction` sends `y` to `(O.tamePart (O.placeAt (.inr i)))⁻¹ (det s) • y`. 

### `sum_blockAction_eq_zero`

 Assume `χ_w ≠ 1` for `w ∈ Q`. Assume also `O.HyperplaneSumsAnnihilate y`: for rows `λ_w` at the
chosen places, not all zero, the product of the sums `∑ χ_w(det s)⁻¹ s` kills `y`, with
`s = 1 + v λ_w` invertible and `v` any column. Then at `w = O.placeAt j` and for a row `l ≠ 0`, the
sum of `O.blockAction s y = χ_w(det s)⁻¹ s̄ y` over `s` in `hyperplaneGroup l` is zero. Here `s̄` is
`s` at a chosen place and `1` at a place of `Q`. 

### `exists_leftMul_eq_and_blockAction_eq`

 Let `l` be an annihilating row for `z` at the place `w` of index `j`: an integral row with
`l z = 0` at `w` whose part `λ`, the entries indexed by `O.incl`, is not `≡ 0`, and whose other
entries are `≡ 0` if `w ∈ Q`. Let `s = 1 + v λ` be invertible over the residue field, for some
column `v`. Then there is an element `h` of the maximal level `stdLevel E n` such that `h z` and `z`
have the same components at the places of `O` and right translation of `y` by `h` gives the form
`O.blockAction s y = χ_w(det s)⁻¹ s̄ y` of `s` at `w`. Here `s̄` is `s`, acting by `O.formAction`,
if `w` is a chosen place, and is `1` if `w ∈ Q`. 

### `descentPairing_eq_zero_of_not_hasIntegralBlockRatio`

 **Points without an integral block ratio.** Let `O` be a descent pair, with spaces `W` and `V`,
chosen places, a second set `Q` of places and residue characters `χ_w`, with `χ_w ≠ 1` for `w ∈ Q`.
Let the hyperplane sums annihilate the form `y` on `V`: for rows `λ_w` over the residue fields of
the chosen places, not all zero, the product of the sums `∑ χ_w(det s)⁻¹ s` over the invertible
`s = 1 + v λ_w` kills `y`. Suppose that at some place `w` of `O` the component of `z` has no
integral block ratio: it is false that its rows `O.incl` form an invertible block `z'` such that,
for the other rows `z''`, the matrix `z'' z'⁻¹` is integral, and `≡ 0` if `w` is chosen. Then
`B(1_C, y) = 0` for the class `C` of `z` modulo any idele `t` at the places of `O`. Here
`B(Ψ, y) = descentPairing u P g Ψ y` is the value at the adelic point `g` of `U(W)` of the theta
lift, by the datum `v_P ⊗ Ψ ⊗ vac`, of the conjugate of the matrix coefficient of `y` for the linear
functional `u`. 

### `descentsVanish_of_hyperplaneSumsAnnihilate`

 **The bottom of the tower.** Let `O` be a descent pair: spaces `W = O.W` and `V = stdSpace E n`
of ranks `r` and `n`, two families of split places and residue characters `χ_w = O.tamePart w`. Let
`y` be a form on `V` and `u` a linear functional on its values. Assume that `χ_w` is nontrivial for
`w ∈ Q`, and that the hyperplane sums annihilate `y`: for rows `λ_w` at the chosen places, not all
zero, the product of the sums `∑ χ_w(det s)⁻¹ s` over the invertible `s = 1 + v λ_w`, with `v` any
column, kills `y`. Assume that the descents of the conjugate of the matrix coefficient
`algFormCoeff 1 u y` by the data `v_P ⊗ Ψ_bl ⊗ vac` vanish for all polynomials `P`. Then its
descents, for the character `O.charW` of `U(1)` attached to `W`, vanish for all data that are the
vacuum at the finite places other than the chosen places, the places of `Q` and their conjugates. 
