---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CompactGroupHaarExists.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.spherical_shell_integral"
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

## Integrability from polynomial sublevel-volume growth

[Theorem ALG.0350](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.spherical_shell_integral/)

Let $(X,\mu)$ be a measure space and $N:X\to\mathbb R$ measurable, with $N\ge1$ almost everywhere. Let $C,d,A\in\mathbb R$ satisfy $d\ge0$ and $A>d$. If $$\mu\{x:N(x)\le R\}\le\max(CR^d,0)\qquad(R\ge1),$$ then $$\int_X\max\bigl(N(x)^{-A},0\bigr)\,d\mu(x)<\infty.$$ The volume bound and integral are interpreted in the nonnegative extended real numbers; real powers have their usual meaning on the almost-everywhere positive base $N$.
