---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/ExistsIntegralWeightProjections.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.exists_integral_weight_projection",
    "Formalism.MainNotions.G.GLWeightTheory.exists_integral_weight_projections"
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

## Integral operators separating finitely many weights

[Theorem REP.0811](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.exists_integral_weight_projection/)

Let $O$ be a discrete valuation ring with fraction field $K$ of characteristic zero, let $n\in\mathbb N$, and let $V$ be a $K$-vector space with the induced $O$-module structure. Let $E_{ab}\in\operatorname{End}_K(V)$ for $1\le a,b\le n$, without further relations assumed. Put $$V_\nu=\{x:E_{aa}x=\nu_a x\text{ for every }a\}\quad(\nu\in\mathbb Z^n).$$ For every $\mu\in\mathbb Z^n$ and finite $F\subseteq\mathbb Z^n$, there are $P\in\operatorname{End}_K(V)$ and $g:\mathbb Z^n\to\mathbb Z$ such that $$g(\mu)=1,\qquad g(\nu)=0\ (\nu\in F\setminus\{\mu\}),\qquad P|_{V_\nu}=g(\nu)\operatorname{id}_{V_\nu}\ (\nu\in\mathbb Z^n).$$ Moreover, $P(M)\subseteq M$ for every $O$-submodule $M\subseteq V$ stable under the operators specified below.

For each fixed finite $F$, the pairs $(P_\mu,g_\mu)$ satisfying these conditions can be chosen simultaneously for every $\mu\in\mathbb Z^n$.
