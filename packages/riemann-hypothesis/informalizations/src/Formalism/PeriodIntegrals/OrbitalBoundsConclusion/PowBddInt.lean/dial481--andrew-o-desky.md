---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/PowBddInt.lean",
  "declarations": [
    "power_bounded_integral"
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

## Bounded denominators of matrix powers force integral characteristic coefficients

[Theorem ALG.0367](https://andrewodesky.com/rh/lean/power_bounded_integral/)

Let $E$ be a number field and $\gamma\in\operatorname{Mat}_k(E)$. Suppose there is an integer $N>0$ such that $N(\gamma^n)_{ij}$ is integral over $\mathbb Z$ for every $n\ge0$ and all $i,j$. Then every coefficient of $\det(T-\gamma)$ is integral over $\mathbb Z$.
