---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeCountingBound/ArchIneq.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.LCG.archimedean_inequality"
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

## A determinant inequality for an operator with a prescribed kernel

[Theorem ALG.0883](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.LCG.archimedean_inequality/)

Let $n,k\ge0$, $A\in\operatorname{Mat}_n(\mathbb C)$, $C,D\in\operatorname{Mat}_{n\times k}(\mathbb C)$, and $\kappa\ge0$. Suppose $$\|Aw\|_2^2\le\kappa\|w\|_2^2\quad(w\in\mathbb C^n),\qquad \ker D^*\subseteq\ker A.$$ Then $$\operatorname{Re}\det((AC)^*(AC))\,\operatorname{Re}\det(D^*D) \le\kappa^k|\det(D^*C)|^2.$$
