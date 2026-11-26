---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryApproximation/EigenvalueAvoidance.lean",
  "declarations": [
    "PI.UnitaryApproxFinWork.eigenvalue_avoidance"
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

## A norm-one scalar avoiding finitely many local eigenvalues

[Theorem ANT.0779](https://andrewodesky.com/rh/lean/PI.UnitaryApproxFinWork.eigenvalue_avoidance/)

Let $E/F$ be number fields and let $\sigma\in\operatorname{Aut}_F(E)$ satisfy $\sigma^2=1$ and $\sigma\ne1$. Let $I$ be finite, let $T$ be a finite set of finite places of $F$, and for each $v\in T$ choose $$g_v\in M_I(E\otimes_F F_v).$$ There exists $\mu\in E$ with $\sigma(\mu)\mu=1$ such that $$\det(1+\mu g_v)\in(E\otimes_F F_v)^\times\qquad(v\in T).$$
