---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SchurDeterminants/PDenseSub.lean",
  "declarations": [
    "UpperTheory.Gal.Schur.denseSub"
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

## Zariski density of a spanning additive subgroup and its translates

[Theorem ALG.0827](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Schur.denseSub/)

Let $K$ be a characteristic-zero field, $I$ a finite set, and $\Lambda\subseteq K^I$ an additive subgroup with $\operatorname{span}_K\Lambda=K^I$. For every $a\in K^I$, the translate $a+\Lambda$ is Zariski dense: if $P\in K[X_i:i\in I]$ vanishes on $a+\Lambda$, then $P=0$.
