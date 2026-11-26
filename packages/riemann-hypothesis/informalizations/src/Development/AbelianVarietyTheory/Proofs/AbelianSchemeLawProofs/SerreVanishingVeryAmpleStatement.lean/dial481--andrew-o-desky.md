---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/SerreVanishingVeryAmpleStatement.lean",
  "declarations": [
    "GlobalTheory.T.serre_vanishing_very_ample"
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

## Serre vanishing and polynomial realization of sections

[Theorem AG.1445](https://andrewodesky.com/rh/lean/GlobalTheory.T.serre_vanishing_very_ample/)

Let $R$ be a commutative Noetherian ring, $f:X\to\operatorname{Spec}R$ a scheme morphism, $H$ a line bundle on $X$, and $s_0,\ldots,s_m\in H^0(X,H)$ sections defining a closed immersion $X\hookrightarrow\mathbb P_R^m$ over $R$.

For every line bundle $M$ on $X$, there is $t_0\in\mathbb Z$ such that $$H^1(X,M\otimes H^{\otimes t})=0\qquad(t\in\mathbb Z,\ t\ge t_0).$$ There is also $t_1\in\mathbb N$ such that for every integer $t\ge t_1$, every section $\sigma\in H^0(X,H^{\otimes t})$ has the form $$\sigma=F(s_0,\ldots,s_m)$$ for a homogeneous polynomial $F\in R[T_0,\ldots,T_m]$ of degree $t$.
