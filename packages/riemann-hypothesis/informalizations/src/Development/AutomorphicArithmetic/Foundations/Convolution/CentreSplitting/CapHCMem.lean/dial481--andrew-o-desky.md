---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/CapHCMem.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.Dp.capHC"
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

## A central Capelli element and its Harish-Chandra image

[Theorem REP.0185](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.Dp.capHC/)

Let $n\ge0$, let $E_{ab}$ be the matrix-unit generators of $U(\mathfrak{gl}_n(\mathbb C))$, indexed by $0\le a,b<n$, and let $u\in\mathbb C$. The element $$C_n(u)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{j=0}^{n-1}\left(E_{\sigma(j),j}+\delta_{\sigma(j),j}\left(u+\frac{n-1}{2}-j\right)\right)$$ is central and its Harish-Chandra image is $$\prod_{j=0}^{n-1}(u+X_j).$$
