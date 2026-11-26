---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/CliffordSemidirectPrimeIndexIrreducibleCharacterStatement.lean",
  "declarations": [
    "GlobalTheory.T.clifford_semidirect_primeIndex_irreducibleCharacter"
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

## Characters on a coset of a prime-index semidirect product

[Theorem REP.0786](https://andrewodesky.com/rh/lean/GlobalTheory.T.clifford_semidirect_primeIndex_irreducibleCharacter/)

Let $G$ and $\Gamma$ be finite groups, let $\varphi:\Gamma\to\operatorname{Aut}(G)$ be an action, and suppose $|\Gamma|$ is prime. Fix $s\in\Gamma\setminus\{1\}$ and an irreducible complex character $\chi$ of $G\rtimes_\varphi\Gamma$. Then either $$\chi(g,s)=0\quad\text{for every }g\in G,$$ or $\chi|_G$ is irreducible and $$\sum_{g\in G}|\chi(g,s)|^2=|G|.$$
