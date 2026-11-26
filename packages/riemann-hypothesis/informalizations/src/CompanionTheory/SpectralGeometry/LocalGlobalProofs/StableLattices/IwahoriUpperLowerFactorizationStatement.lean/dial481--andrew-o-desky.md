---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/IwahoriUpperLowerFactorizationStatement.lean",
  "declarations": [
    "GlobalTheory.T.iwahori_upper_lower_factorization"
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

## Upper and lower factorization near the identity

[Theorem ALG.1154](https://andrewodesky.com/rh/lean/GlobalTheory.T.iwahori_upper_lower_factorization/)

Let $E$ be a ring, $I$ a finite set, and $w:I\to\mathbb N$ injective. Let $P_i\in E$ satisfy $P_i^2=P_i$, $P_iP_j=0$ for $i\ne j$, and $\sum_iP_i=1$. Let $J\subset E$ be an additive subgroup closed under multiplication and under $x\mapsto P_ix$ and $x\mapsto xP_i$. Assume that for every $x\in J$ there is $y\in J$ with $(1+x)(1+y)=(1+y)(1+x)=1$. For every $k\in E$ with $k-1\in J$, there exist $a,b\in E$ with $a-1,b-1\in J$ and $k=ab$, such that $$P_i aP_j=0\quad(w(j)<w(i)),\qquad P_i bP_j=0\quad(w(i)<w(j)),\qquad P_i bP_i=P_i.$$
