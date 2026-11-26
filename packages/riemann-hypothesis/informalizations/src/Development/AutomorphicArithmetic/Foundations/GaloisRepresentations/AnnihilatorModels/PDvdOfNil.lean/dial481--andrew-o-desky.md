---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/AnnihilatorModels/PDvdOfNil.lean",
  "declarations": [
    "UpperTheory.Gal.crystallineComparison.dvdOfNil_of"
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

## Characteristic polynomial from a nilpotent polynomial value

[Theorem ALG.1398](https://andrewodesky.com/rh/lean/UpperTheory.Gal.crystallineComparison.dvdOfNil_of/)

Let $K$ be an algebraically closed field, $W$ a finite-dimensional $K$-vector space, $M\in\operatorname{End}_K(W)$, $S$ a finite multiset in $K$, and $u\in K^\times$. Put $$P_S(T)=\prod_{s\in S}(T-s).$$ If $uP_S(M)$ is nilpotent, then for some integer $m\ge0$, $$\det(T-M)\mid P_S(T)^m\quad\text{in }K[T].$$
