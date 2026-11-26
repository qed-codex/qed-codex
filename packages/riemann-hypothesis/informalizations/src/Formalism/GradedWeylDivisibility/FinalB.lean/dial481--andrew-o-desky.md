---
{
  "module": "src/Formalism/GradedWeylDivisibility/FinalB.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.hwInClosed",
    "Formalism.GradedWeylDivisibility.hwLine"
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

## A nonzero row-stable subspace contains the highest-weight polynomial

[Theorem REP.0206](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.hwInClosed/)

Let $0\le n\le r$ be integers and let $\nu=(\nu_1,\ldots,\nu_n)$ be a weakly decreasing list of nonnegative integers. Use the dual Weyl module $\nabla_\nu(\mathbb Q)$, the row coefficient operators $D_{ab}^{(k)}$ and the highest-weight polynomial $v_\nu$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in $r\times n$ variables.

Let $M\subseteq\nabla_\nu(\mathbb Q)$ be a nonzero rational vector subspace satisfying $$D_{ab}^{(k)}(M)\subseteq M\qquad(1\le a,b\le r,\ k\ge0).$$ Then $$v_\nu\in M.$$

## The highest-weight line in a polynomial dual Weyl module

[Theorem REP.0278](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.hwLine/)

Let $K$ be an infinite field, let $0\le n\le r$ be integers, and let $\nu=(\nu_1,\ldots,\nu_n)$ be a weakly decreasing list of nonnegative integers. Use the module $\nabla_\nu(K)$, the operators $D_{ab}^{(k)}$ and the highest-weight polynomial $v_\nu$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)).

If $f\in\nabla_\nu(K)$ satisfies $$D_{ab}^{(k)}f=0\qquad(1\le a<b\le r,\ k\ge1),$$ then $$f=cv_\nu\qquad\text{for some }c\in K.$$
