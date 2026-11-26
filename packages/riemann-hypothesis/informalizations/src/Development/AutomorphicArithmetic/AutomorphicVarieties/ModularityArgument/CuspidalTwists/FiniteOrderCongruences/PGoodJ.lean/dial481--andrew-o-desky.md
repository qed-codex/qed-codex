---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CuspidalTwists/FiniteOrderCongruences/PGoodJ.lean",
  "declarations": [
    "UpperTheory.V.Cu2.goodJ"
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

## A bounded choice of twist separating infinity characters

[Theorem AGR.1158](https://andrewodesky.com/rh/lean/UpperTheory.V.Cu2.goodJ/)

Let $K$ be a totally complex number field of degree two and $\pi$ a cuspidal automorphic representation of $\operatorname{GL}_2(\mathbb A_K)$ whose associated infinitesimal-character datum is regular algebraic. For every integer $m\ge1$, there is an integer $j$ with $1\le j\le9$ such that the following holds. Let $Y$ be a Hecke character and $a:\operatorname{Hom}(K,\mathbb C)\to\mathbb Z$ satisfy $Y_\infty(x)=\prod_\sigma\sigma(x)^{a(\sigma)}$ for every $x\in K^\times$, where $Y_\infty$ denotes its archimedean restriction on principal elements. Let $\tau:K\hookrightarrow\mathbb C$. If $$a(\tau)=-mj,\qquad a(\overline\tau)=mj,$$ then $\pi\otimes Y$ has infinitesimal-character multisets $M,M'$ at $\tau,\overline\tau$ such that $M\ne\varnothing$, the multiset union $M+M'$ has no repetitions, and $$M+M'\subset\mathbb Z+\tfrac32.$$
