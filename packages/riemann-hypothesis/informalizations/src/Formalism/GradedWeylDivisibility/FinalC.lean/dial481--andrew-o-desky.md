---
{
  "module": "src/Formalism/GradedWeylDivisibility/FinalC.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.standardMonomialSpanDomain"
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

## Initial-column minors span a dual Weyl polynomial space

[Theorem REP.1289](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.standardMonomialSpanDomain/)

Let $B$ be a commutative integral domain, let $r,n\ge0$ be integers, and let $\nu=(\nu_1,\ldots,\nu_n)\in\mathbb N^n$. Write $X=(X_{ij})$ for an $r\times n$ matrix of independent variables, and let $V_\nu=\nabla_\nu(B)$ be the polynomial dual Weyl module defined in ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)). Then $V_\nu$ is spanned over $B$ by all products $$\prod_{a=1}^{K}\det\bigl(X_{I_a(i),j}\bigr)_{1\le i,j\le s_a},$$ where $K\ge0$, $0\le s_a\le n$, each $I_a:\{1,\ldots,s_a\}\to\{1,\ldots,r\}$ is any map, and $$\nu_j=\#\{a:j\le s_a\}\qquad(1\le j\le n).$$
