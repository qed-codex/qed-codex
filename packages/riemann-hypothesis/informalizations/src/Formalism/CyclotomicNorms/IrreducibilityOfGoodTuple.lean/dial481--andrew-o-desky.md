---
{
  "module": "src/Formalism/CyclotomicNorms/IrreducibilityOfGoodTuple.lean",
  "declarations": [
    "Formalism.CyclotomicNorms.restriction"
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

## An irreducibility criterion for restriction to a normal subgroup

[Theorem REP.0518](https://andrewodesky.com/rh/lean/Formalism.CyclotomicNorms.restriction/)

Let $G$ be a group, $k$ a field, $V$ a $k$-vector space with basis $e_1,\ldots,e_N$, and $\rho:G\to\operatorname{GL}_k(V)$ irreducible. Let $H\triangleleft G$ have finite solvable quotient, and let $I\le H$. Suppose $N\ge8$ and there are functions $c_i:G\to k$ such that $$\rho(y)e_i=c_i(y)e_i\qquad(y\in I),$$ with $c_i|_I\ne c_j|_I$ whenever $i\ne j$. Suppose $\varphi\in G$ normalizes $I$ and there is a permutation $\pi\in S_N$ satisfying $$c_{\pi(i)}(y)=c_i(\varphi^{-1}y\varphi)\qquad(y\in I).$$ If there is a prime $p$ with $N<2p$, $p+3\le N$, and a cycle of length $p$ in $\pi$, then $\rho|_H$ is irreducible.
