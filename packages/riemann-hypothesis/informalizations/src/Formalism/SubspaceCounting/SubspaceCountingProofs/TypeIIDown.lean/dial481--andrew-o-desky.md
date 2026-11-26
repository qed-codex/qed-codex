---
{
  "module": "src/Formalism/SubspaceCounting/SubspaceCountingProofs/TypeIIDown.lean",
  "declarations": [
    "Formalism.G0.countAboveRangeCodimFormula"
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

## Counting subspaces above the range of a linear map

[Theorem ALG.0456](https://andrewodesky.com/rh/lean/Formalism.G0.countAboveRangeCodimFormula/)

Let $F$ be a finite field of cardinality $q$ and let $f:P\to Q$ be linear, with $\dim_FP=N$ and $\dim_FQ=N+g$, where $N,g\ge0$. Write $b_d(K)$ for the number of $d$-dimensional subspaces of a finite $F$-vector space $K$. For every $j\ge0$, $$\#\{U\le Q:\operatorname{im}f\subseteq U,\ \dim_FU+j=N+g\} =\sum_{\ell=0}^j q^{(j-\ell)\max(g-\ell,0)}{g\brack\ell}_q\,b_{j-\ell}(\ker f).$$ Here ${g\brack\ell}_q$ is the Gaussian binomial coefficient, taken to be zero for $\ell>g$.
