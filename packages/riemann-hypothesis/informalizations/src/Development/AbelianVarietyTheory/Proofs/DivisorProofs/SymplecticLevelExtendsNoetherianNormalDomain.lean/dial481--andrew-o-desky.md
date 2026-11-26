---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SymplecticLevelExtendsNoetherianNormalDomain.lean",
  "declarations": [
    "GlobalTheory.SympLevelExt.level_extends"
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

## Extension of a symplectic level structure over a normal domain

[Theorem AV.0704](https://andrewodesky.com/rh/lean/GlobalTheory.SympLevelExt.level_extends/)

Let $R_1$ be a commutative ring, $P_1$ a polarized abelian scheme over $R_1$ in the convention below, and $h:R_1\to R$ a homomorphism to a Noetherian integrally closed domain. Let $F$ be the fraction field of $R$. Let $Q$ be a polarized abelian scheme over $F$ of the same dimension as $P_1$, and let $\phi:Q\to P_1$ identify its underlying group scheme with the base change along $R_1\to R\to F$, with $L_Q\simeq\phi^*L_{P_1}$.

Let $K>0$ be invertible in $R$ and $\zeta\in R^\times$. If $Q$ admits a full symplectic level-$K$ structure for the image of $\zeta$ in $F$, there exist a polarized abelian scheme $P/R$ and a group-compatible base-change map $\psi:P\to P_1$, of the same dimension, such that $$L_P\simeq\psi^*L_{P_1},$$ and $P$ admits a full symplectic level-$K$ structure for $\zeta$.
