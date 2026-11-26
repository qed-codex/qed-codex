---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/IntegrableConvolution/UnitsTrace.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.L1.unitsTrace"
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

## A trace identity for cyclically permuted matrix algebra actions

[Theorem ALG.0833](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.L1.unitsTrace/)

Let $W$ be a finite-dimensional complex vector space, and let $m,d\ge0$. Suppose $$r_i:M_d(\mathbb C)\longrightarrow\operatorname{End}_{\mathbb C}(W)\qquad(i\in\mathbb Z/(m+1)\mathbb Z)$$ are unital complex algebra homomorphisms with commuting images for distinct $i$. Assume that the only subspaces stable under every $r_i(a)$ are $0$ and $W$. Let $U\in\operatorname{GL}_{\mathbb C}(W)$ satisfy $$U r_{i+1}(a)=r_i(a)U\qquad(i\in\mathbb Z/(m+1)\mathbb Z,\ a\in M_d(\mathbb C)).$$ There is $c\in\mathbb C^\times$ such that for every index $i_0$ and every $S\in\operatorname{End}_{\mathbb C}(W)$ commuting with all $r_j(a)$ for $j\ne i_0$, $$\operatorname{tr}(SU)=c\,\operatorname{tr}(S).$$
