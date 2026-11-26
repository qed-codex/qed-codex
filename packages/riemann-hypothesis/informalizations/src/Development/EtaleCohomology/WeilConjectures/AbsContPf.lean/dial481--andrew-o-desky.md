---
{
  "module": "src/Development/EtaleCohomology/WeilConjectures/AbsContPf.lean",
  "declarations": [
    "LateralTheory.EWeil.AbsContPf.AbsCont_of"
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

## Continuity of coefficients from a separated module filtration

[Theorem PHT.0501](https://andrewodesky.com/rh/lean/LateralTheory.EWeil.AbsContPf.AbsCont_of/)

Assume the module-filtration property in the conventions below. Let $\ell$ be prime, $G$ a topological group, $M$ a finitely generated $\mathbb Z_\ell$-module, and $\rho:G\to\operatorname{Aut}_{\mathbb Z_\ell}(M)$ a representation. Let $M\supseteq K_0\supseteq K_1\supseteq\cdots$ be submodules with $\bigcap_jK_j=0$. Suppose $$\{g\in G:\rho(g)x-x\in K_j\}$$ is open for every $x\in M$ and every $j\ge0$. Then for every $\mathbb Z_\ell$-linear map $\phi:M\to\mathbb Q_\ell$ and every $x\in M$, the function $g\mapsto\phi(\rho(g)x)$ is continuous.
