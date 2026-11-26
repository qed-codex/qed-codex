---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/ThetaZeroTwoComplexMult.lean",
  "declarations": [
    "Formalism.L2.Th1.B.LCm.quadratic_two_adic_holds",
    "Formalism.L2.Th1.B.LCm.roots_two_adic_holds"
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

## A 2-adic quadratic has one unit root and one nonunit root

[Theorem PHT.0955](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.LCm.quadratic_two_adic_holds/)

Let $T,N\in\mathbb Z$, with $T$ odd and $N$ even. There are $b,b'\in\mathbb Z_2$ such that $$b+b'=T,\qquad bb'=N,\qquad |b|_2=1,\qquad |b'|_2<1.$$

## Two-adic images of quadratic conjugate roots

[Theorem PHT.0981](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.LCm.roots_two_adic_holds/)

Let $\iota:\mathbb C\simeq\mathbb C_2$ be a field isomorphism, let $\alpha\in\mathbb C$, and let $T,N\in\mathbb Z$ satisfy $$\alpha+\overline\alpha=T,\qquad\alpha\overline\alpha=N,\qquad T\text{ odd},\quad N\text{ even}.$$ There are $b,b'\in\mathbb Z_2$ with $|b|_2=1$ and $|b'|_2<1$ such that either $$(\iota(\alpha),\iota(\overline\alpha))=(b,b')\quad\text{or}\quad(\iota(\alpha),\iota(\overline\alpha))=(b',b),$$ using the natural embeddings $\mathbb Z_2\subset\mathbb Q_2\subset\mathbb C_2$.
