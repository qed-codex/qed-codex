---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/NewtonLowerBounds/NewtonIdentitiesLowDegree.lean",
  "declarations": [
    "PositivityTheory.RgJS.newton_identities_low_degree"
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

## A lower bound for the first power sums

[Theorem ALG.1351](https://andrewodesky.com/rh/lean/PositivityTheory.RgJS.newton_identities_low_degree/)

For every integer $N\ge1$ there is a constant $c_N>0$ such that, for every finite set $A$ with $|A|=N$ and every family $(a_i)_{i\in A}\subset\mathbb C$ satisfying $|\prod_i a_i|=1$, $$c_N\le\sum_{k=1}^{N}\left|\sum_{i\in A}a_i^k\right|^2.$$
