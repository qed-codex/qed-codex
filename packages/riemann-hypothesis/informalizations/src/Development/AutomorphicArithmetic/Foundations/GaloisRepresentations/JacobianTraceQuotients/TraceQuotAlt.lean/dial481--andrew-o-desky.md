---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/JacobianTraceQuotients/TraceQuotAlt.lean",
  "declarations": [
    "UpperTheory.Gal.Join.traceQuot"
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

## Trace after a quotient with a locally nilpotent kernel

[Theorem ALG.0244](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Join.traceQuot/)

Let $V,W$ be complex vector spaces and $S\subseteq V$ a finite-dimensional subspace. Let $B:V\to V$, $p:V\to W$, and $T:W\to W$ be complex-linear maps. Suppose $$B(V)\subseteq S,\qquad p(Bv)=T(pv)\quad(v\in S),$$ and, for every $v\in S\cap\ker p$, there is an integer $m\ge0$ such that $B^m v=0$. Then $B$ has finite rank, $T$ preserves $p(S)$, and $$\operatorname{tr}(B|_{\operatorname{im}B})=\operatorname{tr}(T|_{p(S)}).$$
