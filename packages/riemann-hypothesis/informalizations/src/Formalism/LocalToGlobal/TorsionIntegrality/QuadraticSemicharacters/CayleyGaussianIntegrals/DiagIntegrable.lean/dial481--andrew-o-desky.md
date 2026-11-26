---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/DiagIntegrable.lean",
  "declarations": [
    "Formalism.L2.Th1.H.UC.kerPNonzero"
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

## Nonvanishing of a theta projection kernel

[Theorem THETA.0657](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.UC.kerPNonzero/)

Let $V$ be a finite-dimensional complex normed vector space and $H:V\times V\to\mathbb C$ a positive-definite Hermitian form, linear in its first variable. Let $\Lambda\subseteq V$ be a discrete additive subgroup spanning $V$ over $\mathbb R$, and assume $$\Lambda=\{x\in V:\operatorname{Im}H(x,y)\in\mathbb Z\text{ for all }y\in\Lambda\}.$$ Let $\alpha:V\to\mathbb C$ satisfy, for $x,y\in\Lambda$, $$\alpha(x)\in\{1,-1\},\qquad \alpha(x+y)=\alpha(x)\alpha(y)e^{\pi i\operatorname{Im}H(x,y)}.$$ Define $$P(z,w)=\sum_{x\in\Lambda}\alpha(x)\exp\!\left(\pi H(z+x,w)-\pi H(z,x)-\frac{\pi}{2}H(x,x)\right).$$ There exist $z,w\in V$ with $P(z,w)\ne0$.
