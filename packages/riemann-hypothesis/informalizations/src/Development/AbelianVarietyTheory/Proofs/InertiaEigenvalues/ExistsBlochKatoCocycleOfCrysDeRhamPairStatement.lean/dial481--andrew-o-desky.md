---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBlochKatoCocycleOfCrysDeRhamPairStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_blochKato_cocycle_of_crys_deRham_pair"
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

## A finite local cocycle from crystalline and de Rham vectors

[Theorem PHT.1375](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_blochKato_cocycle_of_crys_deRham_pair/)

Let $\ell$ be prime and $K/\mathbb Q_\ell$ finite. Let $L/\mathbb Q_\ell$ be a finite coefficient extension with its vector-space topology, and let $\mathcal O\subset L$ be an open discrete valuation ring with fraction field $L$. Fix local crystalline, de Rham, and integral period data identified with Fontaine's rings as in ([An invariant crystalline period matrix for an unramified representation](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)). Let $V$ be a finite-dimensional continuous $L$-representation of $G_K$ with compatible $\mathcal O$- and $\mathbb Q_\ell$-module structures.

For every $d_1\in D_{\mathrm{cris}}(V)$ and $d_2\in D_{\mathrm{dR}}(V)$ there are $$x\in V\otimes_{\mathbb Q_\ell}B_{\mathrm{cris}},\qquad y\in\mathrm{Fil}^0(V\otimes_{\mathbb Q_\ell}B_{\mathrm{dR}}),$$ and a continuous cocycle $c:G_K\to V$ which becomes a coboundary after extension to $B_{\mathrm{cris}}$, such that $$(1-\varphi)x=d_1,\qquad\iota(x)-y=d_2,\qquad c(g)\otimes1=gx-x\quad(g\in G_K).$$ Here $\iota$ is the crystalline-to-de Rham inclusion and $\varphi$ acts on the crystalline period factor.
