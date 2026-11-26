---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/ExistsSquareRootOfCharacterNearOne.lean",
  "declarations": [
    "UpperTheory.exists_square_root_of_character_near_one"
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

## A continuous square root of an l-adic character near one

[Theorem PHT.0656](https://andrewodesky.com/rh/lean/UpperTheory.exists_square_root_of_character_near_one/)

Let $\ell$ be an odd prime, let $\Gamma$ be a group with a topology, and let $\eta:\Gamma\to\overline{\mathbb Q}_\ell^{\times}$ be a continuous character satisfying $|\eta(g)-1|_\ell<1$ for every $g\in\Gamma$. There is a continuous character $\delta:\Gamma\to\overline{\mathbb Q}_\ell^{\times}$ such that $$\delta(g)^2=\eta(g),\qquad |\delta(g)-1|_\ell<1\qquad(g\in\Gamma).$$
