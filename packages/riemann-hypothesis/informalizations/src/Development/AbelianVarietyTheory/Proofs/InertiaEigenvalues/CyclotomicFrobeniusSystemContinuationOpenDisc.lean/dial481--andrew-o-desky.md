---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CyclotomicFrobeniusSystemContinuationOpenDisc.lean",
  "declarations": [
    "GlobalTheory.Cyc.Cont.continuation_abstract"
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

## Coefficient bounds for a contracting power series system

[Theorem PHT.1092](https://andrewodesky.com/rh/lean/GlobalTheory.Cyc.Cont.continuation_abstract/)

Let $K$ be an ultrametric normed field, $J$ a finite set, $I$ any set, $\sigma:I\to I$, and $\gamma:K[[X]]\to K[[X]]$ a $K$-algebra endomorphism. For $r>0$ and $f\in K[[X]]$, set $$B_r(f)=\sup_{n\ge0}|[X^n]f|r^n\in[0,+\infty].$$ Assume $\gamma(X)$ has zero constant term and, for some real $\lambda<1$, $$|[X^n]\gamma(X)|r^n\le\max(\lambda,r)r\qquad(n\ge0,\ 0<r<1).$$ Let $W_i,P_i,D_i\in M_J(K[[X]])$ satisfy $$W_i=P_i\,\gamma(W_{\sigma(i)})\,D_i,$$ where $\gamma$ is applied entrywise. Suppose every entry of $P_i,D_i$ has finite $B_r$ for every $0<r<1$, and every entry of every $W_i$ has finite $B_\rho$ for one common $\rho>0$. Then every entry of every $W_i$ has finite $B_r$ for every $0<r<1$.
