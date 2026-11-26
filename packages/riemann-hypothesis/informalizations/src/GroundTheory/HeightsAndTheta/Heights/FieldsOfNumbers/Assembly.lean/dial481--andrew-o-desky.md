---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/FieldsOfNumbers/Assembly.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.FieldNumbers.CutRegular.full",
    "GroundTheory.Heights₂.Heights.FieldNumbers.HilbEventuallyPoly.full"
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

## Eventual polynomiality of a multigraded Hilbert function

[Theorem AG.1586](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.FieldNumbers.HilbEventuallyPoly.full/)

Let $F$ be a field, $K$ a finite set, and $I_k$ finite sets for $k\in K$. Give $R=F[X_{k,i}:k\in K,i\in I_k]$ the multigrading $\deg X_{k,i}=e_k$. For every multihomogeneous ideal $J\subseteq R$, there is $P\in\mathbb Q[T_k:k\in K]$ such that $$\dim_F(R/J)_{\mathbf m}=P(\mathbf m)$$ for all sufficiently large multidegrees $\mathbf m$, with every coordinate sufficiently large.

## Cutting a multigraded intersection number by a regular section

[Theorem AG.1626](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.FieldNumbers.CutRegular.full/)

Let $F$ be a field, $K$ a finite set, and $I_k$ finite sets. Give $R=F[X_{k,i}:k\in K,i\in I_k]$ the block grading $\deg X_{k,i}=e_k$. Let $P\subseteq R$ be a multihomogeneous prime such that, for each $k$, some $X_{k,i}\notin P$. Suppose $$\dim(R/P)-|K|=n+1\qquad(n\ge0).$$ Let $s\notin P$ be multihomogeneous of degree $c\in\mathbb N^K$, and let $b_1,\ldots,b_n\in\mathbb Z^K$. For an ideal $J$, let $h_J(m)=\dim_F(R/J)_m$ for componentwise $m\ge0$ and zero otherwise. Define $\Delta_bh(m)=h(m)-h(m-b)$, and let $I_J(b_1,\ldots,b_t)$ be the eventual constant value of $\Delta_{b_1}\cdots\Delta_{b_t}h_J$ as all coordinates of $m$ tend to infinity, with value zero if no such constant exists. Then $$I_P(b_1,\ldots,b_n,c)=\sum_W\operatorname{length}_{R_W}\bigl((R/(P,s))_W\bigr)I_W(b_1,\ldots,b_n),$$ where $W$ runs over the minimal primes of $(P,s)$ for which every block has a variable outside $W$.
