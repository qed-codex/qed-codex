---
{
  "module": "src/Development/AutomorphicArithmetic/MeanSquareBounds/IndDrop.lean",
  "declarations": [
    "QH.ind_drop"
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

## Extending the identity for a primitive quadratic twist

[Theorem ANT.0167](https://andrewodesky.com/rh/lean/QH.ind_drop/)

Let $B,H,N\ge1$ be integers, let $q$ be an odd prime with $q\nmid B$, let $\xi$ be a complex Dirichlet character modulo $B$, and let $\chi$ be a primitive complex Dirichlet character modulo $N$. Suppose $$\chi(n)=\xi(n)\left(\frac nq\right)\qquad\text{for every }n\in\mathbb N\text{ with }(n,H)=1,$$ where the parenthesized symbol is the Jacobi symbol. Then $$\chi(n)=\xi(n)\left(\frac nq\right)\qquad\text{for every }n\in\mathbb N\text{ with }(n,Bq)=1.$$
