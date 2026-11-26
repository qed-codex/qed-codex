---
{
  "module": "src/Lib/PadicHodge/Limit/TraceLimit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Limit/TraceLimit.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Limit/TraceLimit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hodge–Tate jumps with bounded denominators and local conditions at limits of traces

The multiplicities of Hodge–Tate jumps can be read from traces with uniformly bounded denominators,
which lets jumps pass to `p`-adic limits of representations. These bounded denominators are used to
prove `New.GaloisRep.local_clauses_of_trace_limit`.

## Overview of this theory

One period ring `B = New.Period.Bmax` defines crystalline and potentially crystalline
representations `T` of a group `Γ` mapping to `G_p = Gal(ℚ̄_p/ℚ_p)`, such as `G_K` with `K/ℚ_p`
finite. This ring is Colmez's `B_max`, not Fontaine's `B_cris`, and their comparison is not
formalised. `B` also gives a linear Frobenius and the crystalline cocycles `Z_f(T)`. The Hodge–Tate
jumps of `T` form a multiset of integers, defined via `ℂ_p ⊗ T`.

* `New.Period.ax_mem_closure_fixedField`, `New.Period.tate_eq_zero_of_cyclotomicGp_twist`: for a
  subgroup `J` of `G_p`, `ℂ_p^J` lies in the closure of `ℚ̄_p^J`. An element of `ℂ_p(i)`, `i ≠ 0`,
  fixed by an open subgroup is `0`.
* `New.Period.IsAdmissible.of_jointly_injective`: being crystalline, or potentially crystalline,
  passes to subrepresentations of finite direct sums.
* `New.Period.crysCocycles.finrank_eq`: let `T` be a potentially crystalline `ℤ_p`-lattice with
  jumps `J`. Then `Z_f(T)` is finitely generated of rank `rk T + n · #(negative jumps)`, where `n`
  is the index of the image of `Γ` in `G_p`.
* `New.GaloisRep.local_clauses_of_trace_limit`: let `r` be a continuous Galois representation with
  non-degenerate trace form. Let its trace be a uniform limit of linear combinations of traces of
  continuous representations unramified or crystalline at a place `A`. Require finitely many
  approximations, or the same jumps for all terms. Then `r` is unramified or crystalline at `A`. Its
  jumps follow if their multiplicities are compatible with the limit. A polynomial killing an
  element `s` at `A` passes to `r`, given bounded degrees and convergence weighted by each
  coefficient.

The development proves only the parts of the standard theory that it uses: of the Ax–Sen–Tate
theorem only Ax's weaker form, and of Tate's theorem only the statement on `H⁰`. The notions below
take the place of Fontaine's admissible representations, of the Weil–Deligne representation and of
the Bloch–Kato rank formula. For local–global compatibility of automorphic Galois representations,
only the passage to limits is proved, with `r` given. Crystalline means that the invariants span
`B ⊗ T`.

In place of the Weil–Deligne representation stands `New.Period.linearFrob`. For `s ∈ Γ` and `m ∈ ℕ`,
it is a chosen `B`-linear endomorphism of `B ⊗ T`. It agrees with `φ^m s ⊗ s` on `D_pcris(T)` when
one exists, where `φ` is the Frobenius of `B`. In place of `H¹_f` stands the rank of `Z_f(T)`.

Organisation of `Lib.PadicHodge`. (1) `PeriodRings`: Ax's theorem, `A_inf`, Fontaine's map `θ`,
`B`, the period `t` of `ℤ_p(1)`, `B_dR`. (2) `TateSen`: Tate's theorem, invariants of `B_dR`.
(3) `Crystalline`: `Basic` (definitions, twists), `HodgeTateJumps`, `Regularity` (regularity of
`B`, using `Kisin`). (4) `BlochKato`: the rank, by the fundamental exact sequence; duality is in
`Lib.ClassField.LocalDuality.CrystallineDuality`. (5) `Limit`: the trace-limit theorem.

## Main definitions and results

* `New.Period.exists_uniform_trace_sum_eq_jump`: the multiplicity of one jump is `t` times a sum of
  traces with coefficients of norm at most `1`, where `t` is the same for every crystalline lattice
  with jumps in `[0, n]` and depends only on `Γ`, `n` and the jump.

Notions from other files:
* `New.GaloisRep.HasJumpsAt`: For each local datum at `A` with embedding `e` and each `g` in
  `Gal(ℚ̄_ℓ/ℚ_ℓ)`, the Hodge–Tate jumps of `r` at `g`, with multiplicity, are `J` at the embedding
  `ι_ℓ⁻¹ ∘ g⁻¹ ∘ e` of `E` in `ℂ`.
* `New.Period.IsKilledBy`: the form of `PolyKillsAt` above ℓ. For a Weil pair (s, k), with s acting
  on residues as x ↦ x^(1/ℓ^k), it says that the representation T is potentially crystalline. It
  also says that P kills the operator β = `linearFrob` on `Bmax ℓ` ⊗ T, which acts as φ^k s on the
  elements fixed by all g near 1.
* `New.Period.IsPotentiallyCrystalline`: the elements of B⊗T fixed by all g with j(g) near 1 span
  B⊗T over B.

## Relation to the literature

Known result: Limits of crystalline representations with bounded weights are crystalline. Here the
hypothesis is a uniform limit of traces with unbounded coefficients and ranks, and crystallinity is
Liu's theorem applied to the image of the group ring. The file also proves limit formulas for the
multiplicities of jumps and for killing polynomials. Source: T. Liu, Torsion p-adic Galois
representations and a conjecture of Fontaine, Ann. Sci. ENS 40 (2007) 633–674; L. Berger, Limites de
représentations cristallines, Compositio Math. 140 (2004) 1473–1498; for the passage from traces to
the image of the group ring, P. Wake, C. Wang-Erickson, Deformation conditions for
pseudorepresentations, Forum Math. Sigma 7 (2019).



## Bounded denominators of Hodge–Tate projectors for jumps in [0, n]

Here the instance `𝒥 : OverGp Γ p` gives a map from `Γ` to the absolute Galois group of `ℚ_p`.
`New.Period.IsCrystallineUpTo n ρ` says that `ρ` is crystalline with all jumps in `[0, n]`.
`New.Period.jump` is the multiplicity of a jump.


### `New.Period.exists_norm_thetaBdR_mul_le`

 Bounded denominators in `BdRPlus`. Let `R` be a coefficient ring (the integers of a finite
Galois extension of `ℚ_p` in `ℚ̄_p`) and let `e ∈ Amax` be nonzero in `BdR`. Then some
`κ ∈ BdRPlus` with `θ κ ≠ 0`, where `θ = thetaBdR : BdRPlus → ℂ_p`, has `‖θ (κ * z)‖ ≤ 1` for
every `z` such that `e • z` is the image of some `y` under the map `Amax ⊗ R → BdRPlus`. 

### `New.Period.jumpProjector`

 The diagonal matrix with entry `1` at the indices `i` with `k i = w` and `0` elsewhere: the
projector onto the coordinates of Hodge–Tate weight `w`. 

### `New.Period.sum_thetaBdR_mul_trace_eq_jump_of_isHodgeFrame`

 Trace formula for the multiplicity of a jump. Let `W · diag (t ^ k)` be a Hodge frame of `T`,
basis `ε` (`IsHodgeFrame` for `⊤`: fixed by the twisted action of `Γ`, `W` a unit over `BdRPlus`),
and `z = W · P · W⁻¹ · x`, where `P = jumpProjector w k` keeps the coordinates of weight `w`. For
`r` potentially crystalline and `ℤ_p`-linear `u` with `u (g y) = r g * u y`, `u x = 1`, the sum over
`s` of `thetaBdR (z s) * γ (trace (u (ε s)))` is the multiplicity of the jump `w` of `r` at `γ`. 

### `New.Period.map_mulVec_apply_eq_smul_of_isHodgeFrame`

 Integrality of the projection onto one jump. Let `U * Y = W · diag (t ^ k)` be a Hodge frame
(`IsHodgeFrame`) with `det Y = 1` and `U * U' = e • 1`, and let `y` over `Amax ⊗ R` map to `Y`
under `O`. Then `e` times the projection `W · P · W⁻¹ · x` onto the coordinates of weight `w`
(`P = jumpProjector w k`) is the image under `O` of `M x`, with `M = U · y · P · adj y · U'`. 

### `New.Period.exists_uniform_trace_sum_eq_jump`

 Hodge–Tate projectors of lattices with jumps in `[0, n]` have bounded denominators (`𝒥` maps `Γ`
to `Gp p` with open image). Some `t ∈ ℂ_p`, depending on `Γ`, `n`, `w` only, serves each crystalline
`T` with jumps in `[0, n]`, basis `ε`, `x ∈ T`. Some `z` has (a) `‖z s‖ ≤ 1` and (b) for potentially
crystalline `r` and `ℤ_p`-linear `u` with `u (g y) = r g * u y`, `u x = 1`,
`t * ∑ s, z s * γ (trace (u (ε s)))` is the multiplicity of the jump `w` of `r` at `γ`. 


## Goodness, jumps and killing polynomials at limits of traces

The conditions are `New.GaloisRep.IsGoodAt` (unramified off ℓ, crystalline above ℓ),
`New.GaloisRep.JumpsRelAt` (a relation on the multiplicities of the Hodge–Tate jumps) and
`New.GaloisRep.PolyKillsAt` (a polynomial kills a given element). Off ℓ these are linear relations
in the group ring, which pass to the limit because the trace form is non-degenerate
(`New.IsTraceNondeg`). Above ℓ one first bounds all jumps, so that the periods have bounded
denominators, and then reduces to such relations.


### `New.GaloisRep.eventually_trace_sub_sum_mem_closedBall`

 If the combinations of the traces of the `ρ η x` with coefficients `a η x` tend uniformly on `G`
to `b` times the trace of `r`, they do so uniformly on the group ring `ℤ_ℓ[G]`: for each `ε > 0`,
eventually along `F` the error is at most `ε` at every `y`. Representations act on the group ring
by `groupRingHom`, their linear extension; `⟨r⟩` is `r` as a `PadicRep`. 

### `New.GaloisRep.matrix_eq_zero_of_relation_of_limit`

 Linear relations pass to the limit. Let `r` have non-degenerate trace form, `F` be a proper
filter, `S` a finite set of indices `l`, and let the traces of the `ρ η x` weighted by `a * c l`
tend uniformly to `b l` times the trace of `r`. If the group ring elements `y θ l` satisfy the
relation with coefficients `c l θ x` in each `ρ θ x`, and their combination with coefficients `b l`
has a value `M` in `r` that does not depend on `θ`, then `M = 0`. 

### `New.GaloisRep.exists_periodTensorMap_eq_linearFrob`

 Let the maps `x ↦ u o x *ᵥ v` intertwine a lattice `lat` with potentially crystalline `σ o`,
let `(toGp s, k)` be a Weil pair (`s` acts on residues as `x ↦ x ^ (1 / ℓ ^ k)`), and let `y` lie in
the `Amax`-span of the invariant periods of `lat` (elements of `Amax ⊗ T` fixed by `Γ`). Then one
`y' ∈ Amax ⊗ T` represents `linearFrob` of `s` on the image of `y` in every `σ o`; here
`periodTensorMap Amax Bmax f` is the map `a ⊗ x ↦ a ⊗ f x` into `Bmax ⊗ _`. 

### `tateTwistHom`

 The map `g ↦ χ(g) ^ (-d) · [g]` from the decomposition group at `A` to the group ring, where `χ`
is the cyclotomic character. A representation read along it is its Tate twist by `χ ^ (-d)`. 

### `viaGroupRing_tateTwistHom`

 Read along `tateTwistHom A d`, an element `g` acts as `χ(g) ^ (-d)` times its action in `σ`. 

### `finite_setOf_jump_ne_zero`

 A continuous representation `σ` has finitely many Hodge–Tate jumps at `A`: the integers `k`
of nonzero multiplicity at some `γ : ℚ̄_ℓ → ℂ_ℓ`, for the restriction of `σ` to the decomposition
group at `A`, form a finite set. 

### `isCrystallineUpTo_tateTwistHom`

 If the twist of `σ` by `χ ^ (-d)` is crystalline and every jump of `σ` at `A` has absolute
value at most `d`, then the twist is crystalline with jumps in `[0, 2 d]`: the twist adds `d` to
every jump. 

### `IsTraceLimit`

 The trace of `r` is the uniform limit along `F` of the sums ∑ᵢ a η i · tr ρ η i, where the
`ρ η i` are unramified or crystalline at `A`, and are finitely many or share their jumps. 

### `IsTraceLimit.continuous_limit`

 The limit is continuous. 

### `IsTraceLimit.isTraceNondeg`

 The trace form of the limit is non-degenerate. 

### `IsTraceLimit.continuous_approx`

 Each `ρ η i` is continuous. 

### `IsTraceLimit.isGoodAt_approx`

 Each `ρ η i` is unramified or crystalline at `A`. 

### `IsTraceLimit.finite_or_hasJumpsAt`

 There are finitely many `η`, or all `ρ η i` have the same jumps. 

### `IsTraceLimit.tendstoUniformly_trace`

 The combinations of traces converge uniformly along `F` to the trace of `r`. 

### `_root_.New.Period.nonempty_adicBasis_span_natCast`

 `Amax` has a `p`-adic basis, for the ideal of `ℤ_p` generated by `p`. 

### `eventually_norm_trace_sub_le`

 The convergence of traces is uniform on the group ring: for every `ε > 0`, eventually along
`F`, the trace of every `y ∈ ℤ_ℓ[Gal(Ω/E)]` on `r` differs by at most `ε` from the combination
∑ᵢ a η i · (trace of `y` on `ρ η i`). 

### `finite_setOf_jump_approx_ne_zero`

 In a chart at `A` (an embedding `PadicPlaceEmbedding E A ℓ`), the integers that occur as jumps
of some `ρ η i` at some `γ : ℚ̄_ℓ → ℂ_ℓ` form a finite set. 

### `exists_isCrystallineUpTo_tateTwistHom`

 In a chart at `A`, one Tate twist, by `χ ^ (-d)` (`tateTwistHom A d`), makes `r` and all
`ρ η i` crystalline with jumps in `[0, 2 d]` (`IsCrystallineUpTo (2 * d)`). 

### `isCrystalline`

 In a chart at `A` (an embedding `PadicPlaceEmbedding E A ℓ`), the restriction of `r` to the
decomposition group at `A` is crystalline. 

### `isGoodAt`

 A limit of traces of representations that are unramified or crystalline at `A` is unramified or
crystalline at `A`. 

### `tendsto_jump`

 Suppose the trace of `r` is the uniform limit along the nontrivial filter `F` of the sums
∑ᵢ a η i · tr (ρ η i), where the `ρ η i` are unramified or crystalline at the place `A` and are
either finitely many or share their jumps (`IsTraceLimit r A F a ρ`). Suppose also that we fix an
embedding of Ω into ℚ̄_ℓ inducing `A`, with a compatible map from the decomposition group to
Gal(ℚ̄_ℓ/ℚ_ℓ) (`PadicPlaceEmbedding E A ℓ`). Then for every `γ` and `w`, the multiplicity of the
Hodge–Tate jump `w` at `γ` of `r` restricted to the decomposition group at `A` is the limit along
`F` of ∑ᵢ a η i · (the multiplicity of `w` at `γ` for the corresponding restriction of `ρ η i`). 

### `jumpsRelAt`

 Let the jump multiplicities of `ρ η i` be `R'`-related to `J' η i`. Suppose that `n` is
`R`-related to the multiplicity in `J` whenever numbers `x η i` are `R'`-related to the
multiplicities in `J' η i` and ∑ᵢ a η i · x η i tends to `n`. Then the jump multiplicities of `r`
are `R`-related to `J`. 

### `eq_zero_of_relation`

 Relations in the group ring pass to the limit. Let the traces weighted by the coefficients of
the `Q η i` and of `P` converge (`h_coeff`). If the group ring elements `y θ l` satisfy, in each
`ρ θ x`, the relation with the coefficients of `Q θ x`, and their combination with the
coefficients of `P` has in `r` a value `M` that does not depend on `θ`, then `M = 0`. 

### `periodTensorMap_sum_lTensor_eq`

 Untwisting the powers of a Weil element. Let the twist of `σ` by `χ ^ (-d)` be crystalline with
jumps in `[0, 2 d]`, `σ` crystalline at `A`, `(s, k)` a Weil pair, and `Y N ∈ Amax ⊗ T` represent
(`hY`) the linear Frobenius of `s ^ N` (degree `N k`) of the twist on `ℓ ^ (k d (n - N)) δ ⊗ 1`. For
`deg Q < n`, `periodTensorMap` sends `∑ N, lTensor Amax (Q.coeff N • applyVec u v) (Y N)` to
`(δ • (ℓ ^ (k d)) ^ n) • Q(β) (1 ⊗ v)`, `β = linearFrob (decompRep σ.rep A) ⟨s, hs⟩ k`. 

### `exists_periodTensorMap_eq_and_lift_eq`

 Integral representatives. In the setting of `periodTensorMap_sum_lTensor_eq`, let `u ∘ q` be the
action of the group ring on `σ` (`hu`), and let `q (y f N)` be the element that the linear form `f`
reads off `Y N` (`hy`). Write `V` for the space `σ.Index → ℚ̄_ℓ` of `σ`. Then one `M ∈ Amax ⊗ V`
has image `(δ • (ℓ ^ (k d)) ^ n) • Q(β) (1 ⊗ v)` in `Bmax ⊗ V`, and every `f` reads `M` as
`(∑ N < n, Q.coeff N • y f N) *ᵥ v` on `σ`. 

### `isKilledBy`

 The case of `polyKillsAt` at a place `A` above `ℓ`, given by an embedding `L` of Ω in ℚ̄_ℓ.
Assume the trace of `r` is the uniform limit along `F` of ∑ᵢ `a η i`·tr `ρ η i` (`h`). Let `Q η i`
kill `s` on `ρ η i`, let all degrees be below `n`, and let the traces also converge when weighted by
each coefficient of `Q η i` and of `P` (`h_coeff`). If `(s, k)` is a Weil pair through `L` (`s⁻¹` is
a Frobenius for `ℓ ^ k`), then the restriction of `r` to the decomposition group is potentially
crystalline and `P` kills its linearized Frobenius in degree `k` (`IsKilledBy`). 

### `polyKillsAt`

 If `Q η i` kills `s` on `ρ η i`, all degrees are below `n`, and the traces also converge when
weighted by each coefficient of `Q η i` and of `P`, then `P` kills `s` on `r`. 

### `local_clauses_of_trace_limit`

 Limits of traces keep the local clauses: unramified or crystalline, the jumps, and the
polynomials that kill a Weil element (`IsTraceLimit.isGoodAt`, `.jumpsRelAt`, `.polyKillsAt`). 
