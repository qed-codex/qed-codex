---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/VirtualCharacterCosetNormOneSingleStatement.lean",
  "declarations": [
    "GlobalTheory.T.virtualCharacter_coset_normOne_single"
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

## A norm-one virtual character on a prime cyclic coset

[Theorem REP.1043](https://andrewodesky.com/rh/lean/GlobalTheory.T.virtualCharacter_coset_normOne_single/)

Let $G$ be a finite group, $\Gamma$ a group of prime order, $\varphi:\Gamma\to\operatorname{Aut}(G)$ an action, and $s\in\Gamma\setminus\{1\}$. Let $X$ be a virtual complex character of $G\rtimes_\varphi\Gamma$. If $$\sum_{g\in G}|X(g,s)|^2=|G|,$$ then there are an irreducible complex character $\chi$ of $G\rtimes_\varphi\Gamma$ and $e\in\mathbb C$ such that $\chi|_G$ is irreducible and $$X(g,s)=e\chi(g,s)\qquad(g\in G).$$
