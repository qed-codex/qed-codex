---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/LevelCharts/SelfDualPI.lean",
  "declarations": [
    "Formalism.L2.G.self_dual_lattice_at"
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

## Local self-duality away from an integer bounding the dual

[Theorem ANT.0936](https://andrewodesky.com/rh/lean/Formalism.L2.G.self_dual_lattice_at/)

Let $E/F$ be an extension of number fields, $\sigma:E\to E$ an $F$-algebra homomorphism, $J\in M_n(E)$, and $L\subseteq E^n$ a finitely generated $\mathcal O_E$-module. Put $$h(x,y)=\sum_{i,j}\sigma(x_i)J_{ij}y_j.$$ Suppose $h(L,L)\subseteq\mathcal O_E$ and there is $T\ge0$ such that $$h(L,y)\subseteq\mathcal O_E\quad\Longrightarrow\quad Ty\in L\qquad(y\in E^n).$$ For every nonzero prime $v$ of $\mathcal O_F$ with $T\notin v$, the completed lattice $L_v$ is self-dual for the extended pairing: $$L_v=\{y\in(F_v\otimes_FE)^n:h_v(L_v,y)\subseteq O_{E,v}\}.$$
