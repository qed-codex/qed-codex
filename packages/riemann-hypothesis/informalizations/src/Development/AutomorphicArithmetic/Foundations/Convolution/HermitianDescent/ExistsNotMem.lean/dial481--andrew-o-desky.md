---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/HermitianDescent/ExistsNotMem.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.D.h90"
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

## A norm-one equation over a finite algebra

[Theorem ALG.1654](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.D.h90/)

Let $k$ be a commutative local ring, let $R$ be a commutative $k$-algebra, let $S$ be a commutative $k$-algebra finite as a $k$-module, and let $T$ be a commutative $S$-algebra. Let $\sigma$ be an $S$-algebra automorphism of $T$ and $q\ge1$. Assume that $\sigma^q=1$, that $S\to T$ is injective, that every element fixed by $\sigma$ lies in the image of $S$, and that there are finitely many $x_i,y_i\in T$ satisfying $$\sum_i x_i\,\sigma^j(y_i)= \begin{cases}1&j=0,\\0&0<j<q\end{cases} \qquad(0\le j<q).$$ For every $a\in T^\times$ with $\prod_{j=0}^{q-1}\sigma^j(a)=1$, there exists $z\in T^\times$ such that $$a\,\sigma(z)=z.$$
