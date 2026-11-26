---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/NormSubOnePowThreeLe.lean",
  "declarations": [
    "GlobalTheory.AmiceDist.amice"
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

## A power series approximating finite Fourier transforms of a distribution

[Theorem PHT.0268](https://andrewodesky.com/rh/lean/GlobalTheory.AmiceDist.amice/)

Let $\ell$ be prime and $O\subset\overline{\mathbb Q}_\ell$ a discrete valuation $\mathbb Z_\ell$-subalgebra finite as a $\mathbb Z_\ell$-module. For every $r\ge0$, let $\mu_r:\mathbb Z/\ell^r\mathbb Z\to O$ satisfy $$\mu_r(x)=\sum_{x'\bmod\ell^{r+1},\ x'\equiv x\bmod\ell^r}\mu_{r+1}(x').$$ There is $L(T)=\sum_{n\ge0}a_nT^n\in O[[T]]$ such that for every $r\ge1$ and $z\in\overline{\mathbb Q}_\ell$ with $z^{\ell^r}=1$, $$\left|\sum_{n=0}^{\ell^{3r}-1}a_n(z-1)^n-\sum_{x\bmod\ell^r}\mu_r(x)z^{\widetilde x}\right|_\ell\le|\ell|_\ell^{2r},$$ where $\widetilde x\in\{0,\ldots,\ell^r-1\}$ is the standard representative.
