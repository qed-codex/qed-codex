---
{
  "module": "src/Formalism/ThetaSupremumBounds/GaussianShiftBounds/FockJet.lean",
  "declarations": [
    "Formalism.DimensionVariation.gaussianCoeffIntegral"
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

## Gaussian recovery of Taylor coefficients

[Theorem THETA.0112](https://andrewodesky.com/rh/lean/Formalism.DimensionVariation.gaussianCoeffIntegral/)

Let $F:\mathbb C^N\to\mathbb C$ be continuous and have a power-series expansion $F(z)=\sum_{\alpha\in\mathbb N^N}c_\alpha z^\alpha$ converging at every $z$. Suppose $|F(z)|\le S e^{\|z\|^2/2}$ for some real $S$. For every multi-index $\alpha$, the integrand below is integrable and $$\int_{\mathbb C^N}F(z)\overline z^{\,\alpha}e^{-\|z\|^2}\,dz=\pi^N\alpha!c_\alpha,$$ where $dz$ is ordinary Lebesgue measure, $\|z\|^2=\sum_j|z_j|^2$ and $\alpha!=\prod_j\alpha_j!$.
