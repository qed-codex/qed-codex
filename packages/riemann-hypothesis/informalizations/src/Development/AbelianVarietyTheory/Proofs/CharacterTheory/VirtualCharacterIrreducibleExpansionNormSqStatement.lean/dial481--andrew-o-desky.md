---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CharacterTheory/VirtualCharacterIrreducibleExpansionNormSqStatement.lean",
  "declarations": [
    "GlobalTheory.T.virtualCharacter_irreducible_expansion_normSq"
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

## Irreducible expansion and norm of a virtual character

[Theorem REP.1300](https://andrewodesky.com/rh/lean/GlobalTheory.T.virtualCharacter_irreducible_expansion_normSq/)

Let $G$ be a finite group and let $\varphi:G\to\mathbb C$ be a virtual character, meaning an integral linear combination of characters of finite-dimensional complex representations. There is a finitely supported family of integers $(c_\chi)$, supported on irreducible complex characters of $G$, such that $$\varphi=\sum_\chi c_\chi\chi,\qquad \sum_{g\in G}|\varphi(g)|^2=|G|\sum_\chi c_\chi^2.$$

If $\sum_{g\in G}|\varphi(g)|^2=|G|$, then either $\varphi$ or $-\varphi$ is an irreducible character. Under the same equality, if $\varphi$ is itself the character of a representation, then $\varphi$ is irreducible and there is an integer $n\ge1$ with $\varphi(1)=n$.
