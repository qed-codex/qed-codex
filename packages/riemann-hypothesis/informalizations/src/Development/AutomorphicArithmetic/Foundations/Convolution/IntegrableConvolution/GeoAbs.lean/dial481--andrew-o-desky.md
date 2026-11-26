---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/IntegrableConvolution/GeoAbs.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.L1.geoAbs"
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

## Absolute convergence and reduction of a cyclic orbital integral

[Theorem REP.0340](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.L1.geoAbs/)

Let $G$ be a locally compact, Hausdorff, second-countable topological group, with its Borel structure and Haar measure $\mu$. Let $\gamma\in G$ have closed conjugacy class and abelian centralizer $T=C_G(\gamma)$, and let $\nu$ be Haar measure on $T$. Let $m\ge0$ and $\delta_0,\ldots,\delta_m\in T$ satisfy $\delta_0\cdots\delta_m=\gamma$. For continuous compactly supported $\Phi:G^{m+1}\to\mathbb C$, put $$\begin{aligned}F(x_0,\ldots,x_m)&=\Phi(x_0^{-1}\delta_0x_1,\ldots,x_m^{-1}\delta_mx_0),\\P\Phi(z)&=\int_{G^m}\Phi(y_0,\ldots,y_{m-1},(y_0\cdots y_{m-1})^{-1}z)\,d\mu^m(y).\end{aligned}$$ For every measurable $\rho:G^{m+1}\to[0,\infty]$ with $$\int_T\rho(tx_0,\ldots,tx_m)\,d\nu(t)=1\qquad(x\in G^{m+1}),$$ one has $\int_{G^{m+1}}|F(x)|\rho(x)\,d\mu^{m+1}(x)<\infty$. Moreover, $$\int_{T\backslash G^{m+1}}F=\int_{T\backslash G}P\Phi(x^{-1}\gamma x).$$
