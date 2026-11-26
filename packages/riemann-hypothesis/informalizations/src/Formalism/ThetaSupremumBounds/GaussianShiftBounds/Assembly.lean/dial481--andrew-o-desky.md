---
{
  "module": "src/Formalism/ThetaSupremumBounds/GaussianShiftBounds/Assembly.lean",
  "declarations": [
    "Formalism.DimensionVariation.size_at_embedding"
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

## Logarithmic conversion of a kernel product bound

[Theorem THETA.0126](https://andrewodesky.com/rh/s/kernel-norm.html)

Let $\Sigma$ be finite, let $r,g_0\ge0$ be integers, and let $\nu_{\tau,i}\in\mathbb R$, $n_\tau\in\mathbb N$, and $\Omega_\tau>0$ for $\tau\in\Sigma$ and $1\le i\le r$. Put $\phi(y)=y\log y-y$, with $\log0=0$ and the real logarithm interpreted as $\log|y|$ for $y<0$. Let $K^2,c,M^2,T^2,h$ be positive real numbers. Assume the product bound $$K^2\le h c^2M^2T^2\prod_{\tau\in\Sigma}\left[\Omega_\tau^{-n_\tau}\,e\,(2n_\tau+2)^{2g_0}\exp\!\left(\sum_{i=1}^r\phi(\nu_{\tau,i})\right)\right].$$ Then $$\log K^2\le\sum_{\tau\in\Sigma}\left(\sum_{i=1}^r\phi(\nu_{\tau,i})-n_\tau\log\Omega_\tau\right)+\log T^2+\log M^2+2\log c+\sum_{\tau\in\Sigma}\bigl[1+2g_0\log(2n_\tau+2)\bigr]+\log h.$$ No relation $n_\tau=\sum_i\nu_{\tau,i}$ is assumed in this conversion.
