---
{
  "module": "src/New/Congruences/FirstOrder/HeckeStrings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/HeckeStrings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/HeckeStrings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chains of roots for weak lifts, and Hecke-stable subspaces of forms

Let `O` be a descent pair, with spaces W and V of ranks r < n, put t = n − r, and let `f` be a
nonzero eigenform on V with Galois representation R. Its normalised representation is u = R ⊗ χ. The
case of interest is that det (1 − u(g)) = 0 for all g, the condition that defines weak lifts.

Notions from other files:
* `New.Parameters`, `New.Data`: the fixed parameters P and admissible data D over them (numerical
  scales, ranks, levels); D determines the CM field E = `D.E`.
* `New.DescentPair`: places, weights and a hermitian space W of rank r, beside the definite space
  V = `New.stdSpace` of rank n > r; `New.DescentPair.rankDiff` is t = n − r. The forms on V have
  the weight (`columnCount`, `detExp`): column numbers and a power of the determinant at each
  infinite place.
* `New.Patching.Isotypic`: spaces of forms with given Hecke eigenvalues at almost all places; such a
  space `x` has Hecke polynomials `x.heckePolyAt w` and a Galois representation `x.galRep`.
* `New.Selmer.normalisedRep`: the twist of a Galois representation by the ℓ-adic character
  χ = `New.Selmer.normalizingAvatar`, the avatar of an algebraic Hecke character made from W.
* `Ω`: a fixed algebraic closure of ℚ, so that Gal(Ω/E) is the absolute Galois group of E.
* `New.mostFrobenii`: a filter on the triples of a place, a place of `Ω` over it and a geometric
  Frobenius element there.
* `ιℓ`: the fixed isomorphism ι from `ℂ` to `ℚ̄_ℓ`.

## Main definitions and results

* `New.Selmer.exists_diagonal_mem_norm_ge`: diagonal operators, one for each vector of a basis, are
  combined into one operator with an eigenvalue at each vector at least as large in norm.
* `New.Selmer.isRoot_hecke_chain`: if det (1 − u(g)) = 0 for all g, the Hecke polynomial at a split
  place w ∤ ℓ has the chain of roots X₀, X₀q, …, X₀q^(t−1), where q is the norm of w and
  ι(X₀) = χ(Frob_w)⁻¹.
* `New.Selmer.eventually_exists_hasRootChain`: for most Frobenius elements φ, if u has integral
  characteristic polynomials with root 1 and that of u(φ) is congruent to a product of S and ∏_{j<t}
  (X − c(φ)^j), with c the inverse cyclotomic character, for a polynomial S with ‖S(1)‖ ≥ 1, the
  rescaled Hecke polynomial is ∏ (X − q^i) times a divisor of an integral polynomial with value 1 at
  1.
* `New.Selmer.orthogonal_mem_invtSubmodule_heckePolyOnForms`, `New.Selmer.le_of_isotypic_mem`: the
  orthogonal complement of a Hecke-stable subspace Z is Hecke stable, and Z lies in a subspace N
  once every nonzero form of Z in an isotypic space lies in N.



## A single operator from several diagonal operators

Take operators that are diagonal in one basis, one for each basis vector. Some integral combination
has at every basis vector an eigenvalue of norm at least that of the operator chosen for it, since
finitely many hyperplanes do not cover a space over the infinite residue field of `ℚ̄_ℓ`.


### `New.Selmer.exists_integral_combination_norm_ge`

 For a square array `l p k` of elements of `ℚ̄_ℓ` there are coefficients `d p` of norm at most
one such that, for every `k`, the combination `∑ p, l p k * d p` has norm at least `‖l k k‖`. 

### `New.Selmer.exists_diagonal_mem_norm_ge`

 Let `Good` be a set of operators on `Z` that contains every combination of `m` of its members
with `ℓ`-adically integral coefficients. If for each `k` the operator that is diagonal in the basis
`b` with eigenvalues `l k` lies in `Good`, then some operator in `Good`, diagonal in `b`, has
eigenvalues `μ k` with `‖μ k‖ ≥ ‖l k k‖` for every `k`. Norms are `ℓ`-adic, through the fixed
isomorphism `ιℓ` from `ℂ` to `ℚ̄_ℓ`. 

### `New.Selmer.pow_finrank_le_nnnorm_det`

 Let `Λ` be an operator on a complex space `Z` of finite dimension `N`, and `ιℓ` the fixed
isomorphism from `ℂ` to `ℚ̄_ℓ`. If `c * ιℓ μ` has norm at least `ε` for every eigenvalue `μ` of
`Λ`, then `c ^ N * ιℓ (det Λ)` has norm at least `ε ^ N`. 


## The Hecke polynomial as a chain times an integral factor

Congruences are coefficientwise modulo the maximal ideal of the integers of ℚ̄_ℓ (norm < 1).


### `norm_coeff_lt_one_of_mul_monic`

 If `R` is monic and all coefficients of `Q * R` have norm less than one, then so do all
coefficients of `Q`. 

### `exists_integral_multiple_eval_one`

 Let B be monic, C integral, AB ≡ C ≡ A'B coefficientwise modulo the maximal ideal of the
integers `intQpBar ℓ` of ℚ̄_ℓ, and ‖A'(1)‖ ≥ 1. Then A divides an integral polynomial e with
e(1) = 1. 

### `exists_one_le_nnnorm_one_sub_pow_mul_root`

 Let p be a nonzero polynomial over ℚ̄_ℓ, and let y^j − 1 have norm one for 1 ≤ j ≤ deg p. Then
for some i every root μ of p has ‖1 − y^i μ‖ ≥ 1, that is, y^i μ is not congruent to one modulo the
maximal ideal. 

### `exists_eventually_one_le_norm_eval_charpoly`

 Let `P` be fixed parameters and `D` data for them, which determine a CM field E = `D.E`. Let
`AbsGal D` = Gal(Ω/E) be its absolute Galois group, with Ω an algebraic closure of E. Let T be a
continuous function from this group to n × n matrices over ℚ̄_ℓ. Let δ_i be a sequence of elements
of the group with T(δ_i) = y^i A, and let y^j − 1 have norm one for 1 ≤ j ≤ 4n + 2. Then for some i,
‖det(1 − T(φ))‖ ≥ 1 for all φ near δ_i. 

### `norm_coeff_comp_sub_charpoly_smul_lt_one`

 Let M be an n × n matrix over ℚ̄_ℓ and u a number of norm one. Call two numbers congruent if
their difference has norm less than one, that is, lies in the maximal ideal. If the i-th
coefficients of H and of char M are congruent, then so are those of u^n·H(u⁻¹X) and char (uM). 

### `normalizingAvatar_eq_of_isFrob`

 If s⁻¹ is an arithmetic Frobenius at a place `A` of `Ω` over w ∤ ℓ, that is, s is a geometric
one, then χ(s) = ι(X₀⁻¹), where X₀ = `O.charW.frobValue r w` and ι = `ιℓ` is the fixed isomorphism
from ℂ to ℚ̄_ℓ. 

### `isRoot_hecke_chain`

 Let `f` be a nonzero form on the definite space V of highest weight `(O.columnCount, O.detExp)`:
column numbers and a power of the determinant at each infinite place. Let `f` lie in the isotypic
space `x`, a space of forms with given Hecke eigenvalues at almost all places. Let
χ = `normalizingAvatar O` be the ℓ-adic character attached, via ιℓ, to the Hecke character of W.
Assume every g in Gal(Ω/E) has eigenvalue 1 on `normalisedRep O x.galRep`, the twist of `x.galRep`
by χ. Let w ∤ ℓ be a split place of norm q where `f` has Hecke polynomial S. Then each X₀q^i with
i < n − r is a root of S. Here X₀ = `O.charW.frobValue r w` is the inverse of χ at a geometric
Frobenius, read in ℂ. 

### `prod_X_sub_C_dvd_comp_of_hasHeckePolyAt`

 Let `O` be a descent pair, `f` a nonzero form on V in the space `x` of forms of weight
`(O.columnCount, O.detExp)` with given Hecke eigenvalues, and let every g in Gal(Ω/E), Ω an
algebraic closure of ℚ, have the eigenvalue 1 on the twist of `x.galRep` by the ℓ-adic character
χ = `normalizingAvatar O`. Let σ = `y.frob` be a geometric Frobenius at a split place w = `y.place`,
w ∤ ℓ, of norm q, where `f` has Hecke polynomial H, and ι = `ιℓ` the fixed isomorphism from ℂ to
ℚ̄_ℓ. Then ∏_{i<n−r}(X − q^i) divides H(ι⁻¹(χ(σ))⁻¹·X). 

### `eventually_exists_hasRootChain`

 Let `O` be a descent pair, `f` a nonzero form on V in the space `x` of forms with given Hecke
eigenvalues, and u the twist of `x.galRep` by the ℓ-adic character χ = `normalizingAvatar O`. Assume
that all characteristic polynomials of u are integral and have the root 1. Write t = `O.rankDiff` (=
n − r), ι = `ιℓ` for the isomorphism from ℂ to ℚ̄_ℓ and c = `cyclotomicInv` for the inverse
cyclotomic character. The following holds for most geometric Frobenius elements φ = `y.frob`, at
places w = `y.place`: every nonempty open subset of Gal(Ω/E) has a nonempty open part in which it
holds for almost all w. If det (X − u(φ)) is congruent, coefficientwise modulo the maximal ideal, to
S · ∏_{i<t} (X − c(φ)^i) with ‖S(1)‖ ≥ 1, then the rescaled Hecke polynomial H_w(X₀X) of `x`,
X₀ = ι⁻¹(χ(φ))⁻¹, is the chain ∏_{i<t} (X − q_w^i) times a divisor of an ℓ-adically integral
polynomial e with e(1) = 1 (`HasRootChain`). 


## Hecke-stable subspaces of forms: orthogonal complements, eigenforms

Hecke-stable subspaces Z of the space `New.DescentPair.FormV` of forms on the definite space V of a
descent pair (`New.DescentPair`); `New.DescentPair.heckePolyOnForms` is the Hecke polynomial at a
split place as an operator.


### `orthogonal_mem_invtSubmodule_heckePolyOnForms`

 Let `O` be a descent pair over the CM field E = `D.E` of admissible data `D`, and `Z` a subspace
of `O.FormV`, the forms of the level and weight of `O` on its definite space, with their inner
product. For a split place w the operator `O.heckePolyOnForms` is the Hecke polynomial
∑ᵢ (−X)^i q^(i(i−1)/2) T_{w,i}, evaluated at the complex number `X`. If `Z` is stable under these
operators for all X at all split w off the places of `O` and their conjugates, then so is its
orthogonal complement. 

### `le_of_isotypic_mem`

 Let `O` be a descent pair over the CM field E = `D.E` of admissible data `D`, and `Z`, `N`
subspaces of `O.FormV`, the forms of the level and weight of `O` on its definite space
V = `stdSpace D.E n`. Let `Z` be stable under the Hecke polynomial operators `O.heckePolyOnForms`,
evaluated at any complex X, at all split places off the places of `O` and their conjugates. If every
form of `Z` that, viewed as a smooth form on V, is nonzero and lies in an isotypic space lies in
`N`, then `Z ≤ N`. 
