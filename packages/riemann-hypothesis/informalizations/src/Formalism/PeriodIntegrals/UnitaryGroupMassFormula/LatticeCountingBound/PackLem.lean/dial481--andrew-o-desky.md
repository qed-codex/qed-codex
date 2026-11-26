---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeCountingBound/PackLem.lean",
  "declarations": [
    "PI.UnitaryGroupMassFormula.LCG.lattice_packLem"
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

## Packing bound for products of complex matrix balls

[Theorem ALG.0944](https://andrewodesky.com/rh/lean/PI.UnitaryGroupMassFormula.LCG.lattice_packLem/)

Let $I$ be a finite set, $N\ge0$, and $R_v\ge0$, $\rho_v>0$ for $v\in I$. For a complex matrix $A$, write $\|A\|_{\mathrm{HS}}=(\sum_{i,j}|A_{ij}|^2)^{1/2}$. Let $T$ be a finite subset of $\prod_{v\in I}M_N(\mathbb C)$ such that $$\|p_v\|_{\mathrm{HS}}\le R_v\quad(p\in T,\ v\in I),$$ and for any distinct $p,q\in T$ there is $v\in I$ with $\|p_v-q_v\|_{\mathrm{HS}}\ge\rho_v$. Then $$|T|\le\prod_{v\in I}\left(\frac{2R_v+\rho_v}{\rho_v}\right)^{2N^2}.$$
