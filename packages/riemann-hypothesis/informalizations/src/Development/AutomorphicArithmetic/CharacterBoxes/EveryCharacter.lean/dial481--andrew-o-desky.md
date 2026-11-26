---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean",
  "declarations": [
    "UpperTheory.EveryCharacter"
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

## Zero-freeness: no Dirichlet L-function vanishes in the half-plane Re s \> 1/2

[Definition / hypothesis ANT.D107](https://andrewodesky.com/rh/lean/UpperTheory.EveryCharacter/)

**Definition (zero-freeness).** For every integer $N\ge 1$, every Dirichlet character $\chi$ modulo $N$ and every $s\in\mathbb C$ with $\operatorname{Re}s>\tfrac12$, excluding the case in which $\chi$ is the trivial character modulo $N$ and $s=1$, $$L(s,\chi)\neq 0 .$$
