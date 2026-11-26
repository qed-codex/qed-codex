---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/UnitaryEighthOf.lean",
  "declarations": [
    "Formalism.L2.Th1.H.cayleyDet"
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

## Conjugation of the determinant of a unitary difference

[Theorem ALG.1040](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.cayleyDet/)

Let $V$ be a finite-dimensional complex vector space, $H$ a positive definite Hermitian form, and $\delta\in\operatorname{GL}(V)$ an $H$-isometry. Suppose $A=1-\delta^{-1}$ is invertible. Then $$\overline{\det A}=(-1)^{\dim_{\mathbb C}V}\det(\delta)\det A.$$
