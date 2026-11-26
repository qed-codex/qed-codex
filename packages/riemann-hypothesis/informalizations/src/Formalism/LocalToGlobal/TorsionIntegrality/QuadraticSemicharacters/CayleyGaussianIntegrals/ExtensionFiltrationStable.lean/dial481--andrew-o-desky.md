---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/ExtensionFiltrationStable.lean",
  "declarations": [
    "Formalism.L2.Th1.H.characterIntegral"
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

## Vanishing of a nontrivial dual-lattice character integral

[Theorem THETA.0795](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.characterIntegral/)

Let $V$ be a finite-dimensional complex normed vector space, $\mu$ an additive Haar measure for its Borel structure, and $H$ a positive-definite Hermitian form on $V$. Let $\Lambda\subseteq V$ be an additive subgroup and $D$ a measurable additive fundamental domain for $\Lambda$ with respect to $\mu$. For every nonzero $v\in V$ satisfying $$\operatorname{Im}H(v,\lambda)\in\mathbb Z\qquad(\lambda\in\Lambda),$$ one has $$\int_D\exp\bigl(2\pi i\operatorname{Im}H(v,z)\bigr)\,d\mu(z)=0.$$
