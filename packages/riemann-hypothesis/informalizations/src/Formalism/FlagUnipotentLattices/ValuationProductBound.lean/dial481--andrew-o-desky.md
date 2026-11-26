---
{
  "module": "src/Formalism/FlagUnipotentLattices/ValuationProductBound.lean",
  "declarations": [
    "Formalism.HermitianLatticeCounting.Final.S4.weightedCS"
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

## Weighted Cauchy-Schwarz for a sum of vectors

[Theorem ALG.0626](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticeCounting.Final.S4.weightedCS/)

Let $I$ be a finite set, $V$ a seminormed abelian group, $v_i\in V$, and $w_i>0$ for $i\in I$. Then $$\left\|\sum_{i\in I}v_i\right\|^2\le\left(\sum_{i\in I}w_i^{-1}\right)\left(\sum_{i\in I}w_i\|v_i\|^2\right).$$
