---
{
  "module": "src/Formalism/PeriodIntegrals/UnimodLocStd.lean",
  "declarations": [
    "PI.ULS.CmOK",
    "PI.ULS.IsSelfDual",
    "PI.ULS.cmL",
    "PI.ULS.cmPair",
    "PI.ULS.cmTheta",
    "PI.ULS.relIdx",
    "PI.ULS.scalePair",
    "PI.ULS.stdH",
    "PI.ULS.stdLat"
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

## Self-dual lattices from an imaginary quadratic period pair

[Definition / hypothesis ANT.D010](https://andrewodesky.com/rh/lean/PI.ULS.CmOK/)

Let $a,d>0$ be integers and $b,c\in\mathbb Z$ satisfy $$4ac=b^2+d,\qquad a\text{ odd},\qquad d\text{ prime},\quad d\equiv7\pmod8.$$ Put $\theta=(b+i\sqrt d)/2$, where $\sqrt d$ is the positive real square root. Fix $\lambda\in\mathbb C^\times$ and let $L=\lambda(a\mathbb Z+\theta\mathbb Z)$, with ordered periods $(\lambda a,\lambda\theta)$. Its area $\operatorname{area}(L)$ is defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)).

For a finite set $I$, put $L_0=L^I$ and $H(x,y)=\sum_i x_i\bar y_i/\operatorname{area}(L)$ on $\mathbb C^I$. Let $\Lambda\subseteq\mathbb C^I$ be an additive subgroup satisfying $$\Lambda=\{x:\operatorname{Im}H(x,y)\in\mathbb Z\text{ for all }y\in\Lambda\},\qquad\theta\Lambda\subseteq\Lambda.$$ Assume both relative indices $[L_0:L_0\cap\Lambda]$ and $[\Lambda:L_0\cap\Lambda]$ are finite.
