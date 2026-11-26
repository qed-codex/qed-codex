---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutEllRegW.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.elliptic_regularity_weighted"
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

## Smoothness of continuous weak solutions of an elliptic system

[Theorem ALG.0280](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.SmoothTransferRegularity.elliptic_regularity_weighted/)

Let $U\subseteq\mathbb R^d$ be open, $J$ finite, and for each $j\in J$ let $$P_ju=\sum_{k=0}^{m_j}\sum_{w\in\{1,\ldots,d\}^k}a_{j,k,w}(x)\partial_wu$$ with complex coefficients smooth on $U$. Let $u:\mathbb R^d\to\mathbb C$ be continuous on $U$. Suppose $$\int_{\mathbb R^d}u(x)P_j^{\mathsf t}\varphi(x)\,dx=0$$ for every $j$ and every smooth compactly supported $\varphi$ with support in $U$. If for every $x\in U$ and $\xi\in\mathbb R^d\setminus\{0\}$ there is $j$ with $$\sum_{w\in\{1,\ldots,d\}^{m_j}}a_{j,m_j,w}(x)\prod_{h=1}^{m_j}\xi_{w_h}\ne0,$$ then $u$ is smooth on $U$.
