---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsUniqueHaarOfInvariantRadonOnCosets.lean",
  "declarations": [
    "GlobalTheory.QuotientHaar.existsUnique_haar_of_invariantRadon"
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

## Recovering Haar measure from an invariant quotient measure

[Theorem REP.0381](https://andrewodesky.com/rh/lean/GlobalTheory.QuotientHaar.existsUnique_haar_of_invariantRadon/)

Let $G$ be a locally compact second-countable Hausdorff topological group, $H\subseteq G$ a closed subgroup, and $dh$ a left Haar measure on $H$. Give all spaces their Borel measurable structures. Let $\mu\ne0$ be a $G$-invariant measure on $G/H$, finite on compact sets. There is a unique left Haar measure $dg$ on $G$ such that for every measurable $f:G\to[0,\infty]$, the function $$gH\longmapsto\int_H f(gh)\,dh$$ is measurable and $$\int_G f(g)\,dg=\int_{G/H}\int_Hf(gh)\,dh\,d\mu(gH).$$
