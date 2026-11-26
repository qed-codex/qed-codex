---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaFamilyOrigin/LbIsoOfAssociatedGermsFlatStatement.lean",
  "declarations": [
    "GlobalTheory.T.lbIso_of_associated_germs_flat"
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

## Associated section germs after a flat cover identify line bundles

[Theorem AG.0200](https://andrewodesky.com/rh/lean/GlobalTheory.T.lbIso_of_associated_germs_flat/)

Let $X$ be an integral scheme and $f:Y\to X$ a flat surjective morphism. Let $L,L'$ be line bundles on $X$ with global sections $s,s'$, and assume $s\ne0$. Suppose that for every $y\in Y$ there are local frames for $L,L'$ near $f(y)$ in which the coefficient germs of $f^*s,f^*s'$ in $\mathcal O_{Y,y}$ are associated, meaning that one is a unit times the other. Then $L\simeq L'$ as line bundles on $X$.
