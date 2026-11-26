---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NcardUnitCellsDirichletLZerosNearOneLe.lean",
  "declarations": [
    "GlobalTheory.ZeroCells.ncard_cells_le"
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

## Few unit height intervals containing zeros near one

[Theorem ANT.1301](https://andrewodesky.com/rh/lean/GlobalTheory.ZeroCells.ncard_cells_le/)

There is an absolute constant $C>0$ with the following property. Let $Q\ge3$ and let $T$ be any finite set of triples $(N,\chi,\rho)$, where $N\ge1$, $\chi$ is a primitive Dirichlet character modulo $N$, and $$N\le Q,\qquad L(\rho,\chi)=0,\qquad \Re\rho\ge\frac{399}{400},\qquad |\Im\rho|\le Q.$$ Then $$\#\{(N,\chi,\lfloor\Im\rho\rfloor):(N,\chi,\rho)\in T\}\le C Q^{1/8}.$$ Each triple $(N,\chi,j)$ records a character together with the unit interval $j\le\Im\rho<j+1$; repeated zeros in that interval count only once.
