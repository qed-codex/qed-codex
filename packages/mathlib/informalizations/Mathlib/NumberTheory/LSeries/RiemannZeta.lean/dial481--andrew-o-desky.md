---
{
  "module": "Mathlib/NumberTheory/LSeries/RiemannZeta.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "0df444a360eaa60ab8c11dca51a86af692955474",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Zeta values and functional equation

[Theorem ANT.1739](https://andrewodesky.com/rh/s/z1-zeta-functional-equation.html)

Let $\zeta(s)$ denote the meromorphic continuation of $\sum_{n\ge1}n^{-s}$ from $\Re s>1$. If $\chi$ is the unique Dirichlet character modulo $1$, then its Dirichlet $L$-function satisfies $$L(s,\chi)=\zeta(s),\qquad \zeta(0)=-\frac12.$$ Let $\Gamma$ denote Euler's gamma function. For every $w\in\mathbb C$ such that $w\notin\{0,-1,-2,\ldots\}$ and $w\ne1$, $$\zeta(1-w)=2\,(2\pi)^{-w}\,\Gamma(w)\,\cos\!\left(\frac{\pi w}{2}\right)\,\zeta(w),$$ where $(2\pi)^{-w}=\exp(-w\log(2\pi))$.
