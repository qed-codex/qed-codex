---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/IntegrableConvolution/MatImage.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.L1.matImage"
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

## A full matrix algebra from commuting joint irreducibility

[Theorem REP.0788](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.L1.matImage/)

Let $A$ be a complex algebra, $W$ a nonzero finite-dimensional complex vector space, $\rho:A\to\operatorname{End}_{\mathbb C}(W)$ a unital algebra homomorphism, and $B\subset\operatorname{End}_{\mathbb C}(W)$. Assume every element of $B$ commutes with every $\rho(a)$, and the only subspaces stable under both $\rho(A)$ and $B$ are $0$ and $W$. Then for some integer $d>0$, $$\rho(A)\simeq M_d(\mathbb C)$$ as complex algebras.
