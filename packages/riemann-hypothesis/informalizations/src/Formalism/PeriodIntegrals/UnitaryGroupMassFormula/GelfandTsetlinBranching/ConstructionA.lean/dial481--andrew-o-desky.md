---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinBranching/ConstructionA.lean",
  "declarations": [
    "PI.WGB.fixed_line_exists"
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

## Uniqueness of a highest-weight line in a general linear restriction

[Theorem REP.1076](https://andrewodesky.com/rh/lean/PI.WGB.fixed_line_exists/)

Let $N=n+1$, and let $\lambda_1\ge\cdots\ge\lambda_N$ and $\mu_1\ge\cdots\ge\mu_n$ be integer dominant weights. In the complex dual Weyl representation $V_\lambda$ of $\operatorname{GL}_N$, restrict along $g\mapsto\operatorname{diag}(g,1)$. Suppose $f_1,f_2\in V_\lambda$ are fixed by the upper unitriangular subgroup of $\operatorname{GL}_n$ and satisfy $$\operatorname{diag}(t_1,\ldots,t_n,1)f_j=\left(\prod_{i=1}^n t_i^{\mu_i}\right)f_j\qquad(t_i\in\mathbb C^\times),$$ with $f_2\ne0$. Then $f_1=cf_2$ for some $c\in\mathbb C$, and $$\lambda_i\ge\mu_i\ge\lambda_{i+1}\qquad(1\le i\le n).$$
