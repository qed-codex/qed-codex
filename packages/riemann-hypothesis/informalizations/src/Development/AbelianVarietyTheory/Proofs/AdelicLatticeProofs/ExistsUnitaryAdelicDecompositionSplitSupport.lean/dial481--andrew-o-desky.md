---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ExistsUnitaryAdelicDecompositionSplitSupport.lean",
  "declarations": [
    "GlobalTheory.UnRep.exists_rep_suppSplit"
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

## A unitary adelic factorization supported at split places

[Theorem ANT.0360](https://andrewodesky.com/rh/lean/GlobalTheory.UnRep.exists_rep_suppSplit/)

Let $E/F$ be a quadratic extension of number fields, $c\in\operatorname{Aut}_F(E)$ its nontrivial involution, and $G\in M_n(E)$ invertible with $c(G_{ij})=G_{ji}$. Put $$h(x,y)=\sum_{i,j}x_iG_{ij}c(y_j).$$ Let $L\subseteq E^n$ be a finitely generated $\mathcal O_E$-module spanning $E^n$, and $\widehat L$ its finite-adelic completion. For every $g\in U(h)(\mathbb A_{F,f})$ and integer $N\ge1$, there are $$\gamma\in U(h)(F),\qquad a,k\in U(h)(\mathbb A_{F,f})$$ such that $g=\gamma ak$, $a_v=1$ outside a finite set of places $v$ split in $E/F$ and not dividing $N$, and $$(k-1)\widehat L\subseteq N\widehat L,\qquad k^{-1}\widehat L\subseteq\widehat L.$$ Here $U(h)$ is the group preserving $h$; finite adelic matrices are regarded over $\mathbb A_{F,f}\otimes_FE$.
