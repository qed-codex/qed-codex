---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/SumTruncConv.lean",
  "declarations": [
    "GlobalTheory.ZeroDetect.zero_detect"
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

## A Dirichlet polynomial detecting zeros near one

[Theorem ANT.0498](https://andrewodesky.com/rh/lean/GlobalTheory.ZeroDetect.zero_detect/)

There is an integer $Q_0\ge0$ such that, for every integer $Q\ge Q_0$, every $q\ge1$, every nontrivial Dirichlet character $\chi$ modulo $q$ with $q\le Q$, and every $\rho\in\mathbb C$ satisfying $$\operatorname{Re}\rho\ge1-\frac1{400},\qquad |\operatorname{Im}\rho|\le Q,\qquad L(\rho,\chi)=0,$$ one has $$\left|\sum_{Q^3<n\le Q^6}\left(\sum_{\substack{d\mid n\\d\le Q^3}}\mu(d)\right)\chi(n)n^{-\rho}\right|\ge\frac12.$$ Here $\mu$ is the Möbius function and $n^{-\rho}=\exp(-\rho\log n)$ for $n>0$.
