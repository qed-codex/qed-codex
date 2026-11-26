---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/FrobeniusFields/QuadEx.lean",
  "declarations": [
    "UpperTheory.V.Ws.quadEx"
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

## A quadratic character with prescribed splitting and sign

[Theorem AGR.0617](https://andrewodesky.com/rh/lean/UpperTheory.V.Ws.quadEx/)

Fix an algebraic closure $\Omega$ of $\mathbb Q$, a sign $s\in\{1,-1\}$, and a finite set $S$ of rational primes. There exist a rational prime $p\notin S$ and a character $$\eta:\operatorname{Gal}(\Omega/\mathbb Q)\longrightarrow\{1,-1\}$$ with open kernel of index two such that $\eta$ is unramified at every finite prime other than $p$, is nontrivial on inertia at $p$, is trivial on the decomposition group at every $q\in S$, and takes the value $s$ on every complex conjugation.
