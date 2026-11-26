---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeGlobalOneFormsProjectiveRank.lean",
  "declarations": [
    "GlobalTheory.AbCoh.globForm_FP"
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

## Finite projectivity and rank of global one-forms

[Theorem AV.1371](https://andrewodesky.com/rh/lean/GlobalTheory.AbCoh.globForm_FP/)

Let $R$ be a commutative ring, and let $A/\operatorname{Spec}R$ be an abelian scheme smooth of constant relative dimension $g\ge0$. The $R$-module $$H^0(A,\Omega^1_{A/R})$$ is finitely generated and projective. For every prime $\mathfrak p\in\operatorname{Spec}R$, its rank at $\mathfrak p$ is $g$.
