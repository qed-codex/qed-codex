---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MapWithDensityEqOfScale.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.QuotVan.haarNM"
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

## Haar measure in semidirect product coordinates

[Theorem ALG.1056](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.QuotVan.haarNM/)

Let $Q$ be a locally compact, second countable Hausdorff topological group with its Borel measurable structure. Let $N,M\subseteq Q$ be closed subgroups, with $N$ normal, $N\cap M=\{1\}$, and $Q=NM$. For Haar measures $\nu_Q,\nu_N,\nu_M$, there is a measurable function $\delta:M\to[0,\infty)$ such that $$\nu_Q=\Phi_*\bigl(\delta(m)\,d\nu_N(n)\,d\nu_M(m)\bigr),\qquad \Phi(n,m)=nm.$$
