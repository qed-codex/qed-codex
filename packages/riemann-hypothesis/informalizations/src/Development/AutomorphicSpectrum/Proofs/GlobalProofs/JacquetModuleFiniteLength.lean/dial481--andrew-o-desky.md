---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/JacquetModuleFiniteLength.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.JacquetBridge.jacquetFiniteLength"
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

## Finite length of Jacquet modules

[Theorem REP.1688](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.JacquetBridge.jacquetFiniteLength/)

Let $k$ be a nonarchimedean local field. Let $I$ be a finite linearly ordered set, let $(n_i)_{i\in I}$ be finite block sizes, and choose an identification of their disjoint union with a finite index set of size $n=\sum_i n_i$. Let $P$ be the resulting block parabolic of $\operatorname{GL}_n(k)$ with Levi subgroup $M=\prod_i\operatorname{GL}_{n_i}(k)$. If $\pi$ is a smooth complex representation of $\operatorname{GL}_n(k)$ of finite length, then its Jacquet representation $r_P(\pi)$ of $M$ has finite length.
