---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ConjugateNormBound/MemIntegerRingIffNormLeOne.lean",
  "declarations": [
    "PI.BeConjNormW.inverse_integral_padic"
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

## Integrality of a p-adic formal inverse

[Theorem PHT.0442](https://andrewodesky.com/rh/lean/PI.BeConjNormW.inverse_integral_padic/)

Let $p$ be prime and let $f,g\in\mathbb C_p[[T]]$ have zero constant term. Suppose the linear coefficient of $f$ has absolute value $1$, every coefficient of $f$ has absolute value at most $1$, and $$g(f(T))=T.$$ Then every coefficient of $g$ has absolute value at most $1$.
