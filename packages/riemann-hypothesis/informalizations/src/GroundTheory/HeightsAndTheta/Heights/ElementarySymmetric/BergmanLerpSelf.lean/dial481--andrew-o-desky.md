---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ElementarySymmetric/BergmanLerpSelf.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.BergmanL1Convergence.full"
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

## L1 convergence of normalized Bergman functions

[Theorem AG.1528](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.BergmanL1Convergence.full/)

Let $X$ be a compact Hausdorff space with a finite holomorphic atlas of complex dimension $D\ge0$, its Borel measurable structure, and a holomorphic line bundle $L$. Give $L$ a smooth semipositive Hermitian metric, written locally as $\|s\|^2=|s|^2e^{-\phi}$, and let $\mu$ be a probability measure with smooth positive coordinate densities $v(z)$. Let $V_n\subseteq H^0(X,L^{\otimes n})$ be finite-dimensional complex subspaces. Define $$B_n(x)=\sup_{s\in V_n}\frac{\|s(x)\|^2}{\int_X\|s\|^2\,d\mu},\qquad b(x)=\frac{\operatorname{Re}\det(\pi^{-1}(\partial_i\bar\partial_j\phi)(x))}{v(x)},$$ with the value $0$ for a quotient $0/0$. Suppose that for every $\epsilon>0$ and all sufficiently large $n$, $$\dim_{\mathbb C}V_n\ge n^D\left(\int_X b\,d\mu-\epsilon\right).$$ Then $$\lim_{n\to\infty}\int_X|n^{-D}B_n(x)-b(x)|\,d\mu(x)=0,$$ where $n^{-D}$ at $n=0$ uses the convention $0^{-1}=0$.
