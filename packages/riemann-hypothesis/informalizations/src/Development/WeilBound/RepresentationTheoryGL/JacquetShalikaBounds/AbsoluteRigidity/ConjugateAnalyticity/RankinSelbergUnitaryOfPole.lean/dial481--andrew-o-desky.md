---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/ConjugateAnalyticity/RankinSelbergUnitaryOfPole.lean",
  "declarations": [
    "PositivityTheory.RgJS.rankin_selberg_unitary_of_pole"
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

## Analytic regularization of a unitary Rankin–Selberg product

[Theorem ANT.1600](https://andrewodesky.com/rh/lean/PositivityTheory.RgJS.rankin_selberg_unitary_of_pole/)

Assume the normalization, Satake-twist and normalized Rankin–Selberg regularization packages specified below. Let $E$ be a totally complex number field and $\pi,\pi'$ unitary cuspidal automorphic representation classes of ranks $m,k\ge1$. There is a finite set $S_0$ of finite places such that, for every finite $S\supseteq S_0$ and every choice of unramified Satake parameters $\alpha_{w,i}$ of $\pi$ and $\beta_{w,j}$ of $\pi'$ outside $S$, the product $$L^S(s)=\prod_{w\notin S}\prod_{i=1}^m\prod_{j=1}^k(1-\alpha_{w,i}\overline{\beta_{w,j}}(Nw)^{-s})^{-1}$$ admits a function $F:\mathbb C\to\mathbb C$ analytic at every positive real number, and a real $\sigma_0$, such that for every real $\sigma>\sigma_0$, $$F(\sigma)=\begin{cases}(\sigma-1)L^S(\sigma),& (m,\pi)=(k,\pi'),\\L^S(\sigma),& (m,\pi)\ne(k,\pi').\end{cases}$$
