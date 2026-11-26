---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean",
  "declarations": [
    "UpperTheory.FinalTheorems.everyCharacter",
    "UpperTheory.FinalTheorems.everyCharacter_of_row"
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

## Zero-freeness for all Dirichlet characters

[Theorem ANT.1.0002](https://andrewodesky.com/rh/lean/UpperTheory.FinalTheorems.everyCharacter/)

Let $N\ge1$ be an integer, let $\chi$ be a complex Dirichlet character modulo $N$, and let $s\in\mathbb C$. Then $$\Re s>\frac12,\qquad (\chi\ne1\ \text{or}\ s\ne1)\quad\Longrightarrow\quad L(s,\chi)\ne0.$$

## The main theorem with the existence of automorphic Galois representations as its hypothesis

[Theorem ANT.0003](https://andrewodesky.com/rh/lean/UpperTheory.FinalTheorems.everyCharacter_of_row/)

Assume the assertion of ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)). Then for every integer $N\ge1$, every complex Dirichlet character $\chi$ modulo $N$ and every $s\in\mathbb C$, $$\Re s>\frac12,\qquad (\chi\ne1\ \text{or}\ s\ne1)\quad\Longrightarrow\quad L(s,\chi)\ne0.$$
