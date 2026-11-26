---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/FrameLinearAlgebraFirst.lean",
  "declarations": [
    "Formalism.HN.frame_linear_algebra_first"
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

## Codimension bound from second moments

[Theorem ALG.0115](https://andrewodesky.com/rh/lean/Formalism.HN.frame_linear_algebra_first/)

Let $\mathcal I$ be a finite index set, let $V_i$ for $i\in\mathcal I$ be finite-dimensional complex Hilbert spaces, and let $H$ be another such space. Let $B_i:V_i\to H$, $c_i>0$. Put $d_i=\dim V_i$, $D=\dim H$, $R=\sum_i d_i>0$, and $Q=\sum_i c_iB_iB_i^*$. Suppose $0\le e\le1/4$, $\eta\ge0$, and $$\sum_i\|c_iB_i^*B_i-I\|_{\mathrm{HS}}^2\le eR,\qquad\operatorname{tr}(Q^2)\le(1+\eta)\frac{(\operatorname{tr}Q)^2}{D}.$$ For a real number $\varepsilon$ and subspaces $V'_i\subseteq V_i$ with $\sum_i(d_i-\dim V'_i)\le\varepsilon R$, $$\operatorname{codim}_H\sum_iB_i(V'_i)\le(\eta+4\varepsilon+4\sqrt e)D.$$ Here $I$ denotes the identity on each source. The Hilbert–Schmidt norm is $\|T\|_{\mathrm{HS}}^2=\operatorname{tr}(T^*T)$. Division by zero, if $D=0$, is assigned the value zero; the conclusion then reads $0\le0$.
