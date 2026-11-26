---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/PAdicTorsionHoms/SplitCM.lean",
  "declarations": [
    "UpperTheory.V.Z.Win.splitCM"
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

## A CM quadratic extension splitting a prescribed place

[Theorem AGR.0188](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Win.splitCM/)

Let $F$ be a totally real number field, $E/F$ a quadratic CM extension, and $\Omega$ an algebraic closure of $F$ containing $E$. Let $\ell$ be prime and $r:G_F\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$, $n\ge0$, a representation whose restriction to $G_E$ is irreducible. For every finite place $v$ of $F$, there are CM number fields $E',M\subseteq\Omega$, containing $F$, with $E,E'\subseteq M$, such that $$[E':F]=[M:E]=[M:E']=2,$$ $r|_{G_M}$ is irreducible, and every place $w$ of $E'$ above $v$ admits a continuous field isomorphism $$F_v\simeq E'_w$$ which agrees with the given embedding of $F$.
