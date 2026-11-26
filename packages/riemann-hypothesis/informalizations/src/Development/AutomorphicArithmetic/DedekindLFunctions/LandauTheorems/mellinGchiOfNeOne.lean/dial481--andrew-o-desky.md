---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiOfNeOne.lean",
  "declarations": [
    "Deduction.mellin_Gchi_of_ne_one"
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

## Mellin transform of a smoothed character sum

[Theorem ANT.0134](https://andrewodesky.com/rh/lean/Deduction.mellin_Gchi_of_ne_one/)

Let $\chi$ be a nonprincipal Dirichlet character of positive modulus, and use $g_\chi$ from ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)). For $\Re s>1$, $$\int_1^\infty g_\chi(y)y^{-s-1}\,dy=-\frac{(L'/L)(s,\chi)-s(L'/L)(1,\chi)}{s(s-1)}.$$
