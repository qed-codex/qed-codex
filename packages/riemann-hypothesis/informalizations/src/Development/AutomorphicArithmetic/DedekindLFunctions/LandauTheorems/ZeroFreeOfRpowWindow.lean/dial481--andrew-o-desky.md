---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ZeroFreeOfRpowWindow.lean",
  "declarations": [
    "Deduction.zeroFree_of_rpow_window"
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

## Landau theorem on intervals

[Theorem ANT.1.0127](https://andrewodesky.com/rh/lean/Deduction.zeroFree_of_rpow_window/)

Let $J\ge0$ be an integer, let $\chi_1,\ldots,\chi_J$ be Dirichlet characters of positive integer moduli, each of them nonprincipal or of modulus $1$, and let $a_1,\ldots,a_J$ be positive real numbers. Let $\theta$, $\lambda$ and $C$ be real numbers with $0<\theta<1$ and $\lambda>1$. Write $g_\chi$ and $L(s,\chi)$ for the functions defined in ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)). Suppose that for every real number $Y_0\ge1$ there is a real number $Y\ge Y_0$ such that $$\sum_{i=1}^Ja_i\Re g_{\chi_i}(x)\le Cx^\theta\qquad\text{for every }x\in[Y,Y^\lambda].$$ Then, for every $i\in\{1,\ldots,J\}$, the meromorphic function $L(s,\chi_i)$ has no zero in the half-plane $\Re s>\theta$.
