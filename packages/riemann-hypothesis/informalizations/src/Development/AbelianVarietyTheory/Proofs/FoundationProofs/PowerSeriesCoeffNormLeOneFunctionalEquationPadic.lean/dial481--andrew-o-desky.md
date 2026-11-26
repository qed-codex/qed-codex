---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/PowerSeriesCoeffNormLeOneFunctionalEquationPadic.lean",
  "declarations": [
    "GlobalTheory.EvenTheta.FunEq.intSer_of_funEq"
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

## Integral coefficients from a power-series functional equation

[Theorem PHT.0598](https://andrewodesky.com/rh/lean/GlobalTheory.EvenTheta.FunEq.intSer_of_funEq/)

Let $K$ be an ultrametric normed field. Let $f,h,A,B\in K[[X]]$, and let $N$ be a nonnegative integer. Suppose $$f(0)=A(0)=B(0)=1,\qquad h(0)=0,\qquad |[X]h|=1,\qquad |N\cdot 1_K|<1.$$ Suppose every coefficient of $h,A,B$ has norm at most one and $$f(h(X))A(X)=f(X)^N B(X).$$ Then every coefficient of $f$ has norm at most one.
