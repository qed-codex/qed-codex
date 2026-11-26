---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/DualModuleCocycles/IdemDiag.lean",
  "declarations": [
    "UpperTheory.V.Th.Coc.idemDiag"
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

## Diagonalization of rank-one orthogonal idempotents over a local ring

[Theorem ALG.0694](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.Coc.idemDiag/)

Let $O$ be a commutative local ring and $n\ge0$. Suppose $e_1,\ldots,e_n\in M_n(O)$ are complete orthogonal idempotents: $$e_i^2=e_i,\qquad e_ie_j=0\ (i\ne j),\qquad \sum_i e_i=1.$$ Assume $\operatorname{tr}(e_i)=1$ for every $i$. Then some $Q\in\operatorname{GL}_n(O)$ satisfies $$Q^{-1}e_iQ=E_{ii}\qquad(1\le i\le n).$$
