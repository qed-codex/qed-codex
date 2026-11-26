---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/SelfdualMeasureTwistBySymmetricAutoStatement.lean",
  "declarations": [
    "GlobalTheory.T.selfdual_measure_twist_by_symmetric_auto"
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

## Self-dual measure under a symmetric change of variables

[Theorem ANT.0738](https://andrewodesky.com/rh/lean/GlobalTheory.T.selfdual_measure_twist_by_symmetric_auto/)

Let $V$ be a second-countable locally compact Hausdorff abelian topological group with its Borel measurable structure. Let $\mu$ be a measure and $\chi:V\times V\to\mathbb C$, and suppose $\mu$ is self-dual for $\chi$ in the convention below. Let $B:V\to V$ be a continuous additive automorphism with continuous inverse, satisfying $$\chi(x,By)=\chi(Bx,y)\qquad(x,y\in V).$$ If $c\ge0$ and $B_*\mu=c\mu$, then $(\sqrt c)^{-1}\mu$ is self-dual for $(x,y)\mapsto\chi(x,By)$.
