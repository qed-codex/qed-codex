---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/IrreducibleSubquotientParabolicProductTwoFiniteLStatement.lean",
  "declarations": [
    "GlobalTheory.T.irreducibleSubquotient_parabolicProductTwo_finiteLength"
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

## Irreducible factors beneath an induced subquotient

[Theorem REP.0765](https://andrewodesky.com/rh/lean/GlobalTheory.T.irreducibleSubquotient_parabolicProductTwo_finiteLength/)

Assume the universal representation-theoretic package stated below. Let $k$ be a nonarchimedean local field, let $r,t\ge0$, and let $\rho_1,\rho_2$ be smooth complex representations of $\operatorname{GL}_r(k),\operatorname{GL}_t(k)$ of finite length. Write $\rho_1\times\rho_2$ for normalized parabolic induction from the standard Levi subgroup.

If an irreducible smooth representation $\pi$ of $\operatorname{GL}_{r+t}(k)$ is a subquotient of $\rho_1\times\rho_2$, then there are irreducible smooth representations $\pi_1,\pi_2$ such that $$\pi_1\text{ is a subquotient of }\rho_1,\qquad \pi_2\text{ is a subquotient of }\rho_2,\qquad \pi\text{ is a subquotient of }\pi_1\times\pi_2.$$
