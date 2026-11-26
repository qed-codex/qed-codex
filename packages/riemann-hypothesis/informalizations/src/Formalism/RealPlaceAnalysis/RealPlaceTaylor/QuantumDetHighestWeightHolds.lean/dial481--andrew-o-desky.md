---
{
  "module": "src/Formalism/RealPlaceAnalysis/RealPlaceTaylor/QuantumDetHighestWeightHolds.lean",
  "declarations": [
    "Formalism.REAL.quantumDetHighestWeight_holds"
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

## The quantum determinant on a highest-weight vector

[Theorem REP.0619](https://andrewodesky.com/rh/lean/Formalism.REAL.quantumDetHighestWeight_holds/)

Let $V$ be a complex vector space, $n\ge0$, and $E_{ab}\in\operatorname{End}_{\mathbb C}(V)$ for $0\le a,b<n$, with $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ Let $v\in V$ and $\nu_0,\ldots,\nu_{n-1}\in\mathbb C$ satisfy $$E_{aa}v=\nu_av,\qquad E_{ab}v=0\quad(a<b).$$ For $u\in\mathbb C$, define the ordered quantum determinant $$D(u)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{k=0}^{n-1}\bigl(E_{\sigma(k),k}+\delta_{\sigma(k),k}(u-k)\operatorname{id}_V\bigr),$$ where products are in increasing order of $k$. Then $$D(u)v=\prod_{k=0}^{n-1}(u-k+\nu_k)\,v.$$
