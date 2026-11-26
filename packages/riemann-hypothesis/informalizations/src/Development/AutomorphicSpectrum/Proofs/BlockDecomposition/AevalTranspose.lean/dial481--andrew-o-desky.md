---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AevalTranspose.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.TorusCh.exists_idem'"
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

## A polynomial projector onto an invariant subspace

[Theorem ALG.0571](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.TorusCh.exists_idem'/)

Let $K$ be a field, let $n\ge0$, and let $\gamma\in M_n(K)$ have separable characteristic polynomial. For every $\gamma$-invariant subspace $W\subseteq K^n$, there is $p\in K[T]$ such that $$p(\gamma)^2=p(\gamma),\qquad\operatorname{im}p(\gamma)=W.$$
