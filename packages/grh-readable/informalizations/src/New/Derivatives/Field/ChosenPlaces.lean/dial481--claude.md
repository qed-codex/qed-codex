---
{
  "module": "src/New/Derivatives/Field/ChosenPlaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chosen places, characters of given weight, finiteness of pairs and sizes of the different

Fix admissible data `D` (`New.Data`) with primes p₀, p₁ (p_i is `D.levelPrime i`) and an integer
`D.piMBar` of K of norm p₀p₁. The chosen places are the finite places of E that divide the complex
conjugate of `D.piMBar`.

The file defines residue characters at the chosen places, characters of U(1)(𝔸) of given weight and
pairs, and proves that there are finitely many pairs. It also bounds the generator of the different
of E and the root discriminant at the infinite places between `x ^ 10` and `x ^ 12`, where `log x`
is `D.logX`.

## Main definitions and results

* `New.Data.IsChosen`, `New.Data.ChosenPlace`: the chosen places, and those above p_i. Each lies
  above p₀ or p₁ (`New.Data.exists_levelPrime_mem_of_isChosen`). A place above p_i has norm p_i
  (`New.Data.q_eq_levelPrime`).
* `New.Data.chiMLocal`: residue characters of order q₂ at the chosen places, trivial elsewhere. At a
  chosen place it is the q₂-th power of a character `New.Data.chiMLocalRoot` of order q₂².
* `New.Data.chiZero`, `New.Data.chiM`: characters of U(1)(𝔸) of weight -w₀ and trivial tame part,
  and of weight 0 and tame part `New.Data.chiMLocal`. By
  `New.AutChar.exists_hasWeight_of_prod_eq_one` they exist because the formula of
  `New.AutChar.HasWeight` gives 1 on the integral rational points of U(1), which are q₁-th roots of
  unity (`New.Data.exists_char_hasWeight`).
* `New.Data.CriticalPair`: a character of weight -c with tame part trivial off the chosen places,
  and an integer z with 1 ≤ z ≤ t and z ≤ c ≤ 4b. There are finitely many
  (`New.Data.finite_criticalPair`).
* `New.Data.hasLogBound_deltaE`: at every infinite place the generator `New.Parameters.deltaE` of
  the different has absolute value in `[x ^ 10, x ^ 12]`.
* `New.Data.rootDisc_mem_Icc`, `New.Data.hasLogBound_rootDisc`: so does the root discriminant
  `New.Data.rootDisc`, their geometric mean. The class `D.HasLogBound u F l` says `|F| ≤ exp l` for
  `u = true` and `exp l ≤ F` for `u = false`; so `(if u then 12 else 10) * log x` gives both bounds
  at once.

Notions from other files:
* `New.Data.E`: The field E = K(ζ), ζ a primitive root of unity of order q₁, a multiple of q₀ that
  depends on the exponent s = `D.towerExp` of the data; `New.Data.Φ` is the type of its infinite
  places.
* `New.AutChar`: The group of continuous circle-valued characters of U(1)(𝔸), the norm-one adeles of
  the CM field E, trivial on elements coming from E.
* `New.AutChar.HasWeight`: μ has weight e and tame part ψ: almost all residue characters ψ_w are
  trivial, and μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part.
* `New.Parameters.q₂`: The natural number q₂ = (q₀d)^(s+6); q₂² divides p_i - 1.
* `New.Data.liftWeight`: The number w_j(σ) = κ(σ) + (j + 1/2) Δ, with κ = `New.Data.weight`, the gap
  Δ = `New.Data.gap` and Δ/2 = `New.Data.halfGap`.


 ## Chosen places and characters of given weight 

### `piM`

 The complex conjugate of the integer `D.piMBar` of K, of norm p₀p₁, as an integer of E; the
chosen places are its prime divisors. 

### `IsChosen`

 The finite place w of E is chosen: it divides the complex conjugate of the integer `D.piMBar` of
K, of norm p₀p₁. 

 ### The chosen places 

### `ChosenPlace`

 The chosen places above the prime p_i = `D.levelPrime i`: the finite places w of E that are
chosen, that is, divide the complex conjugate of `D.piMBar` (`New.Data.IsChosen`, written out), and
divide p_i. 

### `piM_mul_star`

 The product of `D.piM` and its complex conjugate is `D.M = p₀ p₁` in 𝓞_E. 

### `exists_piM_mul_star_eq_levelPrime_mul_coprime`

 The data `D` carry two distinct primes p₀, p₁ and an integer `D.piMBar` of K of norm p₀p₁;
`D.piM` is the complex conjugate (`star`) of its image in 𝓞_E. For i = 0 and i = 1, the product of
`D.piM` and its conjugate is p_i = `D.levelPrime i` times a natural number prime to p_i. 

### `exists_levelPrime_mem_of_isChosen`

 If a finite place w of E is chosen, that is, its prime ideal contains `D.piM` (an integer of E
whose product with its complex conjugate is p₀p₁), then w lies above one of the two primes
p₀ = `D.levelPrime 0`, p₁ = `D.levelPrime 1` of the data `D`. 

### `isChosen_iff`

 A finite place w of E whose prime ideal contains `D.piM` (`D.IsChosen w`) lies above p₀ or p₁.
So the set of such places is the union over i = 0, 1 of the places that contain both `D.piM` and p_i
(`D.ChosenPlace i`). 

### `q_eq_levelPrime`

 If a finite place w of E lies above the prime p_i = `D.levelPrime i` of the data, then its
absolute norm `w.q`, the number of elements of the residue field, equals p_i; that is, w has residue
degree one. 

 ### The residue characters ω 

### `exists_mulChar_orderOf_eq_sq_of_isChosen`

 Let w be a chosen place of E: its prime ideal contains `D.piM`, the complex conjugate of the
integer `D.piMBar` of K of norm p₀p₁. Then the residue field at w has a complex multiplicative
character `T` of order q₂², where q₂ = `P.q₂ D.towerExp` is (q₀d)^(s+6) for s = `D.towerExp`. 

### `chiMLocalRoot`

 A fixed complex multiplicative character of order q₂² of the residue field at a chosen place. 

### `chiMLocal`

 The residue characters ω_w: at a chosen place the q₂-th power of the character
`New.Data.chiMLocalRoot` of order q₂², and trivial elsewhere. 

### `chiMLocal_of_isChosen`

 At a chosen place, ω_w = `D.chiMLocal w` is the q₂-th power of the fixed character of order
q₂². 

### `chiMLocal_apply_eq_one_of_pow_q₁_eq_one`

 Let w be a finite place of E and ω_w = `D.chiMLocal w` the character of its residue field that
is the q₂-th power of a fixed character of order q₂² if w divides `D.piM`, and trivial otherwise.
Then ω_w(x) = 1 for every x in the residue field with x^q₁ = 1. 

### `chiMLocal_zpow_mul_pow_eq_one`

 Let `ψ` give, for each finite place w of E, a complex multiplicative character of the residue
field at w. If `ψ w = 1`, then for every integer n the w-component of ωⁿψ, where ω = `D.chiMLocal`,
raised to the power q₂ = `P.q₂ D.towerExp`, is trivial. 

 ### The characters `chiZero` and `chiM`, and pairs 

### `exists_zeta_pow_eq_of_isIntegral`

 Let γ be an element of `unitary D.E`, that is, γγ̄ = 1 in E, and suppose γ is integral over ℤ.
Then γ is a power of ζ = `P.ζ D.towerExp`, the primitive root of unity of order q₁. 

### `prod_phi_zeta_pow_pow_liftWeight_zero_eq_one`

 For every k, the product ∏_v γ_v^{w₀(v)} over the infinite places v of E is 1 at γ = ζ^k. Here
γ_v = `New.Φ v γ` is the image of γ under the complex embedding chosen at v, and
ζ = `P.ζ D.towerExp` is the primitive root of unity of order q₁ = `D.q₁` in E. The exponent
w₀(v) = `D.liftWeight 0 v` is the natural number κ(v) + r⁸, where κ(v) = `D.weight v` is a multiple
of q₁ given with the data and r⁸ = `D.halfGap` does not depend on v. 

### `exists_char_hasWeight`

 For all natural numbers a and n there is a character μ of U(1)(𝔸), the norm-one adeles of E,
trivial on the elements coming from E, of weight v ↦ -a·w₀(v) and tame part (ω_w^n)_w: for u with
integral finite part, μ(u) = ∏_v u_v^{-a·w₀(v)} · ∏_w ω_w(u mod w)^n, over the infinite places v and
the finite places w. Here w₀(v) = `D.liftWeight 0 v` is the natural number `D.weight v + D.r ^ 8`,
and ω_w = `D.chiMLocal w` is a character of the residue field at w, of order q₂ if w divides `D.piM`
and trivial otherwise. 

### `chiZero`

 A fixed character of U(1)(𝔸), trivial on rational points, of weight −w₀ (`New.Data.liftWeight`
at j = 0) and trivial tame part. 

### `chiM`

 A fixed character of U(1)(𝔸), trivial on rational points, of weight 0 and tame part ω
(`New.Data.chiMLocal`). 

### `CriticalPair`

 A pair: an integer 1 ≤ z ≤ t and a character ν of U(1)(𝔸) of weight −c, with z ≤ c(v) ≤ 4b at
every infinite place v and tame part supported on the chosen places. Here t = `D.t` is the natural
number 5r, r the rank of the target, and b = `D.b` is the real scale b of the data, the weight at
the b-places. 

### `CriticalPair.character`

 The character ν of `U(1)(𝔸)`, trivial on rational points. 

### `CriticalPair.negWeight`

 The function c: minus the weight of ν at each infinite place. 

### `CriticalPair.tamePart`

 The tame part ψ of ν: a character of the residue field at each finite place. 

### `CriticalPair.z`

 The integer of the pair, a lower bound for c. 

### `CriticalPair.hasWeight`

 ν has weight -c and tame part ψ. 

### `CriticalPair.tamePart_eq_one`

 The tame part is trivial off the chosen places. 

### `CriticalPair.z_mem`

 `1 ≤ z ≤ t`. 

### `CriticalPair.le_negWeight`

 c is at least `z` at every infinite place. 

### `CriticalPair.negWeight_le`

 c is at most `4 b` at every infinite place. 


## Finiteness of pairs

The type `New.Data.CriticalPair` is finite. The input is the finiteness of the set of characters of
a given weight and tame part (`New.AutChar.finite_setOf_hasWeight`).


### `New.Data.finite_criticalPair`

 There are finitely many pairs for the data `D`: an integer `z ∈ [1, t]` with a character of
`U(1)(𝔸)` of weight `-c`, `z ≤ c v ≤ 4 b`, whose tame part is trivial off the chosen places. 

 ## Bounds for the different and the root discriminant at infinity 

### `exists_abs_log_le_and_apply_deltaE_eq`

 At every infinite place `v` of `E = P.E s`, the generator `δ = P.deltaE s` of the different has
`|δ|_v = A * towerDeg s * √d` for some `A > 0` with `|log A| ≤ P.constantBound`. Here `d = P.d` is
the prime with `K = ℚ(√-d)`, `towerDeg s = q₁ / q₀` is the quotient of the orders of the roots of
unity `ζ` and `ζ ^ towerDeg s`, `q₀ = P.q₀` the fixed modulus, and `P.constantBound` is a sum of
constants that depend only on `q₀` and `d`. 

### `abs_log_deltaE_sub_log_rootDiscr_le`

 At every infinite place `v` of `E = P.E s`, the absolute value of the generator `P.deltaE s` of
the different has the order of magnitude of the root discriminant `rootDiscr (P.E s)` (this is
`D.rootDisc` for data `D` of exponent `s`): their logarithms differ by at most
`2 * P.constantBound`. 

### `hasLogBound_deltaE`

 At every infinite place `v : D.Φ` of the field `E` of exponent `s = D.towerExp`, the generator
`δ = P.deltaE s` of the different has `|δ|_v` in `[x ^ 10, x ^ 12]`, where `x = exp D.logX` is the
smallest of the three scales `x`, `x₁`, `b` of the data: the upper bound for `u = true`, the lower
bound for `u = false`. 

### `rootDisc_mem_Icc`

 The root discriminant `rd_E = D.rootDisc` of the field `E = D.E` lies in `[x ^ 10, x ^ 12]`. 

### `hasLogBound_rootDisc`

 The root discriminant of `E` has the upper exponent `12 log x` (`u = true`) and the lower
exponent `10 log x` (`u = false`), where `log x = D.logX`. 
