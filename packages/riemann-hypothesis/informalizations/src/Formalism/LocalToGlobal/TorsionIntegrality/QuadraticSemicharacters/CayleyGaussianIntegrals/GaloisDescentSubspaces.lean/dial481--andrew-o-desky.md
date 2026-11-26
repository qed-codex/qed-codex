---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/GaloisDescentSubspaces.lean",
  "declarations": [
    "Formalism.L2.Th1.H.latticeGaussSummable"
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

## A summable Gaussian majorant uniform on bounded sets

[Theorem ALG.0902](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.latticeGaussSummable/)

Let $V$ be a finite-dimensional normed complex vector space and $\Lambda\subseteq V$ a discrete additive subgroup spanning $V$ over $\mathbb R$. For every $c>0$ and $r\in\mathbb R$, there is a summable family $u:\Lambda\to\mathbb R$ such that $$e^{-c\|x-z\|^2}\le u(x)\qquad(x\in\Lambda,\ z\in V,\ \|z\|\le r).$$
