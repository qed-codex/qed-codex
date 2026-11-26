---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CoherentCohomologyProofs/SerreVanishingH1TwistStatement.lean",
  "declarations": [
    "GlobalTheory.T.serre_vanishing_h1_twist"
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

## Vanishing of first cohomology after a large very ample twist

[Theorem AG.1328](https://andrewodesky.com/rh/lean/GlobalTheory.T.serre_vanishing_h1_twist/)

Let $R$ be a commutative Noetherian ring, let $Y$ be a scheme over $\operatorname{Spec}R$, and let $H,M$ be line bundles on $Y$. Assume sections $s_0,\ldots,s_m$ of $H$, for some $m\ge0$, exhibit $H$ as relatively very ample over $\operatorname{Spec}R$ in the following chart sense: the nonzero loci of the $s_i$ cover $Y$, each is affine, and on each such locus the ratios $s_j/s_i$ generate its coordinate ring as an $R$-algebra. There is $t_0\in\mathbb Z$ such that for every integer $t\ge t_0$, every Čech $1$-cocycle with values in $$M\otimes H^{\otimes t}$$ on an open cover subordinate to line-bundle trivializations is a coboundary.
