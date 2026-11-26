---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/IdeleGenerators/HolomorphicIrreducibility/FinCoef.lean",
  "declarations": [
    "UpperTheory.V.Sd.finCoef"
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

## A finite coefficient field for a compact group representation

[Theorem PHT.1284](https://andrewodesky.com/rh/lean/UpperTheory.V.Sd.finCoef/)

Let $\ell$ be prime, let $\overline{\mathbb Q}_\ell$ be a fixed algebraic closure with its $\ell$-adic topology, and let $\Gamma$ be a compact Hausdorff topological group. For every $n\ge0$ and continuous homomorphism $$r:\Gamma\longrightarrow\mathrm{GL}_n(\overline{\mathbb Q}_\ell),$$ there is an intermediate field $E$, finite over $\mathbb Q_\ell$, such that $$r(g)_{ij}\in E\qquad(g\in\Gamma,\ 1\le i,j\le n).$$
