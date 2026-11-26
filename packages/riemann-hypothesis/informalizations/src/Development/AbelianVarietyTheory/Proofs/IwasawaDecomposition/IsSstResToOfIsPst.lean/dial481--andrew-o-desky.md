---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/IsSstResToOfIsPst.lean",
  "declarations": [
    "GlobalTheory.PstSst.isSst_resTo_of_isPst"
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

## Potentially semistable periods become semistable over every large enough extension

[Theorem PHT.0284](https://andrewodesky.com/rh/lean/GlobalTheory.PstSst.isSst_resTo_of_isPst/)

Let $\ell$ be prime. For this prime, choose the abstract local period data in ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)), and use its semistable period ring $B_{\mathrm{st}}$ and potentially semistable condition.

Let $K,L\subseteq\overline{\mathbb Q}_\ell$ be finite extensions of $\mathbb Q_\ell$, put $G_K=\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)$, and let $V$ be a finite-dimensional $L$-vector space with an $L$-linear $G_K$-action. If $V$ is potentially semistable, there is a finite extension $K_1/K$ inside $\overline{\mathbb Q}_\ell$ such that, for every finite $K'/K$ containing $K_1$, the restricted representation on $V$ is semistable.
