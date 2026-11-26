---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean",
  "declarations": [
    "GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt"
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

## Upper bound for the maximal slope of the row lattice at the points that have a grid with compatible choices

[Theorem ARAK.1.1769](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt/)

Assume the following five hypotheses.

- (H1) All fifty-three statements of ([Hypothesis list B: fifty-three assumed statements on Weil representations, theta lifts, discrete series, L-functions and complex multiplication](https://andrewodesky.com/rh/lean/GlobalTheory.FunPr.ThetaLocalInputs/)).
- (H2) All seven statements of ([Seven additional assumptions for the maximal slope bound](https://andrewodesky.com/rh/lean/GlobalTheory.Published.HeckeFunctionalEquationAbs/)).
- (H3) ([Theta integrals agree: for a matching datum the two theta integrals are proportional on matching functions, with a unique nonzero constant, and the constant changes by an L-value when a hyperbolic plane is removed](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree/)).
- (H4) ([Local matching: a matching datum for two Hermitian spaces of complementary dimensions admits matched quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching/)).
- (H5) The lower bound for the scalars, in the sense of ([Admissible points over the members of a family, the row lattice of a point and its maximal slope](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.FamHyp/)).

Let $\mathcal C$ be the class of families of that page. Then there is a real number $C_F^0$ such that for every real number $C_F\ge C_F^0$ the following holds for all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal C$, with the real number $C_H$ of the definition of "sufficiently constrained". If $\mathrm{Fm}$ satisfies the divisibility bound, then eventually at the admissible points of $\mathrm{Fm}$: every such point that has a grid with compatible choices at $C_F$, in the sense of ([Grids with compatible choices over a point of a family, and their period functionals](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.Fun.HasGrid/)), satisfies $$\mu_{\max}(R_0)\ \le\ x^{C_H}\,b\;-\;\frac1{s_K}\sum_{v}\log\kappa_v .$$ Here $(x,i)$ is the member over which the point lies, $b=\exp(x^{\varepsilon})$, $R_0$ is the row lattice of the point and $\mu_{\max}(R_0)$ its maximal slope, $K$ is the coefficient field of the member, the sum runs over the $s_K$ infinite places $v$ of $K$, and $\kappa_v$ are the scalars of the point at the base level.
