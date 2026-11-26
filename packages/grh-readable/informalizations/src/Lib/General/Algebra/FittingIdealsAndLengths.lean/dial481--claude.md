---
{
  "module": "src/Lib/General/Algebra/FittingIdealsAndLengths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/FittingIdealsAndLengths.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/FittingIdealsAndLengths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relations, relative lengths and Fitting ideals for Selmer group estimates

This file gives linear algebra for the Selmer group estimates. Conditions on a function `c : Γ → Bⁿ`
are written as relations: finitely supported matrix-valued `f` on `Γ` acting by `c ↦ ∑ γ, f γ • c γ`
(`New.relEval`). Sizes are lengths of modules in `ℕ∞`, and `addVal` is the valuation of a discrete
valuation ring, normalised to be 1 at a uniformiser. The zeroth Fitting ideal of a quotient is
controlled as relations are added.

## Main definitions and results

* `New.obeying R B`: the functions with values in `Bⁿ` killed by all relations in `R`. For
  `New.cocycleRelations ρ` these are the cocycles (`New.mem_obeying_cocycleRelations`).
* `New.relLength S T`: the length of `S / (S ⊓ T)`, with its monotonicity and additivity rules.
* `New.length_obeying_relationsOn_le`: the relations `New.relationsOn Z` of a finitely generated `Z`
  cut out a module of length at most `rank Z * length B`.
* `New.length_ker_le_addVal_det`, `New.exists_matrix_addVal_det_le_length`: lengths compared with
  valuations of determinants.
* `New.Lift.relLength_le_of_relations`: if `p ^ t L ≤ L'` and any `m + 1` elements of `L` killed by
  `p` modulo `L'` have a combination in `L'` with some coefficient `1`, the length of `L` modulo
  `L'` is at most `t m`.
* `New.Selmer.fittingIdeal.exists_addVal_le_relLength`: if `p ≠ 0`, `R` is Noetherian and
  `Φ (p • v) ∈ N` for all `v`, then for a condition `V` on the linear forms modulo `p`, some `c` of
  valuation at most the length modulo `V` of the forms that vanish on `Φ⁻¹ N` multiplies the Fitting
  ideal of an enlargement `K` of `N` into that of `N`; here `K` contains `Φ v` for every `v` killed
  by all the forms that satisfy `V`.

## Relation to the literature

Three standard properties of Fitting ideals are proved in the cases that are used, for fixed
generators: base change (Stacks Project, Tag 07ZA), the product rule for an exact sequence, and the
bound by a length.



## Modules cut out by matrix relations, their lengths and determinants

The classes `New.DVR` and `New.PadicIntegerRing` describe the coefficient rings: a discrete
valuation ring, and the integer ring of a finite extension of `ℚ_ℓ`.


### `DVR`

 O is a discrete valuation ring (in particular a domain). 

### `QuotSpan`

 The quotient ring O/aO. 

### `PadicIntegerRing`

 O is a discrete valuation ring of characteristic 0, finite and free over ℤ_ℓ, with finite
quotients by nonzero ideals: the integer ring of a finite extension of ℚ_ℓ. 

 ### Relations, the functions they kill, and lengths modulo a submodule 

### `relEval`

 Evaluation of relations. A finitely supported function `f` from `Γ` to `n × n` matrices over
`O` is sent to the `O`-linear map `c ↦ ∑ γ, f γ • c γ` from functions `Γ → Bⁿ` to `Bⁿ`. The
dependence on `f` is linear over the matrix ring. 

### `obeying`

 The submodule of the functions `c : Γ → Bⁿ` killed by every relation `f` in `R`, that is, with
`∑ γ, f γ • c γ = 0` in `Bⁿ`. 

### `mapRel`

 The matrix-valued finitely supported function obtained from f by applying the ring
homomorphism e: O → O' to every matrix entry. 

### `relationsOn`

 The linear relations of Z: the finitely supported matrix-valued f on Γ with Σ_γ f(γ)z(γ) = 0
in O^n for all z in Z. 

### `relLength`

 The length of S/(S ∩ T) as an A-module, for submodules S, T of M. 

### `relLength_iInf_le`

 The length of `S` modulo an intersection is at most the sum of its lengths modulo each of the
finitely many submodules intersected. 

### `relLength_add_length_inf`

 The length of `S` is the sum of its length modulo `T` and the length of `S ⊓ T`. 

### `comp_mem_obeying_iff`

 A linear map `φ` applied coordinatewise to `c : Γ → Bⁿ` gives a function killed by all the
relations in `R` if and only if `φ` kills each coordinate of `∑ γ, f γ • c γ` for `f ∈ R`. 

### `mkQ_mem_obeying_relationsOn`

 The reduction modulo `a` of a function `z ∈ Z` is killed by all linear relations of `Z`. 

### `cocycleRelations`

 The set of matrix-valued relations, one for each pair (g, h), expressing the cocycle
identity c(gh) = c(g) + ρ(g)c(h). 

### `mem_obeying_cocycleRelations`

 A function `c : Γ → Bⁿ` is killed by the cocycle relations of `ρ` if and only if it satisfies
the cocycle identity `c (g * h) = c g + ρ g • c h`. 

 ### Maps and monotonicity of relative lengths 

### `relLength_le_of_mapsTo`

 If a linear map `f` maps `S` into `S'` and every point of `S` mapped into `T'` lies in `T`,
then the length of `S` modulo `T` is at most that of `S'` modulo `T'`. 

### `length_le_of_le_map`

 A submodule contained in the image of `S` under a linear map has length at most that of `S`. 

 ### Length bounds over a discrete valuation ring 

### `length_obeying_relationsOn_le`

 Let `O` be a discrete valuation ring, `n` a nonempty finite type, `B` an `O`-module and `Z` a
finitely generated `O`-module of functions `Γ → Oⁿ`. A relation on `Z` is a finitely supported
family `f` of `n × n` matrices over `O` with `∑ γ, f γ * z γ = 0` for all `z ∈ Z`. The functions
`c : Γ → Bⁿ` with `∑ γ, f γ • c γ = 0` for every such relation form a submodule of length at most
`finrank O Z * length O B`. 

### `length_ker_le_addVal_det`

 For a square matrix M over a discrete valuation ring O and p in O, the kernel of M acting on
(O/p)^n (the endomorphism `M • 1`) has O-length at most the valuation of det M, normalised so that a
uniformiser has valuation 1. It is a consequence of the theorem on elementary divisors. 

### `OddPart.length_le_of_detecting_points`

 Let `O` be a discrete valuation ring, `B ≅ O/p` a cyclic `O`-module and `Z` an `O`-module of
functions from `Γ` to `B`. If `n i • z (q i) = 0` for all `z ∈ Z`, and only `0` vanishes at all
the finitely many points `q i`, then the length of `Z` is at most the valuation of `∏ n i`. 

### `exists_matrix_addVal_det_le_length`

 Let O be a discrete valuation ring and aO^n ⊆ L ⊆ O^n, a ≠ 0. There are a square matrix M with
rows in L and a submodule S of (O/a)^n whose annihilator in O^n is exactly L, with the valuation of
det M at most the length of S.

It is a consequence of the theorem on elementary divisors. 


## Relative lengths of p-adic integer modules

Lemmas on `New.relLength L L'`, the length of `L / (L ⊓ L')` ("the length of `L` modulo `L'`"), for
`ℤ_p`-submodules `L`, `L'`, `L''` of a module `V`, where `p` is a prime natural number (not the
`p : O` used above) and `m`, `n` are natural numbers.


### `relLength_trans`

 If `L` has length at most `m` modulo `L'` and `L'` has length at most `n` modulo `L''`, then
`L` has length at most `m + n` modulo `L''`. 

### `relLength_le_of_prime_smul_mem`

 Let `T` be a submodule with `p T ≤ L'`. If any `m + 1` elements `x j` of `T` have a combination
`∑ a j • x j` in `L'` with some coefficient `a j = 1`, then `T / (T ⊓ L')` has length at
most `m`. 

### `relLength_le_of_relations`

 Suppose `p ^ t L ≤ L'`, and that any `m + 1` elements `x j` of `L` with `p x j ∈ L'` have a
combination `∑ a j • x j` in `L'` with some coefficient `a j = 1`. Then `L / (L ⊓ L')` has length
at most `t m`. 


## The Fitting ideal of a quotient under added relations

The zeroth Fitting ideal `New.Selmer.fittingIdeal N` of a quotient `R^ι / N`, defined by
determinants of square matrices with rows in `N`, and how it changes when `N` grows.


### `fittingIdeal`

 The ideal of R generated by the determinants of square matrices with all rows in N ⊆ R^ι:
the zeroth Fitting ideal of R^ι modulo N. 

### `fittingIdeal.sup_smul_top_le`

 Adding the relations `I • ⊤` to `N` changes the zeroth Fitting ideal only modulo `I`: for every
ideal `I`, the Fitting ideal of `N ⊔ I • ⊤` is contained in `fittingIdeal N ⊔ I`.

This is one inclusion of the base change property of Fitting ideals along `R → R ⧸ I`, stated
inside `R`. 

### `mul_det_mem_fittingIdeal`

 If `r • v ∈ N` and each row of the square matrix `s` lies in `N` or is equal to `v`, then
`r * det s` lies in the Fitting ideal of `N`. 

### `fittingIdeal.mul_mem_of_smul_mem`

 If `r • v ∈ N`, then `r * d` lies in `fittingIdeal N` for every `d` in the Fitting ideal of
`N ⊔ R ∙ v`. In other words, adding the vector `v` to the relations costs at most the factor `r`.

This is a case of the inclusion `Fitt(M') * Fitt(M'') ≤ Fitt(M)` for an exact sequence
`M' → M → M'' → 0`: here `M' = R / (r)` maps to `M = R^ι / N` by `1 ↦ v`. 

### `fittingIdeal.exists_ge_mul_prod_mem`

 Let `I` be a finite ordered set of indices. Suppose that for each `j ∈ I`, every submodule
`K ≥ N` that contains the `v i` with `i ∈ I`, `i < j` also contains `r j • v j`. Then there is
`K ≥ N` containing all `v j`, `j ∈ I`, such that `∏ j ∈ I, r j` multiplies `fittingIdeal K` into
`fittingIdeal N`.

This is the submultiplicativity of Fitting ideals along exact sequences, in the form
`fittingIdeal.mul_mem_of_smul_mem`, iterated along the filtration by the `v j`, whose steps are
cyclic modules killed by the `r j`. 


## Linear forms modulo p and the cost of a length in the Fitting ideal

Let `O` be a discrete valuation ring, `Φ : O^n → R^ι` an `O`-linear map and `N ≤ R^ι` a submodule
with `Φ (p • O^n) ⊆ N`, `p ≠ 0`. The quotient `O^n / Φ⁻¹ N` is studied through its linear forms with
values in `O / p`.


### `formsMod`

 The module of the functions `g ↦ Ψ (z g)` on `G`, where `Ψ : O^n → O / p` runs over the
`O`-linear maps that vanish on `Φ⁻¹ N`. The values are taken in `Unit → O / p`, vectors of
length one, as for cocycles of a representation of rank one. 

### `mem_formsMod`

 A function lies in `formsMod Φ z N p` if and only if it is `Ψ ∘ z` for an `O`-linear map
`Ψ : O^n → O / p` that vanishes on every `v` with `Φ v ∈ N`. 

### `formsMod_anti`

 Enlarging `N` imposes more conditions on the forms `Ψ`, so `formsMod Φ z N p` shrinks. 

### `mem_of_forall_form_eq_zero`

 Duality. Let `p ≠ 0` with `Φ (p • O^n) ⊆ N`. If every `O`-linear map `Ψ : O^n → O / p` (with
values written in `Unit → O / p`) vanishing on `Φ⁻¹ N` vanishes at `v`, then `Φ v ∈ N`. 

### `exists_pow_smul_notMem_and_succ_mem`

 If `Φ (p • O^n) ⊆ N`, `p` is associated to `ϖ ^ m` and `Φ v ∉ N`, then for some `k` the vector
`Φ (ϖ ^ k • v)` is outside `N` and `Φ (ϖ ^ (k + 1) • v)` is inside. 

### `map_mkQ_formsMod_lt`

 Let `O` be a discrete valuation ring, `R` an `O`-algebra, `Φ : O^n → R^ι` an `O`-linear map
with `n` finite, and `z` a family of vectors of `O^n` indexed by `G`. For `p : O` and a submodule
`N` of `R^ι`, `formsMod Φ z N p` is the module of the functions `Ψ ∘ z` on `G`, where `Ψ` runs over
the `O`-linear forms `O^n → O / p` that vanish on `Φ⁻¹ N`; values in `O / p` are written as vectors
of length one, in `Unit → QuotSpan p`.

Assume `p ≠ 0` and `Φ (p • O^n) ⊆ N ≤ N'`. Let `V` be an `O`-module of functions `G → O / p` and
`v` a vector killed by every form `Ψ` with `Ψ ∘ z ∈ V`. If `Φ (a • v)` lies in `N'` but not in `N`
for some `a : O`, then the image of `formsMod Φ z N' p` in the quotient by `V` is strictly smaller
than the image of `formsMod Φ z N p`. 

### `fittingIdeal.exists_addVal_le_relLength`

 Let `p ≠ 0`, `Φ (p • O^n) ⊆ N`, and let `V` be an `O`-module of functions on `G` with values in
`O / p`. There are `c : O` and `K ≥ N` such that (a) the valuation of `c` is at most the length
modulo `V` of `formsMod Φ z N p`, the functions `g ↦ Ψ (z g)` for the linear `Ψ : O^n → O / p`
that vanish on `Φ⁻¹ N`; (b) `K` contains `Φ v` whenever every linear `Ψ` with `Ψ ∘ z ∈ V` kills
`v`; (c) `c` multiplies `fittingIdeal K`, the zeroth Fitting ideal of `R^ι / K`, into
`fittingIdeal N`.

This is a relative, dual form of the bound of a Fitting ideal by length over a discrete valuation
ring, for Noetherian `R`. 
