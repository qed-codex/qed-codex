---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/FreeActionAffineChartStatement.lean",
  "declarations": [
    "GlobalTheory.T.free_action_affine_chart"
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

## Affine quotient chart for a free finite action

[Theorem AG.1682](https://andrewodesky.com/rh/lean/GlobalTheory.T.free_action_affine_chart/)

Let $S$ be a scheme, $G/S$ a finite locally free group scheme, and $X/S$ a scheme with a free $G$-action $a:G\times_SX\to X$. Let $V\subset X$ and $W\subset S$ be affine opens such that $V\subset X\times_SW$ and $$a^{-1}(V)=\operatorname{pr}_2^{-1}(V).$$ There exist an affine scheme $Y$ and a finite, flat, locally finitely presented, surjective morphism $q:V\to Y$ for which the action and projection induce a Cartesian square $$\begin{array}{ccc} G\times_SV&\xrightarrow{\ a\ }&V\\ \operatorname{pr}_2\downarrow&&\downarrow q\\ V&\xrightarrow{q}&Y. \end{array}$$
