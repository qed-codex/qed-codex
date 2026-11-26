---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/NewtonBoundPosAndNewtonStep.lean",
  "declarations": [
    "GlobalTheory.newtonBound_pos_and_newtonStep"
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

## A logarithmic threshold and a binomial-transform valuation window

[Theorem PHT.0940](https://andrewodesky.com/rh/lean/GlobalTheory.newtonBound_pos_and_newtonStep/)

For integers $\ell\ge5$, $i,n\ge1$, put $$S_0=\left\lceil64n^2\bigl(i+3+3\log_\ell(n+1)\bigr)\right\rceil.$$ For every integer $s\ge S_0$, $$0<\frac{s}{8}-n^2\bigl(3\log_\ell n+2\log_\ell s+i+3\bigr).$$ Also, let $C$ be any field with an additive valuation $v:C\to\mathbb R\cup\{+\infty\}$, let $S\ge1$, and let $a_0,a_1,\ldots\in C$ satisfy $a_0=1$ and $v(a_s)>0$ for every $s\ge S$. Every interval $[Y_0,Y_0+S)$ with integer $Y_0\ge0$ contains an integer $y$ for which $$v\!\left(\sum_{s=0}^y\binom ys a_s\right)\le0.$$
