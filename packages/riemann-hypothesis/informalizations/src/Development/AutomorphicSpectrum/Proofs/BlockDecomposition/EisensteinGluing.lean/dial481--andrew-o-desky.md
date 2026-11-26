---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/EisensteinGluing.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.PolyDenominator.exists_poly_factor"
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

## Factoring the zeros of an entire function on a compact set

[Theorem ALG.0595](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.PolyDenominator.exists_poly_factor/)

Let $A:\mathbb C\to\mathbb C$ be an entire function that is nonzero at some point, and let $Q\subset\mathbb C$ be compact. There exist a nonzero polynomial $d\in\mathbb C[X]$ and an entire function $u$ such that $$A(z)=d(z)u(z)\quad(z\in\mathbb C),\qquad u(z)\ne0\quad(z\in Q).$$
