---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/BesselModels/HyperbolicFrameCongruentSplitHermGram.lean",
  "declarations": [
    "UpperTheory.Lit.Bur.hyperbolic_frame_congruent_splitHermGram"
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

## Putting a Hermitian frame in split coordinates

[Theorem ALG.1260](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Bur.hyperbolic_frame_congruent_splitHermGram/)

Let $m,r\ge0$, $n=2r+m+1$, and $J\in M_n(\mathbb C)$ be Hermitian. Let $A\in M_{n,m}(\mathbb C)$, $e,f\in M_{n,r}(\mathbb C)$, and $y\in\mathbb C^n$ satisfy $$A^*JA=I_m,\quad e^*Je=f^*Jf=0,\quad e^*Jf=I_r,\quad A^*Je=A^*Jf=0,$$ $$A^*Jy=e^*Jy=f^*Jy=0,\qquad y^*Jy=-1.$$ Index coordinates by $0,\ldots,n-1$. Let $H$ have entries $H_{i,n-1-i}=H_{n-1-i,i}=1$ for $0\le i<r$, diagonal entries $1$ for $r\le i<r+m$, diagonal entry $-1$ at $r+m$, and all other entries zero. There are inverse matrices $Q,Q^{-1}\in M_n(\mathbb C)$ such that $$Q^*JQ=H,\qquad Q_{\cdot,i}=e_{\cdot,i}\ (0\le i<r),\qquad Q_{\cdot,r+j}=A_{\cdot,j}\ (0\le j<m),\qquad Q_{\cdot,r+m}=y.$$
