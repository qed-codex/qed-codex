---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/WeightSpaceEqBotOutsideSupport.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.weight_projections_exist"
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

## Simultaneous projections onto integral weight spaces

[Theorem REP.1073](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.weight_projections_exist/)

Let $K$ be a field of characteristic zero, let $V$ be finite-dimensional over $K$, and let $E_{ab}\in\operatorname{End}_K(V)$ for $1\le a,b\le n$ satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ For $\mu\in\mathbb Z^n$, put $V_\mu=\{x:E_{aa}x=\mu_ax\text{ for every }a\}$, and suppose $\sum_\mu V_\mu=V$. Also assume every vector lies in a finite-dimensional subspace stable under all $E_{ab}$.

There are a finite set $S\subset\mathbb Z^n$ and operators $\pi_\mu\in\operatorname{End}_K(V)$ for every $\mu\in\mathbb Z^n$ such that $$\pi_\mu|_{V_\mu}=1,\qquad \pi_\mu|_{V_\nu}=0\ (\nu\ne\mu),\qquad \pi_\mu(V)\subseteq V_\mu,$$ $$V_\mu=0\ (\mu\notin S),\qquad \sum_{\mu\in S}\pi_\mu=1_V.$$ Each $\pi_\mu$ preserves every subspace stable under all the diagonal operators $E_{aa}$.
