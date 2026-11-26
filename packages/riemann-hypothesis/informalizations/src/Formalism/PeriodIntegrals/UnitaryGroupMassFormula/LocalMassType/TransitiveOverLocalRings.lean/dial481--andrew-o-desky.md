---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalMassType/TransitiveOverLocalRings.lean",
  "declarations": [
    "PI.LocMassTypW.transitiveOverLocalRings"
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

## Transitivity for split matrix pairs over a local ring

[Theorem ALG.1021](https://andrewodesky.com/rh/lean/PI.LocMassTypW.transitiveOverLocalRings/)

Let $O$ be a commutative local ring and let $A_0,A,B_0,B\in M_{n,m}(O)$, with $n,m\ge0$. Assume each of the four matrices has a left inverse over $O$ and $$A_0^tB_0=A^tB.$$ There is $k\in\operatorname{GL}_n(O)$ such that $$kA_0=A,\qquad k^tB=B_0.$$
