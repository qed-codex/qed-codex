---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/NonemptyMeasAndReps.lean",
  "declarations": [
    "GlobalTheory.JR.EtMeas.exists_selfDual"
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

## A self-dual measure over an ultrametric local field

[Theorem ANT.1060](https://andrewodesky.com/rh/lean/GlobalTheory.JR.EtMeas.exists_selfDual/)

Let $F$ be a nontrivially normed, locally compact ultrametric field. Let $\psi:F\to\mathbb C$ be an additive character satisfying $$\psi(a)=1\quad(|a|\le1),$$ and suppose there is $x\in F$ with $\psi(x)\ne1$ and $|xy|\le1$ for every $y\in F$ with $|y|<1$.

Let $V$ be a finite-dimensional $F$-vector space with its module topology and Borel measurable structure, and let $\beta:V\times V\to F$ be symmetric bilinear and nondegenerate. There is an additive Haar measure $\mu$ on $V$ which is self-dual for $\chi(x,y)=\psi(\beta(x,y))$.
