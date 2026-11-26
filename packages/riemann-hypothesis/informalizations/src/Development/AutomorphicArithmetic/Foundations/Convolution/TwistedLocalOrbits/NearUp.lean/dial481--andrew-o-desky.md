---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/TwistedLocalOrbits/NearUp.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.Loc.nearUp"
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

## Cyclic orbital transfer for functions supported near the identity

[Theorem REP.0612](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.Loc.nearUp/)

Let $E/k$ be a finite Galois extension of nonarchimedean local fields, with $k$ of characteristic zero and the valuation on $E$ extending that on $k$. Let $\sigma$ generate $\operatorname{Gal}(E/k)$, let $n\ge0$, and choose Haar measures $\mu_E,\mu_k$ on $\operatorname{GL}_n(E)$ and $\operatorname{GL}_n(k)$, with their Borel sigma algebras.

There is a positive valuation radius $\rho$ such that every locally constant compactly supported $f:\operatorname{GL}_n(k)\to\mathbb C$ with $$\operatorname{supp}f\subseteq\{g:v_k(g_{ij}-\delta_{ij})\le\rho\ \text{for all }i,j\}$$ has a locally constant compactly supported transfer $\phi:\operatorname{GL}_n(E)\to\mathbb C$ satisfying the matching conditions below.
