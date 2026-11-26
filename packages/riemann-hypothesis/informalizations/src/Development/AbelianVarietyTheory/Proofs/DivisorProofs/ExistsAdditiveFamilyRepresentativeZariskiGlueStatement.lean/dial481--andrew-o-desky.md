---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAdditiveFamilyRepresentativeZariskiGlueStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_additiveFamily_representative_zariski_glue"
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

## Zariski gluing of representatives for additive line bundles

[Theorem AV.1566](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_additiveFamily_representative_zariski_glue/)

Let $A\to S$ be an abelian scheme. For an $S$-scheme $T$, call a line bundle $N$ on $A\times_ST$ additive if, for every $S$-scheme $Y$ and maps $a,a':Y\to A$, $t:Y\to T$, $$(a+a',t)^*N\simeq(a,t)^*N\otimes(a',t)^*N.$$ Suppose $S=\bigcup_{i\in I}U_i$ is an open cover and, for each $i$, additive line bundles over $U_i$ are represented by a scheme $B_i\to U_i$ with a universal additive line bundle. Assume $B_i\to U_i$ is proper, smooth of relative dimension $g_i\ge0$, and geometrically connected.

There are an $S$-scheme $B$ and an additive line bundle $P$ on $A\times_SB$ such that every additive $N$ on $A\times_ST$ is isomorphic to $(1_A\times x)^*P$ for a unique $S$-map $x:T\to B$. For every $i$, $B\times_SU_i\to U_i$ is proper, smooth of relative dimension $g_i$, and geometrically connected.
