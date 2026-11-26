---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/SpectralSobolevSecondOrder.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.CutSE.spectral_sobolev_second_order"
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

## A local estimate using first and mixed second derivatives

[Theorem ALG.0653](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.CutSE.spectral_sobolev_second_order/)

Let $z_0\in\mathbb C$ and $\delta>0$. There is a real constant $C$ with the following property for every real normed vector space $E$ and functions $f,f_x,f_y,f_{xy}:\mathbb C\to E$.

On the closed disc $D=\{z:|z-z_0|\le2\delta\}$, suppose $f$ is real Fréchet differentiable with $$df_z(h)=\operatorname{Re}(h)f_x(z)+\operatorname{Im}(h)f_y(z).$$ Suppose also that, for every $z\in D$, there is $f_{yy}(z)\in E$ such that $f_y$ is real Fréchet differentiable at $z$ with $$d(f_y)_z(h)=\operatorname{Re}(h)f_{xy}(z)+\operatorname{Im}(h)f_{yy}(z).$$ Assume $f_x,f_{xy}$ are continuous on $D$. Then, for $|z-z_0|<\delta$, $$\|f(z)\|^2\le C\int_D\bigl(\|f\|^2+\|f_x\|^2+\|f_y\|^2+\|f_{xy}\|^2\bigr)\,dA.$$
