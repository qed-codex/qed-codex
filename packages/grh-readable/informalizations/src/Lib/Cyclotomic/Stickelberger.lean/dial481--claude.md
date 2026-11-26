---
{
  "module": "src/Lib/Cyclotomic/Stickelberger.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Stickelberger.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Stickelberger.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A weak form of Stickelberger's theorem for Gauss sums, and a family of Jacobi-type quotients

Gauss sums over `𝔽_p` give a family of elements `J x` of `Ωˣ`, `Ω = ℚ̄`, indexed by torsion points
`x` of `ℚ/ℤ`, with a known Galois action and a distribution relation up to elements of finite order.

* `New.OddPart.floorDiff`, `New.OddPart.sum_floorDiff`: the integer `⌊c ⟨x⟩⌋ - ⌊c ⟨-x⟩⌋` and its
  distribution relation (Hermite's identity).
* `New.OddPart.exists_galUnitsRep_gaussSum_eq`, `New.OddPart.stickelberger`: Galois action on Gauss
  sums, and their orders at a place `B` above `p`.
* `New.OddPart.exists_isJacobiFamily`: the family `J`, built from the quotients
  `j t = g(χ) ^ c / g(χ ^ c)` as `j t / j (-t)`.

Notions from other files:
* `Ω` is `ℚ̄`, and `DiscreteUnits Ω` is `Ωˣ` written additively: a sum is a product, `c • u` is
  `u ^ c`. `galUnitsRep σ` is the action of `σ ∈ Gal(Ω/ℚ)` on it.
* `ClosurePlace`: a valuation subring `B` of `Ω`; it lies above `p` when `B.valuation p < 1`, and
  `centrePrime Ω B` is the prime ideal of `𝓞 Ω` that it defines; `principalUnits B` is the subgroup
  of `DiscreteUnits Ω` of the `u` with `B.valuation (u - 1) < 1`, that is `u ≡ 1` at `B`.
* `ordRat ℚ B u`: the order of `u` at `B`, normalised so that a prime `p` below `B` has order one.
* `cyclotomicCharMod Ω N σ`: the cyclotomic character of `σ` modulo `N`, the unit `a` with
  `σ ζ = ζ ^ a` for every `N`-th root of unity `ζ`.
* `New.QZ`: the group `ℚ/ℤ`; `New.QZ.fracRep x = ⟨x⟩` is the representative in `[0, 1)`, and
  `New.QZ.ofZMod r b = b / r`.

## Relation to the literature

Known result: Stickelberger's factorisation of Gauss sums and the Davenport–Hasse product relation.
Here only prime fields are treated, and characters are named by the valuation of their Gauss sum.
The product relation is proved for Jacobi-type quotients of Gauss sums and only up to a root of
unity. Source: L. Washington, Introduction to Cyclotomic Fields, 2nd ed. 1997, 6.2 and Thm 15.1; for
the product relation, H. Davenport, H. Hasse, J. reine angew. Math. 172 (1935).


### `floorDiff`

 For `c : ℕ`, the integer `⌊c ⟨x⟩⌋ - ⌊c ⟨-x⟩⌋`, where `⟨x⟩` is the representative of `x ∈ ℚ/ℤ`
in `[0, 1)`. 

### `sum_floorDiff`

 The distribution relation for `floorDiff m`, with `m` prime to `r`: its sum over the translates
of `x` by the points `v b / r`, for a unit `v` mod `r`, is its value at `r • x`. 

### `isOfFinOrder_of_norm_eq_one`

 Kronecker's theorem in `Ω = ℚ̄`: an element of `Ω` that lies in every valuation ring of `Ω` and
has absolute value one in every complex embedding is a root of unity. 

 ### Gauss sums 

### `exists_galUnitsRep_gaussSum_eq`

 Galois action on Gauss sums. Let `ψ` be an additive character of `𝔽_p`, let `t ↦ χ t` be a
homomorphism from `ZMod r` to the multiplicative characters of `𝔽_p`, and let the unit `g t` of
`Ω` be the Gauss sum of `χ t` and `ψ`. There are homomorphisms `K σ : ZMod r → Ωˣ` with
`σ (g t) = K σ (a t) * g (a t)`, where `a` is the cyclotomic character of `σ` modulo `r`; in the
additive notation of `DiscreteUnits Ω` the right side is `(K σ + g) (a * t)`. 

### `mk_centrePrime_eq_one_of_pow_eq_one`

 Let `B` be a place of `Ω` above the prime `p`. An algebraic integer `x` with `x ^ p = 1` is
congruent to `1` modulo the prime ideal `centrePrime Ω B` of `𝓞 Ω` that `B` defines. 

### `stickelberger`

 A weak form of Stickelberger's theorem for `𝔽_p`. Let `B` be a place of `Ω` above `p`, `ψ` a
primitive additive character of `ZMod p`, `r` prime to `p`, `t ↦ χ t` a primitive (so injective)
additive map from `ZMod r` to the multiplicative characters of `ZMod p`, and `g t` the Gauss sum of
`χ t` and `ψ`. Then some injective `S : ZMod r →+ ℚ/ℤ` has, for every `t`, representative
`(S t).fracRep` in `[0, 1)` equal to `ordRat ℚ B (g t)`, the order at `B` normalised so that `p` has
order `1`. Stickelberger's factorisation of Gauss sums computes these orders; here they are only
tied to `S`. 

### `isOfFinAddOrder_distribution`

 The distribution relation up to roots of unity. Let `Ω` be the algebraic closure of `ℚ`, let `B`
be a place of `Ω` above `p`, and let `J : ℚ/ℤ → Ωˣ` (written additively) satisfy the following on
the `M`-torsion: it is Galois equivariant (`σ (J x) = J (a • x)` when `σ` raises `M`-th roots of
unity to the power `a`), a unit at every place not above `p`, of order
`floorDiff c x = ⌊c⟨x⟩⌋ − ⌊c⟨−x⟩⌋` at `B` normalised on `ℚ` (where `⟨x⟩` is the representative of
`x` in `[0, 1)`), and of absolute value one in every complex embedding. Then for `M • x = 0`,
`r ∣ M` and `c` prime to `r`, the quotient `(∏ b mod r, J (x + b / r)) / J (r x)` is a root of
unity. 

### `IsJacobiFamily`

 The properties of a family `J : ℚ/ℤ → Ωˣ` (written additively) of Jacobi-type quotients of
Gauss sums over `𝔽_p`, on the points `x` with `M • x = 0`. Here `B` is a place of `Ω` (above `p`
where the family is built), and `c` is the exponent in `g(χ) ^ c / g(χ ^ c)`. 

### `IsJacobiFamily.isOfFinAddOrder_sum_sub`

 The distribution relation up to a root of unity: for `r ∣ M` prime to `c`, the quotient
  `(∏ b mod r, J (x + b / r)) / J (r • x)` has finite order. 

### `IsJacobiFamily.galUnitsRep_apply`

 The Galois action: `σ (J x) = J (a • x)` if `σ` raises the `M`-th roots of unity to the
  power `a`. 

### `IsJacobiFamily.valuation_eq_one`

 `J x` is a unit at every place not above `p`. 

### `IsJacobiFamily.ordRat_eq`

 The order of `J x` at `B` is `floorDiff c x`. 

### `IsJacobiFamily.norm_eq_one`

 `J x` has absolute value one in every complex embedding. 

### `IsJacobiFamily.sub_mem_principalUnits`

 For a prime `q ∣ p - 1` and `q • b = 0`, the quotient `J (x + b) / J x` is `≡ 1` at every
  place above `q`. 

### `gaussSum_dvd_natCast_of_isPrimitive`

 A Gauss sum over `𝔽_p` of a multiplicative character `χ₀` and a primitive additive character
`ψ` divides `p` in `𝓞 Ω`. 

### `valuation_gaussSum_eq_one_of_valuation_eq_one`

 Let `A` be a place of `Ω` not above `p`. A Gauss sum over `𝔽_p` of a multiplicative character
`χ₀` and a primitive additive character `ψ` has valuation one at `A`: it is integral and divides
`p`, which is a unit at `A`. 

### `exists_apply_eq_and_nsmul_eq_zero_of_injective`

 An injective homomorphism `S : ℤ/r → ℚ/ℤ` maps the `m`-torsion onto the `m`-torsion, for
`m ∣ r`. 

### `exists_addChar_isPrimitive_and_mulChar_isPrimitive`

 For a prime `p`, there are a primitive additive character `ψ` of `𝔽_p` and a primitive (so
injective) homomorphism `χ` from `ZMod (p - 1)` to the multiplicative characters of `𝔽_p`, both with
values in `𝓞 Ω`. 

### `gaussSum_add_sub_gaussSum_mem_centrePrime_of_nsmul_eq_zero`

 Let `A` be a place of `Ω` above a prime `q`, let `ψ` be an additive character of `𝔽_p` and
`t ↦ χ t` a homomorphism from `ZMod n` to the multiplicative characters of `𝔽_p`. If `q • u = 0`,
the Gauss sums of `χ (w + u)` and of `χ w` with `ψ` are congruent modulo the prime ideal
`centrePrime Ω A`: the values of `χ u` on units are `q`-th roots of unity, so `≡ 1` at `A`. 

### `exists_isJacobiFamily`

 Let `B` be a place of `Ω` above the prime `p` and let `c : ℕ`. There is a family `J : ℚ/ℤ → Ωˣ`
(written additively) such that, for every `M` with `p ≡ 1` mod `M`, its values at the points `x`
with `M • x = 0` have the properties `New.OddPart.IsJacobiFamily`. It is built from the Jacobi-type
quotients `j t = g(χ) ^ c / g(χ ^ c)` of Gauss sums over `𝔽_p` (`χ` the character of index `t`): at
the point `x` of index `t` it is `j t / j (-t)`.

Such quotients of Gauss sums are used to prove Stickelberger's theorem on annihilators of class
groups of cyclotomic fields; no class group appears in the statement. 
