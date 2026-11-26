---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/HermDefON.lean",
  "declarations": [
    "posDefCongruentOne"
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

## Congruence of a positive definite Hermitian matrix to the identity

[Theorem ALG.0893](https://andrewodesky.com/rh/lean/posDefCongruentOne/)

For every $n\ge0$ and every positive definite Hermitian matrix $G\in\operatorname{Mat}_n(\mathbb C)$, there is $Y\in\operatorname{Mat}_n(\mathbb C)$ such that $$\det Y\ne0,\qquad Y^*GY=I_n.$$
