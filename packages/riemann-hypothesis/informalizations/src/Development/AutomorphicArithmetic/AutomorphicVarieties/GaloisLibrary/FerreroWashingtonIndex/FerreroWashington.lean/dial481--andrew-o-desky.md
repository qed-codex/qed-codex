---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean",
  "declarations": [
    "UpperTheory.V.FW.ferreroWashington"
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

## Class-group ranks in cyclotomic towers

[Theorem GC.0081](https://andrewodesky.com/rh/lean/UpperTheory.V.FW.ferreroWashington/)

Let $K/\mathbb Q$ be an abelian number field and $\ell$ a prime. Suppose $K$ contains a primitive $\ell$-th root of unity if $\ell$ is odd, or a primitive fourth root if $\ell=2$. There is an integer $r\ge0$ such that for every $n\ge0$, with $K_n=K(\mu_{\ell^n})$, $$\#\big(\operatorname{Cl}(\mathcal O_{K_n})/\ell\operatorname{Cl}(\mathcal O_{K_n})\big)\le\ell^r.$$ Here $\mu_m$ denotes the group of $m$-th roots of unity and $\operatorname{Cl}$ the ideal class group.
