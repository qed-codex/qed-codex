---
{
  "module": "src/Development/EtaleCohomology/DivisorCycles/DivPlus.lean",
  "declarations": [
    "LateralTheory.DivDb.plus_of"
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

## Extracting a representation from low-degree annihilators

[Theorem AGR.1171](https://andrewodesky.com/rh/lean/LateralTheory.DivDb.plus_of/)

Let $\Gamma$ be a compact topological group, $K$ an algebraically closed field of characteristic zero with a Hausdorff topological-ring structure, and $K'/K$ an algebraically closed field extension. Let $\rho:\Gamma\to\operatorname{GL}_N(K)$ be a continuous semisimple representation, $S\subset\Gamma$ dense, and $P:\Gamma\to K[T]$ a family such that $P_s$ is monic of degree $n$ and $P_s(\rho(s))=0$ for $s\in S$. Suppose the Lie algebra of the Zariski closure of $\rho(\Gamma)$, after extension to $K'$, contains $X$ with distinct eigenvalues $e_1,\ldots,e_n\in K'$ satisfying $$\frac1{|A|}\sum_{i\in A}e_i\ne\frac1{|B|}\sum_{i\in B}e_i$$ for every two disjoint nonempty subsets $A,B\subset\{1,\ldots,n\}$. Let $\psi:\Gamma\to K^\times$ be a character, continuous as a $K$-valued function, and satisfy $\psi(s)=(-1)^nP_s(0)$ for $s\in S$.

There exists a continuous semisimple $r:\Gamma\to\operatorname{GL}_n(K)$ and an injective intertwiner $A:K^n\hookrightarrow K^N$ such that, for every $g\in\Gamma$, $$\operatorname{charpol}(r(g))(\rho(g))=0,\qquad\det r(g)=\psi(g),$$ and $P_s(r(s))=0$ for $s\in S$. The set of $g$ for which $r(g)$ has separable characteristic polynomial is open and dense. For $s\in S$, that characteristic polynomial equals $P_s$ whenever it is separable, and also whenever $P_s$ is separable and its root multiset is the only size-$n$ multiset supported on its roots with that product.

There are finitely many intertwiners $T_j:K^N\to K^n$ and $T'_j:K^n\to K^N$ satisfying $$T_j\rho(g)=r(g)T_j,\qquad\rho(g)T'_j=T'_jr(g),\qquad\sum_jT'_jT_j=1_{K^N}.$$
