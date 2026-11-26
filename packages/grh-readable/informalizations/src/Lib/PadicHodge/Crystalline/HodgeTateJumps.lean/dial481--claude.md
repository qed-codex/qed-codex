---
{
  "module": "src/Lib/PadicHodge/Crystalline/HodgeTateJumps.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/HodgeTateJumps.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/HodgeTateJumps.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hodge frames and Hodge–Tate jumps under operations on representations

This file works with the period ring B_dR⁺, its uniformiser `t` and its residue map θ to ℂ_p. An
invertible matrix `U` of de Rham periods with `N g · g U = U` for `g` near 1 is brought into the
form `New.Period.hodgeMatrix W k` by an algebraic change of basis, and the columns of θ(W) are then
Hodge–Tate vectors. From this the file builds Hodge–Tate frames of potentially crystalline
representations, counts their jumps, and computes the jumps under base change, restriction of
scalars, twists, duals and submodules of products.

## Main definitions and results

* `New.Period.exists_isHodgeFrame`: an invertible `U` over B_dR with `N g · g U = U` becomes
  `hodgeMatrix W k`, with `W` invertible over B_dR⁺, after an algebraic change of basis of
  determinant 1.
* `New.Period.IsPotentiallyCrystalline.exists_isHodgeTateFrame`: there is an invertible `P` over
  `ℂ_[p]` whose columns are Hodge–Tate vectors of weights `k` (`New.Period.IsHodgeTateFrame`); the
  `k i` are the jumps, and the rows of `P⁻¹` form a basis of Hodge–Tate maps
  (`New.Period.hodgeTateMaps`).
* `New.Period.IsPotentiallyCrystalline.exists_hasJumps`: the number of jumps is the rank.
* `New.Period.jump_baseChange`, `New.Period.IsPotentiallyCrystalline.sum_jump_eq_jump_overZp`:
  extension, restriction of scalars.
* `New.Period.jump_twist_of_period`, `New.Period.jump_twist_cyclotomicGp`,
  `New.Period.hasJumps_of_cyclotomicGp_zpow`: twists shift jumps.
* `New.Period.exists_jump_of_jointly_injective`: a jump of a submodule of ∏ S_i is a jump of some
  S_i.

Notions from other files:
* `New.Period.BdRPlus`, `New.Period.BdR` (built for the prime p fixed by the instance `ThePrime p`,
  hence written without `p`): the discrete valuation ring B_dR⁺, with uniformiser `t`
  (`New.Period.tPeriod`) and residue map θ to ℂ_p (`New.Period.thetaBdR`), and its fraction field
  B_dR.
* `New.cyclotomicGp`: The p-adic cyclotomic character χ of G_p = Gal(Q̄_p over Q_p) (`New.Gp`);
  `New.Period.χ` is its composite with `toGp : Γ → G_p`, the map supplied by the class `OverGp Γ p`;
  the "open image" of `toGp` assumed in the lemmas comes with this class.
* `New.Period.nearOne`: The filter 'near 1' on Γ: the pull-back along `toGp` of the filter of
  neighbourhoods of the identity.
* `New.Period.IsPotentiallyCrystalline`: ρ is potentially crystalline: the vectors of Bmax ⊗ T (Bmax
  the crystalline period ring B_max, a ℤ_p-algebra on which G_p acts) fixed by `toGp g ⊗ ρ g` for
  `g` near 1 span Bmax ⊗ T.
* `New.Period.hodgeTateMaps`, `New.Period.jump`: the space of γ-semilinear forms f on T with f(g
  x) = χ(g)^(−u) · g f(x) for g near 1, and its dimension, the multiplicity of the jump u.
* `New.Period.overZp`: A representation of Γ on a module T over a Z_p-algebra R, regarded as a
  Z_p-linear representation.
* `New.Period.HasJumps`: The property of a multiset J of integers that for every integer u the
  multiplicity of the jump u of T at γ equals its count in J.

## Relation to the literature

Known; see `Lib.PadicHodge.Crystalline.Regularity` for sources.



## The Hodge frame of a Galois-invariant matrix of de Rham periods

`New.Period.BdRPlus` is the discrete valuation ring B_dR⁺ with uniformiser `t`
(`New.Period.tPeriod`; `New.Period.tUnit` as a unit of the field B_dR) and residue map
`New.Period.thetaBdR` to ℂ_p. Galois acts on `t` by the cyclotomic character.

* `New.Period.hodgeMatrix W k`: the matrix `W · diag (t ^ k i)`.

Group elements are `toGp g` with `g` along a filter `F` coarser than `New.Period.nearOne Γ`.


### `hodgeMatrix`

 The matrix `W · diag (t ^ k i)` over `B_dR`, where `t` is the period `tUnit`. 

### `IsHodgeTateFrame`

 The columns of `P` are Hodge–Tate vectors of weights `k` for the semilinear map
`v ↦ N (g • v)` of `ℂ_p ^ ι`: it multiplies the column `j` by `χ(g) ^ (-k j)`, where `χ` is the
cyclotomic character. 

### `IsHodgeTateFrame.mulVec_twist`

 In the coordinates given by a Hodge–Tate frame `P`, the map `v ↦ N (g • v)` acts on the
coordinate `j` by `x ↦ χ(g) ^ (-k j) • g • x`. 

### `IsHodgeFrame`

 `Y`, `W`, `k` form a Hodge frame for the matrix `U` over `B_dR` and the family `N` along the
filter `F` on `Γ`: the algebraic, integral, fixed change of basis `Y` turns `U` into the invariant
matrix `W · diag (t ^ k i)` with `W` invertible over `B_dR⁺`. 

### `IsHodgeFrame.isUnit`

 The matrix `W` is invertible over `B_dR⁺`. 

### `IsHodgeFrame.eventually_map_eq`

 The entries of `Y` are fixed by `g`, eventually along `F`. 

### `IsHodgeFrame.mul_map_eq`

 The product `U Y` is `W · diag (t ^ k i)`. 

### `IsHodgeFrame.eventually_mul_smul_eq`

 The matrix `W · diag (t ^ k i)` is fixed by `M ↦ N g * g • M`, eventually along `F`. 

### `IsHodgeFrame.norm_le_one`

 The entries of `Y` are integral. 

### `isHodgeTateFrame_of_hodgeMatrix`

 If `W · diag (t ^ k i)` is fixed by `M ↦ N * g • M`, then `θ(W)` is a Hodge–Tate frame of
weights `k` at `g` for `N`, whose entries are read in `ℂ_[p]`. 

### `exists_eq_hodgeMatrix`

 Every matrix `U` over `B_dR` is `W · diag (t ^ k i)` for a matrix `W` over `B_dR⁺`: write a
common denominator of the entries of `U` as `u * t ^ d` with `u` a unit, and take `k i = -d`. 

### `_root_.Matrix.det_eq_mul_det_updateCol_of_mulVec_eq_smul_of_apply_eq_one`

 Cramer's rule for one column: if `W *ᵥ a = c • V` and `a i = 1`, then `det W = c * det W'`,
where `W'` is `W` with the column `i` replaced by `V`. 

### `hodgeMatrix_mul_map_updateCol`

 The column step of the Hodge frame: let `a` be supported where the weight is `k i`, with
`W a = t V`. Then replacing the column `i` of the identity by `a` turns `W · diag (t ^ k)` into
`W' · diag (t ^ k')`, where `W'` is `W` with the column `i` replaced by `V` and `k'` is `k`
with `k i` raised by one. 

### `exists_isHodgeFrame`

 Let `Γ` map to `Gp p` by `j` with open image, let `F` be a filter on `Γ` with `nearOne Γ ≤ F`
(`nearOne Γ` is the pull-back along `j` of the neighbourhoods of `1`), and let `N g` be matrices
over a ring `A` that maps compatibly to ℚ̄_p and `B_dR`. An invertible matrix `U` over `B_dR` with
`N g * j(g) • U = U` for `F`-almost all `g` (with `j(g)` acting entrywise) has a Hodge frame
`IsHodgeFrame F N U Y W k`: a change of basis `Y` of determinant one over ℚ̄_p, integral and fixed
as `IsHodgeFrame` requires, turns `U` into `W · diag (t ^ k i)` with `W` invertible over `B_dR⁺` and
`k : ι → ℤ`.

A variant of the existence of bases of B_dR^+⊗T adapted to the Hodge filtration, for de Rham T. 


## Hodge–Tate frames and jumps of potentially crystalline modules

For `ρ` potentially crystalline (`New.Period.IsPotentiallyCrystalline`) on a free `R`-module with
basis `e`, with `R` algebraic over `ℤ_[p]` and `toGp` of open image, the Hodge–Tate decomposition is
written in matrices.

The frame is the image under θ (`New.Period.thetaBdR`) of a basis adapted to the Hodge filtration
(`New.Period.exists_isHodgeFrame`).


### `inv_mul_apply_of_isHodgeTateFrame`

 The rows of the inverse of an invertible Hodge–Tate frame `P` satisfy
`P⁻¹ N = diag (χ(g) ^ (-k i)) · g(P⁻¹)`. 

### `hasJumps_of_rows`

 Let `R` be algebraic over `ℤ_[p]` and `e` a finite basis of `T`. Let `Q` be invertible over
`ℂ_[p]` with `Q · γ(ρ g) = diag (χ(g) ^ (-k i)) · g(Q)` for `g` near `1`, where `ρ g` is written
as a matrix in the basis `e`. Then the `k i` are the jumps of `ρ` at `γ`, and the `γ`-semilinear
forms whose values on `e` are the rows of `Q` form a basis, the `i`-th in
`New.Period.hodgeTateMaps` for the weight `k i`. 

### `IsPotentiallyCrystalline.top_le_span_fixed`

 Let `ρ` be potentially crystalline and `δ : R → ℚ̄_p` a `ℤ_[p]`-algebra map. Then the vectors
`v : ι → B_dR` with `δ(ρ g) · (toGp g • v) = v` for `g` near `1` span `B_dR ^ ι`; here `ρ g` is
written as a matrix in the basis `e`. This is the implication 'potentially crystalline ⇒
potentially de Rham', in coordinates. 

### `IsPotentiallyCrystalline.exists_isHodgeTateFrame`

 For `toGp` with open image and `R` algebraic over ℤ_p, the Hodge–Tate frame of a potentially
crystalline `ρ` along `γ`: an invertible matrix `P` over `ℂ_[p]` and integers `k i` such that (a)
near `1` the columns of `P` are Hodge–Tate vectors of weights `k` for the matrix of `ρ g` in the
basis `e`; (b) the `k i` are the jumps of `ρ` at `γ`; (c) the semilinear maps whose values on `e`
are the rows of `P⁻¹` form a basis, the `i`-th of weight `k i`. 

### `IsPotentiallyCrystalline.exists_hasJumps`

 Let `toGp` have open image, R be algebraic over Z_p, and T be finite free over R and potentially
crystalline. Then at each γ: R → C_p the jumps of T, with multiplicity, form a multiset of
cardinality the rank of T.

This is the equality between the number of Hodge–Tate weights of a potentially crystalline
representation and its rank (Brinon–Conrad), for R algebraic over Z_p, with weights counted as jumps
at each embedding γ: R → C_p of the coefficients. 


## Hodge–Tate jumps under operations on representations

Here Γ maps to G_p by `toGp`, with open image, and acts on an R-module T; γ : R → ℂ_p is a
ℤ_p-algebra map. `New.Period.hodgeTateMaps ρ γ u` is the Q̄_p-space of γ-semilinear forms f on T
with f(g x) = χ(g)^(−u) · g f(x) for g near 1 (`New.Period.nearOne`), and `New.Period.jump ρ γ u`,
its dimension, is the multiplicity of the jump u; so χ^c has the jump −c.

* `New.Period.jump_baseChange`, `New.Period.jump_twist_of_period`: extension of scalars, twists.
* `New.Period.exists_jump_bound`: the jumps at γ are bounded.
* `New.Period.jump_eq_of_pairing`: duals.


 ### Pull-back of forms, base change and twists 

### `hodgeTateMaps.pull`

 For a φ-semilinear map i: T' → T equivariant near 1, the Q̄_p-linear map f ↦ f∘i between the
spaces `New.Period.hodgeTateMaps` for u, of T at γ and T' at γ' = γ∘φ. 

### `jump_baseChange`

 Extension of scalars. Let R' be algebraic over Z_p, and let f: T → T' be semilinear along φ:
R → R', map a basis to a basis, and be equivariant near 1. Then the jump u has the same multiplicity
for T' at γ' as for T at γ'∘φ; T need not be potentially crystalline. This is the invariance of
Hodge–Tate weights under extension of coefficients. 

### `jump_twist_of_period`

 If ρ'(g) = a(g)ρ(g) with scalars a(g) in R, and some nonzero y in C_p has γ(a(g))y = χ(g)^(−v)·g
y near 1, then the multiplicity of the jump u+v of ρ' at γ equals that of u for ρ. 

 ### Bounds, duals and cyclotomic twists 

### `jump_eq_zero_iff`

 For `toGp` with open image and T finite over R, the jump u has multiplicity zero at γ exactly
when there is no non-zero form of weight u. 

### `exists_jump_bound`

 For `toGp` with open image and T finitely generated over R, there is a natural number a such
that every jump k of T at γ (nonzero multiplicity) satisfies −a ≤ k ≤ a. 

### `jump_eq_of_pairing`

 Let R be algebraic over Z_p, `toGp` have open image, and T be finite free and potentially
crystalline (`hρ`). Let b: T' → Hom_R(T,R) be bijective with b(gx,gy) = χ(g)^c b(x,y). Then the
jump u of T' at γ has the multiplicity of the jump −u−c of T. This is the rule for Hodge–Tate
weights under a perfect pairing into a cyclotomic twist. 

### `hasJumps_of_cyclotomicGp_zpow`

 For R algebraic over Z_p, `toGp` with open image and T finite free over R, if ρ(g)x = χ(g)^c x
for all g and x, then the only jump at γ is −c, with multiplicity the rank of T. 

### `jump_twist_cyclotomicGp`

 Let Γ be a group with an open-image map to Gal(Q̄_p/Q_p), and let ρ, ρ' be representations of Γ
on an R-module T, where R is a ℤ_p-algebra. Suppose ρ' is the twist of ρ by
the c-th power of the p-adic cyclotomic character χ pulled back to Γ, that is, ρ' g x = χ(g)^c • ρ g
x. Then for every ℤ_p-algebra map γ : R → ℂ_p, the multiplicity `jump ρ' γ (u - c)` of the
Hodge–Tate jump u − c of ρ' at γ equals the multiplicity `jump ρ γ u` of the jump u of ρ. 

 ### Modules that map to a family S_i 

### `top_le_span_pullback`

 Under the independence hypothesis `h_indep`, for any bases b_i of the δ_i-semilinear forms on
S_i, the pull-backs b_{i,y} ∘ f_i span over ℂ_p all γ'-semilinear forms on T'. 

### `exists_jump_of_linearIndependent`

 Let `toGp` have open image, R be a domain algebraic over Z_p, and each S_i be finite free and
potentially crystalline over R (`h_potCrys`). Let f_i: T' → S_i be φ-semilinear and equivariant
near 1 (`h_equiv`), with δ_i∘φ = γ'. Let e be a finite basis of T'. Suppose (`h_indep`) that the
vectors (δ_i(l(f_i e_a)))_{i,l}, indexed by a, are ℂ_p-independent, where l runs over the
coordinates of S_i. Then every jump of T' at γ' is a jump of some S_i at δ_i. 

### `exists_jump_of_jointly_injective`

 Let R be a domain algebraic over Z_p, `toGp` of open image, and T finite free with jointly
injective (`h_inj`) equivariant (`hf`) R-linear maps f_i to finitely many finite free potentially
crystalline S_i (`h_potCrys`). Then every jump of T at γ is a jump of some S_i at γ.

This is a weak form, without multiplicities, of the additivity of Hodge–Tate weights in exact
sequences. 

 ### Restriction of scalars from R to ℤ_p 

### `linearIndependent_algHom_coord`

 Let R ⊃ Z_p be an algebraic domain and each S_i finite free over R. Let the f_i: T' → S_i be
Z_p-linear and jointly injective, and let (e_a) be a finite Z_p-basis of T'. Then the vectors
v_a = (γ(l-th coordinate of f_i e_a))_{i,γ,l} are C_p-linearly independent, where γ runs over the
Z_p-algebra maps R → C_p. 

### `asSemilinear`

 For Z_p-linear maps f_i: T' → S_i and a pair (i, k) in ι × κ, the map f_i regarded as semilinear
along the structure map Z_p → R; it does not depend on k. 

### `instance : RingHomCompTriple (algebraMap (ℤ_[p]) R) (toRingHom γ) (toRingHom (ofId ℤ_[p] ℂ_[p]))`

 Composing the structure map ℤ_p → R with γ gives the structure map ℤ_p → ℂ_p. 

### `instance : Fintype (R →ₐ[ℤ_[p]] ℂ_[p])`

 The ℤ_p-algebra maps R → ℂ_p, finitely many as R is finite over ℤ_p, form a `Fintype`. 

### `card_algHom_eq_finrank`

 A domain R that is finite free over ℤ_p has rank_{ℤ_p} R embeddings into ℂ_p over ℤ_p. 

### `IsPotentiallyCrystalline.sum_jump_eq_jump_overZp`

 Let `toGp` have open image, R be a domain finite free over ℤ_p, and T be finite free over R and
potentially crystalline. With γ running over the ℤ_p-algebra maps R → ℂ_p: (a) the multiplicity of
the jump u of T as a ℤ_p-module is ∑_γ jump_γ(u); (b) for ζ ∈ R and w ∈ ℂ_p, a set F of ℤ_p-linear
forms f of weight u with f(ζt) = w·f(t) spans over ℂ_p a space of dimension at most the sum of
jump_γ(u) over the γ with γ(ζ) = w. Part (a) is the formula for the graded dimensions of D_dR as a
sum over the embeddings of the coefficients. 
