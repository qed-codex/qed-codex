---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectorGridDenominatorBoundStatement.lean",
  "declarations": [
    "GlobalTheory.T.projector_grid_denominator_bound"
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

## A denominator bound for a product of root projectors

[Theorem ALG.1267](https://andrewodesky.com/rh/lean/GlobalTheory.T.projector_grid_denominator_bound/)

Let $V$ be a $\mathbb Q$-vector space, $a,b,K,w,\Lambda\in\mathbb N$, $e_{ij}\in\operatorname{End}_{\mathbb Q}(V)$ for $i,j\ge0$, and $L,M\subseteq V$ be $\mathbb Z$-submodules. Suppose that both $L$ and $M$ are preserved by $e_{ij}^{,k}/k!$ for all $i,j<a+b$ with $i\ne j$ and all $k\ge0$. Assume $$K+a+b\le w+1,\qquad(j+k+1)!\mid\Lambda\,j!k!\quad(j,k\ge0,\ j+k+1\le w).$$ On $\operatorname{End}_{\mathbb Q}(V)$ set $D_{ij}(T)=e_{ij}T-Te_{ij}$ and, for $i<a\le j<a+b$, set $$P_{ij}=\sum_{k=0}^K\frac{(-1)^k(j-i-1)!}{k!(k+j-i)!}\,D_{ji}^{,k}D_{ij}^{,k}.$$ Let $P$ be the ordered composition of the row products $P_{i,a}P_{i,a+1}\cdots P_{i,a+b-1}$, with rows $i=a-1,a-2,\ldots,0$ in that order and multiplication denoting composition. If $c\in\mathbb N$ and $T\in\operatorname{End}_{\mathbb Q}(V)$ satisfy $cT(L)\subseteq M$, then $$c\Lambda^{ab}P(T)(L)\subseteq M.$$
