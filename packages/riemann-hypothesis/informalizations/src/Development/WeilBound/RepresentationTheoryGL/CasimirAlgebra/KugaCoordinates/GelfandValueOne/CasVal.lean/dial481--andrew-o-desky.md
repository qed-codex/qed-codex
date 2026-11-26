---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/KugaCoordinates/GelfandValueOne/CasVal.lean",
  "declarations": [
    "PositivityTheory.Rg.Cz.J.casVal_holds"
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

## Linear and quadratic Casimir values from a quantum determinant

[Theorem REP.1606](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Cz.J.casVal_holds/)

Let $M$ be a complex vector space, $n\ge0$, and $E_{ij}\in\operatorname{End}_{\mathbb C}(M)$ for $0\le i,j<n$ satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ Define the ordered quantum determinant $$Q(u)=\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\prod_{j=0}^{n-1}\bigl(\delta_{\pi(j),j}(u-j)\,\mathrm{id}_M+E_{\pi(j),j}\bigr),$$ where factors are multiplied in increasing $j$. If $\lambda_0,\ldots,\lambda_{n-1}\in\mathbb C$ satisfy $Q(u)=\prod_j(u+\lambda_j)\,\mathrm{id}_M$ for all $u\in\mathbb C$, then $$\sum_iE_{ii}=\left(\sum_{k=0}^{n-1}(\lambda_k+k)\right)\mathrm{id}_M,$$ $$\sum_{i,j}E_{ij}E_{ji}=\left(\sum_{k=0}^{n-1}\left[(\lambda_k+\tfrac{n-1}{2})^2-(\tfrac{n-1}{2}-k)^2\right]\right)\mathrm{id}_M.$$
