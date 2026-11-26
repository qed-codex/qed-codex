---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/DeRhamH1RankPrimitive.lean",
  "declarations": [
    "GlobalTheory.AbCoh.rank_prim_HH1"
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

## Rank and primitivity of first de Rham cohomology

[Theorem AV.1488](https://andrewodesky.com/rh/lean/GlobalTheory.AbCoh.rank_prim_HH1/)

Let $R$ be a commutative ring and $A/R$ an abelian scheme of constant relative dimension $g\ge0$. Then $H^1_{\mathrm{dR}}(A/R)$ is a finitely generated projective $R$-module of constant rank $2g$. Every class $x$ in this module is primitive for the group law $m:A\times_R A\to A$: $$m^*x=\operatorname{pr}_1^*x+\operatorname{pr}_2^*x.$$
