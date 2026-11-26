---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/QuantumDeterminantCommute/QuantumDeterminantCommutes.lean",
  "declarations": [
    "QmCapCommW.quantum_determinant_commutes"
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

## Commutativity of shifted quantum determinants

[Theorem REP.0895](https://andrewodesky.com/rh/lean/QmCapCommW.quantum_determinant_commutes/)

Let $A$ be a complex algebra, not necessarily commutative, and let $E_{ab}\in A$ for $0\le a,b<n$ satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ For $u\in\mathbb C$, define the ordered product $$Q(u)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma) \prod_{j=0}^{n-1}\bigl(E_{\sigma(j),j}+\delta_{\sigma(j),j}(u-j)\bigr),$$ where factors are multiplied in increasing order of $j$ and scalars act through $\mathbb C\to A$. Then $Q(u)Q(v)=Q(v)Q(u)$ for every $u,v\in\mathbb C$.
