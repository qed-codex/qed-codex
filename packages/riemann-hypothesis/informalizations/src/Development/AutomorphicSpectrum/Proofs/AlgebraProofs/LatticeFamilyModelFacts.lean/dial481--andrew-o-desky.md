---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/LatticeFamilyModelFacts.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.FamGood1.flatten_summand"
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

## Refining a projective model to make lattice families and subspaces split

[Theorem AG.1019](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.FamGood1.flatten_summand/)

Let $O$ be a discrete valuation domain, $\Omega$ a field with an $O$-algebra structure, and $x=(x_{ki})$ a coordinate family indexed by a finite set $K$ of finite blocks $I_k$. Let $d\in\mathbb N$. Assume the dimension-$d$ model conditions and field-generation condition of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)), and use its chart notation $m_c(x),R_c(x)$.

Let $I$ be finite, $E$ an $\Omega$-vector space, $U_j\subseteq E$ subspaces, and $(\Gamma_{j,c})$ compatible families in the sense of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)), for $j\in I$. Suppose for every $j$ and $c$ with $m_c(x)\ne0$, $\Gamma_{j,c}$ is generated over $R_c(x)$ by a finite set spanning $E$ over $\Omega$.

One can add finitely many finite coordinate blocks $z$ so that the combined coordinates $(x,z)$ satisfy the same dimension-$d$ model conditions, and on every nonzero combined chart $c'$ the module $$L_{j,c'}=R_{c'}(x,z)\Gamma_{j,c'|_K}$$ is locally free of rank $\dim_\Omega E$ inside $E$ for every $j\in I$, in the sense of ([Coordinate models and compatible chart lattices](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.IsModelOver/)). Moreover, for each $j$ and nonzero combined chart $c'$ there is an $\Omega$-linear projection $\rho:E\to U_j$ restricting to the identity on $U_j$ and preserving $L_{j,c'}$.
