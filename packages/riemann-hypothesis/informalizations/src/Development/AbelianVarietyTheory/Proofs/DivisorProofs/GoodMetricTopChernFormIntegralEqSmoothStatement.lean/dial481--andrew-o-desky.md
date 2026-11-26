---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/GoodMetricTopChernFormIntegralEqSmoothStatement.lean",
  "declarations": [
    "GlobalTheory.T.goodMetric_topChernForm_integral_eq_smooth"
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

## Chern integrals for a good metric and a smooth metric

[Theorem AG.1652](https://andrewodesky.com/rh/lean/GlobalTheory.T.goodMetric_topChernForm_integral_eq_smooth/)

Use ([Rational frame systems and flag refinements](https://andrewodesky.com/rh/lean/GlobalTheory.FlagBundle.Fr/)) and ([Good Hermitian metrics and signed Chern integrals](https://andrewodesky.com/rh/lean/GlobalTheory.GoodMetric.IsMetricOn/)). Let $F$ be a field with an embedding $\sigma:F\hookrightarrow\mathbb C$, let $X/F$ be smooth, geometrically integral and projective of dimension $d\in\mathbb N$, and let $E$ be a rational frame system of type $0$ for a single bundle of rank $m\in\mathbb N$. Let $O\subseteq X$ be open.

Let $H$ be a good smooth positive Hermitian metric on $E$ over $O(\mathbb C)$, and let $H_0$ be a smooth positive Hermitian metric on $E$ over all of $X_\sigma(\mathbb C)$. If $c_d(E,H_0)$ has Chern integral $t\in\mathbb R$ on $X_\sigma(\mathbb C)$ in the finite signed-measure sense, then $c_d(E,H)$ has Chern integral $t$ on $O(\mathbb C)$: $$\int_{O(\mathbb C)}c_d(E,H)=t=\int_{X_\sigma(\mathbb C)}c_d(E,H_0).$$
