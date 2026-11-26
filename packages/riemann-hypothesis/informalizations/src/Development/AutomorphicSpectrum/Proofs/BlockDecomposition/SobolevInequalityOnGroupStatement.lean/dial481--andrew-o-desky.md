---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SobolevInequalityOnGroupStatement.lean",
  "declarations": [
    "GlobalTheory.T.sobolev_inequality_on_group"
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

## A local Sobolev inequality on the complex general linear group

[Theorem REP.1501](https://andrewodesky.com/rh/lean/GlobalTheory.T.sobolev_inequality_on_group/)

For $n\ge0$ put $G=\mathrm{GL}_n(\mathbb C)$ and $$\ell(g)=\log\!\left(1+\sum_{a,b}(|g_{ab}|^2+|(g^{-1})_{ab}|^2)\right).$$ For a real tangent matrix $X$ define $R_Xf(g)=df_g(gX)$. Let $\mathcal B=\{E_{ab},iE_{ab}\}$ be the real matrix-unit basis, and, for a finite word $w=(X_1,\ldots,X_j)$ in $\mathcal B$, let $R_w=R_{X_1}\cdots R_{X_j}$, with $R_\varnothing$ the identity.

For every Borel Haar measure $\mu$ on $G$, there are a finite set $S$ of such words and real constants $r,C$ such that, for every complex Hilbert space $V$, every $V$-valued function on $M_n(\mathbb C)$ smooth on $G$, and every $x\in G$, $$\|f(x)\|^2\le C\sum_{w\in S}\int_{\ell(y)\le r}\|R_wf(xy)\|^2\,d\mu(y).$$
