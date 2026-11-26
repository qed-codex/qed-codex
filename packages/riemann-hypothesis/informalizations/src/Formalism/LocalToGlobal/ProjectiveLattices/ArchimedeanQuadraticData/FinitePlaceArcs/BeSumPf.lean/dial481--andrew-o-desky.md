---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/FinitePlaceArcs/BeSumPf.lean",
  "declarations": [
    "Formalism.L2.Pj.QAt.beSum_holds"
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

## A logarithmic bound for discriminant and integer prime costs

[Theorem ARAK.0471](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.QAt.beSum_holds/)

Let $E,K$ be number fields, let $n\ge1$ and $A\ge0$ be integers, and put $D=|\operatorname{disc}E|$. For each nonzero prime $\mathfrak p\subset\mathcal O_K$, define $$b_{\mathfrak p}=A\max\{v_{\mathfrak p}((D)),v_{\mathfrak p}((n))\},$$ where the valuations are the exponents in the factorizations of the indicated principal ideals of $\mathcal O_K$. Only finitely many $b_{\mathfrak p}$ are nonzero, and $$\frac1{[K:\mathbb Q]}\sum_{\mathfrak p}b_{\mathfrak p}\log N\mathfrak p\le A(\log D+\log n).$$
