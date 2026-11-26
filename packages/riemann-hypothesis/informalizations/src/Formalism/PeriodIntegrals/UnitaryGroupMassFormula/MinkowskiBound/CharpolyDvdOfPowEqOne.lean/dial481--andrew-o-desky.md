---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/MinkowskiBound/CharpolyDvdOfPowEqOne.lean",
  "declarations": [
    "PI.Mk.traceStep"
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

## The trace of an integral matrix of prime power order

[Theorem ALG.1295](https://andrewodesky.com/rh/lean/PI.Mk.traceStep/)

Let $N,a\ge0$ be integers and $\ell$ prime. If $g\in M_N(\mathbb Z)$ satisfies $g^{\ell^a}=I_N$, then there is an integer $y\ge0$ such that $$y\le\left\lfloor\frac{N}{\ell-1}\right\rfloor,\qquad \operatorname{tr}(g)=N-\ell y,\qquad y=0\Longrightarrow g=I_N.$$
