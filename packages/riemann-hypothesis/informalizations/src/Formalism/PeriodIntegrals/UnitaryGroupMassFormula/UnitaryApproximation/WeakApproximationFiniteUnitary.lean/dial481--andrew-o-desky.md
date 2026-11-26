---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryApproximation/WeakApproximationFiniteUnitary.lean",
  "declarations": [
    "PI.UnitaryApproxFinWork.weak_approximation_finite_unitary"
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

## Simultaneous approximation at finite places

[Theorem ANT.0807](https://andrewodesky.com/rh/lean/PI.UnitaryApproxFinWork.weak_approximation_finite_unitary/)

Let $F$ be a number field, $T$ a finite set of nonzero prime ideals of $\mathcal O_F$, and $c_v\in F_v$ for every finite place $v$ of $F$. For every nonzero $D\in\mathcal O_F$, there exists $a\in F$ such that $$c_v-a\in D\mathcal O_{F_v}\qquad(v\in T).$$
