---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsSatakeParamTrivialBoundUnitaryGLStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_satakeParam_trivialBound_unitaryGL"
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

## A two-sided Satake bound for a unitary spherical eigenvector

[Theorem REP.0625](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_satakeParam_trivialBound_unitaryGL/)

Let $E$ be a number field, $w$ a finite place, $E_w$ its completion, $q_w$ its residue cardinality, and $n\ge0$. Let $\rho$ be a unitarisable complex representation of $\operatorname{GL}_n(E_w)$. Suppose $0\ne x$ is fixed by $K=\operatorname{GL}_n(\mathcal O_{E_w})$ and is an eigenvector for every element of the spherical Hecke algebra.

There is a multiset $B$ of $n$ nonzero complex numbers such that, for every uniformizer $\varpi$ and every $0\le j\le n$, $$T_jx=q_w^{j(n-j)/2}e_j(B)x,$$ and every $\beta\in B$ satisfies $$|\beta|\le q_w^{(n-1)/2},\qquad |\beta^{-1}|\le q_w^{(n-1)/2}.$$
