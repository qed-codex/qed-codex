---
{
  "module": "src/Formalism/SatakeDualWeyl/AdelicIwasawaHecke/Wlocal.lean",
  "declarations": [
    "Formalism.UG.P.wlocal_main"
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

## Stability of a Weyl polynomial module under an invertible row substitution

[Theorem REP.0937](https://andrewodesky.com/rh/lean/Formalism.UG.P.wlocal_main/)

Let $R$ be a commutative local ring, let $0\le n\le r$ be integers, and let $\nu=(\nu_1,\ldots,\nu_n)\in\mathbb N^n$. Use the module $W_\nu=\Delta_\nu(R)$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in a generic $r\times n$ matrix $X$.

Let $d,k\ge0$ satisfy $k+d=r$, and let $M,N\in M_r(R)$ satisfy $NM=1$. Suppose the first $k$ columns of $M$ are the corresponding standard coordinate columns. Then $$f(X)\in W_\nu\quad\Longrightarrow\quad f(MX)\in W_\nu.$$ No monotonicity assumption on $\nu$ is imposed.
