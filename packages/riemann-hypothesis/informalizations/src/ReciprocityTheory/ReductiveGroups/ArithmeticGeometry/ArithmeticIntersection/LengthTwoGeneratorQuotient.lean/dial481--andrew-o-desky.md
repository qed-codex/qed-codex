---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArithmeticIntersection/LengthTwoGeneratorQuotient.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.AI.length_two_generator_quotient"
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

## Symmetry of local intersection lengths with a kernel correction

[Theorem AG.1474](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.AI.length_two_generator_quotient/)

Let $A$ be a two-dimensional Noetherian local domain and let $a,b\in A\setminus\{0\}$ satisfy $\ell_A(A/(a,b))<\infty$. Put $$K_a(b)=\ker(b:A/(a)\to A/(a)),$$ and, for a prime $\mathfrak p$, put $o_{\mathfrak p}(a)=\ell_{A_{\mathfrak p}}(A_{\mathfrak p}/aA_{\mathfrak p})$ and $o^{\mathfrak p}(b)=\ell_{A/\mathfrak p}((A/\mathfrak p)/b(A/\mathfrak p))$. Then $$\ell_A(A/(a,b))=\ell_A K_a(b)+\sum_{\substack{\operatorname{ht}\mathfrak p=1\\a\in\mathfrak p}}o_{\mathfrak p}(a)o^{\mathfrak p}(b),$$ $$\ell_A K_a(b)=\ell_A K_b(a)<\infty,$$ and the displayed prime sum equals the corresponding sum with $a,b$ exchanged. Lengths and sums are taken in $\mathbb N\cup\{\infty\}$; the sums are finitely supported sums, with value zero if the nonzero support is infinite.
