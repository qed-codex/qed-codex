---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/ExistsSquareRootCharacter.lean",
  "declarations": [
    "UpperTheory.exists_square_root_character"
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

## Square roots of characters congruent to one

[Theorem PHT.1302](https://andrewodesky.com/rh/lean/UpperTheory.exists_square_root_character/)

Let $\mathcal O$ be a commutative local ring, complete for the powers of its maximal ideal $\mathfrak m$, with $2\in\mathcal O^\times$. Let $\Gamma$ be a group with a topology, and let $\mu:\Gamma\to\mathcal O^\times$ be a homomorphism. Assume $\mu(g)\equiv1\pmod{\mathfrak m}$ for every $g$, and that for every $N\ge0$ the map $g\mapsto\mu(g)\bmod\mathfrak m^N$ is locally constant.

There is a homomorphism $\eta:\Gamma\to\mathcal O^\times$ such that, for every $g$, $$\eta(g)^2=\mu(g),\qquad\eta(g)\equiv1\pmod{\mathfrak m},\qquad \mu(g)=1\Longrightarrow\eta(g)=1.$$ For every $N\ge0$, reduction of $\eta$ modulo $\mathfrak m^N$ is locally constant.
