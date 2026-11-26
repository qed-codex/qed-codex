---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/LocallyFreeOfShortExactStatement.lean",
  "declarations": [
    "GlobalTheory.T.locally_free_of_short_exact"
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

## Local freeness of a kernel lattice

[Theorem ALG.1061](https://andrewodesky.com/rh/lean/GlobalTheory.T.locally_free_of_short_exact/)

Let $o$ be a commutative ring, $\Omega$ a field with an $o$-algebra structure, and $R\subseteq\Omega$ an $o$-subalgebra. Let $$0\longrightarrow E_1\xrightarrow{i}E\xrightarrow{q}E_2\longrightarrow0$$ be an exact sequence of $\Omega$-vector spaces. Let $L\subseteq E$ be an additive subgroup and $r_1,r_2\ge0$. If $L$ is locally free of rank $r_1+r_2$ over $R$ and $q(L)$ is locally free of rank $r_2$, then $i^{-1}(L)$ is locally free of rank $r_1$.
