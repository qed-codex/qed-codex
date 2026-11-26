---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean",
  "declarations": [
    "UpperTheory.GalC.final_alt_alt"
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

## A divisibility bound for constructed families from the norm bound at 2 and 3

[Theorem GC.0019](https://andrewodesky.com/rh/lean/UpperTheory.GalC.final_alt_alt/)

Assume the following statements.

1. Items (55), (56), (57), (58), (59) and (60) of ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)).
2. Items (1) and (2) under **Six further assumptions, relative to the reciprocity maps** in ([Hypotheses for the existence of built points with origin data](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.Bl.HypAAlt/)).
3. ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)).

Fix any real $c$. If the condition $\mathrm{NB}(c)$ of ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)) holds, then the following condition holds for the same construction with parameter $c$.

There is a property $R$ of points such that the eventual assertion (A) in the definition of $\mathrm{NB}(c)$ holds for $R$, and the following property holds for the families produced through the good points satisfying $R$ and the construction's link, in the sense of the **Transfer** definition in ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)): every sufficiently constrained family of the second refinement of the class satisfies the divisibility bound stated in item (40) of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)).
