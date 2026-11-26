---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/UnitarySchrodingerModel/UnitarySchrodingerLemmas/LowRankSiegelDensities/MassTop.lean",
  "declarations": [
    "PositivityTheory.PfSWUS.HMass.oneVecBinaryMass"
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

## A uniform estimate for unit fibres of a binary Hermitian form

[Theorem ANT.0999](https://andrewodesky.com/rh/lean/PositivityTheory.PfSWUS.HMass.oneVecBinaryMass/)

Let $E/F$ be a CM extension of number fields with conjugation, and let $J\in M_2(E)$ be nonsingular Hermitian. Choose any $F$-basis $b_1,\ldots,b_d$ of $E$. For a finite place $v$ of $F$, write $F_v$ for the completion, $E_v=F_v\otimes_FE$, $q_v=|\mathcal O_F/\mathfrak p_v|$, and $$\Lambda_v=\sum_{j=1}^d\mathcal O_{F_v}b_j\subset E_v.$$ There is $C\in\mathbb R$ such that, outside finitely many $v$, the following holds for every additive Haar measure $\lambda_v$ with $\lambda_v(\mathcal O_{F_v})=1$ and every family $(m_s)_{s\in F_v}$ satisfying the fibre-measure conditions below: $$\left|m_s(\Lambda_v^2)_{\mathbb R}-1\right|\le\frac C{q_v^2}\qquad(|s|_v=1).$$
