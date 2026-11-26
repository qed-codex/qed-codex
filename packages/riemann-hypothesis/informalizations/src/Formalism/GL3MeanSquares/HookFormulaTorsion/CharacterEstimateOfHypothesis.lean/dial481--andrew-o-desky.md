---
{
  "module": "src/Formalism/GL3MeanSquares/HookFormulaTorsion/CharacterEstimateOfHypothesis.lean",
  "declarations": [
    "Formalism.HermitianLattices.ZeroFreeRegionGL2.gl2b2_thinIntegral",
    "Formalism.HermitianLattices.ZeroFreeRegionGL2.nonvanishing_of_hypothesis"
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

## A decaying bound for a weighted tail integral

[Theorem ANT.0705](https://andrewodesky.com/rh/lean/Formalism.HermitianLattices.ZeroFreeRegionGL2.nonvanishing_of_hypothesis/)

For every $\varepsilon,c,C>0$, there are $c'>0$ and $x_0\in\mathbb R$ such that the following holds for all $x\ge x_0$. Let $y,\lambda\in\mathbb R$ and $\psi:\mathbb R\to\mathbb C$ satisfy $$\frac{\exp(x^{\varepsilon/3})}{3}\le y,\qquad 1\le\lambda\le2x^{\varepsilon/5}(\log x)^2,$$ and, for every $u\ge y$, $$|\psi(u)|\le Cu(\log u+\lambda)^2 \exp\left(-\frac{c\log u}{\lambda+\sqrt{\log u}}\right).$$ Then $$\left|y\int_y^\infty\frac{\psi(u)}{u^2}\,du\right| \le y\exp(-c'x^{\varepsilon/8}).$$

## A stretched exponential bound for an integral tail

[Theorem ANT.1106](https://andrewodesky.com/rh/lean/Formalism.HermitianLattices.ZeroFreeRegionGL2.gl2b2_thinIntegral/)

For every $\varepsilon,c>0$ there are $c'>0$ and $x_0\in\mathbb R$ such that for all $x\ge x_0$ and real $V,\lambda$ with $$V\ge\tfrac12x^{\varepsilon/3},\qquad1\le\lambda\le2x^{\varepsilon/5}(\log x)^2,$$ the function $(v+\lambda)^2\exp(-cv/(\lambda+\sqrt v))$ is integrable on $(V,\infty)$ and $$\int_V^\infty(v+\lambda)^2\exp\!\left(-\frac{cv}{\lambda+\sqrt v}\right)\,dv\le\exp(-c'x^{\varepsilon/8}).$$
