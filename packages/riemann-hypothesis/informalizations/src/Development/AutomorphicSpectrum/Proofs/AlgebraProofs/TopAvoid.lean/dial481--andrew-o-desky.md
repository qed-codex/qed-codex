---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/TopAvoid.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Giv.topAvoid"
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

## Multihomogeneous forms avoiding finitely many relevant prime ideals

[Theorem ALG.1657](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Giv.topAvoid/)

Let $R$ be a commutative ring, $J$ a finite set, and $I_j$ a finite set of variables for each $j\in J$. Give $$B=R[X_{ji}:j\in J,\ i\in I_j]$$ the grading in which every $X_{ji}$ has degree $1$ in block $j$ and degree $0$ in all other blocks. Let $\mathcal W$ be a finite family of prime multihomogeneous ideals of $B$ such that, for every $W\in\mathcal W$ and every block $j$, at least one variable $X_{ji}$ is outside $W$. There exists $d_0\in\mathbb N^J$ such that, for every componentwise $d\ge d_0$, there is a multihomogeneous polynomial $s\in B$ of degree $d$ with $$s\notin W\qquad(W\in\mathcal W).$$
