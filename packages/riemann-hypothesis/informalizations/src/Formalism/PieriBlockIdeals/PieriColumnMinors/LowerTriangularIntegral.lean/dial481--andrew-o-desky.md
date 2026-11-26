---
{
  "module": "src/Formalism/PieriBlockIdeals/PieriColumnMinors/LowerTriangularIntegral.lean",
  "declarations": [
    "Formalism.CohomologicalDescent.LR.lower_triangular_integral"
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

## Integral lower-triangular coefficients force all coefficients to be integral

[Theorem REP.0611](https://andrewodesky.com/rh/lean/Formalism.CohomologicalDescent.LR.lower_triangular_integral/)

Let $r,n\ge0$ be integers and let $\nu=(\nu_1,\ldots,\nu_n)\in\mathbb N^n$. Use the dual Weyl module $\nabla_\nu(\mathbb Q)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in variables $X_{as}$ with $1\le a\le r$ and $1\le s\le n$.

Let $Q\in\nabla_\nu(\mathbb Q)$. Suppose the coefficient of every monomial $\prod_{a,s}X_{as}^{m_{as}}$ with $m_{as}=0$ whenever $a<s$ is an integer. Then every coefficient of $Q$ is an integer.
