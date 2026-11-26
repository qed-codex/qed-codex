---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/WittFrameLocaliserOrders.lean",
  "declarations": [
    "Formalism.MainNotions.G.WittFrameLocaliserOrders.gauss_quotient_integral"
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

## Divisibility by a generic minor descends from the fraction field

[Theorem ALG.1094](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.WittFrameLocaliserOrders.gauss_quotient_integral/)

Let $R$ be a commutative domain, $I$ a finite set, $r\ge0$, and $A:\{1,\ldots,r\}\hookrightarrow I$ an injection. In $R[X_{ij}:i\in I,1\le j\le r]$ put $$\Delta_A=\det(X_{A(i),j})_{1\le i,j\le r}.$$ For every $n\ge0$ and polynomial $G$ over $R$, if $\Delta_A^n$ divides $G$ after extending coefficients to $\operatorname{Frac}R$, then it already divides $G$ over $R$.
