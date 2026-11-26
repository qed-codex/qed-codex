---
{
  "module": "src/ReciprocityTheory/L2DbarEstimates/WeakHolomorphy/ExtWeak.lean",
  "declarations": [
    "ReciprocityTheory.L2DbarEstimates.C.extWeak",
    "ReciprocityTheory.L2DbarEstimates.C.extWeak_of_smooth"
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

## Weak holomorphy across the zero set of a holomorphic function

[Theorem AG.0362](https://andrewodesky.com/rh/lean/ReciprocityTheory.L2DbarEstimates.C.extWeak/)

Let $n\ge0$, $\Omega\subseteq\mathbb C^n$ be open, and $F,u:\mathbb C^n\to\mathbb C$. Assume $F$ is holomorphic on $\Omega$, $u$ is holomorphic on $\Omega\setminus Z(F)$, and $$\int_{\Omega\setminus Z(F)}|u(z)|^2\,dz<\infty.$$ Extend $u|_{\Omega\setminus Z(F)}$ by zero to a function $\widetilde u$ on $\mathbb C^n$. Then $\widetilde u$ is locally integrable on $\Omega$ and, for every smooth compactly supported $g:\mathbb C^n\to\mathbb C$ with support in $\Omega$ and every $v\in\mathbb C^n$, $$\int_\Omega\widetilde u(z)\bigl(Dg(z)[iv]-iDg(z)[v]\bigr)\,dz=0.$$ Here $Dg$ is the real differential and $Z(F)=\{z:F(z)=0\}$.
