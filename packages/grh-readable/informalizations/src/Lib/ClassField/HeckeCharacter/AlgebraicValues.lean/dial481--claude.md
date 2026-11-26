---
{
  "module": "src/Lib/ClassField/HeckeCharacter/AlgebraicValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/AlgebraicValues.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/AlgebraicValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Values of algebraic Hecke characters

An algebraic Hecke character of a number field `K` is a character of the finite ideles with open
kernel that is `∏ τ, τ x ^ (-n τ)` on `Kˣ`, for integers `n τ` indexed by the complex embeddings of
`K`. Over a CM field, a unitary Hecke character of suitable type becomes algebraic after a twist by
a half-integral power of the absolute value. This is applied to the base change `y ↦ μ (y / ȳ)` of a
character `μ` of `U(1)(𝔸)` with a weight, and to `υ |·| ^ (-1 / 2)`, with `υ` the splitting
character of the Weil data.

## Main definitions and results

* `New.AlgHeckeChar.exists_pow_eq_prod`, `New.AlgHeckeChar.norm_map_eq_sqrt_finIdeleAbs_zpow`,
  `New.AlgHeckeChar.norm_padic_eq_prod`, `New.AlgHeckeChar.conjugateBy`: powers, complex and
  `p`-adic absolute values and conjugates of the values of an algebraic Hecke character.
* `New.IsHeckeOfType.toAlgebraic`: the algebraic character `ψ |·|^{k/2}` of infinity type `m`, for
  `ψ` of type `m (Φ w) - m (Φ̄ w)` with `m (Φ w) + m (Φ̄ w) = k` at every infinite place `w`.
* `New.AutChar.HasWeight.isHeckeOfType`: if `ν` has weight `e`, its base change has type `2 • e`.
* `New.AutChar.HasWeight.baseChangeAlgebraic`: this base change as an algebraic Hecke character.
* `New.AutChar.HasWeight.norm_map_eq_one`, `New.AutChar.HasWeight.norm_padic_eq_prod`: at a point
  `u` of `U(1)(𝔸)` with archimedean part `1`, the conjugates of the value `μ u` of a character of
  weight `e` have modulus `1`, and its absolute value under `ι : ℂ →+* ℂ_[p]` is
  `∏ τ, ‖u_τ‖ ^ (-e τ)`, with `u_τ` the component of `u` at the prime induced by `ι ∘ Φ τ`.
* `New.WeilData.chiFinAlgebraic`: the character `υ |·|^{-1/2}` as an algebraic Hecke character.

Notions from other files:
* `New.IsHeckeOfType`: The character ψ of the finite ideles is the finite part of a Hecke character
  of type n: its kernel is open and ψ(x) ∏_w (Φ_w(x)/|Φ_w(x)|)^{n_w} = 1 on K^×.
* `New.AutChar.HasWeight`: μ has weight e and tame part ψ: almost all residue characters ψ_w are
  trivial, and μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part.
* `New.adeleExtension` σ: the extension of an embedding σ of E into `ℂ_[p]` to the finite adeles,
  through the prime that σ induces.

## Relation to the literature

Known result: the values of characters of type A₀. Source: A. Weil, On a certain type of characters
of the idèle-class group of an algebraic number-field (1956).



## Values of algebraic Hecke characters

An element `θ` of `New.AlgHeckeChar K` is a pair of a character `θ.val.fst` of the finite ideles
with open kernel and exponents `n τ = θ.val.snd.toAdd τ`, one for each complex embedding `τ` of `K`,
such that the character is `∏ τ, τ x ^ (-n τ)` on `Kˣ`.


### `exists_pow_eq_prod`

 Let `θ` be an algebraic Hecke character with exponents `n τ` and `y` a finite idele. There are
`N > 0` and `γ` in `Kˣ` such that `y ^ N / γ` is a unit at all finite places and
`θ(y) ^ N = ∏ τ, τ γ ^ (-n τ)`. This is the key step in Weil's proof that characters of type A₀
take algebraic values on finite ideles. 

### `prod_norm_map_embeddings_eq_inv_finIdeleAbs_pow`

 Let `γ` in `Kˣ` and the finite idele `y` be such that `y ^ N / γ` is a unit at all finite
places. Then the moduli of the conjugates `σ (τ γ)` have product `|y| ^ (-N)`, where `|y|` is the
norm of `y` and `τ` runs over the embeddings of `K`. This is the product formula for `γ`. 

### `norm_map_eq_sqrt_finIdeleAbs_zpow`

 Let `K` be a CM field and `θ` an algebraic Hecke character whose exponents satisfy
`n τ + n τ̄ = j` for all `τ`. Then every conjugate `σ (θ y)` of a value has modulus `|y| ^ (j / 2)`,
where `|y|` is the norm of the finite idele `y`. 

### `norm_padic_eq_prod`

 Let `θ` be an algebraic Hecke character with exponents `n τ`, and let `ι : ℂ →+* ℂ_[p]`. Then
`‖ι (θ y)‖ = ∏ τ, ‖y_τ‖ ^ (-n τ)`, where `y_τ` is the image in `ℂ_[p]` of the component of the
finite idele `y` at the prime induced by `ι ∘ τ`. 

### `norm_padic_eq_one`

 If the finite idele `y` is a unit at all primes above `p`, then the value `θ y` of an algebraic
Hecke character is a unit at `ι : ℂ →+* ℂ_[p]`. 

### `conjugateBy`

 The conjugate `σ ∘ θ` of an algebraic Hecke character `θ` by an automorphism `σ` of `ℂ`. It is
algebraic, and its exponent at `σ ∘ τ` is that of `θ` at `τ`. 

### `conjugateBy_apply`

 For an algebraic Hecke character `θ` of the number field `K`, an automorphism `σ` of `ℂ` and a
finite idele `y`, the finite-idele character of the conjugate `θ.conjugateBy σ` (that is, `σ ∘ θ`)
takes at `y` the value `σ` applied to the value of `θ` at `y`. 

### `conjugateBy_exponent`

 The conjugate of the character `θ` by `σ` has at `σ ∘ τ` the exponent of `θ` at `τ`. 

 ## Algebraic characters from unitary Hecke characters of a CM field 

### `IsHeckeOfType.toAlgebraic`

 Let `Φ w` be the embedding of the CM type at an infinite place `w`. Suppose that
`m (Φ w) + m (Φ̄ w) = k` for every `w` and that the character `ψ` of the finite ideles is the finite
part of a Hecke character of type `m (Φ w) - m (Φ̄ w)`. This is the algebraic Hecke character
`ψ |·| ^ (k / 2)` of infinity type `m`. 

### `IsHeckeOfType.toAlgebraic_locIdele`

 At the idele `locIdele w x` (equal to `x` at `w` and `1` elsewhere), the value of
`ψ |·| ^ (k / 2)` is `ψ x` times the power `k` of the square root of `|x|_w`. The logarithm of the
valuation of `x` is minus its order, so `|x|_w = q_w ^ log (v x)`, where `q_w = w.q` is the size of
the residue field at `w`. 

### `HeckeChar.isHeckeOfType_finPart`

 If the unitary Hecke character `χ` is `z ↦ ∏ w, (z w / ‖z w‖) ^ n w` at infinity, its finite
part has type `n`: it has open kernel and is inverse to `∏ w, (Φ w x / ‖Φ w x‖) ^ n w` on `Eˣ`. Here
`E` is a CM field and `Φ w` is the complex embedding that the CM type chooses to induce the infinite
place `w`. 

 ## Characters of U(1) with a weight 

### `baseChange_apply_inf`

 At infinity the base change `x ↦ ν (x / x̄)` of a character `ν` of weight `e` is
`z ↦ ∏ w, (z w / ‖z w‖) ^ (2 * e w)`. 

### `isHeckeOfType`

 If the character `ν` of `U(1)(𝔸)` has weight `e` and tame part `ψ`, then the restriction of
`x ↦ ν (x / x̄)` to the finite ideles of `E` is the finite part of a Hecke character of type
`2 e`. 

### `baseChangeAlgebraic`

 The base change `y ↦ μ (y / ȳ)` of a character `μ` of `U(1)(𝔸)` of weight `e`, on finite
ideles, as an algebraic Hecke character: its exponents are `e` on the CM type and `-e` on its
conjugate. 

### `baseChangeAlgebraic_exponent`

 For a character `μ` of weight `e`, the algebraic Hecke character `h.baseChangeAlgebraic`, which
is the base change of `μ` on finite ideles, has the exponent `e w` at the embedding `Φ w` of the CM
type and `-e w` at its conjugate. 

### `exists_baseChangeAlgebraic_apply_eq`

 Let `μ` have weight `e` and tame part `ψ`. If `u` in `U(1)(𝔸)` has archimedean part `1`, then
its finite part is `y / ȳ` for a finite idele `y`, and `μ u` is the value at `y` of the base change
of `μ`. 

### `norm_map_eq_one`

 Let `μ` have weight `e` and tame part `ψ`. If `u` in `U(1)(𝔸)` has archimedean part `1`, then
`|σ (μ u)| = 1` for every ring homomorphism `σ : ℂ → ℂ`. 

### `norm_padic_eq_prod`

 Let `μ` have weight `e` and tame part `ψ`, let `ι : ℂ →+* ℂ_[p]`, and let `u` in `U(1)(𝔸)` have
archimedean part `1`. Then `‖ι (μ u)‖ = ∏ τ, ‖u_τ‖ ^ (-e τ)` over the infinite places `τ`, where
`u_τ` is the image in `ℂ_[p]` of the finite part of `u` at the prime induced by `ι ∘ Φ τ`, with `Φ`
the CM type. 

 ## The character `υ |·| ^ (-1 / 2)` on finite ideles 

### `chiFinAlgebraic`

 The character `υ |·| ^ (-1 / 2)` of the finite ideles, with `υ` the splitting character, as an
algebraic Hecke character: its exponents are `0` on the CM type and `-1` on its conjugate. 

### `chiFinAlgebraic_apply`

 Let `E` be a CM field with a chosen CM type and Weil data, and let `υ` be the splitting
character. For every finite idele `x`, the finite-idele character underlying the algebraic Hecke
character `chiFinAlgebraic`, evaluated at `x` and read in `ℂ`, equals
`chiFin x = υ(x)|x|^(-1/2)`. 

### `chiFinAlgebraic_exponent`

 The algebraic Hecke character `υ |·| ^ (-1 / 2)` has the exponent `0` at the embedding `Φ w` of
the CM type and `-1` at its conjugate. 

### `exists_chiFin_pow_eq_prod`

 For Weil data on `E` and a finite idele `x`, there are `n > 0` and `y` in `Eˣ` such that `x ^ n`
and `y` have the same valuation at every finite place and
`(υ(x) |x| ^ (-1 / 2)) ^ n = ∏ v, Φ v ȳ`, over the embeddings `Φ v` of the CM type. 

### `norm_map_chiFin`

 For an embedding `ι` of `ℂ` into `ℂ_[p]`, the `p`-adic absolute value of
`υ(x) |x| ^ (-1 / 2)` is the product over the infinite places `v` of the absolute values of `x`
under the extension to the finite adeles of `y ↦ ι (Φ v ȳ)`, the embedding `weightEmbedding ι v`. 
