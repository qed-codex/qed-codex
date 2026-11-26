---
{
  "module": "src/New/Congruences/Selmer/GeneralTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Twisting, general form

For finitely many Selmer data and Stickelberger systems (under the hypotheses of
`New.Selmer.exists_anticyclotomic_twist`) there is one anticyclotomic character whose first `m`
powers have short Selmer groups, values of small valuation at the elements of the systems, and
values far from `1` at the tame generators. The character is `∏ ζ_𝔮 ^ λ_𝔮`, with the `λ_𝔮` of
`New.Selmer.exists_twistPolynomials` and roots of unity `ζ_𝔮` from
`New.Selmer.exists_rootsOfUnity_ellVal_eval_le_add`.

* `New.Selmer.IsSmallTwist`: the bounds for one character.
* `New.Selmer.exists_rootsOfUnity_ellVal_eval_le`: roots of unity that serve all powers up to `m`.
* `New.Selmer.exists_anticyclotomic_twist`: one twist that works for all powers up to `m`.

Notions from other files:
* `New.Selmer.SelmerDatum ℓ S₀ g₀ O n`: a lattice `T = O ^ n` with an action of `Gal(Ω/E)`
  unramified outside `S₀`, local conditions above `ℓ`, and the number `β_T`, which includes the
  valuations of `det(ρ g - 1)` for `g = g₀` and its conjugate inverse. `TwistedLengthLe Q ψ b`
  says that its Selmer group `Sel_Q(T ψ)` has normalised length at most `b` over all large
  coefficient rings (`CoeffRing.normLength`: `len (O / ℓ) = 1`).
* `New.Selmer.StickelbergerSystem ℓ S₀ g₀`: a character `ϑ` unramified outside `S₀` with
  `ϑ g₀ ≠ 1`, elements `Θ_Q` of the group rings of class groups `Cl_Q` with a norm relation, and
  the number `β`.
* `New.Selmer.TwistPolynomials T Y s₀ r N`: an auxiliary set `Q` of at most `s₀ / 2` primes,
  homomorphisms `λ_𝔮` to `ℤ / ℓ ^ N` for `𝔮 ∈ Q`, and for each datum and system a polynomial in
  variables indexed by `Q` with a point whose coordinates have valuation at least `r`.
* `New.ellVal`: the valuation `v` on `PadicAlgCl ℓ` with `v(ℓ) = 1`, read in `[0, ∞]`.


### `IsSmallTwist`

 The conclusions of the general twisting theorem for Selmer data `T i`, Stickelberger systems
`Y k`, a bound `ε`, a set of primes `Q` and one character `ψ`. The datum `T i` is a lattice
`O ^ n i` with a Galois action unramified outside `S₀`, local conditions above `ℓ` and a finite
number `β_T = (T i).β`, a sum of lengths of `O`-modules. The system `Y k` has elements
`Θ_Q = (Y k).element Q` of the group rings of class groups `Cl_Q` and a finite number
`β = (Y k).β`, a sum of valuations. The element `g₀` enters the bounds through `β_T` and `β`.
Below, `v` is the valuation `ellVal` with `v(ℓ) = 1`. 

### `IsSmallTwist.isFromU1`

 `ψ` comes by `y ↦ y / ȳ` from an idele class character of tame level `Q` trivial above `ℓ`;
  so it is locally constant, anticyclotomic, unramified outside `Q ∪ Q̄` and trivial on the
  decomposition groups above `ℓ`. 

### `IsSmallTwist.exists_pow_eq_one`

 The order of `ψ` is a power of `ℓ`. 

### `IsSmallTwist.ramified`

 `ψ` is ramified at every prime of `Q`. 

### `IsSmallTwist.length_le`

 (a) `len Sel_Q(T ψ) ≤ β_T + ε` for each datum, with lengths scaled so that
  `len (O / ℓ) = 1`. 

### `IsSmallTwist.ellVal_value_le`

 (b) `v(ψ(Θ_Q)) ≤ β + ε` for each system. 

### `IsSmallTwist.sum_le_of_isTameGenerator`

 (c) `∑ v(ψ(γ_w) - 1) ≤ ε`, over `w ∈ Q ∪ Q̄`, for any tame generators `γ_w` at any places
  `A w` above `w`. 

### `IsSmallTwist.mono`

 If `ψ` satisfies `IsSmallTwist T Y ε Q ψ` (the conclusions of the general twisting theorem with
bound `ε`), then it satisfies `IsSmallTwist T Y ε' Q ψ` for every `ε' ≥ ε`. 

### `IsSmallTwist.sum_ellVal_tameGenerator_sub_one_le`

 If `ψ` is a small twist (`IsSmallTwist T Y ε Q ψ`), then the sum of `ellVal (ψ γ_w - 1)` over
`w ∈ Q ∪ Q.image star` is at most `ε`. Here `γ_w` is the chosen tame generator
(`(hA w).tameGenerator`) at the place `A w` above `w`. 

### `exists_map_eq_map_pow_of_isTameGenerator`

 Let `ψ` be a locally constant character of `Gal(Ω/E)` with `ψ ^ q = 1`. Let `A` be a place of
`Ω` (a valuation subring) above `w` at which `q` is a unit. Let `γ` be a tame generator of the
inertia group of `A`: for each `n` that is a unit at `A`, it multiplies an `n`-th root of some
uniformiser of `E` by a primitive `n`-th root of unity. Then `ψ` maps every element of an inertia
group above `w` to a power of `ψ γ`. 

### `eval_aeval`

 Evaluation at `x` of `P` with `f j` put for the variable `j` is evaluation of `P` at the values
of the `f j` at `x`. 

### `normLength_ne_top`

 A finite length `b` has finite normalised length `O.normLength b` (the multiple of `b` by the
valuation of a uniformiser of `O`). 

### `exists_nnrat_mul_le`

 For a natural number `s` and `ε > 0` there is a rational `r > 0` with `s r ≤ ε`. 

### `twist`

 The character `ψ = ∏ ζ_𝔮 ^ λ_𝔮`, a product over the primes `𝔮` of `X.auxPrimes`, for twist
polynomials `X` with homomorphisms `λ_𝔮 = X.primeChar 𝔮` to `ℤ / ℓ ^ N`, and for roots of unity
`ζ_𝔮` of order dividing `ℓ ^ N` in the ring `intQpBar ℓ` of integers of `PadicAlgCl ℓ`. The
parameters `s₀` (at least twice the number of primes) and `r` (a lower bound for the valuations of
the points of `X`) play no part in the definition. 

### `twist_apply`

 The value of the twist at `g` is `∏ ζ_𝔮 ^ λ_𝔮(g)`, with `λ_𝔮(g)` read in `[0, ℓ ^ N)`. 

### `coe_pow_apply_pow_eq_one`

 If each `ζ_𝔮` has order dividing `ℓ ^ N`, then so does each `ζ_𝔮 ^ j`. 

### `twist_pow`

 The power `ψ ^ j` of the twist `ψ = ∏ ζ_𝔮 ^ λ_𝔮` by roots of unity `ζ_𝔮` of order dividing
`ℓ ^ N` is the twist by the `ζ_𝔮 ^ j`, which again have order dividing `ℓ ^ N`. 

### `twist_pow_eq_one`

 The twist by roots of unity of order dividing `ℓ ^ N` has order dividing `ℓ ^ N`. 

### `isFromU1_twist`

 Let `Q = X.auxPrimes` be the auxiliary primes of the twist polynomials `X`, and let
`ψ = X.twist hζ` be the twist by `ℓ ^ N`-th roots of unity `ζ v`, for `v ∈ Q`. Then `ψ` is locally
constant and `ψ(Art y) = η(y / ȳ)` for a character `η` of the finite ideles of `E` that is trivial
on `Eˣ` and on the ideles that are units away from `ℓ`, arbitrary above `ℓ` and congruent to `1` at
the primes of `Q` not above `ℓ`. 

### `exists_mem_inertiaAbove_twist_eq`

 Let `X` be twist polynomials for the Selmer data `T` and the Stickelberger systems `Y`. Of `X`
only two parts enter: the set of primes `X.auxPrimes` of `E` and, for each prime `u` in it, a
homomorphism `λ_u = X.primeChar u` from `Gal(Ω/E)` to `ℤ / ℓ ^ N` that is onto on inertia at `u`
and unramified outside `u` and its conjugate. Let `ζ u` be `ℓ ^ N`-th roots of unity in the ring
`intQpBar ℓ` of integers of `PadicAlgCl ℓ`, and let `ψ = X.twist hζ = ∏ (ζ u) ^ λ_u`. For a prime
`v` of `X.auxPrimes` and `w` equal to `v` or to its conjugate `star v`, the character `ψ` takes
the value `ζ v` on some element of an inertia group above `w`. 

### `ellVal_twist_tameGenerator_sub_one_le`

 Let `X` be twist polynomials, with auxiliary primes `X.auxPrimes` and homomorphisms `λ_u` from
`Gal(Ω/E)` to `ℤ / ℓ ^ N`, one for each prime `u` of `X.auxPrimes`. Let `ζ u` be `ℓ ^ N`-th roots of
unity and `ψ = X.twist hζ = ∏ (ζ u) ^ λ_u`. Let `S₀` contain the places above `ℓ`, let `v` be an
auxiliary prime and `w` be `v` or its conjugate. For a generator `γ` of tame inertia at a place `A`
of `Ω` above `w`, the valuation of `ψ γ - 1` is at most that of `ζ v - 1`, since `ζ v` is a power of
`ψ γ`. 

### `sum_ellVal_twist_tameGenerator_sub_one_le`

 Let `X` be twist polynomials, with a set `X.auxPrimes` of at most `s₀ / 2` auxiliary primes and
homomorphisms `λ_v` from `Gal(Ω/E)` to `ℤ / ℓ ^ N`, one for each prime `v` of `X.auxPrimes`. Let
`ζ v` be `ℓ ^ N`-th roots of unity and `ψ = X.twist hζ = ∏ (ζ v) ^ λ_v`. Let `S₀` contain the
places above `ℓ`, and let all `ζ v - 1` have valuation at most `r`, for the valuation `ellVal`
that is `1` at `ℓ`. For any generators `γ w` of tame inertia at places `A w` of `Ω` above `w`, the
sum of the valuations of `ψ (γ w) - 1`, over the primes `w` of `X.auxPrimes` and their conjugates,
is at most `s₀ r`. 

### `isSmallTwist_twist`

 Let `T i` be Selmer data and `Y k` Stickelberger systems. Let `X` be twist polynomials with
primes `Q = X.auxPrimes`, let `ζ v` be `ℓ ^ N`-th roots of unity for `v ∈ Q`, let `ψ = X.twist hζ`
and let `x` be the point `(ζ v - 1)_v`. The valuation of `X.datumPoly i` at `x` bounds the length of
the Selmer group of `T i` twisted by `ψ` when it is below `O.normLength (T i).β + 1`, and the value
of `X.systemPoly k` at `x` is `ψ(Θ_Q)`. Suppose that `S₀` contains the places above `ℓ`, that all
`ζ v - 1` have valuation at most `r`, with `s₀ r ≤ ε < 1`, and that these polynomials have at `x`
valuation at most `O.normLength (T i).β + ε` and `(Y k).β + ε`. Then `ψ` satisfies `IsSmallTwist`:
it is anticyclotomic of tame level `Q`, of `ℓ`-power order and ramified at every prime of `Q`; the
Selmer lengths are at most `O.normLength (T i).β + ε`; the valuations of the `ψ(Θ_Q)` are at most
`(Y k).β + ε`; and the valuations of `ψ(γ_w) - 1`, for generators `γ_w` of tame inertia above the
primes `w` of `Q` and their conjugates, have sum at most `ε`. 

### `exists_rootsOfUnity_ellVal_eval_le`

 Let natural numbers `s₀` and `m ≥ 1`, a rational `r > 0`, finitely many finite bounds `β i` and
`ε > 0` be given, and write `v` for the valuation `ellVal` on the ring `intQpBar ℓ` of integers of
`PadicAlgCl ℓ`. There is an `h₀` with the following property. If the `P i` are integral polynomials
in at most `s₀` variables and the coordinates of the points `x i` have valuation at least `r`, with
`v(P i (x i)) ≤ β i`, then there are roots of unity `ζ_u` of order dividing `ℓ ^ h₀`, one for each
variable `u`, with `v(ζ_u - 1) ≤ r / m` and `v(P i ((ζ_u ^ j - 1)_u)) ≤ v(P i (x i)) + ε` for
`1 ≤ j ≤ m`. 

### `exists_anticyclotomic_twist`

 The twisting theorem, general form. Let `E` be a CM number field inside the algebraic closure
`Ω` of `ℚ`, let `ℓ` be a prime, `v` the valuation of `PadicAlgCl ℓ` with `v(ℓ) = 1`, and `O` the
ring of integers of a finite Galois extension of `ℚ_ℓ`; lengths are scaled so that
`len (O / ℓ) = 1`. Let `S₀` be a finite set of places of `E` that contains those above `ℓ`, and let
`g₀` be inertial at a place of `S₀` prime to `ℓ`. Finitely many objects of two kinds are given.
* A Selmer datum `T i` is a lattice over `O` with an action `ρ` of `Gal(Ω/E)` unramified outside
  `S₀` and local conditions above `ℓ`. Its number `β_T` is a finite sum of lengths: a global term,
  local terms at places of `S₀` prime to `ℓ`, and the valuations of `det(ρ g - 1)` for `g = g₀` and
  for the inverse of its complex conjugate.
* A Stickelberger system `Y k` has a character `ϑ` and elements `Θ_Q` of the group rings of class
  groups `Cl_Q` with a norm relation. Its number `β` is the valuation of the trivial character at
  `Θ_∅` plus a multiple of `v(ϑ g₀ - 1)`.

The ring `O` is large enough: `IsTorsionLevel T M` says that `M > β_T + 1` for each datum and that
the residue field of `O` has more than `2 rank(T i) a + 1` elements, where `a` is the unscaled
length of `O / ℓ ^ M` (`frequently_lt_card_residueField` gives such rings). Let `m ≥ 1` and `ε > 0`.
Then there are an auxiliary set `Q` (primes of prime norm such that neither they nor their
conjugates lie in `S₀` and their conjugates lie outside `Q`) and a character `ψ` of `Gal(Ω/E)` such
that each `χ` among `ψ, …, ψ ^ m` satisfies `IsSmallTwist`. That is, `χ` comes by `y ↦ y / ȳ` from
an idele class character of tame level `Q` trivial above `ℓ`, has `ℓ`-power order, is ramified at
every prime of `Q`, and
* the Selmer group of each `T i` twisted by `χ` has length at most `β_T + ε`;
* `v(χ(Θ_Q)) ≤ β + ε` for each `Y k`;
* `∑ v(χ(γ_w) - 1) ≤ ε`, over the primes `w` of `Q` and their conjugates, for any generators `γ_w`
  of tame inertia above `w`. 
