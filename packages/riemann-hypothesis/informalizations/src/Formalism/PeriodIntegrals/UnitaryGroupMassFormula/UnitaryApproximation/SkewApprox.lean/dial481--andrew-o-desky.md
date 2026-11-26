---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryApproximation/SkewApprox.lean",
  "declarations": [
    "PI.UnitaryApproxFinWork.skew_approx"
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

## Simultaneous approximation of skew-Hermitian matrices

[Theorem ALG.0667](https://andrewodesky.com/rh/lean/PI.UnitaryApproxFinWork.skew_approx/)

Assume the scalar approximation property below. Let $E/F$ be an extension of number fields, let $\sigma:E\to E$ be an $F$-algebra involution, and let $I$ be a finite index set. Fix a finite set $T$ of finite primes of $F$, local matrices $Y_v\in M_I(E\otimes_F F_v)$, and $0\ne\delta\in\mathcal O_F$. If $Y_v^{\sigma,t}=-Y_v$ for every $v\in T$, there is $Y\in M_I(E)$ such that $$Y^{\sigma,t}=-Y,\qquad Y-Y_v\in\delta M_I(S_v)\quad(v\in T).$$
