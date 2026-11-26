---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean",
  "declarations": [
    "Deduction.G",
    "Deduction.Gchi",
    "Deduction.ramp"
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

## Regularized smoothed character sums

[Definition / hypothesis ANT.D088](https://andrewodesky.com/rh/lean/Deduction.Gchi/)

For positive integers $n$, let $\Lambda(n)=\log p$ if $n=p^k$ for a prime $p$ and an integer $k\ge1$, and let $\Lambda(n)=0$ otherwise. Let $\gamma$ be Euler's constant. For a Dirichlet character $\chi$ of positive integer modulus, write $L(s,\chi)$ for the meromorphic continuation of the Dirichlet series $\sum_{n\ge1}\chi(n)n^{-s}$, initially defined for $\Re s>1$, and write $(L'/L)(s,\chi)=L'(s,\chi)/L(s,\chi)$. If $\chi$ is nonprincipal, then $L(1,\chi)\ne0$ by ([Dirichlet nonvanishing on and to the right of one](https://andrewodesky.com/rh/lean/Deduction.charFamily_LFunction_ne_zero_of_one_le_re/)).

For a nonprincipal Dirichlet character $\chi$ of positive integer modulus and a real number $y>0$, define $$g_\chi(y)=\sum_{1\le n\le y}\Lambda(n)\chi(n)(y/n-1)+y\frac{L'}L(1,\chi).$$ For the principal character of modulus $1$, define $$g_1(y)=\sum_{1\le n\le y}\Lambda(n)(y/n-1)-y\log y+(1+\gamma)y\qquad(y>0).$$ Both sums run over positive integers; they are empty when $0<y<1$. The $L$-function of the principal character of modulus $1$ is the Riemann zeta function $\zeta(s)$.
