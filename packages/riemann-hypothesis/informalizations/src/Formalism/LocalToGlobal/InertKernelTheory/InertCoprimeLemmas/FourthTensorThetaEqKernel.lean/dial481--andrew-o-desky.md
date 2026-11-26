---
{
  "module": "src/Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FourthTensorThetaEqKernel.lean",
  "declarations": [
    "Formalism.L2.KerInert.AlgP.fourth_tensor_algebraic"
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

## Algebraicity descends from a fourth tensor power

[Theorem ALG.1055](https://andrewodesky.com/rh/lean/Formalism.L2.KerInert.AlgP.fourth_tensor_algebraic/)

Let $I$ be finite and let $\theta:\mathbb C^I\to\mathbb C$ be an entire function which is not identically zero. Put $$F(z_1,z_2,z_3,z_4)=\prod_{a=1}^4\theta(z_a),\qquad z_a\in\mathbb C^I.$$ If all Taylor coefficients of $F$ at the origin lie in one number field inside $\mathbb C$, then all Taylor coefficients of $\theta$ at the origin lie in one number field inside $\mathbb C$.
