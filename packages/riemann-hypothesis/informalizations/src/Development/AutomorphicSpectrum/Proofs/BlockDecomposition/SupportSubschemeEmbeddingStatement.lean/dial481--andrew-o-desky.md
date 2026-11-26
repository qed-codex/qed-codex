---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/SupportSubschemeEmbeddingStatement.lean",
  "declarations": [
    "GlobalTheory.T.support_subscheme_embedding"
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

## Embedding an irreducible representation in cuspidal induction

[Theorem REP.1535](https://andrewodesky.com/rh/lean/GlobalTheory.T.support_subscheme_embedding/)

Let $k$ be a nonarchimedean local field, $N\ge0$, and $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_N(k)$. There are $c\ge0$, integers $n_1,\ldots,n_c\ge0$ with $\sum_i n_i=N$, and irreducible cuspidal smooth complex representations $\rho_i$ of $\operatorname{GL}_{n_i}(k)$ such that $\pi$ admits an injective intertwining map $$\pi\hookrightarrow\rho_1\times\cdots\times\rho_c,$$ where $\times$ denotes normalized parabolic induction for the ordered block decomposition $(n_1,\ldots,n_c)$.
