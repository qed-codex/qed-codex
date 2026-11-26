---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalMassType/SaturatedSplitLattice.lean",
  "declarations": [
    "PI.LocMassTypW.saturated_split_lattice"
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

## An integral left inverse from an integrality condition

[Theorem ALG.0983](https://andrewodesky.com/rh/lean/PI.LocMassTypW.saturated_split_lattice/)

Let $F$ be a number field, $v$ a finite place, $K=F_v$ its completion, and $O=\mathcal O_{F_v}$. Let $A\in M_{n\times m}(O)$, where $m,n\ge0$. Suppose $$t\in K^m,\quad At\in O^n\quad\Longrightarrow\quad t\in O^m.$$ Then there is $L\in M_{m\times n}(O)$ with $LA=I_m$.
