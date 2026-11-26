---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/CloudPropOfMapsBasis.lean",
  "declarations": [
    "Formalism.MainNotions.flipOneThree.Pf.latRetract"
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

## A retraction preserving lattices defined by bases

[Theorem ALG.0849](https://andrewodesky.com/rh/lean/Formalism.MainNotions.flipOneThree.Pf.latRetract/)

Let $\mathcal O$ be a discrete valuation domain with fraction field $K$. Let $V,V'$ be finite-dimensional $K$-vector spaces with chosen bases $(b_i)_{i\in I}$ and $(b'_j)_{j\in J}$ indexed by finite sets. Put $$L=\sum_{i\in I}\mathcal O b_i,\qquad L'=\sum_{j\in J}\mathcal O b'_j.$$ Let $\iota:V\to V'$ be $K$-linear and suppose $$\iota(v)\in L'\quad\Longleftrightarrow\quad v\in L\qquad(v\in V).$$ There is a $K$-linear map $r:V'\to V$ such that $$r\iota=\operatorname{id}_V,\qquad r(L')\subseteq L.$$
