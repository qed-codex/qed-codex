---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/TorsionRankCounts/RankCountAlt.lean",
  "declarations": [
    "UpperTheory.V.ZK.Up.rankCount"
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

## Counting images of a subgroup of bounded rank

[Theorem ALG.0355](https://andrewodesky.com/rh/lean/UpperTheory.V.ZK.Up.rankCount/)

Let $H,B$ be abelian groups, $q\ge1$ and $r\ge0$ integers, and assume $qB=0$ and the torsion subgroup $H_{\mathrm{tors}}$ is finite. Let $J\le H$ have $\mathbb Z$-module rank at most $r$, and let $f:H\to B$ be a homomorphism. Every finite subset $S\subseteq f(J)$ satisfies $$|S|\le q^r|H_{\mathrm{tors}}|.$$
