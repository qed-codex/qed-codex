---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ChiGen.lean",
  "declarations": [
    "GlobalTheory.ThetaInversion.inversion"
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

## Inversion formula for the square of a theta function

[Theorem THETA.1363](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaInversion.inversion/)

Let $g\ge0$, $a,b\in\mathbb R^g$, $z\in\mathbb C^g$, and let $\tau$ be a symmetric complex $g\times g$ matrix with positive-definite imaginary part. Put $$\theta[a,b](z,\tau)=\sum_{m\in\mathbb Z^g}\exp\!\left(2\pi i\left[\tfrac12(m+a)^t\tau(m+a)+(m+a)^t(z+b)\right]\right).$$ Then $$\theta[a,b](\tau^{-1}z,-\tau^{-1})^2 =(-i)^g\det(\tau)\,e^{2\pi i z^t\tau^{-1}z}\,e^{4\pi i a^tb}\,\theta[b,-a](z,\tau)^2.$$
