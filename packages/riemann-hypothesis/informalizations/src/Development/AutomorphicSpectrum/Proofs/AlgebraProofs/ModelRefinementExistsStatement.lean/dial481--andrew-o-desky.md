---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/ModelRefinementExistsStatement.lean",
  "declarations": [
    "GlobalTheory.T.model_refinement_exists"
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

## Adding projective coordinates to obtain normal affine charts

[Theorem AG.1100](https://andrewodesky.com/rh/lean/GlobalTheory.T.model_refinement_exists/)

Let $O$ be a discrete valuation domain of characteristic zero, $\Omega$ a field with an $O$-algebra structure, and $x=(x_{ki})$ a coordinate family indexed by a finite set $K$ of finite blocks $I_k$. Let $d\in\mathbb N$. Assume the dimension-$d$ model conditions and field-generation condition of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)), and use its chart notation $m_c(x),R_c(x)$.

There are finitely many additional finite coordinate blocks $z$ such that the combined tuple $(x,z)$ satisfies the same model conditions with the same $d$, and, on every chart $c$ with $m_c(x,z)\ne0$, $R_c(x,z)$ is integrally closed in $\Omega$.
