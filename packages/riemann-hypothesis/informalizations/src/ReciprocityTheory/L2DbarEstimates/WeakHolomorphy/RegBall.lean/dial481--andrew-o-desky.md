---
{
  "module": "src/ReciprocityTheory/L2DbarEstimates/WeakHolomorphy/RegBall.lean",
  "declarations": [
    "ReciprocityTheory.L2DbarEstimates.C.reg"
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

## A weakly holomorphic function has a holomorphic representative

[Theorem ALG.0417](https://andrewodesky.com/rh/lean/ReciprocityTheory.L2DbarEstimates.C.reg/)

Let $\Omega\subseteq\mathbb C^n$ be open and let $u:\mathbb C^n\to\mathbb C$ be locally integrable on $\Omega$. Suppose that for every smooth compactly supported $g:\mathbb C^n\to\mathbb C$ with support contained in $\Omega$, and every $v\in\mathbb C^n$, $$\int_\Omega u(z)\bigl(D_{\mathbb R}g(z)(iv)-iD_{\mathbb R}g(z)(v)\bigr)\,dz=0.$$ There is $U:\mathbb C^n\to\mathbb C$ holomorphic on $\Omega$ such that $u=U$ almost everywhere on $\Omega$.
