---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean",
  "declarations": [
    "Formalism.MainNotions.WeightDegreeSizes.secondComplement_of_split"
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

## Combining the two auxiliary-prime error sums

[Theorem ARAK.0174](https://andrewodesky.com/rh/lean/Formalism.MainNotions.WeightDegreeSizes.secondComplement_of_split/)

Fix the source's arithmetic size datum, with distinct auxiliary primes $g_0,g_1$, finite set $\mathcal V$ of finite places, residue characteristics $p_v$, weighted errors $e_{u,j,v}=[E_{u,j}(v)]_v$, $A_0=\sum_{t\in T}a_t$, and nonnegative budget $B_0$. Let $C_1,C_2\in\mathbb R$ with $C_1\ge0$. Suppose, for both $i=0,1$, every source index $u$ and every lift $1\le j\le m$, $$\left|\sum_{v\in\mathcal V:\,p_v=g_i}e_{u,j,v}-A_0\log g_i\right|\le C_1B_0,$$ and suppose $$\sum_{v\in\mathcal V:\,p_v\notin\{g_0,g_1\}}|e_{u,j,v}|\le C_2B_0.$$ Then, for all $u,j$ in these ranges, $$\left|\sum_{v\in\mathcal V}e_{u,j,v}-A_0\log(g_0g_1)\right|\le(2C_1+C_2)B_0,$$ $$\sum_{v\in\mathcal V:\,p_v\notin\{g_0,g_1\}}|e_{u,j,v}|\le(2C_1+C_2)B_0.$$
