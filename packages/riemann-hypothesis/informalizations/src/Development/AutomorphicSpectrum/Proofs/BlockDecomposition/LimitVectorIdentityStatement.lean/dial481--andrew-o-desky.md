---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LimitVectorIdentityStatement.lean",
  "declarations": [
    "GlobalTheory.T.limit_vector_identity"
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

## Hecke eigenvectors under limits of induction parameters

[Theorem REP.1392](https://andrewodesky.com/rh/lean/GlobalTheory.T.limit_vector_identity/)

Assume the following discrete-spectrum admissibility assertion: over every CM number field, the vectors of any discrete automorphic subspace with a prescribed open finite level and finite-dimensional archimedean type span a finite-dimensional space. Fix a CM number field $E$, ranks $a,b\ge0$, and a finite index set $I$.

For each rank choose a fixed binary induction expression with leaves given by discrete automorphic spaces and complex determinant-twist exponents. A rank-zero leaf is required to be the full rank-zero function space with exponent zero. At a node of ranks $r,s$, use the source's induced function space with additional twists $s/2,-r/2$ on the two children, and retain its finite vectors. Let $A_j,B_j$ be the resulting spaces when the leaf exponents vary with $j\in\mathbb N$, with the trees and underlying leaf spaces fixed. Suppose every leaf exponent converges, and all limiting exponents have real part zero; write $A_\infty,B_\infty$ for the limiting spaces.

Fix open finite levels $K_a,K_b$, finite-dimensional spaces of functions $W_a,W_b$ on the two maximal compact groups, and a countable set $\mathcal C$ of operators on $I$-tuples given by finite sums of finite-adelic right translations: $(Tf)_i(x)=\sum_{j,g}c_{ij,g}f_j(xg)$, with each coefficient family finitely supported. For every $j$, suppose there is a nonzero tuple $f_j=(f_{j,i})_{i\in I}$ with each component in the span of products from $A_j,B_j$, fixed at finite level $K_a\times K_b$ and having archimedean type in the span of products from $W_a,W_b$. Suppose $$Tf_j=\lambda_j(T)f_j\quad(T\in\mathcal C),\qquad\lambda_j(T)\longrightarrow\lambda_\infty(T).$$ Then a nonzero tuple $F$ with the same levels and types exists in the span of products from $A_\infty,B_\infty$, with $$TF=\lambda_\infty(T)F\qquad(T\in\mathcal C).$$
