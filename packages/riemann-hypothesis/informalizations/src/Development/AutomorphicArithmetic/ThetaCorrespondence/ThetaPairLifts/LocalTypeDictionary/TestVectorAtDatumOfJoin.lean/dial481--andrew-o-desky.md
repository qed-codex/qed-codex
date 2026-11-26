---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TestVectorAtDatumOfJoin.lean",
  "declarations": [
    "GlobalTheory.RowTestAssembly.test_vector_at_datum_of_join"
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

## Rationality of the row theta maps at all admissible realisation records

[Theorem THETA.1.1764](https://andrewodesky.com/rh/lean/GlobalTheory.RowTestAssembly.test_vector_at_datum_of_join/)

Assume the following six hypotheses.

- (H1) All fifty-three statements of ([Hypothesis list B: fifty-three assumed statements on Weil representations, theta lifts, discrete series, L-functions and complex multiplication](https://andrewodesky.com/rh/lean/GlobalTheory.FunPr.ThetaLocalInputs/)).
- (H2) The polynomial parametrization of ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)).
- (H3) The functional equation in item (54)(e) of ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)).
- (H4) Items (2)–(7) of ([Seven additional assumptions for the maximal slope bound](https://andrewodesky.com/rh/lean/GlobalTheory.Published.HeckeFunctionalEquationAbs/)).
- (H5) ([Theta integrals agree: for a matching datum the two theta integrals are proportional on matching functions, with a unique nonzero constant, and the constant changes by an L-value when a hyperbolic plane is removed](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree/)).
- (H6) ([Local matching: a matching datum for two Hermitian spaces of complementary dimensions admits matched quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching/)).

Then the rationality test for the rows holds at all admissible realisation records, in the sense of ([Realisation records over the stages of the construction, and properties that hold at all admissible realisation records](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.Bl.AtDat/)).

Written out, the conclusion says that the following holds eventually for large bases. Let $B$ be a base with coefficient field $\mathbb L$ and embedding $\jmath\colon\mathbb L\to\mathbb C$, let $f$ be a frame for $B$ and $T$ twist data for $B$, and suppose that $(B,f)$ is exact and $T$ is saturated. Let $c$ be a pinned column input for $(B,f,T)$, $Z$ a completion of $c$, $W$ a set of finite places of $\mathbb L$, and $z$ an admissible realisation record over $(c,Z,W)$, with rational family $\mathcal A$ and realisation $R$. Then $R$ satisfies the rationality test for the rows of ([Rational families of forms, their realisations by theta maps, and the rationality test](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)): there are finitely many complex-linear functionals $\psi_1,\dots,\psi_N$ on $H_E^{\epsilon}$, with common kernel zero, such that $$\psi_i\bigl(\widetilde\Theta_t(\widetilde j_X(t)\,x)\bigr)\in\sigma(\mathbb L)\qquad\text{for every tuple }t\text{ of }\mathcal A,\ 1\le i\le N,\ x\in R_t .$$
