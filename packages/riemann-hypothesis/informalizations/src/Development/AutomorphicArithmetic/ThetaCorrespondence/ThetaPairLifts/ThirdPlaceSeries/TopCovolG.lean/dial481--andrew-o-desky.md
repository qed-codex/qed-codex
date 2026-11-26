---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean",
  "declarations": [
    "SelfIntersectionVolumeEstimates.topCovolG_alt_alt"
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

## The covolume bound from self-intersection, small-section and geometric estimates

[Theorem ARAK.1.1757](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.topCovolG_alt_alt/)

Assume the following four statements.

1. The four groups of assumptions of ([Geometric and counting assumptions for the covolume bound](https://andrewodesky.com/rh/lean/SelfIntersectionVolumeEstimates.VolumeEstimateHypotheses/)).
2. All twenty-eight assertions of ([Global hypotheses for Hodge-bundle estimates](https://andrewodesky.com/rh/s/k2-hodge-bundle-hypotheses.html)).
3. Item (15), on deformations along divided-power thickenings, of ([Hypothesis list C: sixty assumed statements on resolution of singularities, arithmetic intersection theory, positivity of line bundles, toroidal compactifications, abelian schemes and p-divisible groups](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.ResolutionCharZero/)).
4. The conclusion of ([A lower bound for the mean component volume slope, under arithmetic geometry hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use/)): there is a nonnegative constant with which the lower bound stated there for the mean of the volume slopes holds for every arithmetic datum, enhanced realization, stage, level cover and weight admitted there.

Then the estimate of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)) holds. In the notation of that page, there is $\varepsilon_0>0$ such that for every $0<\varepsilon\le\varepsilon_0$ there are threshold rules for the family constants with the following property. For every theta family and every value of $C_H$ that satisfy conditions 1–14 of that page and the threshold rules, there are $C_0\ge0$ and $x_0$ such that $$\frac{2\log H_K(M_j)}{[K:\mathbb Q]\,D}\le P_j+C\,B_0\log\log x\qquad(1\le j\le m)$$ for every $x\ge x_0$ above the starting scale of the family, every member $\iota\in I_x$, every compatible point and every $C\ge C_0$.
