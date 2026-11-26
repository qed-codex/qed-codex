---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FischerDecompositionFockNoncompactPartsStatement.lean",
  "declarations": [
    "GlobalTheory.T.fischerDecomposition_fockNoncompactParts"
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

## Three Fischer decompositions of homogeneous Fock polynomials

[Theorem THETA.1176](https://andrewodesky.com/rh/lean/GlobalTheory.T.fischerDecomposition_fockNoncompactParts/)

Let $p,q,r,s,d\ge0$. Put $I=\{1,\ldots,p\}\sqcup\{1,\ldots,q\}$ and $J=\{1,\ldots,r\}\sqcup\{1,\ldots,s\}$, with the two blocks labeled $+$ and $-$. On $\mathcal P=\mathbb C[z_{ac}:(a,c)\in I\times J]$, set $L_{ac}=\partial_{ac}$, $R_{ac}=z_{ac}$ for matching block signs, and $L_{ac}=z_{ac}$, $R_{ac}=-\partial_{ac}$ otherwise. Define the complex-linear matrix actions by $$D_1(E_{ab})=\sum_{c\in J}\left(R_{ac}L_{bc}+\tfrac12\delta_{ab}\right),\qquad D_2(E_{ce})=\sum_{a\in I}\left(R_{ac}L_{ae}+\tfrac12\delta_{ce}\right).$$ For any operator $D$, write $D^+,D^-$ for the parts increasing and decreasing homogeneous degree by two. Let $\mathfrak p_1,\mathfrak p_2$ be the spaces of matrices with zero diagonal blocks on $I,J$, respectively, and set $$\mathcal H_i=\{P:D_i(Z)^-P=0\ \text{for all }Z\in\mathfrak p_i\},\quad \mathcal R_{i,d}=\operatorname{span}_{\mathbb C}\{D_i(Z)^+Q:Z\in\mathfrak p_i,\ Q\in\mathcal P_d\},$$ where $\mathcal P_j$ denotes the degree-$j$ homogeneous subspace. Then $$\mathcal P_{d+2}=(\mathcal P_{d+2}\cap\mathcal H_1)+\mathcal R_{1,d} =(\mathcal P_{d+2}\cap\mathcal H_2)+\mathcal R_{2,d} =(\mathcal P_{d+2}\cap\mathcal H_1\cap\mathcal H_2)+(\mathcal R_{1,d}+\mathcal R_{2,d}).$$
