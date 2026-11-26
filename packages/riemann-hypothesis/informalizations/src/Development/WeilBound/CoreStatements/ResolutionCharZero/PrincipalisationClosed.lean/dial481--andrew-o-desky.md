---
{
  "module": "src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationClosed.lean",
  "declarations": [
    "PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed"
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

## Principalization on a smooth projective variety

[Theorem AG.0139](https://andrewodesky.com/rh/lean/PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed/)

Let $Y$ be an integral smooth projective variety of dimension $d$ over a characteristic-zero field $k$, and let $\mathcal I\subseteq\mathcal O_Y$ be a nonzero ideal sheaf. The ideal may be the unit ideal. There are an integral smooth projective $k$-variety $Y'$ of dimension $d$ and a morphism $\pi:Y'\to Y$, obtained by a finite sequence of blow-ups with smooth centers lying over $\operatorname{Supp}(\mathcal O_Y/\mathcal I)$, such that $\pi$ is an isomorphism off that support. Moreover, $\mathcal I\mathcal O_{Y'}$ is an effective Cartier ideal whose reduced support is a simple normal-crossing divisor: $$\mathcal I\mathcal O_{Y'}=\mathcal O_{Y'}(-D)\quad\text{for an effective Cartier divisor }D.$$
