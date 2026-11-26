---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/IrreducibleCapelliModules.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.branching_algebraic"
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

## An interlacing decomposition into irreducible Capelli eigenspaces

[Theorem REP.1077](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.branching_algebraic/)

Let $V$ be a finite-dimensional complex vector space, and let $E_{ab}\in\operatorname{End}_{\mathbb C}V$, $0\le a,b\le n$, satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ Assume $V\ne0$ and the only subspaces stable under every $E_{ab}$ are $0,V$. Let $\beta\in\mathbb C$ and integers $L_0>\cdots>L_n$ satisfy $$Q_{n+1}(u)=\prod_{j=0}^n(u+\beta+L_j)\,1_V\qquad(u\in\mathbb C),$$ where $Q_s$ uses the leading $s\times s$ block and the normalization below. For each integer tuple $M=(M_0,\ldots,M_{n-1})$ with $L_{j+1}<M_j\le L_j$, put $$V_M=\{v:Q_n(u)v=\prod_{j=0}^{n-1}(u+\beta+M_j)v\text{ for every }u\in\mathbb C\}.$$ Then $V=\bigoplus_M V_M$, every $V_M$ is nonzero, and every subspace of $V_M$ stable under the leading $n\times n$ operators is either $0$ or $V_M$.
