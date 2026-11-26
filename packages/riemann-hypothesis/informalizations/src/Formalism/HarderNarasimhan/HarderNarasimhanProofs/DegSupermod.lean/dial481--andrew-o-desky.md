---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/DegSupermod.lean",
  "declarations": [
    "Formalism.HN.degree_supermodular"
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

## Supermodularity of lattice degree

[Theorem ARAK.1317](https://andrewodesky.com/rh/lean/Formalism.HN.degree_supermodular/)

Let $R$ be a ring, $V$ a left $R$-module, $E$ a finite-dimensional real inner-product space, and $\rho:V\to E$ an additive map. Let $A,B\subset L\subset V$ be $R$-submodules. Assume $\rho$ is injective on $L$ and $\rho(L)$ is discrete.

For an $R$-submodule $N\subset L$, let $r(N)$ be the rank over $\mathbb Z$ of $\rho(N)$ and let $$\deg(N)=-\log\operatorname{covol}(\rho(N)),$$ where covolume is measured in the real span of $\rho(N)$ with the induced Euclidean metric. Then $$r(A+B)+r(A\cap B)=r(A)+r(B),$$ $$\deg(A)+\deg(B)\le\deg(A+B)+\deg(A\cap B).$$
