---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/EpiOfFiniteFlatStatement.lean",
  "declarations": [
    "GlobalTheory.T.epi_of_finite_flat"
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

## Faithfully flat quasi-compact maps are epimorphisms

[Theorem AG.1499](https://andrewodesky.com/rh/lean/GlobalTheory.T.epi_of_finite_flat/)

Let $R$ be a commutative ring, let $A,B,A'$ be schemes over $\operatorname{Spec}R$, and let $f:A\to B$ be flat, surjective, and quasi-compact. If two morphisms $g_1,g_2:B\to A'$ over $R$ satisfy $g_1\circ f=g_2\circ f$, then $g_1=g_2$.
