---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LubinTateIterateLimitCongruenceStatement.lean",
  "declarations": [
    "GlobalTheory.T.lubin_tate_iterate_limit_congruence"
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

## Compatible congruences for iterated Lubin–Tate polynomials

[Theorem PHT.1318](https://andrewodesky.com/rh/lean/GlobalTheory.T.lubin_tate_iterate_limit_congruence/)

Let $B$ be a commutative ring, $S\subset B$ a subring, $\varpi\in S$ a unit of $B$, and $F_0,F_1,\ldots$ ideals of $B$. Assume:

1. $F_0=B$, $F_{k+1}\subset F_k$, $F_aF_b\subset F_{a+b}$, and $\bigcap_kF_k=0$.
2. Whenever $x_{k+1}-x_k\in F_k$ for a sequence in $B$, there is $t\in B$ with $t-x_k\in F_k$ for every $k$.
3. For every sequence $s_n\in S$ there is $r\in S$ such that $r-\sum_{n<N}\varpi^ns_n\in\varpi^NS$ for all $N\ge0$.
4. For $x\in S$ and $k\ge0$, membership $x\in\varpi^aS+F_k$ for every $a\ge0$ implies $x\in F_k$.

Let $q\ge2$ be an integer with $q\in\varpi S$, and let $v_n\in S$ satisfy $v_{n+1}^q=v_n$. Define $f(X)=\varpi X+X^q$, and let $f^{\circ n}$ denote its $n$-fold composition. There is $Q\in S$ such that $$Q-f^{\circ n}(v_n)\in\varpi^{n+1}S\qquad(n\ge0).$$
