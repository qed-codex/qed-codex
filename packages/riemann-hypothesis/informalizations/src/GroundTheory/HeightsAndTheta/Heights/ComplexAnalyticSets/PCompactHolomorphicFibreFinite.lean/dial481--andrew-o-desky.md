---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PCompactHolomorphicFibreFinite.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.IndefiniteRowSideFullHecke.ComplexSets.CompactHolomorphicFibreFinite.proof"
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

## Compact fibres of holomorphic maps are finite

[Theorem AG.1609](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.ComplexSets.CompactHolomorphicFibreFinite.proof/)

Assume the following analytic curve principle in every finite dimension: if $U\subseteq\mathbb C^k$ is open, $f:U\to\mathbb C^m$ is holomorphic, and $p\in U$ is an accumulation point of $f^{-1}(f(p))$, there are $r>0$ and an injective holomorphic map $\gamma:\{t\in\mathbb C:|t|<r\}\to U$ with $\gamma(0)=p$ and $f\circ\gamma=f(p)$. Then, for every $k,m\ge0$, every such $U,f$, and every $y\in\mathbb C^m$, $$f^{-1}(y)\text{ compact in }\mathbb C^k\quad\Longrightarrow\quad f^{-1}(y)\text{ finite}.$$
