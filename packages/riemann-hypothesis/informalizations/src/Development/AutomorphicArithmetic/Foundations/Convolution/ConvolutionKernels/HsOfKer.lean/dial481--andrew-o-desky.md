---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/ConvolutionKernels/HsOfKer.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.K.hsOfKer"
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

## A square-integrable vector kernel gives a Hilbert-Schmidt operator

[Theorem ALG.0352](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.K.hsOfKer/)

Let $(X,\nu)$ be an $s$-finite measure space such that $L^2(X,\nu;\mathbb C)$ is separable. Let $A:L^2(X,\nu)\to L^2(X,\nu)$ be bounded and complex-linear, and $k:X\to L^2(X,\nu)$ an $L^2$ function, in the sense of almost-everywhere strong measurability and $$\int_X\|k(x)\|_{L^2}^2\,d\nu(x)<\infty.$$ If, for every $\varphi\in L^2(X,\nu)$, $$(A\varphi)(x)=\langle k(x),\varphi\rangle\qquad\text{for almost every }x,$$ then $A$ is Hilbert–Schmidt. The inner product is conjugate-linear in its first argument; the exceptional null set may depend on $\varphi$.
