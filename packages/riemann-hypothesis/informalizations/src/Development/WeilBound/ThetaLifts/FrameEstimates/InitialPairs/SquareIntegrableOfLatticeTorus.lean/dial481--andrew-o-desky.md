---
{
  "module": "src/Development/WeilBound/ThetaLifts/FrameEstimates/InitialPairs/SquareIntegrableOfLatticeTorus.lean",
  "declarations": [
    "PositivityTheory.ThKEst.Sq.square_integrable_of_lattice_torus"
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

## Square integrability of theta integrals in the Weil range

[Theorem THETA.1559](https://andrewodesky.com/rh/lean/PositivityTheory.ThKEst.Sq.square_integrable_of_lattice_torus/)

Assume the source's eight global input packages for adelic unitary groups and theta kernels: group topology and heights, signatures and split-frame ranks, Siegel sets, basic theta regularity, squared-kernel bounds, finite tensor decompositions, compact-translate lattice-sum bounds, and torus lattice-sum bounds. Fix a compatible global Weil-pair datum for number fields $E/F$ and $\sigma\in\operatorname{Aut}_F(E)$, with Hermitian $X$ of rank $n$ and signature $(r,s)$, skew-Hermitian $W$ of rank $d$ and signature $(r',s')$, a normalized model, splitting characters and Weil action $\omega$. Suppose $$d+2\min(r,s)<2n\quad\text{or}\quad\min(r,s)=0,$$ $$\min(r',s')=0\quad\text{or}\quad n+\min(r',s')<d.$$ For every Haar measure $\mu$ on $U(W)(\mathbb A_F)$, every rational fundamental domain $\mathcal F_W$, and every adelic Schwartz–Bruhat function $\Phi$, the theta integral $I_\Phi(h)$ over the model's rational quotient of $U(X)$ satisfies $$\int_{\mathcal F_W}|I_\Phi(h)|^2\,d\mu(h)<\infty.$$
