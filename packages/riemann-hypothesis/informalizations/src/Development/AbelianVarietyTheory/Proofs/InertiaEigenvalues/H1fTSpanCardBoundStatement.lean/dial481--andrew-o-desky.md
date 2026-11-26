---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/H1fTSpanCardBoundStatement.lean",
  "declarations": [
    "GlobalTheory.T.h1fT_span_card_bound"
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

## A bound for generators of integral finite local cohomology

[Theorem PHT.0643](https://andrewodesky.com/rh/lean/GlobalTheory.T.h1fT_span_card_bound/)

Fix a prime $\ell$ and the source's compatible local period and $A_{\inf}$ data. Let $K\subseteq\overline{\mathbb Q}_\ell$ be finite over $\mathbb Q_\ell$, let $L$ be a finite extension of $\mathbb Q_\ell$, and let $O\subseteq L$ be a discrete valuation domain with fraction field $L$. Give $L$ its finite-dimensional $\mathbb Q_\ell$-module topology, and assume it is a topological ring and $O$ is open in $L$. Let $T$ be an $O$-lattice in a finite-dimensional continuous $L$-linear representation $V$ of $G_K$, with the compatible scalar structures and module topologies. Assume $V$ is de Rham.

There is a finite subset $S\subseteq H^1(G_K,T)$ such that $$O S=H_f^1(K,T),\qquad |S|+\dim_L V^{G_K}\le\dim_L H_f^1(K,V)+\dim_L V.$$
