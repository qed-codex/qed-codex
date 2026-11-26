---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/FockModels/TransposeWords/TransposeWordsProofs/FockPairingRowAction.lean",
  "declarations": [
    "Formalism.L2.G.Model.TS.fock_pairing_row_action"
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

## Transpose adjointness for row substitutions in the Fock pairing

[Theorem ALG.0325](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fock_pairing_row_action/)

Let $R$ be a commutative ring, $r,n\ge0$ integers, and $P,Q\in R[X_{aj}:1\le a\le r,\ 1\le j\le n]$. Use $[\ ,\ ]=[\ ,\ ]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)).

For $g\in M_r(R)$, put $R_g=A_g$, the row substitution of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)). Then $$[R_gP,Q]=[P,R_{g^t}Q].$$

For $1\le a,b\le r$ and $k\in\mathbb N$, let $D_{ab}^{(k)}$ be the divided row operator of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)). Then $$[D_{ab}^{(k)}P,Q]=[P,D_{ba}^{(k)}Q],$$ including when $a=b$.
