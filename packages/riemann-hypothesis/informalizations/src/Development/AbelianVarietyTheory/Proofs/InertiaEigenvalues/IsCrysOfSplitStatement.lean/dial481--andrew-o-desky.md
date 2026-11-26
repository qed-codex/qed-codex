---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsCrysOfSplitStatement.lean",
  "declarations": [
    "GlobalTheory.T.isCrys_of_split_alt"
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

## Crystallinity from an invertible period matrix

[Theorem PHT.0588](https://andrewodesky.com/rh/lean/GlobalTheory.T.isCrys_of_split_alt/)

Fix the period data described below. Let $L/Q$ be a finite field extension, $V$ an $L$-vector space with its compatible $Q$-vector-space structure, and $\rho:G\to\operatorname{GL}_L(V)$ a representation. Suppose $e_1,\ldots,e_n$ is a $Q$-basis of $V$. If $W\in M_n(B)$ has invertible determinant and $$[\rho(g)]_e\,g(W)=W\qquad(g\in G),$$ where the first factor is mapped from $Q$ to $B$ and $g$ acts entrywise on $W$, then $$\dim_L(V\otimes_Q B)^G=[K_0:Q]\dim_L V.$$
