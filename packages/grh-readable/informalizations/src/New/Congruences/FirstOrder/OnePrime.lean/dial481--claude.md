---
{
  "module": "src/New/Congruences/FirstOrder/OnePrime.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/OnePrime.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/OnePrime.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Norms, logarithms and first-order deformations of the norm

The algebra behind the family of operators at the auxiliary places. A finite group maps to a ring
`R`, and a congruence `a ≡ b` is an equality `σ a = σ b` after a ring map `σ`. The file treats the
norm `Nm` (the sum of the group elements), the coefficients of a product of first-order deformations
`Nm j + α j ∂ j` of the norms `Nm j` of the factors of a product group (the `α j` are variables
and `∂ j ∈ R`), the first entry on the stabiliser of a line in `GL_N`, and logarithms, that is,
norms weighted by a homomorphism to `ℤ/m`.

## Main definitions and results

* `New.Patching.familyCoeff`, `New.Patching.exists_empty_eq_sum_and_insert_eq_mul`: the coefficients
  of `∏ (Nm j + α j ∂ j)` and their properties.
* `New.Patching.map_top_coeff_mul_C_sub_X_mul_C_eq_zero`,
  `New.Patching.exists_map_pow_mul_family_eq_mul_norm`: this product times any multiple of
  `t - α j r` has top coefficient `≡ 0` when `Nm j t = 0` and `∂ j t ≡ Nm j r`, and suitable
  multiples of the coefficients factor through the norm.
* `New.Patching.transfer_firstEntry`: over a finite field, the transfer to `GL_N` of the first entry
  on the stabiliser of a line is the determinant.
* `New.Patching.map_cosetNorm_mul_weightedSum_mul_cosetNormInv`,
  `New.Patching.map_sub_one_mul_weightedSum_valMinAbs`,
  `New.Patching.exists_map_valMinAbs_mul_sub_one`: three congruences for logarithms.
* `New.Patching.map_valMinAbs_eq_zero_of_shift`: a map on weights that kills all differences
  `f (· - k) - f` kills the logarithm modulo `m / (2 k)`.
* `New.Patching.cosetDerivative`, `New.Patching.exists_map_nsmul_mul_sub_one_eq_sum_mul`: the
  operator `∂` built from a logarithm on a subgroup; `n ∂ (g - 1)` is congruent to a multiple of the
  norm.

Notions from other files:
* `New.LocField w`, `New.LocInt w`, `New.ResField w`: for a finite place `w` of a number field, the
  completion `E_w`, its ring of integers `O_w` and its residue field, which has `w.q` elements.
* `New.localIntGL n w`: the subgroup `GL_n(O_w)` of `GL_n(E_w)`.



## Congruences, norms and the family


### `IsReductionMod`

 A ring map `σ` is a reduction modulo `m / k` if it kills every `x` with `k x ∈ m R`. Then a
congruence `a ≡ b` modulo `m / k` implies `σ a = σ b`; `exists_isReductionMod` gives a `σ` for which
the converse holds. 

### `exists_isReductionMod`

 Let `R` be an `O`-algebra that has no `k`-torsion, and let `μ ∈ O` satisfy `k μ = m`. There is a
ring map `σ` on `R` that is a reduction modulo `m / k` (it kills `x` if `k x ∈ m R`) and whose
kernel lies in `μ R`. 

### `mul_sum_monoidHom`

 The norm `∑ ρ h` is fixed by left multiplication with `ρ g`. 

### `sum_monoidHom_mul`

 The norm `∑ ρ h` is fixed by right multiplication with `ρ g`. 

### `nsmul_eq_norm_mul`

 If `∑ g⁻¹ Ψ g = n` and `g A = A` for all `g`, then `n A = Nm Ψ A`, where `g` stands for `ρ g`
and `Nm = ∑ g`. 

### `nsmul_eq_mul_norm`

 If `∑ g⁻¹ Ψ g = n` and `A g = A` for all `g`, then `n A = A Ψ Nm`, where `g` stands for `ρ g`
and `Nm = ∑ g`. 

### `map_nsmul_eq_mul_norm`

 Let `ρ` map the product of the finite groups `Γ j` to the ring `R`, and let `σ : R → R'` be a
ring map. Write `g` for `ρ g`, `Nm = ∑ g`, and `a ≡ b` for `σ a = σ b`. If `∑ g⁻¹ Ψ g = n` and
`A (g - 1) ≡ 0` for all `g` in each factor `Γ j`, then `n A ≡ A Ψ Nm`. 

### `commutingProd`

 The product `x ↦ ∏ x j` of elements `x j ∈ 𝒜 j` of pairwise commuting subrings of `R`. 

### `commutingProd_update`

 In a product of elements of pairwise commuting subrings, any one factor can be written last. 

### `commutingProd_sum`

 A product of sums of elements of pairwise commuting subrings expands as a sum of products:
`∏_j ∑_i x j i = ∑_f ∏_j x j (f j)`. 

### `familyCoeff`

 The coefficient `∏_{j ∈ S} ∂ j ∏_{j ∉ S} Nm j` of `∏_{j ∈ S} α j` in the family
`∏ (Nm j + α j ∂ j)` in commuting variables `α j`, where `Nm j` and `∂ j = der j` lie in the `j`-th
of the pairwise commuting subrings `𝒜 j`. 

### `commute_familyCoeff`

 An element that commutes with all the subrings `𝒜 j` commutes with every product
`familyCoeff h𝒜 Nm der S = ∏_{j ∈ S} der j ∏_{j ∉ S} Nm j` of elements `der j`, `Nm j` of `𝒜 j`. 

### `familyCoeff_empty`

 Let `𝒜 j` be pairwise commuting subrings of `R`, with elements `Nm j` and `der j`, so that
`familyCoeff h𝒜 Nm der S` is the product `∏_{j ∈ S} der j ∏_{j ∉ S} Nm j`. Let `ρ` map the product
of the finite groups `Γ j` to `R`, with `Γ j` going into `𝒜 j`. If `Nm j` is the sum of `ρ` over
`Γ j`, then the product `∏ Nm j` at `S = ∅`, in which no `der j` occurs, is the sum of `ρ` over the
whole group. 

### `exists_familyCoeff_eq_mul`

 Let `Nm j` and `∂ j = der j` lie in the `j`-th of the pairwise commuting subrings `𝒜 j` of `R`.
Then `familyCoeff h𝒜 Nm der S` is the coefficient of `∏_{i ∈ S} α i` in the product
`∏ (Nm i + α i ∂ i)` in commuting variables `α i`. For `j ∉ S` the coefficients at `S` and at
`insert j S` differ only in the factor at `j`: they are `N' Nm j` and `N' ∂ j` for one `N'`. 

### `exists_empty_eq_sum_and_insert_eq_mul`

 Let `ρ` map the product of the finite groups `Γ j` to the ring `R`. Let `𝒜 j` be pairwise
commuting subrings that contain `der j` and the image of `Γ j`. Let `Nm j` be the sum of `ρ` over
`Γ j`. There are elements `N S` that commute with every `t` commuting with all `𝒜 j`, such that
`N ∅` is the sum of `ρ` over the whole group and, for `j ∉ S`, `N S = N' * Nm j` and
`N (insert j S) = N' * der j` for some `N'`. One may take `N S` to be the coefficient of
`∏_{j ∈ S} α j` in `∏ (Nm j + α j * der j)`. 

### `coeff_mul_C_sub_X_mul_C_of_notMem`

 For `j ∉ S`, the coefficient of `∏_{i ∈ S} X i` in `G (t - X j r)` is `t` times that in `G`. 

### `coeff_mul_C_sub_X_mul_C_insert`

 For `j ∉ S`, the coefficient of `X j ∏_{i ∈ S} X i` in `G (t - X j r)` is `t` times that in `G`
minus `r` times the coefficient of `∏_{i ∈ S} X i` in `G`. 

### `map_top_coeff_mul_C_sub_X_mul_C_eq_zero`

 Let `σ : R → R'` be a ring map, write `a ≡ b` for `σ a = σ b` and `∂ j = der j`, and let the
commutative ring `T` map to `R` by `ac`. Let `𝒩 = ∑_S N S ∏_{i ∈ S} X i` be the polynomial over `R`
with coefficients `N S`, of degree at most one in each of the variables `X i`, which commute with
each other and with `R`. For a polynomial `P` over `T`, the coefficient of `∏_{i ∈ J} X i` in
`𝒩 P` is then the sum over `S` of `N Sᶜ` times the coefficient of `∏_{i ∈ S} X i` in `P`. Suppose
that for `j ∉ S` there is `N'` with `N S = N' Nm j` and `N (insert j S) = N' ∂ j`. If `Nm j t = 0`
and `∂ j t ≡ Nm j r`, then this coefficient is `≡ 0` for every multiple `P = G (t - X j r)`. 

### `exists_map_pow_mul_family_eq_mul_norm`

 Let `ρ` map the product of the finite groups `Γ j` to the ring `R`, and let `σ : R → R'` be a
ring map. Write `g` for `ρ g`, `Nm = ∑ g` for the norm, `Nm j` for the sum over `Γ j`,
`∂ j = der j`, and `a ≡ b` for `σ a = σ b`. Let `N S ∈ R` be indexed by the subsets `S` of `J`, with
`N ∅ = Nm`, and for `j ∉ S` let `N S = N' Nm j` and `N (insert j S) = N' ∂ j` for some `N'`, as for
the coefficients of `∏ (Nm j + α j ∂ j)` in variables `α j`. Let `∑ g⁻¹ Ψ g = n` and `δ = n² δ'`,
where `δ'` commutes with the group and with all `N S`. Suppose that each `g ∈ Γ j` has a `Z` with
`n ∂ j (g - 1) ≡ Nm j Z` and `δ' Nm Z = 0`. Then for `i ≥ #S` there is a `Y` with
`δ ^ i N S ≡ Y Nm`, and `Y = δ ^ i` if `S` is empty. 


## The first entry on the stabiliser of a line

The transfer of the first entry over a finite field; then the first entry and the determinant of
the reduction of an integral matrix, and the logarithm on the residue units.


### `residueLineStabilizer`

 The stabiliser in `GL_N(F)` of the line of the first basis vector. 

### `mem_residueLineStabilizer`

 A matrix stabilises the line of the first basis vector if and only if its first column
vanishes below the first entry. 

### `mul_apply_zero_of_mem_residueLineStabilizer`

 If `p` stabilises the line of the first basis vector, then the first column of `h p` is the
first column of `h` times the first entry of `p`. 

### `firstEntry`

 The first entry `g ↦ g 0 0`, a character of the stabiliser of the line of the first basis
vector: the scalar by which `g` acts on that line. 

### `firstEntry_conj_diagGL`

 Let `d = diagGL t` be the diagonal matrix with entries `t i`. If `h⁻¹ d h` stabilises the line
of the first basis vector, then the first column of `h` is an eigenvector of `d`, so the first entry
of `h⁻¹ d h` is `t i` whenever the `i`-th entry of that column is nonzero. 

### `transfer_firstEntry_diagGL`

 Let `F` be a finite field, and let `firstEntry` be the character `g ↦ g 0 0` of the stabiliser
in `GL_N(F)` of the line of the first basis vector. Its transfer to `GL_N(F)` takes the value `x` at
the diagonal matrix `diag (x, 1, …, 1)`. 

### `map_toGL_transvection_eq_one`

 A character `τ` of `GL n F` with values in `Fˣ`, for a finite field `F`, is trivial on
transvections: `τ` sends the image of each transvection `t` to `1`. 

### `transfer_firstEntry_diagGL_mulSingle`

 Let `F` be a finite field, and let `firstEntry` be the character `g ↦ g 0 0` of the stabiliser
in `GL_N(F)` of the line of the first basis vector. Its transfer to `GL_N(F)` takes the value `x` at
the diagonal matrix with `x` in place `i` and `1` elsewhere. 

### `transfer_firstEntry`

 Let `F` be a finite field, and let `firstEntry` be the character `g ↦ g 0 0` of the stabiliser
in `GL_N(F)` of the line of the first basis vector, the scalar by which `g` acts on that line. Its
transfer to `GL_N(F)` is the determinant. 

### `transfer_comp_firstEntry`

 Let `F` be a finite field, `l` a homomorphism from `Fˣ` to a commutative group, and `firstEntry`
the character `g ↦ g 0 0` of the stabiliser in `GL_N(F)` of the line of the first basis vector. The
transfer of `l ∘ firstEntry` to `GL_N(F)` is `l ∘ det`. 

### `residueUnit`

 The reduction of a unit of `O_w` as a unit of the residue field, and `1` for the other elements
of `E_w`. 

### `eq_residueUnit`

 A unit `x` of the residue field `ResField w` that is the reduction of a local integer
`y : LocInt w` equals `residueUnit z`, where `z : LocField w` is `y` seen in `E_w`. 

### `reduceGL_mem_iff_mem_residuePreimage`

 The reduction of `g ∈ GL_N(O_w)` lies in a subgroup `H` if and only if `g` lies in the open
subgroup `residuePreimage P H hP`, for any property `P` that describes the preimage of `H`. 

### `reduceGL_mem_residueLineStabilizer_iff`

 The reduction of `g ∈ GL_N(O_w)` stabilises the line of the first basis vector if and only if
`g` lies in the parahoric subgroup with blocks of sizes `1` and `N - 1`. 

### `firstEntry_reduceGL`

 If the reduction of `g ∈ GL_N(O_w)` stabilises the line of the first basis vector, then its
first entry is the reduction of the first entry of `g`. 

### `det_reduceGL`

 The determinant of the reduction of `g ∈ GL_N(O_w)` is the reduction `residueUnit` of the
determinant of `g`, a unit of `O_w`. 

### `det_firstEntry_reduceGL_eq_one_of_mem_proIwahori`

 If `g ∈ GL_N(O_w)` lies in the pro-`p` Iwahori subgroup (its reduction is upper triangular with
ones on the diagonal), then the reduction has determinant `1` and first entry `1`. 

### `exists_residue_log`

 Let `q = w.q` be the order of the residue field at `w`, let `m ∣ q - 1`, and let `z` generate
the residue units. There is a logarithm modulo `m` to the base `z`: a homomorphism from the residue
units to `ℤ/m` that sends `z` to `1`. 


## Logarithms


### `map_eq_of_weights_modEq`

 If `m = 0` in `S`, then only the weights modulo `m` matter: an additive map `B` on integer
weights takes weights that are congruent modulo `m` to elements with the same image under `σ`. 

### `weightedSum`

 The weighted norm `∑ f (c g) ρ g` for a homomorphism `c : Γ → ℤ/m`, as an additive function of
the weight `f : ℤ/m → ℤ`. The weight `1` gives the norm; the weight `valMinAbs`, which lifts
`ℤ/m` to `ℤ`, gives the logarithm of `c`. 

### `mul_weightedSum`

 Left multiplication by `ρ g` shifts the weight of the weighted norm `∑ f (c h) ρ h` by
`c g`. 

### `weightedSum_mul`

 Right multiplication by `ρ g` shifts the weight of the weighted norm `∑ f (c h) ρ h` by
`c g`. 

### `cosetNorm`

 The sum `∑ ρ h` over the fixed representatives `h` of `Γ / H`, namely the elements `η.out` that
`Quotient.out` chooses in the cosets `η`. 

### `cosetNormInv`

 The sum `∑ ρ h⁻¹` over the fixed representatives `h` of `Γ / H`. A sum `∑ f p ρ p` over `H`,
times this sum, is the sum over `Γ` in which `ρ (p h⁻¹)` has the weight `f p`. 

### `cosetDerivative`

 The derivative `∂ = -(∑ ρ h) B(valMinAbs) (∑ ρ h⁻¹)` attached to an additive map `B` on weights
`ℤ/m → ℤ`, where `h` runs over the fixed representatives of `Γ / H`. For the weighted norm `B` of a
homomorphism `a : H → ℤ/m`, the middle factor is the logarithm of `a`. 

### `cosetComponent`

 The element `p ∈ H` with `g x = h p`, where `h` is the fixed representative of the coset
`g x H`. 

### `cosetNorm_mul_sum_mul`

 Let `ρ` be a multiplicative map from a finite group `Γ` to a ring `R`, let `H` be a subgroup,
and let `h` run over the representatives `η.out` that `Quotient.out` chooses for the cosets
`η ∈ Γ / H`, so that `cosetNorm ρ H = ∑ ρ h`. For a weight `f : H → ℤ` and `x ∈ Γ`, the product
`(∑ ρ h) (∑_{p ∈ H} f p ρ p) ρ x⁻¹` is the sum over `g ∈ Γ` of `f p ρ g` with
`p = cosetComponent H g x`, the element of `H` in the unique factorisation `g = h p x⁻¹`. 

### `transfer_eq_prod_cosetComponent`

 The transfer of `a : H → A` at `g` is the product, over the fixed representatives `h` of
`Γ / H`, of the values of `a` at the components `p ∈ H` of `g h = h' p`. 

### `map_cosetNorm_mul_weightedSum_mul_cosetNormInv`

 Let `ρ` map the finite group `Γ` to the ring `R`, and let `σ : R → S` be a ring map with `m = 0`
in `S`. For a homomorphism `c` to `ℤ/m` let `L c = ∑ valMinAbs (c g) ρ g` be its logarithm, the
`weightedSum` for the lift `valMinAbs : ℤ/m → ℤ`. For `a : H → ℤ/m` on a subgroup `H`, the elements
`(∑ ρ h) (L a) (∑ ρ h⁻¹)` and `L a.transfer` have the same image under `σ`, where `h` runs over the
fixed representatives of `Γ / H` and `a.transfer` is the transfer of `a` from `H` to `Γ`. 

### `map_sub_one_mul_weightedSum_valMinAbs`

 Let `ρ` map the finite group `Γ` to the ring `R`, and let `σ : R → S` be a ring map with `m = 0`
in `S`. Let `L = ∑ valMinAbs (c g) ρ g` be the logarithm of a homomorphism `c : Γ → ℤ/m` that sends
`γ` to the generator `1`. Then `(ρ γ - 1) L` and `-∑ ρ g` have the same image under `σ`. 

### `exists_map_valMinAbs_mul_sub_one`

 Let `ρ` map the finite group `Γ` to the ring `R`, and let `σ : R → S` be a ring map with `m = 0`
in `S`. Let `a : H → ℤ/m` be a homomorphism on a subgroup `H`. Let `B` be an additive map on weights
`ℤ/m → ℤ` such that right multiplication by `ρ p` shifts the weight by `a p`, as for the weighted
norm over `H` or a fixed left multiple of it. Then `B valMinAbs * (∑ ρ h⁻¹) * (ρ g - 1)` has the
same image under `σ` as a right multiple `B 1 * Q` of the value of `B` at the constant weight `1`.
Here `valMinAbs` is the weight sending `x` to its representative in `ℤ` of least absolute value, and
`h` runs over the fixed representatives of `Γ / H`. 

### `map_valMinAbs_eq_zero_of_shift`

 Let `σ` be a reduction modulo `m / (2 k)`, that is, let it kill every `x` with `2 k x ∈ m R`.
If an additive map `C` on weights `ℤ/m → ℤ` kills every `f (· - k) - f`, then `σ` kills its value
at the weight `valMinAbs`. 

### `exists_map_nsmul_mul_sub_one_eq_sum_mul`

 Let `ρ` map the finite group `Γ` to the ring `R`, and let `σ : R → S` be a ring map with `m = 0`
in `S`. Let `a : H → ℤ/m` be a homomorphism on a subgroup `H`, let `B` be an additive map on weights
`ℤ/m → ℤ` such that right multiplication by `p ∈ H` shifts the weight by `a p`, and let
`∂ = cosetDerivative ρ H B` be `-(∑ h) B(valMinAbs) (∑ h⁻¹)`, with `h` running over the fixed
representatives of `Γ / H`. Let `H` fix `B 1` from the left, let `∑ p⁻¹ Ψ p = n` over `H`, and let
`L g = L` for all `g` and `L (B 1) = 0`. If `R` has no `#H`-torsion, then `n ∂ (g - 1) ≡ Nm Z` for
some `Z` with `L Z = 0`. 
