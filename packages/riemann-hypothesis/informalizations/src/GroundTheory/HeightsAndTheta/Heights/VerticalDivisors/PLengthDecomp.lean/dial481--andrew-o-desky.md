---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/VerticalDivisors/PLengthDecomp.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Vertical.LengthDecomp.proof"
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

## Length decomposition in a finite algebra

[Theorem ALG.0322](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Vertical.LengthDecomp.proof/)

Let $R$ be a commutative Noetherian local ring, $B$ a commutative $R$-algebra finite as an $R$-module, and $b\in B$. If $\ell_R(B/bB)<\infty$, then $$\ell_R(B/bB)=\sum_{\mathfrak n\in\operatorname{Max}B}\ell_{B_{\mathfrak n}}(B_{\mathfrak n}/bB_{\mathfrak n})\,\ell_R(B/\mathfrak n).$$ Here $\ell$ denotes module length; the sum is the finitely supported sum over maximal ideals.
