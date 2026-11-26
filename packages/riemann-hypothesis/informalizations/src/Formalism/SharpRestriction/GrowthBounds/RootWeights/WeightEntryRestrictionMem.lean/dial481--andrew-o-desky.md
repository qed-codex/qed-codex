---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/WeightEntryRestrictionMem.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.binomial_stable_contains_components"
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

## Binomial stability preserves each polynomial weight component

[Theorem ALG.1000](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.binomial_stable_contains_components/)

Let $R$ be a commutative ring, $I$ a finite set, $n\ge0$, $S\subseteq I$, and choose a sign $\varepsilon_i\in\{1,-1\}$ for each $i\in I$. In $R[X_{ia}:i\in I,1\le a\le n]$, give a monomial $X^m$ the weight $$w_a(m)=\sum_{i\in S}\varepsilon_i m_{ia}\in\mathbb Z.$$ For $1\le a\le n$ and $k\ge0$, define the $R$-linear operator $$B_{a,k}(X^m)=\binom{w_a(m)}kX^m.$$ If an $R$-submodule $W$ is stable under every $B_{a,k}$, then for every $f=\sum_mc_mX^m\in W$ and every $\nu\in\mathbb Z^n$, $$\sum_{m:w(m)=\nu}c_mX^m\in W.$$
