---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnramifiedLocalFormulaStatement.lean",
  "declarations": [
    "GlobalTheory.T.unramified_local_formula"
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

## An unramified Hermitian representation-density formula

[Theorem THETA.0458](https://andrewodesky.com/rh/lean/GlobalTheory.T.unramified_local_formula/)

Let $(R,\sigma,\varpi,q,\varepsilon)$ satisfy the ring conditions below. Let $0\le n\le m$ and let $S\in M_m(R)$ and $T\in M_n(R)$ be $\sigma$-Hermitian with unit determinants. Put $R_k=R/(\varpi^k)$, and write $X^*=\sigma(X)^t$. Let $N_k$ be the number of matrices $X\in M_{m,n}(R_k)$ satisfying $X^*SX=T$, and let $H_k$ be the image in $M_n(R_k)$ of the $\sigma$-Hermitian matrices over $R$. Then $$\lim_{k\to\infty}\frac{N_k\,|H_k|}{|M_{m,n}(R_k)|}=\prod_{i=0}^{n-1}\left(1-\left(\frac{\varepsilon}{q}\right)^{m-i}\right).$$
