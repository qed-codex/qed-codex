---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/PowerSumTraces/PowIndep.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.C.powIndep"
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

## Eventual vanishing of power sums determines multiplicities

[Theorem ALG.0514](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.C.powIndep/)

Let $I$ be finite, let $c_i\in\mathbb C$, and let $Z_i$ be finite multisets of nonzero complex numbers. Suppose $$\sum_{i\in I}c_i\sum_{z\in Z_i}z^m=0$$ for every sufficiently large integer $m\ge0$, with multiset repetitions counted. Then for every $\zeta\in\mathbb C$, $$\sum_{i\in I}c_i\,\operatorname{mult}_{Z_i}(\zeta)=0.$$
