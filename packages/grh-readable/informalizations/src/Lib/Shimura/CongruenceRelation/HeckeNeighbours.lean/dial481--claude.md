---
{
  "module": "src/Lib/Shimura/CongruenceRelation/HeckeNeighbours.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/HeckeNeighbours.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/HeckeNeighbours.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke elements on adelic torsion and reductions of Frobenius twists of Hecke neighbours

Fix a split place `w` of the CM field `E` and a subspace `C` of `(𝓞 / w)ⁿ`, and let `q` be the order
of the residue field. This file describes how the Hecke element `New.Variety.invHeckeIsogeny w C`
acts on the torsion module `New.AdelicTorsion E n`, which is `(𝔸_f / Ô)ⁿ`. These computations are
combined with Frobenius-twisted reductions of linear maps to prove
`New.Variety.UniversalFamily.exists_ne_bot_factorsThrough_sup`. This result is the geometric step
behind the congruence relation at `w`.

## Main definitions and results

* `New.Variety.exists_residue_torsion_emb`: the `w`-torsion is `(𝓞 / w)ⁿ`, compatibly with integral
  matrices.
* `New.Variety.frobeniusTwist`: the absolute Frobenius of a `k`-scheme, as a map between its two
  structures over `V`.
* `New.Variety.IsTwistedReduction`: a map between reductions is the reduction of a map `ψ` twisted
  by a Frobenius.
* `New.Variety.IsTwistedReduction.exists_comp_eq_smul`: a multiple of one twisted reduction factors
  through another.

Notions from other files:
* `New.Variety.invHeckeIsogeny`: For a subspace U of k_wⁿ of dimension r, the product of a central
  factor, the conjugate of N(ϖ_w)^(−r) with N the norm from E to ℚ(√−d₀), and a unitary local
  factor, which is (`New.basicCosetRep` U)⁻¹ at w and 1 away from w and w̄.
* `New.basicCosetRep`: For a subspace U of k_wⁿ of dimension r, a matrix in the double coset of
  diag(ϖ 1_r, 1) in GL_n(E_w) whose reduction modulo w has kernel U.
* `New.Variety.SplitFinPlace`: The finite places w of E with w̄ ≠ w, that is, those split over the
  maximal real subfield.
* `New.Variety.IsSafe`: The place u of ℚ(√−d₀) below w contains some (1 + √−d₀)/2 − b coprime to its
  conjugate (so u is split), and the level 𝔑 lies neither in w nor in a place above ū.

## Relation to the literature

Known result: Pointwise step of the Eichler–Shimura congruence relation for GU(1,n−1) at a split
place. Only the geometric step is treated here, and it uses no ordinary locus. At each geometric
point of the special fibre, the Frobenius-twisted Hecke neighbour of a subspace depends only on its
sum with one fixed non-zero subspace. Source: Wedhorn, Congruence relations on some Shimura
varieties, J. reine angew. Math. 524 (2000) 43–71; the method follows Katz–Mazur 1985 ch. 13 and
Harris–Taylor 2001 III.4.


 ## The w-torsion and the action of Hecke elements on adelic torsion 

### `exists_residue_torsion_emb`

 The `w`-torsion of `(𝔸_f / Ô)ⁿ` is a copy of `(𝓞 / w)ⁿ`, and an integral matrix kills a
torsion point exactly when its reduction modulo `w` kills the corresponding vector. 

### `smul_torsionClass_eq_zero_iff`

 An integer `a` of `E` kills the class of `v` in `(𝔸_f / Ô)ⁿ` exactly when
`|a|_u · |v i|_u ≤ 1` for every coordinate `i` and every finite place `u`. 

### `invHeckeIsogeny_inv_at_eq_basicCosetRep`

 If `w` is safe for `I`, then at `w` the inverse of the Hecke element `invHeckeIsogeny w C` is
the matrix `basicCosetRep C`. 

### `invHeckeIsogeny_inv_mulVec_of_ne`

 The inverse Hecke element acts trivially at the places other than `w` that do not lie above the
conjugate of the place below `w`. 

### `isScalarFrame_invHeckeIsogeny`

 The Hecke element `g = invHeckeIsogeny w C` is a frame for the scalar form `q ^ dim C`: the
matrix `q ^ dim C • gᴴ g` is a scalar unit of the profinite integers. 

### `torsionClass_inv_mulVec_eq_of_mem_levelTorsion`

 If `w` is safe for the level `𝔑` and the class of `v` is killed by `𝔑`, then the inverse of
the Hecke element `New.Variety.invHeckeIsogeny w C` fixes the class of `v`. 

### `mem_torsionBySet_of_pow_smul_eq_zero_of_torsionClass_inv_mulVec_eq_zero`

 Let `E` be a CM field containing `ℚ(√-d₀)`, with `D.β` the image of `betaK d₀ = (1 + √-d₀)/2`.
Let `w` be a split finite place of `E` that is safe for the level `D.level` (`IsSafe`: the place of
`ℚ(√-d₀)` below `w` is split and prime to the discriminant, and `𝔑` lies neither in `w` nor in any
place above the conjugate place), and let `b` be an integer with `β - b ∈ w` coprime to
`star β - b`. For a vector `v` of finite adeles and a subspace `C` of `k_wⁿ` (`k_w` the residue
field at `w`), suppose `(β - b) ^ N` kills the class `torsionClass v` in `(𝔸f E / Ô E)ⁿ`, and the
inverse of the Hecke matrix `invHeckeIsogeny w C` attached to `C` sends `v` to a vector of class
`0`; then the ideal `w` kills `torsionClass v`. 


## Reductions of Frobenius twists of Hecke neighbours

Take a point of level one over a valuation subring of ℂ. Let w be the split place below its
reduction to an algebraically closed residue field, good for `D` and safe. The point has one Hecke
neighbour for each subspace A of k_wⁿ. Reduce it to that field and twist by the Frobenius of
exponent q ^ (n - dim A). Under a further condition on `D.β`, for some nonzero subspace W, the
result depends only on A + W.


 ### Counting fibres, torsion bounds and Frobenius on residue fields 

### `mul_card_preimage_singleton`

 For a homomorphism `Φ` from a finite group `G`, `n` times the number of elements of the fibre
of `Φ` over `a` is `n * |G| / |Φ.range|` if `a` is in the range of `Φ`, and `0` otherwise. 

### `q_pow_smul_torsionClass_eq_zero`

 A torsion class killed by `(invHeckeIsogeny w C)⁻¹` is killed by `q ^ dim C`, where `q` is the
norm of `w`. 

### `pow_smul_conj_pow_smul_eq_zero`

 If `D.β - b` vanishes in a field of characteristic `l`, then `l ^ n` divides the `n`-th power
of its norm `(D.β - b) * (star D.β - b)`, so that power kills the `l ^ n`-torsion. 

### `iterateFrobenius_comp_eq_of_ker_eq`

 Raising to a power of the norm `q` of `w` fixes the residue field of `w`, so it does not
change a ring map with kernel `w`. 

### `comp_nsmul_id_eq_zero_of_torsionPoint`

 The torsion sections are dense in the kernel of an isogeny `ψ`, so a number `μ` that kills the
torsion sections of the kernel kills all its points. 

### `torsionPoint_comp_eq_of_mem_levelTorsion`

 If `ψ` acts on torsion sections by `(invHeckeIsogeny w C)⁻¹` and `w` is safe for the level,
then `ψ` respects the level points. 

### `nsmul_eq_zero_of_torsionPoint_comp_eq_zero`

 If `ψ` acts on torsion sections by `(invHeckeIsogeny w C)⁻¹`, then `q ^ dim C` kills each
torsion class whose section `ψ` kills, where `q` is the norm of `w`. 

### `mem_torsionBySet_of_pow_smul_eq_zero_of_torsionPoint_comp_eq_zero`

 Let `ψ` act on torsion sections by `(invHeckeIsogeny w C)⁻¹`, with `w` safe for the level and
`D.β - b ∈ w` coprime to its conjugate. A torsion class killed by a power of `D.β - b` whose
section `ψ` kills is `w`-torsion. 

### `torsionPoint_comp_of_heckeIsogeny`

 Let `ψ` act on torsion sections by `(invHeckeIsogeny w C)⁻¹`, with `w` safe of norm `q` and
`D.β - b ∈ w` coprime to its conjugate. Then `ψ` respects the level points, `q ^ dim C` kills the
torsion of its kernel, and the part of that torsion killed by a power of `D.β - b` is
`w`-torsion. 

### `torsionPoint_comp_eq_zero_iff_mem`

 Let `σ : k_wⁿ → (𝔸_f / Ô)ⁿ` be `𝓞 E`-linear, with `σ v` the class of the adelic vector
`rep v`, such that an integral matrix kills `σ v` exactly when its reduction at `w` kills `v`. If
`ψ` acts on torsion sections by `(invHeckeIsogeny w C)⁻¹` and `w` is safe, then `ψ` kills the
torsion section of `σ v` exactly when `v ∈ C`. 

### `pairing_smul_eq_of_comp_eq_smul`

 Let `g` and `g'` be linear isogenies with the same source and the same multiplier `μ`. A map `j`
with `g ≫ j = c • g'` satisfies `⟨c • u, g v⟩ = ⟨j u, g' v⟩`, where `⟨·,·⟩` is the pairing
`picClass.pairing` of the line bundle class of `x`, resp. `x'`. 

### `exists_factor_of_conj_pow_smul_factors`

 Let `g : x₀ ⟶ x` and `g' : x₀ ⟶ x'` be linear isogenies of objects over an algebraically closed
field `k` with multiplier `μ` (`E` is the CM field of the datum `D`), `x` rigid, and let `l ^ n`
kill the kernel of `g'`. If `(star D.β - b) ^ n` times each of `g`, `g'` factors through the other,
and `D.β - b` is coprime to its conjugate, then `g` itself factors through `g'`. 

### `eq_of_comp_eq_of_pull_picClass_eq`

 Let `g : x₀ ⟶ x`, `g' : x₀ ⟶ x'` be linear isogenies of objects over an algebraically closed
field `k` with the same multiplier (`E` is the CM field of the datum `D`), `x'` rigid, and
`g' ≫ j = g`. If `x` and `x'` have the same map `𝓞 E → k` and `j` respects the level points, then
`x' = x` and `j` respects the maps to the family. 

### `frobeniusTwist`

 The absolute Frobenius `t ↦ t ^ l ^ f` of a `k`-scheme, as a map over `V` between its two
structures given by `π` followed by the Frobenius of `k` and by `π`. 

### `IsTwistedReduction`

 Let `x₀` be the reduction of `y` along `π`, and `x` that of `y'` along `π` followed by the
Frobenius `t ↦ t ^ l ^ f`. The map `g : x₀ → x` is the reduction of `ψ : y → y'` twisted by that
Frobenius. 

### `IsTwistedReduction.pointEquiv_comp`

 On points, `g` is the Frobenius followed by `ψ`. 

### `IsTwistedReduction.isLinear`

 The map `g` is `𝓞 E`-linear. 

### `IsTwistedReduction.pullSection_comp`

 The map `g` sends the reduction of a section `a` to the reduction of `ψ a`. 

### `exists_isTwistedReduction`

 A linear map `ψ : y ⟶ y'` over `V` has a twisted reduction: a map `g : x₀ ⟶ x` between the
reductions of `y` and `y'` that is the reduction of `ψ` twisted by the Frobenius `t ↦ t ^ l ^ f`
(`New.Variety.IsTwistedReduction`). 

### `IsTwistedReduction.pull_picClass_eq_nsmul`

 The multiplier of the twisted reduction is that of `ψ` times `l ^ f`. Here `X` is a theta family
of the PEL datum `D`, and `x₀`, `x` are its objects over the field `k` of characteristic `l`. 

### `IsTwistedReduction.surjective`

 If `π` and `ψ` are surjective, then so is a twisted reduction `g` of `ψ`, on underlying
schemes. 

### `IsTwistedReduction.comp_nsmul_id_eq_zero`

 If `x₀` is rigid, `g` has multiplier `μ` and `μ` kills the kernel of `ψ`, then `μ` kills the
points of the kernel of `g` with values in local Noetherian rings. 

### `exists_isTwistedReduction_isIsogeny`

 Let `y`, `y'` be objects of the theta family `X` over `V`, `k` an algebraically closed field of
characteristic `l`, `ψ : y ⟶ y'` a linear isogeny with multiplier `r`, and `l ^ f * r = M` with
`M ≠ 0`. Then the reduction `x` of `y'` along `π` followed by the Frobenius `t ↦ t ^ l ^ f` has a
twisted reduction `g : x₀ ⟶ x` of `ψ`, and `g` is an isogeny with multiplier `M`. 

### `IsTwistedReduction.exists_comp_eq_smul`

 Let `X` be a theta family of the PEL datum `D` of the CM field `E`, and `k` an algebraically
closed field. Let `g`, `g'` be twisted reductions of `ψ`, `ψ'` (`hg`, `hg'`), with `D.β - b` in the
kernel of `𝓞 E → k` and coprime to its conjugate (`hb`, `h_cop`), and `c`, `c'` injective families
of torsion vectors killed by that kernel. If `υ` moves the torsion of the kernel of `ψ` into `c`,
`ψ'` kills `c'`, `(D.β - b) ^ n • υ` kills the kernel of the isogeny `g`, and `c`, `c'` have equal
numbers of sections through each `k`-point (weights `l ^ f`, `l ^ f'`), then `υ • g'` factors
through `g`. 

### `IsTwistedReduction.eq_of_conj_pow_smul_factors`

 Rigidity for two twisted reductions `g₁ : x₀ ⟶ x₁` and `g₂ : x₀ ⟶ x₂` of maps from `y` that
respect the level points: if they are linear isogenies with multiplier `l ^ n`, `l ^ n` kills the
kernel of `g₂`, `x₁`, `x₂` are rigid with the same map `𝓞 E → k`, `D.β - b` is coprime to its
conjugate (`h_cop`), and `(star D.β - b) ^ n` times each of `g₁`, `g₂` factors through the other,
then `x₂ = x₁`, and some `j : x₂ ⟶ x₁` with `g₂ ≫ j = g₁` respects the maps to the family. 

### `exists_apply_eq_conj_pow_smul_of_comp_eq_zero`

 Let `X` be a theta family of the PEL datum `D` of the CM field `E`, and `k` a field of
characteristic `l`. Let `D.β` be the image of `betaK d₀ = (1 + √-d₀)/2` (`hβ`), and let `D.β - b`
vanish under `ρ : 𝓞 E → k`. Suppose that `l ^ M` kills the torsion classes whose sections `ψ` kills,
that such a class killed by a power of `D.β - b` lies in the image of `σ`, and that `ψ` kills the
section of `σ v` exactly when `v ∈ C`. Then `(star D.β - b) ^ M` maps each torsion class whose
section `ψ` kills into `σ C`. 

### `_root_.New.PEL.IsGoodAt.exists_coprime`

 A place `w` good for `D` contains `D.β - b` for an integer `b` with `D.β - b` coprime to its
conjugate. 

### `pow_mul_sectionCount_eq_of_sup_span_eq`

 Let the torsion section of `σ t` reduce to zero at the closed point, and let
`l ^ m B * q ^ dim B` be the same for all subspaces `B` of `k_wⁿ`. If `A' ⊔ span t = A ⊔ span t`,
then the number of `v ∈ A` whose section `σ v` reduces to a given `k`-point `a`, weighted by
`l ^ m A`, equals the same number for `A'`, weighted by `l ^ m A'`. 

### `exists_comp_eq_and_eq_of_sectionCount_eq`

 The kernel and rigidity steps of `New.Variety.UniversalFamily.exists_ne_bot_factorsThrough_sup`.
Here `X` is a theta family of the PEL datum `D` of the CM field `E`, `k` is a field,
`ψ B : y ⟶ y' B` are linear isogenies respecting the level points, `g B` their twisted reductions,
isogenies with multiplier `l ^ M` onto rigid `x B`, and `σ` embeds `k_wⁿ` onto the torsion killed by
the kernel of `x₀.baseHom`, which holds `D.β - b` (`hb`, `h_cop`). Suppose `ψ B` kills the section
of `σ v` exactly when `v ∈ B`, `l ^ M` kills the torsion classes whose sections `ψ B` kills, those
among them killed by a power of `D.β - b` lie in the range of `σ`, `x₀` is rigid, and each `x B` has
the map `𝓞 E → k` of `x₀`. If `A`, `A'` have equal weighted section counts, then `x A' = x A`, and
some `j` with `g A' ≫ j = g A` respects the maps to the family. 

### `New.Variety.UniversalFamily.exists_ne_bot_factorsThrough_sup`

 The pointwise step of the congruence relation at the split place `w` below `π`, good for `D` and
safe, of norm `q`, where `π : V → k` is onto an algebraically closed field of characteristic `l`.
Here `E` contains the imaginary quadratic field ℚ(√−d₀), and `D.β` is its integer
`betaK d₀ = (1 + √−d₀)/2`. Let `x₀` reduce the object under the level-one point `s` with moduli
point `z`, and let `α A` be the Hecke neighbour of `z` given by `A ≤ k_wⁿ`, with
`l ^ m A = q ^ (n - dim A)` with `n = D.rank`. Then for some `W ≠ ⊥`, the reduction of `α A` twisted
by `t ↦ t ^ l ^ m A` depends only on `A ⊔ W`. 
