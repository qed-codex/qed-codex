---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJASSnRepPolyFinish.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.Core.TC.polynomial_finish_holds"
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

## A polynomial whose squared modulus is a pure even power

[Theorem ALG.0770](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutMP.JA.SSn.Rep.Core.TC.polynomial_finish_holds/)

Let $q\in\mathbb C[T]$, $n\ge0$, and $a,C\in\mathbb R$. If $$|q(x)|^2=C(x-a)^{2n}\qquad\text{for every real }x>a,$$ then there is $c\in\mathbb C$ such that $$q(T)=c(T-a)^n.$$
