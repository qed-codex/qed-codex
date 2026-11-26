---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/HybridLargeSieve.lean",
  "declarations": [
    "GlobalTheory.HybridLargeSieve.hybrid_large_sieve",
    "GlobalTheory.HybridLargeSieve.window"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A large-sieve bound on a multiplicative interval

[Theorem ANT.0453](https://andrewodesky.com/rh/lean/GlobalTheory.HybridLargeSieve.window/)

Let $Q,N\in\mathbb N$, $Q\ge1$, $T\ge1$, $x>0$, and let $(a_n)_{n\ge0}$ be complex numbers. Put $$I=\{n\in\mathbb N:1\le n\le N,\ x<n\le xe^{1/T}\}.$$ Then $$\sum_{q=1}^{Q}\ \sum_{\substack{\chi\bmod q\\\chi\text{ primitive}}}\left|\sum_{n\in I}a_n\chi(n)\right|^2 \le\sum_{n\in I}\left(Q^2+8\left(\frac{2n}{T}+1\right)\right)|a_n|^2.$$ Characters are extended by zero on integers not coprime to their modulus.

## A hybrid large sieve for primitive characters

[Theorem ANT.0601](https://andrewodesky.com/rh/lean/GlobalTheory.HybridLargeSieve.hybrid_large_sieve/)

There is an absolute constant $C>0$ such that, for all integers $Q\ge1$ and $N\ge0$, every $a:\mathbb N\to\mathbb C$, and every real $T\ge1$, $$\sum_{q=1}^{Q}\ \sum_{\substack{\chi\bmod q\\\chi\ \mathrm{primitive}}}\int_{-T}^{T}\left|\sum_{n=1}^{N}a(n)\chi(n)n^{-it}\right|^2\,dt \le C\sum_{n=1}^{N}(Q^2T+n)|a(n)|^2.$$
