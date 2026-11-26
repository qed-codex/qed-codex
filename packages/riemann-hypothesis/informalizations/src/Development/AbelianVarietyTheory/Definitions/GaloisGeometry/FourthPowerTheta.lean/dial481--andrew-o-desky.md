---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FourthPowerTheta.lean",
  "declarations": [
    "GlobalTheory.ThLoc.LocJets.jets_linear"
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

## Integral derivatives descend from a fourfold tensor

[Theorem PHT.0971](https://andrewodesky.com/rh/lean/GlobalTheory.ThLoc.LocJets.jets_linear/)

Let $K$ be an ultrametric normed field of characteristic zero, let $I,J$ be finite sets, and let $T\in K[[X_i:i\in I]]$. For a matrix $A=(A_{ij})$, write $A^*T=T((\sum_jA_{ij}Y_j)_{i\in I})$, and put $$T^{\otimes4}=\prod_{a=1}^4T((X_{a,i})_{i\in I}).$$ Let $\gamma$ be a matrix indexed by $\{1,2,3,4\}\times I$ in both directions. Suppose every factorial-weighted coefficient of $\gamma^*(T^{\otimes4})$ has norm at most one. Let $M\in K^{I\times J}$ and $C\in K^{(\{1,2,3,4\}\times I)\times(\{1,2,3,4\}\times J)}$ satisfy $|C_{wx}|\le1$ and $$\sum_w\gamma_{(a,i),w}C_{w,(b,j)}=\begin{cases}M_{ij},&a=b,\\0,&a\ne b.\end{cases}$$ Then every factorial-weighted coefficient of $M^*T$ has norm at most one.
