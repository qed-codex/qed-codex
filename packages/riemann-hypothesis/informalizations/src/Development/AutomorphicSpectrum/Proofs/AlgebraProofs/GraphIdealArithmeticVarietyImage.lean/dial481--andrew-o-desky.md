---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/GraphIdealArithmeticVarietyImage.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Giv.graphIdeal_isArithVar"
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

## Arithmetic graph ideals preserve dimension

[Theorem AG.1236](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Giv.graphIdeal_isArithVar/)

Let $K,K'$ be finite sets with finite coordinate sets $I_k,J_h$, and put $R=\mathbb Z[X_{k,i}]$. Let $P\subset R$ be a relevant multihomogeneous prime with $P\cap\mathbb Z=0$, $K\ne\varnothing$, and $\dim(R/P)=d+|K|$, where $d\ge0$. Relevant means that no entire coordinate block belongs to $P$.

For each $h\in K'$, let $(g_{h,j})_{j\in J_h}$ be integral multihomogeneous polynomials of one multidegree $\delta_h\in\mathbb N^K$, with at least one $g_{h,j}\notin P$. In $R[Y_{h,j}]$ define $$Q=\ker\bigl(R[Y_{h,j}]\longrightarrow(R/P)[T_h:h\in K'],\quad X_{k,i}\mapsto\overline X_{k,i},\quad Y_{h,j}\mapsto\overline g_{h,j}T_h\bigr).$$ Then $Q$ is a relevant multihomogeneous horizontal prime, $\dim(R[Y]/Q)=d+|K|+|K'|$, and $Q\cap R=P$.
