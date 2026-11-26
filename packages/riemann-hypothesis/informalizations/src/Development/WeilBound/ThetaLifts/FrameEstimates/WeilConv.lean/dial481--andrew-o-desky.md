---
{
  "module": "src/Development/WeilBound/ThetaLifts/FrameEstimates/WeilConv.lean",
  "declarations": [
    "PositivityTheory.ThKEst.weilConv"
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

## Convergence and growth of theta integrals in the Weil range

[Theorem THETA.1555](https://andrewodesky.com/rh/lean/PositivityTheory.ThKEst.weilConv/)

Assume the unitary Siegel-set conclusions of ([Siegel sets and rapid decay for unitary groups](https://andrewodesky.com/rh/lean/UpperTheory.LiteratureTheorems.siegel_set_unitary_of_literature/)) and the basic theta-function conclusions of ([Continuity, invariance, and growth of theta series](https://andrewodesky.com/rh/lean/PositivityTheory.ThKF0.thetaBasic/)). Let $E/F$ be number fields, $\sigma\in\operatorname{Aut}_F(E)$, and choose a full compatible global Weil-pair datum: a normalized base datum, a rank-$n$ Hermitian space $X$ of signature $(r,s)$, a rank-$d$ skew-Hermitian space $W$ of signature $(r',s')$, their lattice and Haar/fundamental-domain model, two Hecke splitting characters with the prescribed quadratic restrictions, and a Weil action $\omega$. Suppose $$d+2\min(r,s)<2n\quad\text{or}\quad\min(r,s)=0.$$ For every adelic Schwartz–Bruhat function $\Phi$, the theta kernel $\theta_\Phi(g,h)$ is integrable in $g$ over the chosen fundamental domain $\mathcal F_X$, and for some $C\in\mathbb R$, $k\ge0$, $$\int_{\mathcal F_X}|\theta_\Phi(g,h)|\,dg\le C H_W(h)^k\qquad(h\in U(W)(\mathbb A_F)),$$ where $H_W$ is the prescribed adelic matrix height. For fixed finite-adelic Schwartz–Bruhat part $\phi$ and $h$, the theta integral of $f\otimes\phi$ is a continuous function of the archimedean Schwartz function $f$.
