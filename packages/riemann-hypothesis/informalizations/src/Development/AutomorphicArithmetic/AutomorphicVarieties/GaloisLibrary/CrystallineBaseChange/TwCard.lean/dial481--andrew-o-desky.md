---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/CrystallineBaseChange/TwCard.lean",
  "declarations": [
    "UpperTheory.V.Br.twCard"
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

## A bound for the number of self-twists

[Theorem REP.0621](https://andrewodesky.com/rh/lean/UpperTheory.V.Br.twCard/)

Let $\Gamma$ be a group, $k$ a field, $n\ge0$, and $\rho:\Gamma\to\operatorname{GL}_n(k)$ an irreducible representation. If $S$ is a finite set of characters $\delta:\Gamma\to k^\times$ such that $\rho\simeq\rho\otimes\delta$ for every $\delta\in S$, then $$\#S\le n^2.$$ Here $(\rho\otimes\delta)(g)=\delta(g)\rho(g)$.
