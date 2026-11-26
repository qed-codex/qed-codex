---
{
  "module": "src/Development/WeilBound/CoreStatements/MinimalPrimeDimensions/ChowDegreeSection.lean",
  "declarations": [
    "ChowFormHeightComparison₂.CF.V.chowDegreeSection"
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

## Chow degree and a hyperplane divisor cycle

[Theorem AG.1379](https://andrewodesky.com/rh/lean/ChowFormHeightComparison%E2%82%82.CF.V.chowDegreeSection/)

Let $F$ be a perfect field, $n,e\ge0$, and $I\subset F[X_1,\ldots,X_n]$ a homogeneous prime ideal not containing all coordinate variables. Assume $$\dim F[X_1,\ldots,X_n]/I=e+2.$$ Let $u=(u_i)\in F^n$ and $\ell_u=\sum_i u_iX_i\notin I$. Put $A=F[X_1,\ldots,X_n]$ and $J=I+(\ell_u)$. Let $W$ range over the minimal primes of $J$ for which some $X_i\notin W$, and put $$m_W=\operatorname{length}_{A_W}(A_W/JA_W),$$ viewed as a natural number, with infinite length assigned zero. Then $$\deg_{\mathrm{Chow}}(I;e+2)=\sum_Wm_W\deg_{\mathrm{Chow}}(W;e+1).$$
