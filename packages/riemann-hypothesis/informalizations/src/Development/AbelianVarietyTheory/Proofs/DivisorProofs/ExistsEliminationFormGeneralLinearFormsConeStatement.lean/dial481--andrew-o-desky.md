---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsEliminationFormGeneralLinearFormsConeStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_eliminationForm_generalLinearForms_cone"
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

## An elimination form for linear sections of a cone

[Theorem AG.0790](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_eliminationForm_generalLinearForms_cone/)

Let $F$ be a field of characteristic zero, let $D,N,d\in\mathbb N$ with $D\ge1$, and let $I\subset F[X_1,\ldots,X_N]$ be a homogeneous prime ideal such that $$\dim F[X_1,\ldots,X_N]/I=D+1.$$ Let $g\notin I$ be homogeneous of degree $d$. There is a nonzero polynomial $Q\in F[S_{ij}:1\le i\le D,\ 1\le j\le N]$ with the following property. For every field extension $K/F$, matrix $s\in M_{D,N}(K)$ and nonzero vector $y\in K^N$, if $$a(y)=0\ (a\in I),\qquad g(y)=0,\qquad \sum_{j=1}^Ns_{ij}y_j=0\ (1\le i\le D),$$ then $Q(s)=0$.
