---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/DiagonalMulMemCongruenceSubgroup.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.WeberRay.ncard_rayClassField_iff"
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

## Complete splitting in a ray class field

[Theorem ANT.1403](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.WeberRay.ncard_rayClassField_iff/)

Let $K$ be a number field with a chosen embedding into $\mathbb C$, let $n\ge1$, and let $K_n\subset\mathbb C$ be the ray class field for the finite modulus $n\mathcal O_K$ with trivial archimedean component. Let $\mathfrak p$ be a nonzero prime ideal of $\mathcal O_K$ with $n\notin\mathfrak p$.

The number of primes of $\mathcal O_{K_n}$ above $\mathfrak p$ equals $[K_n:K]$ if and only if there is $\pi\in\mathcal O_K$ such that $$\mathfrak p=(\pi),\qquad \pi\equiv1\pmod{n\mathcal O_K}.$$
