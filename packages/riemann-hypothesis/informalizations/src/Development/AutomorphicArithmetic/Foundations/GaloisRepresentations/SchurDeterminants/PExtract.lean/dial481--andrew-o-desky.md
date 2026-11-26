---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SchurDeterminants/PExtract.lean",
  "declarations": [
    "UpperTheory.Gal.Schur.extract"
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

## Finite linear interpolation of distinct monomials on a dense set

[Theorem ALG.0470](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Schur.extract/)

Let $K$ be a field, let $S,M$ be finite sets, let $A$ be a set, and let $x:A\to K^S$. Assume that a polynomial over $K$ vanishing at every $x(a)$ is the zero polynomial. Let $e:M\to\mathbb N^S$ be injective and let $w_m\in K$ be prescribed. There is a finitely supported family $(c_a)_{a\in A}$ in $K$ such that $$\sum_{a\in A}c_a\prod_{s\in S}x(a)_s^{e(m)_s}=w_m\qquad(m\in M).$$
