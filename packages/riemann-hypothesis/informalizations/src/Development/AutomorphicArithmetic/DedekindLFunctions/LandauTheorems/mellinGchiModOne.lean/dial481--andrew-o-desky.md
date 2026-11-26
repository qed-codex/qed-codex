---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean",
  "declarations": [
    "Deduction.mellin_Gchi_modOne"
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

## Mellin transform for the principal character

[Theorem ANT.0144](https://andrewodesky.com/rh/lean/Deduction.mellin_Gchi_modOne/)

Use $g_1$, Euler's constant $\gamma$ and the Riemann zeta function $\zeta$ as in ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)). For every $s\in\mathbb C$ with $\Re s>1$, $$\int_1^\infty g_1(y)y^{-s-1}\,dy=-\frac{\zeta'(s)/\zeta(s)+1/(s-1)+1-(1+\gamma)s}{s(s-1)}.$$
