---
{
  "module": "src/New/UpperBound/Divisibility/LocalDivisibility.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The divisibility of the composite lift at each prime

This file bounds the gauge of the composite lift `New.Data.compositeLift` at a prime p, for a fixed
embedding ι : ℂ → ℂ_p; for p ≠ N it does so through the expansion `New.Data.restrictedChain` into
chains of `m` lifts. At the exceptional primes it uses the bound of
`New.Data.IsMarked.isOntoUpToColength_scaledHeckeOperator` for the elementary divisors of the
normalised Hecke operators `New.Data.IsMarked.scaledHeckeOperator`.

A form *has valuation at least* `v` if its gauge at the base point `1` is at most `p ^ (-v)`. The
*a-places* (`New.Data.aPlaces`) are the infinite places ≡ 1 modulo q₀. At a non-split prime `p < x₁`
that is not *exceptional* (`New.Data.IsExceptional`), the loss pays for all collisions between
a-places. For an exceptional prime `p < x₁`, a *full mark* is a choice `Λ` of one prime from each
conjugate pair induced by the a-places; the places *inducing* `Λ` are those that induce a prime of
`Λ`, the *odd* places those that induce the conjugate of one.

With `m` the number of lifts, `f` the number of infinite places of `E` and `a` the length of a long
row, the exponents below are built from the following numbers.

* `D.heckeScalingExponent l` is `a` times the number of a-places that induce the prime `l`.
* `D.collisionExponent p`, written `j_p`, is the ceiling of `2 m f a / p`.
* `D.collisionSum p ev` is the sum of `a / p ^ e` over the collisions `(τ, e)` outside the set of
  places `ev` (`New.Data.IsCollision`).

## Main definitions and results

* `New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_one`: for p different from N and d, the chain
  of lifts keeps integrality.
* `New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_collisionSum`: at a non-split prime `p < x₁`
  the bounds for single lifts add up to the gain, less the loss and `m` times the collision sum.
* `New.Data.IsWeakChainDatum.gaugeLe_restrictedChain_of_isFullMark`: for a full mark Λ, the bound
  for `New.Data.restrictedChain` on the image of the m-th power of the product of the operators
  `New.Data.IsMarked.scaledHeckeOperator`.
* `New.Data.IsMarked.isOntoUpToColength_prod_scaledHeckeOperator_pow`: this power keeps the integral
  source forms and is onto modulo `p ^ j_p` up to a small colength.
* `New.Data.exists_colengthDvd_gaugeLe_compositeLift`: there is a module of source forms whose
  integral members have colength at most l in the integral source forms, with
  l ≤ allowedLoss(p) · dim (source forms), and on whose ramified members the composite lift of a
  chain datum has valuation at least gain(p) − allowedLoss(p).
* `New.Data.exists_err_gaugeLe_compositeLift`: the same bound for all primes p, on a submodule of
  the integral ramified source forms, with losses err(p) such that every finite sum ∑ err(p) log p
  is at most `New.Data.errorUnit`.

Notions from other files:
* `New.GaugeLe d c φ`: for every `g`, the p-adic gauge of the value `φ g` at `g * d` is at most `c`.
* `New.ColengthDvd M N z`: the index of `N` in `M` divides `z`, that is, each finite family in `M`
  has combinations in `N` by a matrix whose determinant divides `z`.
* `New.IsOntoUpToColength p M n y c`: the endomorphism `y` keeps `M`, and `y (M) + p ^ n • M` has
  index dividing `p ^ l` in `M` for some natural number `l ≤ c`.
* `New.Data.allowedLoss`: 2·loss(p) for a non-split prime p < x₁ (`New.Data.loss`); otherwise 2mfb
  if p = N, and 0 if not.
* `New.Data.gain`: the divisibility asked of the chain of lifts at p.

## Relation to the literature

For each prime p and twist of conductor prime to p, the chain of theta lifts is divisible by the
predicted power of p, less an error, on a submodule of the ramified source forms whose colength per
dimension is at most that error. The errors times log p have a small sum, which gives the
divisibility side of the bound. p-integrality of single theta lifts is known in the literature.
Related work: X. Zhang, Non-vanishing mod p of theta lifts for (O(2n+1),Mp(4n)), 2022; Berger,
Arithmetic properties of similitude theta lifts, 2009; Prasanna, Integrality of a ratio of Petersson
norms, 2006.

At an inert prime p pairing two a-places, each lift may lose divisibility. Outside a sparse set of
such p, the chain regains the predicted power of p, up to about one lift's loss, on the image of
scaled Hecke operators above p applied once per lift. Once enlarged by a p-power multiple of all
source forms, this image has small colength. Hecke operators passing through theta lifts, p-power
scaling by weight and p-adapted lifts at ordinary p are known in the literature. Related work:
Rallis, Langlands' functoriality and the Weil representation, 1982; V. Lafforgue, Estimées pour les
valuations p-adiques des valeurs propres des opérateurs de Hecke, 2011; Z. Liu, Test Schwartz
functions at p for theta lifts of Hida families, arXiv 2510.21644, 2025.


 ## Gauge bounds under sums, scalars and larger exponents 

### `rpow_mono`

 Gauge bounds can be weakened. If the `p`-adic gauge of every value `φ g` of a form, taken at
`g * d` for a fixed adelic point `d` (`New.GaugeLe`), is at most `p ^ r`, then it is at most
`p ^ r'` for every `r' ≥ r`. 

### `add`

 The `p`-adic gauge is ultrametric. If, for a fixed adelic point `d` and every `g`, the gauges of
the values of two forms at `g`, taken at `g * d` (`New.GaugeLe`), are at most `c`, then the same
holds for the sum of the two forms. 

### `smul`

 Let `c` bound, for a fixed adelic point `d` and every `g`, the `p`-adic gauge of the value `φ g`
at `g * d` (`New.GaugeLe`). Then the values of `a • φ` are bounded in the same sense by `c` times
the `p`-adic absolute value of the complex number `a`. 

### `zpow_neg_smul`

 Let `p ^ r` bound, for a fixed adelic point `d` and every `g`, the `p`-adic gauge of the value
`φ g` at `g * d` (`New.GaugeLe`), and let `β` be an integer with `β ≤ -r`. Then `p ^ (-β) • φ` has
these gauges at most `1`. 

 ## The valuation of the chains of lifts of a weak chain datum 

### `IsWeakChainDatum.gaugeLe_restrictedChain_of_mem_raises`

 Let `Ψ` be a weak chain datum for the twist `ϑ`: coefficients, subject to integrality and
invariance conditions, of tuples `x` of translations. The datum `translateDatum x j` of the `j`-th
theta lift is the normalised vacuum vector translated by `x j`. That it lies in
`raises 1 1 (p ^ r j)` says that this lift, with both gauges based at the identity, multiplies
`p`-adic gauges by at most `p ^ r j`. Suppose this holds for every `x` in the support of `Ψ`, that
`p ≠ D.N`, and that `p` is prime to `ϑ.normQ`, the product of the norms of the places in the set Q
of `ϑ`. Then `restrictedChain ϑ Ψ`, the combination with coefficients `Ψ` of chains of `D.m` lifts,
sends an integral source form to a form of gauge at most `p ^ ∑ j < D.m, r j`. 

### `IsWeakChainDatum.gaugeLe_restrictedChain_one`

 Let `Ψ` be a weak chain datum for the twist `ϑ`: coefficients, subject to integrality and
invariance conditions, of tuples of translations. Let `p` be a prime prime to the norm of the level
of `ϑ` and different from the level `N` and from `d`, the prime parameter that defines the quadratic
character `χ_K`. Then `restrictedChain ϑ Ψ`, the combination with coefficients `Ψ` of chains of `m`
theta lifts, sends an integral source form `v` to an integral form: in `GaugeLe 1 1`, the first `1`
is the base point, the second the bound on the `p`-adic gauge. 

### `IsWeakChainDatum.gaugeLe_restrictedChain_collisionSum`

 Let `Ψ` be a weak chain datum for the twist `ϑ`, and `p < x₁` a non-split prime
(`IsSmallNonsplit`) prime to the norm of the level of `ϑ`. For an integral source form `v`, the
image under the combination `restrictedChain ϑ Ψ` of chains of `m` theta lifts has valuation at
least `gain p - loss p - m * collisionSum p ∅`.

Here `gain p` is the divisibility asked of the chain at `p` and `loss p = f a (log b)² / p`, times
`m` if `p ≡ ±1` modulo `m`. 

### `IsWeakChainDatum.gaugeLe_pow_collisionExponent_smul`

 The crude bound. Let `Ψ` be a weak chain datum for the twist `ϑ`, and `p < x₁` a non-split prime
(`IsSmallNonsplit`) prime to the norm of the level of `ϑ`. For an integral source form `v` and
`j_p = D.collisionExponent p = ⌈2 m f a / p⌉`, the image of `p ^ j_p • v` under the combination
`restrictedChain ϑ Ψ` of chains of `m` theta lifts has valuation at least `gain p - loss p`. 

### `IsWeakChainDatum.gaugeLe_restrictedChain_of_isFullMark`

 **Valuation.** Let `Ψ` be a weak chain datum for the twist `ϑ` (`New.Data.IsWeakChainDatum`) and
let `p` be prime to the norm of the level of `ϑ`. Let `Λ` be a full mark: a set of primes above `p`,
disjoint from its conjugate and induced by a-places, that contains the prime of each a-place or its
conjugate, where `p < x₁` is exceptional and non-split. Let `Y` be the product over `l ∈ Λ` of
`scaledHeckeOperator l`, the Hecke operator at `l` of index `D.ceilLogLifts p` scaled by
`p ^ heckeScalingExponent l`.

For an integral source form `v`, the image of `(Y ^ m) v` under the combination
`restrictedChain ϑ Ψ` of chains of `m` theta lifts has valuation at least `gain p - 2 * loss p`,
that is, `p`-adic gauge at most `p ^ (2 * loss p - gain p)`. Here `gain p` is the divisibility asked
of the chain and `loss p = f a (log b)² / p`, times `m` if `p ≡ ±1` modulo `m`. 

 ## The index of the image of the scaled Hecke operators 

### `IsMarked.mul_sum_heckeScalingExponent_le_loss`

 Let `Λ` be a marked set of primes of `E` above the exceptional non-split prime `p < x₁`: it is
disjoint from its conjugate and each of its primes is induced by an a-place. Let
`A_l = heckeScalingExponent l`, which is `a` times the number of a-places that induce `l`,
`j_p = collisionExponent p = ⌈2 m f a / p⌉`, `m` the number of lifts and `f` the number of infinite
places of `E`. Then `m` times the sum over `l ∈ Λ` of `12 A_l / (m p) + j_p / (m ^ 2 f)`, the
colength exponent per dimension of the scaled Hecke operator at `l`, is at most `loss p`, which is
`f a (log b)² / p`, times `m` if `p ≡ ±1` modulo `m`. 

### `IsMarked.isOntoUpToColength_prod_scaledHeckeOperator_pow`

 **Colength.** Let `Λ` be a marked set of primes above the exceptional non-split prime `p < x₁`,
`Y` the product over `l ∈ Λ` of the Hecke operators at `l` scaled by `p ^ heckeScalingExponent l`,
and `M` the module of integral source forms. Then `Y ^ m`, with `m` the number of lifts, keeps `M`,
and the index of `Y ^ m M + p ^ j_p M` in `M` divides `p ^ c` for some natural number
`c ≤ loss p * dim (source forms)`. 

### `mem_smallNonsplitPrimes_iff_isSmallNonsplit`

 A prime `p` lies in `D.smallNonsplitPrimes` if and only if `p < x₁` and `χ_K(p) ≠ 1`. 

### `chiK_eq_one_or_le_of_notMem_smallNonsplitPrimes`

 A prime `p` outside `D.smallNonsplitPrimes` splits in `K`, that is `χ_K(p) = 1`, or is at least
`x₁`. 

### `IsChainDatum.gaugeLe_compositeLift_of_isFullMark`

 Let `Ψ` be a chain datum for the twist `ϑ`, with `p` prime to the norm of the level of `ϑ`. Let
`Λ` be a full mark: a set of primes above the exceptional non-split prime `p < x₁`, disjoint from
its conjugate and induced by a-places, that contains the prime of each a-place or its conjugate. Let
`Y` be the product over `l ∈ Λ` of the Hecke operators at `l` scaled by
`p ^ heckeScalingExponent l`, `M` the module of integral source forms over the ring `embValRing` of
complex numbers that are `p`-integral under `ιₚ`, and `j_p = collisionExponent p = ⌈2 m f a / p⌉`.

The composite lift passes a source form through `m` theta lifts with the glued tensor of `Ψ` as data
and restricts the result from `X_m` to `Y_m`. For a source form in `Y ^ m M + p ^ j_p M` it has
valuation at least `gain p - 2 * loss p`. 

### `exists_colengthDvd_gaugeLe_compositeLift`

 The divisibility at one prime. There are a natural number `l ≤ allowedLoss p * dim`, where `dim`
is the dimension of the space of source forms, and a module `S` of source forms whose integral
members have index dividing `p ^ l` in the integral source forms (`New.ColengthDvd`), such that for
every twist `ϑ` of level prime to `p` and every chain datum `Ψ` (`New.Data.IsChainDatum`) the
composite lift of a ramified source form in `S` has valuation at least `gain p - allowedLoss p`. 

### `exists_err_gaugeLe_compositeLift`

 **Divisibility of the composite lift.** There are real numbers `err p` with these properties.
* (a) Each `err p` is non-negative.
* (b) If `p ≠ N`, and `chiK d p = 1` (split primes) or `x₁ ≤ p`, then `err p = 0`.
* (c) Every finite sum `∑ err p * log p` is at most `errorUnit`.
* (d) For every prime `p` and every embedding `ιₚ` of `ℂ` in `ℂ_p`, the module of integral ramified
  source forms has a submodule `S`, over the ring `embValRing` of numbers that `ιₚ` sends to
  `p`-adic integers, of index dividing `p ^ l` for a natural number `l ≤ err p * dim`, such that the
  composite lift of every source form in `S` has valuation at least `gain p - err p`, for all twists
  `ϑ` of level prime to `p` and all chain data `Ψ`.

Here `dim` is the dimension of the space of source forms, `N` the level, `x₁` the second cut-off and
`chiK d` the quadratic character `χ_K` of the prime parameter `d`. 
