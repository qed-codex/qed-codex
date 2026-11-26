---
{
  "module": "src/New/Congruences/FirstOrder/RibetLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetLemma.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ribet's method to first order over a discrete valuation ring

This file proves an algebraic form of Ribet's method to first order that does not involve Galois
groups. Here `u x` (`x : Y`) is a finite family of representations of a group `G` over a discrete
valuation ring `O`; at certain `x`, `u x` is the sum of a main summand (the block) and of
characters. The file glues the matrices of tied rows for the block and for the characters, so that
one element serves the determinants of all combinations `∑ ω g (u x g - 1)`, and passes from
coefficients modulo powers of `p` to coefficients in `K/O`. The result is applied to Galois
representations in `New.Selmer.ribet_columns`.

In that application the data of `New.Selmer.exists_isCommonRibetElement_addVal_le` are as follows.
The elements `τ (j, true)` and `φ (j, true)` are a tame generator and a Frobenius element at the new
place `j`, and `τ (j, false)`, `φ (j, false)` are the inverses of their conjugates. The `δ v` are
tame generators at the old places, `γ x` acts on the summand by a scalar `y x` with `y x - 1` a
unit, `a` generates the cyclotomic quotient, `p` is `ℓ ^ ν`, and `C : O` is the cost of telling the
characters apart. The `X j` are free variables; only the coefficients of the monomials that divide
`∏ X j` are read.

## Main definitions and results

* `New.Selmer.exists_isCommonRibetElement_addVal_le`: the determinants of all combinations
  `∑ ω g (u x g - 1)` have one Ribet element whose coefficient comes from `O` and has bounded
  valuation. The proof finds matrices of tied rows with bounded determinant on the block
  (`exists_tiedRows_addVal_det_le`) and on the characters (`nonempty_characterRows`), and glues them
  (`exists_traceIdeal_multiplier_eq_sum_det`).
* `New.Selmer.exists_traceIdeal_multiplier_eq_sum_det`: the gluing, on the set where `u x` is the
  block `ρ x` plus the characters `ξ e`, with `ξ 0 = 1`.

Notions from other files:
* `New.Selmer.ribetCocyclesIn u ρ B`: the cocycles `G → B^d` for `ρ` that obey the linear relations
  among the families `(u x g - 1)_x`.
* `New.Selmer.IsCommonRibetElement` (`FittingBlock`): one `f : S` that serves as Ribet element for
  a family `β` of functions `β i : Y → L`.
* `New.Selmer.IsTraceIdeal` (`FittingBlock`): `S` holds the characteristic polynomials, and the
  `S`-module `𝒥` holds the traces of given relations.
* `New.Selmer.tiedRows` (`RibetMatrices`): the rows whose element `∑ r i (gen i - 1)` lies in the
  tie ideal.


 ### The gluing 

### `polyAction_eq_reindex`

 If `u x` is, after reindexing by `blockEquiv`, the block `ρ` plus the characters `ξ e`, then so
is its extension to `O[X j][G]` (`polyAction`, and `polyChar` for the characters). 

### `det_polyAction_rowValue`

 If the `z g` are coordinates of the `u · g - 1` (`AreCoordinates`), then under every `u x` the
value of the row `∑ ω g z g` (`rowValue`, `coordRows`) has the determinant of
`∑ ω g (u x g - 1)`, read in `L[X j]`. 

### `exists_mulVec_eq_add_mul_of_mem_tiedRows`

 Let `u x` (`x : Y`) be matrix representations of the group `G` over `O`, with
`u x g - 1 = ∑ z g i (u x (gen i) - 1)` for all `g` and `x` (`AreCoordinates`). A row `r` over
`O[X j][G]` is tied (`tiedRows`) if `∑ r i (gen i - 1)` lies in `tieIdeal`, the left ideal of
`O[X j][G]` spanned by the elements that every `u x` kills, by `p I`, by the ties
`τ k - 1 - X j * (ε j)(φ k) * (φ k - 1)` for `k = (j, b)`, and by `I ρ₀`; here `p : O`, the `τ k`
and `φ k` are elements of `G`, the `ε j` are polynomials over `O`, and `I` is the augmentation
ideal. Let the `S`-module `𝒥` of families `Y → L[X j]` contain the traces under the `u x` of the
`p g` and of the ties times `g`, for `g : G` (part of `IsTraceIdeal`). If the rows of `R` are tied,
the value `∑ R j i (gen i - 1)` of row `j` is `b + m ρ₀`, with `b` in the left ideal spanned by the
`r` with the traces of all `r g` in `𝒥` (`traceLeftIdeal`) and `m` in the left ideal of the
`gen i - 1`. This is the hypothesis on rows of `exists_ribet_element_of_tied_rows`. 

### `exists_ringHom_comp_eq_algebraMap`

 If `S` holds the variables `X j`, the map from `O[X j]` to the constant families factors through
`S`. 

### `coeff_charpoly_map_polyAction_single`

 The characteristic polynomial of a group element `g` acting through `polyAction J ρ`, read over
`L[X j]`, has the constant coefficients given by the characteristic polynomial of `ρ g`. 

### `C_det_linearCombination_mem`

 The determinants of all combinations `∑ ω g (u x g - 1)`, as families of constant polynomials,
lie in `S` when `S` holds the variables and the coefficients of the characteristic polynomials of
the `u x g`. Here `z g` are coordinates of `u · g - 1` in the `u · (gen i) - 1`
(`AreCoordinates`). 

### `det_linearCombination_sub_one_eq_zero`

 If `u x` is a block `ρ` plus characters `ξ e` with `ξ 0 = 1`, every combination
`∑ ω g (u x g - 1)` has determinant zero: its column at `ξ 0` is zero. 

### `exists_traceIdeal_multiplier_eq_sum_det`

 The gluing. Let `u x` (`x : Y`) be matrix representations of the group `G` over `O`, with
`u x g - 1 = ∑ z g i (u x (gen i) - 1)` for all `g` and `x` (`AreCoordinates`). On `𝓧`, `u x` is,
after reindexing along `blockEquiv`, the block `ρ x` plus the characters `ξ e`, with `ξ 0 = 1`.
Further let `S` be an algebra of families `Y → L[X j]`, where `L[X j]` is `MvPolynomial J L`, and
`𝒥` an `S`-module of such families; `S` contains the `X j` and the coefficients of the
characteristic polynomials of the `u x g`, and `𝒥` the traces under the `u x` of the `p g` and of
the ties (see below) times `g` (`IsTraceIdeal`). Representations act on `O[X j][G]` through
`polyAction` and characters through `polyChar`. Let `k` be `1` on the characters and `0` on the
blocks, and let `q₀` be `μ₀` on `ξ 0` and `0` on the other characters. Let `B₀` and the `M i`
(`i : κ`) be matrices of tied rows for `ρ₀ = n + (1 - n) (a - 1)` with `n = c₁ (γ - 1)`
(`tiedNormaliser`), and `wt i` weights. Then one `f : S` multiplies the determinants of all
combinations `∑ ω g (u x g - 1)` into `𝒥`, and its value at `x ∈ 𝓧` is
`∑ wt i μ₀ det (B₀ on the block) ∏ det (M i on ξ e)`. A row `r` over `O[X j][G]` is tied
(`tiedRows`) if `∑ r i (gen i - 1)` lies in `tieIdeal`, the left ideal of `O[X j][G]` spanned by the
elements that every `u x` kills, by `p I`, by the ties `τ l - 1 - X j * (ε j)(φ l) * (φ l - 1)` for
`l = (j, b)`, and by `I ρ₀`; here `p : O`, the `τ l` and `φ l` are elements of `G`, the `ε j` are
polynomials over `O`, and `I` is the augmentation ideal. 

### `exists_character_projector`

 The projector to the characters: if every block `ρ x` has an element `γ x` acting by a scalar
`y x` with `y x - 1` a unit, on which every character is `1`, then some element of `O[X j][G]` is
`1` on every character and `0` on every block. 

### `exists_areCoordinates_ribetGenerators`

 Finitely many generators. Let `u x` (`x : Y`) be finitely many matrix representations of `G`
over the discrete valuation ring `O`. There are a finite `s₀ ⊆ G` and vectors `z g` over `O` with
`u x g - 1 = ∑ z g i (u x (gen i) - 1)` for all `g` and `x` (`AreCoordinates`), where `gen` lists
the `δ w`, the members of `s₀` and those of `s` (`ribetGenerators`). 

### `CharacterRows.sum_prod_coeff_mul_prod_det_tiedMatrix`

 Let `R` be a system of matrices for the characters `ξ e`, `e : Fin t` (`CharacterRows`). For
each `e` it has `R.count e` matrices `R.charMatrix e j` over `O[X j]` and weights `R.coeff e j` with
`∑ j, R.coeff e j det (R.charMatrix e j) = R.detSum e`. For each choice `i` of one index `i e` for
every `e`, it has a matrix `R.tiedMatrix i` over `O[X j][G]` whose determinant on `ξ e` is
`c₀ det (R.charMatrix e (i e))`, where `c₀ = (∏ o v (1)) C ^ #s`. Then the products over `e` of the
determinants of `R.tiedMatrix i` on the `ξ e`, summed with the weights `∏ R.coeff e (i e)`, give
`c₀ ^ t ∏ R.detSum e`. 

### `CharacterRows.addVal_constantCoeff_prod_le`

 Let `O` be a discrete valuation ring with additive valuation `v = addVal O`, and let `R` be a
system of matrices for the characters `ξ e`, `e : Fin t` (`CharacterRows`). It has polynomials
`R.multiplier e` in the variables `X j` with
`R.detSum e + R.correction e = R.multiplier e * ∏ j with ty j = e, X j`, and the constant term of
`R.multiplier e` has valuation at most `b e + (#{j | ty j = e} + #s) v(C)`. As the sets
`{j | ty j = e}` partition `J`, the constant term of `∏ R.multiplier e` has valuation at most
`∑ b e + (#J + t #s) v(C)`. 

### `mem_ribetCocyclesIn_iff`

 Membership in `ribetCocyclesIn`: `c` is a cocycle for `ρ`, and it obeys every linear relation
among the families `u · g - 1`. 

### `comp_mem_ribetCocyclesIn_iff`

 Let `u x` (`x : Y`) be matrix representations of the group `G` over `O`, and let `f` be an
injective linear map of coefficient modules. Then `c` is a cocycle for `ρ` with `∑ θ g • c g = 0`
whenever `∑ θ g • (u x g - 1) = 0` for all `x` (`ribetCocyclesIn`) if and only if `f ∘ c` is one. 

### `exists_smul_eq_zero_of_mem_ribetCocyclesIn`

 Let `u x` be a finite family of representations of `G` over a discrete valuation ring `O` with
fraction field `K`. The cocycles of `ρ` with values in `K/O` that obey the linear relations among
the families `(u x g - 1)_x` are torsion: by the coordinates of
`exists_areCoordinates_ribetGenerators` the values of a member are combinations of finitely many of
them, and each element of `K/O` has a nonzero denominator. 

### `length_ribetCocyclesVanishingOn_divisibleQuot_le`

 From coefficients modulo powers of `p` to coefficients in `K/O = Frac(O) / O`. Let `u x` be a
finite family of representations of `G` over `O`. Consider the cocycles `c` of `ρ` that vanish on
`T` and at `γ` and have `∑ θ g • c g = 0` whenever `∑ θ g • (u x g - 1) = 0` for all `x`. If for
every `M` those modulo `p ^ M` have length at most `b`, where `p ≠ 0` is not a unit, so have those
with values in `K/O`: division by `a = p ^ (b + 1)` maps the cocycles modulo `a` onto the
`a`-torsion, and as `v(a) > b` this torsion is everything. 

### `exists_isCommonRibetElement_addVal_le`

 Ribet's lemma to first order, for any group and any discrete valuation ring. Let `u x` (`x : Y`)
be a finite family of matrix representations of `G` over `O` and `L` an `O`-algebra; let `S` be an
algebra of families `Y → L[X j]`, where `L[X j]` is `MvPolynomial J L`, and `𝒥` an `S`-module of
such families. (1) On `𝓧`, `u x` is, after reindexing along `blockEquiv`, a block `ρ x` plus
characters `ξ e` with `ξ 0 = 1`, and `ρ π` spans all matrices. (2) An element `γ x` acts on the
block by a scalar `y x` with `y x - 1` a unit, and trivially on the characters. (3) For `p ≠ 0` in
`O`, elements `τ k`, `φ k` of `G` (`k : J × Bool`) and polynomials `ε j` over `O`, `S` contains the
`X j` and the coefficients of the characteristic polynomials of the `u x g`, and `𝒥` contains the
families over `x` of the traces under `u x` of `p g` and of
`(τ k - 1 - X j * (φ k - 1) * (ε j)(φ k)) * g` for `g : G` and `k = (j, b)` (`IsTraceIdeal`); `ε j`
is `1` modulo `p` at the `ξ e (φ k)`. (4) For an element `a` of `G` and each `e`, the product of the
`ξ e a - ξ k a` over `k ≠ e` divides `C`; each `j` has a type `ty j`, monotone in `j`. (5) The
cocycles `c` of `ρ π` with values in `Frac(O) / O` that have `∑ θ g • c g = 0` whenever
`∑ θ g • (u x g - 1) = 0` for all `x` and vanish at the `τ k` and at `γ π` form a module of length
at most `b₀`. (6) The `δ v` are trivial on the characters and `o v * (X - 1)` kills every
`u x (δ v)`. (7) Every module `Z` of character cocycles for `ξ e` satisfies `HasTriangleCost` along
the `j` of type `e`, and a member of `Z` that vanishes on the finite set `s ⊆ G` is zero
(`IsDetectedBy`). Then the determinants of all combinations `∑ ω g (u x g - 1)` lie in `S` and
vanish on `𝓧`, one `f : S` multiplies them into `𝒥`, `f` has on `𝓧` no monomial properly dividing
`∏ X j`, and the coefficient of `∏ X j` in `f π` comes from some `c : O` of valuation at most
`b₀ + ∑ b e + t (∑ val (o v (1)) + 2 #s val C) + (#J + 1) val C`, with `val = addVal O` and `t` the
number of characters. A character cocycle for `ξ e` is a cocycle `c : G → O / p` for `ξ e` that has
`∑ θ g • c g = 0` whenever `∑ θ g • (u x g - 1) = 0` for all `x`, vanishes at the `δ v`, and, if it
vanishes at `γ π`, has `(ξ e g - 1) • c a = 0` for all `g`. `HasTriangleCost` asks for a set `A ⊆ G`
such that, with `Z₀` the part of `Z` vanishing on `A`: for `j` of type `e` and `c ∈ Z₀`, `C` kills
`c (τ (j, true)) - c (τ (j, false))` as soon as `c (τ (i, true)) = c (τ (i, false))` for all `i < j`
and `c (φ (i, true)) = c (φ (i, false))` for the `i < j` of type `e`; and the length of `Z / Z₀`
plus the length of `Z₁` modulo its `C`-torsion is at most `b e`, for every submodule `Z₁ ≤ Z₀` whose
members vanish at all `τ k` and have `c (φ (j, true)) = c (φ (j, false))` for `j` of type `e`. 
