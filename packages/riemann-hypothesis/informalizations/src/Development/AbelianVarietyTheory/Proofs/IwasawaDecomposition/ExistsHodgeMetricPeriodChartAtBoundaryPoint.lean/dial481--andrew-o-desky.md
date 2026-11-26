---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsHodgeMetricPeriodChartAtBoundaryPoint.lean",
  "declarations": [
    "GlobalTheory.LieBase.HodgeChart.exists_hodge_period_chart"
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

## Logarithmic period coordinates for the Hodge metric at a boundary point

[Theorem AV.0072](https://andrewodesky.com/rh/lean/GlobalTheory.LieBase.HodgeChart.exists_hodge_period_chart/)

Fix the source's CM moduli, coefficient, toroidal-model, flag-compactification and eigenframe data described below, and its compatible analytic uniformization. Identify the variety's base field with the coefficient field by the specified isomorphism, and choose a compatible embedding into $\mathbb C$. Let $X$ be the resulting variety, of dimension $d$, let $X^\circ$ be its specified interior, and let $y\in X(\mathbb C)\setminus X^\circ(\mathbb C)$.

There is a holomorphic coordinate chart $z:U\to\mathbb C^d$, with $y\in U$, $z(y)=0$ and $z(U)\subset\mathbb D^d$, and an integer $0\le a\le d$ such that $$x\notin X^\circ(\mathbb C)\quad\Longleftrightarrow\quad\prod_{i=1}^az_i(x)=0\qquad(x\in U).$$ There are integers $0\le\rho\le g$, a symmetric holomorphic matrix $\tau_0:\mathbb D^d\to M_g(\mathbb C)$, and positive-semidefinite integral matrices $B_1,\ldots,B_a$ supported in the first $\rho$ rows and columns. The sum of these matrices is positive definite on that $\rho$-dimensional block, and $\operatorname{Im}\tau_0$ is positive definite on the complementary block throughout $\mathbb D^d$.

One can choose a frame matrix $A$ from the prescribed local frame family at $y$, and holomorphic matrices $$Q_\tau:\mathbb D^d\to M_{m_\tau,g}(\mathbb C),\qquad\sum_\tau m_\tau=g,$$ whose combined rows at zero are linearly independent. Put $$H(z)=\operatorname{Im}\tau_0(z)-\sum_{i=1}^a\frac{\log|z_i|}{2\pi}B_i.$$ For $x\in U\cap X^\circ(\mathbb C)$, the source's Lie-metric matrices in this frame satisfy $$G_{\tau,A}(x)=Q_\tau(z(x))H(z(x))^{-1}Q_\tau(z(x))^*,$$ and, for $\tau\ne\tau'$, $$Q_\tau(z(x))H(z(x))^{-1}Q_{\tau'}(z(x))^*=0.$$
