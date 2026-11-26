---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ResultantDerivativeNeZero.lean",
  "declarations": [
    "GlobalTheory.PencilDisc.exists_poly_noSquare"
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

## A polynomial excluding repeated linear factors after specialization

[Theorem ALG.1032](https://andrewodesky.com/rh/lean/GlobalTheory.PencilDisc.exists_poly_noSquare/)

Let $F$ be a characteristic-zero field, $D,N\ge0$, $\delta\ge1$, and let $f$ be a polynomial over $F$ in $D+1$ blocks of $N$ variables, homogeneous of degree $\delta$ in every block. Assume $f$ remains irreducible over an algebraic closure of $F$.

There is a nonzero polynomial $Q$ in $D$ blocks of $N$ variables over $F$, of total degree at most $2D\delta^2$, with this property: for every field extension $K/F$ and every $s=(s_1,\ldots,s_D)\in(K^N)^D$ with $Q(s)\ne0$, the polynomial $$g(Z)=f(s_1,\ldots,s_D,Z)$$ is nonzero, and no square of a nonzero linear form $\sum_{j=1}^Ny_jZ_j$ over $K$ divides $g$.
