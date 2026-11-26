---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExtendsToSemiAbelianOfLocallyNormalNoetherianStatement.lean",
  "declarations": [
    "GlobalTheory.T.extendsToSemiAbelian_of_locally_normal_noetherian"
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

## Local semiabelian extensions glue over a normal base

[Theorem AV.1636](https://andrewodesky.com/rh/lean/GlobalTheory.T.extendsToSemiAbelian_of_locally_normal_noetherian/)

Let $S$ be a normal Noetherian scheme, $j:X\hookrightarrow S$ a dominant open immersion, and $A\to X$ an abelian scheme. Suppose that for every $s\in S$ there is an open neighbourhood $U\subseteq S$ and a semiabelian group scheme $G_U\to U$ whose pullback to $X\times_S U$ is isomorphic to the restriction of $A$ as a group scheme. Then there is a semiabelian group scheme $G\to S$ and a group-scheme isomorphism $$A\simeq X\times_S G.$$
