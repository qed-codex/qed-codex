---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/AdelicIndexEquality/GLDelta.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.AdIndexEq.gl_character"
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

## Positive rational characters trivial on scalars are trivial

[Theorem ALG.0771](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.AdIndexEq.gl_character/)

Let $k$ be a field of characteristic zero and $n\ge0$. Let $\chi:\operatorname{GL}_n(k)\to\mathbb Q$ be a multiplicative monoid homomorphism such that $\chi(g)>0$ for every $g$. If $$\chi(a\,1_n)=1\qquad(a\in k^\times),$$ then $\chi(g)=1$ for every $g\in\operatorname{GL}_n(k)$.
