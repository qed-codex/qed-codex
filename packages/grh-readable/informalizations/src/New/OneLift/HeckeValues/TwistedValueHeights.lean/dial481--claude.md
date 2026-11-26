---
{
  "module": "src/New/OneLift/HeckeValues/TwistedValueHeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Heights of ratios of twisted to untwisted Hecke values via rank-one theta lifts

This file builds a test form (`New.DescentPair.IsTestForm`: integral above `ℓ` and orthogonal to the
false lifts) from class sums on four blocks of indices. Its pairing with the lift of a main pair has
small valuation at `ℓ`. With the bound for the denominators of the projections to the line of the
lift, this bounds the valuation of the squared norm of the twisted lift from above. Here
`New.HeightLe c y` says that the family `y ι`, one number for each `ι : ℂ ≃ ℚ̄_ℓ`, has height at
most `c`; the file bounds the heights of inverse ratios of twisted to untwisted Hecke values, with
twists along a family `θ` with `New.Data.IsRegularFamily`.

## Main definitions and results

* `New.Data.exists_isTestForm_le_norm_inner_trivialLift`: at every prime `l` coprime to `ϑ.normQ` of
  a twist `ϑ`, some test form has a pairing of small valuation with the lift
  `New.Data.CriticalPair.trivialLift` of a main pair.
* `New.Data.heightLe_inv_ratio`: the inverse ratios of a main pair have height at most
  `6 denominatorBudget - directionAmount`.
* `New.Data.exists_heckeValueProd_eq_mul_prod_ratio`: the quotient of the Hecke values
  `New.Data.heckeValueProd j` at a twist and at `1` as a product of ratios of L-values.
* `New.Data.heightLe_inv_heckeValueProd_div`: a bound for the height of the inverse of this
  quotient.

Notions from other files:
* `New.Data.CriticalPair`: An integer 1 ≤ z ≤ t and a character ν of U(1)(𝔸) of weight −c,
  z ≤ c(v) ≤ 4b, with tame part supported on the chosen places.
* `New.Data.CriticalPair.integralAlgebraicPart`: The product of
  `n_L = chosenGroupOrder * denomBound ^ 2` and the algebraic part `‖φ‖² / N(Q) ^ (2 z - 1)`
  (`New.Data.CriticalPair.algPart`); the first factor of `n_L` clears the orders of automorphism
  groups, the second the denominators of `φ`.
* `New.Data.CriticalPair.ratio`: The ratio |L(z, (νϑ^s)⁻¹)| / |L(z, ν⁻¹)| for a sign s (by default
  1), without the Euler factors at the level.

The data `D` over the parameters `P` supply the CM field `D.E`, with `f` infinite places and
`D.towerExp` its index in the tower over `K = ℚ(i√d)`, the natural numbers `m`, `k`, `r`, `t`, `M`
and `a`, and the reals `b`, `x`, `x₁` of the bounds. Here `M ^ f` is the norm of the product of the
chosen places, `x` the length of the prime sum, `denominatorBudget = f a log³ b / (m k)` and
`directionAmount` the sum over the infinite places `σ` of `jetSize (κ σ) - primeSum (κ σ) σ`, where
`κ = D.weight`, `jetSize` is the size of a derivative and `primeSum` measures its guaranteed
divisibility.

`P.vacuumScale D.towerExp` scales the vacuum of rank one to integral values, `P.jetScale D.towerExp`
scales Taylor series of theta functions, `modKernel` is the theta kernel given by a function on
matrices modulo an ideal and a polynomial, and `p.rowLengthSum` is `∑ τ, (p.negWeight τ - p.z)`.

## Relation to the literature

Norms of lifts of Hecke characters as L-values, their divisibility via congruences, and divisibility
at inert primes are known from the literature. Related work: Prasanna, Integrality of a ratio of
Petersson norms, 2006; Coates–Liang–Sujatha, Tate–Shafarevich group for elliptic curves with CM II,
2010 (after Katz, 1977); Y.-S. Lee, Hida family of theta lift from U(1) to definite U(2), 2024.


### `_root_.New.rationalU1_sup_integralU1_le_comap`

 Let `u` be a norm-one adele, rational or with integral finite part congruent to `1` at the
places of `S`, or a product of such. Let `Γ` contain the rational points of `U(1)`, and let `K`
contain the principal level at places `w i ∈ S`. Then the finite part of `u`, as a `1 × 1` matrix,
lies in `Γ ⊔ K`. 

### `_root_.New.exists_norm_le_norm_twisted_classSum`

 Orthogonality of characters on the classes of `U(1)(𝔸_f) = Gf E Unit`. Let `Γ` contain the
rational points, let `K` contain the principal level at the places `w i ∈ S`, let `K` be compact
open and `Γ \ U(1)(𝔸_f) / K` finite (`HasFiniteType`), and let all stabilisers be trivial, so that
`classSum Γ K` is the sum over chosen representatives of the classes. Let `l` be a prime and
`ι : ℂ → ℂ_l` an embedding. Then for every function `s` there are a translation `z` and a character
`χ` of weight zero, with tame part trivial off `S`, such that the class sum of
`g ↦ χ(det(g z)) · s(g z)`, divided by the class sum of `1`, has norm under `ι` at least that of
`s 1`. 

### `exists_mul_eq_norm_map_le_norm_map_mul`

 Multiplicative pigeonhole. Let `V^{|G|} = ∏_χ a(χ)b(χ)` over a finite group `G`, and let `ι` be
a ring homomorphism into a normed field. Then every `ψ` has a factorisation `ψ = φχ` with
`‖ι V‖ ≤ ‖ι(a(φ)b(χ))‖`. 

### `pointForm_mem_integralForms`

 The point form with vector `v`, supported on one class next to the point `h`, is integral at
`j : ℂ → ℂ_l`, for a prime `l`, if `v` has gauge at most one at `h`. The gauge `weylGauge` is the
largest `l`-adic norm of a coordinate of `h⁻¹ v`, in the representation of weight `O.columnCount`
twisted by the determinant powers `O.detExp`, with coordinates indexed by
`WeylIndex n O.columnCount`. 

### `CriticalPair.trivialLiftClassSum`

 For a pair `q = (ν, z)` that is flat (`HasEmptyRow`: the character has weight `-z` at every
infinite place, and the index type has `2 z ≥ 4` elements) on `Fin m` and a function `F` on
`U(m)(𝔸_f)` with values in the forms for `X`, this is `D.chosenGroupOrder` times the class sum over
`h` of `d / N(Q) ^ (m - 1) * ⟨1, d • Ξ h⟩ • F h`. Here `Ξ = trivialLift H.hasLiftRank ϑ` is the
normalised lift of `ν ϑ`, `d = q.denomBound`, `N(Q) = ϑ.normQ` is the norm of the modulus of `ϑ`,
and `⟨ , ⟩` is the pairing `gramForm`. 

### `CriticalPair.trivialLiftClassSum_mem`

 Let the pair `q = (ν, z)` be flat on `Fin m`, and fix a prime `l` with an embedding `ℂ → ℂ_l`
(`PadicPlace l`), of valuation ring `embValRing`. Let `l` be prime to the norm `ϑ.normQ` of the
modulus of `ϑ`. If `F` takes values in an `embValRing`-module `N` of forms for the lift data `X`,
then `N` contains `trivialLiftClassSum hq ϑ F`, the class sum of `F` over `U(m)` weighted by the
values of the lift of `ν ϑ`. 

### `CriticalPair.smul_apply_trivialLiftClassSum`

 Let `ϑ` be a tame character, `g` a point of `Gf D.E Unit`, and `F` a map from `Gf D.E (Fin m)`
to the forms `X.descentPair.FormV`. Let the pair `q = (ν, z)` have an empty row on `Fin m`. Let a
conjugate-linear form `L` take at `F h` the value `B * (A * kernelForm g h i)`, for every `h` and
every coordinate `i` of the theta kernel at `(g, h)` of the lift data `lValueData` of `ν ϑ`. Then
`N * P.vacuumScale D.towerExp ^ m` times the value of `L` at the class sum
`trivialLiftClassSum hq ϑ F` is `B * integralAlgebraicPart * A`. Here
`N = stdClassSum chosenLevel 1` is the class sum of `1` on `U(1)` at the chosen level. 

### `CriticalPair.kernelForm_eq_modKernelStdSpace_of_hasEmptyRow`

 Let the pair `q = (ν, z)` be flat on `Fin m`, let `ϑ` be a tame character and `lValueData` the
data of the lift of `ν ϑ` from `U(1)` to `U(m)`. Every coordinate of its kernel at `(g, h)` is the
theta kernel `modKernelStdSpace`, with polynomial `1` and character `charV = ν ϑ υ ^ z` (`υ` the
splitting character), of the function `residueBlockDatum`, read modulo any multiple `𝔪` of
`levelModulus 2` through the residues `levelResidueAt`. This function is zero unless the residue at
each chosen place is the standard column, and is then the product over the twist places `w` of the
tame part at `w` of the determinant of the chosen row. 

### `twistRow`

 The chosen row of the second of the four blocks of `RankOneIndex z`, the block that carries the
twist. 

### `testColumn`

 For a main pair `p` and a chosen place `i`, the column over the residue field at `i`, with rows
`RankOneIndex p.z`, made of the residue of `x₀` on the first block, of size `12`, and of a standard
basis vector on each of the other three blocks. 

### `testColumn_injective`

 The column `testColumn` is injective as a linear map, since its last block is a standard basis
vector. 

### `inner_pointForm_kernelForm`

 Seesaw factorisation at one point. Let `X` be the lift data of a main pair `p`, with point
`z = p.z`, at the twist `ϑ`; its `2 z` indices form blocks of sizes `12`, `4`, `4`, `2 z - 20`. Let
`q₂`, `q₃`, `q` be flat on the last three blocks; `q₂` is taken at `ϑ`, the other two at the trivial
character. Take the point form, supported on one class of `U(2 z)(𝔸_f)`, at the block diagonal point
`diag (1, h₂, h₃, h₁)`. Its datum is `testColumn` (`x₀` on the first block) at the chosen places and
reads the row `twistRow` of the second block at the places of the modulus of `ϑ`. Its vector `c` has
as polynomial `a` times the monomial `α` in the first block. If `χ` and the characters of the last
three blocks multiply to the character of `X`, then the inner product of the point form with the
theta kernel `X.kernelForm g`, for `g ∈ U(1)(𝔸_f)`, is `a` times a product of four theta kernels at
`g`, one for each block. The first, `modKernel`, belongs to `χ`, the indicator of `x₀` and `α`. 

### `isTestForm_trivialLiftClassSum_pointForm`

 Let `l` be a prime, `p` a main pair for `j` with point `z = p.z`, whose `2 z` indices form
blocks of sizes `12`, `4`, `4`, `2 z - 20`, and `ϑ` a twist. Let `q` be flat on the last block. Take
the point forms at the block diagonal points `diag (1, h₂, h₃, h₁)` of `U(2 z)(𝔸_f)` whose datum is
`testColumn` at the chosen places and reads the row `twistRow` of the second block at the twist
places. Let their integer vector `c` be fixed by `weylRep`, the representation of weight
`columnCount` twisted by the powers `detExp` of the determinant, at every family `g` over the
infinite places `D.Φ`, over a field of characteristic zero, whose columns in the first block are
those of the identity. Then their class sum `trivialLiftClassSum` over `h₁`, weighted by the values
of the untwisted lift of `q`, is a test form (`IsTestForm`): integral above `l` and orthogonal to
the false lifts, the forms in the kernel of the descent to `U(1)`, in the image of the mean over the
residue units at the chosen places, that the Hecke polynomial of a split place `w` at
`liftHeckeRoot w` kills. 

### `exists_isTestForm_inner_kernelForm_eq`

 Seesaw factorisation. Let `l` be a prime with a chosen embedding `ℂ → ℂ_l`. Let `p` be a main
pair for `j` with point `z = p.z`, and let `X` be the lift data of `p` at the twist `ϑ`, with `l`
prime to `ϑ.normQ`. Let `q₂`, `q₃`, `q` have empty row on blocks of sizes `4`, `4` and `2 z - 20`:
`q₂` is taken at `ϑ`, the other two at the trivial character. Let the monomial `α` have degree
`X.rowLength τ` at each infinite place `τ`, and let `χ` and the characters of the three blocks
multiply to that of `X`. Then there is a test form `Ξ` on `U(2 z)` at `l`. Its inner product with
the theta kernel `X.kernelForm g`, for `g ∈ U(1)(𝔸_f)`, times
`N ^ 3 * vacuumScale ^ (2 z - 20 + 8)`, is `∏ (X.rowLength τ)! / α!` times the three numbers
`integralAlgebraicPart` and the theta kernel `modKernel` of `χ`, the indicator of `x₀` and `α`. Here
`integralAlgebraicPart` is `chosenGroupOrder * denomBound ^ 2 * ‖φ‖² / N(Q) ^ (2 z' - 1)` for the
normalised lift `φ` of a pair with point `z'` at a twist of norm `N(Q)`, `N` is the class sum of `1`
over `X.chosenLevel`, `vacuumScale` scales the vacuum vector of the Weil representation of rank one
to integral values, and `x₀` is read modulo `X.levelModulus 1 false`, the product of the chosen
places. 

### `modKernel_div_apply`

 The theta kernel `modKernel` of the datum given by a function `Ψ` modulo `𝔪` and a polynomial
`Q`, with the characters `a` and `b` that twist the action, is multiplied at `(g, h)` by
`ψ (det g)` when `b`, the character of the first group, is divided by `ψ`. 

### `norm_map_mul_le_iff_le_div`

 For an embedding `ι` of `ℂ` in a normed field and `ρ ≠ 0`, the bound
`‖ι (V * ρ)‖ * a ≤ ‖ι y‖` is the bound `‖ι V‖ * a ≤ ‖ι (y / ρ)‖`. 

### `exists_root_prod_integralAlgebraicPart`

 Let `χ` run over the finite group `tameChars` of characters of `U(1)(𝔸)` of weight zero whose
tame part is trivial off the chosen places. Let the critical pairs `q₁ χ` and `q₃ χ` have empty row
(`HasEmptyRow`) on `n` and on `Fin 4`. Some geometric mean `L` over `χ` of the products of their
untwisted values `integralAlgebraicPart` is not zero, and its conjugates have size at most
`exp (x ^ 34) ^ 2`. 

### `exists_isTestForm_le_norm_inner_trivialLift`

 A form with small pairing. Let `1 ≤ j ≤ m`, let `p` be a main pair for `j` (`IsMainPair`) and
`q₂ = (ν₂, 2)` a pair with empty row on `Fin 4`. There is a number `c₀ ≠ 0` whose conjugates have
size at most `exp (f m b / k + 3 x ^ 34)` such that, for every prime `l`, every embedding
`ιₚ : ℂ → ℂ_l` (`PadicPlace l`) and every twist `ϑ` with modulus prime to `l`, some test form `Ξ` on
`U(2 p.z)` has `v ⟪Ξ, φ⟫ ≤ v(c₀ · q₂.ratio ϑ) + localPrimeSumTotal l`. Here `φ` is the normalised
lift of the character of `p` times `ϑ`, `q₂.ratio ϑ = |L(2, (ν₂ ϑ)⁻¹)| / |L(2, ν₂⁻¹)|` without the
Euler factors at the level, `localPrimeSumTotal l` is the exponent of `l` that is forced on
derivatives of order `D.weight`, summed over the infinite places, and the valuation `v` of `ιₚ` is
written with norms. 

### `heightLe_inv_ratio`

 Let `θ ι` be `m`-fold twists (characters of weight zero whose first `m` powers are ramified at
every place of the modulus), one for each prime `l` and isomorphism `ι : ℂ ≃ ℚ̄_l`. Let them form a
regular family (`IsRegularFamily`): the modulus is prime to `l`, the inverse ratios of `L`-values of
ramified pairs have height at most the second cut-off `x₁ = D.x₁`, and the logarithmic denominators
of projections to lifts add up over `l` to at most `denominatorBudget`. Let `p = (ν, z)` be a main
pair for `j` (`IsMainPair`) and `p.ratio ϑ = |L(z, (ν ϑ)⁻¹)| / |L(z, ν⁻¹)|`, without the Euler
factors at the level. Then the family over `ι` of the inverse ratios at `ϑ = (θ ι) ^ j` has height
(`New.HeightLe`) at most `6 denominatorBudget - directionAmount`. Here
`denominatorBudget = f a log³ b / (m k)`. 

### `isMainPair_lowerPoint_exchangePair_none`

 Let `1 ≤ j ≤ m`, and let `exchangePair j none = (ν_j, z_*)` be the pair made from the character
of the `j`-th lift, of tame part `D.chiMLocal ^ j`, at the point
`z_* = mainPairPoint = 7 (m / 2) + k / 2`, where `m = D.m` and `k = D.r + 1 - m`. For
`7 (m / 2) < z ≤ z_*` the pair `lowerPoint z = (ν_j, z)` is a main pair for `j`. 

### `isRamified_lowerPoint_exchangePair`

 For every `z`, the pair `(exchangePair j i).lowerPoint z`, which has the same character as
`exchangePair j i`, is ramified: its tame part is non-trivial exactly at the chosen places. 

### `heckeValueProd_eq_mul_prod_ratio_sq`

 The Hecke value `heckeValueProd j ϑ` is the product, over the three pairs
`(ν_i, z_i) = exchangePair j i` for `i = none, 1, -1`, of `∏_{w ∈ S} q_w ^ (z_i ^ 2) ∏_{1 ≤ z ≤ z_i}
|L^S(z, (ν_i ϑ ^ s_i)⁻¹)|²`. Here `s_i = i.getD 1` is a sign, and `S` consists of the chosen places
and the places `ϑ.Q` of the twist `ϑ`. It equals the untwisted value `heckeValueProd j 1`, times
`ϑ.normQ ^ ∑ z_i ^ 2` (the product of the norms of the places of `ϑ.Q`), times the square of the
product of the ratios `ratio ϑ s_i = |L(z, (ν_i ϑ ^ s_i)⁻¹)| / |L(z, ν_i⁻¹)|`. These ratios are
taken for the pairs `lowerPoint z = (ν_i, z)` with `1 ≤ z ≤ z_i`. 

### `exists_heckeValueProd_eq_mul_prod_ratio`

 Let `heckeValueProd j ϑ` be the product of the squared `L`-values at `1 ≤ z ≤ z_i` of the three
pairs `(ν_i, z_i) = exchangePair j i`, twisted by `ϑ` or its inverse, with powers of the norms of
the omitted places. It is the untwisted value times a power `e` of the norm `ϑ.normQ` of the modulus
of `ϑ` and the square of a product of ratios `(ν, z).ratio ϑ s = |L(z, (ν ϑ ^ s)⁻¹)| / |L(z, ν⁻¹)|`.
Of these `k / 2` belong to main pairs `p a` for `j` (`IsMainPair`), with `s = 1`, and `5 m` to
ramified pairs `q b`, with signs `s b`. Here `m = D.m` is the number of lifts and `k = D.r + 1 - m`.
The exponent, the pairs and the signs do not depend on `ϑ`. 

### `heightLe_inv_heckeValueProd_div`

 Let `θ ι` be `m`-fold twists, one for each prime `l` and isomorphism `ι : ℂ ≃ ℚ̄_l`. Let them
form a regular family (`IsRegularFamily`): the modulus is prime to `l`, the inverse ratios of
`L`-values of ramified pairs have height at most the second cut-off `x₁ = D.x₁`, and the logarithmic
denominators of projections to lifts add up over `l` to at most `denominatorBudget`. Let
`1 ≤ j ≤ m`, and let `heckeValueProd j ϑ` be the product of the Hecke values `lValueProd` of the
three pairs `exchangePair j i`, twisted by `ϑ` or its inverse: the pair made from the character of
the `j`-th lift, and two flat pairs of tame parts `D.chiMLocal ^ (± j)` at the points `m` and
`m / 2`. Then the family over `ι` of the inverse ratios of its value at `(θ ι) ^ j` to its value at
`1` has height (`New.HeightLe`) at most `10 m x₁ + k (6 denominatorBudget - directionAmount)`. 
