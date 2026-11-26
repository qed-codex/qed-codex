---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean",
  "declarations": [
    "GlobalTheory.miStarRow_alt_alt"
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

## Period identities for linked records and sufficiently constrained families

[Theorem THETA.0017](https://andrewodesky.com/rh/lean/GlobalTheory.miStarRow_alt_alt/)

Assume items (1)–(10) and (13) of ([Fourteen statements from the literature on representations, automorphic forms and theta series, taken as hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.PrimIn.PublishedThetaConditionTheorems/)), items (40) and (41) of ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)), and ([Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)). Assume also ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)).

Choose a permitted extension of the norm choices, an extension parameter and a geometric parameter. Use the transfer definition in ([Transfer conditions and numerical bounds for the stage-zero construction](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.OpenParameterStatements/)) for the construction determined by these choices and the assumed reciprocity statement. Each of the following two properties transfers through this construction, with its own witnessing property of points:

1. For every family in the class, every member above its initial threshold, and its selected record, ([A period identity with norm-preserving maps and local units](https://andrewodesky.com/rh/lean/Formalism.IndefR.Cx.CxData.MIstar2/)) holds.
2. For every sufficiently constrained family of the second refinement of the class, eventually at its members above the initial threshold, the selected record satisfies ([A period identity with norm-preserving maps and local units](https://andrewodesky.com/rh/lean/Formalism.IndefR.Cx.CxData.MIstar2/)).

The second assertion uses the same period identity as the first, with weaker family and member quantifiers.
