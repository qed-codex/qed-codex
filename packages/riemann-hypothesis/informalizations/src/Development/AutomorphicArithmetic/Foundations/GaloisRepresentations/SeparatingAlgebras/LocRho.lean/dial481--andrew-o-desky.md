---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SeparatingAlgebras/LocRho.lean",
  "declarations": [
    "UpperTheory.Gal.Gen.Loc.block_le"
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

## A coefficient bound under block substitution

[Theorem ALG.1337](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Gen.Loc.block_le/)

Let $\ell$ be prime, let $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ be a field isomorphism, let $T$ be a set, $I\subseteq T$ finite, and $n,D\ge0$. Choose matrices $A_\tau\in M_n(\mathbb C)$ and $R\ge1$ such that $$|\iota^{-1}((A_\tau)_{ij})|_\ell\le\begin{cases}R&\tau\in I,\\1&\tau\notin I.\end{cases}$$ Let $P\in\mathbb C[X_{\tau,i,j}:\tau\in T,\ 0\le i,j<n]$. Give the variables in blocks $\tau\in I$ weight one and all other variables weight zero. Assume $P$ is weighted homogeneous of degree $D$ and every coefficient $c$ of $P$ satisfies $|\iota^{-1}(c)|_\ell\le1$.

Apply in each block the linear matrix substitution $X_\tau\mapsto A_\tau X_\tau$, and call the resulting polynomial $Q$. Every coefficient $d$ of $Q$ satisfies $$|\iota^{-1}(d)|_\ell\le R^D.$$
