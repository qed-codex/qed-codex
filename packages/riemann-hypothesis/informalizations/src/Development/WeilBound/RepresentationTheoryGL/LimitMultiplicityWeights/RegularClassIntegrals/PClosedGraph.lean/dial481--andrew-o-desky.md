---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/LimitMultiplicityWeights/RegularClassIntegrals/PClosedGraph.lean",
  "declarations": [
    "MainStatements.WeightKernel.closedGraph"
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

## A uniform integral bound from integrable absolute sums

[Theorem ALG.0307](https://andrewodesky.com/rh/lean/MainStatements.WeightKernel.closedGraph/)

Let $(\Omega,\mu)$ be a measure space, $I$ any set, and $u_i:\Omega\to\mathbb C$. Suppose $\{u_i(x):i\in I\}$ is bounded for each $x$. Suppose also that for every family $a=(a_i)_{i\in I}$ with $\sum_i|a_i|<\infty$, the function $$x\longmapsto\sum_i a_i u_i(x)$$ is integrable. There is $B\in\mathbb R$ such that every $u_i$ is integrable and $$\int_\Omega|u_i(x)|\,d\mu(x)\le B\qquad(i\in I).$$
