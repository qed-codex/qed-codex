---
{
  "module": "src/New/Reduction/Zeros/Criterion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The one-sided criterion for a zero-free half-plane

`New.LFunction_ne_zero_of_primeRemainder_le`: an eventual upper bound `R_q(x) ≤ x ^ (β - 1)` for the
remainder of a sum over prime powers `≡ 1` mod `q` with weights depending on a prime `d`, for all
`d` of a suitable class, excludes zeros `s ≠ 1` of the `L(s, ψ)`, `ψ` mod `q`, in `re s > β`.

Notions from other files:
* `primeRemainder d q x`: the remainder `R_q(x) = ∑_{n ≤ x} λ(n) (1/n - 1/x) - log x / φ(q) - c_q`,
  where `λ(n) = Λ(n) (1 - (n/d))` for `n ≡ 1` mod `q` and `0` otherwise, and `c_q` is a constant.
* `entireL ψ`: the entire function `L(s, ψ)`, times `s - 1` if `ψ` is principal.
* `quadTwist ψ d`: the product of `ψ` and the Legendre symbol `(·/d)`.
* `IsPolar E r`: the transform `∫₀^∞ E(v) e^{(1-s)v} dv` continues meromorphically, with at most
  simple poles in `re s > 0` and residues `r`.

## Relation to the literature

The hypotheses concern only the remainders, for all primes `d` of the class, and not the real zeros
of the `L(s, ψ)`. In the literature: a one-sided bound for a weighted sum over primes `≡ 1` modulo
`q` gives a zero-free half-plane if there are no real zeros. Related work: M. Suzuki, On variants of
Chebyshev's conjecture, arXiv 2411.07436, 2024; Montgomery–Vaughan, Multiplicative Number Theory I,
§15.1–15.2, 2007; Landau, Über einen Satz von Tschebyschef, 1905.


### `New.LFunction_ne_zero_of_primeRemainder_le`

 **One-sided criterion.** Let `q₀` be a positive multiple of `8`, let `d₀ ≡ 7` mod `8` be prime
to `q₀`, and let `β > 1/2`. Suppose that for each prime `d ≡ d₀` mod `q₀` the remainder
`primeRemainder d q₀ x = ∑_{n ≤ x} λ(n) (1/n - 1/x) - log x / φ(q₀) - c` is at most `x ^ (β - 1)`
for all large `x`; here `λ(n) = Λ(n) (1 - (n/d))` for `n ≡ 1` mod `q₀` and `0` otherwise, and `c` is
the constant for which the remainder tends to `0`. Then `L(ρ, ψ) ≠ 0` for every character `ψ` modulo
`q₀` and every `ρ ≠ 1` with `re ρ > β`. 
