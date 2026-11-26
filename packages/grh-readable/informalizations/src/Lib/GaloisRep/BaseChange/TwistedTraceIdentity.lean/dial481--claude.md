---
{
  "module": "src/Lib/GaloisRep/BaseChange/TwistedTraceIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/TwistedTraceIdentity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/TwistedTraceIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Twisted trace identity for a step E'/E of CM fields of prime degree

The main result is `New.twisted_trace_identity`. For a step `E'/E` (`New.IsStep`) of prime degree,
it compares a `σ`-twisted trace on forms over `E'` with a trace on forms over `E`, on the definite
unitary groups of `New.stdSpace`, for matching pairs of test functions. Both sides are expanded by
`New.Space.isSampleTotal_twisted_trace` as weighted sums over samples of pairs
(`New.IsSampleTotal`).

## Main definitions and results

* `New.IsSampleTotal`: a number `a` is a weighted sum of `F` over finitely many points, and the
  weighted number of moves from these points to each relevant point is `c`.
* `New.IsSampleTotal.mul_eq_mul_of_bijOn`: two such sums `a`, `b` with weights `c`, `d` satisfy
  `b * c = d * a` when a map between the point sets matches values and moves.
* `New.Weight.baseChange`: the weight of `E'` that has at each infinite place the data of `κ` at the
  place below.
* `New.exists_trace_mul_weightRep_eq_of_twistedNorm_eq`: the twisted character of `κ.baseChange` at
  `δ` is the character of `κ` at the norm of `δ`.

Notions from other files:
* `New.Space.forms V κ`: the forms of weight `κ` on a space `V`, smooth functions `ψ` on the finite
  adelic unitary group `Gf E n` (`U (1 : Matrix n n (𝔸f E))`; `U V.J` is the rational one) with
  `ψ (V.embFin γ * g) = ρ γ (ψ g)` for rational `γ`, where `ρ` is `V.weightRep κ.fst κ.snd` and
  `V.embFin` embeds the rational unitary group; `V.formTranslation κ` is right translation on them.
* `levelSpace π L`: the vectors fixed by `π k` for every `k ∈ L`.
* `New.IsOperatorOf π L T φ`: `T` is the Hecke operator of `φ` on the `L`-fixed vectors.
* `New.stdSpace`: the definite space `I_n`, the sum of `n` norms with its standard lattice.
* `New.twistedNorm τ p δ`: the product `δ * τ δ * ⋯ * τ^[p - 1] δ`.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.


 ## Double counting of moves between weighted samples of pairs 

### `New.IsSampleTotal`

 There are finitely many points `p i` with complex weights `w i` such that
`a = ∑ w i * F (p i)`, and `∑ w i * #(M (p i) y) = c` for every point `y` such that `F x ≠ 0`
whenever there is a move in `M x y`. Here `M x y` is thought of as the set of moves from `x` to
`y`, and `Set.ncard` is `0` on infinite sets. 

### `New.IsSampleTotal.mul_eq_mul_of_bijOn`

 Double counting of moves. `IsSampleTotal M F c a` says that, for finitely many points `p i` with
complex weights `w i`, `a = ∑ w i * F (p i)` and `∑ w i * #(M (p i) y) = c` for every `y` such that
`F x ≠ 0` whenever `M x y` (the set of moves from `x` to `y`, with `#` equal to `0` if infinite) is
nonempty. Let `a`, `b` be such totals of `F`, `F'` with weights `c`, `d` for the moves `M`, `N`, and
suppose: `F` vanishes off `S`; `F' y = F x` when `x ∈ S` and `y` has a move to `m x`; and for each
`y` with `F' y ≠ 0`, some `z` and `J` map, for every `x`, the moves from `x` to `z` bijectively onto
the moves from `y` to `m x` (onto `∅` if `x ∉ S`). Then `b * c = d * a`. 


## The twisted trace of a Hecke operator as a sum over a sample

The moves from a pair `(x, γ)` to a pair `(y, δ)` are the rational `g` with `y⁻¹ * j g * x ∈ K`
and `g⁻¹ * δ * τ g = γ`, where `j` is `V.embFin`.


### `New.Space.compLeft_comp_funLeft_mem_forms`

 The twist `ψ ↦ s ∘ ψ ∘ σ⁻¹` maps forms of weight `κ` on `V` to forms. Here `σ` is an
automorphism of the finite adelic group with continuous inverse, `τ` an automorphism of the
rational unitary group with `V.embFin (τ γ) = σ (V.embFin γ)`, and `s` a linear map of the
coefficient space with `s * ρ γ = ρ (τ γ) * s` for `ρ = V.weightRep κ.fst κ.snd`. 

### `New.Space.restrict_compLeft_comp_funLeft_mem_levelSpace`

 The twist `ψ ↦ s ∘ ψ ∘ σ⁻¹` of forms of weight `κ` (a map of `V.forms κ` by `h_forms`) maps
forms fixed by `L` to forms fixed by `L`, when the automorphism `σ` maps `L` onto itself. 

### `New.Space.sum_inv_card_classAut_mul_card_eq_relIndex`

 A weighted count of transporters. Let `L ≤ J` be subgroups of `Gf E n` of finite type for the
rational points `V.Γf`, and let `S g h` be finite sets with `#(S g h) = #(classAut V.Γf J g)` if `g`
and `h` lie in one double coset (`Γ g J = Γ h J`), and `0` otherwise. Then for every `x` the sum
over the double cosets `i` in `Γ \ G / L` of `#(S x i.out) / #(classAut V.Γf L i.out)` is the
index `[J : L]`. 

### `New.Space.range_domRestrict_levelSpace_eq_coindV_inf`

 The `L`-fixed forms of weight `κ` on `V`, seen as functions on `Gf E n`, are the functions that
are equivariant for `ρ = V.weightRep κ.fst κ.snd` (`ψ (V.embFin γ * g) = ρ γ (ψ g)`) and right
invariant under the open subgroup `L`. The factor `Submodule.pi ∅ ⊥` (no vanishing condition) is
the form in which `New.trace_eq_weighted_sum` takes this space. 

### `New.Space.isSampleTotal_twisted_trace`

 Twisted trace formula on a definite space `V`. Let `σ` be an automorphism of `Gf E n` with
continuous inverse, `L ≤ K ≤ stdLevel E n` with `L` open and `σ`-stable, `τ` a lift of `σ` to the
rational unitary group along `j = V.embFin`, and `s * ρ γ = ρ (τ γ) * s` for
`ρ = V.weightRep κ.fst κ.snd`. Then `ψ ↦ s ∘ ψ ∘ σ⁻¹` preserves forms and `L`-fixed forms, and for
some `c ≠ 0` the trace of each Hecke operator `T` of `φ` at level `L` composed with it is a sample
sum of weight `c` over pairs. 


## Base change of weights and twisted characters at the norm

A weight `κ` (`New.Weight`) is a Young diagram `κ.fst` and a power `κ.snd` of the determinant at
each infinite place, and `New.Space.weightRep` is the representation of the rational unitary
group that it defines.


### `New.Weight.baseChange`

 The base change of a weight: at an infinite place of `E'`, the diagram and the power of the
determinant that `κ` has at the place of `E` below it. 

### `New.exists_trace_mul_weightRep_eq_of_twistedNorm_eq`

 Twisted characters of a base changed weight. For `E'/E` Galois of prime degree `p` with
compatible CM types and `σ ≠ 1` in its Galois group, let `ω` apply `σ` to entries and `ρ` be the
representation of the base change of `κ`. Some `s` satisfies `s * ρ δ = ρ (ω δ) * s`, and when the
twisted norm `δ * ω δ * ⋯ * ω^[p - 1] δ` is the image `j γ` of `γ` over `E`, the trace of `s * ρ δ`
is the character of `κ` at `γ`. 


## The twisted trace identity for matching pairs

Conventions: `New.galoisGf σ` is the action of `σ` on `New.Gf E' n`, `New.baseChangeGf` the
inclusion of `New.Gf E n` into `New.Gf E' n`, and `New.IsMatchingPair` the matching condition
between a function `f` over `E` and a function `φ` over `E'` (on `New.Gf E' n`, written `U 1`).


### `New.twistedNorm_inv_mul_mul_galoisGf`

 Let `x` and `δ` be finite adelic unitary points over `E'`. The twisted norm (for the action
`galoisGf σ` of `σ`, with `[E' : E]` factors) of the twisted conjugate `x⁻¹ * δ * σ x` is the
conjugate `x⁻¹ * N δ * x` of the twisted norm `N δ` of `δ`. This uses `σ ^ [E' : E] = 1`. 

### `New.exists_isUnit_aeval_and_isRootQuotient_le`

 A global completion of a norm root `z` of the characteristic polynomial `P` of a rational
unitary `δ` over `E'`, when `σ` fixes `P`: for some rational `z₀` and adelic `b`,
`x = z₀ * σ b * z` is invertible at `e ν` for every rational `ν` of characteristic polynomial `P`,
and every root quotient `r` of `x` at `e ν` (`r * x(e ν)ᴴ = x(e ν)`) is one of `b` (`e` the
inclusion of rational into adelic points). 

### `New.exists_isRootQuotient_of_isNormRoot`

 Let `C` be a class of `σ`-fixed polynomials over `E'` with norm roots `z P` (`IsNormRoot`: among
other things, the twisted norm `z * σ z * ⋯` of `z P` has root quotient `g` at each adelic `g` of
characteristic polynomial `P`). To each rational `ν` with characteristic polynomial `q ν` in `C`
belong a rational `A ν` and an adelic `B ν`, compatible with conjugation, such that for `δ` with
`δ * ω ν = ν * δ` (`ω` the action of `σ`) a root quotient `r` of `z (q ν)` at `e ν`
(`r * z(e ν)ᴴ = z(e ν)`) makes `r⁻¹ * e δ` the twisted conjugate of `e (A ν * δ)` by `B ν`; `e`
includes rational into finite adelic unitary points, and `U 1` is the rational unitary group
`U (1 : Matrix n n E')`. 

### `New.IsBaseChangeMaps`

 Facts about the maps between unitary points over `E` and `E'` in `New.twisted_trace_identity`:
`j` is base change of rational points from `E` to `E'`, `ω` the action of `σ` on rational points
over `E'`, `e` the inclusion of rational into finite adelic points. The maps `j` and `e` are
injective, the three maps are compatible with `σ` and with base change, Galois descent holds for
adelic and for rational points, and a rational cocycle of twisted norm one that splits adelically
splits (Hasse principle). 

### `New.IsBaseChangeMaps.exists_baseChangeGf_eq`

 Galois descent for finite adelic points. 

### `New.IsBaseChangeMaps.exists_j_eq`

 Galois descent for rational points. 

### `New.IsBaseChangeMaps.exists_ω_eq_inv_mul`

 The Hasse principle: a rational cocycle of twisted norm one that splits adelically splits. 

### `New.IsMatchingRoots`

 Facts about a matching pair `(f, φ)` used by the double counting in
`New.twisted_trace_identity`. `Good ν` marks the rational `ν` over `E'` whose characteristic
polynomial occurs in the matching condition, with a rational root quotient `A ν` and an adelic one
`B ν`. The fields: twisted invariance of `φ` under `K`, goodness at non-zero terms, compatibility
with conjugation, the twisted norm through `A ν` and `B ν`, and matching of values and of `K`. 

### `New.smul_charpoly_eq_of_semiconjBy`

 If `δ * ω ν = ν * δ` for the action `ω` of `σ` on rational points over `E'`, then the
characteristic polynomial of `ν` is fixed by `σ`. 

### `New.isBaseChangeMaps`

 The maps of `New.twisted_trace_identity` satisfy `IsBaseChangeMaps` for `σ ≠ 1` over a step
`E'/E`: base change `j` of rational points, the action `ω` of `σ` on rational points over `E'`, and
the inclusion `e` of rational into finite adelic points. 

### `New.IsBaseChangeMaps.twistedNorm_conj`

 The twisted norm for `galoisGf σ` of a twisted conjugate `x⁻¹ * e δ * σ x` of a rational point
`δ` over `E'` is the conjugate by `x` of `e` applied to the twisted norm of `δ` for `ω`. 

### `New.IsBaseChangeMaps.semiconjBy_twistedNorm`

 A rational point `δ` over `E'` and its twisted norm `ν` for `ω` satisfy `δ * ω ν = ν * δ`. 

### `New.IsMatchingRoots.commute_inv`

 `(A ν)⁻¹` commutes with a good `ν`: take `g = ν' = ν` in
`IsMatchingRoots.good_and_conj_of_semiconjBy`. 

### `New.IsMatchingRoots.semiconjBy_inv`

 For a good base change `j γ`, `(A (j γ))⁻¹ * ω (j γ) = j γ * (A (j γ))⁻¹` (`ω` fixes `j γ`). 

### `New.IsMatchingRoots.commute_map`

 `B ν` commutes with `e ν` for a good `ν`: take `g = ν' = ν` in
`IsMatchingRoots.good_and_conj_of_semiconjBy`. 

### `New.IsMatchingRoots.twistedNorm_inv`

 For a good base change `j γ`, the twisted norm of `(A (j γ))⁻¹` is `j γ`. 

### `New.IsMatchingRoots.apply_inv_mul_embFin_mul_eq`

 For a good base change `j γ` and `x` over `E`, the value of `f` at `x⁻¹ * γ * x` is the value of
`φ` at the twisted conjugate of `e (A (j γ))⁻¹` by `y = (B (j γ))⁻¹ * baseChangeGf x`. 

### `New.exists_isMatchingRoots`

 For a matching pair `(f, φ)` (`IsMatchingPair`) over a step `E'/E`, with `e` the inclusion of
rational into finite adelic unitary points over `E'`, `ω` the action of `σ` on rational points
and `j` base change from `E` (`IsBaseChangeMaps`), there are a class `Good` of rational points and
root quotients `A`, `B` with the properties of `IsMatchingRoots`. 

### `New.IsMatchingRoots.exists_bijOn_of_ne_zero`

 The bijection of moves in `New.twisted_trace_identity`. Let `m` send a pair `(y, γ)` over `E`
to the pair `((B (j γ))⁻¹ * y, (A (j γ))⁻¹)` over `E'`. For a pair `(x, δ)` over `E'` with
`φ (x⁻¹ * e δ * σ x) ≠ 0` there are a pair `z` over `E` and a map `J` on rational points such that,
for every pair `p` over `E`, `J` takes the moves from `p` to `z` bijectively onto the moves from
`(x, δ)` to `m p` (onto `∅` if `j p.2` is not good). A move over `E'` from `(x₀, γ)` to `(x₁, γ₁)`
is a rational `a` with `x₁⁻¹ * a * x₀ ∈ K` and `a⁻¹ * γ₁ * τ a = γ`; `hK_split` says that every
`s ∈ K` of twisted norm one splits in `K`. 

### `New.twisted_trace_identity`

 Twisted trace identity for a step `E'/E` (`IsStep`) and `σ ≠ 1` in its Galois group. Let
`L ≤ K ≤ stdLevel E' n` with `L` open and `σ`-stable, and let every `s ∈ K` of twisted norm one be
`t * (σ t)⁻¹` with `t ∈ K` (`hK_split`). Then for some `c ≠ 0`, an operator `t` on forms of weight
`κ.baseChange` over `E'` (a) turns translation by `g` into that by `σ g`, (b) keeps `L`-fixed forms,
and (c) has `tr (T' * t) = c * tr T` for Hecke operators `T'`, `T` of a matching pair `(φ, f)`. 
