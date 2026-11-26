---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/DensInfTop.lean",
  "declarations": [
    "PI.VolStabS.submLocal_holds"
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

## Continuous densities for compactly supported submersion integrals

[Theorem ALG.0671](https://andrewodesky.com/rh/lean/PI.VolStabS.submLocal_holds/)

Let $\mu,\nu$ be additive Haar measures on $\mathbb R^n,\mathbb R^m$, and let $f:\mathbb R^n\to\mathbb R^m$ be $C^1$. If $df_{x_0}$ is surjective, there is an open neighborhood $N$ of $x_0$ with the following property: for every continuous compactly supported $\varphi:\mathbb R^n\to\mathbb R$ with $\operatorname{supp}\varphi\subseteq N$, there is a continuous $g:\mathbb R^m\to\mathbb R$ such that, for every compact set $S\subseteq\mathbb R^m$, $$\int_{f^{-1}(S)}\varphi\,d\mu=\int_S g\,d\nu.$$
