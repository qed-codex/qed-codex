---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/QuadraticSemicharacters/CayleyGaussianIntegrals/MatrixFormFourfoldBlockFirstBlockEmb.lean",
  "declarations": [
    "Formalism.L2.Th1.H.fourth_root"
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

## A fourth tensor root of a one-dimensional theta space

[Theorem THETA.0922](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.fourth_root/)

Let $I$ be finite, $V=\mathbb C^I$, $h\in M_I(\mathbb C)$, $\Lambda\subseteq V$ an additive subgroup, and $\alpha:V\to\mathbb C$ with $\alpha(0)=1$. Use $H=H_h$ and write $\Theta(H,\alpha,\Lambda)=\mathcal T(H,\alpha,\Lambda)$ for the theta space defined in ([Fourfold theta kernels and lattice intertwiners](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.StdData/)). On $V^4$, put $H^{(4)}(z,w)=\sum_{a=1}^4H(z_a,w_a)$ and $\alpha^{(4)}(x)=\prod_{a=1}^4\alpha(x_a)$. Suppose $P\ne0$ belongs to $\Theta(H^{(4)},\alpha^{(4)},\Lambda^4)$ and spans that space. Then there is $\theta\in\Theta(H,\alpha,\Lambda)$ with $$P(z_1,z_2,z_3,z_4)=\prod_{a=1}^4\theta(z_a).$$ For every such $\theta$, any other such root is $\zeta\theta$ for some $\zeta^4=1$, and every member of $\Theta(H,\alpha,\Lambda)$ is a scalar multiple of $\theta$.
