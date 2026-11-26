---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/CuspidalGenericity/Direct.lean",
  "declarations": [
    "GlobalTheory.BZSeg.Cusp.isGenericFor_of_isCuspidal_direct"
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

## Genericity of smooth cuspidal representations

[Theorem REP.1281](https://andrewodesky.com/rh/lean/GlobalTheory.BZSeg.Cusp.isGenericFor_of_isCuspidal_direct/)

Let $k$ be a nonarchimedean local field, $N\ge0$, and $V$ a nonzero complex vector space. Let $\pi$ be a smooth representation of $\mathrm{GL}_{N+1}(k)$ on $V$ whose Jacquet module for every nontrivial parabolic unipotent radical is zero. No irreducibility hypothesis is imposed. For every continuous nontrivial additive character $\psi:k\to S^1$, the twisted Jacquet module $$V_{U,\psi_U}=V/\langle\pi(u)v-\psi_U(u)v:u\in U,\ v\in V\rangle_{\mathbb C},\qquad \psi_U(u)=\psi\left(\sum_{i=1}^{N}u_{i,i+1}\right),$$ is nonzero, where $U$ is the upper unitriangular subgroup.
