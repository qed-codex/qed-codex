---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ToricGeometry/ExistsMulDotProductLeOfIsCompactThetaDomain.lean",
  "declarations": [
    "GlobalTheory.thetaMTest_and_thetaSummable"
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

## Absolute and locally uniform convergence of theta series

[Theorem THETA.1517](https://andrewodesky.com/rh/lean/GlobalTheory.thetaMTest_and_thetaSummable/)

For a finite index set $I$, real vectors $a,b\in\mathbb R^I$, $z\in\mathbb C^I$, and a complex matrix $\tau$, put $$\theta_m[a,b](z,\tau)=\exp\!\left(2\pi i\left(\tfrac12(m+a)^t\tau(m+a)+(m+a)^t(z+b)\right)\right),\qquad m\in\mathbb Z^I.$$ Let $\mathcal D$ be the set of matrices for which $\operatorname{Im}\tau+(\operatorname{Im}\tau)^t$ is positive definite; symmetry of $\tau$ is not required. For $\tau\in\mathcal D$, the series $\sum_m|\theta_m[a,b](z,\tau)|$ converges.

Fix $a$ and a compact set $K\subset\mathbb C^I\times\mathcal D$. There is a summable real family $(u_m)_{m\in\mathbb Z^I}$ such that $$|\theta_m[a,b](z,\tau)|\le u_m\qquad(b\in\mathbb R^I,\ (z,\tau)\in K,\ m\in\mathbb Z^I).$$
