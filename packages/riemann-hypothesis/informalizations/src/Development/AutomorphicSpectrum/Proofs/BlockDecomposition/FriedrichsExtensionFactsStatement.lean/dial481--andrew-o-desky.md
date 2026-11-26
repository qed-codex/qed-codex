---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FriedrichsExtensionFactsStatement.lean",
  "declarations": [
    "GlobalTheory.T.friedrichs_extension_facts"
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

## A bounded inverse for a positive symmetric operator

[Theorem REP.1229](https://andrewodesky.com/rh/lean/GlobalTheory.T.friedrichs_extension_facts/)

Let $H$ be a complex Hilbert space, $D\subset H$ a complex linear subspace, and $A:D\to H$ a complex-linear map. Suppose $$\langle Ax,y\rangle=\langle x,Ay\rangle,\qquad \|x\|^2\le\Re\langle Ax,x\rangle\quad(x,y\in D).$$ There exists a bounded complex-linear operator $R:H\to H$ with $R=R^*$, $\|R\|\le1$, and $R(Ax)=x$ for every $x\in D$. Moreover, $UR=RU$ for every bounded operator $U$ satisfying $U^*U=UU^*=1$ and the following two conditions: for each $x\in D$, there is $y\in D$ with $y=Ux$ and $Ay=U(Ax)$, and there is $z\in D$ with $z=U^*x$ and $Az=U^*(Ax)$.
