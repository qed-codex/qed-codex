---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/PolynomialDerivatives/IntegrableRpowGauss.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.LC.oneMom"
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

## Moments of a complex Gaussian

[Theorem ALG.0507](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.LC.oneMom/)

Let $c>0$ and let $p,q\ge0$ be integers. The function $z\mapsto z^p\bar z^{\,q}e^{-c|z|^2}$ is integrable on $\mathbb C$ and $$\int_{\mathbb C}z^p\bar z^{\,q}e^{-c|z|^2}\,dz=\begin{cases}\displaystyle\frac{\pi p!}{c^{p+1}},&p=q,\\0,&p\ne q.\end{cases}$$
