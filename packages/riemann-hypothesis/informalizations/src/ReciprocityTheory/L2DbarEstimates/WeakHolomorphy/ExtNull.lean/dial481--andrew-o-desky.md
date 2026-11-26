---
{
  "module": "src/ReciprocityTheory/L2DbarEstimates/WeakHolomorphy/ExtNull.lean",
  "declarations": [
    "ReciprocityTheory.L2DbarEstimates.C.ext"
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

## Holomorphic extension across a zero locus

[Theorem AG.0262](https://andrewodesky.com/rh/lean/ReciprocityTheory.L2DbarEstimates.C.ext/)

Let $n\ge0$, let $\Omega\subseteq\mathbb C^n$ be open, and let $F:\mathbb C^n\to\mathbb C$ be holomorphic on $\Omega$. Write $Z=\{z\in\Omega:F(z)=0\}$. Suppose $u:\mathbb C^n\to\mathbb C$ is holomorphic on $\Omega\setminus Z$ and $|u|^2$ is Lebesgue integrable there. There exists a function $U:\mathbb C^n\to\mathbb C$ holomorphic on $\Omega$ such that $$U(z)=u(z)\qquad(z\in\Omega\setminus Z).$$
