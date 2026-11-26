---
{
  "module": "src/New/Congruences/Selmer/Untied.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Untied.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Untied.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The failure to be tied

At a prime of norm `≡ 1` modulo `ℓ ^ N`, a Frobenius element `φ` and an inertial element `γ` commute
up to wild inertia and `ℓ ^ N`-th powers of inertia. If these act trivially and a cocycle `z`
vanishes on them, then `z(γ φ) = z(φ γ)`, which is the relation `(φ - 1) z(γ) = (γ - 1) z(φ)`.

Let `𝔮₀` be the first auxiliary prime and `s_𝔮` the slopes at the others. At a point of the line
`X_{𝔮₀} = Y`, `X_𝔮 = s_𝔮 Y` the relation puts `tie_w(z) = z(γ_w) - s_𝔮 z(φ_w)`, for `w = 𝔮, 𝔮̄`, in
the kernel of `φ_w - 1` for the twisted action. At `Y = 0` it does the same for `z(γ_w)`,
`w = 𝔮₀, 𝔮̄₀`. The valuation of a determinant bounds the length of the kernel.

* `New.Selmer.sub_one_smul_eq_of_tame`: the relation.
* `New.Selmer.selmerOnLine`: the Selmer module of the twist at a point of the line.
* `New.Selmer.IsTiedPrimes.relLength_tied_le`: the failure to be tied at the primes other than the
  first is at most `v(P¹(y))`, where `P¹ = New.Selmer.tiePolynomial`.
* `New.Selmer.IsTiedPrimes.relLength_tieRelations_le_sum_addVal_det`: the cost of dropping the ties
  at the first prime and its conjugate, at the point `0`.

Letters: `J` is the set of all auxiliary primes, `P₀ ∈ J` is the first prime `𝔮₀`, and `d` attaches
to `v ∈ J` the elements `φ_v = (d v).1.frob` and `γ_v = (d v).1.tameGenerator`, the homomorphism
`λ_v = (d v).1.character` to `ℤ / ℓ ^ N` and, for each index `i : ι`, the slope `(d v).2 i`.
Coefficients are taken modulo `ℓ ^ M`.

Notions from other files:
* `New.Selmer.IsTiedPrimes`: an auxiliary set `J` of primes with places, Frobenius elements `φ`,
  tame generators `γ`, characters to `ℤ / ℓ ^ N` and slopes, and a first prime `P₀ ∈ J`.
* `New.Selmer.tieRelations`: the ties `z(γ) = s z(φ)` at the primes of a set and at their
  conjugates.
* `New.Selmer.universalChar`: the polynomial `ψ_X(g) = ∏ (1 + X_j) ^ (h_j g)`;
  `New.Selmer.selmerAtPoint` is the Selmer module `Sel(x)` of the twist by `ψ_x`.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `affineAction_pow_apply`

 If `g` acts through `ρ` by the scalar `α`, then the affine action `u ↦ c(g) + g u` of the
cocycle `c` has `k`-th iterate `u ↦ α ^ k u + ∑ i < k, α ^ i c(g)` at `g`. At `u = 0` this says
`c(g ^ k) = ∑ i < k, α ^ i c(g)`. 

### `affineAction_pow_eq_one`

 If `g` acts through `ρ` by the scalar `α` and `∑ i < k, α ^ i = 0`, then the affine action
`u ↦ c(g) + g u` of the cocycle `c` at `g` has `k`-th power `1`: the element `g ^ k` acts trivially
and `c` vanishes at it. 

### `commute_affineAction`

 Let `c` be a locally constant cocycle for `ρ`, let `A` be a place of `Ω` over the prime `v`, and
let `ρ` be trivial on the elements of inertia at `A` near `1`. Each `g` acts by the affine map
`u ↦ c(g) + ρ(g) u` (`affineAction`). Suppose that this map has `q`-th power `1` for every `g` in
inertia at `A`, with `q` prime to `A`. Then the affine maps of a Frobenius element `φ` at `A` of
norm `k ≡ 1` modulo `q` and of an element `γ` of inertia at `A` commute. 

### `sub_one_smul_eq_of_commute`

 If the affine maps `u ↦ c(g) + g u` of the cocycle `c` at `g = φ` and `g = γ` commute, then
`c(γ φ) = c(φ γ)`, which is `(φ - 1) c(γ) = (γ - 1) c(φ)` by the cocycle rule. 

### `inv_sub_one_smul_eq`

 The relation `(φ - 1) c(γ) = (γ - 1) c(φ)` for a cocycle `c` passes from `φ` to `φ⁻¹` if `γ`
acts by a scalar: multiply it by `-φ⁻¹` and use `c(φ⁻¹) = -φ⁻¹ c(φ)`. 

### `sub_one_smul_eq_of_tame`

 The relation from tame inertia. Let `q` be prime to the place `A`, let `ρ` be trivial on
inertia near `1`, and let each inertial element act by a scalar `α` with `∑ i < q, α ^ i = 0`. If
`φ` or `φ⁻¹` is a Frobenius element of norm `k ≡ 1` modulo `q` and `γ` is inertial, every locally
constant cocycle `c` has `(φ - 1) c(γ) = (γ - 1) c(φ)`. 

### `lineDirection`

 The direction of the line `X_{P₀} = Y`, `X_v = s_v Y` in the space with coordinates `X_v`,
`v ∈ J`: the entry at the prime `P₀` is `1`, and the entry at `v ≠ P₀` is the slope
`s_v = (d v).2 i` that `d` attaches to `v` and the index `i`. 

### `selmerOnLine`

 The Selmer module at the point `Y = y` of the line with index `i`. The point `x` has coordinates
`x_{P₀} = y` and `x_v = e(s_v) y` for `v ≠ P₀` in `J`, where `s_v = (d v).2 i` (`lineDirection`).
The module is `Sel(x)` (`selmerAtPoint`) for the characters that `d` attaches to the primes of `J`:
the locally constant cocycles in `(O' / ℓ ^ M) ^ n` for the twist of `ρ` at `x` that are unramified
outside `S` and obey the linear relations `L`. 

### `shiftedDet`

 The polynomial `det ((1 + Y) A - 1)`. 

### `eval₂_shiftedDet`

 Evaluating `shiftedDet A` at `y`, with coefficients mapped by `e`, gives
`det ((1 + y) e(A) - 1)`. 

### `tiePolynomial`

 The polynomial `P¹(Y) = ∏_w det ((1 + Y) ρ(φ_w) - 1)`, over the primes `w` of `I` and their
conjugates; here `φ_w` is the Frobenius element of the data `d` at `v ∈ I` for `w = v`, and its
conjugate inverse for the conjugate prime. 

### `selmerAtPoint_zero`

 For a family `h` of characters to `ℤ / q`, the twist of `ρ` by the function
`ψ_x(g) = ∏ (1 + x_j) ^ (h_j g)` is trivial at `x = 0`. So the Selmer module at the point `0`, with
the places `S` of allowed ramification and the relations `L`, is the Selmer module of `ρ` with
values in `(O / ℓ ^ M) ^ n`. 

### `selmerOnLine_zero`

 For the line with index `i` (the points `x_{P₀} = Y` and `x_v = s_v Y` for `v ≠ P₀`, with
`s_v = (d v).2 i`), the point at `Y = 0` is `0`. So the Selmer module `selmerOnLine` at
`Y = 0` is the Selmer module of `ρ` with values in `(O / ℓ ^ M) ^ n`. 

### `map_smul_eq_of_reduceModPow_eq`

 If `ρ(g)` and `ρ(g')` agree modulo `ℓ ^ M`, then their images under `e : O →+* O'` act in the
same way on `(O' / ℓ ^ M) ^ n`. 

### `dvd_eval_universalChar_sub_one`

 If `y` divides all coordinates of the point `x`, then it divides `ψ_x(g) - 1`, where `ψ_x(g)` is
the value at `x` of the polynomial `universalChar h g = ∏ (1 + X_j) ^ (h_j g)`. 

### `exists_monoidHom_smul_eq_pointTwist_smul`

 Let `h` be a finite family of characters `h_j` to `ℤ / q`, let `e : O →+* O'` be a change of
coefficients, and let `ψ_x(g) = ∏ (1 + x_j) ^ (h_j g)` be the value of `universalChar h g` at a
point `x` with coordinates in `O'`. If the `1 + x_j` are `q`-th roots of unity modulo `ℓ ^ M`, then
the twisted matrices `pointTwist h x e ρ g = ψ_x(g) e(ρ(g))` act on `(O' / ℓ ^ M) ^ n` through a
representation `R` over `O' / ℓ ^ M`, and `R(g)` is the scalar `ψ_x(g)` wherever `ρ(g) ≡ 1` modulo
`ℓ ^ M`. 

### `sub_one_smul_eq_of_isAuxPrimeDataAt`

 Let `v ∤ ℓ` be a prime of the CM field `E` of norm `≡ 1` modulo `ℓ ^ N`, and let `a` consist of
a place over `v`, a Frobenius element `φ`, the tame generator `γ` and a character
(`IsAuxPrimeDataAt`). Let `S` contain `v` and its complex conjugate `star v`, let `ρ` be trivial
on inertia above `S` near `1`, and let each element of inertia above `S` act by a scalar `α` with
`∑ j < ℓ ^ N, α ^ j = 0`. Then every locally constant cocycle `c` has
`(φ_b - 1) c(γ_b) = (γ_b - 1) c(φ_b)`. Here `g_b = idOrConjInv b g` is `g` for `b = true` and
`(τ g τ)⁻¹` for `b = false`, where `τ = cmConj` is the chosen complex conjugation of `Ω`. 

### `IsTiedPrimes.frob_sub_one_smul_eq`

 Let `J` be a finite set of primes of the CM field `E` that lie, with their conjugates, outside
`S₀`, and let `d` attach to each `u ∈ J` a Frobenius element `φ_u`, a tame generator `γ_u` of
inertia and a character `λ_u` to `ℤ / ℓ ^ N`. This is the part of `hp` (`IsTiedPrimes`) that is
used; its conditions on the first prime `P₀`, the set `W`, the properties `V` and the slopes play no
role. Let `ρ` modulo `ℓ ^ M` (`reduceModPow`) be trivial on inertia outside `S₀`. Let `e : O →+* O'`
be a ring map, let `x` be a point over `O'` with coordinates divisible by `y`, and let
`∑ j < ℓ ^ N, α ^ j` vanish modulo `ℓ ^ M` whenever `α ≡ 1` modulo `y`. Let `g` act through the
twist `pointTwist`, the matrix `ψ_x(g) e(ρ(g))` with `ψ_x(g) = ∏_{u ∈ J} (1 + x_u) ^ (λ_u g)`, and
let `z` be a locally constant cocycle in `(O' / ℓ ^ M) ^ n` for this twist, unramified outside `S`
and obeying the linear relations `L` (`selmerAtPoint`). Then `(φ_w - 1) z(γ_w) = (γ_w - 1) z(φ_w)`
for `w` a prime `v` of `J` (`b = true`) or its conjugate (`b = false`), where `φ_w`, `γ_w` are
`φ_v`, `γ_v` or their conjugate inverses (`idOrConjInv`). 

### `IsTiedPrimes.frob_sub_one_smul_tie_eq_zero_of_selmerOnLine`

 Let `J` be a finite set of primes of the CM field `E` that lie, with their conjugates, outside
`S₀`. Let `d` attach to each `v ∈ J` a Frobenius element `φ_v`, a tame generator `γ_v` of inertia, a
character `λ_v` to `ℤ / ℓ ^ N` and a slope `s_v = (d v).2 i` in `O` for the index `i : ι`. The
hypothesis `hp` (`IsTiedPrimes`) says this, and further that `P₀ ∈ J` is a first prime, that for
`v ≠ P₀` the value `λ_u(φ_v)` is `1` for `u = P₀` and `0` otherwise, and that the property `V i`
holds at `φ_v` and its conjugate inverse if `s_v ≠ 0`.

Let `ρ` modulo `ℓ ^ M` be trivial on inertia outside `S₀` and at the elements with the property
`V i`, and let `∑ j < ℓ ^ N, α ^ j` vanish modulo `ℓ ^ M` whenever `α ≡ 1` modulo `y`. Let `z` be a
locally constant cocycle for the twist of `ρ` at the point `x_{P₀} = y`, `x_v = e(s_v) y`,
unramified outside `S` and obeying the linear relations `L` (`selmerOnLine`). Then the matrix
`(1 + y) e(ρ(φ_w)) - 1` kills `z(γ_w) - e(s_v) z(φ_w)`. Here `w` is a prime `v` of `J` (`b = true`)
or its conjugate (`b = false`), where `φ_w`, `γ_w` are `φ_v`, `γ_v` or their conjugate inverses
(`idOrConjInv`), and `v` may be `P₀` only if `y = 0`. 

### `IsTiedPrimes.relLength_tied_le_sum_ker`

 Let `J` be a finite set of primes of the CM field `E` that lie, with their conjugates, outside
`S₀`. Let `d` attach to each `v ∈ J` a Frobenius element `φ_v`, a tame generator `γ_v` of inertia, a
character to `ℤ / ℓ ^ N` and a slope `s_v = (d v).2 i` in `O` for the index `i : ι`. The hypothesis
`hp` (`IsTiedPrimes`) says this, singles out a first prime `P₀ ∈ J` with Frobenius element in `W`,
fixes the values of the characters at the `φ_v` with `v ≠ P₀`, and gives the property `V i` at `φ_v`
and its conjugate inverse if `s_v ≠ 0`.

Let `ρ` modulo `ℓ ^ M` be trivial on inertia outside `S₀` and at the elements with the property
`V i`, and let `∑ j < ℓ ^ N, α ^ j` vanish modulo `ℓ ^ M` whenever `α ≡ 1` modulo `y`. Consider the
locally constant cocycles `z` for the twist of `ρ` at the point `x_{P₀} = y`, `x_v = e(s_v) y`,
unramified outside `S` and obeying the linear relations `L` (`selmerOnLine`). Let `I ⊆ J` contain
`P₀` only if `y = 0`, and let `w` run over the primes `v` of `I` and their conjugates, where `φ_w`,
`γ_w` are `φ_v`, `γ_v` or conjugate inverses (`idOrConjInv`). The quotient by the cocycles with
`z(γ_w) = e(s_v) z(φ_w)` for all `w` (`tieRelations`) has length (`relLength`) at most the sum of
the lengths of the kernels of the `(1 + y) e(ρ(φ_w)) - 1` on `(O' / ℓ ^ M) ^ n`. 

### `IsTiedPrimes.relLength_tied_le`

 Let `J` be a finite set of primes of the CM field `E` that lie, with their conjugates, outside
`S₀`. Let `d` attach to each `v ∈ J` a Frobenius element `φ_v`, a tame generator `γ_v` of inertia, a
character to `ℤ / ℓ ^ N` and a slope `s_v = (d v).2 i` in `O` for the index `i : ι`. The hypothesis
`hp` (`IsTiedPrimes`) says this, singles out a first prime `P₀ ∈ J` with Frobenius element in `W`,
fixes the values of the characters at the `φ_v` with `v ≠ P₀`, and gives the property `V i` at `φ_v`
and its conjugate inverse if `s_v ≠ 0`.

Let `ρ` modulo `ℓ ^ M` be trivial on inertia outside `S₀` and at the elements with the property
`V i`, and let `∑ j < ℓ ^ N, α ^ j` vanish modulo `ℓ ^ M` whenever `α ≡ 1` modulo `y`. Consider the
locally constant cocycles `z` for the twist of `ρ` at the point `x_{P₀} = y`, `x_v = e(s_v) y`,
unramified outside `S` and obeying the linear relations `L` (`selmerOnLine`). Adding the ties
`z(γ_w) = e(s_v) z(φ_w)` for `w` a prime `v ≠ P₀` of `J` or its conjugate (`tieRelations`) lowers
the length by at most the normalised valuation `addVal` of `tiePolynomial ρ (J.erase P₀) d`, with
coefficients mapped by `e`, evaluated at `y`. 

### `IsTiedPrimes.relLength_tieRelations_le_sum_addVal_det`

 Release of the first prime. Let `J` be a finite set of primes of the CM field `E` that lie, with
their conjugates, outside `S₀`. Let `d` attach to each `v ∈ J` a Frobenius element, a tame generator
of inertia, a character to `ℤ / ℓ ^ N` and a slope `(d v).2 i` in `O` for the index `i : ι`. The
hypothesis `hp` (`IsTiedPrimes`) says this, singles out a first prime `P₀ ∈ J` of slope `0` with
Frobenius element `φ₀` in `W`, and gives the property `V i` at the Frobenius elements of the primes
with nonzero slope.

Let `ρ` modulo `ℓ ^ M` be trivial on inertia outside `S₀` and at the elements with the property
`V i`, let `M ≤ N`, and let `φ₀` and its conjugate inverse `φ₀^{-c}` (`idOrConjInv`) act modulo
`ℓ ^ M` as `g₀` and `g₀^{-c}`. Consider the locally constant cocycles `z` for `ρ` in
`(O / ℓ ^ M) ^ n`, unramified outside `S` and obeying the linear relations `L` (`selmerModule`). The
relations `tieRelations {P₀} d i` say `z(γ₀) = 0 = z(γ₀^{-c})` for the tame generator `γ₀` at `P₀`.
Adding them lowers the length by at most `∑ v(det (ρ(g) - 1))`, over `g = g₀, g₀^{-c}` (`relLength`
is the length of the quotient, `v = addVal` the normalised valuation). 
