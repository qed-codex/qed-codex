---
{
  "module": "src/Lib/PadicHodge/Limit/CrystallineLimit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Limit/CrystallineLimit.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Limit/CrystallineLimit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform period bounds and limits of crystalline lattices with bounded jumps

Let `A = New.Period.Amax` and `B = New.Period.Bmax`, with tensor products over `ℤ_p`. A continuous,
trace-nondegenerate `p`-adic limit of continuous crystalline representations with jumps in `[0, h]`
is crystalline. The limit is formulated through representations of the group ring `ℤ_p[G]`,
restricted along a multiplicative map from a local Galois group.

## Main definitions and results

* `New.Period.IsCrystallineUpTo`: crystalline with all Hodge–Tate jumps (`New.Period.jump`) in [0,
  h].
* `New.Period.PadicRep`: a matrix representation of Γ over Q̄_p, bundled with its index set.
* `New.Lift.uniform_period_bound`: one element `a` of the period ring `A = New.Period.Amax` bounds
  the denominators of the periods of all crystalline `ℤ_p`-lattices with Hodge–Tate jumps in
  `[0, h]` (`New.Period.IsCrystallineUpTo`). The element `a` is chosen for the given `Γ`, with its
  `OverGp Γ p` instance (the map `toGp` to `G_p`), and for the given `h`.
* `New.Period.exists_finite_groupRing_quotient`: the image of `ℤ_p[G]` in finitely many continuous
  representations is a finite free `ℤ_p`-algebra with the properties
  `New.Period.IsFiniteGroupRingQuotient`.
* `New.Period.isCrystalline_of_trace_limit`: the limit theorem.

Notions from other files:
* `New.Period.IsCrystalline`: T is crystalline: the elements of B⊗T fixed by all of Γ span B⊗T over
  B.
* `New.Period.Amax`: Colmez's period ring A_max, the p-adic completion of A_inf[X]/(pX − ξ).
* `New.Period.Bmax`: The period ring B = B^+[1/μ] (Colmez's B_max, used in place of Fontaine's
  B_cris), over which crystalline representations are defined; B^+ = A[1/p] is `New.Period.BPlus`.
* `New.IsTraceNondeg`: for a representation r, any x in the span of r(G) with tr(x r(g)) = 0 for all
  g is zero.
* `OverGp Γ p`: a group Γ with a homomorphism `toGp` to G_p = Gal(Q̄_p/Q_p) whose image is open.
* `New.Period.fixedPeriods ρ B F`: the elements of B ⊗ T fixed by `toGp g ⊗ ρ g` for F-almost all g.
* `New.Lift.Chart` c with `c.IsChartOf j`: a chart W(F_q)⟦X⟧ → A_inf with coefficients `WittFq c.f`,
  sending X to z; `IsChartOf j` says that every g in G_p that fixes `WittFq c.f` pointwise and fixes
  θ(z) lies in j(Γ).
* `New.Lift.AdicBasis I A`: for an ideal I of a ring Λ and a Λ-module A, a topological basis of A
  for the I-adic topology, with coordinate forms.

## Relation to the literature

Known; see `Lib.PadicHodge.Limit.TraceLimit` and `Lib.PadicHodge.RadiusLemma` for sources.


 ## Crystalline modules with Hodge–Tate jumps in [0, h] 

### `periodTensorMap_injective`

 For `T` flat over `ℤ_p`, the map `A ⊗ T → B ⊗ T` (`periodTensorMap`) induced by the inclusion
of `A = Amax` in `B = Bmax` and the identity of `T` is injective. 

### `IsCrystallineUpTo`

 The representation is crystalline and all its Hodge–Tate jumps, at every γ: R → C_p, lie in
[0, h]. 

### `PadicRep`

 A finite index type m with a group homomorphism Γ → GL_m(ℚ̄_p): a matrix representation of
unspecified dimension. 

### `PadicRep.Index`

 The index set of the rows and columns. 

### `PadicRep.fintypeIndex`

 The index set is finite. 

### `PadicRep.rep`

 The homomorphism from `Γ` to invertible matrices over the algebraic closure of `ℚ_p`. 

### `applyVec`

 For a Z_p-linear map u from T to square matrices over Q̄_p and a vector v, the Z_p-linear
map sending x to u(x)v. 

 ## The uniform period bound 

### `New.Lift.uniform_period_bound`

 **Uniform period bound.** For `Γ` over `G_p` with open image (instance `OverGp Γ p`) and `h : ℕ`
there is `a` in `A = Amax`, a unit in `B = Bmax`, such that for every crystalline `ρ` on `T` with
basis `e` and jumps in `[0, h]`: (a) each `a ⊗ t` lies in the `A`-span of the invariants of `A ⊗ T`;
(b) some `U`, `U'` over `A` have `U U' = a · 1` and `ρ(g) · g(U) = U`, with `ρ(g)` the matrix of
`ρ g` in `e`: the columns of `U` are invariant vectors.
Known result: Dwork's trick (an integral crystalline comparison with a uniform denominator). 


## Limits of crystalline representations in group-ring form

A continuous, trace-nondegenerate `p`-adic limit of continuous crystalline representations with
jumps in `[0, h]` is crystalline.

Representations of a compact group `G` are extended to the group ring (`New.Period.groupRingHom`)
and restricted along a multiplicative map `w : Δ →* ℤ_p[G]` from a local Galois group
(`New.Period.viaGroupRing`).


### `groupRingHom`

 For a matrix representation σ: G→GL_m(Q̄_p), the Z_p-algebra homomorphism from the group
ring Z_p[G] to m×m matrices over Q̄_p extending σ. 

### `viaGroupRing`

 For a multiplicative map w: Δ→Z_p[G] and a matrix representation σ of G over Q̄_p, the matrix
representation of Δ sending g to σ(w(g)), σ extended linearly. 

### `IsFiniteGroupRingQuotient`

 `q : ℤ_p[G] → T` and the maps `u s` from `T` to matrices over `Q̄_p` indexed by `(τ s).Index`
present `T` as a finite free quotient of the group ring `ℤ_p[G]` through which the representations
`τ s` factor; along any multiplicative map `w : Δ → ℤ_p[G]`, `T` is crystalline with jumps in
`[0, h]` if all `τ s`, read along `w`, are. 

### `IsFiniteGroupRingQuotient.free`

 `T` is free as a `ℤ_p`-module. 

### `IsFiniteGroupRingQuotient.finite`

 `T` is finitely generated as a `ℤ_p`-module. 

### `IsFiniteGroupRingQuotient.surjective`

 `T` is a quotient of the group ring. 

### `IsFiniteGroupRingQuotient.factors`

 The extension of `τ s` to the group ring (`groupRingHom`) is `u s ∘ q`. 

### `IsFiniteGroupRingQuotient.apply_eq_zero_iff`

 The kernel of `q` is the common kernel of these extensions. 

### `IsFiniteGroupRingQuotient.isCrystallineUpTo`

 If every `τ s`, read along `w`, is crystalline with jumps in `[0, h]`, so is `Δ` acting on `T`
  by left multiplication with `q (w g)`. 

### `exists_finite_groupRing_quotient`

 For finitely many continuous representations `τ s` of the compact group `G` over `Q̄_p`, there
exist a `ℤ_p`-algebra `T`, a map `q : ℤ_p[G] → T` and maps `u s` from `T` to matrices over `Q̄_p`
indexed by `(τ s).Index`. These present `T` as a finite free quotient of the group ring `ℤ_p[G]`
through which every `τ s` factors (`IsFiniteGroupRingQuotient`). Moreover, for the group `Δ` with
its map to `Gal(Q̄_p/Q_p)` and any multiplicative map `w : Δ → ℤ_p[G]`, `T` is crystalline with
jumps in `[0, h]` whenever all `τ s`, read along `w`, are. 

### `exists_pos_mem_pow_of_norm_trace_le`

 Let `R` be a continuous matrix representation of the compact group `G` whose trace form is
non-degenerate. Let `T` be a finite free `ℤ_p`-algebra, a quotient `q` of `ℤ_p[G]` whose kernel
contains that of `groupRingHom R`, and let `u` map `T` to matrices with `u ∘ q = groupRingHom R`.
Traces define the `p`-adic topology on `T`: for every `k` there is `ε > 0` such that `t ∈ p ^ k T`
as soon as the traces of all `u t * R g` have norm at most `ε`. 

### `linearIndependent_of_mem_fixedPeriods`

 Let `c` be a chart (a Λ-algebra map Λ[[X]] → `A_inf`, Λ = `WittFq c.f`, sending X to z = [ϖ^♭])
for `Δ`: every g in Gal(Q̄_p/Q_p) fixing Λ pointwise and fixing θ(z) lies in the image of `Δ`. Let
`A = Amax` and `W = WittFq c.f`, with an algebra map `W → A` that agrees with `W → Ainf` after both
are mapped to `Bmax` (`halg`), and let `T` be flat over `ℤ_p` with a representation `ρ` of `Δ`.
Finitely many elements of `A ⊗ T` fixed by `Δ` that are linearly independent over `W` stay so over
`A`. 

### `finite_free_of_fixed_periods`

 Let `A = Amax`, and let `W = WittFq c.f` be the coefficient ring of a chart `c` for `Δ`, with
an algebra map `W → A` that agrees with `W → Ainf` after both are mapped to `Bmax` (`halg`). Let
`T` be finite free over `ℤ_p` with a representation `ρ` of `Δ`. A `W`-submodule `D` of invariant
elements of `A ⊗ T` is finite free, and `A ⊗_W D → A ⊗ T` is injective. 

### `separated_and_complete_of_free`

 A finite free module over `Amax` is `p`-adically separated and complete: the bundle of
`eq_zero_of_forall_mem_nsmulRange` and `exists_forall_sub_mem_nsmulRange_of_sub_mem`. 

### `eq_zero_of_forall_mem_nsmulRange`

 In a finite free `Amax`-module, an element that lies in `p ^ k M` for every `k` is zero. 

### `exists_forall_sub_mem_nsmulRange_of_sub_mem`

 In a finite free `Amax`-module, a sequence `s` with `s k - s m ∈ p ^ k M` for `k ≤ m` has a
limit `x`: `s k - x ∈ p ^ k M` for every `k`. 

### `exists_monotone_coord_support`

 For finite families `b k` in a module with topological basis `c` there are increasing finite
sets `S k` of indices that give every `b k i` modulo `I ^ k`; the other coordinates of `b k i` lie
in `I ^ k`. 

### `mem_span_of_forall_mem_span_preimage`

 Passage to the limit. Let `A = Amax` be an algebra over a `p`-adically complete ring `Λ` with
`(p)` maximal. Let `Q : M → N` and `Q' k : M → N' k` be `A`-linear, with `Q` zero modulo `p ^ k` on
the kernel of `Q' k`, and let `D ⊆ N`, `D' k ⊆ N' k` be `Λ`-submodules (`N` finite free over `A`,
`D` finite free over `Λ` and `p`-saturated, `A ⊗_Λ D' k → N' k` injective) such that the preimages
`Q' k ⁻¹' D' k` decrease and `D` holds the limits of their images. If `x` lies in the `A`-span of
every preimage, then `Q x` lies in the `A`-span of `D`. 

### `baseChange_mem_nsmulRange_and_eq_zero_of_eq_zero`

 The kernel step of `isCrystalline_of_trace_limit`, for `R: PadicRep G p` (any group `G`) and
families `X η` (`η: I`) indexed by `ι η`; `groupRingHom` extends a representation linearly to
`ℤ_p[G]`. Let `u (q y)` extend `R` (`hu`), let traces of `R` bound `p`-divisibility in `T`
(`htrace`), let the trace of `R` be small on the common kernel of each family `X (η k)` (`hη`), and
let each surjection `π k` have as kernel the common kernel of the `X (η l)`, `l ≤ k` (`hπ_ker`).
Then over `Amax` an element killed by `π k` is sent by `q` into `p ^ k (Amax ⊗ T)` and killed by
every `π l`, `l ≤ k`. 

### `isCrystalline_of_trace_limit`

 Let `G` be a compact group, `Δ` a group with a homomorphism `j : Δ → G_p` of open image
(`OverGp Δ p`), `w : Δ → ℤ_p[G]` multiplicative, and `R : G → GL_m(ℚ̄_p)` continuous with trace form
non-degenerate on the span of the matrices `R(g)`. Let `X η` be finite families of continuous
representations of `G` over `ℚ̄_p` whose pullbacks `g ↦ X(w(g))` along `w` (`viaGroupRing`, through
the linear extension `groupRingHom` to `ℤ_p[G]`; `η : I`, members indexed by finite `ι η`) are
crystalline (with respect to `j`) with Hodge–Tate jumps in `[0, h]`. If for each `ε > 0` some `X η`
has `‖tr R(y)‖ ≤ ε` for all `y ∈ ℤ_p[G]` killed by every member of `X η`, then the pullback of `R`
along `w` is crystalline. 
