---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArithmeticIntersection/LengthCokerEqKerAddDimOneOrderSum.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.AI.dimOneFormula"
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

## A one-dimensional local length formula

[Theorem ALG.0197](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.AI.dimOneFormula/)

Let $A$ be a one-dimensional commutative Noetherian local ring, $M$ a finite $A$-module, and $x\in A$. If $M/xM$ has finite length, then $\ker(x:M\to M)$ has finite length and $$\ell_A(M/xM)=\ell_A\ker(x:M\to M)+\sum_{\substack{\mathfrak p\in\operatorname{Spec}A\\ \dim(A/\mathfrak p)=1}}\ell_{A_{\mathfrak p}}(M_{\mathfrak p})\,o_{\mathfrak p}(x).$$
