---
{
  "module": "src/Development/WeilBound/ThetaLifts/SphericalLattices/ExistsIsUnitAddMul.lean",
  "declarations": [
    "PositivityTheory.Sph.orbit"
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

## Mutual integral matrix containment gives an invertible change of rows

[Theorem ALG.1504](https://andrewodesky.com/rh/lean/PositivityTheory.Sph.orbit/)

Let $k$ be a nonarchimedean local field with valuation ring $\mathcal O$, let $n,d\ge0$, $t\in k$, and $Y,Y'\in M_{n,d}(k)$. Suppose there are $A,B\in M_n(\mathcal O)$ and $Z,Z'\in M_{n,d}(\mathcal O)$ such that $$Y=AY'+tZ,\qquad Y'=BY+tZ'.$$ Then there are $U\in\mathrm{GL}_n(\mathcal O)$ and $Z_0\in M_{n,d}(\mathcal O)$ with $$Y=UY'+tZ_0.$$
