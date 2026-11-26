---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeTransference/Poisson.lean",
  "declarations": [
    "PI.Tr.poissonGauss"
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

## Poisson summation for translated lattice Gaussians

[Theorem ANT.0474](https://andrewodesky.com/rh/lean/PI.Tr.poissonGauss/)

Let $E$ be a real inner-product space of dimension $d<\infty$ and let $\Lambda\subset E$ be a full discrete lattice. Put $$\Lambda^*=\{y\in E:\langle x,y\rangle\in\mathbb Z\text{ for all }x\in\Lambda\}.$$ For every $t>0$ and $v\in E$, the Gaussian sums over $\Lambda$ and $\Lambda^*$ below converge absolutely. There is $c>0$, depending on $\Lambda$, such that for all such $t,v$, $$\sum_{x\in\Lambda}e^{-\pi t\|x+v\|^2}=ct^{-d/2}\sum_{y\in\Lambda^*}e^{-\pi\|y\|^2/t}\cos(2\pi\langle y,v\rangle).$$
