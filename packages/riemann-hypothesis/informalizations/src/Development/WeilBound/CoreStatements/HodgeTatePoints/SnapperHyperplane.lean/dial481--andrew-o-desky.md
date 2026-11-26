---
{
  "module": "src/Development/WeilBound/CoreStatements/HodgeTatePoints/SnapperHyperplane.lean",
  "declarations": [
    "PositivityTheory.HtPt.Kra.interNumAdditive"
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

## Additivity of the intersection integer in a line bundle

[Theorem AG.1316](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Kra.interNumAdditive/)

Let $k$ be a field, $\Omega/k$ a field extension, $N\ge0$, and $x=(x_0,\ldots,x_N)\in\Omega^{N+1}$. Let $P\subset k[X_0,\ldots,X_N]$ be a homogeneous prime ideal containing the homogeneous vanishing ideal of $x$, with some $X_j\notin P$ and $$\dim(k[X_0,\ldots,X_N]/P)=n+1.$$ Let $L_1,\ldots,L_n,L',L''$ be line bundles on the projective closure of $[x]$, represented by compatible invertible fractional modules on its coordinate charts, and choose $1\le i\le n$. Write $I_P$ for the intersection integer on the subvariety defined by $P$. Then $$I_P(L_1,\ldots,L_{i-1},L'\otimes L'',L_{i+1},\ldots,L_n) =I_P(L_1,\ldots,L_{i-1},L',L_{i+1},\ldots,L_n) +I_P(L_1,\ldots,L_{i-1},L'',L_{i+1},\ldots,L_n).$$
