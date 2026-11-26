---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/AssemblyBase.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Kleiman.SerreFinite.full",
    "GroundTheory.Heights₂.Heights.Kleiman.SerreVanish.full"
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

## Finiteness of each graded Cech cohomology module

[Theorem AG.0599](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Kleiman.SerreFinite.full/)

Let $S$ be a noetherian commutative ring and $N\ge0$. Let $M$ be a finitely generated graded module over $S[X_0,\ldots,X_N]$, with its compatible underlying $S$-module structure. For every $i\ge0$ and every $c\in\mathbb Z$, the degree-$c$ cohomology module of the projective Čech complex of $M$ is finitely generated over $S$.

## Eventual vanishing of higher graded Cech cohomology

[Theorem AG.1405](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Kleiman.SerreVanish.full/)

Let $S$ be a noetherian commutative ring, $N\ge0$, and let $M$ be a finitely generated graded module over $S[X_0,\ldots,X_N]$, with the compatible underlying $S$-module structure. Let $H^i_{\check C}(M)_c$ denote degree-$c$ cohomology of the projective Čech complex, formed by localizing at the coordinate variables and their products.

There exists an integer $c_0$ such that $$H^i_{\check C}(M)_c=0\qquad(i\ge1,\ c\ge c_0).$$
