---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsSemistableOfInvertiblePeriodMatrixSemistableRi.lean",
  "declarations": [
    "GlobalTheory.PMon.isSst_of_periodMatrix"
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

## Semistability from an invertible period matrix

[Theorem PHT.1591](https://andrewodesky.com/rh/lean/GlobalTheory.PMon.isSst_of_periodMatrix/)

Let $\ell$ be prime. For this prime, choose data satisfying Hypothesis (local period data) in ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)), and use its semistable ring $B_{\mathrm{st}}$ and Galois action.

Let $K\subseteq\overline{\mathbb Q}_\ell$ be a finite extension of $\mathbb Q_\ell$, put $G_K=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)$, and write $K_0$ for the maximal unramified subfield of $K$. Let $V$ be a $\mathbb Q_\ell$-vector space with a finite basis $b$, and let $\rho:G_K\to\operatorname{GL}(V)$ be a representation. If there is $Q\in\operatorname{GL}_n(B_{\mathrm{st}})$, $n=\dim_{\mathbb Q_\ell}V$, such that $$[\rho(g)]_b\,g(Q)=Q\qquad(g\in G_K),$$ then $$\dim_{\mathbb Q_\ell}(V\otimes_{\mathbb Q_\ell}B_{\mathrm{st}})^{G_K}=[K_0:\mathbb Q_\ell]\dim_{\mathbb Q_\ell}V.$$
