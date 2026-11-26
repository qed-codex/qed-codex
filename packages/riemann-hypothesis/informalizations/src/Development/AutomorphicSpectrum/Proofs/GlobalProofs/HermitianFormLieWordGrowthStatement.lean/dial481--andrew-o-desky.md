---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/HermitianFormLieWordGrowthStatement.lean",
  "declarations": [
    "GlobalTheory.T.hermitian_form_lie_word_growth"
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

## Factorial growth bound for words in Lie operators

[Theorem REP.1310](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitian_form_lie_word_growth/)

Let $M$ be a complex vector space with a positive-definite Hermitian form $Q$, linear in its second variable, and put $\|u\|_Q=\sqrt{\operatorname{Re}Q(u,u)}$. Let $d\ge0$ and $X_1,\ldots,X_d\in\operatorname{End}_{\mathbb C}(M)$. Assume there are constants $c_{ij\ell}\in\mathbb C$ and $A\ge0$ such that $$[X_i,X_j]=\sum_{\ell=1}^d c_{ij\ell}X_\ell,\qquad |2\operatorname{Re}Q(X_i u,u)|\le A\operatorname{Re}Q(u,u)\quad(u\in M).$$ Let $V\subset M$ be a finite-dimensional complex subspace preserved by $\sum_iX_i^2$. There is $C>0$ such that for every $m\ge0$, every $i_1,\ldots,i_m\in\{1,\ldots,d\}$, and every $u\in V$, $$\|X_{i_1}\cdots X_{i_m}u\|_Q\le C^{m+1}m!\,\|u\|_Q.$$
