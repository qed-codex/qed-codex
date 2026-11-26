---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/GlRelOfCanonicalCommutationRelationsStatement.lean",
  "declarations": [
    "GlobalTheory.T.glRel_of_canonicalCommutationRelations"
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

## General linear Lie relations from canonical commutation relations

[Theorem ALG.1002](https://andrewodesky.com/rh/lean/GlobalTheory.T.glRel_of_canonicalCommutationRelations/)

Let $A$ be a unital ring and $n,m\ge0$. Suppose $x_{ia},d_{ia}\in A$ satisfy $$[x_{ia},x_{jb}]=[d_{ia},d_{jb}]=0,\qquad[d_{jb},x_{ia}]=\delta_{ij}\delta_{ab}1.$$ Set $$E_{ij}=\sum_{a=1}^m x_{ia}d_{ja},\qquad F_{ab}=-\sum_{i=1}^n x_{ib}d_{ia}.$$ Each family satisfies the general linear Lie relations: $$[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj},\qquad [F_{ab},F_{cd}]=\delta_{bc}F_{ad}-\delta_{da}F_{cb}.$$
