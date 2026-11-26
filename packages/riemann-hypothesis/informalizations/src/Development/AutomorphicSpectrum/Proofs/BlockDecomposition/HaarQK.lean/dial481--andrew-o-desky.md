---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HaarQK.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.QuotVan.haarQK"
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

## Haar measure from a closed subgroup and a compact subgroup

[Theorem REP.0884](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.QuotVan.haarQK/)

Let $G$ be a second countable locally compact Hausdorff topological group with a left and right invariant Haar measure $\mu$ on its Borel sets. Let $Q,K\subseteq G$ be subgroups, with $Q$ closed, $K$ compact, and $G=QK$. For Haar measures $\nu$ on $Q$ and $\kappa$ on $K$, there is a real constant $0<c<\infty$ such that $$\mu=c\,m_*(\nu\times\kappa),\qquad m(q,k)=qk.$$
