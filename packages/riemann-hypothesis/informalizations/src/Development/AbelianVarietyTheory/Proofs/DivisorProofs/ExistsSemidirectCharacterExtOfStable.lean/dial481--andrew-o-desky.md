---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemidirectCharacterExtOfStable.lean",
  "declarations": [
    "GlobalTheory.StableExt.exists_ext"
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

## Extension of an invariant character to a cyclic semidirect product

[Theorem REP.0720](https://andrewodesky.com/rh/lean/GlobalTheory.StableExt.exists_ext/)

Let $G$ be a finite group, let $\Gamma=\langle s\rangle$ be a finite cyclic group, and let $\varphi:\Gamma\to\operatorname{Aut}(G)$ be an action. Let $\chi:G\to\mathbb C$ be the character of a finite-dimensional complex representation. If $$\chi(\varphi(s)(g))=\chi(g)\qquad(g\in G),$$ there is a character $\widetilde\chi$ of a finite-dimensional complex representation of $G\rtimes_\varphi\Gamma$ whose restriction to $G$ is $\chi$.
