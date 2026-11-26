---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/CuspidalSupport/SatArith.lean",
  "declarations": [
    "UpperTheory.V.Cj.S.satArith"
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

## Recovering a scaled union from normalized symmetric functions

[Theorem ALG.0347](https://andrewodesky.com/rh/lean/UpperTheory.V.Cj.S.satArith/)

Let $q\ge1$ and $r,s\ge0$ be integers. Let $B,B_1,B_2$ be multisets of nonzero complex numbers of cardinalities $r+s,r,s$ respectively. For a multiset $C$ put $$E_n(C,j)=q^{j(n-j)/2}e_j(C),$$ where $e_j$ is the elementary symmetric function, with $e_0=1$. Assume, for every $0\le j\le r+s$, $$\sum_{\substack{0\le a\le r,\ 0\le b\le s\\a+b=j}}q^{a(s-b)}E_r(B_1,a)E_s(B_2,b)=E_{r+s}(B,j).$$ Then, as multisets, $$B=q^{s/2}B_1\sqcup q^{-r/2}B_2.$$ The powers of the positive real number $q$ are their positive real values, viewed in $\mathbb C$; multiplying a multiset scales every element with multiplicity.
