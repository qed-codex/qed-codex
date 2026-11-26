---
{
  "module": "src/Lib/ClassField/Avatar/HeckeBaseChange.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Avatar/HeckeBaseChange.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Avatar/HeckeBaseChange.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Base change of U(1) and Hecke characters, their L-functions and parallel twists

Let `E` be a CM field with CM type `Φ`. A character `ν` of `U(1)(𝔸)` trivial on rational points
gives by base change the Hecke character `x ↦ ν(x / x̄)` of `E`. For `e ≠ 0` and `S` finite, its
`L`-function without the factors at `S ∪ S̄` does not vanish at real `s ≥ 1`. Algebraic Hecke
characters are also base changed along the norm.

## Main definitions and results

* `New.AutChar.L`: the Euler product of the base change, without the factors at `S ∪ S̄`.
* `New.AutChar.HasWeight.L_ne_zero`: for `e ≠ 0` and `S` finite, this `L`-function does not vanish
  at real `s ≥ 1`.
* `New.AutChar.HasWeight.toAlgebraic`: the algebraic Hecke character
  `ν(x / x̄) υ(x)^{-k} |x|^{j - k/2}`, with `υ` the splitting character of `New.SplittingChar`.
* `New.Variety.exists_twist_algHeckeChar`: twisting ρ by ω, controlled at the places w where ω is
  unramified and its type is one natural number d. The twist is by χ^d·μ, with χ the cyclotomic
  character and μ the ℓ-adic avatar of ω|·|^(−d), whose type vanishes over w.

Notions from other files:
* `New.AutChar`: The group of continuous circle-valued characters of U(1)(𝔸), the norm-one adeles of
  the CM field E, trivial on elements coming from E.
* `New.HeckeChar`: The group of unitary Hecke characters of E: continuous circle-valued characters
  of the idele group trivial on principal ideles.
* `New.IsHeckeOfType`: The character ψ of the finite ideles is the finite part of a Hecke character
  of type n: its kernel is open and ψ(x) ∏_w (Φ_w(x)/|Φ_w(x)|)^{n_w} = 1 on K^×.
* `New.IsHeckeOfType.toAlgebraic`: the algebraic character `ψ |·|^{k/2}` of infinity type `m`, for
  `ψ` of type `m (Φ w) - m (Φ̄ w)` with `m (Φ w) + m (Φ̄ w) = k` at every infinite place `w`.
* `New.AutChar.HasWeight`: μ has weight e and tame part ψ: almost all residue characters ψ_w are
  trivial, and μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part.
* `New.heckeCoeff` φ S: the value of φ at the chosen uniformiser at v for v outside S, and 0 for v
  in S; `New.eulerProd` a is the Euler product ∏_v (1 - a_v q_v^(-s))⁻¹.

## Relation to the literature

Known; see `Lib.ClassField.HeckeL.ContinuationAtOne`,
`Lib.ClassField.Avatar.LocalGlobalCompatibility` and `Lib.ClassField.Global.CMSplittingCharacters`
for sources.



## Base change of U(1) characters: L-function and algebraicity

Conventions: `ν.HasWeight e ψ` says that `ν` has weight `e` at infinity and tame part `ψ` (one
character `ψ w` of each residue field). `star` is complex conjugation, also on places. `χ.finPart`
is the restriction to finite ideles, and `χ.atUniformizer w` is the value at the chosen uniformiser
at `w`.


### `AutChar.L`

 The Euler product of the character `x ↦ ν (x / x̄)` of `E`, without the factors at `S ∪ S̄`.
It is the partial Hecke `L`-function if `S ∪ S̄` contains the ramified places. 

### `baseChange_mul_upsilon_zpow_inv_apply`

 Let `ν` have weight `e`. At an idele `y` with finite part `1`, the Hecke character
`y ↦ ν(y / ȳ) υ(y) ^ (-k)` takes the value `∏ w, (y_w / |y_w|) ^ (2 e_w - k)`. 

### `spaceChar_apply_of_snd_eq_one`

 Let `ν` be a character of `U(1)(𝔸)` of weight `e` with tame part `ψ`, and let `υ` be the
splitting character in the Weil data on `E`, whose component at each infinite place `w` is
`z ↦ z / |z|` in the chosen embedding. At an idele `y` with finite part `1`, the rank-`r` space
character `ν.spaceChar r : y ↦ ν(y / ȳ) υ(y) ^ (-r)` takes the value
`∏ w, (y_w / |y_w|) ^ (2 e_w - r)`, where `y_w` is the complex component of `y` at the infinite
place `w`. In this sense it has the weight `e - r / 2`. 

### `L_ne_zero`

 Let `ν` have weight `e ≠ 0` and some tame part, and let `S` be finite. Then the `L`-function of
`x ↦ ν(x / x̄)` without the factors at `S ∪ S̄` does not vanish at any real `s ≥ 1` (at `s = 1`
its value is the limit from the right, see `New.eulerProd`). 

### `charUnramifiedAt`

 If the tame part `ψ` of `ν` is trivial at `w` and at `w̄`, the base change of `ν` is unramified
at `w`. 

### `atUniformizer_star`

 Let `ν` have weight `e` and tame part `ψ`, with `ψ w` and `ψ w̄` trivial. Then the Hecke
character `x ↦ ν (x / x̄)` takes mutually inverse values at the chosen uniformisers at `w̄` and at
`w`. 

### `L_inv`

 Let ν be a continuous circle-valued character of the norm-one adeles of the CM field E that is
trivial on E. Suppose ν has weight `e` and tame part `ψ`: almost all residue characters ψ_w are
trivial, and ν(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part. If
ψ_v = 1 for all v ∉ S, then `ν⁻¹` and `ν` have the same `L`-function without the factors at
`S ∪ S̄`. 

### `toAlgebraic`

 For a character ν of U(1)(𝔸) of weight e, the algebraic Hecke character ν(x/x̄) υ(x)^{−k}
|x|^{j−k/2}, of infinity type j + e − k on the CM type, j − e on its conjugate. 

### `charUnramifiedAt_toAlgebraic`

 The algebraic character made from `ν` is unramified at `w` if the tame part of `ν` is trivial at
`w` and at `w̄` (the section hypotheses `hψ_w`, `hψ_star`). 


## Base change of algebraic Hecke characters and twists of parallel type

An element ω of `New.AlgHeckeChar` E is a pair (θ, n). Here θ = ω.1.1 is a character of the finite
ideles with open kernel, n = ω.1.2.toAdd is its type, and θ(x) = ∏_σ σ(x)^(−n_σ) on E^×.
`New.GaloisRep.IsSphericalAbove` ρ R J w P says that above w, ρ is unramified or crystalline, its
jump multiplicities are related to J by R, and P kills every geometric Frobenius.


### `prod_norm_zpow`

 For the norm from `E` to `K₀`: `∏ s, s (N x) ^ n s = ∏ σ, σ x ^ n (σ|K₀)`, the products running
over the complex embeddings of `K₀` and of `E`. 

### `AlgHeckeChar.baseChange`

 Base change `ω ∘ N` to `E` of an algebraic Hecke character `ω` of `K₀`; its exponent at an
embedding `σ` of `E` is that of `ω` at `σ|K₀`. 

### `scalarRep`

 The one-dimensional representation of `Gal(Ω/E)` by the scalars `μ g`. 

### `decompRep_scalarRep_cyclotomicCharIn_pow_mul`

 In a chart `L : PadicPlaceEmbedding E A ℓ` at `A` above `ℓ` (`decompRep` restricts to the
decomposition group at `A`; `cyclotomicGp` is the cyclotomic character of its image `L.toGp g`),
twisting the scalar representation of `μ` by the `d`-th power of the cyclotomic character is its
Tate twist by `d`. 

### `decompRep_scalarRep_eq_cyclotomicCharIn_pow_mul`

 In a chart at `A` above `ℓ`, the scalar representation of `μ` is the Tate twist by `-d` of its
twist by the `d`-th power of the cyclotomic character. 

### `isGoodAt_scalarRep_cyclotomicCharIn_pow_mul`

 Twisting a character by the `d`-th power of the cyclotomic character keeps it unramified or
crystalline at `A`. 

### `hasJumpsAt_scalarRep_cyclotomicCharIn_pow_mul`

 Twisting a character by the `d`-th power of the cyclotomic character lowers its jumps at `A`
by `d`. 

### `polyKillsAt_scalarRep_cyclotomicCharIn_pow_mul`

 Let μ be a character of Gal(Ω/E) with values in the algebraic closure of ℚ_ℓ, let A be a place
of Ω, and let s be such that s⁻¹ stabilises A and acts as x ↦ x^q modulo its maximal ideal, with
q ≠ 0. If X − q^d c kills s at A for the one-dimensional representation μ, then X − c kills s at A
for χ_ℓ^d · μ, where χ_ℓ is the ℓ-adic cyclotomic character. "P kills s at A" (`PolyKillsAt`) means
P(r(s)) = 0 when ℓ is a unit at A, and otherwise the Weil-pair condition `New.Period.IsKilledBy`
along every local datum at A. 

### `map_heckePoly`

 Mapping the Hecke polynomial of `t` by a ring homomorphism `f` gives the Hecke polynomial of
`f ∘ t`. 

### `Variety.exists_twist_algHeckeChar`

 Let ω be an algebraic Hecke character of the CM field E of type n, and let ι = ιℓ be the fixed
isomorphism of ℂ with the algebraic closure of ℚ_ℓ. For continuous ρ there is a continuous ρ' (in
the proof, a twist of ρ) with the following property at every finite place w where ω is unramified
and n_σ = d for all σ with ισ inducing w. Put c = ω(ϖ_w), with ϖ_w the chosen uniformiser
`uniformizer w` at w. If `IsSphericalAbove` holds for ρ with jump data J and `heckePoly q a` of the
ι(t_j c^(−j)), it holds for ρ' with jump data J(τ) − n_τ and `heckePoly q a` of the ι(t_j). Here
`IsSphericalAbove ρ R J w P` means that at each place of Ω over w, ρ is good, its jump
multiplicities are R-related to J, and P kills geometric Frobenius. Also `heckePoly q a t = Σ_{j≤a}
(−1)^j q^{j(j−1)/2} t_j X^{a−j}`. 
