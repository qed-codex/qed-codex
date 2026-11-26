---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/LevelSubgroupProperties.lean",
  "declarations": [
    "Formalism.L2.SG.Closed.fold_L2_second"
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

## A square-integrability bound for a Poincare series

[Theorem REP.0218](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.fold_L2_second/)

Let $G$ be a second-countable locally compact Hausdorff topological group with its Borel measurable structure and left Haar measure $\mu$. Let $\Gamma\subseteq G$ be discrete, $S\subseteq\Gamma$ a subgroup, $\Omega\subseteq G$ compact with $1\in\Omega$, and $a\ge0$. Let $\Phi:G\to\mathbb C$ be measurable and left $S$-invariant, with $$|\Phi(y)|\le a\int_\Omega |\Phi(y\omega)|\,d\mu(\omega)\qquad(y\in G).$$ Choose measurable fundamental domains $F_S,F_\Gamma$ for left translation by $S,\Gamma$, and a set $D\subseteq\Gamma$ such that every $\gamma\in\Gamma$ has a unique expression $\gamma=s\delta$, $s\in S,\delta\in D$. Put $$m(x)=\sup_{y\in G}\#\{\gamma\in\Gamma:x^{-1}\gamma y\in\Omega\},\quad I=\int_{F_S}m(x)|\Phi(x)|\,d\mu(x),\quad J=\int_{F_S}|\Phi(x)|\,d\mu(x).$$ If $I<\infty$, then $P(x)=\sum_{\delta\in D}\Phi(\delta x)$ belongs to $L^2(F_\Gamma,\mu)$ and $$\int_{F_\Gamma}|P(x)|^2\,d\mu(x)\le aJI\le aI^2.$$
