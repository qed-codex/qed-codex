---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/InvHodgeMetricGramMumfordGoodGrowthBoundaryChartStatement.lean",
  "declarations": [
    "GlobalTheory.T.inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart"
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

## Growth of the inverse metric in a logarithmic period chart

[Theorem ARAK.0517](https://andrewodesky.com/rh/lean/GlobalTheory.T.inv_hodgeMetricGram_mumfordGoodGrowth_boundaryChart/)

Let $0\le a\le n$ and $0\le r\le g$. Let $\tau_0$ be a symmetric holomorphic $g\times g$ matrix on the unit polydisc in $\mathbb C^n$. Let $B_1,\ldots,B_a$ be positive semidefinite integral matrices, all zero outside their upper left $r\times r$ blocks. Suppose the upper left block of $\sum_{j=1}^a B_j$ is positive definite and the lower right $(g-r)\times(g-r)$ block of $\Im\tau_0(z)$ is positive definite throughout the unit polydisc. Put $$Y(z)=\Im\tau_0(z)-\frac1{2\pi}\sum_{j=1}^a\log|z_j|\,B_j.$$ There are $0<\rho\le1/2$, $c\in\mathbb R$, and $N\in\mathbb N$ such that, on $\{|z_j|<\rho\ (1\le j\le n),\ z_1\cdots z_a\ne0\}$, $Y$ is positive definite, every entry of $G=Y^{-1}$ is twice continuously real differentiable, and the bounds in the conventions hold.
