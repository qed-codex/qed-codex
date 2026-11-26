---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HasPolyhedralCoverBalancedFormsCMFieldStatement.lean",
  "declarations": [
    "GlobalTheory.T.hasPolyhedralCover_balancedForms_CMField"
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

## Finite polyhedral cover for balanced forms

[Theorem ALG.1716](https://andrewodesky.com/rh/lean/GlobalTheory.T.hasPolyhedralCover_balancedForms_CMField/)

Let $E$ be a CM number field unramified over its maximal real subfield. Fix a prime $d_0\equiv7\pmod{16}$, $r,w_0\in\mathcal O_E$ with $r^2=-d_0$ and $2w_0=1+r$, and a complex number $r_0$ with $r_0^2=-d_0$. Denote complex conjugation on $\mathcal O_E$ by $a\mapsto\bar a$. Let $X$ be a finite projective $\mathcal O_E$-module. A real-valued $\mathbb Z$-bilinear form $B$ is balanced if it is symmetric and $$B(ax,y)=B(x,\bar a y).$$ Consider the forms obtained by pulling back a positive-definite balanced form along a surjective $\mathcal O_E$-linear map from $X$ to a projective module.

There are finitely many finite lists $(P_{j,i})_i$ of symmetric, positive-semidefinite, integer-valued $\mathbb Z$-bilinear forms on $X$ such that every such $B$ satisfies $$B(ex,ey)=\sum_i c_iP_{j,i}(x,y)$$ for some $\mathcal O_E$-linear automorphism $e$ of $X$, some list $j$, and nonnegative real numbers $c_i$.
