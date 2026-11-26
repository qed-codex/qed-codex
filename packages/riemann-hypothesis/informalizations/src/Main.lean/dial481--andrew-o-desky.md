---
{
  "module": "src/Main.lean",
  "declarations": [
    "LFunction_eq_zero_re",
    "LFunction_ne_zero_of_half_lt_re",
    "riemannHypothesis"
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

## Riemann hypothesis for Dirichlet L-functions

[Theorem ANT.1.0001](https://andrewodesky.com/rh/lean/riemannHypothesis/)

Let $N\ge1$ be an integer and let $\chi$ be a complex Dirichlet character modulo $N$. Denote by $\chi_0$ the principal character modulo $N$, equal to $1$ on integers coprime to $N$ and $0$ on the remaining integers. Write $L(s,\chi)$ for the meromorphic continuation of $\sum_{n\ge1}\chi(n)n^{-s}$ from $\Re s>1$. For every $s\in\mathbb C$, $$\Re s>\frac12,\qquad (\chi\ne\chi_0\ \text{or}\ s\ne1) \quad\Longrightarrow\quad L(s,\chi)\ne0.$$

Consequently, $$L(s,\chi)=0,\qquad0<\Re s<1\quad\Longrightarrow\quad\Re s=\frac12.$$ Let $\zeta(s)$ denote the meromorphic continuation of $\sum_{n\ge1}n^{-s}$. If $\zeta(s)=0$, $s\ne1$, and $s$ is not one of the trivial zeros $-2,-4,-6,\ldots$, then $\Re s=1/2$.
