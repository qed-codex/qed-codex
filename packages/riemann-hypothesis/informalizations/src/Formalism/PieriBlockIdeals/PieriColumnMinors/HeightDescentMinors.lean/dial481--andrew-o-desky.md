---
{
  "module": "src/Formalism/PieriBlockIdeals/PieriColumnMinors/HeightDescentMinors.lean",
  "declarations": [
    "Formalism.CohomologicalDescent.HeightDescentMinors.general_basis_holds",
    "Formalism.CohomologicalDescent.HeightDescentMinors.r2_basis_holds"
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

## A power-series basis over the cyclotomic invariant parameter

[Theorem PHT.0698](https://andrewodesky.com/rh/lean/Formalism.CohomologicalDescent.HeightDescentMinors.r2_basis_holds/)

Let $l$ be an odd prime and $O$ a commutative $\mathbb Z_l$-algebra. Define $$\pi_0(X)=\prod_{\substack{d\in\mathbb Z_l\\d^{\,l-1}=1}}\bigl((1+X)^d-1\bigr)\in O[[X]],$$ where powers with $l$-adic exponents are binomial series mapped to $O$. For every $f\in O[[X]]$, there is a unique tuple $g_0,\ldots,g_{l-2}\in O[[X]]$ such that $$f(X)=\sum_{j=0}^{l-2}g_j(\pi_0(X))X^j.$$

## A basis over a power series substitution

[Theorem ALG.1101](https://andrewodesky.com/rh/lean/Formalism.CohomologicalDescent.HeightDescentMinors.general_basis_holds/)

Let $R$ be a commutative ring, $n\ge1$, and $w\in R[[X]]^\times$. Every $f\in R[[X]]$ has a unique representation $$f(X)=\sum_{j=0}^{n-1}g_j(w(X)X^n)X^j,\qquad g_j\in R[[X]].$$
