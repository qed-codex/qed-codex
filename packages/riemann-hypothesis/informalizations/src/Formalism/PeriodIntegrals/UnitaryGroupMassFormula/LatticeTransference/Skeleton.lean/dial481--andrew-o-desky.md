---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeTransference/Skeleton.lean",
  "declarations": [
    "PI.Tr.key_of"
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

## Distance to a lattice from integral short dual pairings

[Theorem ALG.0513](https://andrewodesky.com/rh/lean/PI.Tr.key_of/)

Assume that the assertion below holds in every dimension at least two and in every dimension at most one. Then it holds in every dimension.

Let $E$ be a finite-dimensional real inner product space and $\Lambda\subset E$ a discrete subgroup spanning $E$. Write $$\Lambda^*=\{y\in E:\langle x,y\rangle\in\mathbb Z\text{ for all }x\in\Lambda\}.$$ Let $u\in E$ and $\lambda>0$. If $\langle u,y\rangle\in\mathbb Z$ for every $y\in\Lambda^*$ with $\|y\|<\lambda$, then there is $l\in\Lambda$ such that $$\|u-l\|\lambda\le\frac{\dim_{\mathbb R}E}{2}.$$
