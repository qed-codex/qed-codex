---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TorusSplitting/NearestPlaneRounding.lean",
  "declarations": [
    "GlobalTheory.nearestPlane_rounding"
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

## Rounding in a lattice with a squared-distance bound

[Theorem ALG.0932](https://andrewodesky.com/rh/lean/GlobalTheory.nearestPlane_rounding/)

Let $V$ be a real inner product space, and let $v_1,\ldots,v_n\in V$ be linearly independent, where $n\ge0$. For every $x\in\operatorname{span}_{\mathbb R}\{v_1,\ldots,v_n\}$, there are integers $c_1,\ldots,c_n$ such that $$\left\|x-\sum_{i=1}^n c_iv_i\right\|^2\le\frac14\sum_{i=1}^n\|v_i\|^2.$$
