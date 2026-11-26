---
{
  "module": "src/Formalism/RealPlaceAnalysis/RealPlaceTaylor/CompactExponentialSurjective.lean",
  "declarations": [
    "Formalism.REAL.compact_exists_log_bounded"
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

## A bounded logarithm in a compact unitary subgroup

[Theorem REP.0315](https://andrewodesky.com/rh/lean/Formalism.REAL.compact_exists_log_bounded/)

Let $n\ge0$, $J=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)$ with $\varepsilon_i\in\{1,-1\}$, and let $k\in U(n)$ commute with $J$. There is $Y\in M_n(\mathbb C)$ such that $$Y^*J+JY=0,\qquad YJ=JY,\qquad \exp Y=k,\qquad \|Y\|_{\mathrm F}^2\le3\|k-I_n\|_{\mathrm F}^2.$$ Here $\|A\|_{\mathrm F}^2=\sum_{i,j}|A_{ij}|^2$ and $A^*$ is the conjugate transpose.
