---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeUnobstructedSquareZeroAffine.lean",
  "declarations": [
    "GlobalTheory.UnobTop.abelianUnobstructed"
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

## Lifting abelian schemes through a square-zero quotient

[Theorem AV.0054](https://andrewodesky.com/rh/lean/GlobalTheory.UnobTop.abelianUnobstructed/)

Let $R$ and $R_0$ be commutative rings and let $\pi:R\twoheadrightarrow R_0$ be a surjective ring homomorphism with kernel $I$ satisfying $I^2=0$. For every abelian scheme $A_0$ over $\operatorname{Spec}R_0$, there exists an abelian scheme $A$ over $\operatorname{Spec}R$ and an isomorphism of group schemes $$A\times_{\operatorname{Spec}R}\operatorname{Spec}R_0\simeq A_0.$$
