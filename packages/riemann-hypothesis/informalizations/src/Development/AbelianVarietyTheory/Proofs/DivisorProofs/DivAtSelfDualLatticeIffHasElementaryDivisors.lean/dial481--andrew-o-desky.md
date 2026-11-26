---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/DivAtSelfDualLatticeIffHasElementaryDivisors.lean",
  "declarations": [
    "GlobalTheory.DivTransfer.hasDiv_iff"
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

## Elementary-divisor decompositions do not depend on the uniformizer

[Theorem ALG.0913](https://andrewodesky.com/rh/lean/GlobalTheory.DivTransfer.hasDiv_iff/)

Let $E$ be a number field, $\mathfrak p$ a nonzero prime of $\mathcal O_E$, $K=E_{\mathfrak p}$, and $O$ its valuation ring. Fix a uniformizer $\varpi\in K$ with normalized valuation $v(\varpi)=1$, an integer $n\ge0$, and a finite list $d=(d_0,\ldots,d_{m-1})$ of integers. Extend it by $d_i=0$ for $i\ge m$. For $g\in\operatorname{GL}_n(K)$, the following are equivalent:

- for some uniformizer $u$ with $v(u)=1$, there are $a,b\in\operatorname{GL}_n(O)$ with $g=a\operatorname{diag}(u^{d_i})b$;
- there are $a,b\in\operatorname{GL}_n(O)$ with $g=a\operatorname{diag}(\varpi^{d_i})b$.

No ordering or length condition on the list is required.
