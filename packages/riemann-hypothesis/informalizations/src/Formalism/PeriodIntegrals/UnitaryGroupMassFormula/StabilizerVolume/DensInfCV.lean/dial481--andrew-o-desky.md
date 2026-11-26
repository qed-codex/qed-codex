---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/DensInfCV.lean",
  "declarations": [
    "PI.VolStabS.changeVar_holds"
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

## Replacing a local submersion integral by a linear pushforward

[Theorem ALG.0777](https://andrewodesky.com/rh/lean/PI.VolStabS.changeVar_holds/)

Let $\mu$ be an additive Haar measure on $\mathbb R^n$, and let $f:\mathbb R^n\to\mathbb R^m$ be continuously differentiable. If $Df(x_0)$ is surjective, there are an open neighborhood $N$ of $x_0$ and a surjective real-linear map $A:\mathbb R^n\to\mathbb R^m$ such that the following holds.

For every continuous compactly supported $\varphi:\mathbb R^n\to\mathbb R$ with closed support contained in $N$, there is a continuous compactly supported $G:\mathbb R^n\to\mathbb R$ satisfying $$\int_{f^{-1}(S)}\varphi\,d\mu=\int_{A^{-1}(S)}G\,d\mu$$ for every compact set $S\subseteq\mathbb R^m$.
