---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/PAreaMultiplicityWeight.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.AreaMultiplicityWeight.proof"
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

## The weighted area formula with fibre multiplicity

[Theorem AG.1370](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.AreaMultiplicityWeight.proof/)

Let $E$ be a finite-dimensional real normed vector space with its Borel measurable structure and additive Haar measure $\mu$. Let $A\subseteq E$ be measurable, $f:E\to E$, and $L_x:E\to E$ continuous real-linear maps such that $L_x$ is a derivative of $f$ within $A$ at every $x\in A$. Put $$N_A(y)=\#\{x\in A:f(x)=y\}\in[0,\infty],$$ with every infinite fibre assigned value $+\infty$. Then $N_A$ is almost everywhere measurable for $\mu$, and for every measurable $g:E\to[0,\infty]$, $$\int_A g(f(x))\,|\det L_x|\,d\mu(x)=\int_E N_A(y)g(y)\,d\mu(y).$$ The determinant on the left is embedded in the extended nonnegative reals.
