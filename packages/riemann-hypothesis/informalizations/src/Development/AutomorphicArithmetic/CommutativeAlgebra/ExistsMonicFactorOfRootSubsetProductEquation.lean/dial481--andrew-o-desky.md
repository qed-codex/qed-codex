---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/ExistsMonicFactorOfRootSubsetProductEquation.lean",
  "declarations": [
    "UpperTheory.exists_monic_factor_of_root_subset_product_equation"
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

## A monic factor with prescribed product of roots

[Theorem ALG.1064](https://andrewodesky.com/rh/lean/UpperTheory.exists_monic_factor_of_root_subset_product_equation/)

Let $A$ be a commutative ring, let $n,m,N\ge0$ satisfy $n+m=N$, and let $g\in A[X]$ be monic of degree $N$. Fix $\alpha\in A$ and a unit $c\in A^\times$. Suppose that for every commutative $A$-algebra $S$ and every factorization $$g(X)=\prod_{i=1}^N(X-x_i)\quad\text{in }S[X],$$ the elements $b_J=\prod_{i\in J}x_i$, indexed by the $m$-element subsets $J\subseteq\{1,\ldots,N\}$, satisfy $$\prod_{|J|=m}(\alpha-b_J)=0,\qquad \sum_{|J|=m}\prod_{\substack{|J'|=m\\J'\ne J}}(\alpha-b_{J'})=c.$$ Here $\alpha,c$ denote their images in $S$. Then there are monic $P,Q\in A[X]$ such that $$g=PQ,\qquad \deg Q\le m,\qquad [X^m]Q=1,\qquad Q(0)=(-1)^m\alpha.$$
