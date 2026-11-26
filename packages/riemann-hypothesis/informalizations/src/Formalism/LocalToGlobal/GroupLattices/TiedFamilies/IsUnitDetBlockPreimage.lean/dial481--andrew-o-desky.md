---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/TiedFamilies/IsUnitDetBlockPreimage.lean",
  "declarations": [
    "Formalism.L2.G.eq_zero_of_blocks"
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

## A polynomial vanishing on every invertible block tuple is zero

[Theorem ALG.1748](https://andrewodesky.com/rh/lean/Formalism.L2.G.eq_zero_of_blocks/)

Fix $p,O,K,w$, the local fields and maps, and the integers and rows subject to the base-ring and place conditions of ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)). Denote the number of places by $n_V$, and put $m=m_0$, $r=r_0$. Let $$Q\in\mathbb C[X_{v,s,a,b}:0\le v<n_V,\ 0\le s<n_v,\ 0\le a,b\le m].$$ If $Q((Z_{v,s})_{a,b})=0$ for every tuple of matrices $Z_{v,s}\in\operatorname{GL}_{m+1}(\mathbb C)$, then $Q=0$.
