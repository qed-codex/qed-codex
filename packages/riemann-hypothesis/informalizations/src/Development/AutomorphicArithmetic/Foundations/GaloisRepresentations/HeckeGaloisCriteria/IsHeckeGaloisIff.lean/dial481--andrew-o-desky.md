---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/IsHeckeGaloisIff.lean",
  "declarations": [
    "UpperTheory.GalC.etaJ_le"
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

## Projection defects under restriction of eigensystems

[Theorem ALG.0169](https://andrewodesky.com/rh/lean/UpperTheory.GalC.etaJ_le/)

Fix the source's arithmetic datum. At each local coefficient index $i$, let $X_i$ be its Hecke eigensystems, $Z_i^{\mathrm{good}}$ its good selected systems, and $Z_i$ its larger selected set. Choose a subset $X'_i\subseteq X_i$, retaining exactly those indices with $Z_i^{\mathrm{good}}\ne\varnothing$. Assume this is a good restriction in the sense below. Let $H>0$ be the supplied finite group order. For every $1\le j\le m$ and coefficient place $v$, $$\eta_j(v)\le\eta'_j(v)+\left(\sum_{i\in I(j,v)}\sum_{\pi\in Z_i^{\mathrm{good}}}m_{i,\pi}\right)v_{p_v}(H).$$ Here $\eta'_j(v)$ is the projection defect in the restricted datum, $m_{i,\pi}$ is the eigenspace multiplicity, $I(j,v)$ the local indices for lift $j$ and place $v$, and $p_v$ the residue prime. In particular, if the multiplicity sum is at most $d_j$, then $\eta_j(v)\le\eta'_j(v)+d_jv_{p_v}(H)$.
