---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/WeilCriterionInvariantMeasureHomogeneousSpace.lean",
  "declarations": [
    "GlobalTheory.WeilCriterion.exists_isInvariantRadon"
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

## An invariant measure on a homogeneous quotient

[Theorem REP.0252](https://andrewodesky.com/rh/lean/GlobalTheory.WeilCriterion.exists_isInvariantRadon/)

Let $G$ be a locally compact, second countable Hausdorff topological group, equipped with its Borel measurable structure. Let $H\subseteq G$ be a closed subgroup, with its induced locally compact topology. If $$\Delta_G(h)=\Delta_H(h)\qquad(h\in H),$$ then the Borel quotient $G/H$ admits a nonzero $G$-invariant measure finite on compact subsets.
