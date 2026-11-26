---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/DualWeylSchurEndomorphismStatement.lean",
  "declarations": [
    "GlobalTheory.T.dualWeyl_schur_endomorphism"
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

## A normalized commuting endomorphism of a dual Weyl module

[Theorem REP.1283](https://andrewodesky.com/rh/lean/GlobalTheory.T.dualWeyl_schur_endomorphism/)

Let $N\ge0$ be an integer and let $\nu=(\nu_1,\ldots,\nu_N)$ be a weakly decreasing list of nonnegative integers. Use the dual Weyl module $V_\nu=\nabla_\nu(\mathbb Q)$ and the highest-weight polynomial $v_\nu$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in square $N\times N$ variables $X_{ij}$.

For $1\le c,d\le N$, let $D_{cd}$ be the restriction to $V_\nu$ of the row derivation $$D_{cd}=\sum_{j=1}^{N}X_{cj}\frac{\partial}{\partial X_{dj}}.$$

Use $[f,g]_F=[f,g]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)) over $\mathbb Q$. If $S\in\operatorname{End}_{\mathbb Q}(V_\nu)$ commutes with every $D_{cd}$ and satisfies $[v_\nu,Sv_\nu]_F=[v_\nu,v_\nu]_F$, then $S=1$.
