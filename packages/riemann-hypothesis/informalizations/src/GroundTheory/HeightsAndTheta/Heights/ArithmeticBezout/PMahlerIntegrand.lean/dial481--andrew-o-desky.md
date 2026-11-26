---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/PMahlerIntegrand.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.MahlerIntegrand.proof"
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

## Integrability of a normalized multihomogeneous logarithm

[Theorem ARAK.0295](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.MahlerIntegrand.proof/)

Let $n,k,\delta\ge0$, $H\in\operatorname{GL}_n(\mathbb C)$, and $f$ a nonzero complex polynomial in $k$ blocks of $n$ variables, homogeneous of degree $\delta$ in each block. Set $$\|v\|_H=\left(\sum_j|(Hv)_j|^2\right)^{1/2},\qquad B_H=\{v:\|v\|_H<1\}.$$ The function $$(u_1,\ldots,u_k)\longmapsto\log\left|f\left(\frac{u_1}{\|u_1\|_H},\ldots,\frac{u_k}{\|u_k\|_H}\right)\right|$$ is Lebesgue integrable on $B_H^k$.
