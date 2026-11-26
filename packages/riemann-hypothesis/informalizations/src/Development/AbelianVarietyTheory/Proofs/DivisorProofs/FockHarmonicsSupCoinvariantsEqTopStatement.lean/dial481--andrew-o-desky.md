---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FockHarmonicsSupCoinvariantsEqTopStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockHarmonics_sup_coinvariants_eq_top"
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

## Fock harmonics span every scalar coinvariant quotient

[Theorem REP.0556](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockHarmonics_sup_coinvariants_eq_top/)

Let $p,q,r,s\ge0$ and $x\in\mathbb C$. Let $I$ have $p$ positive and $q$ negative indices, let $J$ have $r$ positive and $s$ negative indices, and put $\mathcal F=\mathbb C[z_{ij}:i\in I,j\in J]$. Define the oscillator action $D$ and its first-factor action $D_1$ by the conventions below. Let $A^-$ denote the component of an operator $A$ lowering total polynomial degree by two, and put $$\mathcal H=\{f\in\mathcal F:D_1(X)^-f=0\text{ for every matrix }X\text{ supported in the off-diagonal }p\times q\text{ and }q\times p\text{ blocks}\},$$ $$C_x=\operatorname{span}_{\mathbb C}\{D_1(X)f-x\operatorname{tr}(X)f:X\in M_{p+q}(\mathbb C),\ f\in\mathcal F\}.$$ Then $$\operatorname{span}_{\mathbb C}\mathcal H+C_x=\mathcal F.$$
