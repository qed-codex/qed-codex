---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CharacterDecompositionAndClassFunctionExpansion.lean",
  "declarations": [
    "GlobalTheory.CharDec.char_decomp"
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

## Decomposition into irreducible characters

[Theorem REP.1576](https://andrewodesky.com/rh/lean/GlobalTheory.CharDec.char_decomp/)

Let $G$ be a finite group and let $\chi:G\to\mathbb C$ be the character of a finite-dimensional complex representation. There are irreducible complex characters $\chi_1,\ldots,\chi_m$, with repetitions allowed and $m\ge0$, such that $$\chi=\sum_{j=1}^m\chi_j.$$
