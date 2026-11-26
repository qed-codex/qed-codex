---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ZetaZeroDetect.lean",
  "declarations": [
    "GlobalTheory.ZeroDetect.zeta_zero_detect"
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

## A Dirichlet polynomial detecting zeta zeros near one

[Theorem ANT.0543](https://andrewodesky.com/rh/lean/GlobalTheory.ZeroDetect.zeta_zero_detect/)

There is $Q_0\in\mathbb N$ such that for every integer $Q\ge Q_0$ and every zero $\rho$ of $\zeta$ satisfying $$1-\frac1{400}\le\Re\rho<1,\qquad Q^{1/20}\le|\Im\rho|\le Q,$$ one has $$\left|\sum_{Q^3<n\le Q^6}\left(\sum_{\substack{d\mid n\\d\le Q^3}}\mu(d)\right)n^{-\rho}\right|\ge\frac12,$$ where $\mu$ is the Möbius function.
