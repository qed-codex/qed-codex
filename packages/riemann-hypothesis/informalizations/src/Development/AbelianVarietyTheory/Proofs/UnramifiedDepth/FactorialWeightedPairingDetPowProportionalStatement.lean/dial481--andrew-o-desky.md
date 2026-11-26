---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/FactorialWeightedPairingDetPowProportionalStatement.lean",
  "declarations": [
    "GlobalTheory.T.factorialWeightedPairing_detPow_proportional"
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

## A proportionality identity for determinant powers

[Theorem ALG.0794](https://andrewodesky.com/rh/lean/GlobalTheory.T.factorialWeightedPairing_detPow_proportional/)

Let $C$ be a field of characteristic zero and $n,M,Y\in\mathbb N$ with $M\le Y$. Write $\Delta=\det(X_{ij})\in C[X_{ij}:1\le i,j\le n]$. Use $[P,R]=[P,R]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)). For every homogeneous polynomial $Q$ of degree $nM$, $$[\Delta^Y,\Delta^{Y-M}Q]\,[\Delta^M,\Delta^M] =[\Delta^M,Q]\,[\Delta^Y,\Delta^Y].$$
