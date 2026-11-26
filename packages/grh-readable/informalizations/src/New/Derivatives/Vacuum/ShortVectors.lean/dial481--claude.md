---
{
  "module": "src/New/Derivatives/Vacuum/ShortVectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tight frames in `𝔞₀`

A tight frame of length `h` is a finite family of vectors `y` of the lattice `𝔞₀`, counted with
multiplicities, such that `∑ y, (y† z) y = h z` for all `z`: a resolution of `h`.

* `New.Parameters.exists_isTightFrame_coprime`: a tight frame in `𝔞₀` of a length `h` prime to `q₁`,
  namely `New.Parameters.dualResolutionFactor`.
* `New.Parameters.exists_isTightFrame_of_coprime`: this frame and the powers of `ζ` give tight
  frames of every length `m ≥ q₁ h + R (q₁ + h)` with multiplicities at least `R`.
* `New.Data.exists_short_isTightFrame_coprime`: the length `h` is at most the weight `b`, and the
  two frames contain a vector `y` with `HasUnitLinearForm`.
* `New.Data.exists_isTightFrame`: a tight frame of length `p₀ p₁ = D.M` with large multiplicities,
  where `p₀` and `p₁` are the two primes `D.levelPrime 0` and `D.levelPrime 1` of the data.

The powers of `ζ` are a tight frame of length `q₁`. The frame of length `h` comes from the powers of
`ζ⁻¹` and the orbits `ζ ^ k * τ(e i)` of a multiple `e i` in `𝔞₀` of their dual basis for the
Hermitian form `y'† y`, by replacing some pairs of members by their sums; the cross terms add
`β ^ j + conj β ^ j` to the length, which makes it prime to `q₁`.

Notions from other files:
* `P.E s` is the field `E = K(ζ)`, where `K = ℚ(√-d)` and `ζ = P.ζ s` is a primitive root of unity
  of order `q₁ = P.q₁ s = P.q₀ * towerDeg s`; here `q₀ = P.q₀` is the fixed modulus of the
  parameters and `towerDeg s = 3 ^ (log₃ s + 5) * 2 ^ s`. `P.zetaInt s` is `ζ` as an element of
  `𝓞 E`. For admissible data `D` the exponent `s` is `D.towerExp`, so that `D.E = P.E D.towerExp`.
* `P.Φ s` is the set of infinite places of `E`, a group isomorphic to `Gal(E/K)` by
  `P.galOfPlace s`; `Φ τ` is the complex embedding of `E` chosen at the infinite place `τ`.
* `finiteImage id y ∈ Ô E` says that `y` lies in the lattice `𝔞₀ = E ∩ α Ô`, where `α` is the idele
  of the Weil data and `Ô` is the ring of integral finite adeles.
* `P.periodFactor s` is a complex number; by `norm_iota_periodFactor` its absolute value at an
  embedding `ιₚ : ℂ →+* ℂ_[p]` is given by the idele `α`.
* `β = (1 + √-d) / 2` is `quadGen d` in `ℂ`, `QuadField.betaK d` in `𝓞 K` and `P.betaKInE s` in
  `𝓞 E`.

In comments `P'(ζ)` is `P.relDifferentGen s`, the value at `ζ` of the derivative of the cyclotomic
polynomial of order `q₁`; `φ(q₁)` is the totient of `q₁`, `j` is the least integer with
`2 ^ j ≥ q₁`, and `y'† y = ∑ τ, τ(y) conj τ(y')`.


### `finiteImage_add_mem`

 The lattice of the `x` with `finiteImage id x = α⁻¹ x` integral at every finite place, that is
`E ∩ α Ô`, is closed under addition. 

### `finiteImage_mul_mem`

 The lattice of the `y` with `finiteImage id y = α⁻¹ y` integral at every finite place, that is
`E ∩ α Ô`, is closed under multiplication by integers of `E`. 

### `sum_mul_conj_eq_ofReal_iff`

 A finite sum of products `z i * conj (z i)` equals the real number `r` if and only if `r` is the
sum of the squared norms. 

### `IsTightFrame.sumElim`

 The disjoint union of a tight frame `w` with multiplicities `m` and frame bound `M` and a tight
frame `w'` with multiplicities `m'` and frame bound `M'` is a tight frame with frame bound `M + M'`.
This disjoint union is the family `Sum.elim w w'` with multiplicities `Sum.elim m m'`. 

### `IsTightFrame.join_family`

 The disjoint union of finitely many tight frames `v i` of lengths `L i`, all with multiplicities
`1`, is a tight frame of length `∑ i, L i`. 

### `IsTightFrame.replace_pairs`

 Let `w` be a tight frame of length `M` with multiplicities `1`, meaning each member is taken
once. Let `pair` select disjoint pairs of members, indexed by `J`. Suppose the cross terms of all
pairs add up to `t` times the identity matrix for an integer `t`. Then `M + t` is a natural number
`L`, and the unpaired members together with the sums of the pairs are a tight frame of length
`L`. 

### `QuadField.exists_algebraMap_eq_of_star_eq`

 Let `d` be a prime with `d ≡ 7 mod 8`. An element of `K = ℚ(√-d)` fixed by complex conjugation
is rational. 

### `exists_eq_intCast_of_mem_quadInt_of_conj_eq`

 Let `d` be a prime with `d ≡ 7 mod 8`. If a complex number `z` lies in `quadInt d`, the ring of
integers of `K = ℚ(√-d)` as a subring of `ℂ`, and is real, then `z` is a rational integer. 

### `finiteImage_mem_iff`

 An element `y` of `E` lies in the lattice `𝔞₀`, that is `finiteImage id y ∈ Ô E`, if and only if
`relDifferentGen * y` is integral at the finite places dividing `betaKInE = (1 + √-d) / 2` and `y`
is integral at the other finite places. Here `relDifferentGen` generates the different of `E/K`. 

### `valuation_galOfPlace`

 For the automorphism `galOfPlace τ` of `E/K` named by the infinite place `τ`, the valuation of
`τ(y)` at the finite place `w` is the valuation of `y` at `τ • w`, the preimage of `w` under `τ`. 

### `finiteImage_galOfPlace_mem`

 Let `P` be the parameters, `s` a natural number and `E = P.E s = K(ζ)`. The lattice
`𝔞₀ = E ∩ α Ô` of the `y` with `finiteImage id y = α⁻¹ y` integral at every finite place, `α` being
the idele of the Weil data, is stable under the automorphism `galOfPlace τ` of `E/K` named by any
infinite place `τ`. 

### `phi_betaKInE`

 Every embedding `Φ τ` of the CM type maps `betaKInE` to `quadGen d = (1 + i √d) / 2`. 

### `exists_natCast_eq_sum_norm_sq`

 Take `y` in the lattice `𝔞₀ = E ∩ α Ô`, with `α` the idele of the Weil data and `Ô` the integral
finite adeles; that is, `finiteImage id y = α⁻¹ y` lies in `Ô E`. Then the sum of `‖Φ τ y‖ ^ 2` over
the infinite places `τ` of `E`, with `Φ` the CM type, is a natural number: it is an integer of `K`,
real and nonnegative. 

### `orbit`

 The orbit of `y`: the family of the vectors `ζ ^ i * τ(y)`, indexed by the pairs `(i, τ)` with
`0 ≤ i < q₁` and `τ` an infinite place, read as an element of `Gal(E/K)` by `galOfPlace`. 

### `isTightFrame_orbit`

 Let `y` lie in the lattice `𝔞₀ = E ∩ α Ô`, that is `finiteImage id y ∈ Ô E`, and let the natural
number `ν` be the sum of the `|τ(y)| ^ 2` over the CM type. Then the vectors `w = ζ ^ i * ρ(y)` with
`i < q₁` and `ρ` in `Gal(E/K)`, each taken once, are a tight frame of length `q₁ ν`: they lie in
`𝔞₀` and satisfy `∑ w, σ(w) conj (τ(w)) = q₁ ν δ(σ, τ)` for `σ`, `τ` in the CM type. 

### `ceilLogQ₁`

 The least integer `j` with `2 ^ j ≥ q₁`. 

### `cyclotomicQuotient`

 The quotient of the cyclotomic polynomial of order `q₁` by `X - ζ`, over the integers of `E`. 

### `dualVector`

 The vector `e i`: the `i`-th coefficient of `cyclotomicQuotient`, divided by the value
`relDifferentGen` at `ζ` of the derivative of the cyclotomic polynomial and multiplied by
`conj β ^ j`, where `β = betaKInE = (1 + √-d) / 2` and `j = ceilLogQ₁`. Without `conj β ^ j`
these are, for `i < φ(q₁)`, the basis of `E/K` dual to the powers of `ζ` under the trace
(`trace_coeff_cyclotomicQuotient_div_mul_pow`). 

### `X_sub_C_mul_cyclotomicQuotient`

 `X - ζ`, with `ζ = P.zetaInt s` the primitive root of unity of order `q₁` in `𝓞 E`, times
`cyclotomicQuotient` is the cyclotomic polynomial of order `q₁`. 

### `trace_coeff_cyclotomicQuotient_div_mul_pow`

 Euler's formula. Let `b i` for `i < φ(q₁)` be the coefficients of `cyclotomicQuotient`, the
quotient over `𝓞 E` of the cyclotomic polynomial of order `q₁` by `X - ζ`, and let
`P'(ζ) = relDifferentGen` be the value at `ζ` of the derivative of the cyclotomic polynomial. The
elements `b i / P'(ζ)` are the basis of `E/K` dual to the powers `ζ ^ k` for the trace form. 

### `sum_dualVector_mul_conj`

 The vectors `e i = dualVector i` are `conj β ^ j` times the basis of `E/K` dual to the powers of
`ζ` under the trace. For `σ`, `τ` in `P.Φ s`, the infinite places of `E`, the sum of
`σ(e i) * conj τ(ζ ^ (-i))` over `i < φ(q₁)` is `conj β ^ j` for `σ = τ` and `0` otherwise. 

### `sum_mul_conj_dualVector`

 The conjugate transpose of `sum_dualVector_mul_conj`. For the vectors `e i = dualVector i`, the
sum of `σ(ζ ^ (-i)) * conj τ(e i)` over `i < φ(q₁)` is `β ^ j` for `σ = τ` and `0` otherwise. 

### `q₁_dvd_pow_ceilLogQ₁`

 `q₁` divides `((d + 1) / 4) ^ j = (β conj β) ^ j`, where `β = (1 + √-d) / 2` and
`j = ceilLogQ₁` is the least integer with `2 ^ j ≥ q₁`. 

### `finiteImage_dualVector_mem`

 Let `β = betaKInE = (1 + √-d) / 2`, let `P'(ζ) = relDifferentGen` be the value at `ζ` of the
derivative of the cyclotomic polynomial of order `q₁`, and let `j = ceilLogQ₁` be the least integer
with `2 ^ j ≥ q₁`. The vector `e i = dualVector i` is `conj β ^ j a / P'(ζ)`, where `a` is the
`i`-th coefficient of the quotient of that polynomial by `X - ζ`. It lies in the lattice
`𝔞₀ = E ∩ α Ô`. 

### `isCoprime_of_pow_add_conj_pow_eq`

 Let `P` be the parameters, with prime `d = P.d`, and `s` a natural number. Let
`β = (1 + √-d) / 2` (`quadGen P.d`) and `j ≠ 0`. An integer `t` that is equal to
`β ^ j + conj β ^ j` is prime to `q₁ = P.q₁ s`, the order of the root of unity `ζ` with `E = K(ζ)`
and `K = ℚ(√-d)`. 

### `dualResolutionFactor`

 The complex number `q₁ (1 + ∑ (e i)† (e i)) + β ^ j + conj β ^ j`. Here `e i` is `dualVector`,
for `i` below `φ(q₁)`, `y† y = ∑ |τ(y)| ^ 2` is a sum over the CM type, `β = (1 + √-d) / 2` is
`quadGen` and `j` is `ceilLogQ₁`. It is a natural number, the length of the tight frame of
`exists_isTightFrame_coprime`. 

### `isTightFrame_sumElim_inv_pow_orbit`

 Let the natural number `ν i` be the sum of `|τ(e i)| ^ 2` over the CM type, where `e i` is
`dualVector` and `i < φ(q₁)`. The powers of `ζ⁻¹` together with the orbits `ζ ^ k * τ(e i)` of the
`e i` are a tight frame in the lattice `𝔞₀` of length `q₁ (1 + ∑ ν i)`. 

### `exists_isTightFrame_factor_eq_add`

 Put `f = φ(q₁)` and `β = quadGen d = (1 + √-d) / 2`, and let `j = ceilLogQ₁` be the least
integer with `2 ^ j ≥ q₁`. The vectors `e i = dualVector i`, `i < f`, are `conj β ^ j` times the
basis of `E/K` dual to the powers of `ζ` under the trace. Let the natural number `ν i` be the sum of
`|τ(e i)| ^ 2` over the CM type and let the integer `t` be `β ^ j + conj β ^ j`. There is a tight
frame `v` of length `h = q₁ (1 + ∑ ν i) + t` that contains the vector `ζ e (f - 1)`: the `v i` lie
in the lattice `𝔞₀ = E ∩ α Ô`, with `α` the idele of the Weil data and `Ô` the integral finite
adeles, and `∑ i, σ(v i) conj (τ(v i)) = h δ(σ, τ)` for `σ`, `τ` in the CM type. 

### `exists_isTightFrame_coprime`

 Let `E = P.E s = K(ζ)`, where `K = ℚ(√-d)` and `ζ = P.ζ s` is a primitive root of unity of order
`q₁ = P.q₁ s`. Put `β = (1 + √-d) / 2` and let `j` be the least integer with `2 ^ j ≥ q₁`. The
vectors `e i = dualVector i`, `i < φ(q₁)`, are `conj β ^ j` times the basis of `E/K` dual to the
powers of `ζ` under the trace. A tight frame of length `h` is a finite family `v` in the lattice
`𝔞₀ = E ∩ α Ô`, with `α` the idele of the Weil data, such that
`∑ i, σ(v i) conj (τ(v i)) = h δ(σ, τ)` on the CM type. There is such a frame whose length `h` is
`dualResolutionFactor = q₁ (1 + ∑ i, ∑ τ, |τ(e i)| ^ 2) + β ^ j + conj β ^ j`, is prime to `q₁`, and
which contains the vector `ζ e (φ(q₁) - 1)`. 

### `norm_map_zeta_mul_dualVector`

 Let `φ` be a `p`-adic embedding of `E` whose prime `placeOfEmb φ` contains `β = (1 + √-d) / 2`
(`betaKInE`). Then `φ(ζ e (f - 1))` has the absolute value of `1 / φ(P'(ζ))`. Here `f` is the
totient of `q₁`, and `P'(ζ) = relDifferentGen` is the value at `ζ` of the derivative of the `q₁`-th
cyclotomic polynomial. Finally, `e = dualVector` is the trace-dual basis to the powers of `ζ`, times
`conj β ^ ceilLogQ₁`. 

### `HasUnitLinearForm`

 `periodFactor * conj (Φ τ y)` has absolute value 1 at the embedding `ιₚ : ℂ →+* ℂ_[p]` (the
instance `PadicPlace p`) for all `τ` in the CM type. These numbers are the coefficients of the
linear form `z ↦ periodFactor * ∑ τ, conj (Φ τ y) * Φ τ z`. 

### `exists_hasUnitLinearForm`

 Put `f = φ(q₁)` and `β = (1 + √-d) / 2`, and let `j` be the least integer with `2 ^ j ≥ q₁`. The
vector `e = dualVector (f - 1)` is `conj β ^ j / P'(ζ)`. For every prime `p` and embedding
`ιₚ : ℂ →+* ℂ_[p]`, one of the vectors `y = 1` and `y = ζ e` has the property that
`periodFactor * conj (τ(y))` has absolute value 1 at `ιₚ` for all `τ` in the CM type. 

### `exists_isTightFrame_of_coprime`

 Let `v` be a tight frame with multiplicities 1 of a length `h` prime to `q₁`. For every
`m ≥ q₁ h + R (q₁ + h)`, the powers `ζ ^ i`, `i < q₁`, and the members of `v` form a tight frame of
length `m` with suitable multiplicities, all at least `R`. 

### `norm_coeff_cyclotomic_le`

 The coefficients of the cyclotomic polynomial of order `q₁ = q₀ * towerDeg s`, where `q₀` is
the fixed modulus of the parameters `P` and `towerDeg s = 3 ^ (log₃ s + 5) * 2 ^ s`, have absolute
value at most `2 ^ q₀`. 

### `norm_phi_coeff_cyclotomicQuotient_le`

 The coefficients of `cyclotomicQuotient`, the quotient of the cyclotomic polynomial of order
`q₁` by `X - ζ`, have absolute value at most `q₁ 2 ^ q₀` under the embedding `Φ τ : E → ℂ` chosen at
any infinite place `τ`. 

### `norm_quadGen_le`

 The number `β = quadGen d = (1 + √-d) / 2` has absolute value at most `d`. 

### `norm_phi_dualVector_le`

 The vector `e i = dualVector i` is `conj β ^ j b i / P'(ζ)`, with `β = (1 + √-d) / 2`, `b i` the
`i`-th coefficient of `cyclotomicQuotient` and `P'(ζ) = relDifferentGen` the generator of the
different of `E/K`. If `P'(ζ)` has absolute value at least 1 under the embedding `Φ τ`, then
`|τ(e i)| ≤ d ^ j q₁ 2 ^ q₀`. 

### `ceilLogQ₁_le`

 The least integer `j` with `2 ^ j ≥ q₁` is at most `q₀ + 3 s + 10`. Here `q₀` is the fixed
modulus of the parameters and `q₁ = q₀ * 3 ^ (log₃ s + 5) * 2 ^ s`. 

### `one_le_norm_phi_relDifferentGen`

 For admissible data `D` with exponent `s = D.towerExp`, so that `D.E = P.E s`, the generator
`relDifferentGen` of the relative different of `E/K` has absolute value at least 1 under the
embedding `Φ τ` of every infinite place `τ`. 

### `hasLogUpper_pow_ceilLogQ₁`

 Let `D` be admissible data with weight `b = exp D.logB`. Then
`d ^ j ≤ exp (logB / 100) = b ^ (1 / 100)` for the least integer `j = ceilLogQ₁` with `2 ^ j ≥ q₁`,
where the exponent `s` in `q₁ = P.q₁ s` is `D.towerExp`; `D.HasLogUpper F l` says `|F| ≤ exp l`. 

### `le_b_of_eq_dualResolutionFactor`

 Let `D` be data for the parameters `P` (a `Data P`), with weight `b = D.b` and field
`E = P.E s = K(ζ)` for `s = D.towerExp`. The vectors `e i = dualVector i`, `i < φ(q₁)`, are
`conj β ^ j` times the basis of `E/K` dual to the powers of `ζ` under the trace. A natural number
`h` equal to the complex number `dualResolutionFactor = q₁ (1 + ∑ i, ∑ τ, |τ(e i)| ^ 2) + β ^
j + conj β ^ j` is at most `b`. This number is the length of the tight frame of
`Parameters.exists_isTightFrame_coprime`. 

### `exists_short_isTightFrame_coprime`

 Let `D` be data for the parameters `P` (a `Data P`), with weight `b = D.b` and field
`E = D.E = K(ζ)`. There are `h` prime to `q₁` with `1 ≤ h ≤ b` and a tight frame `v` of length `h`
with multiplicities 1. That is, the `v i` lie in the lattice `𝔞₀ = E ∩ α Ô`, and
`∑ i, σ(v i) conj (τ(v i)) = h δ(σ, τ)` on the CM type. Moreover, for every prime `p` and embedding
`ιₚ : ℂ →+* ℂ_[p]`, some `y` among the powers of `ζ` and the `v i` makes
`periodFactor * conj (τ(y))` a unit at `ιₚ` for all `τ` in the CM type. 

### `exists_isTightFrame`

 Let `D` be data for the parameters `P` (a `Data P`), with field `E = D.E = P.E s` for the
exponent `s = D.towerExp`, weight `b = D.b`, and `f = D.f` the number of infinite places of `E`. The
principal level `M = D.M` is the product of the two distinct primes `D.levelPrime 0` and
`D.levelPrime 1` of the data, which lie in `[b ^ 10, b ^ 11]`. There is a tight frame `v` of length
`M` with multiplicities `c i ≥ 6 f b`. Moreover, for every prime `p` and embedding
`ιₚ : ℂ →+* ℂ_[p]`, some `y = v i` makes `periodFactor * conj (τ(y))` a unit at `ιₚ` for all `τ` in
the CM type. 
