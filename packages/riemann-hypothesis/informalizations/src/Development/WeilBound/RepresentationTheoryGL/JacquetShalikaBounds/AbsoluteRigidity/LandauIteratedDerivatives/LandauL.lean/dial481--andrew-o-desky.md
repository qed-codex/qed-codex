---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/LandauIteratedDerivatives/LandauL.lean",
  "declarations": [
    "PositivityTheory.RgJS.landauL"
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

## Continuation of an exponential forces convergence of a positive series

[Theorem ANT.1623](https://andrewodesky.com/rh/lean/PositivityTheory.RgJS.landauL/)

Let $I$ be any set, $c_i,\lambda_i\ge0$, $\sigma_0,\sigma_1\in\mathbb R$, and $F:\mathbb C\to\mathbb C$. Assume $F$ is complex analytic at each real $\sigma>\sigma_0$. Suppose that for every real $\sigma>\sigma_1$ the family $(c_i e^{-\lambda_i\sigma})_{i\in I}$ is summable and $$F(\sigma)=\exp\!\left(\sum_{i\in I}c_i e^{-\lambda_i\sigma}\right).$$ Then $(c_i e^{-\lambda_i\sigma})_{i\in I}$ is summable for every real $\sigma>\sigma_0$.
