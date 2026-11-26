---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Window.lean",
  "declarations": [
    "UpperTheory.V.Win.window"
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

## An interval avoiding finitely many intermediate exponents

[Theorem ANT.1309](https://andrewodesky.com/rh/lean/UpperTheory.V.Win.window/)

Let $R\ge0$ be an integer, let $0<\eta\le C$, let $X>1$, and let $E\subset\mathbb N$ be a finite set with $|E|\le R$. Put $$J=2^{R+2}(C/\eta)^R.$$ There is $Y\in\mathbb R$ such that $$X^{1/J}\le Y,\qquad Y^2\le X,$$ and, simultaneously for every $x\in[Y,Y^2]$ and every $e\in E$, $$e\le x^C\quad\Longrightarrow\quad e\le x^\eta.$$
