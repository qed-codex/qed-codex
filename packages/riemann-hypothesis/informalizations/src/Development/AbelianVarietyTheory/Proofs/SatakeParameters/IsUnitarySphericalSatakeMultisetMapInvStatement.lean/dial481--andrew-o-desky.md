---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/IsUnitarySphericalSatakeMultisetMapInvStatement.lean",
  "declarations": [
    "GlobalTheory.T.isUnitarySphericalSatakeMultiset_map_inv"
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

## Inversion preserves unitary spherical Satake multisets

[Theorem REP.0487](https://andrewodesky.com/rh/lean/GlobalTheory.T.isUnitarySphericalSatakeMultiset_map_inv/)

Let $O$ be a discrete valuation domain with finite residue field of cardinality $q$, let $K=\operatorname{Frac}O$, let $r\ge0$, and let $\beta$ be a multiset of $r$ complex numbers. If $\beta$ has a unitary spherical realization as defined below, then the multiset $\{b^{-1}:b\in\beta\}$ also has such a realization.
