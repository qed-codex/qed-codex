---
{
  "module": "Zeta23/ZeroSide.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ZeroSide.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ZeroSide.lean — paper §4 "The zero side: signature and rank", Block structure + prop:block.
Builds on the §3 formalization (Zeta23.LinAlg, namespace RHLinalg): posIndex, posIndex_add_le
(subadditivity, the corollary of lem:inertia), Sylvester's subspace characterization,
posIndex_eq_rank_of_posSemidef.

Reference text: the paper, labels [eq:AE], [eq:Ncount], [eq:hatunits], [prop:block].

Design: this file is ζ-free. Section 1 is generic Hermitian-matrix
lemmas missing from Mathlib/RHLinalg. Section 2 proves prop:block for an ABSTRACT finite
zero configuration `ZeroBlockData` (distinct points z with explicit multiplicities m z ≥ 1,
the involution σ = (ρ ↦ 1 − conj ρ) with m ∘ σ = m, and evaluation vectors v z = (φ̂(γ_z − τ_k))_k with
v (σ z) = conj ∘ v z). Section 3 instantiates from Defs.lean's ZeroConfig, φ̂, τ_k, a, L and
lem:poisson.
-/
```

 ## Section 1. Generic lemmas on rank and positive index 

### `rank_add_le`

 `rank (A + B) ≤ rank A + rank B` for matrices (Mathlib has this only for linear maps). 

### `rank_sum_le`

 Rank of a finite sum is at most the sum of given rank bounds. 

### `rank_smul_vecMulVec_le`

 A scalar multiple of a rank-one matrix `w vᵀ` has rank at most one. 

### `posIndex_le_rank`

 The positive index is at most the rank: `#{λᵢ > 0} ≤ #{λᵢ ≠ 0}`. 

### `posIndex_eq_zero_of_hermForm_nonpos`

 If the Hermitian form of `A` is nonpositive everywhere then `n₊(A) = 0`. 

### `posIndex_neg_eq_zero_of_posSemidef`

 `n₊(−N) = 0` for `N ⪰ 0`. 

### `posIndex_sub_le_rank`

 `n₊(P − N) ≤ rank P` for `P, N ⪰ 0`: subadditivity (lem:inertia) plus `n₊(P) = rank P`, `n₊(−N) = 0`. 

### `posIndex_smul_pos`

 The positive index is invariant under multiplication by a positive real scalar. 

### `rank_smul_of_ne_zero`

 Rank is invariant under multiplication by a nonzero scalar. 

 ## Section 2. The abstract block structure (paper §4: [eq:AE], Block structure, [eq:Ncount], [prop:block])

Paper §4, Block structure, verbatim: "Let 𝒵(I') be the set of distinct zeros with γ ∈ I'. Classify its
points as follows: 𝒮₁: β = ½ and m_ρ = 1 (simple zeros on the line); s₁ := #𝒮₁; 𝒮₂: β = ½ and
m_ρ ≥ 2; s₂ := #𝒮₂; 𝒫: unordered pairs {ρ, 1−ρ̄} with β ≠ ½ (both members lie in 𝒵(I'), they are
distinct points, and m_{1−ρ̄} = m_ρ); p := #𝒫. Thus #𝒵(I') = s₁+s₂+2p and, counting with
multiplicity, N(I') = Σ_{𝒮₁} 1 + Σ_{𝒮₂} m_ρ + Σ_{𝒫} 2m_ρ ≥ s₁+2s₂+2p. [eq:Ncount]
Write N_on(I') := Σ_{ρ∈𝒮₁∪𝒮₂} m_ρ, so that also N(I') ≥ N_on(I') + 2p."

We encode 𝒵(I') as a finite index type ι, the grid {0,…,d−1} as a finite type d, and carry:
multiplicities m (≥ 1, explicit — zeros are DISTINCT points), the involution σ = (ρ ↦ 1−ρ̄)
restricted to 𝒵(I') (it preserves the ordinate, hence 𝒵(I')), and the evaluation vectors
u_ρ = (φ̂(γ_ρ − τ_k))_{k<d} ∈ ℂ^d with u_{1−ρ̄} = conj u_ρ (from γ_{1−ρ̄} = conj γ_ρ, τ_k ∈ ℝ, and
conj φ̂(z̄) = φ̂(z) [subsec:family after eq:fk]). On-line ⟺ β = ½ ⟺ σ ρ = ρ.


### `ZeroBlockData`

 Abstract zero-side data of the window 𝒵(I') [§4 Block structure]: distinct points z : ι with
explicit multiplicity `m z ≥ 1`, evaluation vectors `v z = (φ̂(γ_z − τ_k))_k`, and the involution
`σ = (ρ ↦ 1 − ρ̄)` with `m ∘ σ = m` and `v (σ z) = conj ∘ v z`. 

### `ZeroBlockData.m`

 multiplicity m_ρ of the distinct zero ρ 

### `ZeroBlockData.v`

 evaluation vector u_ρ := (φ̂(γ_ρ − τ_k))_{0 ≤ k < d} 

### `ZeroBlockData.σ`

 ρ ↦ 1 − ρ̄ on 𝒵(I') 

### `ZeroBlockData.m_σ`

 m_{1−ρ̄} = m_ρ 

### `ZeroBlockData.v_σ`

 u_{1−ρ̄} = conj u_ρ 

### `onLine`

 𝒮₁ ∪ 𝒮₂: on-line points (β = ½ ⟺ fixed by ρ ↦ 1−ρ̄). 

### `S₁`

 𝒮₁: on-line and simple (m_ρ = 1). 

### `S₂`

 𝒮₂: on-line with m_ρ ≥ 2. 

### `s₁`

 s₁ := #𝒮₁ 

### `s₂`

 s₂ := #𝒮₂ 

### `Ncount`

 N(I') = Σ_{ρ ∈ 𝒵(I')} m_ρ (with multiplicity) [eq:Ncount]. 

### `Non`

 N_on(I') := Σ_{ρ ∈ 𝒮₁ ∪ 𝒮₂} m_ρ. 

### `PairReps`

 A choice of one representative from each off-line pair {ρ, 1−ρ̄} ∈ 𝒫; `p := #R`.
(At instantiation: R = the members with β > ½.) 

### `PairReps.p`

 p := #𝒫, the number of off-line pairs. 

### `pairRepsOfLinearOrder`

 Representatives always exist (pick the smaller member of each pair in any linear order). 

### `sum_split`

 Splitting a sum over 𝒵(I') = 𝒮₁ ∪ 𝒮₂ ∪ ⋃𝒫 into on-line points and pairs. 

### `card_eq_onLine_add`

 #𝒵(I') = #(𝒮₁∪𝒮₂) + 2p. 

### `card_onLine`

 #(𝒮₁ ∪ 𝒮₂) = s₁ + s₂. 

### `card_eq`

 "#𝒵(I') = s₁ + s₂ + 2p" [§4 Block structure]. 

### `s₁_add_two_s₂_le_Non`

 N_on(I') ≥ s₁ + 2 s₂ (since m_ρ = 1 on 𝒮₁ and m_ρ ≥ 2 on 𝒮₂). 

### `Non_add_two_p_le_Ncount`

 "N(I') ≥ N_on(I') + 2p" [§4, after eq:Ncount]. 

### `s₁_add_two_s₂_add_two_p_le_Ncount`

 [eq:Ncount]: "N(I') = Σ_{𝒮₁} 1 + Σ_{𝒮₂} m_ρ + Σ_{𝒫} 2m_ρ ≥ s₁ + 2s₂ + 2p". 

 ### The matrix A [eq:AE] and its decomposition 

### `blockA`

 A_{kl} := Σ_{ρ : γ ∈ I'} m_ρ φ̂(γ_ρ − τ_k) φ̂(γ_ρ − τ_l)  [eq:AE]; i.e. A = Σ_ρ m_ρ u_ρ u_ρᵀ
(transpose, NOT conjugate-transpose). 

### `star_v_of_onLine`

 u_ρ is a real vector for ρ on the line. 

### `blockA_isHermitian`

 "A is real symmetric (same argument as for G: conjugation permutes the summands via ρ ↦ 1−ρ̄)". 

### `star_blockA_apply`

 Every entry of A is real. 

### `xv`

 real part vector x_ρ := Re u_ρ (as a complex vector) 

### `yv`

 imaginary part vector y_ρ := Im u_ρ (as a complex vector) 

### `pair_term`

 The pair block: m(u uᵀ + ū ūᵀ) = 2m(x xᵀ − y yᵀ) for u = x + iy. 

### `onPart`

 the on-line part Σ_{ρ∈𝒮₁∪𝒮₂} m_ρ u_ρ u_ρᵀ 

### `rePart`

 Σ_𝒫 2m_ρ x_ρ x_ρᵀ 

### `imPart`

 Σ_𝒫 2m_ρ y_ρ y_ρᵀ 

### `blockA_decomp`

 A = (on-line part) + (Σ_𝒫 2m x xᵀ − Σ_𝒫 2m y yᵀ). 

### `posSemidef_smul_vecMulVec`

 c • x xᵀ ⪰ 0 for a real vector x and real c ≥ 0. 

### `rank_blockA_le`

 "A is a sum of #𝒵(I') matrices of rank one" ⟹ rank A ≤ #𝒵(I') [prop:block (i)]. 

### `posIndex_blockA_le`

 **prop:block (i), positive index**: "n₊(Ã) ≤ s₁ + s₂ + p" — stated for A itself; positive
scalings (Ã = A/L, Â = A/(aL²)) do not change n₊, see `posIndex_smul_pos`. Paper proof: pull-back of
the direct sum of s₁+s₂ positive 1×1 forms and p hyperbolic 2×2 forms under the evaluation map,
lem:inertia. Lean proof: the same inertia bound via subadditivity (RHLinalg.posIndex_add_le, the
paper's stated corollary of lem:inertia) applied to A = P₀ + (X − Y) with P₀ = Σ_on m u uᵀ ⪰ 0 of
rank ≤ s₁+s₂ and X = Σ_𝒫 2m x xᵀ ⪰ 0 of rank ≤ p, Y ⪰ 0 (each hyperbolic block m(uuᵀ+ūūᵀ) =
2m(xxᵀ − yyᵀ)). 

### `posIndex_smul_blockA_le`

 prop:block (i) for any positive multiple r•A (Ã = A/L: "Dividing by L > 0 changes nothing"). 

### `rank_smul_blockA_le`

 prop:block (i), rank, for any nonzero multiple: "rank(Ã) ≤ s₁ + s₂ + 2p = #𝒵(I')". 

 ### prop:block (ii): Â = P + Q in the units [eq:hatunits] 

### `blockP`

 P := (aL²)⁻¹ Σ_{ρ ∈ 𝒮₁∪𝒮₂} m_ρ u_ρ u_ρᵀ  [prop:block proof of (ii)], with c := aL². 

### `blockQ`

 Q := Â − P, "the sum of the pair contributions". 

### `blockP_add_blockQ`

 Â = P + Q where Â := A/(aL²) [eq:hatunits] (here: c⁻¹ • A with c = aL²). 

### `blockP_posSemidef`

 "P is … positive semidefinite". 

### `star_blockP_apply`

 "P is real symmetric": Hermitian with real entries. 

### `rank_blockP_le`

 "of rank ≤ s₁ + s₂". 

### `rtrace_onPart`

 tr(m u uᵀ) for real u: m Σ_k u_k² = m ‖u‖². 

### `rtrace_blockP_le`

 "by Lemma [lem:poisson], tr P = (aL²)⁻¹ Σ m_ρ Σ_{0≤k<d} φ̂(γ_ρ−τ_k)² ≤ (aL²)⁻¹ Σ m_ρ Σ_{k∈ℤ}
φ̂(γ_ρ−τ_k)² = N_on(I')". The Poisson input enters ONLY as the hypothesis `hPois`: for each on-line
ρ ∈ 𝒵(I'), Σ_{0≤k<d} |φ̂(γ_ρ − τ_k)|² ≤ c = aL² (finite partial sum of the nonnegative series whose
full sum over k ∈ ℤ is exactly aL² by lem:poisson). 

### `blockQ_isHermitian`

 Q is Hermitian (real symmetric). 

### `star_blockQ_apply`

 Every entry of Q is real. 

### `posIndex_blockQ_le`

 **prop:block (ii)**: "n₊(Q) ≤ p" — "The form c ↦ c*Qc is the pull-back under 𝒜 of the direct
sum of the p hyperbolic blocks alone, so n₊(Q) ≤ p by Lemma [lem:inertia]". 

 ## Section 3. Instantiation against Zeta23.Defs: 𝒵(I') ⊂ ZeroConfig, A = Z.Az P T  [eq:AE]

Here ι := 𝒵(I') = Z.ZIprime T (finite by ZeroConfig.finite_window), d := Fin (P.d T),
m := Z.mult, σ := reflect = (ρ ↦ 1 − conj ρ), v ρ k := φ̂(γ_ρ − τ_k) with γ_ρ = gammaOf ρ, τ_k = P.tau T k.
The analytic inputs are explicit hypotheses of this section (discharged elsewhere in the
repository from Zeta23.Taper / Zeta23.Poisson: Params.phiHat_conj, Params.phiHat_ofReal,
Params.hasSum_phiHatR_sq):
  hconj : ∀ z, φ̂(conj z) = conj φ̂(z)                       [subsec:family, after eq:fk]
  hreal : ∀ r : ℝ, φ̂(r) = φ̂_ℝ(r) (φ̂ real on ℝ)
  hPois : ∀ γ : ℝ, HasSum (k ↦ φ̂(γ − τ_k)²) (aL²)            [lem:poisson, "in particular"]


### `ZI`

 𝒵(I') as a Finset of ℂ. 

### `reflect_eq_self_iff`

 fixed points of ρ ↦ 1 − ρ̄ are exactly the points with β = 1/2 

### `gammaOf_reflect`

 γ_{1−ρ̄} = conj γ_ρ. 

### `gammaOf_of_re_eq_half`

 For ρ on the line, γ_ρ = γ = Im ρ is real. 

### `mkData`

 Block data of 𝒵(I') with an arbitrary σ-equivariant family of vectors v (the counting facts do
not depend on v; the matrix facts use v ρ = (φ̂(γ_ρ − τ_k))_k). 

### `mkPairReps`

 Canonical representatives of the off-line pairs: the member with β > 1/2. 

### `card_offLine_eq_mk`

 #offLine = 2p. 

### `zeroVec`

 the zero family of vectors (for the v-independent counting statements) 

### `ncard_ZIprime_eq`

 **"#𝒵(I') = s₁ + s₂ + 2p"**  [§4 Block structure] (Defs' provisional p := #offLine/2). 

### `ncard_offLine_eq`

 #offLine(I') = 2p: Defs' p := ncard(offLine)/2 loses nothing. 

### `s1_add_two_s2_add_two_p_le_NIprime`

 **[eq:Ncount]** "N(I') = Σ_{𝒮₁}1 + Σ_{𝒮₂}m_ρ + Σ_{𝒫}2m_ρ ≥ s₁ + 2s₂ + 2p". 

### `NonIprime_add_two_p_le_NIprime`

 **"N(I') ≥ N_on(I') + 2p"** [§4, after eq:Ncount]. 

 ### The matrix A = Z.Az P T and prop:block for Ã := P.tilde T A, Â := P.hat T A 

### `PhiHatConj`

 Hypothesis shape: conj φ̂(z̄) = φ̂(z) [subsec:family after eq:fk]; = Params.phiHat_conj (Taper.lean). 

### `PhiHatReal`

 Hypothesis shape: φ̂ is real on ℝ; = Params.phiHat_ofReal (Taper.lean). 

### `PoissonSq`

 Hypothesis shape: lem:poisson "in particular Σ_{k∈ℤ} φ̂(γ−τ_k)² = aL²" for real γ;
= Params.hasSum_phiHatR_sq (Poisson.lean). 

### `evalVec`

 the evaluation vectors u_ρ := (φ̂(γ_ρ − τ_k))_{0≤k<d}  [prop:block proof] 

### `evalVec_reflect`

 u_{1−ρ̄} = conj u_ρ (from γ_{1−ρ̄} = conj γ_ρ, τ_k ∈ ℝ, φ̂(conj w) = conj φ̂(w)). 

### `blockData`

 The block data of 𝒵(I') [eq:AE]: m := Z.mult, u_ρ := (φ̂(γ_ρ − τ_k))_{0≤k<d}, σ := ρ ↦ 1 − ρ̄. 

### `Az_eq_blockA`

 **A = Σ_{ρ∈𝒵(I')} m_ρ u_ρ u_ρᵀ**: Defs' finsum matrix Z.Az P T [eq:AE] is the abstract blockA. 

### `Az_isHermitian`

 A is Hermitian (indeed real symmetric). 

### `star_Az_apply`

 Every entry of A is real. 

### `posIndex_tilde_Az_le`

 **prop:block (i)**: "n₊(Ã) ≤ s₁ + s₂ + p" (Ã := A/L; any Hermitian-ness witness h). 

### `rank_tilde_Az_le`

 **prop:block (i)**: "rank(Ã) ≤ s₁ + s₂ + 2p = #𝒵(I')". 

### `hatP`

 P of prop:block (ii): (aL²)⁻¹ Σ_{ρ∈𝒮₁∪𝒮₂} m_ρ u_ρ u_ρᵀ. 

### `hatQ`

 Q of prop:block (ii): Â − P ("the sum of the pair contributions"). 

### `hat_Az_eq_hatP_add_hatQ`

 **prop:block (ii)**: "Â = P + Q" with Â := A/(aL²) [eq:hatunits]. 

### `hatP_posSemidef`

 **prop:block (ii)**: "P ⪰ 0". 

### `star_hatP_apply`

 **prop:block (ii)**: P "real symmetric" — real entries (Hermitian from hatP_posSemidef). 

### `rank_hatP_le`

 **prop:block (ii)**: "rank P ≤ s₁ + s₂". 

### `sum_normSq_v_le`

 The finite Poisson bound for an on-line zero ρ: Σ_{0≤k<d} |φ̂(γ_ρ − τ_k)|² ≤ aL²  (the terms are
≥ 0 and the full sum over k ∈ ℤ is exactly aL² by lem:poisson). 

### `rtrace_hatP_le`

 **prop:block (ii)**: "tr P ≤ N_on(I')" — "by Lemma [lem:poisson], tr P = (aL²)⁻¹ Σ m_ρ
Σ_{0≤k<d} φ̂(γ_ρ−τ_k)² ≤ (aL²)⁻¹ Σ m_ρ Σ_{k∈ℤ} φ̂(γ_ρ−τ_k)² = N_on(I')". 

### `hatQ_isHermitian`

 **prop:block (ii)**: Q is Hermitian. 

### `star_hatQ_apply`

 **prop:block (ii)**: Q "real symmetric" — real entries. 

### `posIndex_hatQ_le`

 **prop:block (ii)**: "n₊(Q) ≤ p" (by lem:inertia), for any Hermitian-ness witness h. 

 ## Section 4. Packaging for Assembly: `Zeta23.Assembly.BlockInputs` 

### `blockInputsAt`

 prop:block (i)+(ii) and [eq:Ncount] at height T, packaged exactly as `Assembly.thmA_abstract`
consumes them (p := Z.p T), from the explicit analytic hypotheses. See Zeta23/ZeroSide/Final.lean
for the version with the hypotheses discharged from Taper/Poisson. 

 ### The export for Main.lean: eventually-in-T form with only the genuinely external inputs left

hconj / hreal are discharged here from Zeta23.GzGp.phiHat_conj / phiHat_ofReal
(φ real and even); 0 < L eventually since L = λ·log(T/2π) → ∞. What remains as hypotheses, both in
∀ᶠ form: positivity of a [eq:abdef] (Main has it from Taper: 1 − 2w/L ≤ b ≤ a) and lem:poisson
(Zeta23.Poisson: Params.hasSum_phiHatR_sq). Zeta23/ZeroSide/Final.lean discharges those two as well. 

### `tendsto_L_atTop'`

 L = λ·log(T/2π) → ∞ as T → ∞ (for λ > 0). 

### `eventually_blockInputs_of`

 **Export consumed by Main.lean**: prop:block + [eq:Ncount], eventually
in T, modulo only (ha) a > 0 eventually and (hPois) lem:poisson eventually. 
