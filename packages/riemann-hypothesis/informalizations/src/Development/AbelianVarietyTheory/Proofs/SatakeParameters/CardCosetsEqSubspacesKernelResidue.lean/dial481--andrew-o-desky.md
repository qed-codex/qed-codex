---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/CardCosetsEqSubspacesKernelResidue.lean",
  "declarations": [
    "GlobalTheory.SplitHecke.Cosets.card_cosets"
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

## Hecke cosets counted by subspaces of a residue kernel

[Theorem ALG.1014](https://andrewodesky.com/rh/lean/GlobalTheory.SplitHecke.Cosets.card_cosets/)

Let $O$ be a discrete valuation ring with fraction field $K$, uniformizer $\pi$, and residue field $k$. Let $0\le j\le n$, $m\ge0$, and $\alpha\in\operatorname{GL}_n(K)$ satisfy $$\alpha\in M_n(O),\qquad\pi\alpha^{-1}\in M_n(O),\qquad\det\alpha=\pi^ju\quad(u\in O^\times).$$ Let $\{\rho_\gamma:\gamma\in R\}$ be a finite, uniquely indexed set of representatives for the right $\operatorname{GL}_n(O)$-cosets in $\operatorname{GL}_n(O)\alpha\operatorname{GL}_n(O)$. For $z\in M_{m,n}(O)$, $$\operatorname{card}_0\{\gamma\in R:\pi^{-1}z\rho_\gamma\in M_{m,n}(O)\} =\operatorname{card}_0\{W\subseteq\ker(\bar z:k^n\to k^m):W\text{ a }k\text{-subspace},\ \dim_kW+j=n\}.$$
