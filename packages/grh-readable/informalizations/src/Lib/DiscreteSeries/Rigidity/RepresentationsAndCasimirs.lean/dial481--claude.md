---
{
  "module": "src/Lib/DiscreteSeries/Rigidity/RepresentationsAndCasimirs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Rigidity/RepresentationsAndCasimirs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Rigidity/RepresentationsAndCasimirs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# gl_n-modules, unitary representations of U(J) and a Casimir bound on K-highest vectors

This file treats representations of the unitary group `New.U J` (the matrices g with gᴴJg = J) and
modules over `gl n` (`New.GlModule`), where `E_ab` acts by `New.GlModule.E`. Signs `ε : n → ℤˣ` fix
the compact subgroup `K`. They split `gl n` into 𝔨, spanned by the `E_ab` with `ε_a = ε_b`, and 𝔭,
spanned by the others. An integer vector `l` (a `New.HCParam ε`, read as 2λ) orders the indices, and
`E_ab` raises when `l_b < l_a`. For a symmetric relation r on the indices, `New.twoRho l r` is the
sum of the roots e_a − e_b with r(a, b) that are positive for this order. `New.GlModule.casimirK` is
the sum of `E_ab E_ba` over the pairs with `ε_a = ε_b`. For the constant sign it is the full Casimir
operator of `gl n`. κ_λ = |λ|² − |ρ|² is `New.HCParam.casimirValue l`, where ρ in this formula is
the half sum of the positive roots.

## Main definitions and results

* `New.GlModule`: a module over the Lie algebra of complex matrices; `New.GlModule.E` is the action
  of an elementary matrix, `New.GlModule.casimir` and `New.GlModule.casimirK` are Casimir operators.
* `New.IsUnitaryRep`: a representation on a normed space that is strongly continuous, of polynomial
  growth, and preserves a positive definite hermitian form.
* `New.IsDerivedAction`, `New.GlModule.IsCoeffMap`: the module is the derivative of a
  representation, or of a family of linear maps indexed by the group, along `New.expU` (the matrix
  exponential).
* `New.IsUnitaryCasimirGe`: the inner product is invariant, ⟨E_ab v, w⟩ = ε_a ε_b ⟨v, E_ba w⟩, and
  the full Casimir operator is bounded below by κ_λ.
* `New.HCParam.IsKHighest.casimirK_eq_smul`: if `l.HasGap g`, the Casimir operator of 𝔨 acts on a
  K-highest vector by `New.HCParam.casimirKValue`.
* `New.HCParam.IsKHighest.sum_card_sq_add_mul_nonneg`: if `l.HasGap g`, the inner product is
  invariant and the full Casimir operator is bounded below by κ_λ, a nonzero K-highest vector of
  weight Λ + ν gives Σ_a (n² + ν_a(ν_a + l_a)) ≥ 0, that is, |ν|² + 2⟨ν, λ⟩ ≥ −n³.

## Relation to the literature

Lowest K-type and Casimir value are known to determine a discrete series coefficient, via analytic
vectors. See `Lib.DiscreteSeries.Rigidity.HighestVectorsAndFiltration`.



## Modules over gl_n and unitary representations of unitary groups

* `New.HCParam.IsKHighest`, `New.HCParam.rootCone`: `K`-highest vectors and the cone of positive
  roots.


### `GlModule`

 A gl_n(ℂ)-module structure on a complex vector space M: a linear map from n×n matrices to
endomorphisms of M that respects commutators. 

### `GlModule.ρ`

 The action: a linear map from complex `n × n` matrices to endomorphisms of `M`. 

### `GlModule.map_bracket`

 The action takes the commutator of two matrices to the commutator of their operators. 

### `IsUnitaryRep`

 The representation π of U(J) on X is strongly continuous with ‖π(g)‖ ≤ c‖g‖^A, and the
bounded form B is hermitian, positive definite and π-invariant. 

### `IsUnitaryRep.continuous`

 `π` is strongly continuous: each orbit map `g ↦ π g x` is continuous. 

### `IsUnitaryRep.invariant`

 The form `B` is invariant under `π`. 

### `IsUnitaryRep.conj_symm`

 The form `B` is hermitian. 

### `IsUnitaryRep.pos`

 The form `B` is positive definite. 

### `IsUnitaryRep.growth`

 Polynomial growth: ‖π(g)‖ ≤ c‖g‖^A for a constant `c`, with the ℓ² operator norm of `g`. 

### `GlModule.E`

 For a gl_n-module and indices a, b, the endomorphism by which the elementary matrix E_{ab}
acts. 

### `GlModule.restrictTo`

 For a gl_n(ℂ)-module and a subspace stable under all X, the gl_n(ℂ)-module structure on that
subspace obtained by restricting the action. 

### `IsDerivedAction`

 The gl_n-module ρ on M is the derivative of π along ι: d/dt π(exp tY)ιv at t = 0 equals
ι(ρ(Y)v) for Y in Lie U(J), v in M. 

### `GlModule.IsCompactPrimitive`

 The vector x is killed by the compact raising operators for l: E_ab x = 0 whenever ε_a = ε_b
and l_b < l_a. 

### `HCParam.IsKHighest`

 `x` is a `K`-highest vector of weight `ν`: each `E a a` acts on it by `ν a`, and it is killed by
the compact raising operators, the `E a b` with `ε a = ε b` and `l b < l a`. The vector `0` is
allowed. 

### `HCParam.rootCone`

 The cone of the positive roots for the order given by `l`, described by duality: the integer
vectors `β` with `o ⬝ᵥ β ≤ 0` for every integer vector `o` that strictly reverses the order of
`l` (`l j < l i` implies `o i < o j`). A root `e_a - e_b` with `l b < l a` pairs with such an
`o` to `o a - o b < 0`, so sums of these roots lie in the cone. 

### `GlModule.IsCoeffMap`

 The maps c(g) : M → X form a coefficient map for ρ: for Y in Lie U(J), the derivative of
t ↦ c(g exp tY)v is c(g exp tY)(ρ(Y)v). 

### `GlModule.casimir`

 For a relation r on indices, the endomorphism Σ E_ab E_ba of a gl_n-module, summed over the
pairs (a,b) with r(a,b). 

### `GlModule.casimirK`

 The Casimir operator of K: the endomorphism Σ E_ab E_ba of a gl_n-module, summed over the
index pairs with ε_a = ε_b. 


## Invariant inner products, twists and the filtration M_s

* `New.HCParam.casimirKValue`: the number |ν + ρ_c|² − |ρ_c|², with 2ρ_c given by `New.twoRho`.


### `IsUnitaryCasimirGe`

 The inner product of the gl_n-module H is invariant under 𝔲(diag ε), and the full Casimir
operator Ω = `ρ.casimirK 1` is bounded below by κ_λ = `l.casimirValue`, which is
|λ|² − |ρ|². 

### `IsUnitaryCasimirGe.inner_E_left`

 Invariance: ⟨E_ab v, w⟩ = ε_a ε_b ⟨v, E_ba w⟩, so E_ab has the adjoint ε_a ε_b E_ba. 

### `IsUnitaryCasimirGe.casimirValue_mul_le`

 The Casimir bound: κ_λ‖y‖² ≤ Re⟨y, Ωy⟩. 

### `HCParam.casimirKValue`

 The integer |ν+ρ_c|² − |ρ_c|², where ρ_c is the half sum of the compact roots (ε_a = ε_b)
that are positive for the order of l. 

### `adTwist`

 The twist of a gl_n-module by an invertible matrix g: X acts as gXg⁻¹ does in the original
module. 

### `word`

 For a list of index pairs (a₁,b₁),…,(a_s,b_s), the endomorphism E_{a₁b₁}⋯E_{a_s b_s} of M,
the product taken in list order. 

### `filtration`

 The filtration M_s generated by x: M_0 = U(𝔨)x, the least subspace containing x stable under
the E_ab with ε_a = ε_b, and M_{s+1} = M_s + Σ E_ab M_s. 


## Commutation relations and Casimir operators on the filtration

* `New.GlModule.casimirK_one_adTwist`: the full Casimir operator is unchanged by the twist
  `New.GlModule.adTwist`.


### `E_apply_E_apply`

 The commutation relation of the matrix units on a vector: E_ab E_cd v is E_cd E_ab v plus E_ad v
if b = c, minus E_cb v if d = a. 

### `commute_E_sum_E_mul_mul_E`

 If ε_a = ε_b and E_ab commutes with D, then E_ab commutes with the sum over all c, d of
f(ε_c, ε_d) E_cd D E_dc, for any coefficients f that depend only on the signs. 

### `casimirK_one_adTwist`

 The Casimir operator of gl_n is unchanged by twisting the module with an invertible matrix. 

 ### The filtration generated by a vector 

### `E_mem_filtration`

 For ε_a = ε_b, every step M_s of the filtration is stable under E_ab. 

### `casimirK_eq_smul_of_mem_filtration`

 If the Casimir operator of 𝔨 acts on x by the scalar c, it acts by c on every y in U(𝔨)x. 

### `generatedModule`

 The gl_n-module U(gl_n)x generated by x: the least subspace that contains x and is stable under
all E_ab, with the restricted action. 

### `casimirK_generatedModule`

 If the full Casimir operator acts on x by the scalar c, it acts by c on the whole module
U(gl_n)x generated by x. 


## Casimir values on K-highest vectors and the bound for weights Λ + ν

The Casimir operators evaluated on K-highest vectors (`New.HCParam.IsKHighest`: E_aa x = ν_a x, and
E_ab x = 0 when ε_a = ε_b and l_b < l_a).


### `HCParam.IsKHighest.of_E_eq_smul`

 A vector x of the gl_n-module σ is K-highest of weight ν if E_ab acts on it by ν_a for a = b,
and by 0 for a ≠ b with ε_a = ε_b and l_b ≤ l_a. 

### `GlModule.casimir_eq_diag_add_twoRho_add`

 For a gl_n-module σ, a symmetric relation r on the indices and an integer vector l with distinct
entries, the Casimir sum `σ.casimir r` = Σ_{r(a,b)} E_ab E_ba equals Σ_{r(a,a)} E_aa² + Σ_a (2ρ_r)_a
E_aa + 2 Σ_{r(a,b), l_a < l_b} E_ab E_ba. Here 2ρ_r = `twoRho l r` has a-th entry #{b : r(a,b),
l_b < l_a} − #{b : r(a,b), l_a < l_b}. 

### `HCParam.IsKHighest.casimirK_eq_smul`

 If `l.HasGap g` (the entries of l are distinct, of the parity of n − 1, and at least 2g apart
where the signs differ; only distinctness is used here), the Casimir operator of 𝔨 acts on a
K-highest vector of weight ν by |ν + ρ_c|² − |ρ_c|² (`New.HCParam.casimirKValue`). 

### `IsUnitaryCasimirGe.inner_casimir`

 If ρ satisfies `New.IsUnitaryCasimirGe` (only the invariance of the inner product is used),
⟨x, `ρ.casimir r` x⟩ is the sum of ε_a ε_b ‖E_ba x‖² over the pairs with r(a, b). 

### `HCParam.IsKHighest.sum_card_sq_add_mul_nonneg`

 Casimir bound. Let l = 2λ satisfy `l.HasGap g`: distinct entries of the parity of n − 1, at
least 2g apart where the signs differ. Let ρ be a module with an invariant inner product such that
Re⟨y, Ωy⟩ ≥ κ_λ‖y‖² for all y (together these are `New.IsUnitaryCasimirGe`); Ω is the full
Casimir operator and κ_λ = |λ|² − |ρ_G|², with ρ_G the half sum of the roots positive for l. Let
x ≠ 0 be K-highest of weight Λ + ν, with Λ = `l.lowestKType` = λ + ρ_G − 2ρ_c. Then
Σ_a (n² + ν_a(ν_a + l_a)) ≥ 0, that is, |ν|² + 2⟨ν, λ⟩ ≥ −n³. 
