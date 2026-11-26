---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/LoeZeroOfPsd.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.PBL.loe_convex"
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

## A positive semidefinite bound for a Gram matrix of sums

[Theorem ALG.0841](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.PBL.loe_convex/)

Let $H$ be a complex inner-product space, $A$ any set, $Y\subseteq A$ finite, and $I$ a finite set. Choose $\lambda_i\in\mathbb C$ and functions $h_i:A\to H$. For $h:A\to H$, define its Gram matrix on $Y$ by $$G_h(P,Q)=\langle h(Q),h(P)\rangle\qquad(P,Q\in Y),$$ with the inner product conjugate-linear in the first argument. Then $$G_{\sum_i\lambda_i h_i}\ \preceq\ \left(\sum_i|\lambda_i|\right)\sum_i|\lambda_i|G_{h_i},$$ where $A\preceq B$ means that $B-A$ is positive semidefinite.
