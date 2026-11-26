---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/OfLeaves.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.SphereMeanLinear.full"
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

## Logarithmic mean of a unit linear form

[Theorem ARAK.0534](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.SphereMeanLinear.full/)

Let $n\ge0$ and $p\in\mathbb C^n$ satisfy $\sum_j|p_j|^2=1$. Then $$\frac1{\operatorname{vol}(B)}\int_B\log\left|\sum_{j=1}^n\frac{u_j}{\|u\|}\overline{p_j}\right|\,du=-\frac12\sum_{j=1}^{n-1}\frac1j,$$ where $B=\{u\in\mathbb C^n:\|u\|<1\}$ and the measure is Euclidean Lebesgue measure.
