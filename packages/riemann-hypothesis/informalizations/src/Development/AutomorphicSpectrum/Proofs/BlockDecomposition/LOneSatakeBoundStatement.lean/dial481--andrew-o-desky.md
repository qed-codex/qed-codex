---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LOneSatakeBoundStatement.lean",
  "declarations": [
    "GlobalTheory.T.l_one_satake_bound"
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

## Singleton Langlands data and spherical Satake parameters

[Theorem REP.0985](https://andrewodesky.com/rh/lean/GlobalTheory.T.l_one_satake_bound/)

Let $k$ be a nonarchimedean local field of characteristic zero, $n\ge0$, and $\xi_1,\ldots,\xi_n:k^\times\to\mathbb C^\times$ unramified characters. Let $\pi$ be a smooth complex representation of $\operatorname{GL}_n(k)$ and fix a uniformizer $\varpi$ of $k$. The following are equivalent:

1. $\pi$ is the Langlands representation attached to the multiset of singleton segments $\{[\xi_1],\ldots,[\xi_n]\}$.
2. $\pi$ is irreducible, has a nonzero $\operatorname{GL}_n(\mathcal O_k)$-fixed vector, and is a subquotient of the normalized principal series induced from the unramified characters taking values $\xi_i(\varpi)$ on $\varpi$.
