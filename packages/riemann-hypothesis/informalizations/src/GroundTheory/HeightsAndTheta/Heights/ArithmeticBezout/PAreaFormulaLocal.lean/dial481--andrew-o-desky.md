---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/PAreaFormulaLocal.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.AreaFormulaLocal.proof"
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

## The local area formula at an immersion point

[Theorem AG.0520](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.AreaFormulaLocal.proof/)

Let $E,F$ be finite-dimensional real inner product spaces with their Borel structures, $k=\dim_{\mathbb R}E$, $U\subseteq E$ open, and $f:E\to F$ continuously differentiable on $U$. If $x_0\in U$ and $Df(x_0)$ is injective, there is an open neighborhood $V$ of $x_0$ contained in $U$ such that, for every measurable $B\subseteq V$, $$\mathcal H^k(f(B))=\int_B J_k(Df(x))\,d\mathcal H^k(x).$$
